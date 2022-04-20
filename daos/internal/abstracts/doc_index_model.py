from abc import ABC

from peewee import (
    DateTimeField,
    BigIntegerField,
    TextField,
    BooleanField
)

from daos.abstracts.database import BaseDBModel


class BaseHtmlDocIndexModel(BaseDBModel, ABC):
    retrieved_from_web_at = DateTimeField()
    document_id = BigIntegerField()
    document_format = TextField()

    raw_version_document_path = TextField()
    html_only_version_document_path = TextField()
    no_js_version_document_path = TextField()

    is_raw_version_stored = BooleanField()
    is_html_only_version_stored = BooleanField()
    is_no_js_version_stored = BooleanField()

    url = TextField()
