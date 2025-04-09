import tkinter as tk

class ManageFrame(tk.Frame):
    def __init__(self, root, controller,  bg_color, width, height):
        super().__init__(root, width=width, height=height, bg=bg_color)
        self.bg_color = bg_color
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.load_frame()

    def load_frame(self):
        self.label1 = tk.Label(self, text="Manage Frame :)", bg=self.bg_color, fg="white")

        self.create_layout()

    def create_layout(self):
        self.label1.pack()
