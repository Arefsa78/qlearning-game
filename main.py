from random import randint
from time import sleep

from game import Game, Dir

game = Game()

while True:
    actoin = randint(0, 3)
    print(Dir(actoin))
    game.move(Dir(actoin))
    game.display()
    sleep(1)
