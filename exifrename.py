#!/usr/bin/env python

"""exifrename.py: Rename a JPEG to the date and time the image was taken in YYYYMMDDHHMMSS.jpg format"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import exifread, glob, sys

for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        print 'File:', filename
        f = open(filename, 'rb')
        tags = exifread.process_file(f, details=False, stop_tag='EXIF DateTimeOriginal')
        date = tags['EXIF DateTimeOriginal']
        print 'Date %d', date


