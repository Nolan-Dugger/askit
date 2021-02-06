from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class Post(models.Model):
    question = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote_count = models.IntegerField(blank=True, null=True)
    response_count = models.IntegerField(default=0)
    cookie_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question + " " + self.body + " " + str(self.author) + " " + str(self.upvote_count) + ' ' + str(self.response_count)

class Post_Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post) + " " + str(self.author)

class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    upvote_count = models.IntegerField()
    cookie_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.author) + " " + str(self.post) + " " + str(self.body) + " " + str(self.upvote_count)

class Response_Upvote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.author) + " " + str(self.response)

class Cookie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cookies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.author) + " " + str(self.cookies)