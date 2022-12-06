from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_03.common import PrioritiesComputer


class GroupPrioritiesComputer(PrioritiesComputer):
    """
    Compute the priorities of items in both compartments of a rucksack
    """
    def _get_items(self, lines_group):
        return self._get_same_items(lines_group)


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = GroupPrioritiesComputer()

    priorities_sum = 0
    for i, _ in enumerate(lines):
        if i % 3 == 0:
            priorities_sum += computer.compute(lines[i:i+3])
        

    logger.info(f"Sum of priorities: {priorities_sum}")

    return priorities_sum


def run():
    executor = FileExecutor('aoc_2022/aoc_03/input.txt')
    return executor.execute(treat_lines)


def run_dummy():
    dummy_lines = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    executor = DummyExecutor(dummy_lines)
    return executor.execute(treat_lines)

if __name__ == "__main__":
    run_dummy()
    run()
