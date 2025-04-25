from flask import Flask, render_template
from Player import *
import random

app = Flask(__name__)
player = Player(1,10)
@app.route('/')
def start():

    return render_template('start.html', player=player)

@app.route('/battle/<string:enemy>')
def battle(enemy):
    rnd = random.choice((-1, 1))
    return render_template('battle.html', enemy=enemy, rnd=rnd)

@app.route('/win/<string:enemy>')
def win(enemy):
    if enemy == "Pikachu":
        player.level += 1
    elif enemy == "Wyverne":
        player.level += 5
    else:
        player.level +=3
    return render_template('win.html', player=player)

@app.route('/lose/<string:enemy>')
def lose(enemy):
    if enemy == "Pikachu":
        player.health -= 1
    elif enemy == "Wyverne":
        player.health -= 5
    else:
        player.health -= 3
    return render_template('lose.html', player=player)

if __name__ == '__main__':
    app.run()