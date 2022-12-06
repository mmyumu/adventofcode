from logger import logger
from utils import DummyExecutor, FileExecutor


class RedundantPairComputer:
    """
    Compute if the pair is redundant
    """
    def compute(self, range1, range2):
        range1_start, range1_end = range1.split("-")
        range2_start, range2_end = range2.split("-")

        range1_start = int(range1_start)
        range1_end = int(range1_end)
        range2_start = int(range2_start)
        range2_end = int(range2_end)

        set1 = self._to_set(range1_start, range1_end)
        set2 = self._to_set(range2_start, range2_end)

        return set1.issubset(set2) or set2.issubset(set1)

    @staticmethod
    def _to_set(start, end):
        return set(range(start, end + 1))



def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = RedundantPairComputer()

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