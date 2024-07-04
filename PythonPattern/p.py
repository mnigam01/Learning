from abc import ABC, abstractmethod
from enum import Enum
from collections import deque

class MarkType(Enum):
    X = 1
    O = 2
    # = 3

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

class Board:
    def __init__(self, size, no_of_players=2):
        self.size = size
        self.initiliase()

    def initiliase(self):
        self.board = [[None]*self.size for _ in range(self.size)]
        self.players = deque()
        self.players.append(Player("player1", MarkType.X))
        self.players.append(Player("player2", MarkType.O))

    def add(self, x, y, mark):
        if self.board[x][y]!=None:
            return False
        self.board[x][y] = mark
        return True

    def isWinner(self, row, col, mark):
        ans = True
        for j in range(self.size):
            if self.board[row][j]!=mark:
                ans = False
                break
        if ans:
            return True
            
        ans = True
        for i in range(self.size):
            if self.board[i][col]!=mark:
                ans = False
                break
        if ans:
            return True
        
        
        ans = True
        for i in range(self.size):
            if self.board[i][i]!=mark:
                ans = False
                break
        if ans:
            return True
        
        ans = True
        for i in range(self.size):
            if self.board[i][-(i+1)]!=mark:
                ans = False
                break
        if ans:
            return True
        
    def display_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.board[i][j]!=None:
                    row.append(self.board[i][j].name)
                else:
                    row.append(" ")
            print(" ".join(row)) 
        
        
        
        

class Game:
    def __init__(self, size=3):
        self.board = Board(size=3)

    def start(self):
        while True:
            player = self.board.players.popleft()
            print(player.name,"please enter row and col")
            x,y = list(map(int, input().split()))
            if not self.board.add(x,y, player.mark):
                self.board.players.appendleft(player)
                continue
            self.board.display_board()
            if self.board.isWinner(x,y,player.mark):
                print(player.name, "won the match!!")
                break
            self.board.players.append(player)
            
                
        
if __name__=="__main__":
    game = Game(3)
    game.start()

    