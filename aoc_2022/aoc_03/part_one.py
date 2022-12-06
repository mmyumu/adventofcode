from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_03.common import DUMMY_LINES, PrioritiesComputer


class RucksackPrioritiesComputer(PrioritiesComputer):
    """
    Compute the priorities of items in both compartments of a rucksack
    """
    def _get_items(self, line):
        half_index = int(len(line) / 2)
        half1 = line[:half_index]
        half2 = line[half_index:]

        return self._get_same_items([half1, half2])


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

    return priorities_sum


def run():
    executor = FileExecutor('aoc_2022/aoc_03/input.txt')
    return executor.execute(treat_lines)


def run_dummy():
    executor = DummyExecutor(DUMMY_LINES)
    return executor.execute(treat_lines)


if __name__ == "__main__":
    run()