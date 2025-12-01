from enum import Enum, auto
from game_engine.board import Board, Cell
from game_engine.errors import (
    ConnectFourError,
    InvalidMoveError,
    ColumnFullError,
    GameOverError,
)


class MoveResult(Enum):
    VALID = auto()
    WIN = auto()
    DRAW = auto()


class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.cur_player = Cell.RED
        self.winner = None

    def play_move(self, col):
        if not self.board.is_valid_move(col):
            raise InvalidMoveError(f"Column {col} is not a valid move")
        elif self.game_over():
            raise GameOverError("Cannot Play Move after game is over.")

        self.board.drop_piece(col, self.cur_player)

        if self.board.check_win(self.cur_player):
            self.winner = self.cur_player
            return MoveResult.WIN

        elif self.board.is_full():
            return MoveResult.DRAW

        self.cur_player = Cell.RED if self.cur_player == Cell.YELLOW else Cell.YELLOW

        return MoveResult.VALID

    def game_over(self) -> bool:
        return self.winner is not None or self.board.is_full()
