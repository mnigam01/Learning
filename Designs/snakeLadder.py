from abc import ABC, abstractmethod
from collections import deque
from random import randint
class Dice:
    def __init__(self, number_of_dice=1, min=1, max=6) -> None:
        self.number_of_dice =  number_of_dice
        self.min = min
        self.max = max
    
    def roll(self):
        return randint(self.min, self.number_of_dice*self.max) 
        # return sum(randint(self.min, self.max) for _ in range(self.number_of_dice))

class Player:
    def __init__(self, id, position=0) -> None:
        self.id = id
        self.position = position

class SnakeAndLadderInterface():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def get_start_end(self):
        return [self.start, self.end]

class Snake(SnakeAndLadderInterface):
    def __init__(self, start, end) -> None:
        super().__init__(start, end)

class Ladder(SnakeAndLadderInterface):
    def __init__(self, start, end) -> None:
        super().__init__(start, end)

class Board:
    def __init__(self, size, no_of_snakes, no_of_ladders) -> None:
        self.size = size
        self.snakes = {}
        self.ladders = {}
        self.add_snakes_ladders(no_of_snakes, no_of_ladders)
    
    def add_snakes_ladders(self, no_of_snakes, no_of_ladders):
        used_cells = set([(self.size)**2])

        ladder_cnt = 0

        while ladder_cnt<no_of_ladders:
            start, end = randint(1, (self.size)**2), randint(1, (self.size)**2)
            if start>=end or start in used_cells or end in used_cells:
                continue
            used_cells.add(start)
            used_cells.add(end)
            self.ladders[start] = end
            ladder_cnt+=1

        snakes_cnt = 0

        while snakes_cnt<no_of_snakes:
            start, end = randint(1, (self.size)**2), randint(1, (self.size)**2)
            if end>=start or start in used_cells or end in used_cells:
                continue
            used_cells.add(start)
            used_cells.add(end)
            self.snakes[start] = end
            snakes_cnt+=1

    
    def move_player(self, player:Player, steps:int):
        if player.position+steps>(self.size)**2:
            return
        player.position+=steps
        if player.position in self.ladders:
            print(f"{player.id} climbed ladder")
            player.position  = self.ladders[player.position]
        elif player.position in self.snakes:
            print(f"{player.id} is bitten by snake")
            player.position  = self.snakes[player.position]

class Game:
    def __init__(self, no_of_dice, no_of_players, no_of_snakes, 
                no_of_ladders, size) -> None:
        self.dice = Dice(no_of_dice)
        self.board = Board(size, no_of_snakes, no_of_ladders)
        self.players = deque([Player(i+1) for i in range(no_of_players)])

    def start(self):
        while len(self.players)>1:
            player = self.players.popleft()
            steps = self.dice.roll()
            previous_pos = player.position
            print(player.id, player.position, "steps", steps)
            self.board.move_player(player, steps)
            if previous_pos!=player.position:
                print(f"{player.id} moved to {player.position}")
            if player.position==(self.board.size)**2:
                print(f"{player.id} won!!")
                continue
            
            self.players.append(player)

if __name__=="__main__":
    game = Game(2, 6, 20, 20, 10)
    game.start()
        
      