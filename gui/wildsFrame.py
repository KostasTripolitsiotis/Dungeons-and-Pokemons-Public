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


class WildFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color, width=800, height=300)
        self.bg_color = bg_color
        self.controller = controller
        # self.columnconfigure(1, 14)
        self.config(width=900, height=1500)
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.grid(sticky='news')

        self.wildpokemon = self.getWilds()

        self.label_title = tk.Label(self, text="Wild Pokemon Spawned: "+str(len(self.wildpokemon)), font=("TkMenuFont", 14), bg=self.bg_color, fg="white")
        self.label_subtitle = tk.Label(self, text="Pokemon    ID    Type    Ability    Nature    Gender      Move 1         Move 2         Move 3         Move 4",
                                       font=("TkMenuFont", 14), bg=self.bg_color, fg="white")


        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = tk.Frame(self)
        self.frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
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
        i=0
        self.oldcheck = 0
        for poke in self.wildpokemon:
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

        self.frame_canvas.config(width=1500+self.vsb.winfo_width(), height=970)
        # Set the canvas scrolling region
        self.canvas.config(scrollregion=(0, 0, 900, (len(self.wildpokemon)*68)))

        self.btn_back = tk.Button(self, text="Back", 
                            command=lambda:[self.controller.load_frame('MasterFrame'),
                                            self.controller.controller.attributes('-fullscreen', False), 
                                            self.controller.controller.geometry(controller.width+ 'x'+ controller.height)],
                            bg="#28393a", 
                            fg="white", 
                            cursor="hand2", 
                            activebackground="#badee2", 
                            activeforeground="black"
                            )
        
        self.btn_despawn = tk.Button(self, text="Depsawn", 
                            command=self.despawn,  
                            bg="#28393a", 
                            fg="white", 
                            cursor="hand2", 
                            activebackground="#badee2", 
                            activeforeground="black"
                            )
        
        self.btn_capture = tk.Button(self, text="Catch", 
                            command=lambda:self.capture(clicked_trainers.get(), createToken.get()),  
                            bg="#28393a", 
                            fg="white", 
                            cursor="hand2", 
                            activebackground="#badee2", 
                            activeforeground="black"
                            )
        
        all_trainers = TRAINERS
        clicked_trainers = tk.StringVar()
        clicked_trainers.set(all_trainers[0])
        self.drop_trainers = ttk.Combobox(self, textvariable=clicked_trainers, values=all_trainers, width=12)

        createToken = tk.IntVar()
        self.checkbox = tk.Checkbutton(self, 
                                       text='Create character sheet', 
                                       variable=createToken,
                                       onvalue=True, 
                                       offvalue=False,
                                       cursor="hand2",
                                       background="#28393a",
                                       activebackground='#badee2',
                                       activeforeground='black',
                                       fg='white',
                                       selectcolor='black',
                                       relief='raised')

        self.create_layout(self.wildpokemon)

    def deselect(self):
        count = 0
        values = []
        for i in range(len(self.wildpokemon)):
            values.append(self.vars[i].get())
            if values[i] == 1:
                count += 1

        if count == 1:
            self.oldcheck = values.index(1)

        if count > 1:
            self.vars[self.oldcheck].set(0)
            values = []
            for i in range(len(self.wildpokemon)):
                values.append(self.vars[i].get())
            self.oldcheck = values.index(1)

    def create_layout(self, wildpokemon:list):
        self.label_title.grid(row=0, column=0, columnspan=12, sticky='news')

        self.label_subtitle.grid(row=1, column=0, columnspan=12, sticky="news")

        i=2
        for poke in wildpokemon:
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

        self.btn_back.grid(row=i, column=0, sticky='W')

        self.btn_despawn.grid(row=1, column=1, sticky='WS')

        self.btn_capture.grid(row=2, column=1, sticky='NW')
        self.drop_trainers.grid(row=2, column=2, sticky='NW')
        self.checkbox.grid(row=1, column=2, columnspan=3, sticky='E')

    def _on_mouseWheel(self,event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def despawn(self):
        index = self.oldcheck
        id = self.wildpokemon[index].uniqueID

        print('###Clearing wild pokemon, id:', id)
        wildpokemon = SaveFiles.openFile(Directory.WILD_POKEMON)
        for poke in wildpokemon:
            if poke.uniqueID == id:
                SheetCommands.removePokemon(poke, SheetName.WILDSPAWNS)
                wildpokemon.remove(poke)
                SaveFiles.savePokemon(wildpokemon, Directory.WILD_POKEMON)

        self.controller.controller.reloadWilds = True
        self.controller.load_frame(WildFrame)

    def capture(self, trainer, createToken):
        index = self.oldcheck
        id = self.wildpokemon[index].uniqueID

        print('###Trainer ', trainer, ' is capturing a pokemon with id:', id, sep='')
        pokemons = SaveFiles.openFile(Directory.WILD_POKEMON)
        playerpoke = SaveFiles.openFile(Directory.PLAYERS)
        for poke in pokemons:
            if poke.uniqueID == id:
                poke.trainer = trainer
                playerpoke.append(poke)
                self.despawn()
                SheetCommands.upload(poke, SheetName.PLAYERS)

                if createToken == True:
                    print('###Creating character sheet for pokemon (', poke.name, ')', sep='')
                    cu.charUpload(poke)

        SaveFiles.savePokemon(pokemons, Directory.WILD_POKEMON)
        SaveFiles.savePokemon(playerpoke, Directory.PLAYERS)

    def getWilds(self):
         return SaveFiles.openFile(Directory.WILD_POKEMON)