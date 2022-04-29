from sqlalchemy import Column, DateTime, String, Integer, ForeignKey

from daos.abstracts.database.base import Model

from .scraping_method import ScrapingMethod


# noinspection PyUnresolvedReferences
class ScrapedHtmlFileIndexEntry(Model):
    """
    Represents an HTML file scraped from a webpage

    Attributes:
        method_used: Method used = either
        scraped_at: Datetime the document was scraped from the web
        url: The URL of the webpage
        session_id: The id of the session which marks the first time this webpage was visited
        ms_elapsed_on_webpage: The total milliseconds spent on this page when this html "snapshot" was scraped
        dom_changes_observed: The amount of changes in the HTML file since the last entry
        file_path: the location of the file in the system
    """
    __tablename__ = 'scraped_html_file_index'

    method_used_id = Column(Integer, ForeignKey(ScrapingMethod.id))
    scraped_at = Column(DateTime(True))
    url = Column(String)
    session_id = Column(String)
    ms_elapsed_on_webpage = Column(Integer)
    dom_changes_observed = Column(Integer)
    file_path = Column(String)
