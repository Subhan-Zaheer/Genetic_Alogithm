list_of_points = [[' ', 2, 1, 4, 3], [' ', 4, 1, 2, 4], [' ', 3, 3, 2, 4], [' ', 1, 3, 4, 2]]


def l_to_r_down(row1, col1, row2, col2, p):
    i = row1
    j = col1
    l_to_r_down_counter = 0
    i += 1
    j += 1
    while (i < len(p) and j < len(p)):

        if (i == row2 and j == col2):
            l_to_r_down_counter += 1
            # print(f"{i - 1},{j - 1} is attacking {i},{j}")
        i += 1
        j += 1
    return l_to_r_down_counter


def l_to_r_up(row1, col1, row2, col2, p):
    i = row1
    j = col1
    l_to_r_up_counter = 0
    i -= 1
    j += 1
    while (i > 0 and j < len(p)):

        if (i == row2 and j == col2):
            l_to_r_up_counter += 1
            # print(f"{i + 1},{j - 1} is attacking {i},{j}")
        i -= 1
        j += 1
    return l_to_r_up_counter


def l_to_r(row1, col1, row2, col2, p):
    l_to_r_counter = 0
    l_to_r_counter += l_to_r_down(row1, col1, row2, col2, p)
    l_to_r_counter += l_to_r_up(row1, col1, row2, col2, p)
    return l_to_r_counter


def r_to_l_up(row1, col1, row2, col2, p):
    i = row1
    j = col1
    r_to_l_up_counter = 0
    i -= 1
    j -= 1
    while (i > 0 and j > 0 ):

        if (i == row2 and j == col2):
            r_to_l_up_counter += 1
            # print(f"{i + 1},{j + 1} is attacking {i},{j}")
        i -= 1
        j -= 1
    return r_to_l_up_counter


def r_to_l_down(row1, col1, row2, col2, p):
    i = row1
    j = col1
    r_to_l_down_counter = 0
    i += 1
    j -= 1
    while (i < len(p) and j > 0):

        if (i == row2 and j == col2):
            r_to_l_down_counter += 1
            # print(f"{i - 1},{j + 1} is attacking {i},{j}")
        i += 1
        j -= 1
    return r_to_l_down_counter


def r_to_l(row1, col1, row2, col2, p):
    r_to_l_counter = 0
    r_to_l_counter += r_to_l_up(row1, col1, row2, col2, p)
    r_to_l_counter += r_to_l_down(row1, col1, row2, col2, p)
    return r_to_l_counter


def checking_diagonals(row1, col1, row2, col2, p):
    attacking_diagonals = 0
    attacking_diagonals += l_to_r(row1, col1, row2, col2, p)
    attacking_diagonals += r_to_l(row1, col1, row2, col2, p)
    return attacking_diagonals


def isAttack(row1, col1, row2, col2, p):
    attacking_counter = 0
    if (row1 == row2):
        attacking_counter = 1
    else:
        attacking_counter += checking_diagonals(row1, col1, row2, col2, p)

    return attacking_counter


def Finding_Attacking_pairs(p):
    ls = [3, 2, 1, 0]
    num = 0
    attacking_pairs = 0
    for j in range(1, len(p)):
        k = 1
        for a in range(ls[num], 0, -1):
            col = j
            if p[j] == ' ':
                continue
            else:
                # print(p[j], j)
                attacking_pairs += isAttack(p[j], j, p[col + k], col + k, p)
            k += 1
        num += 1
    print(p)
    print(f"Total attacking pairs are {attacking_pairs}\n")
    return attacking_pairs

if __name__ == '__main__':
    dict_of_non_attacking_pairs_of_each_pair ={}
    Probability_dict_of_non_attacking_pair = {}
    total_non_attacking_pairs = 0
    # As we have to find non-attacking pairs so will subtract attacking pairs by 6 because in worst case there will
    # be 6 attacking pairs in any population.
    for i in range(len(list_of_points)):
        attacks = Finding_Attacking_pairs(list_of_points[i])
        total_non_attacking_pairs += (6 - attacks)
        dict_of_non_attacking_pairs_of_each_pair[f"Non-Attacking pairs Point{i+1} are "] = 6-attacks
    for i in range(len(list_of_points)):
        Probability_dict_of_non_attacking_pair[f"Probability of Non-Attacking pairs of Point{i+1} is "] = int((list(dict_of_non_attacking_pairs_of_each_pair.items())[i][1]/total_non_attacking_pairs)*100)
    print(total_non_attacking_pairs)
    print(dict_of_non_attacking_pairs_of_each_pair)
    print(Probability_dict_of_non_attacking_pair)
    pass