from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

class PieceType(Enum):
    X=1
    O=2

class PlayingPiece:
    def __init__(self, piece_type : PieceType) -> None:
        self.piece_type = piece_type

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)


class Board:
    def __init__(self, size : int) -> None:
        self._size = size
        self.board = [[None for _ in range(self._size)] for _ in range(self._size)]
    

    def get_free_cells(self):
        free_spaces = []
        for i in range(self._size):
            for j in range(self._size):
                if not self.board[i][j]:
                    free_spaces.append([i,j])
        return free_spaces
        

    def print_board(self):
        for i in range(self._size):
            row = []
            for j in range(self._size):
                if not self.board[i][j]:
                    row.append(" ")
                else:
                    row.append(self.board[i][j].piece_type.name)
            print(" ".join(row))


    def add_piece(self, row, col, playing_piece):
        if self.board[row][col]!=None:
            return False
        self.board[row][col] = playing_piece
        return True
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size

class Player:
    def __init__(self, name: str, playing_piece: PlayingPiece):
        self._name = name
        self._playing_piece = playing_piece

    @property
    def name(self):
        return self._name

    @property
    def playing_piece(self):
        return self._playing_piece

    @name.setter
    def name(self, name):
        self._name = name

    @playing_piece.setter
    def playing_piece(self, playing_piece):
        self._playing_piece = playing_piece


"""
if you want size to be dynamic then you can pass into init below and pass in initilaize_game, similarly
for players you can pass a list and this can be created in if __name__ = "__main__"
"""

class Game:
    def __init__(self):   
        self.players = deque()
        self.game_board = None
        self.initialize_game()

    def initialize_game(self):
        # Creating 2 Players
        cross_piece = PlayingPieceX()
        player1 = Player(name="Player1", playing_piece=cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player(name="Player2", playing_piece=noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board
        self.game_board = Board(3)

    
    
    def start_game(self):
        no_winner = True
        while no_winner:
            player = self.players.popleft()
            
            free_spaces = self.game_board.get_free_cells()
            if len(free_spaces)==0:
                no_winner = False
                continue
            # print(player.name)
            print(f"Player:  {player.name} enter row and columns: ")
            row, col = list(map(int, input().split()))
            print()

            if not self.game_board.add_piece(row,col, player.playing_piece):
                print("incorrect position, try again")
                self.players.appendleft(player)
                continue
            self.game_board.print_board()

            self.players.append(player)
            if self.is_there_winner(row, col, player.playing_piece):
                return f"{player.name} won"
        
        return "tie"
    
    def is_there_winner(self,row, col, playing_piece):
        #checking columns
        tot = 0
        size = self.game_board.size

        board = self.game_board.board
        
        for j in range(size):
            if board[row][j]==playing_piece:
                tot += 1
        if (tot==size):
            return True
        
        tot = 0
        for i in range(size):
            if board[i][col]==playing_piece:
                tot += 1
        if (tot==size):
            return True
        
        tot = 0
        for i in range(size):
            if board[i][i]==playing_piece:
                tot += 1
        if (tot==size):
            return True
        
        tot = 0
        for i in range(size):
            if board[i][-(i+1)]==playing_piece:
                tot += 1
        if (tot==size):
            return True
        
        return False

if __name__=="__main__":
    game = Game()
    print(game.start_game())

        

