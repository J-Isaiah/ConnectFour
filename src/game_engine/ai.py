from board import Board, Cell
from evaluation import  evaluate

class Ai:
    def __init__(self, ai_player: Cell):
        self.ai = ai_player
        self.human = Cell.YELLOW if ai_player == Cell.RED else Cell.RED

    def get_best_move(self, board):
        score, col = self.minimax(
        board=board,
        alpha=-1_000_000,
        beta=1_000_000,
        maximising=True,
        depth=5
    )
        return col

    def minimax(self,board: Board, alpha: int, beta:int, maximising: bool = True,depth:int = 5):
        best_move = None
        

       
        if board.check_win(self.ai):
            return 1000000, None

        elif board.check_win(self.human):
            return -1000000, None

        elif board.is_full():
            return 0, None
        
        elif depth == 0:
            return evaluate(board=board, player=self.ai), None
        
              

        if maximising:
            for move_col in board.valid_moves():
                node_board = board.copy()
                node_board.drop_piece(col=move_col, player=self.ai)
                score,_ = self.minimax(board=node_board, alpha=alpha, beta= beta, maximising= not maximising, depth=depth - 1)

                if score > alpha: 
                    alpha = score
                    best_move = move_col

                if alpha >= beta:
                    break

            return alpha, best_move



        else:
            for move_col in board.valid_moves():
                node_board = board.copy()
                node_board.drop_piece(col=move_col, player=self.human)
                score,_ = self.minimax(board=node_board, alpha=alpha, beta= beta, maximising= not maximising, depth=depth - 1)

                if score < beta: 
                    beta = score
                    best_move = move_col

                if alpha >= beta :
                    break
            return beta, best_move


