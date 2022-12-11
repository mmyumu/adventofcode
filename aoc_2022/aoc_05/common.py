from logger import logger
from abc import abstractmethod


DUMMY_LINES = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]


class Operation:
    def __init__(self, line):
        words = line.split(" ")

        self.number = int(words[1])
        self.src = int(words[3])
        self.dst = int(words[5])

    def __str__(self) -> str:
        return f"move {self.number} from {self.src} to {self.dst}"


class CratesReader:
    def __init__(self, lines) -> None:
        self._lines: str = lines
        self._operations: Operation = []
        self._crates = None

        self._parse_lines()
        self._build_crates_columns()

    def _parse_lines(self):
        for i, line in enumerate(self._lines):
            line = line.strip()
            if line.startswith("1"):
                columns = line.split(" ")
                self._columns_lines_index = i
                self._columns_number = int(columns[len(columns) - 1])
            elif line.startswith("move"):
                self._operations.append(Operation(line))
        return None

    def get_operations(self):
        return self._operations

    def get_crates(self):
        return self._crates

    def _build_crates_columns(self):
        crates = []

        for _ in range(self._columns_number):
            crates.append([])

        for line in self._lines[self._columns_lines_index - 1::-1]:
            for col_index in range(self._columns_number):
                crate = self._get_crate(line, col_index)
                if crate.strip():
                    crate = crate[1:-1]
                    crates[col_index].append(crate)

        self._crates = crates

    @staticmethod
    def _get_crate(line, col_index):
        return line[col_index*4: col_index*4 + 3]


class Crane:
    def __init__(self, crates, operations):
        self._crates = crates
        self._operations = operations

    def operate(self):
        for operation in self._operations:
            self._operate(operation)

    def get_top_crates(self):
        top_crates = ""
        for crates_col in self._crates:
            top_crates += crates_col[len(crates_col) - 1]
        return top_crates

    @abstractmethod
    def _operate(self, operation):
        pass
