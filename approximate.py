from random import uniform

totalDots = 0
circleDots = 0
radius = 100.0

for i in range(0, int(3.14 * 10 ** 7)): # :P
    #random.uniform(a, b)
    x = uniform(-100.0, 100.0)
    y = uniform(-100.0, 100.0)
    totalDots += 1
    if x ** 2 + y ** 2 < radius ** 2: #If it's within the circle
        circleDots += 1

print("Total Dots: %s\nCircle Dots: %s" % (totalDots, circleDots))
pi = 4.0 * circleDots / totalDots
print(pi)
