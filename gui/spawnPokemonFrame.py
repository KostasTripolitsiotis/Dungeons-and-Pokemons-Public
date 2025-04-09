import tkinter as tk
from tkinter import ttk

from constants.campainGen4 import TRAINERS
from constants.pokeAttribute import NATURES, TYPES
from constants.directories import Directory, FILES
from pickleSavefiles import SaveFiles
from campain import PokeCommands

def enableMoveEdit():
    pass

class SpawnFrame(tk.Frame):
    def __init__(self, root, controller,  bg_color, width, height):
        super().__init__(root, width=width, height=height, bg=bg_color)
        self.bg_color = bg_color
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)

        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #creating frames
        self.frames = {}
        frame = MasterFrame(container, self, self.bg_color)
        self.frames[MasterFrame]= frame

        frame = SpawnWild(container, self, self.bg_color)
        self.frames[SpawnWild]= frame

        frame = SpawnCustom(container, self, bg_color)
        self.frames[SpawnCustom] = frame

        self.load_frame(MasterFrame)

    def load_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
class MasterFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.bg_color = bg_color
        self.load_frame()

    def load_frame(self):
        self.label = tk.Label(self, text='Spawn a Pokemon', bg=self.bg_color, fg="white", font=(20))
        self.btn_wild = tk.Button(self,
                                command=lambda:self.controller.load_frame(SpawnWild),
                                text="Spawn a wild pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        self.btn_custom = tk.Button(self,
                                command=lambda:self.controller.load_frame(SpawnCustom),
                                text="Spawn custom pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )

        self.create_layout()

    def create_layout(self):
        self.label.pack(pady=10)
        self.btn_wild.pack()
        self.btn_custom.pack(pady=10)

class SpawnWild(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.bg_color = bg_color
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.load_frame()

    def load_frame(self):
        self.label_route = tk.Label(self, text='Select route', bg=self.bg_color, fg="white", font=(9))
        
        all_routes = PokeCommands.getRoutesGen4()
        clicked = tk.StringVar()
        clicked.set(all_routes[0])
        self.drop_routes = ttk.Combobox(self, textvariable=clicked, values=all_routes, width=45)

        self.label_amount = tk.Label(self, text='Amount', bg=self.bg_color, fg="white", font=(9))

        self.amount = tk.Spinbox(self, from_=1, to=50)

        self.btn_spawn = tk.Button(self,
                                command=lambda:[PokeCommands.spawn(clicked.get(), int(self.amount.get()), createToken.get()), 
                                                self.controller.controller.changeReloadWilds()],
                                text="Spawn", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )

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
        
        self.btn_clear = tk.Button(self,
                                command=lambda:PokeCommands.clearWildPokemon(),
                                text="Clear all wild Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.label_clear = tk.Label(self, text='Clear pokemon by unique ID:', bg=self.bg_color, fg="white", font=(9))
        
        self.entry_clear = tk.Entry(self, bg='#badee2', width=15)

        self.btn_clearone = tk.Button(self,
                                command=lambda:PokeCommands.clearWildPokemon(int(self.entry_clear.get())),
                                text="Clear Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.btn_showPokemon = tk.Button(self,
                                command=lambda:SaveFiles.showSavefile(Directory.WILD_POKEMON),
                                text="Show all wild Pokemon", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black", 
                                anchor='s'
                                )
        
        self.label_capture = tk.Label(self, text='Capture a wild Pokemon', bg=self.bg_color, fg="white", font=(9))
        self.label_id = tk.Label(self, text='ID:', bg=self.bg_color, fg="white", font=(9))

        self.entry_id = tk.Entry(self, bg='#badee2', width=6)

        self.label_trainer = tk.Label(self, text='Trainer:', bg=self.bg_color, fg="white", font=(9))

        all_trainers = TRAINERS
        clicked_trainers = tk.StringVar()
        clicked_trainers.set(all_trainers[0])
        self.drop_trainers = ttk.Combobox(self, textvariable=clicked_trainers, values=all_trainers, width=12)

        self.btn_capture = tk.Button(self,
                                command=lambda:PokeCommands.capture(int(self.entry_id.get()), clicked_trainers.get(), createToken.get()),
                                text="Capture", 
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.btn_back = tk.Button(self, text="Back", 
                                command=lambda:self.controller.load_frame(MasterFrame),  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )

        self.create_layout()

    def create_layout(self):
        self.label_route.grid(row=0, column=0, sticky='EW')
        self.drop_routes.grid(row=0, column=1, sticky='EW')
        self.label_amount.grid(row=0, column=2, sticky='EW')
        self.amount.grid(row=0, column=3, sticky='EW')
        self.btn_spawn.grid(row=0, column=4, sticky='EW', padx=10)

        self.checkbox.grid(row=1, column=0)

        self.btn_clear.grid(row=2, column=0, pady=10)

        self.label_clear.grid(row=3, column=0, pady=10)
        self.entry_clear.grid(row=3, column=1, sticky='w')
        self.btn_clearone.grid(row=3, column=1)

        self.label_capture.grid(row=4, column=0, sticky='w')
        self.label_id.grid(row=4, column=0, sticky='e')
        self.entry_id.grid(row=4, column=1, sticky='w')

        self.btn_capture.grid(row=5, column=0)
        self.label_trainer.grid(row=5, column=0, sticky='e')
        self.drop_trainers.grid(row=5, column=1, sticky='w')

        self.btn_back.grid(row=6, column=3, sticky='ES', columnspan=2, padx=15, pady=15)
        self.btn_showPokemon.grid(row=7, column=3, sticky='ES', columnspan=2, padx=15)

class SpawnCustom (tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        self.place(x=0, y=0, relheight=1, relwidth=1)
        self.bg_color = bg_color
        self.rowconfigure(2, pad=10)
        self.rowconfigure(4, pad=5)
        self.load_frame()

    def load_frame(self):
        self.label_title = tk.Label(self, text='Spawn custom pokemon', font=('Arial bold', 15), bg=self.bg_color, fg="white")

        self.label_pokemon = tk.Label(self, text='Pokemon:', bg=self.bg_color, fg="white", font=(9))

        allpokemon = PokeCommands.getAllPokemon()
        pokemon = tk.StringVar()
        pokemon.set(allpokemon[2])
        self.drop_pokemon = ttk.Combobox(self, textvariable=pokemon, values=allpokemon)

        self.label_hp = tk.Label(self, text='Hp:', bg=self.bg_color, fg="white", font=(5))
        ivs_range = [i for i in range(-1, 32)]
        hp = tk.IntVar()
        hp.set(ivs_range[0])
        self.drop_hp = ttk.Combobox(self, textvariable=hp, values=ivs_range, width=3)

        self.label_atk = tk.Label(self, text='Atk:', bg=self.bg_color, fg="white", font=(5))
        atk = tk.IntVar()
        atk.set(ivs_range[0])
        self.drop_atk = ttk.Combobox(self, textvariable=atk, values=ivs_range, width=3)

        self.label_deff = tk.Label(self, text='Def:', bg=self.bg_color, fg="white", font=(5))
        deff = tk.IntVar()
        deff.set(ivs_range[0])
        self.drop_deff = ttk.Combobox(self, textvariable=deff, values=ivs_range, width=3)

        self.label_spa = tk.Label(self, text='SpA:', bg=self.bg_color, fg="white", font=(5))
        spa = tk.IntVar()
        spa.set(ivs_range[0])
        self.drop_spa = ttk.Combobox(self, textvariable=spa, values=ivs_range, width=3)

        self.label_spd = tk.Label(self, text='SpD:', bg=self.bg_color, fg="white", font=(5))
        spd = tk.IntVar()
        spd.set(ivs_range[0])
        self.drop_spd = ttk.Combobox(self, textvariable=spd, values=ivs_range, width=3)

        self.label_spe = tk.Label(self, text='Spe:', bg=self.bg_color, fg="white", font=(5))
        spe = tk.IntVar()
        spe.set(ivs_range[0])
        self.drop_spe = ttk.Combobox(self, textvariable=spe, values=ivs_range, width=3)

        self.label_title2 = tk.Label(self, text='Optional', font=('Arial bold', 15), bg=self.bg_color, fg="white")
        self.label_trainer = tk.Label(self, text='Trainer:', bg=self.bg_color, fg="white", font=(5))
        
        useOpt = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self, 
                                       text='Use optional settings when spawning Pokemon', 
                                       variable=useOpt,
                                       onvalue=True, 
                                       offvalue=False,
                                       cursor="hand2",
                                       background="#28393a",
                                       activebackground='#badee2',
                                       activeforeground='black',
                                       fg='white',
                                       selectcolor='black',
                                       relief='raised')

        all_trainers = TRAINERS
        all_trainers.insert(0, '')
        clicked_trainers = tk.StringVar()
        clicked_trainers.set(all_trainers[0])
        self.drop_trainers = ttk.Combobox(self, textvariable=clicked_trainers, values=all_trainers, width=12)

        self.label_nature = tk.Label(self, text='Nature:', bg=self.bg_color, fg="white", font=(5))

        all_natures = NATURES
        all_natures.insert(0, '')
        clicked_natures = tk.StringVar()
        clicked_natures.set(all_natures[0])
        self.drop_natures = ttk.Combobox(self, textvariable=clicked_natures, values=all_natures, width=12)

        self.label_level = tk.Label(self, text='Level:', bg=self.bg_color, fg="white", font=(5))
        self.amount_lvl = tk.Spinbox(self, from_=0, to=200, width=3)

        self.label_gender = tk.Label(self, text='Gender:', bg=self.bg_color, fg="white", font=(5))
        
        genders = ['', 'Genderless', 'Male', 'Female']
        clk_genders = tk.StringVar()
        clk_genders.set(genders[0])
        self.drop_genders = ttk.Combobox(self, textvariable=clk_genders, values=genders, width=11)

        self.label_ability = tk.Label(self, text='Ability:', bg=self.bg_color, fg="white", font=(5))
        self.entry_ability = tk.Entry(self, bg='#badee2')

        #Generate moveset checkbox
        self.useMoves = tk.BooleanVar(value=True)
        self.checkbox_moves = tk.Checkbutton(self, 
                                       text='Generate random moveset', 
                                       variable=self.useMoves,
                                       onvalue=True, 
                                       offvalue=False,
                                       cursor="hand2",
                                       background="#28393a",
                                       activebackground='#badee2',
                                       activeforeground='black',
                                       fg='white',
                                       selectcolor='black',
                                       relief='raised')
        self.checkbox_moves.select()

        self.load_moves()

        self.btn_spawn = tk.Button(self, text="SPAWN", 
                                command=lambda:PokeCommands.spawnCustom(str(pokemon.get()), int(hp.get()), int(atk.get()), int(deff.get()), 
                                                           int(spa.get()), int(spd.get()), int(spe.get()), str(clicked_trainers.get()), 
                                                           str(clicked_natures.get()), int(self.amount_lvl.get()), str(clk_genders.get()), 
                                                           str(self.entry_ability.get()), useOpt.get(), self.useMoves.get(), self.getMoveset(),
                                                           createToken.get(), str(clk_files.get())),
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        self.btn_back = tk.Button(self, text="Back", 
                                command=lambda:self.controller.load_frame(MasterFrame),  
                                bg="#28393a", 
                                fg="white", 
                                cursor="hand2", 
                                activebackground="#badee2", 
                                activeforeground="black"
                                )
        
        createToken = tk.BooleanVar()
        self.checkbox_createToken = tk.Checkbutton(self, 
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
        
        self.label_savefile = tk.Label(self, text='Savefile:', bg=self.bg_color, fg="white", font=(5))

        clk_files = tk.StringVar()
        clk_files.set(FILES[0])
        self.drop_files = ttk.Combobox(self, textvariable=clk_files, values=FILES, width=13)
        
        self.create_layout()

    def load_moves(self):
        self.label_moves = tk.Label(self, text='Moves', bg=self.bg_color, fg="white", font=(5))
        self.label_type = tk.Label(self, text='Type', bg=self.bg_color, fg="white", font=(5))
        self.label_category = tk.Label(self, text='Category', bg=self.bg_color, fg="white", font=(5))
        self.label_pow = tk.Label(self, text='Power', bg=self.bg_color, fg="white", font=(5))
        self.label_acc = tk.Label(self, text='Acc', bg=self.bg_color, fg="white", font=(5))
        self.label_pp = tk.Label(self, text='PP', bg=self.bg_color, fg="white", font=(5))

        types = TYPES
        types.insert(0, '—')
        category = ['—', 'Status', 'Physical', 'Special']

        #====Move 1
        #Move1 label
        self.label_move1 = tk.Label(self, text='Move 1:', bg=self.bg_color, fg="white", font=(5))

        #move1 entry
        self.entry_move1 = tk.Entry(self, bg='#badee2', width=20)
        self.entry_move1.insert(0, '—')

        #move1 type (typing)
        self.clk_types1 = tk.StringVar()
        self.clk_types1.set(types[0])
        self.drop_types1 = ttk.Combobox(self, textvariable=self.clk_types1, values=types, width=9)

        #move1 type (physical/special)
        self.clk_category1 = tk.StringVar()
        self.clk_category1.set(category[0])
        self.drop_category1 = ttk.Combobox(self, textvariable=self.clk_category1, values=category, width=9)

        #move1 power
        self.entry_move1_pow = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move1_pow.insert(0, '—')

        #move1 Acc
        self.entry_move1_acc = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move1_acc.insert(0, '—')

        #move1 PP
        self.entry_move1_pp = tk.Entry(self, bg='#badee2', width=3)
        self.entry_move1_pp.insert(0, '—')

        #====Move 2
        #Move2 label
        self.label_move2 = tk.Label(self, text='Move 2:', bg=self.bg_color, fg="white", font=(5))

        #move2 entry
        self.entry_move2 = tk.Entry(self, bg='#badee2', width=20)
        self.entry_move2.insert(0, '—')

        #move2 type (typing)
        self.clk_types2 = tk.StringVar()
        self.clk_types2.set(types[0])
        self.drop_types2 = ttk.Combobox(self, textvariable=self.clk_types2, values=types, width=9)

        #move2 type (physical/special)
        self.clk_category2 = tk.StringVar()
        self.clk_category2.set(category[0])
        self.drop_category2 = ttk.Combobox(self, textvariable=self.clk_category2, values=category, width=9)

        #move2 power
        self.entry_move2_pow = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move2_pow.insert(0, '—')

        #move2 Acc
        self.entry_move2_acc = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move2_acc.insert(0, '—')

        #move2 PP
        self.entry_move2_pp = tk.Entry(self, bg='#badee2', width=3)
        self.entry_move2_pp.insert(0, '—')

        #====Move 3
        #Move3 label
        self.label_move3 = tk.Label(self, text='Move 3:', bg=self.bg_color, fg="white", font=(5))

        #move3 entry
        self.entry_move3 = tk.Entry(self, bg='#badee2', width=20)
        self.entry_move3.insert(0, '—')

        #move3 type (typing)
        self.clk_types3 = tk.StringVar()
        self.clk_types3.set(types[0])
        self.drop_types3 = ttk.Combobox(self, textvariable=self.clk_types3, values=types, width=9)

        #move3 type (physical/special)
        self.clk_category3 = tk.StringVar()
        self.clk_category3.set(category[0])
        self.drop_category3 = ttk.Combobox(self, textvariable=self.clk_category3, values=category, width=9)

        #move3 power
        self.entry_move3_pow = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move3_pow.insert(0, '—')

        #move3 Acc
        self.entry_move3_acc = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move3_acc.insert(0, '—')

        #move3 PP
        self.entry_move3_pp = tk.Entry(self, bg='#badee2', width=3)
        self.entry_move3_pp.insert(0, '—')

        #====Move 4
        #Move4 label
        self.label_move4 = tk.Label(self, text='Move 4:', bg=self.bg_color, fg="white", font=(5))

        #move4 entry
        self.entry_move4 = tk.Entry(self, bg='#badee2', width=20)
        self.entry_move4.insert(0, '—')

        #move4 type (typing)
        self.clk_types4 = tk.StringVar()
        self.clk_types4.set(types[0])
        self.drop_types4 = ttk.Combobox(self, textvariable=self.clk_types4, values=types, width=9)

        #move3 type (physical/special)
        self.clk_category4 = tk.StringVar()
        self.clk_category4.set(category[0])
        self.drop_category4 = ttk.Combobox(self, textvariable=self.clk_category4, values=category, width=9)

        #move4 power
        self.entry_move4_pow = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move4_pow.insert(0, '—')

        #move4 Acc
        self.entry_move4_acc = tk.Entry(self, bg='#badee2', width=4)
        self.entry_move4_acc.insert(0, '—')

        #move4 PP
        self.entry_move4_pp = tk.Entry(self, bg='#badee2', width=3)
        self.entry_move4_pp.insert(0, '—')

    def create_layout(self):
        self.label_title.grid(row=0, column=0, columnspan=14)
        
        self.label_pokemon.grid(row=1, column=0)
        self.drop_pokemon.grid(row=1, column=1)
        self.label_hp.grid(row=1, column=2)
        self.drop_hp.grid(row=1, column=3)
        self.label_atk.grid(row=1, column=4)
        self.drop_atk.grid(row=1, column=5)
        self.label_deff.grid(row=1, column=6)
        self.drop_deff.grid(row=1, column=7)
        self.label_spa.grid(row=1, column=8)
        self.drop_spa.grid(row=1, column=9)
        self.label_spd.grid(row=1, column=10)
        self.drop_spd.grid(row=1, column=11)
        self.label_spe.grid(row=1, column=12)
        self.drop_spe.grid(row=1, column=13)

        self.label_title2.grid(row=2, column=0, columnspan=14, sticky='s')
        self.checkbox.grid(row=2, column=0, columnspan=14, sticky='se')

        self.label_trainer.grid(row=3, column=0)
        self.drop_trainers.grid(row=3, column=1, sticky='w')
        self.label_nature.grid(row=3, column=2)
        self.drop_natures.grid(row=3, column=3, columnspan=2)
        self.label_level.grid(row=3, column=5)
        self.amount_lvl.grid(row=3, column=6)
        self.label_gender.grid(row=3, column=7)
        self.drop_genders.grid(row=3, column=8, columnspan=2)
        self.label_ability.grid(row=3, column=10)
        self.entry_ability.grid(row=3, column=11, columnspan=3)
        
        self.checkbox_moves.grid(row=4, column=0, sticky='Ws', columnspan=4)

        self.label_moves.grid(row=5, column=1)
        self.label_type.grid(row=5, column=2, columnspan=2)
        self.label_category.grid(row=5, column=4)
        self.label_pow.grid(row=5, column=5)
        self.label_acc.grid(row=5, column=6)
        self.label_pp.grid(row=5, column=7)

        self.label_move1.grid(row=6, column=0)
        self.entry_move1.grid(row=6, column=1, sticky='w')
        self.drop_types1.grid(row=6, column=2, columnspan=2)
        self.drop_category1.grid(row=6, column=4)
        self.entry_move1_pow.grid(row=6, column=5)
        self.entry_move1_acc.grid(row=6, column=6)
        self.entry_move1_pp.grid(row=6, column=7)

        self.label_move2.grid(row=7, column=0)
        self.entry_move2.grid(row=7, column=1, sticky='w')
        self.drop_types2.grid(row=7, column=2, columnspan=2)
        self.drop_category2.grid(row=7, column=4)
        self.entry_move2_pow.grid(row=7, column=5)
        self.entry_move2_acc.grid(row=7, column=6)
        self.entry_move2_pp.grid(row=7, column=7)

        self.label_move3.grid(row=8, column=0)
        self.entry_move3.grid(row=8, column=1, sticky='w')
        self.drop_types3.grid(row=8, column=2, columnspan=2)
        self.drop_category3.grid(row=8, column=4)
        self.entry_move3_pow.grid(row=8, column=5)
        self.entry_move3_acc.grid(row=8, column=6)
        self.entry_move3_pp.grid(row=8, column=7)

        self.label_move4.grid(row=9, column=0)
        self.entry_move4.grid(row=9, column=1, sticky='w')
        self.drop_types4.grid(row=9, column=2, columnspan=2)
        self.drop_category4.grid(row=9, column=4)
        self.entry_move4_pow.grid(row=9, column=5)
        self.entry_move4_acc.grid(row=9, column=6)
        self.entry_move4_pp.grid(row=9, column=7)

        self.btn_spawn.grid(row=10, column=0)
        self.label_savefile.grid(row=10, column=1, sticky='e')
        self.drop_files.grid(row=10, column=2, columnspan=2, sticky='w')
        self.checkbox_createToken.grid(row=10, column=4, columnspan=3, sticky='w')
        self.btn_back.grid(row=10, column=11, sticky='ES', columnspan=4, pady=5)

    def getMoveset(self):
        move1 = [str(self.entry_move1.get())]
        move1.append(str(self.clk_types1.get())+' '+str(self.clk_category1.get()))
        move1.append(str(self.entry_move1_pow.get()))
        move1.append(str(self.entry_move1_acc.get())+'%')
        move1.append(str(self.entry_move1_pp.get()))

        move2 = [str(self.entry_move2.get())]
        move2.append(str(self.clk_types2.get())+' '+str(self.clk_category2.get()))
        move2.append(str(self.entry_move2_pow.get()))
        move2.append(str(self.entry_move2_acc.get())+'%')
        move2.append(str(self.entry_move2_pp.get()))

        move3 = [str(self.entry_move3.get())]
        move3.append(str(self.clk_types3.get())+' '+str(self.clk_category3.get()))
        move3.append(str(self.entry_move3_pow.get()))
        move3.append(str(self.entry_move3_acc.get())+'%')
        move3.append(str(self.entry_move3_pp.get()))

        move4 = [str(self.entry_move4.get())]
        move4.append(str(self.clk_types4.get())+' '+str(self.clk_category4.get()))
        move4.append(str(self.entry_move4_pow.get()))
        move4.append(str(self.entry_move4_acc.get())+'%')
        move4.append(str(self.entry_move4_pp.get()))

        moveset = [move1, move2, move3, move4]
        print(moveset)
        
        return moveset
