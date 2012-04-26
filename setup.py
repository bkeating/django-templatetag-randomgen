#!/usr/bin/env python

import os
from distutils.core import setup

setup(name='django-templatetag-randomgen', 
      version='0.3', 
      description='Generate random numbers and hashes inside templates.', 
      author='Ben Keating, Jon Parrish', 
      author_email='oss+randomgen@deepdream.com', 
      url='http://github.com/bkeating/django-templatetag-randomgen', 
      packages=['randomgen', ], 
     )
