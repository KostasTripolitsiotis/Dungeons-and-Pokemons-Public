from pydub import AudioSegment, utils
from pydub.playback import play
from multiprocessing import Process
import os 
import random

AudioSegment.converter = "C:\\PATH_Programs\\ffmpeg.exe"
utils.get_prober_name = lambda: "C:\\PATH_Programs\\ffprobe.exe"
utils.get_player_name = lambda: "C:\\PATH_Programs\\ffplay.exe"

dir = os.listdir("D:\\Dungeons and Pokemons\\Stat generator\\sfx\\button_click")



def play_button():
    mp3_file = random.choice(dir)
    audio = AudioSegment.from_mp3("D:\\Dungeons and Pokemons\\Stat generator\\sfx\\button_click\\"+mp3_file)
    play(audio)


if __name__ == "__main__":
    proc = []
    for _ in range(2):
        p = Process(target=play_button())
        proc.append(p)
        p.start()
    
    p = Process(target=play_button())
    proc.append(p)
    p.start()