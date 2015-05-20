#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'moogoo'
SITENAME = u'suhen suchen | 酥賢尋找'
SITEURL = 'http:\\blog.suhen.org'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


ARTICLE_URL = '{category}/{slug}.html'
#ARTICLE_URL = '{date:%Y-%m-%d}_{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
#ARTICLE_SAVE_AS = '{date:%Y-%m-%d}_{slug}.html'
#THEME = 'themes/reallynotmyidea'
THEME = 'themes/space2001'

# Blogroll
LINKS = (
('About', SITEURL +'/pages/about.html'),
#('Language', 'http://language.suhen.org'),
#('Natural', 'http://natural.suhen.org'),
(u'舊blog', 'http://blog.roodo.com/moogoo'),
(u'電腦程式blog', 'http://moogoo78.blogspot.com'))
# Social widget
SOCIAL = (('facebook', 'http://www.facebook.com/moogee.lee'),
('twitter', 'http://twitter.com/moogoo'),
('github', 'http://github.com/moogoo78'))

DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images", 'extra/CNAME']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGINS = [
    'pelican_youtube',
]


DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE_FORMATS = '%Y.%M.%d'

# ref: http://docs.getpelican.com/en/latest/settings.html#basic-settings
