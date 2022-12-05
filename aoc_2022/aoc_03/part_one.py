from logger import logger
from utils import Executor


class PrioritiesComputer:
    """
    Compute the priorities of items in both compartments of a rucksack
    """
    def compute(self, line):
        """
        Compute the priority of the rucksack

        Args:
            line (str): line describing rucksack content

        Returns:
            int: priority of the rucksack
        """
        half_index = int(len(line) / 2)
        half1 = line[:half_index]
        half2 = line[half_index:]

        item_in_both_compartment = []
        for item1 in half1:
            for item2 in half2:
                if item1 == item2:
                    item_in_both_compartment.append(item1)

        rucksack_priority = 0
        item_in_both_compartment = set(item_in_both_compartment)
        for item in item_in_both_compartment:
            priority = 0
            if item.isupper():
                priority = ord(item) - ord('A') + 27
            else:
                priority = ord(item) - ord('a') + 1
            rucksack_priority += priority

        return rucksack_priority


def treat_lines(lines):
    """
    Treat input lines

    Args:
        lines (str[]): lines as an array of strings
    """

    computer = PrioritiesComputer()

    priorities_sum = 0
    for line in lines:
        priorities_sum += computer.compute(line)

    logger.info(f"Sum of priorities: {priorities_sum}")


if __name__ == "__main__":
    executor = Executor('aoc_2022/aoc_03/input.txt')
    executor.execute(treat_lines)

    # dummy_lines = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw"
    # ]
    # treat_lines(dummy_lines)
