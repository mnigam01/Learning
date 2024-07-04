from abc import ABC, abstractmethod
import random
from collections import *

class Dice:
    def __init__(self, no_of_dices, min=1, max=6):
        self.dice = no_of_dices
        self.min = min
        self.max = max
    def roll(self):
        return random.randint(1, self.dice*self.max)

class Jump:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Player:
    def __init__(self, name=None, initial_pos = 0):
        self.name = name
        self.pos = initial_pos
    

class Board:
    def __init__(self, size:int, no_of_ladder:int, no_of_snakes:int, no_of_dice):
        self.size = size
        self.ladders = dict()
        self.snakes = dict()
        self.dice = Dice(no_of_dice)
        self.initialise(no_of_ladder, no_of_snakes)

    def initialise(self,no_of_ladder, no_of_snakes):
        n = self.size
        seen = set([n*n])
        while no_of_ladder:
            start, end = random.randint(1, n*n), random.randint(1, n*n)
            if start>=end or start in seen or end in seen:
                continue
            seen.add(start)
            seen.add(end)
            self.ladders[start] = end
        
            no_of_ladder-=1
            
        while no_of_snakes:
            start, end = random.randint(1, n*n), random.randint(1, n*n)
            if end>=start or start in seen or end in seen:
                continue
            seen.add(start)
            seen.add(end)
            self.snakes[start] = end
        
            no_of_snakes-=1


    def move_piece(self, player:Player, step):
        n = self.size
        if player.pos+step>n*n:
            return
        player.pos+=step
        print(player.name, "move to", player.pos)
        if player.pos in self.ladders:
            print(player.name, " climbed ladder")
            player.pos = self.ladders[player.pos]
        
        if player.pos in self.snakes:
            print(player.name, " bit by snake")
            player.pos = self.snakes[player.pos]
            
class Game:
    def __init__(self, size, no_of_ladders, no_of_snakes, no_of_players, dice):
        self.board = Board(size, no_of_ladders, no_of_snakes, dice)
        self.players = deque()

    def add_player(self,player:Player):
        self.players.append(player)

    def start(self):
        while len(self.players)>1:
            player = self.players.popleft()
            # roll dice
            step = self.board.dice.roll()
            self.board.move_piece(player, step)
            if player.pos==(self.board.size)**2:
                print(player.name," won")
                continue
            self.players.append(player)
            
if __name__=="__main__"         :
    game = Game(10, 8, 8, 3,1)
    p1 = Player("p1")
    p2 = Player("p2")
    p3 = Player("p3")
    game.add_player(p1)
    game.add_player(p2)
    game.add_player(p3)
    game.start()
            