
from Algorithm import *

def interpolateValues(p, q):
    return int(q + ((p - q) / 2))


def interpolatePoints(p, q):
    return (interpolateValues(p[0], q[0]),
            interpolateValues(p[1], q[1]))


def interpolateLines(linesA, linesB):

    newLines = []

    for i in range(len(linesA)):

        newX = interpolatePoints(linesA[i][0], linesB[i][0])
        newY = interpolatePoints(linesA[i][1], linesB[i][1])
        newLines.append((newX, newY))

    return newLines


def twoImageMorphing(imageA, imageB, linesA, linesB):

    middleInterpolation = interpolateLines(linesA, linesB)
    AHalfInterpolation = interpolateLines(linesA, middleInterpolation)
    BHalfInterpolation = interpolateLines(middleInterpolation, linesB)

    A1 = multipleLineAlgorithm(imageA, imageB, linesA, AHalfInterpolation)
    B3 = multipleLineAlgorithm(imageB, imageA, linesB, AHalfInterpolation)

    A2 = multipleLineAlgorithm(imageA, imageB, linesA, middleInterpolation)
    B2 = multipleLineAlgorithm(imageB, imageA, linesB, middleInterpolation)

    A3 = multipleLineAlgorithm(imageA, imageB, linesA, BHalfInterpolation)
    B1 = multipleLineAlgorithm(imageB, imageA, linesB, BHalfInterpolation)


    AHalfImage = cv.addWeighted(A1, 0.75, B3, 0.25, 0.0)
    middleImage = cv.addWeighted(A2, 0.5, B2, 0.5, 0.0)
    BHalfImage = cv.addWeighted(A3, 0.25, B1, 0.75, 0.0)

    return [imageA, AHalfImage, middleImage, BHalfImage, imageB]
