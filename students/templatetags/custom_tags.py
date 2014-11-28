from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template import Library

register = template.Library()


@register.simple_tag
def admin_edit(obj):
    url = reverse('admin:{}_{}_change'.format(obj._meta.app_label,
                                              obj._meta.module_name), args=[obj.id])
    return '<a href="{}">{}</a>'.format(url, obj.__unicode__())

    #format(obj._meta.app_label,obj._meta.module_name) - add standart(name my app, and name my module)

