import math

from util.data_file import DataFile

point_at_zero = 0
point_passed_zero = 0
def move(cur: int, pos: str):
    num = int(pos[1:]) * (1 if pos[0] == "R" else -1)

    tmp_cur = cur + num

    global point_passed_zero, point_at_zero
    point_passed_zero += abs(tmp_cur) // 100 + (cur and tmp_cur <= 0)

    cur = tmp_cur % 100
    if cur == 0:
        point_at_zero += 1

    return cur


if __name__ == "__main__":

    cur = 50
    df = DataFile("data/d1.data")
    for pos in df.lines:
        cur = move(cur, pos)

    print(point_at_zero)
    print(point_passed_zero)