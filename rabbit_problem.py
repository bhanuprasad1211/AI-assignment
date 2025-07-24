from collections import deque

initial_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']
goal_state = ['W', 'W', 'W', '_', 'E', 'E', 'E']

def get_possible_moves(state):
    moves = []
    for i in range(7):
        if state[i] == '_':
            if i >= 1 and state[i - 1] == 'E':
                new = state[:]
                new[i], new[i - 1] = new[i - 1], new[i]
                moves.append(new)
            if i >= 2 and state[i - 2] == 'E':
                new = state[:]
                new[i], new[i - 2] = new[i - 2], new[i]
                moves.append(new)
            if i <= 5 and state[i + 1] == 'W':
                new = state[:]
                new[i], new[i + 1] = new[i + 1], new[i]
                moves.append(new)
            if i <= 4 and state[i + 2] == 'W':
                new = state[:]
                new[i], new[i + 2] = new[i + 2], new[i]
                moves.append(new)
    return moves

def bfs(start):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal_state:
            return path
        visited.add(tuple(current))
        for move in get_possible_moves(current):
            if tuple(move) not in visited:
                queue.append((move, path + [move]))
    return None

def dfs(start, path, visited):
    if start == goal_state:
        return path
    visited.add(tuple(start))
    for move in get_possible_moves(start):
        if tuple(move) not in visited:
            result = dfs(move, path + [move], visited)
            if result:
                return result
    return None

bfs_result = bfs(initial_state)
dfs_result = dfs(initial_state, [initial_state], set())

print("BFS Solution:")
for step in bfs_result:
    print(step)

print("\nDFS Solution:")
for step in dfs_result:
    print(step)

