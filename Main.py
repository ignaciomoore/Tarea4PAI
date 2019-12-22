
import argparse
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
