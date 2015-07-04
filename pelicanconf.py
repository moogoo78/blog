#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'moogoo'
SITENAME = u'suhen suchen'
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
THEME = 'themes/alchemy'



TAGS_ON_MENU = True
CATEGORIES_ON_MENU = True
ARCHIVES_ON_MENU = True
SITE_SUBTEXT = '酥賢尋找'
FB_ADDRESS = 'https://www.facebook.com/moogoo.lee'
EMAIL_ADDRESS = 'moogoo78@gmail.com'
PROFILE_IMAGE = 'https://lh3.googleusercontent.com/-9wxO5a0JILg/AAAAAAAAAAI/AAAAAAAABmU/BRrqv19ka5I/s120-c/photo.jpg'
## setting
DATE_FORMATS = {
    'zh': ('zh_TW.UTF-8','%Y-%m-%d %H:%M'),
}
LOCALE = ('zh_TW.UTF-8')


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


# ref: http://docs.getpelican.com/en/latest/settings.html#basic-settings
