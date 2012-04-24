django-templatetag-randomgen
============================

An easy way to generate random numbers and hashes inside template files.  
django-templatetag-randomgen is a simple front-end to Python's [hashlib](http://docs.python.org/library/hashlib.html) and [random](http://docs.python.org/library/random.html) modules.

## Install

1. Add ``randomgen`` to your ``INSTALLED_APPS`` 
2. Add ``{% load randomgen %}`` to the top of template files you wish to use these tags in.

## Usage
    
To generate a random floating point number between 0 and 1:

    {% randomgen %}                   # e.g. 0.27684734152988466
    
To generate a md5 hash:

    {% randomgen hash %}              # e.g. 522748524ad010358705b6852b81be4c

To generate a random number between 100 and 1000:

    {% randomgen 100 1000 %}          # e.g. 156
    
To generate a random floating point within a range:

    {% randomgen 100 1000 float %}    # e.g. 241.05597162504844
