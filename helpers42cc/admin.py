# -*- coding: utf-8 -*-
from django.contrib import admin
from .conf import settings

if settings.IS_TESTING or settings.HELP42CC_IS_DEMO:
    from .models import Profile

    admin.site.register(Profile, admin.ModelAdmin)
