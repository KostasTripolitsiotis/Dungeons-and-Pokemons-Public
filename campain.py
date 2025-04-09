import numpy as np
from pokemon import Pokemon
from pickleSavefiles import SaveFiles
from constants.directories import Directory, PathToSheet, Filenames
from constants.googleSheet import SheetName
from sheetInfo import SheetCommands
from constants.routes import RoutesGen4
from constants import campainGen4
import charUpload as cu

class PokeCommands:
    
    @staticmethod
    def __weightedRandom(route:str):
        '''Returns random pokemon from route'''
        weights = []
        for pokemon in route:
            weights.append(pokemon[3])

        sum = 0
        for i in range(len(weights)):
            sum += weights[i]

        r = np.random.randint(sum)

        for i in range(len(weights)):
            r -= weights[i]
            if r < 0:
                return i
        return len(weights)-1
    
    @staticmethod
    def spawn(routeName:str, amount:int, createToken:bool):
        '''Spawn amount of pokemon from route'''
        print('###Spawning ', amount, ' pokemon in route ', routeName, '...', sep='')
        route = getattr(RoutesGen4, routeName)
        temp = []
        wildspawns = SaveFiles.openFile(Directory.WILD_POKEMON)

        for i in range(amount):
            print('Spawning random pokemon ', i+1, '/', amount, sep='')
            x = PokeCommands.__weightedRandom(route)
            pokemon = route[x]
            level = np.random.randint(pokemon[1], pokemon[2]+1)
            pk1 = Pokemon(pokemon[0], lvl=level)
            temp.append(pk1)
            wildspawns.append(pk1)

            i = i+1

        SheetCommands.upload(temp, SheetName.WILDSPAWNS)
        SaveFiles.savePokemon(wildspawns, Directory.WILD_POKEMON)
        
        if createToken == True:
            i=1
            for poke in temp:
                print('Creating character sheet for pokemon ', i, '/', amount, ' (', poke.name, ')', sep='')
                cu.charUpload(poke)
                i = i+1
      
    @staticmethod
    def despawn(savefile:str, ids:int | list[int]):
        '''Deletes pokemon(s) from id or list of ids in savefile'''
        found = False
        temp = []
        if type(ids) != list:
            ids = [ids]
        pokemons = SaveFiles.openFile(savefile)
        for poke in pokemons:
            if poke.uniqueID in ids:
                found = True
                temp.append(poke)
        
        for poke in temp:
            pokemons.remove(poke)
            
        SheetCommands.removePokemon(temp, PathToSheet[savefile])
        SaveFiles.savePokemon(pokemons, savefile)
        if found == False: print("Could not find pokemon with id [", ids, "] in savefile [", savefile, "]")
      
    @staticmethod          
    def spawnCustom(name:str, hp:int, atk:int, deff:int, spa:int, spd:int, spe:int, trainer:str, nature:str, lvl:int, gender:str, 
                    ability:str, useOpt:bool, randMoves:bool, moves:list[list[str]], createToken:bool, savefile:str, custom_id=0):
        '''Spawn pokemon with specific attributes'''
        if int(lvl) == 0: lvl = 5
        if nature == '': poke = Pokemon(name, hp, atk, deff, spa, spd, spe, lvl=lvl, setMoveset=randMoves)
        else: poke = Pokemon(name, hp, atk, deff, spa, spd, spe, lvl=lvl, nature=nature, setMoveset=randMoves)

        if randMoves == False:
            poke.moveset = moves
        if useOpt == True:
            if trainer != '':poke.trainer = trainer
            if gender != '':poke.gender = gender
            if ability !='':poke.ability = ability
        if custom_id != 0:
            poke.uniqueID = custom_id

        match savefile+'.pkl':
            case Filenames.WILD_POKEMON:
                wildspawns = SaveFiles.openFile(Directory.WILD_POKEMON)
                wildspawns.append(poke)
                SheetCommands.upload(poke, SheetName.WILDSPAWNS)
                SaveFiles.savePokemon(wildspawns, Directory.WILD_POKEMON)
            case Filenames.PlAYERS:
                pokeplayers = SaveFiles.openFile(Directory.PLAYERS)
                pokeplayers.append(poke)
                SheetCommands.upload(poke, SheetName.PLAYERS)
                SaveFiles.savePokemon(pokeplayers, Directory.PLAYERS)
            case Filenames.NPCS:
                pokenpc = SaveFiles.openFile(Directory.NPCS)
                pokenpc.append(poke)
                SheetCommands.upload(poke, SheetName.NPCS)
                SaveFiles.savePokemon(pokenpc, Directory.NPCS)
            case Filenames.LEADERS_GEN4:
                pokenpc = SaveFiles.openFile(Directory.LEADERS_GEN4)
                pokenpc.append(poke)
                SheetCommands.upload(poke, SheetName.GYMLEADERS)
                SaveFiles.savePokemon(pokenpc, Directory.LEADERS_GEN4)
            case Filenames.LEADERS_GEN1:
                pokenpc = SaveFiles.openFile(Directory.LEADERS_GEN1)
                pokenpc.append(poke)
                SheetCommands.upload(poke, SheetName.GYMLEADERS)
                SaveFiles.savePokemon(pokenpc, Directory.LEADERS_GEN1)
            case Filenames.TEST:
                poketest = SaveFiles.openFile(Directory.TEST)
                poketest.append(poke)
                SheetCommands.upload(poke, SheetName.TEST)
                SaveFiles.savePokemon(poketest, Directory.TEST)
            case _: print('ERROR - no save file found')

        if createToken == True:
            print('Creating character sheet for pokemon ',poke.name, sep='')
            cu.charUpload(poke)

    @staticmethod
    def clearWildPokemon(id=-1):
        '''Clears wild pokemon by unique ID. -1 to clear all'''
        wildpokemon = SaveFiles.openFile(Directory.WILD_POKEMON)
        if id == -1:
            print('###Clearing all wild pokemon')
            SheetCommands.removePokemon(wildpokemon, SheetName.WILDSPAWNS)
            SaveFiles.savePokemon([], Directory.WILD_POKEMON)
        
        else:
            found = False
            print('###Clearing wild pokemon, id:', id)
            for poke in wildpokemon:
                if poke.uniqueID == id:
                    found = True
                    SheetCommands.removePokemon(poke, SheetName.WILDSPAWNS)
                    wildpokemon.remove(poke)
                    SaveFiles.savePokemon(wildpokemon, Directory.WILD_POKEMON)
            if found == False:
                print("Could not find wild pokemon with ID:", id)
    
    @staticmethod
    def levelUp(savefile:str, id:int, lvl=0):
        '''Levels up pokemon with id from savefile by 1 for lvl=0. Else to the specific level.'''
        if savefile == '':
            files = [SaveFiles.openFile(Directory.NPCS), SaveFiles.openFile(Directory.PLAYERS), SaveFiles.openFile(Directory.LEADERS_GEN4)]
            for file in files:
                found = False
                temp = []
                for pokemon in file:
                    if pokemon.uniqueID == id:
                        found = True
                        pokemon.levelUp(lvl)
                        temp.append(pokemon)
                        SaveFiles.savePokemon(pokemons, savefile)
                        SheetCommands.upload(temp, PathToSheet[savefile])
                if found == True: break
        else:
            pokemons = SaveFiles.openFile(savefile)
            found = False
            temp = []
            for pokemon in pokemons:
                if pokemon.uniqueID == id:
                    found = True
                    pokemon.levelUp(lvl)
                    temp.append(pokemon)
                    SaveFiles.savePokemon(pokemons, savefile)
                    SheetCommands.upload(temp, PathToSheet[savefile])
        
        if found == False:
            print("Could not find pokemon with unique ID [", id, "] in file [", savefile, "]")

    @staticmethod
    def trade(id1:int, savefileOrigin:str, savefileEnd:str, trainer2:str, id2=0, trainer1=""):
        '''Trainer1 is giving pokemon with id1 from Origin and Trainer2 is giving pokemon with id2 from End.
        Use id2=0 to capture wildpokemon as Trainer2 player'''
        pokemonsOrigin = SaveFiles.openFile(savefileOrigin)
        pokemonsEnd = SaveFiles.openFile(savefileEnd)
        found = False
        for poke in pokemonsOrigin:
            if poke.uniqueID == id1:
                poke1 = poke
                found = True
        if found == False:
            print("Could not find pokemon with unique ID [", id1, "] in file [", savefileOrigin, "]")
            return None
                
        if id2 != 0:
            found = False
            for poke in pokemonsEnd:
                if poke.uniqueID == id2:
                    poke2 = poke
                    found = True
            if found == False:
                print("Could not find pokemon with unique ID [", id2, "] in file [", savefileEnd, "]") 
                return None
        
        poke1.trainer = trainer2
        if id2 != 0: poke2.trainer = trainer1
        
        pokemonsEnd.append(poke1)
        if id2 != 0: pokemonsOrigin.append(poke2)
        
        SheetCommands.upload(poke1, PathToSheet[savefileEnd])
        if id2 != 0: SheetCommands.upload(poke2, PathToSheet[savefileOrigin])
        
        SaveFiles.savePokemon(pokemonsEnd, savefileEnd)
        if id2 != 0: SaveFiles.savePokemon(pokemonsOrigin, savefileOrigin)
        
        if savefileEnd != savefileOrigin:
            PokeCommands.despawn(savefileOrigin, id1)
            if id2 != 0: PokeCommands.despawn(savefileEnd, id2)

        if id2 != 0: 
            print("Trainers [", trainer1,"] and [", trainer2, "] have successfully traded [", poke1.name, "] and [", poke2.name,"]")
        else: print(poke1.name, "has been captured by", trainer2+'!!1!')

    @staticmethod
    def capture(id:int, trainer:str, createToken:bool):
        '''Trainer from savefile catches wild pokemon with id'''
        savefile = Directory.NPCS
        if trainer in campainGen4.PCS:
            PokeCommands.trade(id, Directory.WILD_POKEMON, Directory.PLAYERS, trainer)
            savefile = Directory.PLAYERS
        elif trainer in campainGen4.NPCS:
            PokeCommands.trade(id, Directory.WILD_POKEMON, Directory.NPCS, trainer)
        elif trainer in campainGen4.GEN4_LREADERS:
            PokeCommands.trade(id, Directory.WILD_POKEMON, Directory.LEADERS_GEN4, trainer)
            savefile = Directory.LEADERS_GEN4
        else:
            print("Could not find trainer [", trainer, "]. Saving to [", Directory.TEST, "]")
            PokeCommands.trade(id, Directory.WILD_POKEMON, Directory.TEST, trainer)
        
        if createToken == True:
            pokemons = SaveFiles.openFile(savefile)
            for poke in pokemons:
                if poke.uniqueID == id:
                    print('###Creating character sheet for pokemon (', poke.name, ')', sep='')
                    cu.charUpload(poke)
        
    @staticmethod
    def getRoutesGen4():
        '''Returns names of all routes from Gen4'''
        routes = []
        all_vars = dir(RoutesGen4)
        for name in all_vars:
            if name.startswith('ROUTE_') or name.startswith('BIOME_'):
                routes.append(name)
        return routes
    
    @staticmethod
    def getAllPokemon():
        '''Returns names of all pokemon that are available'''
        pokemon = SheetCommands.names
        return pokemon