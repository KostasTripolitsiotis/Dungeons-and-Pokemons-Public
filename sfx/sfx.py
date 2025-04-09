from pydub import AudioSegment, utils
from pydub.playback import play
import sys
import os
FPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(FPATH[0])
from constants.directories import Directory
import random

ENABLE = True

#Find path of ffmpeg bins
AudioSegment.converter = os.path.join(Directory.FFMPEG_BIN, "ffmpeg.exe")
utils.get_prober_name = lambda: os.path.join(Directory.FFMPEG_BIN, "ffprobe.exe")
utils.get_player_name = lambda: os.path.join(Directory.FFMPEG_BIN, "ffplay.exe")

class Sfx:
    @staticmethod
    def play_button_ran():
        if ENABLE:
            dir = os.listdir(os.path.join(Directory.SFX, "button_click"))
            
            mp3_file = random.choice(dir)
            audio = AudioSegment.from_mp3("D:\\Dungeons and Pokemons\\Stat generator\\sfx\\button_click\\"+mp3_file)
            play(audio)

    @staticmethod
    def play_button_click():
        if ENABLE:
            audio = AudioSegment.from_mp3("D:\\Dungeons and Pokemons\\Stat generator\\sfx\\button_click\\app button click sound.mp3")
            play(audio)