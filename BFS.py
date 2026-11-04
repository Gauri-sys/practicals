from collections import deque
sx = int(input("Enter start row: "))
sy = int(input("Enter start column: "))

gx = int(input("Enter goal row: "))
gy = int(input("Enter goal column: "))

ox = int(input("Enter obstacle row: "))
oy = int(input("Enter obstacle column: "))

start = (sx, sy)
goal = (gx, gy)

obstacles = [(ox, oy)]
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque([(start, [start])])
visited = {start}

while queue:

    pos, path = queue.popleft()

    print("Robot at:", pos)

    if pos == goal:
        print("\nGoal Reached!")
        print("Path:", path)
        print("Total Steps:", len(path) - 1)
        break

    for dx, dy in moves:

        x = pos[0] + dx
        y = pos[1] + dy

        new_pos = (x, y)

        if (0 <= x < 3 and 0 <= y < 3
            and new_pos not in obstacles
            and new_pos not in visited):

            visited.add(new_pos)
            queue.append((new_pos, path + [new_pos]))

else:
    print("No Path Found")


# To implement Breadth First Search (BFS) algorithm for solving a Robot Path Planning problem by finding the shortest path from a given start position to a goal position while avoiding obstacles in a 3 × 3 grid.
# Theory
# Breadth First Search (BFS) is an uninformed search algorithm used to explore nodes level by level. It starts from the initial state and explores all neighbouring states before moving to the next level.

# In Robot Path Planning, the environment is represented as a 3 × 3 grid, where each cell represents a possible position of the robot. The robot moves in four directions: up, down, left, and right.

# The user provides the starting position, goal position, and obstacle position. BFS finds a path from the start to the goal while avoiding obstacles.

# BFS uses the following concepts:
# 1. Queue: BFS uses a FIFO (First In First Out) queue to store positions to be explored.
# 2. Visited Set: It stores already visited positions to avoid revisiting the same cell.
# 3. Start State: The initial position of the robot.
# 4. Goal State: The destination position the robot needs to reach.
# 5. Obstacles: Blocked cells that the robot cannot enter.
# 6. Path: Stores the sequence of positions from the start to the goal.
# Since BFS explores positions level by level, it finds the shortest path in terms of the number of moves, provided every move has equal cost.

# If the goal is reached, the program displays the path and total number of steps. If no valid path exists, it displays "No Path Found".
# Algorithm
# 1. Start the program.
# 2. Accept the start position, goal position, and obstacle position from the user.
# 3. Initialize a queue with the start position and its path.
# 4. Initialize the visited set with the start position.
# 5. Repeat while the queue is not empty:
#    - Remove the first position from the queue.
#    - Check whether the current position is the goal.
#    - If the goal is reached, display the path and total steps.
#    - Otherwise, explore all four neighbouring positions.
#    - Check whether each position is within the grid, is not an obstacle, and has not been visited.
#    - Add valid positions to the visited set and queue.
# 6. If the queue becomes empty without reaching the goal, display "No Path Found".
# 7. Stop.
# Result: The Robot Path Planning problem is successfully implemented using the Breadth First Search (BFS) algorithm to find the shortest valid path while avoiding obstacles.