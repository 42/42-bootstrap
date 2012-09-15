# -*- coding: utf-8 -*-
from django.conf import settings

IS_TESTING = getattr(settings, 'IS_TESTING', False)
HELP42CC_IS_DEMO = getattr(settings, 'HELP42CC_IS_DEMO', False)