
from Calculations import *

def multipleLineAlgorithm(imageA, imageB, linesA, linesB):

    #   Morphs al pixels in A into B

    sizeA = imageA.shape
    sizeB = imageB.shape

    DSUM = (0, 0)
    weightSum = 0
    UV = (0, 0)
    D = (0, 0)
    weight = 0
    Xprime = (0, 0)
    dist = 0
    length = 0

    X = (0, 0)
    PQ = ((0, 0), (1, 1))

    newImage = getEmptyImage(sizeA, sizeB)

    for x in range(sizeA[1]):
        for y in range(sizeA[0]):

            X = (x, y)

            DSUM = (0, 0)
            weightSum = 0

            for i in range(len(linesA)):

                PQ = linesA[i]
                length = len(PQ)

                UV = calculateUV(PQ, X)
                Xprime = calculateXprime(UV, linesB[i])
                D = substract(Xprime, X)
                dist = distance(X, PQ)
                weight = calculateWeight(length, dist)
                DSUM += D * weight
                weightSum += weight

            Xprime = X + DSUM/weightSum
            # destinationImage(X) = sourceImage(Xprime)
            imageB[y][x] = imageA[y][x]

    return imageB
