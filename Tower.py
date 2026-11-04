n = int(input("Enter number of disks: "))

rods = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

step = 0

def display():
    print("A:", rods['A'])
    print("B:", rods['B'])
    print("C:", rods['C'])
    print("--------------------")


def hanoi(n, source, auxiliary, destination):
    global step

    if n == 1:
        # Move top disk
        disk = rods[source].pop()
        rods[destination].append(disk)

        step += 1

        print("\nStep", step)
        print("Move disk", disk, "from",
              source, "to", destination)

        display()
        return

    # Move n-1 disks to auxiliary
    hanoi(n-1, source, destination, auxiliary)

    # Move largest disk to destination
    hanoi(1, source, auxiliary, destination)

    # Move remaining disks to destination
    hanoi(n-1, auxiliary, source, destination)


print("Initial State:")
display()

print("Tower of Hanoi Solution:\n")

hanoi(n, 'A', 'B', 'C')

print("Final State:")
display()

print("Total Moves:", step)
print("Goal Achieved!")

# # Aim
# To implement the Tower of Hanoi problem using Recursion in Python and move all disks from the source rod (A) to the destination rod (C) using the auxiliary rod (B), following the rules of the Tower of Hanoi.
# Theory
# Tower of Hanoi is a mathematical puzzle and a classical problem in Artificial Intelligence that demonstrates recursion and problem-solving techniques.

# The problem consists of three rods (A, B, and C) and a number of disks of different sizes arranged on the source rod in decreasing order, with the largest disk at the bottom and the smallest disk at the top.

# The objective is to move all disks from the source rod to the destination rod using the auxiliary rod.

# The following rules must be followed:
# 1. Only one disk can be moved at a time.
# 2. Only the top disk of a rod can be moved.
# 3. A larger disk cannot be placed on a smaller disk.
# 4. All disks must be moved from the source rod to the destination rod while following these rules.
# The program uses recursion to solve the problem. The hanoi() function divides the problem into smaller subproblems:
# 1. Move the top \(n-1\) disks from the source rod to the auxiliary rod.
# 2. Move the largest remaining disk from the source rod to the destination rod.
# 3. Move the \(n-1\) disks from the auxiliary rod to the destination rod.
# The program uses a dictionary to store the disks on each rod and a global variable step to count the total number of moves. The display() function shows the current arrangement of disks after every move.

# The minimum number of moves required to solve the Tower of Hanoi problem is:
# \[
# T(n) = 2^n - 1
# \]

# Where n represents the number of disks.

# Result: The Tower of Hanoi problem is successfully implemented using recursion in Python, and all disks are moved from the source rod (A) to the destination rod (C) while following the given rules.