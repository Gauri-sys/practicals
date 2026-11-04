rooms = {}

for room in ['A', 'B', 'C', 'D', 'E']:
    rooms[room] = input(
        f"Enter status of Room {room} (Dirty/Clean/Partially Dirty): "
    ).strip().title()

location = input("Enter starting location (A/B/C/D/E): ").upper()

step = 1
room_list = list(rooms.keys())

print("\nInitial Environment:", rooms)
print("Initial Location:", location)
print("\nVacuum Cleaner Working:\n")

while any(status != 'Clean' for status in rooms.values()):

    print("Step:", step)
    print("Current Location:", location)
    print("Room Status:", rooms[location])

    if rooms[location] in ['Dirty', 'Partially Dirty']:
        action = "SUCK"
        rooms[location] = 'Clean'

    else:
        index = room_list.index(location)

        # Find the next room that is not clean
        next_room = None

        for room in room_list[index + 1:]:
            if rooms[room] != 'Clean':
                next_room = room
                break

        if next_room is None:
            for room in room_list[:index]:
                if rooms[room] != 'Clean':
                    next_room = room
                    break

        if next_room is not None:
            action = "MOVE TO " + next_room
            location = next_room

    print("Action:", action)
    print("Updated Environment:", rooms)
    print("-" * 30)

    step += 1

print("\nFinal Environment:", rooms)
print("All rooms are CLEAN.")
print("Goal Achieved!")

# To implement a Simple Reflex Vacuum Cleaner Agent that cleans five rooms (A, B, C, D, and E) based on their current conditions (Dirty, Clean, or Partially Dirty) and achieves the goal of making all rooms clean.
# Theory
# A Vacuum Cleaner Agent is a simple reflex agent in Artificial Intelligence that observes the condition of its current location and performs an appropriate action based on predefined rules.

# In this practical, the environment consists of five rooms: A, B, C, D, and E. Each room can have one of three conditions: Dirty, Clean, or Partially Dirty. The user provides the initial status of all rooms and the starting location of the vacuum cleaner.

# The agent follows these rules:
# 1. If the room is Dirty: The vacuum cleaner performs the SUCK action and makes the room Clean.
# 2. If the room is Partially Dirty: The vacuum cleaner performs the SUCK action and makes the room Clean.
# 3. If the room is Clean: The vacuum cleaner moves to the next room that is not clean.
# 4. If all rooms are Clean: The agent stops working and the goal is achieved.
# The program uses a dictionary to store room conditions and a list to maintain the room sequence. A while loop continues execution until all rooms become clean.

# The main objective of this agent is to clean the entire environment by selecting suitable actions based on the current room's condition.

# Result: The Simple Reflex Vacuum Cleaner Agent is successfully implemented to clean all five rooms and achieve the goal state in which every room is clean