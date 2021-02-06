from django import template
from askit.models import *

register = template.Library()

@register.simple_tag
def cookies(user):
    cookie_count = Cookie.objects.get(author=user)
    return cookie_count