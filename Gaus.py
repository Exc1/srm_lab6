mat = [[10, 1, 1, 12],
       [2, 10, 1, 13],
       [2, 2, 10, 14]]

mat_to_rev = [[10, 1, 1, 1, 0, 0],
              [2, 10, 1, 0, 1, 0],
              [2, 2, 10, 0, 0, 1]]


def print_mat(mat):
    for i in range(len(mat)):
        print(mat[i])
    print("------")


mat2 = [[-9, 8, 8, 6, -81],
        [-7, -9, 5, 4, -50],
        [-3, -1, 8, 0, -69],
        [3, -1, -4, -5, 48]]

mat3 = [[-9, 8, 8, 6, -81, 32],
        [-7, -9, 5, 4, -50, 32],
        [-3, -1, 8, 0, -69, 32],
        [3, -1, -4, -5, 48, 32],
        [3, -1, -4, -5, 48, 32]]


def Gaus(mat):
    for i in range(len(mat) - 1):
        for a in range(len(mat) - 1):
            if a + 1 + i == len(mat):
                if a + 1 + i == len(mat[i]) - 1:
                    break
                continue
            min_part = -(mat[a + 1 + i][i] / mat[i][i])
            for b in range(len(mat[i])):
                mat[a + 1 + i][b] = mat[a + 1 + i][b] + (mat[i][b] * min_part)
    return mat


def get_solution(mat):
    res = [1]
    for i in range(len(mat) - 1, -1, -1):
        x = 0
        z = 0
        for a in range(len(mat) - 1, 0, -1):
            z += 1
            if len(mat) - a == len(res):
                break
            x += mat[i][a] * res[z]
        res.append((mat[i][len(mat)] - x) / mat[i][i])
    del res[0]
    return res


print(Gaus(mat))


def determinant(gaus_mat):
    res = 1
    for i in range(len(gaus_mat) - 1):
        res *= mat[i][i]
    return res
