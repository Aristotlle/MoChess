from tkinter import *
from PIL import Image, ImageTk

class ChessBoard():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}')
        self.chess_board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
            ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
            ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
            ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.selected_piece_position = None
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.load_pieces_img()
        self.draw_chessboard()
        self.root.mainloop()
    def load_pieces_img(self):
        self.piece_images = {
            'wR': ImageTk.PhotoImage(Image.open('images/wRook.png')),
            'wB': ImageTk.PhotoImage(Image.open('images/wBishop.png')),
            'wQ': ImageTk.PhotoImage(Image.open('images/wQueen.png')),
            'wK': ImageTk.PhotoImage(Image.open('images/wKing.png')),
            'wN': ImageTk.PhotoImage(Image.open('images/wKnight.png')),
            'wP': ImageTk.PhotoImage(Image.open('images/wPawn.png')),
            'bR': ImageTk.PhotoImage(Image.open('images/bRook.png')),
            'bB': ImageTk.PhotoImage(Image.open('images/bBishop.png')),
            'bQ': ImageTk.PhotoImage(Image.open('images/bQueen.png')),
            'bK': ImageTk.PhotoImage(Image.open('images/bKing.png')),
            'bN': ImageTk.PhotoImage(Image.open('images/bKnight.png')),
            'bP': ImageTk.PhotoImage(Image.open('images/bPawn.png')),
            'e': ImageTk.PhotoImage(Image.open('images/empty.png'))
        }

    def button_clicked(self, row, col):
        if self.selected_piece_position is None:
            if self.chess_board[row][col] == 'e': #tikrina ar nepaspaustas tuscias langelis.
                return
            self.selected_piece_position = (row, col)
            print("Button clicked:", row, col)
        else:
            target_row, target_col = row, col
            source_row, source_col = self.selected_piece_position
            moving_piece = self.chess_board[source_row][source_col]
            if moving_piece != 'e':
                if self.valid_move(moving_piece,source_row,source_col,target_row,target_col):
                    self.chess_board[target_row][target_col] = moving_piece
                    self.chess_board[source_row][source_col] = 'e'
                    self.update_board()

            # Reset the selected piece position
            self.selected_piece_position = None

    def valid_move(self,moving_piece, source_row, source_col, target_row, target_col):
        print("Validating move:", moving_piece, source_row, source_col, target_row, target_col)
        if moving_piece == 'wP':
            return self.wpawn_movement(source_row,source_col,target_row,target_col)
    def wpawn_movement(self, source_row, source_col, target_row, target_col):
        print("Checking wpawn_movement:", source_row, source_col, target_row, target_col)
        if target_col != source_col:
            return False
        if source_row == 6:
            if target_row == source_row -2:
                print("taip")
                return True
        if source_row == 6:
            if target_row == source_row -1:
                return True
        if source_row != 6:
            if target_row == source_row -1:
                return True
        else:
            print("Ne")

    # def king_movement(self):

    # def queen_movement(self):
    #
    # def bishop_movement(self):
    #
    # def rook_movement(self):
    #
    # def knight_movement(self):



    def update_board(self):
        for row in range(8):
            for col in range(8):
                label = self.chess_board[row][col]
                self.buttons[row][col].config(image=self.piece_images[label])

    def draw_chessboard(self):
        for row in range(8):
            for col in range(8):
                label = self.chess_board[row][col]
                button = Button(self.root, image=self.piece_images[label], width=60, height=60,
                                command=lambda row=row, col=col: self.button_clicked(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

if __name__ == '__main__':
    chess = ChessBoard(600, 600)

