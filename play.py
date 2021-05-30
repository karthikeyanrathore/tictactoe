#!/usr/bin/env python3
from flask import Flask
from flask import abort, redirect, url_for , render_template , request , flash
app = Flask(__name__)
app.secret_key = 'usr'
app.config['SESSION_TYPE'] = 'filesystem'

class Matrix3x3(object):
  def __init__(self , board):
    self.board = board
    self.position = ""
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
          exit(0)
        self._print()
      elif(self.position == "01" and self.board[0][1] == 0):
        self.board[0][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "02" and self.board[0][2] == 0):
        self.board[0][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "10" and self.board[1][0] == 0):
        self.board[1][0] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "11" and self.board[1][1] == 0):
        self.board[1][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "12" and self.board[1][2] == 0):
        self.board[1][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "20" and self.board[2][0] == 0):
        self.board[2][0] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "21" and self.board[2][1] == 0):
        self.board[2][1] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
        self._print()
      elif(self.position == "22" and self.board[2][2] == 0):
        self.board[2][2] = "X"
        if(self._check("X") == 1):
          print("X won")
          exit(0)
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
          exit(0)
        self._print()
      elif(self.position == "01" and self.board[0][1] == 0):
        self.board[0][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "02" and self.board[0][2] == 0):
        self.board[0][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "10" and self.board[1][0] == 0):
        self.board[1][0] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "11" and self.board[1][1] == 0):
        self.board[1][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "12" and self.board[1][2] == 0):
        self.board[1][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "20" and self.board[2][0] == 0):
        self.board[2][0] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "21" and self.board[2][1] == 0):
        self.board[2][1] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      elif(self.position == "22" and self.board[2][2] == 0):
        self.board[2][2] = "O"
        if(self._check("O") == 1):
          print("O won")
          exit(0)
        self._print()
      else:
        self.turn -= 1
        return -1

  def _clear(self):
    for i in range(3):
      for j in range(3):
        self.board[i][j] = 0

  def _whosturn(self):
    if(self.turn % 2 == 0):
      return 1;
    else:
      return 0;


@app.route('/')
def Board():
  error = None
  position = request.args.get('type')
  print(position)
  if(position is not None):
    if(play._whosturn() == 1):
      if(play._add(position) == -1):
        error = "position %s is invalid" %(position);
        print(error)
        return render_template("xboard.html" , error = error , turn = play._whosturn() , pos = position)
      return render_template("oboard.html" , error = error , turn = play._whosturn() , pos = position)
    else:
      if(play._add(position) == -1):
        error = "position %s is invalid" %(position);
        print(error)
        return render_template("oboard.html" , error = error , turn = play._whosturn() , pos = position)
      return render_template("xboard.html" , error = error , turn = play._whosturn() , pos = position)
  return render_template("board.html" , error = error , turn = play._whosturn() , pos = position)

@app.route('/clear')
def clear():
  play._clear()
  return redirect(url_for("Board"))


if __name__ == "__main__":
  board = [[0 for i in range(3)] for j in range(3)]
  for i in range(3):
    for j in range(3):
      board[i][j] = 0

  play = Matrix3x3(board)
  play._clear()

  app.run(debug=True)
