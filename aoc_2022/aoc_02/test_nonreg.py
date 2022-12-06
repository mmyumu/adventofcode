from aoc_2022.aoc_02.part_one import run as run1
from aoc_2022.aoc_02.part_two import run as run2


def test_part_one():
    result = run1()
    assert result == 10310


def test_part_two():
    result = run2()
    assert result == 14859