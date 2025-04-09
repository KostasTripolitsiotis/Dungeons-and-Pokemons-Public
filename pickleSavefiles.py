import pickle
from pokemon import Pokemon
from constants.directories import Directory
from constants.googleSheet import SheetName
from constants.trades import TradeGen4
import numpy as np
from sheetInfo import SheetCommands
import datetime
import charUpload as cu
import os

class SaveFiles:
    @staticmethod
    def checkPath(file:str):
        '''Checks if path exist and if not can create that path'''
        try:
            with open(file, 'rb') as f:
                f.close()
        except FileNotFoundError:
            print("File or directory was not found:",file,"\nWould you like to create path and/or file?\n(Y/n)")
            ans = input()
            if ans.lower() == 'y':
                path = os.path.split(file)
                if os.path.exists(path[0]) is False:
                    os.mkdir(path[0])
                temp = open(file, 'wb')
                temp.close()
                print("Path successfully created.")
            else:
                return False
        return True
    
    @staticmethod
    def openFile(file:str) -> list[Pokemon] | None:
        '''Open .pkl file and return obj list. None if path is not found'''
        if SaveFiles.checkPath(file) is False:
            return None
        with open(file, 'rb') as f:
            pokemons = []
            while True:
                try:
                    pokemons.append(pickle.load(f))
                except EOFError:
                    break
        return pokemons
    
    @staticmethod
    def updatePokemon(savefile:str, sheet:str):
        '''Not to be used! Created to generate random movesets when web scrapper was implemented'''
        pokemons = SaveFiles.openFile(savefile)
        temp =[]
        amount = len(pokemons)
        i=1

        for p in pokemons:
            print("Setting up Pokemon ", i, '/', amount, ' ('+p.name+')', sep='')
            setMoveset = False
            if p.moveset == '' and p.name != 'Marowak (Alolan)': setMoveset = True
            poke = Pokemon(p.name, p.ivs[0], p.ivs[1], p.ivs[2], p.ivs[3], p.ivs[4], p.ivs[5], lvl=p.lvl, nature=p.nature, setMoveset=setMoveset)
            if p.moveset == '': setMoveset = False
            poke.ability = p.ability
            poke.gender = p.gender
            poke.moveset = p.moveset
            poke.trainer = p.trainer
            poke.uniqueID = p.uniqueID

            temp.append(poke)
            i += 1
        pokemons = temp

        SheetCommands.upload(temp, sheet)
        SaveFiles.savePokemon(pokemons, savefile)

    @staticmethod
    def savePokemon(pokemons:list[Pokemon], file:str):
        '''Saves pokemons in savefile'''
        if SaveFiles.checkPath(file) is False:
            return None
        with open(file, 'wb') as outp:
            for pokemon in pokemons:
                pickle.dump(pokemon, outp, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def showParty(file:str, trainer:str):
        '''Show party of trainer from savefile'''
        if SaveFiles.checkPath(file) is False:
            return None
        
        pokemons = SaveFiles.openFile(file)
        try:
            for poke in pokemons:
                if poke.trainer == trainer:
                    print('\n#=======#\n')
                    poke.printInfo()
        except Exception as e:
            print(e)
            
    @staticmethod
    def showSavefile(file:str):
        '''Show all pokemon from savefile'''
        if SaveFiles.checkPath(file) is False:
            return None
        
        pokemons = SaveFiles.openFile(file)
        try:
            print("Showing pokemon in", file)
            for poke in pokemons:
                print('\n#=======#\n')
                poke.printInfo()
        except Exception as e:
            print(e)

def captured(poke_wild, id, trainer):
    poke_players = SaveFiles.openFile(Directory.PLAYERS)
    found = False

    for pokemon in poke_players:
        if pokemon.uniqueID == id:
            pokemon.trainer = trainer
            found = True
            SheetCommands.upload(pokemon, SheetName.PLAYERS)
    if not found:
        for pokemon in poke_wild:
            if pokemon.uniqueID == id:
                pokemon.trainer = trainer
                poke_players.append(pokemon)
                pokemon.printInfo()
                SheetCommands.upload(pokemon, SheetName.PLAYERS)

    SaveFiles.savePokemon(poke_players, Directory.PLAYERS)

def getPokecenterTrade():
    i=np.random.randint(0, len(TradeGen4.GIVE)+1)
    return TradeGen4.GIVE[i]

#===============================================================
# pokeplayers = openFile(fl.PLAYERS)
# wild = openFile(fl.WILD_POKEMON)
# temp = []
# npcs = openFile(fl.NPCS)

# for poke in pokeplayers:
#     if poke.uniqueID == 910728:
#         poke.evolve()
#         poke.levelUp(55)
#         temp.append(poke)


# sh.upload(temp, fl.SHEET_PLAYERS)
# savePokemon(pokeplayers, fl.PLAYERS)
#==================================================================
# file = fl.WILD_POKEMON
# temp = []
# pokemons = openFile(file)

# poke = pk.Pokemon('Cherubi', lvl=30)
# temp.append(poke)

# poke = pk.Pokemon('Roselia', lvl=30)
# temp.append(poke)

# poke = pk.Pokemon('Budew', lvl=28)
# temp.append(poke)

# poke = pk.Pokemon('Budew', lvl=29)
# temp.append(poke)

# poke = pk.Pokemon('Budew', lvl=30)
# temp.append(poke)

# poke = pk.Pokemon('Turtwig', lvl=30)
# temp.append(poke)

# poke = pk.Pokemon('Roselia', lvl=30)
# temp.append(poke)

# sh.upload(temp, fl.SHEET_WILDSPAWNS)
# savePokemon(pokemons, file)
#=================================================================
# pokenpc = openFile(fl.NPCS)
# temp = []

# for poke in pokenpc:
#     if poke.uniqueID == 331712:
#         poke.levelUp(50)
#         temp.append(poke)

# sh.upload(temp, fl.SHEET_NPCS)
# savePokemon(pokenpc, fl.NPCS)
#=================================================================
# file = fl.WILD_POKEMON
# pokemons = openFile(file)

# for poke in pokemons:
#     if poke.uniqueID == 14316:
#         poke.printInfo()

#=================================================================

# print(getPokecenterTrade())

#=================================================================

# updatePokemon(fl.PLAYERS, fl.SHEET_PLAYERS)

#=================================================================

# pokemon = openFile(fl.NPCS)
# for poke in pokemon:
#     if poke.uniqueID == 285464:
#         cu.charUpload(poke)

#=================================================================

# for i in range(5):
#     pokemon = fl.TRADES_GEN4_REQUEST
#     index = np.random.randint(0, len(pokemon))
#     print('Pokemon ', i, 'in distress: ', pokemon[index], '!', sep='')

#=================================================================
# pokeplayers = openFile(fl.PLAYERS)
# wild = openFile(fl.WILD_POKEMON)
# temp = []
# npcs = openFile(fl.NPCS)

# for poke in pokeplayers:
#     if poke.uniqueID == 910728:
#         poke.evsUpdate(spD = 20)
#         print(poke.evs)
#         temp.append(poke)

# sh.upload(temp, fl.SHEET_PLAYERS)
# savePokemon(pokeplayers, fl.PLAYERS)