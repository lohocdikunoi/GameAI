import heapq

def heuristic(a, b):
    """Hàm heuristic với khoảng cách (Manhattan Distance)"""
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return dx + dy

def get_neighbors(maze, node):
    """Lấy danh sách hàng xóm, chỉ bao gồm các ô di chuyển theo hướng ngang và dọc"""
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0)  # Chỉ hướng ngang và dọc
    ]
    neighbors = []
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
            neighbors.append((x, y))
    return neighbors


def a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(maze, current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Trả về None nếu không tìm thấy đường đi
