# -*- coding: utf-8 -*-
from django.contrib import admin
from .conf import *

if IS_TESTING or HELP42CC_IS_DEMO:
    from .models import Profile

    admin.site.register(Profile, admin.ModelAdmin)
