import argparse

import skimage.io as skio
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from Calculations import *
from Algorithm import *
from Morphing import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get name of files')
    parser.add_argument('--image_a', type=str, help='Image file name')
    parser.add_argument('--image_b', type=str, help='Image file name')
    parser.add_argument('--lines', type=str, help='Line file name')
    args = parser.parse_args()

    imageA = args.image_a
    imageB = args.image_b
    lines = args.lines

    grayImageB = cv.imread(imageB)
    grayImageA = cv.imread(imageA)

    lines = readLines(lines)

    bLines = lines[1]
    aLines = lines[0]

    morphedImages = twoImageMorphing(grayImageA, grayImageB, aLines, bLines)

    for i in range(len(morphedImages)):
        cv.imshow("Frame "+str(i+1), morphedImages[i])

    cv.waitKey(0)

    out = cv.VideoWriter("out-video.avi", cv.VideoWriter_fourcc(*'DIVX'), 1, grayImageB.shape[:2])

    for i in range(len(morphedImages)):
        out.write(morphedImages[i])
    out.release()

    '''

    img = cv.imread("ford-gt-2005.jpg", 0)
    size = img.shape
    newImg = np.zeros(size)
    newImg2 = []

    for i in range(size[0]):        # HEIGHT
        newImg2.append([])
        for j in range(size[1]):    # WIDTH
            newImg2[i].append(0)

    for i in range(size[0]):        # HEIGHT
        for j in range(size[1]):    # WIDTH
            #newImg[size[0]-1-i][size[1]-1-j] = img[i][j]
            newImg.itemset((size[0]-1-i, size[1]-1-j), img.item(i,j))

    print(img[0][:10])
    print(newImg[size[0]-1][size[1]-10:])

    print(type(img))
    print(img.dtype)
    print(type(newImg))
    print(newImg.dtype)
    print(type(newImg2))

    newImg = newImg.astype(np.uint8)

    print(type(newImg))
    print(newImg.dtype)


    cv.imshow("new-img.jpg", newImg)

    cv.waitKey(0)

__________________________________________________________________________________
    
    image1 = cv.imread("peugeot-207.jpg")
    image2 = cv.imread("ford-gt-2005.jpg")
    image3 = cv.imread("alexis-sanchez.jpg")
    image4 = cv.imread("harold.jpg")

    cars = [image1, image2]
    faces = [image3, image4]

    print(image1.shape[:2])
    print(image3.shape[:2])

    cars_out = cv.VideoWriter("car-video.avi", cv.VideoWriter_fourcc(*'DIVX'), 1, image1.shape[:2])
    faces_out = cv.VideoWriter("face-video.avi", cv.VideoWriter_fourcc(*'DIVX'), 1, image3.shape[:2])

    for i in range(len(cars)):
        cars_out.write(cars[i])
    cars_out.release()

    for i in range(len(faces)):
        faces_out.write(faces[i])
    faces_out.release()

________________________________________________________________________________________________________
    
    for i in range(grayFord.shape[0]):
        for j in range(grayFord.shape[1]):
            new[i][j] = grayFord[i][j]
    

    cv.imshow("A", morphedImages[0])
    cv.imshow("AM", morphedImages[1])
    cv.imshow("M", morphedImages[2])
    cv.imshow("MB", morphedImages[3])
    cv.imshow("B", morphedImages[4])
    cv.waitKey(0)
    
    
    shape = peugeotImage.shape

    a = (2, 2)
    b = (1, 1)

    pq = ((0,0), (3,5))
    x = (5,2)

    uv = calculateUV(pq, x)

    auxImage = np.zeros((5,5))

    auxImage[3][2] = 1

    res = cv.addWeighted(morphedImage[0][1], 0.5, morphedImage[1][1], 0.5, 0.0)

    skio.imshow(res)
    plt.show()
    
    '''
