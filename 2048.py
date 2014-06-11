#coding=utf8
#Wei Guannan

import random

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
    ys = xs[:]
    ys.reverse()
    ys = reduceLineLeft(ys)
    ys.reverse()
    return ys

def reduceLeft(a):
    return map(lambda x: reduceLineLeft(x), a)

def reduceRight(a):
    return map(lambda x: reduceLineRight(x), a)

def reduceUp(a):
    return rotate(reduceLeft(rotate(a)))

def reduceDown(a):
    return rotate(reduceRight(rotate(a)))

def rotate(a):
    b = newEmpty(len(a))
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            b[j][i] = a[i][j]
    return b

def prettyPrint(a):
    for i in a:
        for j in i:
            print j,
        print

def newEmpty(size):
    return [[0 for i in range(0, size)] for i in range(0, size)]

def isWin(a):
    for i in a:
        for j in a:
            if j == 2048: return True
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
    a = newEmpty(4)
    randomInit(a)
    randomInit(a)
    prettyPrint(a)
    while not isWin(a):
        key = raw_input()
        if key == "w":
            a = reduceUp(a)
        elif key == "a":
            a = reduceLeft(a)
        elif key == "s":
            a = reduceDown(a)
        elif key == "d":
            a = reduceRight(a)
        elif key == "q":
            break
        randomNum(a)
        prettyPrint(a)
    if isWin(a):
        print "You win"
    else:
        print "You failed"

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
    #test()
    #prettyPrint(reduceUp([[2, 0, 0, 0], [2, 2, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]]))
    #prettyPrint(reduceDown([[2, 0, 0, 0], [2, 2, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]]))
    #prettyPrint(reduceDown([[0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]]))
    newGame()
