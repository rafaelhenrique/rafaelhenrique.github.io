#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rafael Henrique da Silva Correia'
SITENAME = u'Abra seu C\xf3digo!!!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

USE_FOLDER_AS_CATEGORY = True

DEFAULT_METADATA = (
    (
        'About_author',
        'Desenvolvedor, Linuxista e Gamer'
    ),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ('Arquivo', 'archives.html'),
    ('Sobre', 'about.html'),
]

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/rafaelhenrique'),
    ('twitter', 'https://twitter.com/rafaelhenrique'),
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

#COVER_IMG_URL = 'http://lorempixel.com/g/200/500/animals/'
# COVER_IMG_URL = '/images/cover_img.png'
TAGLINE = 'Por um mundo livre e inteligente!!'
GITHUB_URL = 'https://github.com/rafaelhenrique/rafaelhenrique.github.io'
DISQUS_SITENAME = 'abraseucodigo'
GOOGLE_ANALYTICS = 'UA-66364849-1'

# Theme
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ['images']
