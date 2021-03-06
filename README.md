![image tools logo](icon.png "imagetools") Image Tools 
===========

This repository contains a collection of custom image manipulation utilities written in Python.

exifrename.py
-------------

This utility will rename JPEG files to the date and time the image was taken in YYYYMMDDHHMMSSMSS.jpg format.  This utility uses the Python Pillow fork of the Python Imaging Library (PIL).

resize.py
-------------

This utility will resize the supplied JPEG file to a size suitable for 8"x10" printing, preserving all EXIF information.    This utility uses the Python Pillow fork of the Python Imaging Library (PIL).

Supported Platforms
-------------------

These utilities run under all platforms supported by Python.

Dependencies
------------

These tools use [ExifRead](https://pypi.python.org/pypi/ExifRead). The easiest way to install this dependency is to install [PyPi](https://pypi.python.org/pypi) and run ```pip install exifread```


License
-------

Please see the file named LICENSE. 

Issues
------

Please submit questions, comments, bugs, enhancement requests at https://github.com/mmaraya/imagetools/issues.

Disclaimer
----------

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
