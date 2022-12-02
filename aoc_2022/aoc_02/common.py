from abc import abstractmethod


ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

INPUTS1 = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

SCORE_PER_INPUT = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


class Resolver:
    """
    Abstract resolver for different parts
    """
    @abstractmethod
    def resolve(self, input1, input2):
        """
        Resolve the game between input1 and input2

        Args:
            input1 (str): first input in line
            input2 (str): second input in line
        """
