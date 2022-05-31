import numpy as np
from docplex.mp.model import Model
import matplotlib.pyplot as plt

# read data from file
TXT_FILE = 'Data/Q15.txt'
with open(TXT_FILE) as f:
    risk_map = f.read()
# convert data to a matrix
risk_map = risk_map.split('\n')[:-1]
risk_map = np.array([list(map(int, list(row))) for row in risk_map])

# risk_map = [[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
#             [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
#             [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
#             [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
#             [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
#             [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
#             [1, 3, 5, 9, 9, 1 ,2, 4, 2, 1],
#             [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
#             [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
#             [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]]
# risk_map = np.array(risk_map)

m, n = risk_map.shape
I = range(m); J = range(n)

mdl = Model()

x = [[mdl.binary_var(name = 'x_' + str(i) + '_' + str(j)) for j in J] for i in I]
# x = mdl.binary_var_matrix(m, n, name = 'x')

mdl.add(x[0][0] == 1)
mdl.add(x[m - 1][n - 1] == 1)
mdl.add(x[0][1] + x[1][0] == 1)
mdl.add(x[m - 1][n - 2] + x[m - 2][n - 1] == 1)

for i in range(1, m - 1):
    for j in range(1, n - 1):
        mdl.add(x[i - 1][j] + x[i + 1][j] + x[i][j - 1] + x[i][j + 1] >= 2*x[i][j])
        mdl.add(x[i - 1][j] + x[i + 1][j] + x[i][j - 1] + x[i][j + 1] <= 2*(2 - x[i][j]))

for j in range(1, n - 2):
    mdl.add(x[0][j - 1] + x[0][j + 1] + x[1][j] >= 2*x[0][j])
    mdl.add(x[0][j - 1] + x[0][j + 1] + x[1][j] <= 2*(2 - x[0][j]))
    mdl.add(x[m - 1][j - 1] + x[m - 1][j + 1] + x[m - 2][j] >= 2*x[m - 1][j])
    mdl.add(x[m - 1][j - 1] + x[m - 1][j + 1] + x[m - 2][j] <= 2*(2 - x[m - 1][j]))
for i in range(1, m - 2):
    mdl.add(x[i - 1][0] + x[i + 1][0] + x[i][1] >= 2*x[i][0])
    mdl.add(x[i - 1][0] + x[i + 1][0] + x[i][1] <= 2*(2 - x[i][0]))
    mdl.add(x[i - 1][n - 1] + x[i - 1][n - 1] + x[i][n - 2] >= 2*x[i][n - 1])
    mdl.add(x[i - 1][n - 1] + x[i - 1][n - 1] + x[i][n - 2] <= 2*(2 - x[i][n - 1]))

for i in I:
    mdl.add(mdl.sum(x[i][j] for j in J) >= 1)
for j in J:
    mdl.add(mdl.sum(x[i][j] for i in I) >= 1)

for i in range(m - 2):
    for j in range(n - 2):
        mdl.add(x[i][j] + x[i][j + 1] + x[i + 1][j] + x[i + 1][j + 1] <= 3)

total_risk = mdl.sum(mdl.sum(risk_map[i][j]*x[i][j] for i in I) for j in J)

mdl.minimize(total_risk)

msol = mdl.solve(log_output = False)
# mdl.print_information()
print(mdl.solve_details)
print(msol[total_risk])

map_x = []; map_y = []
x_result = []
for i in I:
    temp_j = []
    for j in J:
        xij = msol[x[i][j]]
        temp_j.append(xij)
        if xij >= 0.99:
            map_x.append(i)
            map_y.append(j)
    x_result.append(temp_j)
x_result = np.array(x_result)
print(x_result)
# plt.scatter(x = map_x, y = map_y)
