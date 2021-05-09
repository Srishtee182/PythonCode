# 3 and half liter - play water.mp3 file 10am to 7 pm - to close done - text file me timestamp generate krenge at what time person drank water
# every 30 min eyes excercise eyes.mp3 file  - to close eyedone - timer reset - log generate
# every 2 hours physical excercise physical.mp3 file - to close exdone
# pygame module to play mp3

from playsound import playsound
from datetime import datetime
from time import time
from pygame import mixer

def musicplay(file, stopper):
    #   playsound(file)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def takelog(msg):
    with open("mylogsforwater.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':

    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watersecs = 40*60
    eyessecs = 90*60
    excercisesecs =120*60
    while True:
        if time() - init_water>watersecs:
            print("Please drink water, when done please enter 'DRANK' to stop the alarm")
            musicplay("Gargling-Water.mp3", "DRANK")
            init_water = time()
            takelog("Drank water at ")

            if time() - init_eyes > eyessecs:
                print("Please Do Eyes excercise, when done please enter 'Done' to stop the alarm")
                musicplay("Cartoon-eye-blink-sound-effect-free-download.mp3", "Done")
                init_eyes = time()
                takelog("Eyes excercise at ")
            if time() - init_excercise > excercisesecs:
                print("Please Do excercise, when done please enter 'Excercise Done' to stop the alarm")
                musicplay("motivation.mp3", "Excercise Done")
                init_excercise = time()
                takelog("excercise at ")
