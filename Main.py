
import skimage.io as skio
from skimage.color import rgb2gray

if __name__ == '__main__':

    imageA = skio.imread("peugeot-207.jpeg")
    imageA = rgb2gray(imageA)
    shape = imageA.shape
    print(shape)

