from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_groups')
def has_groups(user, groups_names):
    return user.groups.filter(name__in=groups_names.split("|")).exists()

@register.filter(name='in_group')
def in_group(user):
    group = Group.objects.get(id=user.idGroup)
    return group.name