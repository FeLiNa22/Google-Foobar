import random

def solution(x, y):
    m, f, gen = int(x), int(y), 0
    while(True):
        if(m == 1 and f == 1):
            return str(gen);
        elif(m < 1 or f < 1 or m==f):
            return "impossible"
        elif(m == 1 or f == 1):
            return str(gen + f * m - 1)
        elif(m > f):
            gen += int(m/f);
            m -= f * int(m/f);
        elif(m < f):
            gen += int(f/m);
            f -= m * int(f/m);
print(solution(random.getrandbits(1280),random.getrandbits(1281)))