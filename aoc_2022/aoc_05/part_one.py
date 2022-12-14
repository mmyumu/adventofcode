from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_05.common import DUMMY_LINES, CratesReader, Crane


class CrateMover9000(Crane):
    def __init__(self, crates, operations):
        super(CrateMover9000, self).__init__(crates, operations)

    def _operate(self, operation):
        logger.info(f"Execute operation: {operation}")

        for _ in range(operation.number):
            crate = self._crates[operation.src - 1].pop()
            self._crates[operation.dst - 1].append(crate)


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    reader = CratesReader(lines)
    crane = CrateMover9000(reader.get_crates().copy(), reader.get_operations())

    crane.operate()
    top_crates = crane.get_top_crates()
    
    logger.info(f"Top crates: {top_crates}")

    return top_crates


def run():
    executor = FileExecutor('aoc_2022/aoc_05/input.txt')
    return executor.execute(treat_lines)


def run_dummy():
    executor = DummyExecutor(DUMMY_LINES)
    return executor.execute(treat_lines)


if __name__ == "__main__":
    run_dummy()
    run()