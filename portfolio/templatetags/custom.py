from django import template

register = template.Library()

@register.filter
def sub(list, id):
    return list.filter(project__id=id)
