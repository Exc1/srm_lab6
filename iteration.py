import numpy as np


def generate_a(mat3):
    mat = mat3
    for i in range(len(mat)):
        for a in range(len(mat[1])):
            if mat[i][a] == mat[i][i]:
                continue
            if mat[i][a] == mat[i][len(mat[1]) - 1]:
                mat[i][a] = mat[i][a] / mat[i][i]
                continue
            mat[i][a] = -mat[i][a] / mat[i][i]
        mat[i][i] = 0
    return mat


def mat_multiply(mat):
    res_mat = [[], []]
    for i in range(len(mat[1]) - 1):
        res = 0
        for a in range(len(mat[1]) - 1):
            res += mat[i][a] * mat[a][len(mat[1]) - 1]
        res_mat[0].append(res)
        res_mat[1].append(mat[i][len(mat[1]) - 1])
    return res_mat


def mat_add(mat):
    res = []
    for i in range(len(mat[1])):
        res.append(mat[0][i] + mat[1][i])
    return res


def Gaus(mat):
    if mat[0][0] == 0:
        temp = mat[0]
        mat[0] = mat[1]
        mat[1] = temp
    for i in range(len(mat) - 1):
        for a in range(len(mat) - 1):
            if a + 1 + i == len(mat):
                if a + 1 + i == len(mat[i]):
                    break
                continue
            min_part = -(mat[a + 1 + i][i] / mat[i][i])
            for b in range(len(mat[i])):
                mat[a + 1 + i][b] = mat[a + 1 + i][b] + (mat[i][b] * min_part)
    return mat


def determinant(gaus_mat):
    res = 1
    for i in range(len(gaus_mat)):
        res *= gaus_mat[i][i]
    return res


def multiply_mat_mat(mat_a, mat_b):
    mid_res = []
    for line in range(len(mat_a)):
        mid_res.append(0)
        for ai in range(len(mat_a[line])):
            mid_res[line] += mat_a[line][ai] * mat_b[ai]
    return mid_res


def mat_min_mat(mat_f, mat_s):
    mat_res = []
    ans = 0
    for i in range(len(mat_f)):
        mat_res.append(mat_f[i] - mat_s[i])
    for i in range(len(mat_res)):
        ans += abs(mat_res[i])
    return abs(ans / len(mat_res))


def mat_plus_mat(mat_f, mat_s):
    mat_res = []
    for i in range(len(mat_f)):
        mat_res.append(mat_f[i] + mat_s[i])
    return mat_res


def iteration(a_mat, b_mat, x1_mat, eps):
    # a_mat - alpha mat n*n
    # b_mat - betta(1*3), also x0_mat
    # x1_mat - solved for x1

    prev_x = b_mat
    next_x = x1_mat

    while mat_min_mat(next_x, prev_x) > eps:
        prev_x = next_x
        next_x = mat_plus_mat(b_mat, multiply_mat_mat(a_mat, prev_x))

    return next_x


mat_my = [[-14, 6, 1, -5, 95],
          [-6, 27, 7, -6, -41],
          [7, -5, -23, -8, 69],
          [3, -8, -7, 26, 27]]

mat1 = [[10, 1, 1, 12],
        [2, 10, 1, 13],
        [2, 2, 10, 14]]

all_mat = generate_a(mat1)
a_gen = []
b_gen = []
for i in range(len(all_mat)):
    b_gen.append(all_mat[i][len(all_mat[i]) - 1])
    a_gen.append([])
    for a in range(len(all_mat[i]) - 1):
        a_gen[i].append(all_mat[i][a])

result = mat_add(mat_multiply(all_mat))

print(iteration(a_gen, b_gen, result, 0.01))
