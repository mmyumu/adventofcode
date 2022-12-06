from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_04.common import RedundantPairComputer


class FullyRedundantPairComputer(RedundantPairComputer):
    """
    Check whether the pair is fully redundant

    Args:
        RedundantPairComputer: Abstract redundant pair computer
    """
    def _compute_redundant(self, set1, set2):
        return set1.issubset(set2) or set2.issubset(set1)


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = FullyRedundantPairComputer()

    priorities_sum = 0
    for line in lines:
        ranges = line.split(",")
        priorities_sum += computer.compute(ranges[0], ranges[1])

    logger.info(f"Number of redundant pairs: {priorities_sum}")

    return priorities_sum


def run():
    executor = FileExecutor('aoc_2022/aoc_04/input.txt')
    return executor.execute(treat_lines)


def run_dummy():
    dummy_lines = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]

    executor = DummyExecutor(dummy_lines)
    return executor.execute(treat_lines)


if __name__ == "__main__":
    run_dummy()
    run()