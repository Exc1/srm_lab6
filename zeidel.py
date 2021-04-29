mat_my = [[-14, 6, 1, -5, 95],
          [-6, 27, 7, -6, -41],
          [7, -5, -23, -8, 69],
          [3, -8, -7, 26, 27]]

mat1 = [[10, 1, 1, 12],
        [2, 10, 1, 13],
        [2, 2, 10, 14]]


def get_mat_default(mat):
    for line in range(len(mat)):
        for ai in range(len(mat[line])):
            if mat[line][ai] == mat[line][line]:
                continue
            if mat[line][ai] == mat[line][len(mat[line]) - 1]:
                mat[line][ai] = mat[line][ai] / mat[line][line]
                continue
            mat[line][ai] = -mat[line][ai] / mat[line][line]

    return mat


def get_first_x(mat):
    res_x = []
    for row in range(len(mat)):
        res_x.append(mat[row][len(mat[row]) - 1] / 10)
    return res_x


def mat_min_mat(mat_f, mat_s):
    mat_res = []
    ans = 0
    for i in range(len(mat_f)):
        mat_res.append(mat_f[i] - mat_s[i])
    for i in range(len(mat_res)):
        ans += abs(mat_res[i])
    return abs(ans / len(mat_res))


def solution(first_x, mat, eps):
    last_kof = []
    prev_kof = []
    for i in first_x:
        last_kof.append(i)
    for i in first_x:
        prev_kof.append(i * 2)

    while mat_min_mat(first_x, prev_kof) > eps:

        for i in range(len(first_x)):
            prev_kof[i] = first_x[i]
        for row in range(len(mat)):
            first_x[row] = last_kof[row]
            for col in range(len(mat[row]) - 1):
                if mat[row][col] == mat[row][row]:
                    continue
                first_x[row] += mat[row][col] * first_x[col]
        print(first_x)
    return first_x


print(solution(get_first_x(mat1), get_mat_default(mat1), 0.01))
