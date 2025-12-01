from game_engine.board import Board, Cell
from game_engine.evaluation import evaluate


class Ai:
    def __init__(self, ai_player: Cell):
        self.ai = ai_player
        self.human = Cell.YELLOW if ai_player == Cell.RED else Cell.RED

    def get_best_move(self, board: Board, depth: int = 6) -> int | None:
        score, col = self.minimax(
            board=board,
            depth=depth,
            alpha=-(10**12),
            beta=10**12,
            maximizing=True,
        )
        return col

    def minimax(
        self, board: Board, depth: int, alpha: int, beta: int, maximizing: bool
    ):

        if board.check_win(self.ai):
            return 10**9, None
        if board.check_win(self.human):
            return -(10**9), None
        if board.is_full():
            return 0, None
        if depth == 0:
            return evaluate(board, player=self.ai), None

        valid_moves = board.valid_moves()
        center = Board.COLUMNS // 2
        ordered_moves = sorted(valid_moves, key=lambda c: abs(center - c))

        best_col = None

        if maximizing:
            value = -(10**12)
            for col in ordered_moves:
                node = board.copy()
                node.drop_piece(col, self.ai)

                if node.check_win(self.ai):
                    return 10**9, col

                score, _ = self.minimax(node, depth - 1, alpha, beta, False)

                if score > value:
                    value = score
                    best_col = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return value, best_col

        else:
            value = 10**12
            for col in ordered_moves:
                node = board.copy()
                node.drop_piece(col, self.human)

                if node.check_win(self.human):
                    return -(10**9), col

                score, _ = self.minimax(node, depth - 1, alpha, beta, True)

                if score < value:
                    value = score
                    best_col = col

                beta = min(beta, value)
                if alpha >= beta:
                    break

            return value, best_col
