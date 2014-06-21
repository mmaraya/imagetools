#!/usr/bin/env python

"""resize.py: Resize a JPEG to to the lowest resolution suitable for 8"x10" printing, preserving all EXIF information."""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import glob
import os
import sys

from PIL import Image




# maximum dimensions in pixels
hsize = 3008
vsize = 2000
for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        outfile = os.path.splitext(filename)[0] + '.resized.jpg'
        try:
            im = Image.open(filename)
        except IOError:
            print 'Could not read image properties for %s' % (filename)
        # check for image orientation
        if im.size[0] >= im.size[1]:
            size = (hsize, vsize)
        else:
            size = (vsize, hsize)
        # save information about the image before we change it
        old_size = im.size
        exif = im.info['exif']
        # resize if either horizontal or vertical exceeds our maximum dimensions
        if im.size[0] > size[0] or im.size[1] > size[1]:
            try:
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(filename, 'JPEG', exif=exif)
            except IOError:
                print 'Could not save resized image file %s' % (filename)
            print '%s resized from %dx%d to %dx%d' % (filename, old_size[0], old_size[1], im.size[0], im.size[1])
        else:
            print '%s is %dx%d not resized' % (filename, im.size[0], im.size[1])
