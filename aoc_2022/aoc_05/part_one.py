from logger import logger
from utils import DummyExecutor, FileExecutor
from aoc_2022.aoc_05.common import DUMMY_LINES, CratesReader, Crane


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    reader = CratesReader(lines)
    crane = Crane(reader.get_crates().copy(), reader.get_operations())

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