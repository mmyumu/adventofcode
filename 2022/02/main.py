from logger import logger


ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

INPUTS1 = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

INPUTS2 = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

SCORE_PER_INPUT = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

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


def run():
    """
    Entrypoint
    """
    resolver = ShiFuMiResolver()

    with open('2022/02/input.txt', 'r', encoding="utf-8") as f:
        lines = f.read().splitlines()

    total_score = 0
    for line in lines:
        inputs = line.split(' ')
        total_score += resolver.resolve(inputs[0], inputs[1])

    logger.info(f"Total score: {total_score}")


if __name__ == "__main__":
    run()
