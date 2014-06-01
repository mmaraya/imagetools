#!/usr/bin/env python

"""exifrename.py: Rename a JPEG to the date and time the image was taken in YYYYMMDDHHMMSSxx.jpg format"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import exifread, glob, os.path, sys, time

for pattern in (sys.argv[1:]):
    for old_filename in glob.glob(pattern):
        f = open(old_filename, 'rb')
        dir = os.path.dirname(os.path.abspath(old_filename)) + os.sep
        tags = exifread.process_file(f, details=False)
        exif_date = tags['EXIF DateTimeOriginal']
        file_date = time.strptime(str(exif_date), "%Y:%m:%d %H:%M:%S")
        counter = 0
        new_filename = dir + time.strftime('%Y%m%d%H%M%S', file_date) + str(counter).zfill(3) + '.jpg'
        while os.path.isfile(new_filename):
            counter += 1
            new_filename = dir + time.strftime('%Y%m%d%H%M%S', file_date) + str(counter).zfill(3) + '.jpg'
        os.rename(os.path.abspath(old_filename), os.path.abspath(new_filename))
        print 'Renamed %s to %s' % (old_filename, new_filename)
        f.close()
