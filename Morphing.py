
from Algorithm import multipleLineAlgorithm

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

    middleImageFromA = multipleLineAlgorithm(imageA, imageB, linesA, middleInterpolation)
    middleImageFromB = multipleLineAlgorithm(imageB, imageA, linesB, middleInterpolation)
    firstHalfImageFromA = multipleLineAlgorithm(imageA, imageB, linesA, firstHalfInterpolation)
    firstHalfImageFromB = multipleLineAlgorithm(imageB, imageA, linesB, firstHalfInterpolation)
    secondHalfImageFromA = multipleLineAlgorithm(imageA, imageB, linesA, secondHalfInterpolation)
    secondHalfImageFromB = multipleLineAlgorithm(imageB, imageA, linesB, secondHalfInterpolation)

    firstImageFromA = multipleLineAlgorithm(imageA, imageB, linesA, linesB)
    imageFromB = multipleLineAlgorithm(imageB, imageA, linesB, linesA)

    return [[firstHalfImageFromA, middleImageFromA, secondHalfImageFromA],
            [firstHalfImageFromB, middleImageFromB, secondHalfImageFromB]]