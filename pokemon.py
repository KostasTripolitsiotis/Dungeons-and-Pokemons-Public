import numpy as np
from statFunctions import Func
from sheetInfo import SheetCommands
import webScrapper as scrapper

class Pokemon:
    def __init__(self, name:str, hp=-1, atk=-1, deff=-1, spA=-1, spD=-1, spe=-1, lvl=5, nature='', setMoveset = True):
        print(name, hp, atk, deff, spA, spD, spe)
        self.name = name
        self.evs = [0, 0, 0, 0, 0, 0]
        self.baseHp = SheetCommands.getBaseHp(name)
        self.baseAtk = SheetCommands.getBaseAtk(name)
        self.baseDef = SheetCommands.getBaseDef(name)
        self.baseSpA = SheetCommands.getBaseSpA(name)
        self.baseSpD = SheetCommands.getBaseSpD(name)
        self.baseSpe = SheetCommands.getBaseSpe(name)
        if nature == '':
            self.setNature()
        else:
            self.nature = nature
        if hp == atk == deff == spA == spD == spe == -1:
            self.randomize()
        else:
            self.ivs = [hp, atk, deff, spA, spD, spe]
            self.calcStats()
        self.gender = SheetCommands.getGender(name)
        self.lvl = lvl
        self.stats = self.calcStats(self.lvl)
        self.ability = SheetCommands.getAbility(name)
        self.type = SheetCommands.getType(name)
        self.eggGroup = SheetCommands.getEggGroup(name)
        self.size = "Small"
        self.dexID = SheetCommands.getDexID(name)
        self.uniqueID = np.random.randint(1,1000001)
        self.trainer = ''
        self.heldItem = ''
        if setMoveset == True:
            self.moveset = scrapper.getMoveset(self.name, lvl = lvl)
        self.shiny = self.getShiny()

    #Generate Random IV seed
    def randomize(self):
        rng = np.random.default_rng()
        self.ivs = rng.integers(0, 32, 6)
        print("IVs seed:",self.ivs)
        self.calcStats()

    #lvl=0: Calculate table of stats, else get stats for level
    def calcStats(self, lvl=0):
        if lvl != 0 :
            stats = []
            stats.append(self.health[self.lvl-1])   #Health
            stats.append(self.hp[self.lvl-1])       #Hp (Con)
            stats.append(self.atk[self.lvl-1])      #Atk
            stats.append(self.deff[self.lvl-1])     #Def
            stats.append(self.spA[self.lvl-1])      #SpA
            stats.append(self.spD[self.lvl-1])      #SpD
            stats.append(self.spe[self.lvl-1])      #Spe
            return stats
        else:
            self.hp = Func.calcStat(self.baseHp, self.ivs[0], 0).astype(int)
            self.atk = Func.calcAtk(self.baseAtk, self.ivs[1], self.nature, self.evs[1]).astype(int)
            self.deff = Func.calcDef(self.baseDef, self.ivs[2], self.nature, self.evs[2]).astype(int)
            self.spA = Func.calcSpA(self.baseSpA, self.ivs[3], self.nature, self.evs[3]).astype(int)
            self.spD = Func.calcSpD(self.baseSpD, self.ivs[4], self.nature, self.evs[4]).astype(int)
            self.spe = Func.calcSpe(self.baseSpe, self.ivs[5], self.nature, self.evs[5]).astype(int)
            self.health = Func.calcHealth(self.baseHp, self.ivs[0], self.evs[0]).astype(int)

    def printInfo(self):
        print("Info for lvl",self.lvl, self.name)
        print("Ability:", self.ability)
        print("Gender:", self.gender)
        print("Egg Group:", self.eggGroup)
        print("Type:", self.type)
        print("Nature:", self.nature)
        print("Health:",self.stats[0])
        print("Hp(Con): ",self.stats[1], ' (', self.ivs[0], ')', sep='')
        print("Atk:",self.stats[2], ' (', self.ivs[1], ')', sep='')
        print("Def:",self.stats[3], ' (', self.ivs[2], ')', sep='')
        print("spA:",self.stats[4], ' (', self.ivs[3], ')', sep='')
        print("spD:",self.stats[5], ' (', self.ivs[4], ')', sep='')
        print("spe:",self.stats[6], ' (', self.ivs[5], ')', sep='')
        print("Dex ID:", self.dexID)
        print("Unique ID:", self.uniqueID)
        print("Trainer:", self.trainer)
        print("Held Item:", self.heldItem)
        print("Moveset:",end=' ')
        for move in self.moveset:
            print(move[0], end=', ')
        print('')
        # if self.shiny == 1:
        #     print('Shonyyyyyy')

    def levelUp(self, lvl=0):
        if lvl == 0:
            self.lvl = self.lvl + 1
        else:
            self.lvl = lvl
        oldStats = self.stats
        self.stats = self.calcStats(self.lvl)

        print(self.name, 'has leveled up')
        print('Health:',self.stats[0],'(+',self.stats[0]-oldStats[0],')', sep='')
        print('Hp(Con):',self.stats[1],'(+',self.stats[1]-oldStats[1],')', sep='')
        print('Atk:',self.stats[2],'(+',self.stats[2]-oldStats[2],')', sep='')
        print('Def:',self.stats[3],'(+',self.stats[3]-oldStats[3],')', sep='')
        print('SpA:',self.stats[4],'(+',self.stats[4]-oldStats[4],')', sep='')
        print('SpD:',self.stats[5],'(+',self.stats[5]-oldStats[5],')', sep='')
        print('Spe:',self.stats[6],'(+',self.stats[6]-oldStats[6],')', sep='')

    def evsUpdate(self, *, hp=0, atk=0, deff=0, spA=0, spD=0, spe=0):
        self.evs[0] = self.evs[0] + hp
        self.evs[1] = self.evs[1] + atk
        self.evs[2] = self.evs[2] + deff
        self.evs[3] = self.evs[3] + spA
        self.evs[4] = self.evs[4] + spD
        self.evs[5] = self.evs[5] + spe

        for ev in self.evs:
            if ev > 252:
                print('Reached max EV for attribute:', self.evs.index(ev))
                ev = 252

        self.calcStats()
        self.stats = self.calcStats(self.lvl)

    def evolve(self, name=''):
        if name == '':
            self.dexID = self.dexID+1
            self.name = SheetCommands.getNameFromID(self.dexID)
        else:
            self.name = name
        
        # Get new base stats
        self.baseHp = SheetCommands.getBaseHp(self.name)
        self.baseAtk = SheetCommands.getBaseAtk(self.name)
        self.baseDef = SheetCommands.getBaseDef(self.name)
        self.baseSpA = SheetCommands.getBaseSpA(self.name)
        self.baseSpD = SheetCommands.getBaseSpD(self.name)
        self.baseSpe = SheetCommands.getBaseSpe(self.name)
        # New stats from 1-100Lvl
        self.calcStats()
        self.stats = self.calcStats(self.lvl)
        # Atributes that can change from evolution
        self.type = SheetCommands.getType(self.name)

    def setNature(self, nature=''):
            natures = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky']
            if nature == '':
                self.nature = natures[np.random.randint(0, 24)]
            else:
                self.nature = nature

    def getShiny(self):
        ran = np.random.randint(4096)
        if ran == 0:
            print('OFMGFOUND SHINYSDFSKJDFHSJKDF, ' + self.name + ', ' +self.uniqueID)
            return 1
        else:
            return 0
        
