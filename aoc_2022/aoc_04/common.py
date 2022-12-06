from abc import abstractmethod


class RedundantPairComputer:
    """
    Check whether the pair is redundant
    """
    def compute(self, range1, range2):
        range1_start, range1_end = range1.split("-")
        range2_start, range2_end = range2.split("-")

        range1_start = int(range1_start)
        range1_end = int(range1_end)
        range2_start = int(range2_start)
        range2_end = int(range2_end)

        set1 = self._to_set(range1_start, range1_end)
        set2 = self._to_set(range2_start, range2_end)

        return self._compute_redundant(set1, set2)

    @staticmethod
    def _to_set(start, end):
        return set(range(start, end + 1))

    @abstractmethod
    def _compute_redundant(self, set1, set2):
        pass
