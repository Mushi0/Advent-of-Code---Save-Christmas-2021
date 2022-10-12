from dataclasses import dataclass
import numpy as np
from tqdm import tqdm

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

# Node class
@dataclass(frozen = False)
class node:
    dis: int = np.inf

@dataclass(frozen = False)
class node(node):
    prev: node = None

    def update_node(self, dis = np.inf, prev = None):
        self.dis = dis
        self.prev = prev

    def print_node(self):
        print(f'distance: {self.dis}, prev: {self.prev}')

# Defining the map
map = [[node() for i in I] for j in J]
Q = set([(i, j) for i in I for j in J])
map[0][0].update_node(0)

# Dijkstra's Algorithm
node_to_remove = (0, 0)
Q.remove(node_to_remove)

pbar = tqdm(total = m*n)
while not len(Q) == 0:
    x = node_to_remove[0]
    y = node_to_remove[1]
    shortest_distance = np.inf
    distance = map[x][y].dis
    if x + 1 < n and map[x + 1][y].dis > distance + risk_map[x + 1][y]:
        map[x + 1][y].update_node(distance + risk_map[x + 1][y], map[x][y])
    if y + 1 < m and map[x][y + 1].dis > distance + risk_map[x][y + 1]:
        map[x][y + 1].update_node(distance + risk_map[x][y + 1], map[x][y])
    if x - 1 >= 0 and map[x - 1][y].dis > distance + risk_map[x - 1][y]:
        map[x - 1][y].update_node(distance + risk_map[x - 1][y], map[x][y])
    if y - 1 >= 0 and map[x][y - 1].dis > distance + risk_map[x][y - 1]:
        map[x][y - 1].update_node(distance + risk_map[x][y - 1], map[x][y])

    for coord in Q:
        if map[coord[0]][coord[1]].dis < shortest_distance:
            shortest_distance = map[coord[0]][coord[1]].dis
            node_to_remove = coord
            print(f'Removing node {node_to_remove}, distance: {shortest_distance}')

    if node_to_remove == (n - 1, m - 1):
        print(f'Finished, distance: {map[n - 1][m - 1].dis}')
        break

    Q.remove(node_to_remove)

    pbar.update(1)

pbar.close()
