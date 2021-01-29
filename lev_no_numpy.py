# import numpy as np
#
#
# def lev(str1, str2):
#     x_len = len(str1) + 1
#     y_len = len(str2) + 1
#     matrix = [[0 for y in range(y_len)] for x in range(x_len)]
#     # matrix = np.zeros((x_len, y_len))
#
#     for x in range(x_len):
#         matrix[x][0] = x
#     for y in range(y_len):
#         matrix[0][y] = y
#
#     for x in range(1, x_len):
#         for y in range(1, y_len):
#             if str1[x-1] == str2[y-1]:
#                 matrix[x][y] = min(
#                     matrix[x][y - 1] + 1,
#                     matrix[x - 1][y - 1],
#                     matrix[x - 1][y] + 1
#                 )
#             else:
#                 matrix[x][y] = min(
#                     matrix[x][y - 1] + 1,
#                     matrix[x - 1][y - 1] + 1,
#                     matrix[x - 1][y] + 1
#                 )
#     return matrix
#
#
# m = lev('lawn', 'flaw')
# # m = lev('', 'hello')
# print(m)
# x1, y1 = len(m), len(m[0])
# print(f"({x1},{y1})")
# score = (m[x1 - 1][y1 - 1])
# print(f"Score = {score}")
f

