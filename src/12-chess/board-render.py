"""玩法 12：国际象棋棋盘 SVG 渲染
用法: python board-render.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" out.svg
依赖: python-chess (pip install python-chess)
"""
import sys
import chess
import chess.svg


def render(fen, out):
    board = chess.Board(fen)
    svg = chess.svg.board(board, size=420)
    with open(out, "w") as f:
        f.write(svg)
    print(f"legal moves: {board.legal_moves.count()} -> {out}")


if __name__ == "__main__":
    fen = sys.argv[1] if len(sys.argv) > 1 else chess.STARTING_FEN
    render(fen, sys.argv[2] if len(sys.argv) > 2 else "board.svg")
