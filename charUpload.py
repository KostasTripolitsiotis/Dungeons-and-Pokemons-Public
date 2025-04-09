import pyautogui as ag
import time
import numpy as np
from sheetInfo import SheetCommands
import pokemon as pk
from  statFunctions import Func

SCREE2 = True

# def moveStat(move, poke):
#     stat = move[1].split()[1]
#     if stat == 'Special' or stat == 'Physical':
#         return stat
#     else:
#         if poke.stats[2] > poke.stats[4]:
#             return 'Physical'
#         else:
#             return 'Special'

# def checkifProf(move, poke):
#     movetype = move[1].split()[0]
#     if movetype in poke.type:
#         return True
#     else:
#         return False

# def getAccModifier(move):
#     modifier = 0
#     acc = move[3].replace('%','')
#     if acc != '—':
#         acc = 100 - int(acc)
#         if acc !=0:
#             modifier = int(acc/5)
#     return modifier
        
# def getDamageDice(move):
#     dices = ''
#     if move[2] != '—':
#         power = int(int(move[2])/5)
#         dice=10
#         while power > 0 and dice > 0:
#             r = int(np.floor(power/dice))
#             power = power - r*dice
#             if r != 0:
#                 dices = dices+str(r)+'d'+str(dice)
#                 if power != 0:
#                     dices = dices+'+'
#             dice = dice - 1

#     return dices

def createCharachter(xoffset):
    ###Click on create charachter
    ag.moveTo(xoffset+1645, 210, duration = 0.5)
    ag.click()
    pass

def uploadImg(xoffset, name, yoffset):
    index = SheetCommands.getDexID(name)
    ###Click on Avatar-Click to Upload
    ag.moveTo(xoffset+760, 380, duration=0.5)
    ag.click()
    time.sleep(0.5)
    #Click on directory and go to pokemon sprites
    ag.moveTo(xoffset+650, 55, duration=0.2)
    ag.click()
    ag.typewrite('D:\Dungeons and Pokemons\pokemon sprites\n')
    #Type pokemon dex id on file name
    ag.moveTo(xoffset+420, 475, duration=0.2)
    ag.click()
    ag.typewrite(str(index)+'.png')

    #Open and wait for upload
    ag.moveTo(xoffset+790, 510, duration=0.2)
    ag.click()
    time.sleep(5)

    ###Upload on default Token
    ag.moveTo(xoffset+730, 550, duration=0.2)
    ag.click()
    time.sleep(0.5)
    #Click on directory and go to pokemon sprites
    ag.moveTo(xoffset+650, 55, duration=0.2)
    ag.click()
    ag.typewrite('D:\Dungeons and Pokemons\pokemon sprites\n')
    #Type pokemon dex id on file name
    ag.moveTo(xoffset+420, 475, duration=0.2)
    ag.click()
    ag.typewrite(str(index)+'.png')

    #Open and wait for upload
    ag.moveTo(xoffset+790, 510, duration=0.2)
    ag.click()
    time.sleep(5)

def initSetup(xoffset, poke):
    ###Click on nameplate and write name, save changes
    ag.moveTo(xoffset+950, 275, duration = 0.5)
    ag.tripleClick()
    charName = poke.name+' '+poke.trainer
    ag.typewrite(charName)
    #Save Changes
    ag.moveTo(xoffset+1180, 830, duration = 0.5)
    ag.click()
    time.sleep(5)

def setupClass(xoffset, poke):
    #Click on sheet settings
    ag.moveTo(xoffset+1280, 445, duration=0.5)
    ag.click()
    ag.scroll(-500)

    #Use custom class
    ag.moveTo(xoffset+553, 450, duration=0.5)
    ag.click()
    ag.moveRel(90, 25, duration=0.2)
    ag.click()
    ag.typewrite(poke.name)
    #Return to CORE sheet
    ag.scroll(500)
    ag.moveTo(xoffset+1150, 445, duration=0.5)
    ag.click()

    #Calculate and write pokemon CR level
    level = int(np.ceil(poke.lvl/5))
    ag.moveTo(xoffset+1280, 350, duration=0.3)
    ag.tripleClick()
    ag.typewrite(str(level))
    #Click outside of level box
    ag.moveRel(0, -50)
    ag.click()

def putStats(xoffset, poke, yoffset):
    #Scroll down and put stats
    ag.scroll(-200)
    #Move to strength
    ag.moveTo(xoffset+575, yoffset+353, duration = 0.5)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[2]))

    ag.moveRel(0, 82, duration = 0.2)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[6]))

    ag.moveRel(0, 82, duration = 0.2)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[1]))

    ag.moveRel(0, 82, duration = 0.2)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[5]))

    ag.moveRel(0, 82, duration = 0.2)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[3]))

    ag.moveRel(0, 82, duration = 0.2)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[4]))

def putHitpoints(xoffset, poke, yoffset):
    #Hit points
    ag.moveTo(xoffset+950, yoffset+370, duration = 0.5)
    ag.doubleClick()
    ag.typewrite(str(poke.stats[0]))

    ag.moveRel(0, 40, duration = 0.5)
    ag.click()
    time.sleep(0.5)
    ag.typewrite(str(poke.stats[0]))

    #Click outside of hit points box
    ag.moveRel(100, 0)
    ag.click()

def putRecources(xoffset, poke, yoffset):
    #Move to sheet recources
    ag.scroll(-400)
    
    ###Calculate and place ACs
    #Physical AC
    ag.moveTo(xoffset+1100, yoffset+460, duration=0.2)
    ac=10+int(np.floor((poke.stats[3]-10)/2))
    ag.click()
    ag.typewrite('Physical AC')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    ag.typewrite(str(ac))

    #Special AC
    ag.moveTo(xoffset+1240, yoffset+460, duration=0.5)
    ac=10+int(np.floor((poke.stats[5]-10)/2))
    ag.click()
    ag.typewrite('Special AC')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    ag.typewrite(str(ac))

    #Add recources
    ag.moveRel(100, 0)
    ag.click()
    ag.moveTo(xoffset+1060, yoffset+480, duration=0.4)
    ag.click()

    #Attack
    ag.moveTo(xoffset+1100, yoffset+540, duration=0.2)
    ag.click()
    ag.typewrite('Attack')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    time.sleep(0.1)
    ag.typewrite(str(poke.stats[2]))

    #Special Attack
    ag.moveTo(xoffset+1240, yoffset+540, duration=0.2)
    ag.click()
    time.sleep(0.1)
    ag.typewrite('Sp. Attack')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    time.sleep(0.1)
    ag.typewrite(str(poke.stats[4]))

    #Add recources
    ag.moveRel(100, 0)
    ag.click()
    ag.moveTo(xoffset+1060, yoffset+560, duration=0.4)
    ag.click()

    #Speed
    ag.moveTo(xoffset+1100, yoffset+617, duration=0.2)
    ag.click()
    time.sleep(0.1)
    ag.typewrite('Speed')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    time.sleep(0.1)
    ag.typewrite(str(poke.stats[4]))

    #Level
    ag.moveTo(xoffset+1240, yoffset+617, duration=0.2)
    ag.click()
    time.sleep(0.1)
    ag.typewrite('Level')
    ag.moveRel(0, -20, duration=0.5)
    ag.click()
    time.sleep(0.1)
    ag.typewrite(str(poke.lvl))

    #Add recources
    ag.moveRel(100, 0)
    ag.click()
    ag.moveTo(xoffset+1060, yoffset+640, duration=0.4)
    ag.click()

    #Moves
    i=0
    for move in poke.moveset:
        x=0
        y=0
        match i:
            case 0:
                x=1100
                y=698
            case 1:
                x=1240
                y=698
            case 2:
                #Add recources
                ag.moveRel(100, 0)
                ag.click()
                ag.moveTo(xoffset+1060, yoffset+720, duration=0.4)
                ag.click()
                x=1100
                y=775
            case 3:
                x=1240
                y=775
        ag.moveTo(xoffset+x, yoffset+y, duration=0.2)
        ag.click()
        time.sleep(0.1)
        ag.typewrite(move[0])
        ag.moveRel(0, -20, duration=0.5)
        ag.click()
        time.sleep(0.1)
        ag.typewrite(move[4])
        ag.moveRel(0, -20, duration=0.5)
        ag.click()
        time.sleep(0.1)
        ag.typewrite(move[4])

        i=i+1
    ag.moveRel(100, 0)
    ag.click()

def putTraits(xoffset, poke, yoffset):
    ag.scroll(-1000)
    #Add Trait
    ag.moveTo(xoffset+1065, yoffset+390, duration=0.2)
    ag.click()
    time.sleep(0.2)

    #Nature
    ag.moveRel(50, 0, duration=0.4)
    ag.click()
    ag.typewrite(poke.nature)
    ag.moveRel(30, 30, 0.2)
    ag.click()
    time.sleep(0.2)
    ag.typewrite('Nature')
    ag.moveRel(135, -35, duration=0.2)
    ag.click()

    #Gender
    ag.moveRel(-212, 45, duration=0.4)
    ag.click()
    time.sleep(0.2)
    ag.moveRel(50, 0, duration=0.2)
    ag.click()
    ag.typewrite(poke.gender)
    ag.moveRel(30, 30, 0.2)
    ag.click()
    time.sleep(0.2)
    ag.typewrite('Gender')
    ag.moveRel(135, -35, duration=0.4)
    ag.click()

    #Ability
    ag.moveRel(-212, 45, duration=0.4)
    ag.click()
    time.sleep(0.2)
    ag.moveRel(50, 0, duration=0.2)
    ag.click()
    ag.typewrite(poke.ability)
    ag.moveRel(30, 30, 0.2)
    ag.click()
    time.sleep(0.2)
    ag.typewrite('Ability')
    ag.moveRel(135, -35, duration=0.2)
    ag.click()

    #Type
    ag.moveRel(-215, 45, duration=0.4)
    ag.click()
    time.sleep(0.2)
    ag.moveRel(50, 0, duration=0.2)
    ag.click()
    for type in poke.type:
        ag.typewrite(type+' ')
    ag.moveRel(30, 35, 0.2)
    ag.click()
    time.sleep(0.1)
    ag.typewrite('Type')
    ag.moveRel(130, -35, duration=0.2)
    ag.click()

    #EggGroup
    ag.moveRel(-215, 45, duration=0.4)
    ag.click()
    time.sleep(0.2)
    ag.moveRel(50, 0, duration=0.2)
    ag.click()
    for group in poke.eggGroup:
        ag.typewrite(group+' ')
    ag.moveRel(30, 30, 0.2)
    ag.click()
    time.sleep(0.1)
    ag.typewrite('Egg Group')
    ag.moveRel(130, -35, duration=0.2)
    ag.click()

    #UniqueID
    ag.moveRel(-212, 45, duration=0.4)
    ag.click()
    time.sleep(0.2)
    ag.moveRel(50, 0, duration=0.2)
    ag.click()
    ag.typewrite(str(poke.uniqueID))
    ag.moveRel(30, 30, 0.2)
    ag.click()
    time.sleep(0.2)
    ag.typewrite('Unique ID')
    ag.moveRel(135, -35, duration=0.2)
    ag.click()

    #Shiny
    if poke.shiny == 1:
        ag.moveRel(-212, 45, duration=0.4)
        ag.click()
        ag.moveRel(50, 0, duration=0.2)
        ag.click()
        ag.typewrite('SHONYY')
        ag.moveRel(160, 0, 0.2)
        ag.click()

def putMoves(xoffset, poke, yoffset):
    #Setup height of ATTACKS & SPELLCASTING box
    ag.scroll(5000)
    ag.scroll(-400)

    #Add Attack
    i=0
    test = True
    for move in poke.moveset:
        x=0
        y=0
        if move[0] == '—':
            continue
        #Use different x, y for different moves
        match i:
            case 0:
                x=815
                y=490
            case 1:
                x=815
                y=510
            case 2:
                #test = False
                x=815
                y=530
            case 3:
                x=815
                y=550
        
        if test == False: continue
        #Add Attack
        #Click ADD symbod
        ag.moveTo(xoffset+x, yoffset+y)
        time.sleep(0.2)
        ag.click()
        #Write Attack's Name
        ag.moveRel(50, 0, duration=0.5)
        time.sleep(0.2)
        ag.click()
        time.sleep(0.2)
        ag.typewrite(move[0])

        #Check if move uses ATK, CHA
        stat = Func.moveStat(move, poke)
        if stat == 'Special':
            #Change attack from using STR to use CHA
            ag.moveRel(5, 20, duration=0.5)
            time.sleep(0.2)
            ag.click()
            ag.moveRel(0, 95, duration=0.5)
            time.sleep(0.2)
            ag.click()
            ag.moveRel(-5, -115, duration=0.1)

        #Check if move is STAB
        if Func.checkifProf(move, poke) == False:
            ag.moveRel(70, 20, duration=0.2)
            ag.click()
            ag.moveRel(-70, -20, duration=0.2)

        #Change Accuracy modifier if exists
        accModifier = Func.getAccModifier(move)
        if accModifier != 0:
            ag.moveRel(45, 20, duration=0.5)
            time.sleep(0.2)
            ag.click()
            time.sleep(0.2)
            ag.typewrite('-'+str(accModifier))
            ag.moveRel(-45, -20, duration=0.2)

        #Setup Damage Dice Rolls
        dmgDice = Func.getDamageDice(move)
        if dmgDice != '':
            ag.moveRel(0, 80, duration=0.5)
            time.sleep(0.2)
            ag.click()
            time.sleep(0.3)
            ag.typewrite(dmgDice)
            if stat == 'Special':
                ag.moveRel(62, 0, duration=0.5)
                ag.click()
                ag.moveRel(0, 95, duration=0.5)
                ag.click()
                ag.moveRel(-62, -95)
            ag.moveRel(0, -80, duration=0.2)

        #Write if its physical or special and the type
        ag.moveRel(0, 100, duration=0.1)
        time.sleep(0.2)
        ag.click()
        time.sleep(0.3)
        ag.typewrite(move[1])
        ag.moveRel(0, -100, duration=0.1)
        
        #Finish Setting up move
        ag.moveRel(160, 0, duration=0.3)
        ag.click()

        i = i+1

def placeToken(xoffset):
    ###put token on map
    ag.moveTo(xoffset+1650, 235, duration = 0.5)
    ag.keyDown('alt')
    ag.mouseDown(button='left')
    ag.moveTo(2275, 420, duration=0.5)
    ag.mouseUp(button='Left')
    ag.keyUp('alt')
    time.sleep(0.5)
    ag.click()

def setupToken(xoffset, yoffset):
    ####Setup token
    #Click On Token Settings
    ag.moveRel(-60, 80, duration = 0.5)
    ag.click()
    #Click on Nameplate
    ag.moveRel(563, yoffset+-70, duration = 0.5)
    ag.click()
    #Click on General-See
    ag.moveRel(55, -145, duration = 0.5)
    ag.moveRel(-138, 75, duration = 0.5)
    ag.click()
    #Click on see Bar 1
    ag.moveRel(475, 0, duration = 0.5)
    ag.moveRel(-145, 63, duration = 0.5)
    ag.click()
    #Search attributes
    ag.moveRel(30, -65, duration = 0.5)
    ag.click()
    ag.typewrite('h')
    #Find health
    ag.moveRel(0, 200, duration = 0.5)
    ag.scroll(-400)
    ag.moveRel(0, 20, duration = 0.5)
    ag.click()

def finishSetup(xoffset, poke, yoffset):
    ###Save and close
    ag.moveTo(xoffset+1230, yoffset+780, duration = 0.5)
    ag.click()
    #Click on edit
    ag.moveTo(xoffset+1300, yoffset+170, duration = 0.5)
    ag.click()
    #Upload Avatar and Default Token
    uploadImg(xoffset, poke.name, yoffset)
    #Use selected token
    ag.moveTo(xoffset+730, 690, duration = 0.5)
    ag.click()
    time.sleep(0.2)
    ag.press('del')
    #Save Changes
    ag.moveTo(xoffset+1180, 830, duration = 0.5)
    ag.click()
    #Close and remove token
    ag.moveTo(xoffset+1390, yoffset+170, duration = 0.5)
    ag.click()
    time.sleep(3)

def charUpload(poke):
    xoffset=0
    yoffset = 20
    if SCREE2 == True:
        xoffset=1920

    #Click on create charachter
    createCharachter(xoffset)

    #Click on nameplate and write name, save changes
    initSetup(xoffset, poke)

    #Setup Class
    setupClass(xoffset, poke)

    #Scroll down and put stats
    putStats(xoffset, poke, yoffset)

    #Hit points
    putHitpoints(xoffset, poke, yoffset)

    #Put AC
    putRecources(xoffset, poke, yoffset)

    #Put Traits
    putTraits(xoffset, poke, yoffset)

    #Put Moves
    putMoves(xoffset, poke, yoffset)

    #Put token on map
    placeToken(xoffset)

    #Setup token
    setupToken(xoffset, yoffset)
 
    ###Save and close
    finishSetup(xoffset, poke, yoffset)

# poke = pk.Pokemon('Gastly')
# charUpload(poke)

