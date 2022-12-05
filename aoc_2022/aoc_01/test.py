from aoc_2022.aoc_01.main import run


def test_both_parts():
    part_one_result, part_two_result = run()

    assert part_one_result == 65912
    assert part_two_result == 195625
