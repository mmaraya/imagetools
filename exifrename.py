#!/usr/bin/env python

"""exifrename.py: Rename a JPEG to the date and time the image was taken in YYYYMMDDHHMMSS.jpg format"""

__author__ = 'Mike Maraya'
__copyright__ = 'Copyright (c) 2014, Mike Maraya'
__license__ = 'The MIT License (MIT)'
__version__ = '1.0'
__email__ = 'mike.maraya@gmail.com'
__status__ = 'Development'
__maintainer__ = 'Mike Maraya'

import glob, sys

for pattern in (sys.argv[1:]):
    for filename in glob.glob(pattern):
        print 'File:', filename

