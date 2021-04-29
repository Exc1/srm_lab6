mat = [[16, -8, 0],
       [-7, -16, 5, -123],
       [4, 12, 3, -68],
       [-4, 12, -7, 104],
       [-1, 7, 20]]

mat1 = [[8, -2, 6],
        [-1, 6, -2, 3],
        [2, 10, -4, 8],
        [-1, 6, 5]]


def create_coef(mat):
    list = [[], []]
    list[0].append(-mat[0][1] / mat[0][0])
    list[1].append(mat[0][2] / mat[0][0])
    for i in range(1, len(mat)):
        if i == len(mat) - 1:
            list[0].append(0)
            list[1].append((mat[i][2] - (mat[i][0] * list[1][i - 1])) / (mat[i][1] + mat[i][0] * list[0][i - 1]))
            break
        list[0].append(-mat[i][2] / (mat[i][1] + mat[i][0] * list[0][i - 1]))
        list[1].append((mat[i][3] - (mat[i][0] * list[1][i - 1])) / (mat[i][1] + (mat[i][0] * list[0][i - 1])))
    return list


def get_x(list):
    res = []
    for i in range(len(list[0]) - 1, 0, -1):
        if i == len(list[0]) - 1:
            res.append(list[1][len(list[1]) - 1])
        res.append(list[0][i] * res[len(list[1]) - 1 - i] + list[1][i])
    return res


print(get_x(create_coef(mat)))
