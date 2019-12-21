#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

AUTHOR = "Nick Vogt"
SITENAME = "Hi, I'm Nick"
SITEURL = os.getenv("SITEURL")
PATH = "content"
TIMEZONE = "America/Detroit"
DEFAULT_LANG = "en"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (("You can add links in your config file", "#"), ("Another social link", "#"))

# Social widget
SOCIAL = (
    ("github", "http://github.com/vogt4nick"),
    ("linkedin", "http://linkedin.com/nicholas-vogt/"),
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme-based globals
THEME = "themes/attila"
DISPLAY_PAGES_ON_MENU = True
SITESUBTITLE = "I like math, programming, and flannel."
SHOW_SITESUBTITLE_IN_HTML = True
HEADER_COVER = "theme/images/about-banner.jpg"
