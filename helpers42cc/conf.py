# -*- coding: utf-8 -*-
from django.conf import settings

settings.IS_TESTING = getattr(settings, 'IS_TESTING', False)
settings.HELP42CC_IS_DEMO = getattr(settings, 'HELP42CC_IS_DEMO', False)