from util.data_file import DataFile

def has_repeating_pattern(num):
    s = str(num)
    length = len(s)

    invalid_d1, invalid_d2 = False, False
    for k in range(2, length + 1):
        if length % k != 0:
            continue

        part_len = length // k
        part = s[:part_len]

        if part * k == s:
            invalid_d1 = True if k == 2 else False
            invalid_d2 = True
            break


    return invalid_d1, invalid_d2


df = DataFile("data/d2.data")
invalid_sum_1 = invalid_sum_2 = 0
for line in df.lines:

    ranges = line.split(",")
    for s, e in (r.split("-") for r in ranges):

        start = int(s)
        end = int(e)

        for n in range(start, end + 1):
            is_invalid_1, is_invalid_2 = has_repeating_pattern(n)
            if is_invalid_1:
                invalid_sum_1 += n
            if is_invalid_2:
                invalid_sum_2 += n

print(invalid_sum_1, invalid_sum_2)