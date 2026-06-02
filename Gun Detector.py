import numpy as np
import cv2 
import imutils
import datetime

# Load the pre-trained Haar Cascade classifier for gun detection
gun_cascade = cv2.CascadeClassifier("cascade.xml")

# Initialize the camera (0 is usually the built-in webcam)
camera = cv2.VideoCapture(0)

# Initialize variables to keep track of frames and detection status
firstFrame = None
gun_exists = None

while True:
    # Read a single frame from the camera
    ret, frame = camera.read()
    
    # Resize the frame for faster processing and standard display
    frame = imutils.resize(frame, width=500)
    
    # Convert the frame to grayscale, which is required for cascade detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the image using the cascade classifier
    # scaleFactor=1.3 and minNeighbors=5 help refine the detection
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    # Check if any guns were detected
    if len(gun) > 0:
        gun_exists = True

    # Draw rectangles around the detected guns
    for (x, y, w, h) in gun:
        # Draw a blue rectangle (255, 0, 0) with a thickness of 2
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Define regions of interest (ROI) for further analysis if needed
        roi_gray = gray[y: y + h, x: x + w]
        roi_color = frame[y : y + h, x : x + w]
        
    # Capture the very first frame to potentially use for background subtraction
    if firstFrame is None:
        firstFrame = gray
        continue

    # Display the processed frame in a window
    cv2.imshow("Security feed", frame) 
    
    # Wait for the 'q' key to be pressed to exit the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
    # Print detection status to the console
    if gun_exists:
        print("Gun Detected")
    else:
        print("Gun didn't detected")

# Cleanup: release the camera resource and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()