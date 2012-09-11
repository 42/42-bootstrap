# -*- coding: utf-8 -*-
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.template import Library

register = Library()

userpic_field = getattr(settings, 'HELP42CC_USERPIC_FIELD', 'userpic')
nopic_path = getattr(settings, 'HELP42CC_NOPIC_PATH', 'img/noavatar.png')


@register.inclusion_tag('helpers42cc/tags/userpic.html')
def userpic_for(user, geometry=None):
    if hasattr(user, 'profile'):
        havepic = (
            hasattr(user.profile, userpic_field) and
            getattr(user.profile, userpic_field)
        )
        if havepic:
            url = user.profile.userpic.url
            image = user.profile.userpic
        elif not hasattr(user.profile, userpic_field):
            raise AttributeError('User profile have no userpic field!')
    else:
        url = staticfiles_storage.url(nopic_path)
        image = None
    if geometry:
        w_h = geometry.split('x')
        width = w_h[0]
        if len(w_h) == 2:
            height = w_h[1]
        else:
            height = ''
    else:
        width = ''
        height = ''
    return dict(
        url=url,
        image=image,
        geometry=geometry,
        width=width,
        height=height,
    )