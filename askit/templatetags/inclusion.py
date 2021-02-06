from django import template
from askit.models import *

register = template.Library()

@register.inclusion_tag('askit/show_posts.html')
def show_posts(test):
    all_posts = Post.objects.all()
    return { 'all_posts': all_posts }

@register.inclusion_tag('askit/upvote_color.html', takes_context=True)
def upvote_color(context, user, post):
    user = context.request.user
    request = context['request']
    print(request.path)
    if Post_Upvote.objects.filter(post=post, author=user).exists():
        upvote = Post_Upvote.objects.get(post=post, author=user)
        print(post.author)
        return { 'user': user, 'upvote': upvote, 'post': post, 'request': request }
        
    else:

        print(post.author)
        return { 'user': user, 'post': post, 'request': request }

@register.inclusion_tag('askit/answers_upvote.html')
def answers_upvote(user, post):
    if Post_Upvote.objects.filter(post=post, author=user).exists():
        upvote = Post_Upvote.objects.get(post=post, author=user)
        return { 'user': user, 'upvote': upvote, 'post': post }
    else:
       return { 'user': user, 'post': post }

@register.simple_tag
def response_upvote(user, response_id):
        response = Response.objects.get(id=response_id)
        if Response_Upvote.objects.filter(author=user, response=response).exists():
            user_upvote = Response_Upvote.objects.get(author=user, response=response)
            return user_upvote

            
@register.simple_tag
def number_of_cookies(user):
    if User.objects.filter(username=user).exists():
        if Cookie.objects.filter(author=user).exists():
            cookie_user = Cookie.objects.get(author=user)
            return cookie_user

