#!/usr/bin/env python

"""exifgps.py: Set EXIF location with GPS coordinates"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2015, Mike Maraya'
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
        print('%s' % (filename)) 
        # check for existing geolocation information
        has_gps = False
        if tags.has_key('GPS GPSLatitude'):
            has_gps = True
            latitude = tags['GPS GPSLatitude']
            latitude_ref = tags['GPS GPSLatitudeRef']
            print('\tlatitude: %s %s' % (latitude, latitude_ref))
        if tags.has_key('GPS GPSLongitude'):
            has_gps = True
            longitude = tags['GPS GPSLongitude'] 
            longitude_ref = tags['GPS GPSLongitudeRef']
            print('\tlongitude: %s %s' % (longitude, longitude_ref))
        if tags.has_key('GPS GPSAltitude'):    
            has_gps = True
            altitude = tags['GPS GPSAltitude']
            altitude_ref = tags['GPS GPSAltitudeRef']
            print('\taltitude: %s %s' % (altitude, altitude_ref)) 
        if has_gps == False:     
            print('\tno GPS information')
        file.close()
