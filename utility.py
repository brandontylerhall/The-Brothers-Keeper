import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_directions(directions, game_state, rooms):
    room = game_state['current_room']
    room_directions = list(rooms.get(room).keys())
    available_directions = []

    print(f"You're currently in: {game_state['current_room']}")

    for direction in directions:
        if direction in room_directions:
            available_directions.append(direction.capitalize())

    print('Your available directions are: {}'.format(', '.join(available_directions)))


def handle_help(inventory):
    commands = [
        'CLEAR -- Clears the screen.',
        'GO (DIRECTION/ROOM NAME) -- Go a direction.',
        "INVENTORY -- Shows what you're carrying.",
        'LOOK (OBJECT/DIRECTION) -- Look around, look at an object, etc.',
        'TAKE (ITEM) -- Take an item.',
        'USE (OBJECT) -- Use an object.'
    ]

    if 'map' in inventory:
        commands.insert(3, 'MAP -- Shows the map')

    print('\n'.join(commands))


def handle_inventory(game_state):
    inventory = game_state["inventory"]

    # checks if inventory is empty
    if not inventory:
        print('You aren\'t carrying anything.')
    else:
        print(f'Inventory: {", ".join(inventory)}')


def start_credits():
    print("-------------------- Welcome to The Brother's Keeper \U0001F642 Nice to have you --------------------\n\n"
          "Pay attention to the words in all CAPS.\n\n"
          "If you end up getting stuck, you can type 'help' to learn various "
          "commands that may be useful.\n\n"
          "Have fun and good luck!\n\n"
          "----------------------------------------------------------------------------------------------")
    time.sleep(5)
    clear()
    print("In the ancient land of Morytania, whispers of a hidden treasure have lured adventurers for centuries. \n"
          "Legend speaks of the Barrows Brothers, six powerful warriors laid to rest in a labyrinthine tomb, \n"
          "their spirits guarding a wealth of powerful artifacts. An old man, his eyes filled with a knowing glint, \n"
          "points you towards the eerie marshes of Mort'ton. 'Seek the Barrows,' he rasps, 'if you dare. But beware, \n"
          "the brothers' spirits are restless, and their treasures are not easily earned.' Driven by the promise of \n"
          "riches and glory, you venture to the swamps of Morytania, your heart pounding with anticipation and \n"
          "trepidation...\n")
    os.system("pause")
    clear()
