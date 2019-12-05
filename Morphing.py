'''
def twoImageMorphing(imageA, imageB, linesA, linesB):

    middleInterpolation = interpolate(linesA, linesB)
    firstHalfInterpolation = interpolate(linesA, middleInterpolation)
    secondHalfInterpolation = interpolate(middleInterpolation, linesB)
'''