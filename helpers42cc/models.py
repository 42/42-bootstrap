# -*- coding: utf-8 -*-
from django.db import models
from .conf import *

INVALID_IMAGE_MESSAGE = (
    u'Image must be .jpg .png .tiff or .gif and less than 10 Mb. Try again.')

if IS_TESTING or HELP42CC_IS_DEMO:
    import urllib2
    import os

    from django.contrib.auth.models import User
    from django.core.files import File
    from django.core.files.temp import NamedTemporaryFile
    from django.db.models.signals import post_save
    from .validators import validate_resizable
    from .utils import resize_image

    class Profile(models.Model):
        """Contains user profile data"""
        user = models.OneToOneField(User, related_name='profile')
        userpic = models.ImageField(
            upload_to='userpics', blank=True, null=True,
            validators=[validate_resizable],
            error_messages={'invalid': INVALID_IMAGE_MESSAGE,
                    'invalid_image': INVALID_IMAGE_MESSAGE,
                    'missing': INVALID_IMAGE_MESSAGE,
                    'empty': INVALID_IMAGE_MESSAGE})

        def save(self, *args, **kwargs):
            super(Profile, self).save(*args, **kwargs)
            if self.userpic:
                resize_image(self.userpic, (100, 100))

        def load_userpic_from_url(self, userpic_url, userpic_file_name):
# http://stackoverflow.com/questions/1393202/django-add-image-in-an-imagefield-from-image-url
            img_temp = NamedTemporaryFile(delete=True)
            image = urllib2.urlopen(userpic_url)
            ext = os.path.splitext(image.geturl())[1]
            img_temp.write(image.read())
            img_temp.flush()
            self.userpic.save(userpic_file_name + ext, File(img_temp))

        @models.permalink
        def get_absolute_url(self):
            return ('helpers42cc.views.profile', [str(self.user.username)])

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)