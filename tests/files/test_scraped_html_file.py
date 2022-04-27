from daos import ScrapedHtmlFile as File


def test_main():
    files = File.all()

    for file in files:
        print(file.path)

