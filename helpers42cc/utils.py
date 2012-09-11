# -*- coding: utf-8 -*-
import logging

from PIL import Image


def need_resize(image, size):
    return image.width < size[0] and image.height < size[1]


def resize_image(image, size=(1920, 1200)):
    """Resize images to size if it bigger than size

    """
    image_need_resize = need_resize(image, size)
    try:
        filename = image.path
        image = Image.open(filename)

        if image_need_resize:
            image.thumbnail(size, Image.ANTIALIAS)

        image.save(filename)

    except IOError as e:
        logging.error("Error in resizing image: %s", e)
