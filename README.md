django-templatetag-randomgen
============================

A collection of template tags that allow front-end developers easy access to [Python's random module](http://docs.python.org/library/random.html).

## Install

Add ``django-templatetag-randomgen`` to your ``INSTALLED_APPS``.

## Usage 

Load the templatetag at the top of a template file:

    {% load randomgen %}
    
To generate a random floating point number between 0 and 1:

    {% random %}                # e.g. 0.27684734152988466

To generate a random number between 100 and 1000:

    {% randrange 100 1000 %}    # e.g. 156
    
To generate a random floating point within a range:

    {% uniform 100 1000%}       # e.g. 241.05597162504844