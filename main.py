p1 = [' ', 2, 3, 1, 2]


def l_to_r_down(row1, col1):
    i = row1
    j = col1
    l_to_r_down_counter = 0
    i += 1
    j += 1
    while (i < len(p1) and j < len(p1)):

        if (p1[j] == i):
            l_to_r_down_counter += 1
            print(f"{i - 1},{j - 1} is attacking {i},{j}")
        i += 1
        j += 1
    return l_to_r_down_counter


def l_to_r_up(row1, col1):
    i = row1
    j = col1
    l_to_r_up_counter = 0
    i -= 1
    j += 1
    while (i > 0 and j < len(p1)):

        if (p1[j] == i):
            l_to_r_up_counter += 1
            print(f"{i + 1},{j - 1} is attacking {i},{j}")
        i -= 1
        j += 1
    return l_to_r_up_counter


def l_to_r(row1, col1):
    l_to_r_counter = 0
    l_to_r_counter += l_to_r_down(row1, col1)
    l_to_r_counter += l_to_r_up(row1, col1)
    return l_to_r_counter


def r_to_l_up(row1, col1):
    i = row1
    j = col1
    r_to_l_up_counter = 0
    i -= 1
    j -= 1
    while (i > 0 and j > 0 ):

        if (p1[j] == i):
            r_to_l_up_counter += 1
            print(f"{i + 1},{j + 1} is attacking {i},{j}")
        i -= 1
        j -= 1
    return r_to_l_up_counter


def r_to_l_down(row1, col1):
    i = row1
    j = col1
    r_to_l_down_counter = 0
    i += 1
    j -= 1
    while (i < len(p1) and j > 0):

        if (p1[j] == i):
            r_to_l_down_counter += 1
            print(f"{i - 1},{j + 1} is attacking {i},{j}")
        i += 1
        j -= 1
    return r_to_l_down_counter


def r_to_l(row1, col1):
    r_to_l_counter = 0
    r_to_l_counter += r_to_l_up(row1, col1)
    r_to_l_counter += r_to_l_down(row1, col1)
    return r_to_l_counter


def checking_diagonals(row1, col1):
    attacking_diagonals = 0
    attacking_diagonals += l_to_r(row1, col1)
    attacking_diagonals += r_to_l(row1, col1)
    return attacking_diagonals


def isAttack(row1, col1, row2, col2):
    attacking_counter = 0
    if (row1 == row2):
        attacking_counter = 1
    else:
        attacking_counter += checking_diagonals(row1, col1)


if __name__ == '__main__':
    ls = [3,2,1,0]
    for j in range(1, len(p1)):
        iteration = 0
        i = j
        #     for i in p1:
        k = 1
        for a in range(3,0,-1):
            #         row = i
            col = j
            if p1[j] == ' ':
                continue
            else:
                print(p1[j], j)
                isAttack(p1[j], j, p1[col + k], col + k)
            k += 1
            iteration += 1