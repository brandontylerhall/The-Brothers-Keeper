import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def handle_help():
    print('Commands:\n'
          'CLEAR -- Clears the screen\n'
          'GO (DIRECTION/ROOM NAME) -- Go a direction (some rooms have single word movement commands)\n'
          'INVENTORY -- Shows what you\'re carrying\n'
          'LOOK (OBJECT/DIRECTION) -- Look around, look at an object, etc\n'
          # TODO: Maybe update to only show this if they're holding the map
          'MAP -- Shows the map\n'
          'TAKE (ITEM) -- Take an item\n'
          'USE (OBJECT) -- Use an object')


def handle_inventory(game_state):
    inventory = game_state["inventory"]

    # checks if inventory is empty
    if not inventory:
        print('You aren\'t carrying anything.')
    else:
        print(f'Inventory: {", ".join(inventory)}')
