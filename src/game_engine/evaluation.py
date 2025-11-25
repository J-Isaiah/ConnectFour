from board import Board, Cell


def evaluate(board: Board, player: Cell) -> int:
    opp = Cell.RED if player == Cell.YELLOW else Cell.YELLOW

    total_score = 0
    total_score += eval_rows(board=board, player=player, opp=opp)
    total_score += eval_cols(board=board, player=player, opp=opp)
    total_score += eval_pos_diagonals(board=board, player=player, opp=opp)
    total_score += eval_neg_diagonals(board=board, player=player, opp=opp)

    center_col = Board.COLUMNS // 2
    center_array = [board.grid[r][center_col] for r in range(Board.ROWS)]
    center_count = center_array.count(player)
    total_score += center_count * 3

    return total_score


def score_window(window, player, opp) -> int:
    score = 0
    own = window.count(player)
    opp_spaces = window.count(opp)
    empty = window.count(Cell.EMPTY)

    # scoring (same as rows)
    if own == 4:
        score += 1000
    elif own == 3 and empty == 1:
        score += 50
    elif own == 2 and empty == 2:
        score += 25

    if opp_spaces == 3 and empty == 1:
        score -= 90
    elif opp_spaces == 2 and empty == 2:
        score -= 50

    return score


def eval_rows(board: Board, player: Cell, opp: Cell):
    b = board.grid
    score = 0

    for row in range(Board.ROWS):
        for col in range(Board.COLUMNS - 3):
            window = [b[row][col], b[row][col + 1], b[row][col + 2], b[row][col + 3]]

            score += score_window(window=window, player=player, opp=opp)
    return score


def eval_cols(board: Board, player: Cell, opp: Cell):
    b = board.grid
    score = 0

    for col in range(Board.COLUMNS):
        for row in range(Board.ROWS - 3):  # slide the window DOWN
            window = [
                b[row][col],
                b[row + 1][col],
                b[row + 2][col],
                b[row + 3][col],
            ]

            score += score_window(window=window, player=player, opp=opp)
    return score


def eval_pos_diagonals(board: Board, player: Cell, opp: Cell):
    score = 0
    for row in range(Board.ROWS - 3):
        for col in range(Board.COLUMNS - 3):
            window = [
                board.grid[row][col],
                board.grid[row + 1][col + 1],
                board.grid[row + 2][col + 2],
                board.grid[row + 3][col + 3],
            ]

            score += score_window(window, player=player, opp=opp)
    return score


def eval_neg_diagonals(board: Board, player: Cell, opp: Cell):
    score = 0
    for row in range(Board.ROWS - 3):
        for col in range(3, Board.COLUMNS):
            window = [
                board.grid[row][col],
                board.grid[row + 1][col - 1],
                board.grid[row + 2][col - 2],
                board.grid[row + 3][col - 3],
            ]

            score += score_window(window=window, player=player, opp=opp)
    return score
