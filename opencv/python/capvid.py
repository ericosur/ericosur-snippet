#
# from: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#

import numpy as np
import cv2
import os

def delete_if_exists(fn):
    # Checks and deletes the output file
    # You cant have a existing file or it will through an error
    if os.path.isfile(fn):
        os.remove(fn)


def main():
    ofn = 'outpy.avi'
    delete_if_exists(ofn)

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Unable to read camera feed")
        return

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #fourcc = cv2.VideoWriter_fourcc(*'8BPS')

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter(ofn, fourcc, 30, (frame_width,frame_height), False)

    while(True):
        ret, frame = cap.read()
        if ret == True:
            aframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Write the frame into the file
            out.write(aframe)

            # Display the resulting frame
            cv2.imshow('aframe', aframe)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Break the loop
        else:
            break

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()
    # Closes all the frames
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
