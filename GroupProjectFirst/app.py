from flask import Flask, render_template
from Player import *

app = Flask(__name__)

@app.route('/')
def start():
    player = Player(1,10)
    return render_template('start.html', player=player)

@app.route('/battle/<string:enemy>')
def battle(enemy):
    return render_template('battle.html', enemy=enemy)

@app.route('/win')
def win():
    return render_template('win.html')

@app.route('/lose')
def lose():
    return render_template('lose.html')

@app.route('/game_over')
def game_over():
    return render_template('game_over.html')

if __name__ == '__main__':
    app.run()