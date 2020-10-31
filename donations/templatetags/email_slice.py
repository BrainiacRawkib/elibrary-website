from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def format_email(value):
    # if len(value) > 5:
    #     return value[:5] + '****' + value[-3:]
    # else:
    return value[:3] + '****' + value[-3:]
