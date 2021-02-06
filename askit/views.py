from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models.functions import Lower
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.paginator import Paginator



# Askit Home Page
def askit_home(request):
    
    query = request.GET.get('q')
    print(query)
    if query != None:
        query = query.strip()

    if 'sort' in request.GET:
        all_posts = Post.objects.all().order_by('-upvote_count')
        paginator = Paginator(all_posts, 5)
        page = request.GET.get('page')
        all_posts = paginator.get_page(page)
        print('sort')
        context = { 'all_posts': all_posts, 'most_popular': 'active' }
        return render(request, 'askit/index.html', context)

    if query != None and query == "":
        all_posts = None
        context = { 'all_posts': all_posts }
        print(all_posts)
        print('line 33')
        return render(request, 'askit/index.html', context)

    elif request.method =='GET' and 'q' in request.GET:
        query = request.GET.get('q')
        print(request.GET)
        print('line 40')
        
        if query is not None:   
            all_posts = Post.objects.filter(
                    Q(question__icontains=query) |
                    Q(body__icontains=query)
                ).order_by('-upvote_count')
            paginator = Paginator(all_posts, 5)
            page = request.GET.get('page')
            all_posts = paginator.get_page(page)
            context = { 'all_posts' : all_posts, 'latest_post': 'active', 'query': query }
            print('line 45')
            print(query)
            return render(request, 'askit/index.html', context)
    else:

        all_posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(all_posts, 5)
        page = request.GET.get('page')
        print(page)
        print('line 78')
        all_posts = paginator.get_page(page)
        context = { 'all_posts' : all_posts, 'latest_post': 'active' }
        print('line 63')
        return render(request, 'askit/index.html', context)




# Askit login page
def askit_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    print(username)
    print(password)
    if user is not None:
        print(request.GET)
        login(request, user)
        # request.session.set_expiry(300)
        if 'next' in request.GET:
            print('inside next')
            return HttpResponseRedirect(request.GET['next'])
        else:
            print('askit home page')
            return HttpResponseRedirect(reverse('askit:askit_home'))
        # return back to login page
    else:
        print('invalid login')
        return HttpResponseRedirect(reverse('askit:askit_login_page'))

def askit_login_page(request):
    context = { }
    return render(request, 'askit/askit_login_page.html', context)

# register new user    
def askit_register(request):
    if User.objects.filter(username=request.POST['username']).exists():
        print('user exists')
        return HttpResponseRedirect(reverse('askit:askit_home'))
    else:
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['username'], password=request.POST['password'])
        Cookie.objects.create(author=user, cookies = 10)
        print(request.POST['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('askit:askit_home'))

@login_required
# log user out
def askit_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('askit:askit_home'))

@login_required
# Change password page
def change_password(request):
    context = { }
    return render(request, 'askit/change_password.html', context)

# Update user's password
@login_required
def update_password(request):
    user = request.user


    if user.check_password(request.POST['current_password']) == False:
        return HttpResponseRedirect(reverse('askit:change_password'))

    elif request.POST['current_password'] == request.POST['new_password']:
        return HttpResponseRedirect(reverse('askit:change_password'))
    
    elif user.check_password(request.POST['current_password']) == True:
        user.set_password(request.POST['new_password'])
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('askit:askit_home'))
    

# New question page
@login_required
def askit_new_post(request):
    context ={ }
    return render(request, 'askit/askit_new_post.html', context)

# New user post
@login_required
def askit_post_save(request):
    post = Post.objects.create(question=request.POST["question"], body=request.POST["body"], author=request.user, upvote_count=1)
    Post_Upvote.objects.create(post=post, author=request.user)
    # request.session.set_expiry(10)
    return HttpResponseRedirect(reverse('askit:askit_home'))
    
@login_required
def response(request, post_id):
    post = Post.objects.get(id=post_id)
    body = request.POST['body']
    author = request.user
    response = Response.objects.create(post=post, body=body, author=author, upvote_count=1)
    Response_Upvote.objects.create(author=author, response=response)
    post.response_count += 1
    post.save()
    print('response created')
    return HttpResponseRedirect(request.GET['next'])

def answers(request, post_id):
    user_post = Post.objects.get(id=post_id)
    author = request.user
    if Response.objects.filter(post=user_post).exists():
        if request.user.is_authenticated:
            author_response = Response.objects.filter(post=user_post, author=author).order_by('-created_at')
            user_response = Response.objects.filter(post=user_post).order_by('-created_at')
            context = { 'user_post': user_post, 'user_response': user_response, 'author_response': author_response }
            return render(request, 'askit/answers.html', context)
            
        user_response = Response.objects.filter(post=user_post).order_by('-created_at')
        context = { 'user_post': user_post, 'user_response': user_response}
        return render(request, 'askit/answers.html', context)
    else:
        context = { 'user_post': user_post, }
        print('yes')
        return render(request, 'askit/answers.html', context) 

@login_required
def post_upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if Post_Upvote.objects.filter(post=post, author=user).exists():
        post.upvote_count -= 1
        post.save()
        print('minus 1')
        upvote = Post_Upvote.objects.get(post=post, author=user)
        upvote.delete()
        print('upvote instance deleted')
        print(request.GET)
    else:
        Post_Upvote.objects.create(post=post, author=user)
        post.upvote_count += 1
        post.save()
        print('new instance - plus 1')
        print(request.GET)
    next = request.GET.get('next')
    return HttpResponseRedirect(next)

@login_required
def response_upvote(request, post_id, response_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if Response.objects.filter(post=post).exists():
        response = Response.objects.get(post=post, id=response_id)
        if Response_Upvote.objects.filter(author=user, response=response).exists():
            response.upvote_count
            response.upvote_count -= 1
            response.save()
            print('minus 1')
            upvote = Response_Upvote.objects.get(author=user, response=response)
            upvote.delete()
            print('upvote instance deleted')
            print(request.GET)
        else:
            Response_Upvote.objects.create(author=user, response=response)
            response.upvote_count += 1
            response.save()
            print('new instance - plus 1')
            print(request.GET)
    next = request.GET.get('next')
    return HttpResponseRedirect(next)     

@login_required
def post_delete(request, post_id):

    Post.objects.get(id=post_id).delete()
    next = request.GET.get('next')
    return HttpResponseRedirect(next)
       
@login_required
def response_delete(request, response_id):
    
    response = Response.objects.get(id=response_id)
    post = response.post
    response.delete()

    post.response_count -= 1
    post.save()
    
    next = request.GET.get('next')
    return HttpResponseRedirect(next)



def post_cookie(request, post_id):
    cookie_give = Cookie.objects.get(author=request.user)
    post = Post.objects.get(id=post_id)

    if cookie_give.cookies >= 1 and cookie_give.author != post.author:
        cookie_give.cookies -= 1
        cookie_give.save()
        
        if post.cookie_count is not None:
            post.cookie_count += 1
            post.save()
        
        else:

            post.cookie_count = 1
            post.save()

        cookie_user = User.objects.get(username=post.author)
        
        if Cookie.objects.filter(author=cookie_user).exists():
            cookie_receive = Cookie.objects.get(author=cookie_user)
            cookie_receive.cookies += 1
            cookie_receive.save()

        else:
        
            Cookie.objects.create(author=cookie_user, cookies=0)
            cookie_receive = Cookie.objects.get(author=cookie_user)
            cookie_receive.cookies += 1
            cookie_receive.save()
    print('cookie next')
    next = request.GET.get('next')
    return HttpResponseRedirect(next)

def response_cookie(request, response_id):
    cookie_give = Cookie.objects.get(author=request.user)
    response = Response.objects.get(id=response_id)

    if cookie_give.cookies >= 1 and cookie_give.author != response.author:
        cookie_give.cookies -= 1
        cookie_give.save()
        
        if response.cookie_count is not None:
            response.cookie_count += 1
            response.save()
        
        else:

            response.cookie_count = 1
            response.save()

        cookie_user = User.objects.get(username=response.author)
        
        if Cookie.objects.filter(author=cookie_user).exists():
            cookie_receive = Cookie.objects.get(author=cookie_user)
            cookie_receive.cookies += 1
            cookie_receive.save()

        else:
        
            Cookie.objects.create(author=cookie_user, cookies=0)
            cookie_receive = Cookie.objects.get(author=cookie_user)
            cookie_receive.cookies += 1
            cookie_receive.save()

    next = request.GET.get('next')
    return HttpResponseRedirect(next) 
