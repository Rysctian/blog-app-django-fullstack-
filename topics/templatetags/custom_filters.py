# custom_filters.py
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import strip_tags

register = template.Library()

@register.filter(name='format_content')
@stringfilter
def format_content(value, exclude_wysiwyg=False, words_limit=50):
    if exclude_wysiwyg:
        return strip_tags(value)[:words_limit]
    return value
