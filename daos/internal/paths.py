from __future__ import annotations
from enum import Enum


def path(*args):
    return 'C:/{}/{}/{}/{}'.format(*args)


# Base
BASE = 'C:/ai-ml-project/data'

# Formats
HTML = '/html'
PDF = '/pdf'
CSV = '/csv'

# Categories
HTML_ONLY = '/html-only'
RAW_HTML = '/raw-html'

# Sub-categories
HTML_ONLY_FEATURES = '/features' + HTML_ONLY


class Paths(Enum):
    html_only = BASE + HTML + HTML_ONLY
    raw_html = BASE + HTML + RAW_HTML

    html_only_pdfs = BASE + PDF + HTML_ONLY
    raw_html_pdfs = BASE + PDF + RAW_HTML

    html_only_features = BASE + CSV + HTML_ONLY_FEATURES
