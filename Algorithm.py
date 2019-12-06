
from Calculations import *

def multipleLineAlgorithm(imageA, imageB, linesA, linesB):

    #   Morphs A pixels in A into B

    sizeA = imageA.shape

    newImage = imageInNewShape(imageB)
    #newImage = np.zeros(imageB.shape)

    for x in range(sizeA[1]):
        for y in range(sizeA[0]):

            X = (x, y)

            DSUM = (0, 0)
            weightSum = 0

            for i in range(len(linesA)):

                PQ = linesA[i]
                length = lineLength(PQ)

                UV = calculateUV(PQ, X)
                Xprime = calculateXprime(UV, linesB[i])
                D = substract(Xprime, X)
                dist = distance(X, PQ)
                weight = calculateWeight(length, dist)
                DSUM = add2(DSUM, multiply(weight, D))
                weightSum += weight

            Xprime = add2(X, devide(DSUM, weightSum))
            Xprime = (int(Xprime[0]), int(Xprime[1]))
            # destinationImage(X) = sourceImage(Xprime)
            newImage[Xprime[1]][Xprime[0]] = imageA[y][x]

            '''
            if Xprime[0] < minX:
                minX = Xprime[0]
            elif Xprime[0] > maxX:
                maxX = Xprime[0]

            if Xprime[1] < minY:
                minY = Xprime[1]
            elif Xprime[1] > maxY:
                maxY = Xprime[1]
            '''

    return newImage
