#!/usr/bin/env python3
import math
class Matrix3x3(object):
  def __init__(self , board):
    self.board = board
    self.position = ""
    self.turn = 0
    self.count = 0
  
  def _turn(self):
    if(self.turn % 2 == 0):
      self.turn += 1
      return 1
    else:
      self.turn += 1
      return 0

  def _check(self , char):
    # columns check
    for i in range(0 , 3):
      if(self.board[0][i] == char and char == self.board[1][i] and char == self.board[2][i]):
        return 1
    # rows check
    for i in range(0 , 3):
      if(self.board[i][0] == char and char == self.board[i][1] and char ==  self.board[i][2]):
        return 1
    # diagonals check
    if(self.board[0][0] == char and char == self.board[1][1] and char == self.board[2][2]):
      return 1
    if(self.board[0][2] == char and char == self.board[1][1] and char == self.board[2][0]) :
      return 1
    return 0;


  def _print(self):
    for i in range(3):
      for j in range(3):
        if(self.board[i][j] == 0):
          print("." , end = " | ")
        else:
          print(self.board[i][j] , end = " | ")
      print("\n")
      print("-----------")

  def _draw(self):
    for i in range(3):
      for j in range(3):
        if(board[i][j] == 0):
          return 0
    return 1    

  def _add(self , pos):
    self.position = pos;
    if(self._turn() == 1):
      print("X")
      if(self.position == 'q' or self.position == 'Q'):
        exit(0)
      if(self.position == "00" and self.board[0][0] == 0):
        self.board[0][0] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "01" and self.board[0][1] == 0):
        self.board[0][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "02" and self.board[0][2] == 0):
        self.board[0][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "10" and self.board[1][0] == 0):
        self.board[1][0] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "11" and self.board[1][1] == 0):
        self.board[1][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "12" and self.board[1][2] == 0):
        self.board[1][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "20" and self.board[2][0] == 0):
        self.board[2][0] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "21" and self.board[2][1] == 0):
        self.board[2][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      elif(self.position == "22" and self.board[2][2] == 0):
        self.board[2][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          return 1
        self._print()
      else:
        self.turn -= 1
        return -1
    else:
      print("O")
      if(self.position == 'q' or self.position == 'Q'):
        exit(0)
      if(self.position == "00" and self.board[0][0] == 0):
        self.board[0][0] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "01" and self.board[0][1] == 0):
        self.board[0][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "02" and self.board[0][2] == 0):
        self.board[0][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "10" and self.board[1][0] == 0):
        self.board[1][0] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "11" and self.board[1][1] == 0):
        self.board[1][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "12" and self.board[1][2] == 0):
        self.board[1][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "20" and self.board[2][0] == 0):
        self.board[2][0] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "21" and self.board[2][1] == 0):
        self.board[2][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      elif(self.position == "22" and self.board[2][2] == 0):
        self.board[2][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          return 2
        self._print()
      else:
        self.turn -= 1
        return -1

  def _clear(self):
    self.position = ""
    self.turn = 0
    for i in range(3):
      for j in range(3):
        self.board[i][j] = 0

  def _whosturn(self):
    if(self.turn % 2 == 0):
      return 1;
    else:
      return 0;
  
  def _undo(self):
    self.turn -= 1 
    row = int(self.position[0])
    col = int(self.position[1])
    self.board[row][col] = 0

  # https://en.wikipedia.org/wiki/Minimax
  def minimax(self , mx):
    if(self._check("X") == 1):
      return 1
    if(self._check("O") == 1):
      return -1
    if(self._draw() == 1):
      return 0
    if(mx):
      value = -math.inf
      for i in range(3):
        for j in range(3):
          if(self.board[i][j] == 0):
            self.board[i][j] = "X"
            value = max(value , self.minimax(False))
            self.board[i][j] = 0
      return value
    else:
      value = math.inf
      for i in range(3):
        for j in range(3):
          if(self.board[i][j] == 0):
            self.board[i][j] = "O"
            value = min(value , self.minimax(True))
            self.board[i][j] = 0
      return value
  
  def _obest(self):
    row = -1
    col = -1
    best = math.inf
    for i in range(3):
      for j in range(3):
        if(self.board[i][j] == 0):
          self.board[i][j] = "O"
          result = self.minimax(True)
          self.board[i][j] = 0
          if(best > result):
            row = i
            col = j
            best = result
    #print("row %d col %d" % (row , col))
    best_position = str(row) + str(col)
    return best_position

  def _xbest(self):
    row = -1
    col = -1
    best = -math.inf
    for i in range(3):
      for j in range(3):
        if(self.board[i][j] == 0):
          self.board[i][j] = "X"
          result = self.minimax(False)
          self.board[i][j] = 0
          if(best < result):
            row = i
            col = j
            best = result
    #print("row %d col %d" % (row , col))
    best_position = str(row) + str(col)
    return best_position

  def _get(self , state):
    for i in range(3):
      for j in range(3):
        if(i == 0):
          if(state[0:3][j] == "-"):
            continue
          elif(state[0:3][j] == "x"):
            self.board[i][j] = "X"
          else:
            self.board[i][j] = "O"
        elif(i == 1):
          if(state[4:7][j] == "-"):
            continue
          elif(state[4:7][j] == "x"):
            self.board[i][j] = "X"
          else:
            self.board[i][j] = "O"
        else:
          if(state[8:11][j] == "-"):
            continue
          elif(state[8:11][j] == "x"):
            self.board[i][j] = "X"
          else:
            self.board[i][j] = "O"
    self._print()
    if(state.count("x") > state.count("o")):
      if(self._obest() == "-1-1"):
        if(self._draw() == 1):
          print("draw")
        elif(self._check("X") == 1):
          print("X won")
        else:
          print("O won")
      else:
        print("best move for o %d rowcol" % self._obest())
    else:
      if(self._xbest() == "-1-1"):
        if(self._draw() == 1):
          print("draw")
        elif(self._check("X") == 1):
          print("X won")
        else:
          print("O won")
      else:
        print("best move for x %d rowcol" % self._xbest())


    
board = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
  for j in range(3):
    board[i][j] = 0

play = Matrix3x3(board)
   

