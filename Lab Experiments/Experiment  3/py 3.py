from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        print((x, y))

        if x == target or y == target:
            print("\nTarget Reached!")
            return

        # Fill Jug 1
        queue.append((jug1, y))

        # Fill Jug 2
        queue.append((x, jug2))

        # Empty Jug 1
        queue.append((0, y))

        # Empty Jug 2
        queue.append((x, 0))

        # Pour Jug 1 -> Jug 2
        transfer = min(x, jug2 - y)
        queue.append((x - transfer, y + transfer))

        # Pour Jug 2 -> Jug 1
        transfer = min(y, jug1 - x)
        queue.append((x + transfer, y - transfer))

# Driver Code
jug1 = 4
jug2 = 3
target = 2

water_jug(jug1, jug2, target)
