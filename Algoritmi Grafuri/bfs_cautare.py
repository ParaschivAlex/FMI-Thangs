R, C = 5, 7
sr, sc = 0, 0
rq, cq = [], []

matrix = [['S', '.', '.', '#', '.', '.', '.'],
          ['.', '#', '.', '.', '.', '#', '.'],
          ['.', '#', '.', '.', '.', '.', '.'],
          ['.', '.', '#', '#', '.', '.', '.'],
          ['#', '.', '#', 'E', '.', '#', '.']]

move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False

visited = [[False for _ in range(R)] for _ in range(C)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def solve():
    global nodes_left_in_layer, nodes_in_next_layer, reached_end, move_count
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while rq:
        r = rq.pop(0)
        c = cq.pop(0)
        if matrix[r][c] == 'E':
            reached_end = True
            break
        explore_neighbours(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


def explore_neighbours(r, c):
    global nodes_in_next_layer
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        if visited[rr][cc]:
            continue
        if matrix[rr][cc] == '#':
            continue
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1


print(solve())
