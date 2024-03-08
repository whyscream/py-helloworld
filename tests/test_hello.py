from helloworld import hello


def test_hello_default():
    assert hello() == "Hello world!"


def test_hello_someone():
    assert hello("John") == "Hello John!"
