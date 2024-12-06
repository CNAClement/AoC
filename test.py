import numpy as np

o = np.genfromtxt(
    r"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\6.txt", dtype=str, deletechars="", comments="_", delimiter=1
)
o = np.pad(o, 1)
directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
start = np.array(np.hstack((o == "^").nonzero()))

# part 1
direction = 0
a = o.copy()
pos = start
while a[tuple(pos + directions[direction])] != "0":
    if a[tuple(pos + directions[direction])] == "#":
        direction = (direction + 1) % 4
    else:
        pos = pos + directions[direction]
        a[tuple(pos)] = "X"
print(sum((a == "X").flatten()))

# part 2
b = a.copy()
count = 0
for coord in np.dstack((b == "X").nonzero()).squeeze():
    direction = 0
    a = o.copy()
    a[tuple(coord)] = "#"
    turns = np.zeros(o.shape, dtype=int)
    pos = start
    while a[tuple(pos + directions[direction])] != "0":
        if a[tuple(pos + directions[direction])] == "#":
            if turns[tuple(pos)] & (1 << direction):
                count += 1
                break
            turns[tuple(pos)] += 1 << (direction)
            direction = (direction + 1) % 4
        else:
            pos = pos + directions[direction]
            a[tuple(pos)] = "X"
print(count)