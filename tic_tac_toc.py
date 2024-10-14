import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ayesha Naz | Tic Tac Toe")
        
        # Create a canvas to hold the grid of buttons
        self.canvas = tk.Canvas(root)
        self.canvas.pack(expand=True, fill='both')

        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.lines = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            self.canvas.grid_rowconfigure(i, weight=1)
            self.canvas.grid_columnconfigure(i, weight=1)
            for j in range(3):
                button = tk.Button(self.canvas, text="", font=('normal', 40), width=5, height=2, 
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                self.buttons[i][j] = button
        
    def on_button_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and self.check_winner() is False:
            self.buttons[i][j]["text"] = self.player
            if self.check_winner():
                self.draw_winning_line()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.lines = [(i, 0, i, 2)]
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.lines = [(0, i, 2, i)]
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.lines = [(0, 0, 2, 2)]
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.lines = [(0, 2, 2, 0)]
            return True
        
        return False
    
    def is_board_full(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def draw_winning_line(self):
        cell_width = self.canvas.winfo_width() / 3
        cell_height = self.canvas.winfo_height() / 3
        for line in self.lines:
            x1 = line[1] * cell_width + cell_width / 2
            y1 = line[0] * cell_height + cell_height / 2
            x2 = line[3] * cell_width + cell_width / 2
            y2 = line[2] * cell_height + cell_height / 2
            self.canvas.create_line(x1, y1, x2, y2, width=4, fill='red')

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.player = "X"
        self.canvas.delete("all")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    game = TicTacToe(root)
    root.mainloop()
