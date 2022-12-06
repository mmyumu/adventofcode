from utils import FileExecutor
from logger import logger


def run():
    executor = FileExecutor('aoc_2022/aoc_01/input.txt')
    return executor.execute(treat_lines)


def treat_lines(lines):
    """
    Entrypoint
    """
    calories = []
    current_calories = 0
    elf_number = 1
    for line in lines:
        if line:
            try:
                calory = int(line)
                current_calories += calory
            except ValueError:
                logger.exception("Cannot get calories from line")
        else:
            logger.info(f"Elf number {elf_number} is carrying {current_calories}")
            calories.append(current_calories)
            calories = sorted(calories, reverse=True)

            current_calories = 0
            elf_number += 1

    part_one_result = calories[0]
    part_two_result = sum(calories[:3])
    logger.info(f"Part one: An elf is carrying {part_one_result} which is the maximum")
    logger.info(f"Part two: Sum of calories carried by top three elves: {part_two_result}")

    return part_one_result, part_two_result


if __name__ == "__main__":
    run()
