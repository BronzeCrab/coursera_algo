"""Union Find QuickFind Class and Tkinter GUI for it to play."""
import tkinter as tk

from tkinter_app import BaseApplication


class QuickFindUF(object):
    """QuickFind Union Find Class"""

    def __init__(self, num_of_elems: int):
        """Created list of elems here."""
        self.alist = list(range(num_of_elems))

    def is_connected(self, p: int, q: int):
        """Func to test if to elemes connected."""
        return self.alist[p] == self.alist[q]

    def union(self, p: int, q: int):
        """Make union of elements."""
        p_val = self.alist[p]
        q_val = self.alist[q]
        for i, x in enumerate(self.alist):
            if x == p_val:
                self.alist[i] = q_val


uf = QuickFindUF(10)
assert len(uf.alist) == 10
assert uf.is_connected(0, 1) is False

uf.union(0, 1)
assert uf.is_connected(0, 1) is True
assert uf.alist[0] == 1


root = tk.Tk()
root.geometry('1024x768')
app = BaseApplication(root, num_of_elems=10, uf_class=QuickFindUF)
app.mainloop()
