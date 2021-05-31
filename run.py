#!/usr/bin/env python3
from flask import Flask
from flask import abort, redirect, url_for , render_template , request
app = Flask(__name__)

class Matrix3x3(object):
  def __init__(self , board):
    self.board = board
    self.positon = ""
    self.turn = 0


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
        print(self.board[i][j] , end = " | ")
      print("\n")
      print("-----------")


    
  def _add(self):
    if(self._turn() == 1):
      while(1):
        print("X turn")
        self.position = input()
        if(self.position == 'q' or self.position == 'Q'):
          exit(0)
        if(self.position == "00" and self.board[0][0] == 0):
          self.board[0][0] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "01" and self.board[0][1] == 0):
          self.board[0][1] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "02" and self.board[0][2] == 0):
          self.board[0][2] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "10" and self.board[1][0] == 0):
          self.board[1][0] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "11" and self.board[1][1] == 0):
          self.board[1][1] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "12" and self.board[1][2] == 0):
          self.board[1][2] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "20" and self.board[2][0] == 0):
          self.board[2][0] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "21" and self.board[2][1] == 0):
          self.board[2][1] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        elif(self.position == "22" and self.board[2][2] == 0):
          self.board[2][2] = "X"
          if(self._check("X") == 1):
            print("X won")
            exit(0)
          self._print()
          break
        
        else:
          print("position %s is taken" % (self.position))
    else:
     while(1):
        print("O Turn")
        self.position = input()
        if(self.position == 'q' or self.position == 'Q'):
          exit(0)
        if(self.position == "00" and self.board[0][0] == 0):
          self.board[0][0] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "01" and self.board[0][1] == 0):
          self.board[0][1] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "02" and self.board[0][2] == 0):
          self.board[0][2] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "10" and self.board[1][0] == 0):
          self.board[1][0] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "11" and self.board[1][1] == 0):
          self.board[1][1] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "12" and self.board[1][2] == 0):
          self.board[1][2] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "20" and self.board[2][0] == 0):
          self.board[2][0] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "21" and self.board[2][1] == 0):
          self.board[2][1] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        elif(self.position == "22" and self.board[2][2] == 0):
          self.board[2][2] = "O"
          if(self._check("O") == 1):
            print("O won")
            exit(0)
          self._print()
          break
        else:
          print("position %s is invalid" % (self.position))

  def _clear(self):
    for i in range(3):
      for j in range(3):
        self.board[i][j] = 0




@app.route('/')
def Board():
  position = request.args.get('type')
  print(position)
    
  return render_template("board.html")

@app.route('/x')
def x_turn():
  return "x" 


@app.route('/o')
def o_turn():
  return "o" 




if __name__ == "__main__":
  #app.run(debug=True)
  board = [[0 for i in range(3)] for j in range(3)]
  for i in range(3):
    for j in range(3):
      board[i][j] = 0
  play = Matrix3x3(board)
  play._clear()
  while(1):
    play._add()

