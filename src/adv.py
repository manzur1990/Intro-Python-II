from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item('bow')),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item('helmet')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item('sword')),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item('shield')),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item('empty chest')),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your name?")

player = Player(player_name, room['outside'])

print(f"Welcome {player.name}!")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    current_room = player.room
    player_inventory = [x.name for x in player.inventory] if len(
        player.inventory) else "Empty"
    room_inventory = [x.name for x in current_room.item] if len(
        current_room.item) else "Empty Room"

    print(
        f" === Entered {player.room.room_name}, {current_room.room_description} ===")
    print(f"*You have found a {room_inventory}")

    print(f"Inventory: [{len(player.inventory)}]")
    print(f"Bag: {player_inventory}")

    move = input(
        '[Movement]: [N]/[S]/[W]/[E]. [Take/Drop]: [T]/[D]. [Q]-Quit \n :> ')

    action = move[0:4]
    item = move[5:]

    if move.lower() == 'n':
        if current_room.n_to is not None:
            player.room = current_room.n_to
            print(f"\t==> Moving north")
        else:
            print("XXX Can't go that way XXX")
    elif move.lower() == 's':
        if current_room.s_to is not None:
            player.room = current_room.s_to
            print(f"\t==> Moving south")
        else:
            print("XXX Can't go that way XXX")
    elif move.lower() == 'e':
        if current_room.e_to is not None:
            player.room = current_room.e_to
            print(f"\t==> Moving east")
        else:
            print("XXX Can't go that way XXX")
    elif move.lower() == 'w':
        if current_room.w_to is not None:
            player.room = current_room.w_to
            print(f"\t==> Moving West")
        else:
            print("XXX Can't go that way XXX")

    elif action.lower() == 'take':
        item_name_list = [i.name for i in current_room.item]
        item_index = item_name_list.index(item)
        player.take(current_room.item[item_index])
        current_room.remove_item(item_index)

    elif action.lower() == 'd':
        item_name_list = [i.name for i in player.inventory]
        item_index = item_name_list.index(item)
        current_room.add_item(player.inventory[item_index])
        player.drop(item_index)

    elif move == 'q':
        exit()
