#!/usr/bin/env python3
import sys
import pytesseract

def _read(board):
  try:
    return pytesseract.image_to_string(board , lang = "eng")
  except:
    return "[ERROR] Unable to process file: %s" % (board)

if __name__ == "__main__":
  board = sys.argv[1]
  print(board)
  print(_read(board)) 


