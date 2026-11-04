
j1 = int(input("Enter capacity of Jug 1: "))
j2 = int(input("Enter capacity of Jug 2: "))

g1 = int(input("Enter goal state of Jug 1: "))
g2 = int(input("Enter goal state of Jug 2: "))

start = (0, 0)
goal = (g1, g2)

stack = [(start, [])]
visited = set()

while stack:
    (a, b), path = stack.pop()

    if (a, b) in visited:
        continue

    visited.add((a, b))

    if (a, b) == goal:
        print("\nSolution Found!")
        print("Step 0: Start - Both jugs are empty")

        for i, (x, y, action) in enumerate(path):
            print("Step", i+1, ":", action, "->", (x, y))

        print("\nGoal Reached!")
        print("Final State:", goal)
        break

    states = [
        ((j1, b), "Fill Jug 1"),
        ((a, j2), "Fill Jug 2"),
        ((0, b), "Empty Jug 1"),
        ((a, 0), "Empty Jug 2"),
        ((a-min(a,j2-b), b+min(a,j2-b)), "Pour Jug 1 into Jug 2"),
        ((a+min(b,j1-a), b-min(b,j1-a)), "Pour Jug 2 into Jug 1")
    ]

    for s, action in states:
        if s not in visited:
            stack.append((s, path + [(s[0], s[1], action)]))

else:
    print("No Solution Found!")

# Aim
# To implement the Water Jug Problem using Depth First Search (DFS) in Python to obtain the required amount of water in two jugs by performing filling, emptying, and pouring operations.
# Theory
# The Water Jug Problem is a classical problem in Artificial Intelligence used to demonstrate state-space search and problem-solving techniques.

# In this problem, two jugs of different capacities are given. The objective is to obtain a specific amount of water in both jugs according to the given goal state, using a sequence of valid operations.

# Initially, both jugs are empty. The program takes the capacities of Jug 1 and Jug 2 and their required goal amounts as input.

# The following operations can be performed:
# 1. Fill Jug 1: Fill Jug 1 completely.
# 2. Fill Jug 2: Fill Jug 2 completely.
# 3. Empty Jug 1: Empty Jug 1 completely.
# 4. Empty Jug 2: Empty Jug 2 completely.
# 5. Pour Jug 1 into Jug 2: Transfer water from Jug 1 to Jug 2 until Jug 1 becomes empty or Jug 2 becomes full.
# 6. Pour Jug 2 into Jug 1: Transfer water from Jug 2 to Jug 1 until Jug 2 becomes empty or Jug 1 becomes full.
# The program uses the Depth First Search (DFS) algorithm to explore different possible states and find the required goal state.

# The following concepts are used:
# - State: Represents the amount of water in both jugs, written as (a, b).
# - Initial State: (0, 0), where both jugs are empty.
# - Goal State: The required amount of water in both jugs.
# - Stack: DFS uses a stack that follows the LIFO (Last In First Out) principle.
# - Visited Set: Stores already explored states to avoid revisiting them.
# - Path: Stores the sequence of actions performed to reach the goal state.
# If the goal state is found, the program displays the sequence of operations and the final state. Otherwise, it displays "No Solution Found".

# Result: The Water Jug Problem is successfully implemented using the Depth First Search (DFS) algorithm to find the required goal state through valid filling, emptying, and pouring operations.