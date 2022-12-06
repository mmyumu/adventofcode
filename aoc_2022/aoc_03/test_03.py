from aoc_2022.aoc_03.part_one import run as run1, run_dummy as run_dummy1


def test_part_one():
    result = run_dummy1()
    assert result == 157


    result = run1()
    assert result == 7990
