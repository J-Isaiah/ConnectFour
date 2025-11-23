from board import Board, Cell


def evaluate(board: Board, player: Cell) -> int:
    opp = Cell.RED if player == Cell.YELLOW else Cell.YELLOW

    rows_score = eval_rows(board=board, player=player, opp=opp)


def eval_rows(board: Board, player: Cell, opp: Cell):
    b = board.grid
    score = 0

    for row in range(Board.ROWS):
        for col in range(Board.COLUMNS - 3):
            window = [b[row][col], b[row][col + 1], b[row][col + 2], b[row][col + 3]]
            own_spaces = window.count(player)
            empty = window.count(Cell.EMPTY)
            opp_spaces = window.count(opp)

            if own_spaces == 4:
                score += 1000
            elif own_spaces == 3 and empty == 1:
                score += 50

            elif own_spaces == 2 and empty == 2:
                score += 25

            elif own_spaces == 1 and empty == 1:
                score += 10

            if opp_spaces == 3 and empty == 1:
                score -= 80
            elif opp_spaces == 2 and empty == 2:
                score -= 50

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
                score -= 80
            elif opp_spaces == 2 and empty == 2:
                score -= 50

    return score


# def eval_pos_diagnals(board:Board, player:Cell, opp:Cell):
#     b = board.grid
#     score = 0
#     for col in range(Board.ROWS):
#         for row in range(Board.ROWS):
