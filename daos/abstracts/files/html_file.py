from bs4 import BeautifulSoup

from daos.abstracts.files.base import File


class HtmlFile(File):
    suffix = '.html'

    def soup(self):
        return BeautifulSoup(self.contents, 'html.parser')
