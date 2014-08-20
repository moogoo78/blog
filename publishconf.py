#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.suhen.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "suhenorg"
GOOGLE_ANALYTICS = "UA-38928548-1"

# for github pages
FILES_TO_COPY = (
('extra/CNAME', 'CNAME'),
)

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

GITHUB_URL = 'http://github.com/moogoo78'

RELATIVE_URLS = True
