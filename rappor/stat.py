from rappor.rappor import Rappor


class Stat:

    def __init__(self, us: list):
        self._total = 0
        self._us = us
        self._count = [0 for i in range(Rappor.n)]
        self._calc()

    def _item_count(self, index):
        n, ni = len(self._us), 0
        for u in self._us:
            if u[index] == 1:
                ni += 1
        return 1 / (1 - Rappor.f) * ((ni - n * Rappor.p) / (Rappor.q - Rappor.p) - Rappor.f * n / 2)

    def _calc(self):
        for i in range(Rappor.n):
            c = self._item_count(i)
            self._count[i] = c
            self._total += c

    def get_result(self):
        return self._count[:]
