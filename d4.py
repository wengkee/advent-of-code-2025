from util.data_file import DataFile


df = DataFile("data/d4.data")
df.convert_to_grid()

def can_lift_toilet_roll(df: DataFile, row, column):

    # print(f"row: {row}, column: {column}")
    if df.grid[row][column] == '.':
        return False

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1),  (1, 0),   (1, 1)
    ]

    surrounding_rolls = 0

    for dir_row, dir_col in directions:
        tmp_row, tmp_col = row + dir_row, column + dir_col

        if 0 <= tmp_row < df.grid_rows and 0 <= tmp_col < df.grid_cols:
            # print(df.grid[tmp_row][tmp_col])
            if df.grid[tmp_row][tmp_col] == '@':
                surrounding_rolls += 1

        if surrounding_rolls >= 4:
            return False

    return True

d1_rolls_of_paper = 0

for r in range(df.grid_rows):
    for c in range(df.grid_cols):
        d1_rolls_of_paper += 1 if can_lift_toilet_roll(df, r, c) else 0

print(d1_rolls_of_paper)

d2_rolls_of_paper = 0
while True:
    tmp_rolls_count = 0
    to_be_removed = []
    for r in range(df.grid_rows):
        for c in range(df.grid_cols):
            can_be_lifted = can_lift_toilet_roll(df, r, c)
            if can_be_lifted:
                tmp_rolls_count += 1
                to_be_removed.append((r, c))

    if tmp_rolls_count == 0:
        break

    d2_rolls_of_paper += tmp_rolls_count

    for tbr_r, tbr_c in to_be_removed:
        df.grid[tbr_r][tbr_c] = '.'


print(d2_rolls_of_paper)