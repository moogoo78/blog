#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

#SITEURL = 'http://suhen.org'
FEED_DOMAIN = SITEURL

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False
DISQUS_SITENAME = "blogsuhenorg"
GOOGLE_ANALYTICS = "UA-38928548-1"

# for github pages
FILES_TO_COPY = ( 
    ('extra/CNAME', 'CNAME'),
)
#GITHUB_URL = 'http://github.com/moogoo78'
