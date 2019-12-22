
import math
import numpy as np

def substract(p, q):
    return (p[0] - q[0], p[1] - q[1])


def dotProduct(p, q):
    return (p[0] * q[0]) + (p[1] * q[1])


def module(p):
    return math.sqrt(math.pow(p[0], 2) + math.pow(p[1], 2))


def perpendicular(PQ):

    size = module(PQ)
    x = PQ[0]
    y = PQ[1]

    vy = size/math.sqrt((math.pow(y, 2)/ math.pow(x, 2)) + 1)
    vx = (-y*vy)/x

    return (vx, vy)


def calculateUV(PQ, X):

    u = dotProduct(substract(X, PQ[0]), substract(PQ[1], PQ[0])) / \
        math.pow(module(substract(PQ[1], PQ[0])), 2)

    v = dotProduct(substract(X, PQ[0]), perpendicular(substract(PQ[1], PQ[0]))) / \
        module(substract(PQ[1], PQ[0]))

    return (u, v)


def add3(p, q, w):
    return (p[0] + q[0] + w[0], 
            p[1] + q[1] + w[1])

def add2(p, q):
    return (p[0] + q[0],
            p[1] + q[1])


def devide(point, num):
    return (point[0]/num, point[1]/num)


def multiply(num, point):
    return (point[0]*num, point[1]*num)


def calculateXprime(UV, PQ):

    p = PQ[0]
    q = PQ[1]
    u = UV[0]
    v = UV[1]

    Xprime = add3(p, multiply(u, substract(q, p)), devide(multiply(v, perpendicular(substract(q, p))),
                                                          module(substract(q, p))))

    return (int(Xprime[0]), int(Xprime[1]))

def distance(x, pq):

    x0 = x[0]
    y0 = x[1]
    x1 = pq[0][0]
    y1 = pq[0][1]
    x2 = pq[1][0]
    y2 = pq[1][1]

    return abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / \
           math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))


def calculateWeight(length, distance):

    a = 0.001   #   - Barely grater than zero.
    b = 1       #   - [0.5, 2] The lower the value the more equal effects from different lines.
    p = 0.5       #   - [0, 1] If zero then all lines have the same weight, if one then longer
                #           lines have more relative eight than shorter lines.

    return math.pow(math.pow(length, p) / (a + distance), b)

def imageInNewShape(image):

    shape = image.shape

    newShape = (int(shape[0] * 1.5),
                int(shape[1] * 1.5))

    newImage = np.zeros(newShape)
    return newImage


def lineLength(PQ):

    p = PQ[0]
    q = PQ[1]

    return math.sqrt(math.pow(q[0] - p[0], 2) + math.pow(q[1] - p[1], 2))

def readLines(lines):

    aLines = []
    bLines = []

    file = open(lines, "r")

    for line in file:

        points = line.find(':')
        pair = line[points+2:]
        pair = pair.split(', ')
        for i in range(len(pair)):
            pair[i] = int(pair[i])

        p1 = pair[:4]
        p2 = pair[4:]

        aLines.append(((p1[0], p1[1]), (p1[2], p1[3])))
        bLines.append(((p2[0], p2[1]), (p2[2], p2[3])))

    return (aLines, bLines)
