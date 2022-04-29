from bs4 import BeautifulSoup

from daos.abstracts.files.base import File


class HtmlFile(File):
    suffix = '.html'

    def set_contents(self, contents: str | BeautifulSoup):
        if isinstance(contents, BeautifulSoup):
            contents = str(contents)
        super().set_contents(contents)

    def soup(self):
        return BeautifulSoup(self.contents, 'html.parser')
