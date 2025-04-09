import tkinter as tk
import showPokemonFrame as shf
import spawnPokemonFrame as spf
import managePokemonFrame as mpf
from sfx.sfx import Sfx
from multiprocessing import Process

class menuFrame(tk.Frame):
    def __init__(self, root, controller, bg_color, width, height):
        super().__init__(root, width=width, height=height, bg=bg_color)
        self.bg_color = bg_color
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.load_frame()


    def load_frame(self):
        # self widgets
        self.label1 = tk.Label(self, text="Main menu", font=("TkMenuFont", 14), bg=self.bg_color, fg="white")
        self.btnShowPokemon = tk.Button(self,
                                command=lambda:[self.controller.load_frame(shf.ShowFrame),
                                                Sfx.play_button_ran()],
                                text="See Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        self.btnSpawnPokemon = tk.Button(self,
                                command=lambda:[self.controller.load_frame(spf.SpawnFrame),
                                                Sfx.play_button_ran()],
                                text="Spawn Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        self.btnManagePokemon = tk.Button(self, 
                                command=lambda:[self.controller.load_frame(mpf.ManageFrame),
                                         Sfx.play_button_ran()],
                                text="Manage Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.create_layout()

    def create_layout(self):
        self.label1.pack()
        self.btnShowPokemon.pack(pady=20)
        self.btnSpawnPokemon.pack()
        self.btnManagePokemon.pack(pady=20)

    