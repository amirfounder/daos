from __future__ import annotations
from enum import Enum


def path(*args):
    return 'C:/{}/{}/{}/{}'.format(*args)


# Base
PROJECT = 'C:/ai-ml-project'
DATA = '/data'

# Formats
HTML = '/html'
PDF = '/pdf'

# Categories
HTML_ONLY = '/html-only'
RAW_HTML = '/raw-html'


class Paths(Enum):
    HTML_ONLY = path(PROJECT, DATA, HTML, HTML_ONLY)
    HTML_ONLY_PDF = path(PROJECT, DATA, PDF, HTML_ONLY)

    RAW_HTML = path(PROJECT, DATA, HTML, RAW_HTML)
    RAW_HTML_PDF = path(PROJECT, DATA, PDF, RAW_HTML)
