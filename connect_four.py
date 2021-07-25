class ConnectFour:

    # Notes:
    # 1. restrict bounds of user input
    # 2. Errors with number of marks to win
    def __init__(self):

        self._board = None

    def run(self):

        winner = False
        columns = int(input("How many columns: "))
        rows = int(input("How many rows: "))
        win_length = int(input("Number to win: "))

        print("Rows: " + str(rows))
        print("Columns: " + str(columns))

        self._board = [[" " for _ in range(columns)] for _ in range(rows)]

        while not winner:

            column_select = int(input("Player 1 - Drop in Column: "))

            while self.column_full(column_select):
                print("Column is full. Please select another.")
                column_select = int(input("Player 1 - Drop in Column: "))

            self.drop("O", column_select)

            self.display_board()

            if self.check_win("O", win_length):
                print("Player 1 wins")
                winner = True

            if not winner:
                column_select = int(input("Player 2 - Drop in Column: "))

                while self.column_full(column_select):
                    print("Column is full. Please select another.")
                    column_select = int(input("Player 2 - Drop in Column: "))

                self.drop("X", column_select)

                self.display_board()

                if self.check_win("X", win_length):
                    print("Player 2 wins")
                    winner = True

    def column_full(self, column):

        return self._board[0][column - 1] != " "

    def drop(self, value, column):

        row_length = len(self._board)
        row_counter = row_length

        while (self._board[row_counter - 1][column - 1] != " ") and row_counter >= 0:
            row_counter = row_counter - 1

        self._board[row_counter - 1][column - 1] = value

    def check_win(self, value, win_length):

        seq_found = False
        max_hor = len(self._board[0]) - win_length
        max_vert = len(self._board) - win_length
        same_bool = True

        row_counter = 0
        column_counter = 0

        while (not seq_found) and (column_counter < len(self._board[0])):
            while (not seq_found) and (row_counter <= max_vert):

                same_bool = True

                for a in range(win_length):

                    same_bool = same_bool and (value == self._board[row_counter + a][column_counter])

                if same_bool:
                    seq_found = True

                row_counter = row_counter + 1

            row_counter = 0
            column_counter = column_counter + 1

        row_counter = 0
        column_counter = 0

        while (not seq_found) and (row_counter < len(self._board)):
            while (not seq_found) and (column_counter <= max_hor):

                same_bool = True

                for a in range(win_length):

                    same_bool = same_bool and (value == self._board[row_counter][column_counter + a])

                if same_bool:
                    seq_found = True

                column_counter = column_counter + 1

            column_counter = 0
            row_counter = row_counter + 1

        row_counter = 0
        column_counter = 0

        while (not seq_found) and (row_counter <= max_vert):
            while (not seq_found) and (column_counter <= max_hor):

                same_bool = True

                for a in range(win_length):
                    """print("Temp Value: " + temp_value)
                    print("Current: " + self._board[row_counter + a][column_counter])
                    print("Boolean: " + str(same_bool))"""

                    same_bool = same_bool and (value == self._board[row_counter + a][column_counter + a])

                if same_bool:
                    seq_found = True

                column_counter = column_counter + 1

            column_counter = 0
            row_counter = row_counter + 1

        row_counter = 0
        column_counter = 0

        while (not seq_found) and (row_counter <= max_vert):
            while (not seq_found) and (column_counter <= max_hor):

                same_bool = True

                for a in range(win_length):
                    """print("Temp Value: " + temp_value)
                    print("Current: " + self._board[row_counter + a][column_counter])
                    print("Boolean: " + str(same_bool))"""

                    same_bool = same_bool and (value == self._board[row_counter + (3 - a)][column_counter + a])

                if same_bool:
                    seq_found = True

                column_counter = column_counter + 1

            column_counter = 0
            row_counter = row_counter + 1

        return seq_found

    def display_board(self):

        for a in range(len(self._board)):
            print("|", end="")

            for b in range(len(self._board[0])):
                print(str(self._board[a][b]) + "|", end="")

            print()