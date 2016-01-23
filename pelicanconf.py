#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'xuhao'
SITENAME = u'Run For Life'
SITESUBTITLE = u'Random words in my brain'
SITEURL = ''

PATH = 'content'
#STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
STATIC_PATHS = ['images',]

TIMEZONE = 'Asia/Harbin'

DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
# MENUITEMS = [('Archives', '/archives.html'),]
# NEWEST_FIRST_ARCHIVES = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

PLUGIN_PATHS = ["../../www/pelican-plugins",]
PLUGINS = ["tag_cloud","neighbors"]

#THEME = 'themes/pelican-octopress-theme'
THEME = '../../www/voidy-bootstrap/'

CUSTOM_ARTICLE_FOOTERS = ("taglist.html",)
SIDEBAR = "sidebar.html"
SOCIAL = (('Google+', 'http://plus.google.com/userid',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/username',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin-url',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('BitBucket', 'http://bitbucket.org/username',
         'fa fa-bitbucket-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/username',
         'fa fa-github-square fa-fw fa-lg'),
        )
FAVICON = u'images/favicon.png'
SKIP_DEFAULT_CSS = True
STYLESHEET_URLS = ("//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css", "//cdn.bootcss.com/font-awesome/4.4.0/css/font-awesome.min.css",)
SKIP_DEFAULT_JS = True
JAVASCRIPT_URLS = ("//cdn.bootcss.com/jquery/1.11.3/jquery.min.js", "//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js",)

DISQUS_SITENAME = u'gotosk'

#SIDEBAR_IMAGE = u'images/linux-127x150.png'
#SIDEBAR_IMAGE_ALT = u'Hello!'
#SIDEBAR_IMAGE_WIDTH = 

#FAVICON_FILENAME = u'images/favicon.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
