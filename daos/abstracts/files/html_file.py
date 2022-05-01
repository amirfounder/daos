from bs4 import BeautifulSoup

from daos.abstracts.files.base import File


class HtmlFile(File):
    suffix = '.html'

    @File.contents.setter
    def contents(self, value):
        if isinstance(value, BeautifulSoup):
            value = str(value)
        File.contents.fset(self, value)

    def soup(self):
        return BeautifulSoup(self.contents, 'html.parser')
