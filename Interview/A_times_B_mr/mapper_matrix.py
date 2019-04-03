import sys
import os

# A: m x n B: n x p
M = 4
N = 3
P = 2

for line in sys.stdin:
    row, col, num = line.strip().split(",")

    #input_file = os.environ["map_input_file"]
    input_file = "B"
    if input_file.find("A") != -1:
        for i in range(1, P + 1):
            key = row + "," + str(i)
            value = ",".join(("A", col, num))
            print key + "," + value
    elif input_file.find("B") != -1:
        for i in range(1, M + 1):
            key = str(i) + "," + col
            value = ",".join(("B", row, num))
            print key + "," + value
