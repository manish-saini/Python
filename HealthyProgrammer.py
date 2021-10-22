# from pygame import mixer
# from datetime import datetime
# from time import time
# def musiconloop(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         a=input()
#         if a ==stopper:
#             mixer.music.stop()
#             break

# def log_now(msg):
#     with open("mylogs.txt","a") as f:
#         f.write(f"{msg} {datetime.now()} \n")

# if __name__=='__main__':
#     musiconloop("Water.mp3","stop")
#     init_water=time() 
#     init_eyes=time() 
#     init_exercise=time()

#     watersecs=5
#     exsecs=10
#     eyessecs=20


#     while True:
#         if time()-init_water>watersecs:
#             print("Watre Drinking time, Enter 'drank' to stop the alarm")
#             musiconloop('Water.mp3','drank')
#             init_water=time()
#             log_now("Drink water at ")
        
#         if time()-init_eyes>eyessecs:
#             print("Watre Drinking time, Enter 'drank' to stop the alarm")
#             musiconloop('Water.mp3','drank')
#             init_eyes=time()
#             log_now("Eye Exercise  at ")

#         if time()-init_exercise>exsecs:
#             print("Watre Drinking time, Enter 'drank' to stop the alarm")
#             musiconloop('Water.mp3','drank')
#             init_exercise=time()
#             log_now("Exercise at ")

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("Water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('Water.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('Water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")
