# Write a function that accepts two parameters, a parent and a child string.
# Determine how many times the child string - or an anagram of the child string
# - appears in the parent string. There is a solution which can be done in near
# instant time.

# f('AdnBndAndBdaBn', 'dAn') // 4 ("Adn", "ndA", "dAn", "And")

import collections
from typing import Iterable, TypeVar


# first naive solution: permute child, search for occurrences in parent
# O(p * c^2)
def anagram_detector_1(parent: str, child: str) -> int:
    c = 0
    for p in permute(child):
        c += parent.count(p)
    return c


def permute(s: str) -> [str]:
    if len(s) == 1:
        return [s]
    res = []
    for i, c in enumerate(s):
        rest = s[:i] + s[i+1:]
        for p in permute(rest):
            res.append(c + p)
    return res


# I don't know what "near instant time" means, but I'm going to shoot for O(p)
def anagram_detector_2(parent: str, child: str) -> int:
    reference_hist = dict(HistogramQueue(child))
    hq = HistogramQueue()

    count = 0

    for p in parent:
        hq.push(p)
        while hq[p] > reference_hist.get(p, 0):
            hq.pop()
        if len(hq) == len(child):
            count += 1

    return count


T = TypeVar('VT')


class HistogramQueue(dict):

    def __init__(self, iterable: [T]=""):
        super().__init__()
        self.queue = collections.deque()
        for c in iterable:
            self.push(c)

    def push(self, a) -> None:
        super().__setitem__(a, 1 + self.get(a, 0))
        self.queue.append(a)

    def pop(self) -> T:
        a = self.queue.popleft()
        super().__setitem__(a, -1 + self.get(a))
        return a

    def __setitem__(self, k: T, v: int) -> None:
        raise Exception("Cannot set value directly in HistogramQueue")

    def __getitem__(self, k: T) -> int:
        return super().__getitem__(k)

    def __len__(self) -> int:
        return len(self.queue)





