from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

app_name = 'askit'

urlpatterns = [
path('askit', views.askit_home, name='askit_home'),
path('askit_login', views.askit_login, name='askit_login'),
path('askit_register', views.askit_register, name='askit_register'),
path('askit_logout', views.askit_logout, name='askit_logout'),
path('change_password', views.change_password, name='change_password'),
path('update_password', views.update_password, name='update_password'),
path('askit_login_page', views.askit_login_page, name='askit_login_page'),
path('askit_new_post', views.askit_new_post, name='askit_new_post'),
path('askit_post_save', views.askit_post_save, name='askit_post_save'),
path('askit/<int:post_id>/answers', views.answers, name='answers'),
path('askit/post_upvote/<int:post_id>', views.post_upvote, name='post_upvote'),
path('askit/<int:post_id>/response', views.response, name='response'),
path('askit/<int:response_id>/response_delete', views.response_delete, name='response_delete'),
path('askit/<int:post_id>/post_delete', views.post_delete, name='post_delete'),
path('askit/post_cookie/<int:post_id>', views.post_cookie, name='post_cookie'),
path('askit/response_cookie/<int:response_id>', views.response_cookie, name='response_cookie'),
path('askit/response_upvote/<int:post_id>/<int:response_id>,', views.response_upvote, name='response_upvote'),
]
