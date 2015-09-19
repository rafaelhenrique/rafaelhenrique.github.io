#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rafael Henrique da Silva Correia'
AUTHOR_USERNAME = u'@rafaelhenrique'
AUTHOR_DESCRIPTION = (
    "Dev, geek, gamer, pythonista, e obviamente o "
    "criador deste log que vôs contempla neste momento."
)

SITENAME = u'Abra seu C\xf3digo!!!'
SITEURL = ''
SITEDESCRIPTION = 'Por um mundo livre e inteligente'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
DATE_FORMATS = {'pt': '%B %d, %Y', }

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_LINKS = (
    ('twitter', 'https://twitter.com/rafaelhenrique'),
    ('github', 'https://github.com/rafaelhenrique'),
    ('linkedin',
     'http://www.linkedin.com/pub/rafael-henrique-da-silva-correia/35/67a/5b3')
    #('rss', 'http://abraseucodigo.com.br/feeds/feeds.atom.xml'),
)

DEFAULT_PAGINATION = 10

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
SITEMAP_SAVE_AS = 'sitemap.xml'

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins',
    'custom-plugins'
]

PLUGINS = [
    'gravatar',
    'sitemap',
    'emoji',
    #'share_post',
    #'pelican_youtube',  # funciona somente com arquivos rst
    #'pelican_vimeo',  # funciona somente com arquivos rst
    'gzip_cache'  # deve ser o ultimo plugin
]

TAGLINE = 'Por um mundo livre e inteligente!!'
GITHUB_URL = 'https://github.com/rafaelhenrique/rafaelhenrique.github.io'
DISQUS_SITENAME = 'abraseucodigo'
GOOGLE_ANALYTICS = 'UA-66364849-1'

# Theme
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ['images', 'favicon.ico']

DIRECT_TEMPLATES = (
    'index', 'categories',
    'authors', 'archives',
    'sitemap', 'robots', 'humans')

ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
TYPOGRIFY = True
