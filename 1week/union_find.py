"""Union Find Class and Tkinter GUI for it to play."""
import tkinter as tk


class UF(object):
    """Union Find Class"""

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


uf = UF(10)
assert len(uf.alist) == 10
assert uf.is_connected(0, 1) is False

uf.union(0, 1)
assert uf.is_connected(0, 1) is True
assert uf.alist[0] == 1


class Application(tk.Frame):
    """Simple Tkinter GUI for union-find theme."""

    def __init__(self, master: object, num_of_elems: int):
        """Creating widgets and uf object."""
        super().__init__(master)
        self.master = master
        self.pack()
        self.num_of_elems = num_of_elems
        self.uf = UF(num_of_elems)
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets."""
        self.canvas = tk.Canvas(
            self,
            width=800,
            height=600,
            borderwidth=2,
            relief='groove',
        )
        self.canvas.pack()

        self.create_circles()

        self.label = tk.Label(
            self, text='Two indexes p and q, comma-separated for union',
        )
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.btn = tk.Button(
            self,
            text='make union',
            command=lambda: self.make_union(self.entry.get()),
        )
        self.btn.pack()

        self.regen_btn = tk.Button(
            self,
            text='clear and regenerate',
            command=self.clear_and_regen,
        )
        self.regen_btn.pack()

        self.quit = tk.Button(
            self,
            text='QUIT',
            fg='red',
            command=self.master.destroy,
        )
        self.quit.pack()

    def create_circles(self):
        """Creating circles with elements inside."""
        x_off = 50
        x = 80
        y = 150
        r = 20
        for el in self.uf.alist:
            x += x_off
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            self.canvas.create_oval(x0, y0, x1, y1)
            self.canvas.create_text(
                x,
                y,
                font='Roboto 20',
                fill='black',
                text=el,
            )

    def make_union(self, value_str):
        """Perform UF uniion operation and rerender canvas."""
        val_list = value_str.split(',')
        p = int(val_list[0])
        q = int(val_list[1])
        self.uf.union(p, q)
        self.canvas.delete('all')
        self.create_circles()

    def clear_and_regen(self):
        """Clear canvas and rerender."""
        self.canvas.delete('all')
        self.uf = UF(self.num_of_elems)
        self.create_circles()


root = tk.Tk()
root.geometry('1024x768')
app = Application(root, num_of_elems=10)
app.mainloop()
