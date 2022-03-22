#!/usr/bin/env python3
import numpy as np
ROW = 3
COL = 3
class Mat3x3(object):
  def __init__(self):
    self.board = np.zeros((ROW, COL))
    self.turn = 1 # first
  
  # p1 (1) play with oppent p2 (-1)
  def play(self, val):
    pass
  
  # check win for both simultaneously (BAD)
  def win(self):
    k = 0
    for r in range(ROW):
      if self.board[r][k] == 1 and  self.board[r][k + 1] == 1 and self.board[r][k + 2] == 1:
        return 1
      if self.board[r][k] == -1 and self.board[r][k + 1] == -1 and self.board[r][k + 2] == -1:
        return -1
    for c in range(COL):
      if self.board[k][c] == 1 and  self.board[k + 1][c] == 1 and self.board[k + 2][c] == 1:
        return 1
      if self.board[k][c] == -1 and  self.board[k + 1][c] == -1 and self.board[k + 2][c] == -1:
        return -1

    if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
      return 1
    if self.board[0][0] == -1 and self.baord[1][1] == -1 and self.board[2][2] == -1:
      return -1
    if self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1:
      return 1
    if self.board[0][2] == -1 and self.board[1][1] == -1 and self.board[2][0] == -1:
      return -1
        
  # check draw
  def draw(self):
    for r in range(ROW):
      for c in range(COL):
        if self.board[r][c] == 0:
          return False
    return True
  
  # check if blank (r, c) == 0
  def free(self, r, c):
    return self.board[r][c] == 0
  
  # push (int: positon)
  def push(self, positon):
    # https://stackoverflow.com/questions/11821899/how-to-get-row-and-column-from-index
    index  = positon - 1
    r = index // COL
    c = index % COL
    if self.free(r, c):
      if self.turn == 1:
        self.board[index // COL][index % COL] = 1
        self.turn = -1
      else:
        self.board[index // COL][index % COL] = -1
        self.turn = 1
    else:
      #print("wrong position")
      raise "position already occupied"
  
  # go back to prev state of board
  def revert(self):
    pass
