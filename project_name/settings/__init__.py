import logging
import os
from distutils.util import strtobool

from default import *
from admins import *
from databases import *
from static import *
from media import *
from middleware import *
from template import *
from apps import *
from cache import *
from debug_toolbar_settings import *
from logging import *
from tests import *

try:
    from local import *
except:
    print '***{{ project_name }}/settins/local.py not found***'


IS_TESTING = strtobool(os.environ.get("TESTING", "no"))