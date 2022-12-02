"""Utils common for whole AOC"""


class Executor:
    """
    Common executor
    """
    def __init__(self, input_path) -> None:
        self._input_path = input_path

    def execute(self, executor):
        """
        Parse the input and call executor

        Args:
            executor: call executor with read lines
        """
        with open(self._input_path, 'r', encoding="utf-8") as f:
            lines = f.read().splitlines()

        executor(lines)
