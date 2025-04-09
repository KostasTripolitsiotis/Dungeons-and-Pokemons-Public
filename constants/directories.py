import os
from constants.googleSheet import SheetName

# Directories
class Directory:
    __MAINPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    __SAVEFILES = os.path.join(__MAINPATH, "savefiles")
    LEADERS_GEN1 = os.path.join(__SAVEFILES, "Gym Leaders", "gen1.pkl")
    LEADERS_GEN4 = os.path.join(__SAVEFILES, "Gym Leaders", "gen4.pkl")
    PLAYERS = os.path.join(__SAVEFILES, "players.pkl")
    NPCS = os.path.join(__SAVEFILES, "npcs.pkl")
    WILD_POKEMON = os.path.join(__SAVEFILES, "wildpokemon.pkl")
    BACKUPS = os.path.join(__SAVEFILES, "backups")
    MASTERSHEET = os.path.join(__SAVEFILES, "master_sheet.pkl")
    SYNC_LOGS = os.path.join(__SAVEFILES, "synclogs")
    TEST = os.path.join(__SAVEFILES, 'test_pokemon.pkl')
    SFX = os.path.join(__MAINPATH, "sfx")
    FFMPEG_BIN = os.path.join(SFX, "ffmpeg-6.1.1-essentials_build", "bin")
    
class Filenames:
    PlAYERS = "players.pkl"
    LEADERS_GEN1 = "gen1.pkl"
    LEADERS_GEN4 = "gen4.pkl"
    NPCS = "npcs.pkl"
    WILD_POKEMON = "wildpokemon.pkl"
    MASTERSHEET = "master_sheet.pkl"
    TEST = 'test_pokemon.pkl'


FILES = ['wildpokemon', 'players', 'npcs', 'gen4', 'test_pokemon']

PathToSheet = {
    Directory.WILD_POKEMON : SheetName.WILDSPAWNS,
    Directory.PLAYERS : SheetName.PLAYERS,
    Directory.NPCS : SheetName.NPCS,
    Directory.LEADERS_GEN4 : SheetName.GYMLEADERS,
    Directory.LEADERS_GEN1 : SheetName.GYMLEADERS,
    Directory.TEST : SheetName.TEST
}

FilenameToSheet = {
    Filenames.PlAYERS : SheetName.PLAYERS,
    Filenames.LEADERS_GEN1 : SheetName.GYMLEADERS,
    Filenames.LEADERS_GEN4 : SheetName.GYMLEADERS,
    Filenames.NPCS : SheetName.NPCS,
    Filenames.WILD_POKEMON : SheetName.WILDSPAWNS,
    Filenames.TEST : SheetName.TEST
}

FilenameToPath = {
    Filenames.PlAYERS : Directory.PLAYERS,
    Filenames.LEADERS_GEN1 : Directory.LEADERS_GEN1,
    Filenames.LEADERS_GEN4 : Directory.LEADERS_GEN4,
    Filenames.NPCS : Directory.NPCS,
    Filenames.WILD_POKEMON : Directory.WILD_POKEMON,
    Filenames.TEST : Directory.TEST
}
