from aoc_2022.aoc_04.part_one import run as run1, run_dummy as run_dummy1
from aoc_2022.aoc_04.part_two import run as run2, run_dummy as run_dummy2


def test_part_one():
    result = run_dummy1()
    assert result == 2


    result = run1()
    assert result == 538


def test_part_two():
    result = run_dummy2()
    assert result == 4


    result = run2()
    assert result == 792
