from flask import Flask, render_template
from Player import *
import random
from pygame import mixer


def playsound(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

app = Flask(__name__)

player = Player(1,10)

@app.route('/')
def start():

    return render_template('start.html', player=player)

@app.route('/battle/<string:enemy>')
def battle(enemy):
    rnd = random.choice((-1, 1))
    if enemy == "Pikachu":
        playsound("./sound/700348__silasonlyw__pikachu-pokemon.wav")
    elif enemy == "Wyvern":
        playsound("./sound/4505__noisecollector__dragon2.wav")
    else:
        playsound("./sound/798331__dr_dig1__troll-or-monster-laughing.mp3")
    return render_template('battle.html', enemy=enemy, rnd=rnd)

@app.route('/win/<string:enemy>')
def win(enemy):
    playsound("./sound/270319__littlerobotsoundfactory__jingle_win_01.wav")
    if enemy == "Pikachu":
        player.level += 1
    elif enemy == "Wyvern":
        player.level += 5
    else:
        player.level +=3
    return render_template('win.html', player=player)

@app.route('/lose/<string:enemy>')
def lose(enemy):
    if enemy == "Pikachu":
        player.health -= 1
    elif enemy == "Wyvern":
        player.health -= 5
    else:
        player.health -= 3
    if player.health <= 0:
        playsound("./sound/524741__lilmati__game-over-08.wav")
    else:
        playsound("./sound/350981__cabled_mess__lose_c_09.wav")

    return render_template('lose.html', player=player)

if __name__ == '__main__':
    app.run()