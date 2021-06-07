#!/usr/bin/env python3
import cv2 as cv

def frame():
  cap = cv.VideoCapture(0)
  if not cap.isOpened():
    print("Cannot open camera")
    exit()
  while(1):
    ret, frame = cap.read()
    if not ret:
      print("Can't receive frame (stream end?). Exiting ...")
      break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if (cv.waitKey(1) == ord('5')):
      break

  cap.release()
  cv.destroyAllWindows()

if __name__ == "__main__":
  frame()
