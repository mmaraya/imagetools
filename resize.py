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
from stat import *

from PIL import Image


size = 3008, 2000
for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        outfile = os.path.splitext(filename)[0] + '.resized'
        try:
            im = Image.open(filename)
            print filename, '%dx%d' % im.size, os.stat(filename)[ST_SIZE]
        except IOError:
            print 'Could not read image properties for %s' % filename
        try:
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, 'JPEG')
        except IOError:
            print 'Could not save resized image file %s' % outfile

