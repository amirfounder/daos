from __future__ import annotations
from enum import Enum


def path(*args):
    return 'C:/{}/{}/{}/{}/{}'.format(*args)


# Base
PROJECT = 'C:/ai-ml-project'
DATA = '/data'

# Domains
NEWS_ARTICLES = '/news-articles'
GOOGLE_SEARCH_RESULTS = '/google-search-results'

# Formats
HTML = '/html'
PDF = '/pdf'

# Categories
HTML_ONLY = '/html-only'
RAW_HTML = '/raw-html'
NO_JS = '/no-js'


class GoogleSearchResults(Enum):
    NO_JS = path(PROJECT, DATA, GOOGLE_SEARCH_RESULTS, HTML, NO_JS)

    HTML_ONLY = path(PROJECT, DATA, GOOGLE_SEARCH_RESULTS, HTML, HTML_ONLY)
    RAW_HTML = path(PROJECT, DATA, GOOGLE_SEARCH_RESULTS, HTML, RAW_HTML)

    HTML_ONLY_PDF = path(PROJECT, DATA, GOOGLE_SEARCH_RESULTS, PDF, HTML_ONLY)
    RAW_HTML_PDF = path(PROJECT, DATA, GOOGLE_SEARCH_RESULTS, PDF, RAW_HTML)


class NewsArticles(Enum):
    NO_JS = path(PROJECT, DATA, NEWS_ARTICLES, HTML, NO_JS)

    HTML_ONLY = path(PROJECT, DATA, NEWS_ARTICLES, HTML, HTML_ONLY)
    RAW_HTML = path(PROJECT, DATA, NEWS_ARTICLES, HTML, RAW_HTML)

    HTML_ONLY_PDF = path(PROJECT, DATA, NEWS_ARTICLES, PDF, HTML_ONLY)
    RAW_HTML_PDF = path(PROJECT, DATA, NEWS_ARTICLES, PDF, RAW_HTML)
