#coding=utf8
#Wei Guannan <kiss.kraks@gmail.com>

import copy
import random
from colorama import Fore, Back

def reduceLineLeft(xs): 
    def aux(acc, y):
        if len(acc) == 0:
            acc.append(y)
        elif acc[len(acc)-1] == y and acc[len(acc)-1] != 0 and y != 0:
            acc[len(acc)-1] = acc[len(acc)-1] + y
            acc.append(0)
        elif y != 0:
            acc.append(y)
        #print acc
        return acc
    res = filter(lambda x: x!=0, reduce(aux, xs, []))
    res.extend([0 for i in range(0, 4-len(res))])
    return res

def reduceLineRight(xs):
    return reduceLineLeft(xs[::-1])[::-1]

def reduceLeft(a):
    return map(lambda x: reduceLineLeft(x), a)

def reduceRight(a):
    return map(lambda x: reduceLineRight(x), a)

def reduceUp(a):
    return rotate(reduceLeft(rotate(a)))

def reduceDown(a):
    return rotate(reduceRight(rotate(a)))

def rotate(a):
    def auxset(i, j): b[j][i] = a[i][j]
    b = newEmpty(len(a))
    map(lambda i: map(lambda j: auxset(i, j), range(0, len(a[i]))), range(0, len(a)))
    return b

def prettyPrint(a):
    def color(x):
        if x == 0:    return Fore.RESET + Back.RESET
        if x == 2:    return Fore.RED + Back.RESET
        if x == 4:    return Fore.GREEN + Back.RESET
        if x == 8:    return Fore.YELLOW + Back.RESET
        if x == 16:   return Fore.BLUE + Back.RESET
        if x == 32:   return Fore.MAGENTA + Back.RESET
        if x == 64:   return Fore.CYAN + Back.RESET
        if x == 128:  return Fore.RED + Back.BLACK
        if x == 256:  return Fore.GREEN + Back.BLACK
        if x == 512:  return Fore.YELLOW + Back.BLACK
        if x == 1024: return Fore.BLUE + Back.BLACK
        if x == 2048: return Fore.MAGENTA + Back.BLACK
        if x == 4096: return Fore.CYAN + Back.BLACK
        if x == 8192: return Fore.WHITE + Back.BLACK
    for i in a:
        for j in i:
            print color(j) + ("%4d" % j) + Fore.RESET + Back.RESET,
        print

def newEmpty(size):
    return [[0 for i in range(0, size)] for i in range(0, size)]

def isWin(a):
    return traverse(a, lambda x: x == 2048)

def isFail(a):
    def aux(a):
        for i in a:
            for j in zip(i, i[1:]):
                if j[0] == j[1]: return False
        return True
    return aux(a) or aux(rotate(a))
    
def traverse(a, f):
    for line in a:
        for ele in line:
            if f(ele): return True
    return False

def randomPoint(size):
    x = random.randint(0, size)
    y = random.randint(0, size)
    return (x, y)

def randomInit(a):
    seed = [2, 2, 2, 4]
    x, y = randomPoint(len(a)-1)
    v = random.randint(0, len(seed)-1)
    a[x][y] = seed[v]

def randomNum(a):
    seed = [2, 2, 2, 4]
    x, y = randomPoint(len(a)-1)
    if a[x][y] == 0:
        v = random.randint(0, len(seed)-1)
        a[x][y] = seed[v]
    else: randomNum(a)

def newGame():
    print "w for move up, a for move left, s for move down, d for move right."
    print "q for quit."
    won = False
    a = newEmpty(4)
    randomInit(a)
    randomInit(a)
    prettyPrint(a)
    while True:
        b = copy.deepcopy(a)
        key = raw_input()
        if key == "w":   a = reduceUp(a)
        elif key == "a": a = reduceLeft(a)
        elif key == "s": a = reduceDown(a)
        elif key == "d": a = reduceRight(a)
        elif key == "q": break
        if a == b: 
            print "no numbers to be reduce"
        else: randomNum(a)
        prettyPrint(a)
        if isWin(a) and not won:
            print "You win"
            won = True
        elif isFail(a):
            print "You fail"
            break

def test():
    assert reduceLineLeft([4, 4, 4, 4]) == [8, 8, 0, 0]
    assert reduceLineLeft([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert reduceLineLeft([2, 0, 2, 0]) == [4, 0, 0, 0]
    assert reduceLineLeft([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert reduceLineLeft([2, 2, 0, 2]) == [4, 2, 0, 0]
    assert reduceLineLeft([4, 0, 2, 2]) == [4, 4, 0, 0]
    assert reduceLineLeft([2, 0, 2, 2]) == [4, 2, 0, 0]
    assert reduceLineLeft([2, 2, 8, 8]) == [4, 16, 0, 0]
    assert reduceLineRight([2, 2, 0, 2]) == [0, 0, 2, 4]
    assert reduceLineRight([0, 0, 0, 2]) == [0, 0, 0, 2]
    assert reduceLineRight([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert reduceLineRight([4, 4, 2, 2]) == [0, 0, 8, 4]
    assert reduceLineRight([2, 4, 4, 2]) == [0, 2, 8, 2]
    
if __name__ == "__main__":
    newGame()
