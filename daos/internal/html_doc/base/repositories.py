class Lol
    class NewsArticleHtmlDocumentIndexRepository(Repository[BaseNewsArticleHtmlDocumentIndexModel]):
        def __init__(self):
            super().__init__('postgresql://postgres:root@localhost:5432/postgres',
                             BaseNewsArticleHtmlDocumentIndexModel)