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
import sys

from PIL import Image


for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        try:
            im = Image.open(filename)
            print filename, im.format, "%dx%d" % im.size, im.mode
        except IOError:
            print 'Could not read image properties for %s' % (filename)
