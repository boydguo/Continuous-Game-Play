# Course: CS 30
# Period: 1
# Date created: 02/02/21
# Date last modified: 02/02/21
# Name: Boyd Guo
# Description: Continuous Game Play


# Defines a formatted menu for directions
def print_directions():
    print(31 * "-", "COMPASS", 32 * "-")
    print("1. North\n2. South\n3. East\n4. West")
    print(72 * "-")


# Defines a formatted menu for actions
def print_actions():
    print(31 * "-", "ACTIONS", 32 * "-")
    print("1. Interact\n2. Rest\n3. Continue\n4. Quit")
    print(72 * "-")


# Movement menu
def movement():
    while True:
        print_directions()
        direction = input("Please choose a direction: ").lower()
        if direction == "north":
            print("\nYou begin to head north\n")
            break
        elif direction == "south":
            print("\nYou begin to head south\n")
            break
        elif direction == "east":
            print("\nYou begin to head east\n")
            break
        elif direction == "west":
                print("\nYou begin to head west\n")
                break
        else:
                print("\nInvalid direction...\n")
                continue


# Action menu with quit command
def actions():
    while True:
        print_actions()
        action = input("Please choose an action: ").lower()
        if action == "interact":
            print("\nYou interact with your surroundings\n")
            actions()
            break
        elif action == "rest":
            print("\nYou rest your tired body\n")
            actions()
            break
        elif action == "continue":
            print("\nYou continue on your way\n")
            movement()
            break
        elif action == "quit":
            print('You have quit the game')
            exit(0)
        else:
            print("\nInvalid action...\n")
            continue


# starting the code
movement()


# continuing the code
while True:
    actions()
