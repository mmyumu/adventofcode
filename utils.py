"""Utils common for whole AOC"""
from abc import abstractmethod

class Executor:
    """
    Abstract executor
    """
    def __init__(self) -> None:
        pass

    def execute(self, executor, lines=1):
        """
        Parse the input and call executor
        """
        lines = self._get_lines()
        executor(self._split_lines(lines))

    @abstractmethod
    def _get_lines(self):
        """
        Get lines from input

        Returns:
            str | str[]: lines to work on
        """

    @staticmethod
    def _split_lines(lines):
        if lines==1:
            pass
        else:
            pass

        return lines


class FileExecutor(Executor):
    """
    Executor to read file
    """
    def __init__(self, input_path) -> None:
        self._input_path = input_path

    def _get_lines(self):
        with open(self._input_path, 'r', encoding="utf-8") as f:
            lines = f.read().splitlines()

        return lines

        
class DummyExecutor(Executor):
    """
    Dummy executor to read manual input
    """
    def __init__(self, dummy_lines) -> None:
        super(DummyExecutor, self).__init__()
        self._dummy_lines = dummy_lines

    def _get_lines(self):
        return self._dummy_lines
