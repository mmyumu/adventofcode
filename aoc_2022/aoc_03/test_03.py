from aoc_2022.aoc_03.part_one import run as run1, run_dummy as run_dummy1
from aoc_2022.aoc_03.part_two import run as run2, run_dummy as run_dummy2


def test_part_one():
    result = run_dummy1()
    assert result == 157


    result = run1()
    assert result == 7990


def test_part_two():
    result = run_dummy2()
    assert result == 70


    result = run2()
    assert result == 2602
