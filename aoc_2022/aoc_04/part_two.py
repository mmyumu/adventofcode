from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_04.common import DUMMY_LINES, RedundantPairComputer


class PartlyRedundantPairComputer(RedundantPairComputer):
    """
    Check whether the pair is partly redundant

    Args:
        RedundantPairComputer: Abstract redundant pair computer
    """
    def _compute_redundant(self, set1, set2):
        return len(set1.intersection(set2)) > 0



def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = PartlyRedundantPairComputer()

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

    executor = DummyExecutor(DUMMY_LINES)
    return executor.execute(treat_lines)


if __name__ == "__main__":
    run_dummy()
    run()