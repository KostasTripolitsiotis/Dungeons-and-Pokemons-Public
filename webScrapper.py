from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
PATH = 'C:/WebDriver/bin/chromedriver.exe'
import numpy as np

TYPES = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy'] 
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
service = ChromeService(executable_path=PATH)

driver = webdriver.Chrome(options)
driver.minimize_window()

def getURL(name):
    return 'https://bulbapedia.bulbagarden.net/wiki/'+name+'_(Pok%C3%A9mon)/Generation_VIII_learnset'

def findMovesTable(driver:webdriver.Chrome, movegroup):
    index=1
    text = []
    while True:
        try:
            elem = driver.find_element(By.XPATH, """//*[@id="mw-content-text"]/div/table["""+str(index)+"""]/tbody/tr[2]/td/table""")
            text = elem.text
            text = text.splitlines()
            for i in range(len(text)):
                text[i] = text[i].split(' ')
            if text[0][1] == movegroup:
                text.pop(0)
                break
        except Exception:
            0
        index +=1
    return text

def getMoves(table, lvl):
    moveset = []

    for row in table:
        if row[0] == 'Evo.':
            row[0] = 1
        if int(row[0]) > lvl:
            break
        moveset.append(row)

    return moveset

def getMoveset(name, *, moves = 'level', lvl=5):
    url = getURL(name)
    driver.get(url)

    table = []
    if moves == 'level':
        table = findMovesTable(driver, 'Level')

    moveset = getMoves(table, lvl)
    
    while len(moveset) > 4:
        moveset.pop(np.random.randint(len(moveset)))

    for move in moveset:
        move.pop(0)
        check = any(item in move[2] for item in TYPES)
        if check:
            move[0:2] = [' '.join(move[0:2])]
        move[1:3] = [' '.join(move[1:3])]
    
    return moveset
