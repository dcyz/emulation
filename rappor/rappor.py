import random


class Rappor:
    f, p, q, n = 0.5, 0.5, 0.75, 1000

    @classmethod
    def setup(cls, n, f=0.5, p=0.5, q=0.75):
        cls.f = f
        cls.p = p
        cls.q = q
        cls.n = n

    def __init__(self, loc):
        self._seq = [0 for i in range(self.n)]
        self._seq[loc] = 1
        self._rr()

    def _rr(self):
        f1, f2 = 0.5 * self.f, self.f
        for i in range(self.n):
            r = random.random()
            if r <= f1:
                self._seq[i] = 1
            elif r <= f2:
                self._seq[i] = 0
            else:
                pass
            b = self._seq[i]
            r = random.random()
            if b == 0:
                if r <= self.p:
                    self._seq[i] = 1
                else:
                    self._seq[i] = 0
            else:
                if r <= self.q:
                    self._seq[i] = 1
                else:
                    self._seq[i] = 0

    def get_value(self):
        return self._seq

# class Rappor:
#
#     @classmethod
#     def setup(cls, n, f=0.5, p=0.5, q=0.75):
#         cls._f = f
#         cls._p = p
#         cls._q = q
#         cls._n = n
#
#     def __init__(self, loc):
#         self._seq = 1 << (self._n - 1) | (1 << loc)
#         self._rr()
#
#     def _rr(self):
#         mask = 1
#         f1, f2 = 0.5 * self._f, self._f
#         for i in range(self._n):
#             r = random.random()
#             if r <= f1:
#                 self._seq |= mask
#             elif r <= f2:
#                 self._seq &= ~mask
#             else:
#                 pass
#             b = self._seq & mask
#             r = random.random()
#             if b == 0:
#                 if r <= self._p:
#                     self._seq |= mask
#             else:
#                 if r <= self._q:
#                     self._seq |= mask
#             mask <<= 1
#
#     def get_value(self):
#         return self._seq
