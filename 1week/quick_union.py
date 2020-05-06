"""Union Find QuickUnion Class and Tkinter GUI for it to play."""
import tkinter as tk


class QuickUnionUF(object):
    """QuickUnion Union Find Class"""

    def __init__(self, num_of_elems: int):
        """Created list of elems here."""
        self.alist = list(range(num_of_elems))

    def _root(self, i: int):
        """Find root element for given index"""
        while i != self.alist[i]:
            i = self.alist[i]
        return i

    def is_connected(self, p: int, q: int):
        """Func to test if to elemes connected."""
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int):
        """Make union of elements."""
        root_p = self._root(p)
        root_q = self._root(q)
        self.alist[root_p] = root_q



uf = QuickUnionUF(10)
assert len(uf.alist) == 10
assert uf.is_connected(0, 1) is False

uf.union(0, 1)
assert uf.is_connected(0, 1) is True
assert uf.alist[0] == 1

