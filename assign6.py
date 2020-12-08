#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4
# 12345


def game_board(rows, columns):
    col = 0  # make col global
    max_columns = 6
    max_rows = 5
    rows = int(rows)
    columns = int(columns)
    if rows <= max_rows and columns <= max_columns:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * col)

        return True
    else:
        x = ""
        if rows > max_rows and columns > max_columns:
            x = "columns max(6) and rows max(5)"
        elif rows > max_rows:
            x += "rows"
        elif columns > max_columns:
            x += "columns"
        print("Ops!, can't create the game. Too many {0:s}.". format(x))

        return False


game_board(5, 6)
