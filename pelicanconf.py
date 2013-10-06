#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'moogoo'
SITENAME = u"Suhen's blog"
#SITEURL = 'http://blog.suhen.org'
SITEURL = ''

TIMEZONE = 'Asia/Taipei'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_LANG = u'zh'

DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = '{category}/{slug}.html'
#ARTICLE_URL = '{date:%Y-%m-%d}_{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
#ARTICLE_SAVE_AS = '{date:%Y-%m-%d}_{slug}.html'

THEME = 'themes/reallynotmyidea'
SUMMARY_MAX_LENGTH = 50
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
LINKS =  (
    ('About', SITEURL +'/pages/about.html'),
    ('Language', 'http://language.suhen.org'),
    ('Natural', 'http://natural.suhen.org'),
    (u'舊blog', 'http://blog.roodo.com/moogoo'),
    (u'電腦程式blog', 'http://moogoo78.blogspot.com'))

# Social widget
SOCIAL = (('facebook', 'http://www.facebook.com/moogee.lee'),
          ('twitter', 'http://twitter.com/moogoo'),
          ('github', 'http://github.com/moogoo78'))
          

DEFAULT_PAGINATION = 10


STATIC_PATHS = ["images", ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}
