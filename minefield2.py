import random
w, h, mines = 6, 5, 20
# gene field
field = [[0 for y in range(h)] for x in range(w)]
# put mine on random position
for i in range(mines):
    rx = random.randint(0, w - 1)
    ry = random.randint(0, h - 1)
    field[rx][ry] = "M"
# print field
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()