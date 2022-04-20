from __future__ import annotations
from enum import Enum


class BasePaths(Enum):
    NEWS_ARTICLE = 'C:/ai-ml-project/data/html/news-articles'
    GOOGLE_SEARCH_RESULTS = 'C:/ai-ml-project/data/html/google-search-results'


class Paths(Enum):
    NEWS_ARTICLE_HTML_ONLY_DIR_PATH = BasePaths.NEWS_ARTICLE.value + '/html-only'
    NEWS_ARTICLE_RAW_DIR_PATH = BasePaths.NEWS_ARTICLE.value + '/raw'
    NEWS_ARTICLE_NO_JS_DIR_PATH = BasePaths.NEWS_ARTICLE.value + '/no-js'
    
    GOOGLE_SEARCH_RESULTS_HTML_ONLY_DIR_PATH = BasePaths.GOOGLE_SEARCH_RESULTS.value + '/html-only'
    GOOGLE_SEARCH_RESULTS_RAW_DIR_PATH = BasePaths.GOOGLE_SEARCH_RESULTS.value + '/raw'
    GOOGLE_SEARCH_RESULTS_NO_JS_DIR_PATH = BasePaths.GOOGLE_SEARCH_RESULTS.value + '/no-js'
