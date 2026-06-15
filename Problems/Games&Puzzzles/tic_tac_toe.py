from abc import ABC, abstractmethod


# -------- Player --------
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


# -------- Strategy --------
class WinningStrategy(ABC):
    @abstractmethod
    def check_win(self, board, row, col, symbol):
        pass


class RowColDiagonalStrategy(WinningStrategy):
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def check_win(self, board, row, col, symbol):
        val = 1 if symbol == "X" else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val
        if row + col == self.n - 1:
            self.anti_diag += val

        return (
            abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diag) == self.n or
            abs(self.anti_diag) == self.n
        )


# -------- Board --------
class Board:
    def __init__(self, n):
        self.n = n
        self.grid = [[" "]*n for _ in range(n)]

    def make_move(self, row, col, symbol):
        if self.grid[row][col] != " ":
            raise ValueError("Cell already occupied")
        self.grid[row][col] = symbol

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)

    def display(self):
        for r in self.grid:
            print(" | ".join(r))
            print("-" * (self.n * 4 - 1))


# -------- Game --------
class Game:
    def __init__(self, n, players, strategy):
        self.board = Board(n)
        self.players = players
        self.strategy = strategy
        self.turn = 0

    def play(self):
        while True:
            player = self.players[self.turn]
            self.board.display()
            print(f"{player.name} ({player.symbol}) turn")

            try:
                r = int(input("Row: "))
                c = int(input("Col: "))

                self.board.make_move(r, c, player.symbol)

                if self.strategy.check_win(self.board.grid, r, c, player.symbol):
                    self.board.display()
                    print(f"{player.name} wins!")
                    return

                if self.board.is_full():
                    self.board.display()
                    print("Draw!")
                    return

                self.turn ^= 1  # switch player

            except Exception as e:
                print(e)


# -------- Run --------
if __name__ == "__main__":
    p1 = Player("P1", "X")
    p2 = Player("P2", "O")

    game = Game(
        n=3,
        players=[p1, p2],
        strategy=RowColDiagonalStrategy(3)
    )
    game.play()