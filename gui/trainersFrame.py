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
from campain import PokeCommands as pcmd

class TrainerFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.bg_color = bg_color

        self.label_subtitle = tk.Label(self, text="Pokemon    ID    Type    Ability    Nature    Gender      Move 1         Move 2         Move 3         Move 4",
                                       font=("TkMenuFont", 14), bg=self.bg_color, fg="white")
        self.label_trainer = tk.Label(self, text="Enter trainer's name:", bg=bg_color, fg="white")

        all_trainers = TRAINERS
        clicked_trainers = tk.StringVar()
        clicked_trainers.set(all_trainers[0])
        self.drop_trainers = ttk.Combobox(self, textvariable=clicked_trainers, values=all_trainers, width=12)

        self.btn_back = tk.Button(self, text="Back", 
                                command=lambda:[Sfx.play_button_click(),
                                                self.controller.load_frame('MasterFrame'),
                                                self.controller.controller.attributes('-fullscreen', False), 
                                                self.controller.controller.geometry(self.controller.width+ 'x'+ self.controller.height)],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.btn_search = tk.Button(self, text="Search", 
                                command=lambda:[self.loadPoke(clicked_trainers.get(), bg_color=bg_color)],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = tk.Frame(self)
        self.frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)

        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = tk.Canvas(self.frame_canvas, bg=bg_color)
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        self.vsb = tk.Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.bind_all("<MouseWheel>", self._on_mouseWheel)

        # Create a frame to contain the pokemon (checkbox and labels)
        self.frame_poke = tk.Frame(self.canvas, bg=bg_color)
        self.canvas.create_window((0, 0), window=self.frame_poke, anchor='nw')

        self.vars= []
        self.checks_poke = []
        self.label_names = []
        self.label_ids = []
        self.label_types = []
        self.label_abilities = []
        self.label_natures = []
        self.label_genders = []
        self.label_moves1 = []
        self.label_moves2 = []
        self.label_moves3 = []
        self.label_moves4 = []
        self.pokemon = []
        self.oldcheck = 0

        self.frame_canvas.config(width=1500+self.vsb.winfo_width(), height=900)
        # Set the canvas scrolling region
        self.canvas.config(scrollregion=(0, 0, 900, (len(self.pokemon)*68)))
        
        #level up button
        self.entry_lvlUp = tk.Entry(self, bg='#badee2', width=3)
        self.entry_lvlUp.insert(0, '0')
        
        self.btn_lvlUp = tk.Button(self, text="Level Up", 
                                command="", #lambda:[pcmd.levelUp("", self.pokemon[self.oldcheck].uniqueID, self.entry_lvlUp.get())],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        #trade
        self.btn_trade = tk.Button(self, text="Trade", 
                                command="", #lambda:[pcmd.levelUp("", self.pokemon[self.oldcheck].uniqueID, self.entry_lvlUp.get())],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        clicked_trade = tk.StringVar()
        clicked_trade.set(all_trainers[0])
        self.drop_trade = ttk.Combobox(self, textvariable=clicked_trade, values=all_trainers, width=12)
        
        #evs
        self.btn_evs = tk.Button(self, text="Update EVs", 
                                command="", #lambda:[pcmd.levelUp("", self.pokemon[self.oldcheck].uniqueID, self.entry_lvlUp.get())],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.entry_evs = tk.Entry(self, bg='#badee2', width=4)
        
        #release
        self.btn_release = tk.Button(self, text="Release", 
                                command="", #lambda:[pcmd.levelUp("", self.pokemon[self.oldcheck].uniqueID, self.entry_lvlUp.get())],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        #evolve
        self.btn_evolve = tk.Button(self, text="Evolve", 
                                command="", #lambda:[pcmd.levelUp("", self.pokemon[self.oldcheck].uniqueID, self.entry_lvlUp.get())],  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.entry_evolve = tk.Entry(self, bg='#badee2', width=20)
        
        #get dice  
        
        self.create_layout()
        
    def create_layout(self):
        self.label_subtitle.grid(row=1, column=0, columnspan=12, sticky="news")
        self.btn_search.grid(row=1, column=1, sticky='w')
                
        self.label_trainer.grid(row=2, column=1, sticky='nw')
        self.drop_trainers.grid(row=2, column=1, sticky='nw', padx=112)
        
        self.btn_lvlUp.grid(row=2, column=1, sticky='nw', pady=22)
        self.entry_lvlUp.grid(row=2, column=1, sticky='nw', pady=22, padx=60, ipady=3)
        
        self.btn_trade.grid(row=2, column=1, sticky='nw', pady=50)
        self.drop_trade.grid(row=2, column=1, sticky='nw', pady=50, padx=42)
        
        self.btn_evs.grid(row=2, column=1, sticky='nw', pady=78)
        self.entry_evs.grid(row=2, column=1, sticky='nw', pady=78, padx=74, ipady=3)
        
        self.btn_release.grid(row=2, column=1, sticky='nw', pady=106)
        
        self.btn_evolve.grid(row=2, column=1, sticky='nw', pady=134)
        self.entry_evolve.grid(row=2, column=1, sticky='nw', pady=134, padx=52, ipady=3)
    
        i=2
        for poke in self.pokemon:
            self.checks_poke[i-2].grid(row=i, column=0, sticky='news')
            self.label_names[i-2].grid(row=i, column=1, sticky='news')
            self.label_ids[i-2].grid(row=i, column=2, sticky='news')
            self.label_types[i-2].grid(row=i, column=3, sticky='news')
            self.label_abilities[i-2].grid(row=i, column=4, sticky='news')
            self.label_natures[i-2].grid(row=i, column=5, sticky='news')
            self.label_genders[i-2].grid(row=i, column=6, sticky='news')
            self.label_moves1[i-2].grid(row=i, column=7, sticky='news')
            self.label_moves2[i-2].grid(row=i, column=8, sticky='news')
            self.label_moves3[i-2].grid(row=i, column=9, sticky='news')
            self.label_moves4[i-2].grid(row=i, column=10, sticky='news')
            i +=1

        self.btn_back.grid(row=i, column=0, sticky="SW")

    def delete_pkm(self):
        self.frame_poke.destroy()
        
        self.checks_poke = []
        self.label_names = []
        self.label_ids = []
        self.label_types = []
        self.label_abilities = []
        self.label_natures = []
        self.label_genders = []
        self.label_moves1 = []
        self.label_moves2 = []
        self.label_moves3 = []
        self.label_moves4 = []

    def loadPoke(self, trainer, bg_color):
        self.delete_pkm()
        self.frame_poke = tk.Frame(self.canvas, bg=bg_color)
        self.canvas.create_window((0, 0), window=self.frame_poke, anchor='nw')
        
        self.pokemon = self.getPoke(trainer)
        self.canvas.config(scrollregion=(0, 0, 900, (len(self.pokemon)*68)))
        
        i=0
        for poke in self.pokemon:
            img = PIL.Image.open(os.path.join(FPATH[0], "sprites",str(poke.name)+'.png'))
            img = PIL.ImageTk.PhotoImage(img)
            self.vars.append(tk.IntVar())
            checkbox = tk.Checkbutton(self.frame_poke,
                                    image=img,
                                    variable=self.vars[i],
                                    command=lambda:self.deselect(),
                                    onvalue=1, 
                                    offvalue=0,
                                    cursor="hand2",
                                    background=bg_color,
                                    activebackground=bg_color,
                                    activeforeground='black',
                                    fg='white',
                                    selectcolor='black',
                                    relief='flat',
                                    height=60)
            checkbox.image = img
            self.checks_poke.append(checkbox)

            label_name = tk.Label(self.frame_poke, text=poke.name, bg=self.bg_color, fg="white", font=(9))
            self.label_names.append(label_name)
            label_id = tk.Label(self.frame_poke, text=poke.uniqueID, bg=self.bg_color, fg="white", font=(9))
            self.label_ids.append(label_id)
            label_types = tk.Label(self.frame_poke, text='\n'.join([t for t in poke.type]).title(), bg=self.bg_color, fg="white", font=(9))
            self.label_types.append(label_types)
            label_ability = tk.Label(self.frame_poke, text=f'{poke.ability}', bg=self.bg_color, fg="white", font=(9))
            self.label_abilities.append(label_ability)
            label_nature = tk.Label(self.frame_poke, text=poke.nature, bg=self.bg_color, fg="white", font=(9))
            self.label_natures.append(label_nature)
            label_gender = tk.Label(self.frame_poke, text=poke.gender, bg=self.bg_color, fg="white", font=(9))
            self.label_genders.append(label_gender)
            label_move1 = tk.Label(self.frame_poke, text=', '.join([poke.moveset[0][0], poke.moveset[0][1]])+'\n'+', '.join([poke.moveset[0][2], 
                                                                                                                  poke.moveset[0][3],
                                                                                                                  poke.moveset[0][4]]), bg=self.bg_color, fg="white", font=(9))
            self.label_moves1.append(label_move1)
            label_move2 = tk.Label(self.frame_poke, text=', '.join([poke.moveset[1][0], poke.moveset[1][1]])+'\n'+', '.join([poke.moveset[1][2], 
                                                                                                                  poke.moveset[1][3],
                                                                                                                  poke.moveset[1][4]]), bg=self.bg_color, fg="white", font=(9))
            self.label_moves2.append(label_move2)
            label_move3 = tk.Label(self.frame_poke, text=', '.join([poke.moveset[2][0], poke.moveset[2][1]])+'\n'+', '.join([poke.moveset[2][2], 
                                                                                                                  poke.moveset[2][3],
                                                                                                                  poke.moveset[2][4]]), bg=self.bg_color, fg="white", font=(9))
            self.label_moves3.append(label_move3)
            label_move4 = tk.Label(self.frame_poke, text=', '.join([poke.moveset[3][0], poke.moveset[3][1]])+'\n'+', '.join([poke.moveset[3][2], 
                                                                                                                  poke.moveset[3][3],
                                                                                                                  poke.moveset[3][4]]), bg=self.bg_color, fg="white", font=(9))
            self.label_moves4.append(label_move4)
            i +=1
            
        self.create_layout()

    def deselect(self):
        count = 0
        values = []
        for i in range(len(self.pokemon)):
            values.append(self.vars[i].get())
            if values[i] == 1:
                count += 1

        if count == 1:
            self.oldcheck = values.index(1)

        if count > 1:
            self.vars[self.oldcheck].set(0)
            values = []
            for i in range(len(self.pokemon)):
                values.append(self.vars[i].get())
            self.oldcheck = values.index(1)

    def getPoke(self, trainer):
        temp = []
        pokemon = []
        players = SaveFiles.openFile(Directory.PLAYERS)
        npc = SaveFiles.openFile(Directory.NPCS)
        leaders = SaveFiles.openFile(Directory.LEADERS_GEN4)
        pokemon.extend(players)
        pokemon.extend(npc)
        pokemon.extend(leaders)
        for poke in pokemon:
            if poke.trainer == trainer:
                temp.append(poke)
        return temp
    
    def _on_mouseWheel(self,event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")