import sys

def output():
    if not current_key:
        return

    result = 0
    for i in range(1, N+1):
       result += array_a[i] * array_b[i]

    if result:
        print current_key + "," + str(result)

# A: m x n B: n x p
N = 3

current_key = None
array_a = [0] * (N+1)
array_b = [0] * (N+1)

for line in sys.stdin:
    c_i, c_j, m_type, m_index, m_value = line.strip().split(",")
    key = c_i + "," + c_j
    if key != current_key:
        output()
        current_key = key
        array_a = [0] * (N+1)
        array_b = [0] * (N+1)
    
    if m_type == "A":
        array_a[int(m_index)] = int(m_value)
    elif m_type == "B":
        array_b[int(m_index)] = int(m_value)

output()
