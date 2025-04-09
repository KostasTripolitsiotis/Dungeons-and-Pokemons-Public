import tkinter as tk
from tkinter import ttk
import pypokedex as pd
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO
import numpy as np
import sys 
import os
FPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(FPATH[0])
from constants.campainGen4 import TRAINERS
from constants.directories import Directory
from constants.googleSheet import SheetName
from pickleSavefiles import SaveFiles
from sheetInfo import SheetCommands
import charUpload as cu
from sfx.sfx import Sfx
from trainersFrame import TrainerFrame
from wildsFrame import WildFrame

def getDamageDice(moveset):
    dices = ''
    for move in moveset:
        if move[2] != '—':
            power = int(int(move[2])/5)
            dice=10
            while power > 0 and dice > 0:
                r = int(np.floor(power/dice))
                power = power - r*dice
                if r != 0:
                    dices = dices+str(r)+'d'+str(dice)
                    if power != 0:
                        dices = dices+'+'
                dice = dice - 1

    return dices


class ShowFrame(tk.Frame):
    def __init__(self, root, controller,  bg_color, width, height):
        super().__init__(root, width=width, height=height, bg=bg_color)
        self.bg_color = bg_color
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.root = root
        self.width = width
        self.height = height
        
        # creating a container
        self.container = tk.Frame(self, width=width, height=height)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        #creating frames
        self.frames = {}
        frame1 = TrainerFrame(self.container, self, self.bg_color)
        self.frames[TrainerFrame]= frame1

        frame1 = MasterFrame(self.container, self, self.bg_color)
        self.frames[MasterFrame]= frame1

        frame1 = WildFrame(self.container, self, self.bg_color)
        self.frames[WildFrame] = frame1

        self.load_frame(MasterFrame)

    def load_frame(self, cont):
        if cont == 'MasterFrame':
            self.load_frame(MasterFrame)
        else:
            frame = self.frames[cont]
            if frame == self.frames[WildFrame]:
                if self.controller.reloadWilds == True:
                    self.frames[WildFrame].destroy()
                    frame = WildFrame(self.container, self, self.bg_color)
                    self.frames[WildFrame] = frame
                    self.controller.changeReloadWilds()
            frame.tkraise()

    def reload_trainers(self):
        self.frames[TrainerFrame].destroy()
        frame = TrainerFrame(self.container, self, self.bg_color)
        self.frames[TrainerFrame] = frame

class MasterFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.bg_color = bg_color
        self.load_frame()

    def load_frame(self):
        self.label1 = tk.Label(self, text="Select a category to search", bg=self.bg_color, fg="white", font=(15))
        self.btn_wild = tk.Button(self,
                                command=lambda:[self.controller.load_frame(WildFrame),
                                                self.controller.controller.attributes('-fullscreen', True)],
                                text="See all wild pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        self.btn_trainer = tk.Button(self,
                                command=lambda:[self.controller.load_frame(TrainerFrame),
                                                self.controller.controller.attributes('-fullscreen', True)],
                                text="See pokemon by trainer", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        self.btn_byname = tk.Button(self,
                                #command=lambda:self.controller.load_frame(shf.ShowFrame),
                                text="Search by atribute", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )

        self.create_layout()

    def create_layout(self):
        self.label1.pack(pady=10)
        self.btn_wild.pack()
        self.btn_trainer.pack(pady=10)
        self.btn_byname.pack()

