from abc import ABCMeta, ABC
from datetime import datetime

from peewee import (
    DateTimeField,
    BigIntegerField,
    TextField,
    BooleanField
)
from pony.orm import Required, Optional

from daos.abstracts.database import BaseDBModel


class BaseHtmlDocIndexModel(BaseDBModel):
    __metaclass__ = ABCMeta

    retrieved_from_web_at = Required(datetime)
    document_id = Required(int)
    document_format = Required(str)

    raw_version_document_path = Optional(str, nullable=True, sql_default='NULL')
    html_only_version_document_path = Optional(str, nullable=True, sql_default='NULL')
    no_js_version_document_path = Optional(str, nullable=True, sql_default='NULL')

    is_raw_version_stored = Required(bool, sql_default='false')
    is_html_only_version_stored = Required(bool, sql_default='false')
    is_no_js_version_stored = Required(bool, sql_default='false')

    url = Required(str)

    # retrieved_from_web_at = DateTimeField()
    # document_id = BigIntegerField()
    # document_format = TextField()
    #
    # raw_version_document_path = TextField()
    # html_only_version_document_path = TextField()
    # no_js_version_document_path = TextField()
    #
    # is_raw_version_stored = BooleanField()
    # is_html_only_version_stored = BooleanField()
    # is_no_js_version_stored = BooleanField()
    #
    # url = TextField()
