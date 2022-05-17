from django import template

register = template.Library()


@register.filter
def before_dot(url: str):
    return url.split('.')[0].split('//')[1]


@register.filter
def after_dot(url: str):
    return url.split('.')[1]
