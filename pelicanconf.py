#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'moogoo'
SITENAME = u'賤透走人 . Gentle Runner'
SITEURL = 'http://gentlerunner.org'

TIMEZONE = 'Asia/Taipei'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_LANG = u'zh'

DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = '{category}/{slug}.html'
#ARTICLE_URL = '{date:%Y-%m-%d}_{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
#ARTICLE_SAVE_AS = '{date:%Y-%m-%d}_{slug}.html'

#THEME = 'themes/pelican-foundation'
THEME = 'reallynotmyidea'

DELETE_OUTPUT_DIRECTORY = True

## ??
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('facebook', 'http://www.facebook.com/farseerfc'),
          ('twitter', 'http://twitter.com/moogoo'),
          ('github', 'http://github.com/moogoo78'))
          

DEFAULT_PAGINATION = 10


STATIC_PATHS = ["images", ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}
