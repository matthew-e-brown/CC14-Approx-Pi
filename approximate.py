import time
from random import uniform
from threading import Thread

totalDots = 0
circleDots = 0
radius = 100.0

numThreads = 8;
done = 0;

timeStart = time.time()

def chunk():
    global totalDots, circleDots, radius, done
    addedDots = 0
    inCircle = 0
    for i in range(0, 8 * 10 ** 6):
        #random.uniform(a, b) -- returns a random float
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        addedDots += 1
        if x ** 2 + y ** 2 < radius ** 2: #If it's within the circle
            inCircle += 1
    # Add them all up at the end
    totalDots += addedDots
    circleDots += inCircle
    done += 1
    print("Thread #%s Complete, at %s seconds!" % (done, str(round(time.time() - timeStart, 2))))

threads = []

for i in range(0, numThreads):
    threads.append( Thread(target = chunk, args = ()) )
    threads[i].start()

print("Thread Initialization Complete!")

finished = False
while not finished:
    if done == numThreads:
        print("Total Dots: %s\nDots within the Circle: %s"
            % ("{:,}".format(totalDots), "{:,}".format(circleDots))
        )
        pi = 4.0 * circleDots / totalDots
        print(pi)
        finished = True
