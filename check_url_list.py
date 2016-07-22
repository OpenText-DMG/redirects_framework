#!/usr/bin/env python
"""
Script to check a list of URLs Response Code 

Copyright 2016 David Duggins <dduggins@opentext.com>
This script is distributed under the terms of the GPLv3, as per the
LICENSE file in this repository.

The canonical version of this script can be found at: <http://github.com/OpenText-DMG/redirects_framework.git>
"""

import sys
import urllib2

def get_url_nofollow(url):
    try:
        response = urllib2.urlopen(url)
        code = response.getcode()
        return code
    except urllib2.HTTPError as e:
        return e.code
    except:
        return 0

def main():
  
if __name__ == "__main__":
main()