# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
matrix = [[0, "v1", "v2", "v3", "v4"],
          ["u1", 0, 1, 0, 0],
          ["u2", 0, 0, 1, 0],
          ["u3", 1, 1, 0, 1],
          ["u4", 1, 0, 1, 0]]
rows = 4
columns = 4
reg_matrix = [[None for j in range(columns)] for i in range(rows)]
reg_matrix = matrix[1:]

print(reg_matrix)


# matrix_list = matrix.tolist()
# cosine_sim = cosine_similarity(matrix)
# cosine_sim_list = cosine_sim.tolist()
# print(cosine_sim_list)
