import gspread 
import random
import pickle
from constants.directories import Directory
from constants.googleSheet import SheetColumn, SheetName
import time
import numpy as np
from statFunctions import Func
#from pokemon import Pokemon

with open(Directory.MASTERSHEET, 'rb') as f:
    mastersheet = pickle.load(f)

names = []
for row in range(len(mastersheet)):
        names.append(mastersheet[row][1])

ids = []
for row in range(len(mastersheet)):
    if row == 0:
        ids.append(0)
    else:
        ids.append(int(mastersheet[row][0]))

class SheetCommands:
    mastersheet = mastersheet
    names = names
    ids = ids
    
    @staticmethod
    def update():
        '''Downloads Poke_Ref spreadsheet and saves it in mastersheet.pkl'''
        sa = gspread.service_account()
        sh = sa.open("PokemonStats")
        wks = sh.worksheet("Poke_Ref")
        mastersheet = wks.get_all_values()
        with open(Directory.MASTERSHEET, 'wb') as outp:
            pickle.dump(mastersheet, outp, pickle.HIGHEST_PROTOCOL)
            
    @staticmethod
    def getIndex(name:str) -> int:
        '''Returns pokemon's index in spreadsheet from name'''
        return names.index(name)
    
    @staticmethod
    def getBaseHp(name:str) -> int:
        '''Returns base Hp from name'''
        i = SheetCommands.getIndex(name)
        print(i, name)
        return int(mastersheet[i][SheetColumn.BASE_HP])

    @staticmethod
    def getBaseAtk(name:str) -> int:
        '''Returns base Atk from name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.BASE_ATK])
    
    @staticmethod
    def getBaseDef(name:str) -> int:
        '''Returns base Def from name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.BASE_DEF])
    
    @staticmethod
    def getBaseSpA(name:str) -> int:
        '''Returns base SpA from name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.BASE_SPA])
    
    @staticmethod
    def getBaseSpD(name:str) -> int:
        '''Returns base SpD from name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.BASE_SPD])
    
    @staticmethod
    def getBaseSpe(name:str) -> int:
        '''Returns base Sppe from name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.BASE_SPE])
    
    @staticmethod
    def getAbility(name:str) -> str:
        '''Returns random ability from name. 1/250 chance for shiny'''
        i = SheetCommands.getIndex(name)
        
        abilities = [mastersheet[i][SheetColumn.AB1]]
        if mastersheet[i][SheetColumn.AB2] != '—':
            abilities.append(mastersheet[i][SheetColumn.AB2])
        hAbility = mastersheet[i][SheetColumn.AB3]

        if random.randrange(250) == 0 and hAbility != '—':
            ability = hAbility
        elif len(abilities) == 2:
            ability = abilities[random.randrange(2)]
        else:
            ability = abilities[0]

        return ability
    
    @staticmethod
    def getGender(name:str) -> str:
        '''Returns random gender by name'''
        i = SheetCommands.getIndex(name)
        cells = [mastersheet[i][SheetColumn.MALE], mastersheet[i][SheetColumn.FEMALE]]
        if cells[0] != '—':
            ratio = float(cells[0].replace('%', '').replace(',','.'))
            if random.randrange(1, 101) < ratio:
                gender = 'Male'
            else:
                gender = 'Female'
        elif cells[1] != '—':
            ratio = float(cells[1].replace('%', '').replace(',','.'))
            if random.randrange(1, 101) < ratio:
                gender = 'Female'
            else:
                gender = 'Male'
        else:
                gender = 'Genderless'
        return gender
    
    @staticmethod
    def getType(name:str) -> tuple[str, str]:
        '''Returns pokemon type by name'''
        i = SheetCommands.getIndex(name)
        cells = [mastersheet[i][SheetColumn.TYPE1], mastersheet[i][SheetColumn.TYPE2]]
        types = []
        for cell in cells:
            if cell != '—':
                types.append(cell)
        return types
    
    @staticmethod
    def getEggGroup(name:str) -> tuple[str, str]:
        '''Returns pokemon egg group by name'''
        i = SheetCommands.getIndex(name)
        cells = [mastersheet[i][SheetColumn.EGRP1], mastersheet[i][SheetColumn.EGRP2]]
        groups = []
        for cell in cells:
            if cell != '—':
                groups.append(cell)
        return groups
    
    @staticmethod
    def getDexID(name:str) -> int:
        '''Returns dex id by name'''
        i = SheetCommands.getIndex(name)
        return int(mastersheet[i][SheetColumn.DEXID])
    
    @staticmethod
    def getNameFromID(id:int) -> str:
        '''Returns name by id'''
        i = ids.index(id)
        return mastersheet[i][SheetColumn.NAME]
    
    @staticmethod
    def upload(pokemons, sheet) -> None:
        '''Gets pokemon list (or individual) and uploads it to google spreadsheet (by id)'''
        sa = gspread.service_account()
        sh = sa.open("PokemonStats")
        wks = sh.worksheet(sheet)

        if type(pokemons) != list:
            pokemons = [pokemons]
        amount = len(pokemons)
        current = 1

        for pokemon in pokemons:
            print("Uploading Pokemon ", current, '/', amount, ' (', pokemon.name, ')', ' in sheet: ', sheet,  sep='')
            row = SheetCommands.convertObjToRow(pokemon)
            try:
                row_num = str(wks.find(str(pokemon.uniqueID)).row)
                wks.update('A'+row_num+':'+'AL'+row_num, row)
            except Exception as e:
                print(e)
                row_num = str(wks.find('-').row)
                wks.update('A'+row_num+':'+'AL'+row_num, row)
            time.sleep(3)
            current = current + 1         
            
    @staticmethod
    def removePokemon(pokemons, sheet) -> None:
        '''Searches spreadsheet from pokemon.uniqueID and removes it'''
        sa = gspread.service_account()
        sh = sa.open("PokemonStats")
        wks = sh.worksheet(sheet)

        if type(pokemons) != list:
            pokemons = [pokemons]
        amount = len(pokemons)
        current = 1
        for pokemon in pokemons:
            print("Deleting Pokemon ", current, '/', amount, ' (', pokemon.name, ')', ' from sheet: ', sheet,  sep='')
            try:
                row = str(wks.find(str(pokemon.uniqueID)).row)
                wks.delete_rows(int(row))
            except Exception as e:
                    print('Exception: ', e)
            current = current + 1
            
    @staticmethod
    def removePokemonByID(ids: str | list[str], sheet) -> None:
        '''Searches spreadsheet from uniqueID and removes it. Similar with removePokemon'''
        sa = gspread.service_account()
        sh = sa.open("PokemonStats")
        wks = sh.worksheet(sheet)
        
        if type(ids) != list:
            ids = [ids]
        amount = len(ids)
        current = 1
        for id in ids:
            print("Deleting Pokemon ", current, '/', amount, ' (', id, ')', ' from sheet: ', sheet,  sep='')
            try:
                row = str(wks.find(str(id)).row)
                wks.delete_rows(int(row))
            except Exception as e:
                    print('Exception: ', e)
            current = current + 1
            
    @staticmethod
    def downloadSheetContents(sheet:str) -> list[list[str]]:
        '''Downloads google spreadsheet from name and returns non-empty rows (checks IDs)'''
        print("Downloading "+sheet+"...")
        sa = gspread.service_account()
        sh = sa.open("PokemonStats")
        wks = sh.worksheet(sheet).get_all_values()
        values = []
        for value in wks:
            if value[2] != '-':
                values.append(value)
        return values
    
    @staticmethod
    def downloadAllSheet() -> dict[str, list[list[str]]]:
        print("Downloading campain sheets...")
        sheets = {
            SheetName.PLAYERS : SheetCommands.downloadSheetContents(SheetName.PLAYERS),
            SheetName.WILDSPAWNS : SheetCommands.downloadSheetContents(SheetName.WILDSPAWNS), 
            SheetName.NPCS : SheetCommands.downloadSheetContents(SheetName.NPCS),
            SheetName.GYMLEADERS : SheetCommands.downloadSheetContents(SheetName.GYMLEADERS)
        }
        
        return sheets
    
    @staticmethod
    def convertObjToRow(pokemons) -> list[list[str]]:
        '''Takes pokemon or list of pokemons (Obj Pokemon) and converts them 
        \ninto list[list[str]] formated to be uploaded to the spreadsheet'''
        if type(pokemons) != list:
            pokemons = [pokemons]
        rows = []
        
        for p in pokemons:
            type2 = '—'
            try: type2 = p.type[1]
            except Exception as e:
                pass
            for i in range(4-len(p.moveset)):
                p.moveset.append(['—', '—', '—', '—', '—'])
            row = [p.trainer, p.name, p.uniqueID, p.type[0], type2, p.ability, p.nature, p.gender, p.stats[2], p.stats[6], p.stats[1], p.stats[5],
                p.stats[3], p.stats[4], p.stats[0], int(10+np.floor((p.stats[5]-10)/2)), int(10+np.floor((p.stats[3]-10)/2)), p.lvl, p.moveset[0][0],
                p.moveset[0][1], p.moveset[0][2], p.moveset[0][3], p.moveset[0][4], p.moveset[1][0], p.moveset[1][1], p.moveset[1][2], 
                p.moveset[1][3], p.moveset[1][4], p.moveset[2][0], p.moveset[2][1], p.moveset[2][2], p.moveset[2][3], p.moveset[2][4], 
                p.moveset[3][0], p.moveset[3][1], p.moveset[3][2], p.moveset[3][3], p.moveset[3][4]]
            row = list(map(str, row))
            
            rows.append(row)

        return rows

