#!/usr/bin/env python3
from flask import Flask
from flask import abort, redirect, url_for , render_template , request , flash

from play import play
app = Flask(__name__)
app.secret_key = 'usr'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/X/<int:moves>')
def x_won(moves):
  mv = (int(moves) // 2) + 1
  return render_template("x_won.html" , mv = mv)
 
@app.route('/O/<int:moves>')
def o_won(moves):
  mv = (int(moves) // 2) 
  return render_template("o_won.html" , mv = mv)
 
@app.route('/Draw')
def draw():
  return render_template("draw.html")


@app.route('/ai/oai')
def o_ai():
  error = None
  ai_result = play._obest()
  output = play._add(ai_result)
  print("ai %s" %(output))
  if(output == -1):
    error = "error";
    print(error)
  if(output == 2):
    return redirect(url_for('o_won' , moves = play.turn))
  if(play._draw() == 1):
    return redirect(url_for('draw'))
  play.count = 0
  return redirect(url_for("ai"))


@app.route('/ai')
def ai():
  error = None
  position = request.args.get('type')
  print(position)
  
  if(position is not None):
    if(play._whosturn() == 1):
      output = play._add(position)
      if(output == -1):
        error = "error";
        print(error)
        return render_template("ai/xboard.html" , error = error , turn = play._whosturn() , pos = position ,board = play.board)
      if(output == 1):
        return redirect(url_for('x_won' , moves = play.turn))
      if(play._draw() == 1):
        return redirect(url_for('draw'))
      return redirect(url_for("o_ai"))
  return render_template("ai/board.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)



@app.route('/')
def Board():
  error = None
  position = request.args.get('type')
  print(position)

  if(position == "u" and play.count % 2 == 0):
    play._undo()
    play._print()
    play.count += 1
    if(play._whosturn() == 1):
      return render_template("xboard.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)
    return render_template("oboard.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)
  
  if(position is not None):
    if(play._whosturn() == 1):
      output = play._add(position)
      if(output == -1):
        error = "error";
        print(error)
        return render_template("xboard.html" , error = error , turn = play._whosturn() , pos = position ,board = play.board)
      if(output == 1):
        return redirect(url_for('x_won' , moves = play.turn))
      if(play._draw() == 1):
        return redirect(url_for('draw'))
      play.count = 0
      return render_template("oboard.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)
    else:
      output = play._add(position)
      if(output == -1):
        error = "error";
        print(error)
        return render_template("oboard.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)
      if(output == 2):
        return redirect(url_for('o_won' , moves = play.turn))
      if(play._draw() == 1):
        return redirect(url_for('draw'))
      play.count = 0
      return render_template("xboard.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)
  return render_template("board.html" , error = error , turn = play._whosturn() , pos = position , board = play.board)

@app.route('/clear')
def clear():
  play._clear()
  return redirect(url_for("Board"))


@app.route('/undo')
def undo():
  play._undo()
  return redirect(url_for("Board"))



if __name__ == "__main__":
  app.run()



