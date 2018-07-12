from src import hello


def test_say_hello():
    test_name = "Pete"
    expected = "Hello, Pete!"
    assert hello.say_hello(test_name) == expected
