# https://www.pyimagesearch.com/2021/01/04/opencv-augmented-reality-ar/
# pip install opencv-contrib-python imutils

import numpy as np
import random
import argparse
import imutils
import sys
import cv2

def myrin_info():
    win = cv2.imread("images/myrin.jpeg")
    text = "Myrin"
    coordinates = (5,20)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0,0,0)
    thickness = 2
    cv2.putText(win, text, coordinates, font, fontScale, color, thickness)
    cv2.imshow("Myrin", win)


def klidoscope_info():
    win = cv2.imread("images/klidoscope.jpeg")
    text = "The Klidoscope"
    coordinates = (5,20)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0,0,0)
    thickness = 2
    cv2.putText(win, text, coordinates, font, fontScale, color, thickness)
    cv2.imshow("The Klidoscope", win)

def commons_info():
    win = cv2.imread("images/commons.jpeg")
    text = "The Commons"
    coordinates = (5,20)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0,0,0)
    thickness = 2
    cv2.putText(win, text, coordinates, font, fontScale, color, thickness)
    cv2.imshow("The Commons", win)

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--source", required=False,
        help="path to input source image that will be put on input")
    args = vars(ap.parse_args())

    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    ret, image = cap.read()
    images = {
        "commons":"images/commons.jpeg",
        "myrin":"images/myrin.jpeg",
        "klidoscope":"images/klidoscope.jpeg"
    }
    choice = random.choice(list(images))
    # load the input image, resize it
    if len(sys.argv) > 1:
        source = cv2.imread(args["source"])
    else:
        source = cv2.imread(images[choice])


    while True:
        
        ret, image = cap.read()
        
        #image = imutils.resize(image, width=600)
        (imgH, imgW) = image.shape[:2]  
        
        # load the ArUCo dictionary, grab the ArUCo parameters, and detect
        # the markers
        #print("[INFO] detecting markers...")
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,parameters=arucoParams)

        # show the found markers
        cv2.aruco.drawDetectedMarkers(image, corners)

        # if we have not found four markers in the input image then we cannot
        # apply our augmented reality technique
        if len(corners) != 4:
            #print("[INFO] could not find 4 corners; found {}... press any key to continue or q to quit".format(str(len(corners))))
            cv2.imshow("Input", image)
            key = cv2.waitKey(3) & 0xFF # 3 ms pause
            if key == ord('q'):
                sys.exit(0)
            else:
                continue
            
        # otherwise, we've found the four ArUco markers, so we can continue
        # by flattening the ArUco IDs list and initializing our list of
        # reference points
        #print("[INFO] constructing augmented reality visualization...")
        ids = ids.flatten()
        refPts = []
        # loop over the IDs of the ArUco markers in top-left, top-right,
        # bottom-right, and bottom-left order
        for i in (923, 1001, 241, 1007):
            # grab the index of the corner with the current ID and append the
            # corner (x, y)-coordinates to our list of reference points
            j = np.squeeze(np.where(ids == i))
            corner = np.squeeze(corners[j])
            refPts.append(corner)  

        # unpack our ArUco reference points and use the reference points to
        # define the *destination* transform matrix, making sure the points
        # are specified in top-left, top-right, bottom-right, and bottom-left
        # order
        (refPtTL, refPtTR, refPtBR, refPtBL) = refPts
        dstMat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
        dstMat = np.array(dstMat)
        # grab the spatial dimensions of the source image and define the
        # transform matrix for the *source* image in top-left, top-right,
        # bottom-right, and bottom-left order
        (srcH, srcW) = source.shape[:2]
        srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])
        # compute the homography matrix and then warp the source image to the
        # destination based on the homography
        (H, _) = cv2.findHomography(srcMat, dstMat)
        warped = cv2.warpPerspective(source, H, (imgW, imgH))

        # construct a mask for the source image now that the perspective warp
        # has taken place (we'll need this mask to copy the source image into
        # the destination)
        mask = np.zeros((imgH, imgW), dtype="uint8")
        cv2.fillConvexPoly(mask, dstMat.astype("int32"), (255, 255, 255),
            cv2.LINE_AA)
        # this step is optional, but to give the source image a black border
        # surrounding it when applied to the source image, you can apply a
        # dilation operation
        rect = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        mask = cv2.dilate(mask, rect, iterations=2)
        # create a three channel version of the mask by stacking it depth-wise,
        # such that we can copy the warped source image into the input image
        maskScaled = mask.copy() / 255.0
        maskScaled = np.dstack([maskScaled] * 3)
        # copy the warped source image into the input image by (1) multiplying
        # the warped image and masked together, (2) multiplying the original
        # input image with the mask (giving more weight to the input where
        # there *ARE NOT* masked pixels), and (3) adding the resulting
        # multiplications together
        warpedMultiplied = cv2.multiply(warped.astype("float"), maskScaled)
        imageMultiplied = cv2.multiply(image.astype(float), 1.0 - maskScaled)
        output = cv2.add(warpedMultiplied, imageMultiplied)
        output = output.astype("uint8")    
        
        # call the function to display info about the image
        if choice == "commons":
            commons_info()
        elif choice == "myrin":
            myrin_info()
        elif choice == "frontgate":
            frontgate_info()
        else:
            klidoscope_info()

        # show the source image, output of our augmented reality
        cv2.imshow("Input", image)
        #cv2.imshow("Source", source)
        cv2.imshow("OpenCV AR Output", output)
        #print("press any key to continue or q to quit")
        #key = cv2.waitKey(0) & 0xFF
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit(0)
        else:
            continue

if __name__ == "__main__":
    main()
