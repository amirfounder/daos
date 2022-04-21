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
PROCESSED_HTML_V1 = '/processed-html-v1'
RAW_HTML = '/raw-html'

# Sub-categories
PROCESSED_HTML_V1_FEATURES = '/features' + PROCESSED_HTML_V1


class Paths(Enum):
    processed_html_v1 = BASE + HTML + PROCESSED_HTML_V1
    raw_html = BASE + HTML + RAW_HTML

    processed_html_v1_pdfs = BASE + PDF + PROCESSED_HTML_V1
    raw_html_pdfs = BASE + PDF + RAW_HTML

    processed_html_v1_features = BASE + CSV + PROCESSED_HTML_V1_FEATURES
