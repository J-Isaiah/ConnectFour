from enum import Enum, auto


class Cell(Enum):
    EMPTY = auto()
    RED = auto()
    YELLOW = auto()


class Board:
    ROWS = 6
    COLUMNS = 7
    CONNECT_N = 4

    def __init__(self) -> None:
        self.grid = [
            [Cell.EMPTY for _ in range(self.COLUMNS)] for _ in range(self.ROWS)
        ]

    def is_valid_move(self, column: int) -> bool:
        """Checks to see if there is a valid move avaliable at the current column

        Args:
            column (int): Column of the piece that is intended to drop

        Returns:
            bool: Bool that represents if the column has a valid move avaliable
        """
        if column < 0 or column >= self.COLUMNS:
            return False

        return self.grid[0][column] == Cell.EMPTY

    def valid_moves(self) -> list[int]:
        """Returns all column indexes that have an avalibale move

        Returns:
            list[int]: A list of all indicies that have an open space to drop a piece into
        """
        return [col for col in range(self.COLUMNS) if self.grid[0][col] == Cell.EMPTY]

    def drop_piece(self, col: int, player: Cell) -> None | int:
        """Handles adding a piece to the board

        Args:
            col (int): Column that piece is attempting to be placed
            player (Cell): Player piece color

        Returns:
            None | int: None if invalid move else the row that the piece was placed at
        """
        if not self.is_valid_move(column=col):
            return None

        for row in range(self.ROWS - 1, -1, -1):
            if self.grid[row][col] == Cell.EMPTY:
                self.grid[row][col] = player
                return row

    def copy(self) -> "Board":
        """Generates a deep copy of the current board state and returns the seperated boards

        Returns:
            Board: Deep copy of the current board state
        """
        new = Board()
        new.grid = [row[:] for row in self.grid]
        return new

    def check_win(self, player: Cell) -> bool:
        """Checks if a winning condition is meet on the board

        Args:
            player (Cell): What player should be expecting the winning condition

        Returns:
            bool: If the win condition was meet or not
        """
        # Horizontal check (row)
        for row in self.grid:
            num_in_row = 0
            for cell in row:
                if cell == player:
                    num_in_row += 1
                else:
                    num_in_row = 0

                if num_in_row == self.CONNECT_N:
                    return True
        # Vertical Check (Col)
        for col in range(self.COLUMNS):
            num_in_row = 0
            for row in self.grid:
                cell = row[col]
                if cell == player:
                    num_in_row += 1
                else:
                    num_in_row = 0
                if num_in_row == self.CONNECT_N:
                    return True
        # Negative diaginal (top Left corner to bottom right corner)

        for r in range(0, self.ROWS - self.CONNECT_N + 1):
            for c in range(0, self.COLUMNS - self.CONNECT_N + 1):
                cur_row = r
                cur_col = c
                num_in_row = 0
                while cur_row < self.ROWS and cur_col < self.COLUMNS:
                    cell = self.grid[cur_row][cur_col]

                    if cell == player:
                        num_in_row += 1
                    else:
                        num_in_row = 0
                    if num_in_row == self.CONNECT_N:
                        return True

                    cur_row += 1
                    cur_col += 1

        # Positive Diagnal Top right corner to bottom left corner

        for r in range(0, self.ROWS - self.CONNECT_N + 1):
            for c in range(self.CONNECT_N - 1, self.COLUMNS):

                num_in_row = 0
                cur_row = r
                cur_col = c

                while cur_row < self.ROWS and cur_col >= 0:
                    cell = self.grid[cur_row][cur_col]

                    if cell == player:
                        num_in_row += 1
                    else:
                        num_in_row = 0

                    if num_in_row == self.CONNECT_N:
                        return True

                    cur_row += 1  # move DOWN
                    cur_col -= 1  # move LEFT

        return False

    def is_full(self) -> bool:
        """Checks to see if there are still playable states on the board

        Returns:
            bool: If there is not a valid move to make returns True if board is full
        """
        for cell in self.grid[0]:
            if cell == Cell.EMPTY:
                return False
        return True
