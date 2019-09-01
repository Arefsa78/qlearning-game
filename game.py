from enum import Enum
from random import randint

from math2 import Vector2D


class Dir(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Game:
    MAP_SIZE = 12
    N_WALL = 20
    EMPTY = 0
    WALL = 1
    AGENT = 2
    GOAL = 3

    def __init__(self):
        self.map = [[Game.EMPTY for _ in range(Game.MAP_SIZE)] for _ in range(Game.MAP_SIZE)]
        self.agent: Vector2D = Vector2D(1, 1)
        self.init_map()
        self.display()

    def init_map(self):
        for i in range(Game.MAP_SIZE):
            for j in range(Game.MAP_SIZE):
                if (i == 0 or i == Game.MAP_SIZE - 1 or
                        j == 0 or j == Game.MAP_SIZE - 1):
                    self.map[i][j] = Game.WALL

        self.map[self.agent.y][self.agent.x] = Game.AGENT
        self.map[Game.MAP_SIZE - 2][Game.MAP_SIZE - 2] = Game.GOAL

        n_wall = 0
        while n_wall < Game.N_WALL:
            wall = Vector2D(randint(1, Game.MAP_SIZE - 2), randint(1, Game.MAP_SIZE - 2))
            if self.map[wall.y][wall.x] != Game.EMPTY:
                continue
            self.map[wall.y][wall.x] = Game.WALL
            n_wall += 1

    def display(self):
        s = ""
        for i in range(Game.MAP_SIZE):
            for j in range(Game.MAP_SIZE):
                s += str(self.map[i][j]) + " "
            s += '\n'

        print(s)

    def move(self, action):
        move = Vector2D(0, 0)
        if action == Dir.RIGHT:
            move = Vector2D(1, 0)
        elif action == Dir.UP:
            move = Vector2D(0, -1)
        elif action == Dir.LEFT:
            move = Vector2D(-1, 0)
        elif action == Dir.DOWN:
            move = Vector2D(0, 1)

        new_pos = self.agent + move
        if self.map[new_pos.y][new_pos.x] != Game.EMPTY:
            self.reset()
            return

        self.map[self.agent.y][self.agent.x] = Game.EMPTY
        self.agent = new_pos
        self.update_map()

    def reset(self):
        self.map[self.agent.y][self.agent.x] = Game.EMPTY
        self.agent = Vector2D(1, 1)
        self.update_map()

    def update_map(self):
        self.map[self.agent.y][self.agent.x] = Game.AGENT
