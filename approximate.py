from random import uniform
from threading import Thread

totalDots = 0
circleDots = 0
radius = 100.0

def chunk():
    global totalDots, circleDots, radius
    for i in range(0, 5 * 10 ** 5): # :P
        #random.uniform(a, b)
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        totalDots += 1
        if x ** 2 + y ** 2 < radius ** 2: #If it's within the circle
            circleDots += 1

threads = []

for i in range(0, 15):
    threads.append( Thread(target = chunk, args = ()) )
    threads[i].start()
    if i == 14: threads[i].join() #Only wait for the last thread to finish

print("Total Dots: %s\nCircle Dots: %s" % (totalDots, circleDots))
pi = 4.0 * circleDots / totalDots
print(pi)
