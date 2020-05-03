'''
///////////////////////////////////////////////////////////////////////////
//
// Copyright (c) 2018, STEREOLABS.
//
// All rights reserved.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
///////////////////////////////////////////////////////////////////////////

/*****************************************************************************************
 ** This sample demonstrates how to capture stereo images and calibration parameters    **
 ** from the ZED camera with OpenCV without using the ZED SDK.                          **
 *****************************************************************************************/
'''

import numpy as np
import os
import configparser
import sys
import cv2


class Resolution :
    width = 1280
    height = 720

def main() :

    # Open the ZED camera
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == 0:
        exit(-1)

    image_size = Resolution()
    image_size.width = 1280
    image_size.height = 720

    # Set the video resolution to HD720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, image_size.width*2)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, image_size.height)

    print("Calibration file found. Loading...")

    # camera_matrix_left, camera_matrix_right, map_left_x, map_left_y, map_right_x, map_right_y = init_calibration(calibration_file, image_size)
    # out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (cv2.CAP_PROP_FRAME_WIDTH,cv2.CAP_PROP_FRAME_HEIGHT))
    save_folder = './images/'

    outleft = cv2.VideoWriter('outleft.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (cv2.CAP_PROP_FRAME_WIDTH,cv2.CAP_PROP_FRAME_HEIGHT))
    outright = cv2.VideoWriter('outright.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (cv2.CAP_PROP_FRAME_WIDTH,cv2.CAP_PROP_FRAME_HEIGHT))


    i = 0
    while True :
        # Get a new frame from camera
        retval, frame = cap.read()
        # out.write(frame)
        # cv2.imshow("RAW", frame)
        outleft.write(frame)
        outright.write(frame)
        # Extract left and right images from side-by-side
        left_right_image = np.split(frame, 2, axis=1)
        # Display images
        left_img = left_right_image[0]
        right_img = left_right_image[1]
        cv2.imwrite(save_folder+'left'+str(i)+'.png', left_img)
        cv2.imwrite(save_folder+'right'+str(i)+'.png', right_img)
        i += 1
        cv2.imshow("left RAW", left_img)
        cv2.imshow("right RAW", right_img)

        
        # left_rect = cv2.remap(left_right_image[0], map_left_x, map_left_y, interpolation=cv2.INTER_LINEAR)
        # right_rect = cv2.remap(left_right_image[1], map_right_x, map_right_y, interpolation=cv2.INTER_LINEAR)

        # cv2.imshow("left RECT", left_rect)
        # cv2.imshow("right RECT", right_rect)
        if cv2.waitKey(30) >= 0 :
            break

    cap.release()
    outleft.release()
    outright.release()

    # Closes all the frames
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
