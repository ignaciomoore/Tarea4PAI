
import skimage.io as skio
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from Calculations import *
from Algorithm import multipleLineAlgorithm
from Morphing import *

if __name__ == '__main__':

    #peugeotImage = skio.imread("peugeot-207.jpeg")
    #peugeotImage = rgb2gray(peugeotImage)

    #fordImage = skio.imread("ford-gt-2005.jpg")
    #fordImage = rgb2gray(fordImage)

    ford = cv.imread("ford-gt-2005.jpg")
    peugeot = cv.imread("peugeot-207.jpeg")

    grayFord = cv.cvtColor(ford, cv.COLOR_BGR2GRAY)
    grayPeugeot = cv.cvtColor(peugeot, cv.COLOR_BGR2GRAY)

    print(grayFord.shape)
    print(grayPeugeot.shape)

    newShape = (max(grayFord.shape[0], grayPeugeot.shape[0]), max(grayFord.shape[1], grayPeugeot.shape[1]))

    print(newShape)

    newFord = np.zeros(newShape)
    newPeugeot = np.zeros(newShape)

    for i in range(peugeot.shape[0]):
        for j in range(peugeot.shape[1]):
            newPeugeot[i][j] = grayPeugeot[i][j]

    for i in range(ford.shape[0]):
        for j in range(ford.shape[1]):
            newFord[i][j] = grayFord[i][j]

    res = cv.addWeighted(newFord, 0.5, newPeugeot, 0.5, 0.0)

    f = cv.resize(grayFord, (newShape[1], newShape[0]))

    d = cv.resize(peugeot, (ford.shape[1], ford.shape[0]))

    #cv.imshow("Blend", res)
    cv.imshow("Ford", d)
    cv.waitKey(0)
    '''
    
    shape = peugeotImage.shape

    a = (2, 2)
    b = (1, 1)

    pq = ((0,0), (3,5))
    x = (5,2)

    uv = calculateUV(pq, x)

    auxImage = np.zeros((5,5))

    fordLines = [((491, 336), (729, 263)),  #wheels
                 ((79, 257), (361, 274)),   #lights
                 ((326, 123), (615, 131)),  #roof
                 ((149, 321), (416, 125))]  #middle of the front

    peugeotLines = [((474, 383), (753, 339)),  #wheels
                 ((73, 266), (364, 276)),   #lights
                 ((341, 84), (624, 77)),  #roof
                 ((161, 308), (426, 89))]  #middle of the front

    auxImage[3][2] = 1

    morphedImage = twoImageMorphing(peugeotImage, fordImage, peugeotLines, fordLines)

    res = cv.addWeighted(morphedImage[0][1], 0.5, morphedImage[1][1], 0.5, 0.0)

    skio.imshow(res)
    plt.show()
    
    '''
