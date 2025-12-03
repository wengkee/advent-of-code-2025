from util.data_file import DataFile

def max_subsequence_2(line):
    max_n = 0
    for j in range(len(line)):

        for k in range( j+1, len(line)):

            tmp = int(line[j] + line[k])

            if tmp > max_n:
                max_n = tmp
    return max_n

def max_subsequence_12(line):
    target = 12
    result = []
    start = 0

    for remaining in range(target, 0, -1):
        end = len(line) - remaining
        best_digit = "0"
        best_pos = start

        for i in range(start, end + 1):
            if line[i] > best_digit:
                best_digit = line[i]
                best_pos = i
                if best_digit == "9":
                    break

        result.append(best_digit)
        start = best_pos + 1

    return int("".join(result))

df = DataFile("data/d3.data")
d1_total = d2_total = 0
for line in df.lines:
    max12 = max_subsequence_12(line)
    d2_total += max12
    max2 = max_subsequence_2(line)
    d1_total += max2

print(d1_total)
print(d2_total)