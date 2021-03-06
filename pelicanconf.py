#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'PeiM'
SITENAME = u'Boston Career'
SITEURL = 'https://scientist-tortoise-12030.netlify.com/'
SITETITLE = u'波士顿职场招聘信息'
SITESUBTITLE = 'Opportunities'
SITELOGO = None 

PATH = 'content'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


# Blogroll
#LINKS = (('TJUAA-Boston', 'http://#www.tjuboston.org/'),
#         ('You can modify those links in your config file', '#'),)

#LINKS = (('TJUAA-Boston', 'http://#www.tjuboston.org/'),)

LINKS = (('', ''),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
#THEME = "/Users/pei-macpro/Desktop/pelican-themes/Flex"
THEME = "theme"


