#!/usr/bin/env python
"""
Script that takes a csv list and generates a file with http redirects.

Copyright 2016 David Duggins <dduggins@opentext.com>
This script is distributed under the terms of the GPLv3, as per the
LICENSE file in this repository.


The canonical version of this script can be found at: http://github.com/OpenText-DMG/redirects_framework.git
"""
import csv

def main():
    f = open('redirect_ca_fin.conf', 'w')
    with open('redirect_ca_fin.csv', 'rb') as csvfile:
         redirects = csv.DictReader(csvfile)
         for row in redirects:
            f.write("Redirect permanent " + row['page-url'] + " "  + row['redirect'] + "\n")
    


if __name__ == "__main__":
    main()