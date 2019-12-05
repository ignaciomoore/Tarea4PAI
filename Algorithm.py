
def multipleLineAlgorithm(imageA, imageB, linesA, linesB):

    sizeA = imageA.shape

    DSUM = (0, 0)
    weightSum = 0
    UV = (0, 0)
    D = (0, 0)
    weight = 0
    Xprime = (0, 0)
    dist = 0
    length = 0

    for X in range(sizeA[0]):

        DSUM = (0, 0)
        weightSum = 0

        for PQ in linesA:

            length = len(PQ)

            UV = calculateUV(PQ)
            Xprime = calculateXprime(UV, PQ)
            D = substract(Xprime, X)
            dist = distance(X, PQ)
            weight = calculateWeight(length, dist)
            DSUM += D * weight
            weightSum += weight

        Xprime = X + DSUM/weightSum
        # destinationImage(X) = sourceImage(Xprime)