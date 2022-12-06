from logger import logger
from utils import FileExecutor
from aoc_2022.aoc_02.common import INPUTS1, SCORE_PER_INPUT, ROCK, PAPER, SCISSORS, Resolver


# LOSE = "lose"
# DRAW = "draw"
# WIN = "win"


# INPUTS2 = {
#     "X": LOSE,
#     "Y": DRAW,
#     "Z": WIN
# }


class ShiFuMiResolver:
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

        if input2 == "Y":
            return 3 + SCORE_PER_INPUT[input1]

        if input2 == "X":
            result_score = 0
            if input1 == ROCK:
                shape_score = SCORE_PER_INPUT[SCISSORS]
            elif input1 == PAPER:
                shape_score = SCORE_PER_INPUT[ROCK]
            elif input1 == SCISSORS:
                shape_score = SCORE_PER_INPUT[PAPER]
        elif input2 == "Z":
            result_score = 6
            if input1 == ROCK:
                shape_score = SCORE_PER_INPUT[PAPER]
            elif input1 == PAPER:
                shape_score = SCORE_PER_INPUT[SCISSORS]
            elif input1 == SCISSORS:
                shape_score = SCORE_PER_INPUT[ROCK]
        
        return result_score + shape_score




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

    return total_score


def run():
    executor = FileExecutor('aoc_2022/aoc_02/input.txt')
    return executor.execute(resolve_lines)

if __name__ == "__main__":
    run()
