
# y↓  x→  -> (value, is_exists)
def get_cell(table, y, x, y_clip=False, x_clip=False):
    if y < 0 or y >= len(table):
        if y_clip:
            pass # TODO
        else:
            return None, False
    if x < 0 or x >= len(table[0]):
        if x_clip:
            pass # TODO
        else:
            return None, False
    return table[y][x], True

# y↓  x→
def get_neighbours(table, y, x, y_clip=False, x_clip=False, allow_oob_cells=False):
    ret = []
    if not allow_oob_cells:
        _, exit = get_cell(table, y, x, y_clip, x_clip)
        if not exit:
            return []
    for yy in [-1, 0, 1]:
        for xx in [-1, 0, 1]:
            if yy == 0 and xx == 0:
                continue
            cell, exist = get_cell(table, y+yy, x+xx, y_clip, x_clip)
            if exist:
                ret.append(cell)
    return ret


def test_get_cell():
    table = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
    ]
    cases = [
        #[-1, 0, False, False, (None, False)],
    ]
    for y in range(4):
        for x in range(5):
            cases.append([y,x, False, False, (table[y][x], True)]) 
    for y in range(-4, 8):
        for x in range(-5, 10):
            if y > -1 and y < 5:
                continue
            if x > -1 and x < 6:
                continue
            cases.append([y,x, False, False, (None, False)]) 
    for cse in cases:
        result = get_cell(table, cse[0], cse[1], cse[2], cse[3])
        if result != cse[4]:
            print("cell", cse, result)


def test_get_neigbours():
    table = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
    ]
    cases = [
        [0, 0, False, False, False, ["b", "f", "g"]],                          # a
        [0, 1, False, False, False, ["a", "c", "f", "g", "h"]],                # b
        [0, 2, False, False, False, ["b", "d", "g", "h", "i"]],                # c
        [0, 3, False, False, False, ["c", "e", "h", "i", "j"]],                # d
        [0, 4, False, False, False, ["d", "i", "j"]],                          # e
        [1, 0, False, False, False, ["a", "b", "g", "k", "l"]],                # f
        [1, 1, False, False, False, ["a", "b", "c", "f", "h", "k", "l", "m"]], # g
        [1, 2, False, False, False, ["b", "c", "d", "g", "i", "l", "m", "n"]], # h
        [1, 3, False, False, False, ["c", "d", "e", "h", "j", "m", "n", "o"]], # i
        [1, 4, False, False, False, ["d", "e", "i", "n", "o"]],                # j
        [2, 0, False, False, False, ["f", "g", "l", "p", "q"]],                # k
        [2, 1, False, False, False, ["f", "g", "h", "k", "m", "p", "q", "r"]], # l
        [2, 2, False, False, False, ["g", "h", "i", "l", "n", "q", "r", "s"]], # m
        [2, 3, False, False, False, ["h", "i", "j", "m", "o", "r", "s", "t"]], # n
        [2, 4, False, False, False, ["i", "j", "n", "s", "t"]],                # o
        [3, 0, False, False, False, ["k", "l", "q"]],                          # p
        [3, 1, False, False, False, ["k", "l", "m", "p", "r"]],                # q
        [3, 2, False, False, False, ["l", "m", "n", "q", "s"]],                # r
        [3, 3, False, False, False, ["m", "n", "o", "r", "t"]],                # s
        [3, 4, False, False, False, ["n", "o", "s"]],                          # t
    ]
    for y in range(-4, 8):
        for x in range(-5, 10):
            if y > -1 and y < 5:
                continue
            if x > -1 and x < 6:
                continue
            cases.append([y,x, False, False, False, []])
    for cse in cases:
        result = get_neighbours(table, cse[0], cse[1], cse[2], cse[3], cse[4])
        if result != cse[5]:
            print("neighbours", cse, result)


test_get_cell()
test_get_neigbours()



