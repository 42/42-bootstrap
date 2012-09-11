# -*- coding: utf-8 -*-
from uuid import uuid1

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from sorl.thumbnail import get_thumbnail, delete

if settings.DEBUG:
    import traceback


def validate_resizable(image):
    """Check if image can't be resized with solr-thumbnail.
    Some resizing backend fail to resize specific images so check is needed

    """
    try:
        # if file is just uploaded then it's not saved. Save it to temp location
        data = image.file
        path = default_storage.save(
            'tmp/' + uuid1().hex, ContentFile(data.read()))
        temp_file = default_storage.open(path)
        get_thumbnail(temp_file, "100x100")
        temp_file.close()
        delete(temp_file)
    except Exception, msg:
        if settings.DEBUG:
            traceback.print_exc()
            raise ValidationError(u"Image is corrupted: %s" % msg)
        else:
            raise ValidationError(
                u"Image is corrupted and can't be resized by server.")