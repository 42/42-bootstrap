# -*- coding: utf-8 -*-
from annoying.decorators import render_to

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@render_to('helpers42cc/profile.html')
def profile(request, username, extra_context=None):
    user = get_object_or_404(User, username=username)

    return dict(target_user=user)