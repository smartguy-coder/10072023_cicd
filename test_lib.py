import library


def test_add_two():
    result = library.add_two(5, 5)
    assert result == 10


def test_add_str():
    result = library.add_two('5', '5')
    assert result == '55'
