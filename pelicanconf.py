#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'G'
SITENAME = 'G not C.'
SITESUBTITLE = 'It\'s G, not C.'
SITEURL = 'http://gnotc.com'

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = '/Volumes/EXT/Projects/gnotc.com/theme'
STATIC_PATHS = ['images']
PLUGIN_PATHS = ['/Volumes/EXT/Projects/pelican-plugins']
PLUGINS = ['neighbors']
ARTICLE_URL = 'entry/{slug}' #remove html before live
ARTICLE_SAVE_AS = 'entry/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_PATHS = ['pages']
DIRECT_TEMPLATES = ["index","about","archives","no-comment","kc"]

