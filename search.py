import pytest
import time

def linear_search(list, value):
    for i, item in enumerate(list):
        if value == item:
            return i
    return -1


def binary_search(list, value, start=0, end=None):
    if end is None:
        end = len(list)

    window = end - start
    half_pos = start + window // 2

    if window <= 1 and list[half_pos] != value:
        return -1

    if list[half_pos] == value:
        return half_pos

    if list[half_pos] > value:
        return binary_search(list, value, start, half_pos)

    return binary_search(list, value, half_pos, end)


algorithms = [
    binary_search,
    linear_search
]


@pytest.mark.parametrize("search", algorithms)
def test_search(search: callable):
    list = [9, 18, 19, 20, 29, 42, 56, 61, 88, 95]

    start = time.time_ns()
    assert search(list, -5) == -1
    assert search(list, 100) == -1
    assert search(list, 30) == -1
    assert search(list, 18) == 1
    assert search(list, 42) == 5
    assert search(list, 61) == 7
    end = time.time_ns()

    print(f'{search.__name__} finished in {end - start} ns on the short list')

    longlist = range(1, 10000)

    start = time.time_ns()
    assert search(longlist, -5) == -1
    assert search(longlist, 10001) == -1
    assert search(longlist, 18) == 17
    assert search(longlist, 42) == 41
    assert search(longlist, 61) == 60
    end = time.time_ns()

    print(f'{search.__name__} finished in {end - start} ns on the long list')