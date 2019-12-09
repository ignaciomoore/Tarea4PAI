
from Algorithm import multipleLineAlgorithm
import cv2 as cv

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
    firstHalfInterpolation = interpolateLines(linesA, middleInterpolation)
    secondHalfInterpolation = interpolateLines(middleInterpolation, linesB)

    A2 = multipleLineAlgorithm(imageA, imageB, linesA, middleInterpolation)
    B2 = multipleLineAlgorithm(imageB, imageA, linesB, middleInterpolation)
    A1 = multipleLineAlgorithm(imageA, imageB, linesA, firstHalfInterpolation)
    B3 = multipleLineAlgorithm(imageB, imageA, linesB, firstHalfInterpolation)
    A3 = multipleLineAlgorithm(imageA, imageB, linesA, secondHalfInterpolation)
    B1 = multipleLineAlgorithm(imageB, imageA, linesB, secondHalfInterpolation)

    firstImageFromA = multipleLineAlgorithm(imageA, imageB, linesA, linesB)
    imageFromB = multipleLineAlgorithm(imageB, imageA, linesB, linesA)

    return [[A1, A2, A3],
            [B3, B2, B1]]