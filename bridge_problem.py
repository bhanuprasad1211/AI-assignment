from collections import deque

people = {'Amogh': 5, 'Ameya': 10, 'Grandma': 20, 'Grandpa': 25}
times = list(people.values())

def bfs_bridge_problem():
    start = (frozenset(people.keys()), frozenset(), 0, 'L')  # (left, right, time, umbrella_side)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (left, right, time_so_far, side), path = queue.popleft()

        if time_so_far > 60:
            continue
        if not left:
            return path + [("All crossed", time_so_far)]

        state_key = (left, right, time_so_far, side)
        if state_key in visited:
            continue
        visited.add(state_key)

        if side == 'L':
            for a in left:
                for b in left:
                    if a >= b:
                        new_left = left - {a, b}
                        new_right = right | {a, b}
                        new_time = time_so_far + max(people[a], people[b])
                        queue.append(((new_left, new_right, new_time, 'R'),
                                      path + [(f"{a} and {b} cross", new_time)]))
        else:
            for a in right:
                new_left = left | {a}
                new_right = right - {a}
                new_time = time_so_far + people[a]
                queue.append(((new_left, new_right, new_time, 'L'),
                              path + [(f"{a} returns", new_time)]))
    return None

solution = bfs_bridge_problem()
for step in solution:
    print(step)
