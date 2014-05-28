#!/usr/bin/env python

"""exifrename.py: Rename a JPEG to the date and time the image was taken in YYYYMMDDHHMMSSxx.jpg format"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import exifread, glob, sys, time

for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        f = open(filename, 'rb')
        tags = exifread.process_file(f, details=False)
        exif_date = tags['EXIF DateTimeOriginal']
        file_date = time.strptime(str(exif_date), "%Y:%m:%d %H:%M:%S")
        new_filename = time.strftime('%Y%m%d%H%M%S', file_date)
        print new_filename