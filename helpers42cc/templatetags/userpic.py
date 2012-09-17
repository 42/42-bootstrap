# -*- coding: utf-8 -*-
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.template import Library

register = Library()

userpic_field = getattr(settings, 'HELP42CC_USERPIC_FIELD', 'userpic')
nopic_path = getattr(settings, 'HELP42CC_NOPIC_PATH', 'img/noavatar.png')


# TODO: create tests for this
@register.inclusion_tag('helpers42cc/tags/userpic.html')
def userpic_for(user, geometry=None):
    profile = user.get_profile()
    if hasattr(user, 'profile'):
        havepic = (
            hasattr(profile, userpic_field) and
            getattr(profile, userpic_field)
        )
        if havepic:
            url = havepic.url
            image = havepic
        elif not hasattr(profile, userpic_field):
            raise AttributeError('User profile have no userpic field!')
        else:
            url = None
            image = None
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