from abc import abstractmethod


class PrioritiesComputer:
    """
    Compute the priorities of items.
    The way to select items must be implemented
    """
    def compute(self, input):
        """
        Compute the priority

        Args:
            line (str): line describing rucksack content

        Returns:
            int: priority
        """
        items = self._get_items(input)
        return self._compute_priority(items)

    @abstractmethod
    def _get_items(self, line):
        pass

    @staticmethod
    def _get_same_items(items_lists):
        return set.intersection(*map(set, items_lists))

    @staticmethod
    def _compute_priority(items):
        rucksack_priority = 0

        for item in items:
            priority = 0
            if item.isupper():
                priority = ord(item) - ord('A') + 27
            else:
                priority = ord(item) - ord('a') + 1
            rucksack_priority += priority

        return rucksack_priority
