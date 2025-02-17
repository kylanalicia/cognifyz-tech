# Map of rooms, paths, and hidden treasures in the maze 
rooms = {
    'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar'},
    'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal'},
    'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff'},
    'Bazaar': {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids'},
    'Meat Locker': {'South': 'Bazaar', 'East': 'Quicksand Pit', 'Item': 'Fig'},
    'Quicksand Pit': {'West': 'Meat Locker', 'Item': 'Robe'},
    'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry'},
    'Dojo': {'West': 'Bazaar', 'Boss': 'Shadow Man'}
}

# Inventory of loot collected 
inventory = []

# Starting point in maze 
current_room = "Liminal Space"

# The code that lets you control your destiny (Main gameplay loop)
while True:
    print(f"\nYou're currently navigating the {current_room}.\nInventory: {inventory}")
    
    # 🔍 Check if there’s any item you can loot in the current room 
    if "Item" in rooms[current_room]:
        item = rooms[current_room]["Item"]
        if item not in inventory:
            print(f"You detect a {item} shimmering in the distance...")

    # Boss encounter (Battle the ultimate force if you have the right items!)
    if "Boss" in rooms[current_room]:
        if len(inventory) < 6:
            print(f"You've been annihilated by {rooms[current_room]['Boss']}! Seems like you're missing some essential loot... Try again.")
            break
        else:
            print(f"Victory! You've successfully defeated {rooms[current_room]['Boss']} and achieved greatness!")
            break

    #  Accepting user input and parsing 
    user_input = input("\nEnter your move (e.g., 'go north', 'get Crystal', 'exit'):\n").lower().split()

    if len(user_input) < 2:
        print("Invalid command detected. Use 'go <direction>', 'get <item>', or 'exit' to control your fate.")
        continue

    action, target = user_input[0], " ".join(user_input[1:])
    
    # Traverse the map and find new dimensions 
    if action == "go":
        if target.capitalize() in rooms[current_room]:
            current_room = rooms[current_room][target.capitalize()]
            print(f"You boldly travel {target}... The universe shifts around you.")
        else:
            print(f"You can't go {target} from this room. The space-time continuum doesn’t allow it!")

    # Collecting loot - Gather items and power up your journey 
    elif action == "get":
        if "Item" in rooms[current_room] and target.capitalize() == rooms[current_room]["Item"]:
            if target.capitalize() not in inventory:
                inventory.append(target.capitalize())
                print(f"You’ve successfully looted the {target}. Your inventory is expanding!")
            else:
                print(f"You already possess the {target}. Are you hoarding it?")
        else:
            print(f"No such item '{target}' in this room. Are you sure it exists?")

    #  Exit - Conquer the game or retreat to the digital realm 
    elif action == "exit":
        print("Exiting the game. Until next time, adventurer!")
        break

    #  Invalid command handling - Only the worthy can make the right moves 
    else:
        print("Invalid command. Make sure to use 'go <direction>', 'get <item>', or 'exit' to control your destiny.")
