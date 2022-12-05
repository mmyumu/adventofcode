from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_03.common import PrioritiesComputer


class RucksackPrioritiesComputer(PrioritiesComputer):
    """
    Compute the priorities of items in both compartments of a rucksack
    """
    def _get_items(self, line):
        half_index = int(len(line) / 2)
        half1 = line[:half_index]
        half2 = line[half_index:]

        item_in_both_compartment = []
        for item1 in half1:
            for item2 in half2:
                if item1 == item2:
                    item_in_both_compartment.append(item1)

        item_in_both_compartment = set(item_in_both_compartment)

        return item_in_both_compartment


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = RucksackPrioritiesComputer()

    priorities_sum = 0
    for line in lines:
        priorities_sum += computer.compute(line)

    logger.info(f"Sum of priorities: {priorities_sum}")


if __name__ == "__main__":
    dummy_lines = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    executor = DummyExecutor(dummy_lines)
    executor.execute(treat_lines)

    executor = FileExecutor('aoc_2022/aoc_03/input.txt')
    executor.execute(treat_lines)
