import numpy as np

MAX_LEVEL = 200

atkP = ['Lonely', 'Brave', 'Adamant', 'Naughty']
atkD = ['Bold', 'Timid', 'Modest', 'Calm']
defP = ['Bold', 'Relaxed', 'Impish', 'Lax']
defD = ['Lonely', 'Hasty', 'Mild', 'Gentle']
spAP = ['Modest', 'Mild', 'Quiet', 'Rash']
spAD = ['Adamant', 'Impish', 'Jolly', 'Careful']
spDP = ['Calm', 'Gentle', 'Sassy', 'Careful']
spDD = ['Naughty', 'Lax', 'Naive', 'Rash']
speP = ['Timid', 'Hasty', 'Jolly', 'Naive']
speD = ['Brave', 'Relaxed', 'Quiet', 'Sassy']

class Func:
    @staticmethod
    def baseNormalized(base):
        return np.floor(base * (30-6)/200) +7

    @staticmethod
    def ivNormalized(iv):
        return np.floor(iv * (20/30))

    @staticmethod
    def evNormalized(ev):
        return np.floor(ev * (40/255))

    @staticmethod
    def calcStat(base, iv, ev):
        lvl=np.arange(1, MAX_LEVEL+1, 1) 
        baseN = Func.baseNormalized(base)
        ivN = Func.ivNormalized(iv)
        evN = Func.evNormalized(ev)
        return np.floor(0.01 * (2 * baseN + ivN + np.floor(0.25 * evN)) * lvl) + 5

    @staticmethod
    def calcHealth(base, iv, ev):
        lvl=np.arange(1, MAX_LEVEL+1, 1)
        baseN = Func.baseNormalized(base)
        ivN = Func.ivNormalized(iv)
        evN = Func.evNormalized(ev)
        return np.floor(0.01 * (2 * baseN + ivN + np.floor(0.25 * evN)) * lvl) + lvl + 10

    @staticmethod
    def calcAtk(base, iv, nature, ev):
        nature_modifier = 1
        if (nature in atkP):
            nature_modifier = 1.1
        elif (nature in atkD):
            nature_modifier = 0.9
        return Func.calcStat(base, iv, ev) * nature_modifier

    @staticmethod
    def calcDef(base, iv, nature, ev):
        nature_modifier = 1
        if (nature in defP):
            nature_modifier = 1.1
        elif (nature in defD):
            nature_modifier = 0.9
        return Func.calcStat(base, iv, ev) * nature_modifier

    @staticmethod
    def calcSpA(base, iv, nature, ev):
        nature_modifier = 1
        if (nature in spAP):
            nature_modifier = 1.1
        elif (nature in spAD):
            nature_modifier = 0.9
        return Func.calcStat(base, iv, ev) * nature_modifier

    @staticmethod
    def calcSpD(base, iv, nature, ev):
        nature_modifier = 1
        if (nature in spDP):
            nature_modifier = 1.1
        elif (nature in spDD):
            nature_modifier = 0.9
        return Func.calcStat(base, iv, ev) * nature_modifier

    @staticmethod
    def calcSpe(base, iv, nature, ev):
        nature_modifier = 1
        if (nature in speP):
            nature_modifier = 1.1
        elif (nature in speD):
            nature_modifier = 0.9
        return Func.calcStat(base, iv, ev) * nature_modifier

    @staticmethod
    def moveStat(move, poke):
        stat = move[1].split()[1]
        if stat == 'Special' or stat == 'Physical':
            return stat
        else:
            if poke.stats[2] > poke.stats[4]:
                return 'Physical'
            else:
                return 'Special'

    @staticmethod
    def checkifProf(move, poke):
        movetype = move[1].split()[0]
        if movetype in poke.type:
            return True
        else:
            return False
        
    @staticmethod
    def getProfBonus(poke) -> int:
        if poke.lvl <= 20:
            return 2
        elif poke.lvl <= 40:
            return 3
        elif poke.lvl <= 60:
            return 4 
        elif poke.lvl <= 80:
            return 5
        else: return 6

    @staticmethod
    def getAccModifier(move):
        modifier = 0
        acc = move[3].replace('%','')
        if acc != '—':
            acc = 100 - int(acc)
            if acc !=0:
                modifier = int(acc/5)
        return modifier
    
    @staticmethod
    def getAccDice(move, poke) -> str:
        modifier = Func.getAccModifier(move)*(-1)
        dice = '1d20'
        
        stat = Func.moveStat(move, poke)
        if stat == 'Physical':
            modifier = modifier + int(np.floor(poke.stats[2]-10)/2)
        else:
            modifier = modifier + int(np.floor(poke.stats[4]-10)/2)
        
        if Func.checkifProf(move, poke):
            prof = Func.getProfBonus(poke)
            modifier += prof
            
        if modifier > 0:
            dice = dice+'+'+str(modifier)
        elif modifier < 0:
            dice = dice+str(modifier)
        return dice
    
    @staticmethod
    def getDamageDiceBonus(move, poke) -> str:
        stat = Func.moveStat(move, poke)
        dice = Func.getDamageDice(move)
        
        if stat == 'Physical':
            modifier = int(np.floor(poke.stats[2]-10)/2)
        else:
            modifier = int(np.floor(poke.stats[4]-10)/2)
            
        if modifier > 0:
            dice = dice+'+'+str(modifier)
        elif modifier < 0:
            dice = dice+str(modifier)

        return dice
      
    @staticmethod      
    def getDamageDice(move):
        dices = ''
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
    
    