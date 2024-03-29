
from Calculations import *
import cv2 as cv

def multipleLineAlgorithm(imageA, imageB, linesA, linesB):

    #   Morphs pixels in A into B

    sizeA = imageA.shape
    newImage = np.zeros(imageA.shape)

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
            if (Xprime[0] < newImage.shape[1] and Xprime[1] < newImage.shape[0]):
                newImage[Xprime[1]][Xprime[0]] = imageA[y][x]

    newImage = newImage.astype(np.uint8)

    return newImage
