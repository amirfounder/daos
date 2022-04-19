from __future__ import annotations
from enum import Enum


class BasePaths(Enum):
    NEWS_ARTICLE_BASE = 'C:/ai-ml-project/data/html/news-articles'


class Paths(Enum):
    NEWS_ARTICLE_HTML_ONLY_DIR_PATH = BasePaths.NEWS_ARTICLE_BASE.value + '/html-only'
    NEWS_ARTICLE_RAW_DIR_PATH = BasePaths.NEWS_ARTICLE_BASE.value + '/raw'
    NEWS_ARTICLE_NO_JS_DIR_PATH = BasePaths.NEWS_ARTICLE_BASE.value + '/no-js'
