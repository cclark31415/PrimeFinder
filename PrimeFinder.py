import numpy as np
import time

def formatTime(secs):
    if secs <= 60:
        return str(secs)
    else:
        days = secs//86400
        hours = (secs - days*86400)//3600
        minutes = (secs - days*86400 - hours*3600)//60
        seconds = secs - days*86400 - hours*3600 - minutes*60
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
        return result

n = int(input("What number should I go up to?\n"))
p = 2
primes = []
squares = {}
start = time.time()
s2 = int(np.sqrt(n + 1))
for s in range(3, s2):
    squares[s] = s**2

print ("Squares\n" + str(squares))
print ("Number of squares:  " + str(len(squares)))

for p in range(2, n + 1):
    if p not in squares:
        for i in range(2, p):        
            if p % i == 0:
                break
        else:
            primes.append(p)

stop = time.time()

print ("Primes\n" + str(primes))
print ("Number of primes:  " + str(len(primes)))
print (formatTime(stop - start))
