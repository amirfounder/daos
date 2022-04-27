from os import makedirs
from os.path import isdir

from daos import ScrapedHtmlFile as File
from shutil import rmtree


TEST_DIRECTORY = 'C:/cleanup-purposes-only'
File.path = TEST_DIRECTORY


def cleanup(func):
    def wrapper(*args, **kwargs):
        if isdir(TEST_DIRECTORY):
            rmtree(TEST_DIRECTORY)
        makedirs(TEST_DIRECTORY)
        result = func(*args, **kwargs)
        if isdir(TEST_DIRECTORY):
            rmtree(TEST_DIRECTORY)
        return result
    return wrapper


@cleanup
def test_not_created_without_flush():
    File()

    files = File.all()

    assert len([x for x in files]) == 0

@cleanup
def test_create_from_init():
    file = File()
    file.flush()

    files = File.all()

    assert len([f for f in files]) == 1


@cleanup
def test_empty_list():
    files = File.all()
    assert len([x for x in files]) == 0


@cleanup
def test_one_item_in_list():
    files = File.all()


@cleanup
def test_multiple_creates():
    file = File()
    file.flush()
    file = File()
    file.flush()
    file = File()
    file.flush()
    file = File()
    file.flush()

    files = File.all()

    assert len([f for f in files]) == 4

@cleanup
def test_all_with_filter():
    file = File()
    file.flush()
    file = File()
    file.flush()
    file = File()
    file.flush()
    file = File()
    file.flush()

    files = File.all(path=TEST_DIRECTORY + '/1.html')
    assert len([x for x in files]) == 1
