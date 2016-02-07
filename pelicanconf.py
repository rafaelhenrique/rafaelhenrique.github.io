#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


BASE = os.path.dirname(__file__)

# Author info

AUTHOR = u'Rafael Henrique da Silva Correia'
AUTHOR_EMAIL = u'rafael@abraseucodigo.com.br'
AUTHOR_USERNAME = u'@rafaelhenrique'
AUTHOR_DESCRIPTION = (
    "Developer #Python on @luizalabs! Gamer into World of Warcraft!"
)
DEFAULT_METADATA = (
    ('about_author',
        u"Developer #Python on @luizalabs! Gamer into World of Warcraft!"),
)

# Site info

SITENAME = u'Abra seu C\xf3digo!!!'
SITEURL = u'http://blog.abraseucodigo.com.br/'
SITEDESCRIPTION = u'Por um mundo livre e inteligente'
TAGLINE = u'Por um mundo livre e inteligente'

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
MENUITEMS = (
    ('Arquivo', 'archives.html'),
    ('Contato', 'pages/contato.html'),
    ('Sobre', 'pages/sobre.html'),
    ('Blog antigo', 'http://abraseucodigo.blogspot.com')
)

# Social links
LINKEDIN_PROFILE = (
    u'http://www.linkedin.com/pub/rafael-henrique-da-silva-correia/35/67a/5b3')

SOCIAL = (
    ('twitter', 'https://twitter.com/rafaelhenrique'),
    ('github', 'https://github.com/rafaelhenrique'),
    ('linkedin', LINKEDIN_PROFILE),
    ('rss', 'feeds/all.atom.xml'),
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
    'pelican_youtube',  # funciona somente com arquivos rst
    'pelican_vimeo',  # funciona somente com arquivos rst
    'json_articles',
    'emoji',
    'gzip_cache'  # deve ser o ultimo plugin
    # 'pdf', # funciona somente com arquivos rst
]

GITHUB_URL = 'https://github.com/rafaelhenrique/rafaelhenrique.github.io'
DISQUS_SITENAME = 'abraseucodigo'
GOOGLE_ANALYTICS = 'UA-66364849-1'

# Theme
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = [
    'images', 'extras/favicon.ico', 'extras/CNAME', 'extras/robots.txt']

EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

TEMPLATE_PAGES = {
    os.path.join(BASE, 'theme/templates/search.html'): (
        os.path.join(BASE, 'output/pages/search.html'))
}

RANDOM_ARTICLES = 10

COVER_IMG_URL = (u"http://i.imgur.com/SxhRd03.png")

# Geracao de PDF
# PDF_GENERATOR = True
