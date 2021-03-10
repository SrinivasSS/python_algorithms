import random
import time

max = 600
min = 1
rand = random.randint(1,max)
half = round(max/2)
print("Random# ",rand)
while True:
    print("Current Guess: ",half)
    if half == rand:
        print("Correct guess!")
        break
    elif (max - min) == 2:
        newhalf == max - 1
    elif (rand - half) > 0:
        print("Guess higher!")
        min = half
    elif (rand - half) < 0:
        print("Guess lower!")
        max = half
    newhalf = round((min+max)/2)
    half = newhalf
    time.sleep(1)