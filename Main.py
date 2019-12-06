
import skimage.io as skio
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from Calculations import *
from Algorithm import multipleLineAlgorithm
from Morphing import *

if __name__ == '__main__':

    peugeotImage = skio.imread("peugeot-207.jpeg")
    peugeotImage = rgb2gray(peugeotImage)

    fordImage = skio.imread("ford-gt-2005.jpg")
    fordImage = rgb2gray(fordImage)

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

    skio.imshow(morphedImage[0][0])
    plt.show()

    skio.imshow(morphedImage[0][1])
    plt.show()

    skio.imshow(morphedImage[0][2])
    plt.show()

    skio.imshow(morphedImage[1][0])
    plt.show()

    skio.imshow(morphedImage[1][1])
    plt.show()

    skio.imshow(morphedImage[1][2])
    plt.show()
