from logger import logger
from utils import Executor
from aoc_2022.aoc_02.common import INPUTS1, SCORE_PER_INPUT, ROCK, PAPER, SCISSORS, Resolver


INPUTS2 = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}


class ShiFuMiResolver(Resolver):
    """
    Resolve ShiFuMi games
    """
    def __init__(self):
        pass

    def resolve(self, input1, input2):
        """
        Resolve the game between opponent input and player input

        Args:
            input1 (str): opponent input
            input2 (str): player input
        """
        input1 = INPUTS1[input1]
        input2 = INPUTS2[input2]

        return self._compute_score(input1, input2)

    def _compute_score(self, input1, input2):
        input_score = SCORE_PER_INPUT[input2]
        if input1 == input2:
            return 3 + input_score

        if input1 == ROCK:
            if input2 == PAPER:
                return 6 + input_score
            else:
                return 0 + input_score

        if input1 == PAPER:
            if input2 == SCISSORS:
                return 6 + input_score
            else:
                return 0 + input_score

        if input1 == SCISSORS:
            if input2 == ROCK:
                return 6 + input_score
            else:
                return 0 + input_score


def resolve_lines(lines):
    """
    Resolve input lines

    Args:
        lines (_type_): _description_
    """
    resolver = ShiFuMiResolver()

    total_score = 0
    for line in lines:
        inputs = line.split(' ')
        total_score += resolver.resolve(inputs[0], inputs[1])

    logger.info(f"Total score: {total_score}")


if __name__ == "__main__":
    executor = Executor('aoc_2022/aoc_02/input.txt')
    executor.execute(resolve_lines)
