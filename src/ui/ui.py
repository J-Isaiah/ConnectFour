import sys
import os

# Make /src importable at runtime (Streamlit doesn’t auto-detect like PyCharm)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import streamlit as st
from game_engine.game import Game, MoveResult
from game_engine.board import Cell
from game_engine.ai import Ai


st.set_page_config(page_title="Connect 4 AI", layout="centered")

if "game" not in st.session_state:
    st.session_state.game = Game()

if "ai" not in st.session_state:
    st.session_state.ai = Ai(ai_player=Cell.YELLOW)

game = st.session_state.game
ai = st.session_state.ai


def render_board(board):
    for row in board.grid:
        cols = st.columns(7)
        for i, cell in enumerate(row):
            if cell == Cell.EMPTY:
                cols[i].markdown(
                    "<div style='font-size: 36px;'>⚪</div>", unsafe_allow_html=True
                )
            elif cell == Cell.RED:
                cols[i].markdown(
                    "<div style='font-size: 36px;'>🔴</div>", unsafe_allow_html=True
                )
            else:
                cols[i].markdown(
                    "<div style='font-size: 36px;'>🟡</div>", unsafe_allow_html=True
                )


def handle_human_move(col):
    if game.game_over():
        return

    if game.cur_player != ai.human:
        return

    result = game.play_move(col)

    if result in (MoveResult.WIN, MoveResult.DRAW):
        return

    handle_ai_move()


def handle_ai_move():
    if game.game_over():
        return

    if game.cur_player != ai.ai:
        return

    _, ai_col = ai.minimax(
        board=game.board,
        alpha=-1_000_000_000,
        beta=1_000_000_000,
        maximizing=True,
        depth=6,
    )

    if ai_col is not None:
        game.play_move(ai_col)


def main():
    st.title("Connect Four AI")

    cols = st.columns(7)
    for i in range(7):
        if cols[i].button(f"↓ {i+1}", key=f"btn_{i}"):
            handle_human_move(i)

    render_board(game.board)

    if game.winner is not None:
        if game.winner == Cell.RED:
            st.success("🔴 You Win!")
        else:
            st.error("🟡 AI Wins!")
    elif game.board.is_full():
        st.info("It's a draw!")

    if st.button("Restart Game"):
        st.session_state.game = Game()
        st.session_state.ai = Ai(ai_player=Cell.YELLOW)


if __name__ == "__main__":
    main()
