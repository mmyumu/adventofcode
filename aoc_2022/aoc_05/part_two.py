from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_05.common import DUMMY_LINES, CratesReader, Crane


class CrateMover9001(Crane):
    def __init__(self, crates, operations):
        super(CrateMover9001, self).__init__(crates, operations)

    def _operate(self, operation):
        logger.info(f"Execute operation: {operation}")

        crates_to_move = self._crates[operation.src - 1][-operation.number:]
        del self._crates[operation.src - 1][-operation.number:]
        self._crates[operation.dst - 1].extend(crates_to_move)


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    reader = CratesReader(lines)
    crane = CrateMover9001(reader.get_crates().copy(), reader.get_operations())

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