#!/usr/bin/env python

"""exifrename.py: Rename a JPEG to the date and time the image was taken in YYYYMMDDHHMMSSmss.jpg format"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import glob
import os.path
import sys
import time

import exifread


for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        file = open(filename, 'rb')
        tags = exifread.process_file(file, details=False)
        # get EXIF date or use file date
        file_date = time.localtime(os.path.getmtime(filename))
        if tags.has_key('EXIF DateTimeOriginal'):
            exif_date = tags['EXIF DateTimeOriginal']
            file_date = time.strptime(str(exif_date), '%Y:%m:%d %H:%M:%S')
        # get EXIF sub-second time or use 000
        counter = 0
        if tags.has_key('EXIF SubSecTime'):
            counter = int(str(tags['EXIF SubSecTime']))
        # rename file
        dir = os.path.dirname(os.path.abspath(filename)) + os.sep
        new_filename = dir + time.strftime('%Y%m%d%H%M%S', file_date) + str(counter).zfill(3) + '.jpg'
        # increase millisecond counter if filename already exists
        while os.path.isfile(new_filename):
            counter += 1
            new_filename = dir + time.strftime('%Y%m%d%H%M%S', file_date) + str(counter).zfill(3) + '.jpg'
        os.rename(os.path.abspath(filename), os.path.abspath(new_filename))
        print 'Renamed %s to %s' % (filename, new_filename)
        file.close()
