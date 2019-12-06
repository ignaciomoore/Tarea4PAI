
import skimage.io as skio
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from Calculations import *
from Algorithm import multipleLineAlgorithm

if __name__ == '__main__':

    imageA = skio.imread("peugeot-207.jpeg")
    imageA = rgb2gray(imageA)

    imageB = skio.imread("ford-gt-2005.jpg")
    imageB = rgb2gray(imageB)

    shape = imageA.shape

    a = (2, 2)
    b = (1, 1)

    pq = ((0,0), (3,5))
    x = (5,2)

    uv = calculateUV(pq, x)

    auxImage = np.zeros((5,5))

    auxImage[3][2] = 1

    #print(multipleLineAlgorithm(imageA, imageB, ))

    skio.imshow(imageA)
    plt.show()