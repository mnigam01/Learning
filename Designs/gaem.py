from abc import ABC
from enum import Enum
from collections import deque

class Player:
    def __init__(self, name:str, playing_piece):
        self.name = name
        self.playing_piece = playing_piece

class PlayingPieceEnum(Enum):
    X = 1
    O = 2
class PlayingPiece(ABC):
    def __init__(self, piece_type):
        self.piece_type = piece_type

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceEnum.X)

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceEnum.O)

class Board:
    def __init__(self,size):
        self.size = size
        self.board = [[None]*size for i in range(size)]
        
    def print_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if not self.board[i][j]:
                    row.append(" ")
                else:
                    row.append(self.board[i][j].piece_type.name)
            print(" ".join(row))
    def free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j]:
                    free_cells.append([i,j])
        return free_cells

    def add_piece(self,row, col, playing_piece):
        if self.board[row][col]:
            return False
        self.board[row][col] = playing_piece
        return True

class Game:
    def __init__(self):
        self.players = deque()
        self.initilize_game()

    def initilize_game(self):
        player1 = Player("Gaurav", PlayingPieceX())
        player2 = Player("Kishan", PlayingPieceO())
        self.players.append(player1)
        self.players.append(player2)
        self.board = Board(3)

    def start_game(self):
        found_winner = False
        while not found_winner:
            player = self.players.popleft()

            if not len(self.board.free_cells()):
                found_winner = True
                continue
            print(f"Player {player.name} enter row, col: ")
            row, col = list(map(int, input().split()))
            if not self.board.add_piece(row, col, player.playing_piece):
                print("Invalid move, try again")
                self.players.appendleft(player)
                continue
            self.board.print_board()
            if self.check_winner(row, col, player.playing_piece):
                return f"{player.name} won the match!!"
            self.players.append(player)
        return "tie"


    def check_winner(self,row, col, playing_piece):
        board = self.board.board
        size = self.board.size
        tot = 0
        for i in range(size):
            if board[row][i] == playing_piece:
                tot += 1
        if tot == size:
            return True


        tot = 0
        for i in range(size):
            if board[i][col] == playing_piece:
                tot += 1
        if tot == size:
            return True

        tot = 0
        for i in range(size):
            if board[i][i] == playing_piece:
                tot += 1
        if tot == size:
            return True


        tot = 0
        for i in range(size):
            if board[i][-(i+1)] == playing_piece:
                tot += 1
        if tot == size:
            return True

        return False

if __name__ == "__main__":
    game = Game()
    print(game.start_game())
            


"""
O(1) approach


from abc import ABC
from enum import Enum
from collections import deque, defaultdict

class Player:
    def __init__(self, name: str, playing_piece):
        self.name = name
        self.playing_piece = playing_piece

class PlayingPieceEnum(Enum):
    X = 1
    O = 2

class PlayingPiece(ABC):
    def __init__(self, piece_type):
        self.piece_type = piece_type

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceEnum.X)

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceEnum.O)

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]
        self.row_counts = defaultdict(lambda: defaultdict(int))
        self.col_counts = defaultdict(lambda: defaultdict(int))
        self.diag_counts = defaultdict(lambda: defaultdict(int))

    def print_board(self):
        for row in self.board:
            print(" ".join([cell.piece_type.name if cell else " " for cell in row]))

    def free_cells(self):
        return [[i, j] for i in range(self.size) for j in range(self.size) if not self.board[i][j]]

    def add_piece(self, row, col, playing_piece):
        if self.board[row][col]:
            return False
        self.board[row][col] = playing_piece
        piece_type = playing_piece.piece_type.name

        self.row_counts[row][piece_type] += 1
        self.col_counts[col][piece_type] += 1
        if row == col:
            self.diag_counts[0][piece_type] += 1
        if row + col == self.size - 1:
            self.diag_counts[1][piece_type] += 1
        return True

    def check_winner(self, row, col, playing_piece):
        piece_type = playing_piece.piece_type.name
        if (self.row_counts[row][piece_type] == self.size or
                self.col_counts[col][piece_type] == self.size or
                self.diag_counts[0][piece_type] == self.size or
                self.diag_counts[1][piece_type] == self.size):
            return True
        return False

class Game:
    def __init__(self):
        self.players = deque()
        self.initialize_game()

    def initialize_game(self):
        player1 = Player("Gaurav", PlayingPieceX())
        player2 = Player("Kishan", PlayingPieceO())
        self.players.append(player1)
        self.players.append(player2)
        self.board = Board(3)

    def start_game(self):
        found_winner = False
        while not found_winner:
            player = self.players.popleft()
            if not self.board.free_cells():
                found_winner = True
                continue
            print(f"Player {player.name} enter row, col: ")
            row, col = list(map(int, input().split()))
            if not self.board.add_piece(row, col, player.playing_piece):
                print("Invalid move, try again")
                self.players.appendleft(player)
                continue
            self.board.print_board()
            if self.board.check_winner(row, col, player.playing_piece):
                return f"{player.name} won the match!!"
            self.players.append(player)
        return "It's a tie!"

if __name__ == "__main__":
    game = Game()
    print(game.start_game())

"""