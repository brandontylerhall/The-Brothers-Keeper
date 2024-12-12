import os

from rooms import rooms

game_state = {
    'has_pickaxe': False,
    'destroyed_wall': False,
    'has_amulet': False,
    'inventory': [],
    'current_room': "Mort'ton",
}

game_running = True
current_room = game_state['current_room']
previous_room = current_room
directions = ['north', 'south', 'east', 'west', 'enter', 'down']


def print_directions():
    room = game_state['current_room']
    room_directions = list(rooms.get(room).keys())
    available_directions = []

    print(f"You're currently in: {game_state['current_room']}")

    for direction in directions:
        if direction in room_directions:
            available_directions.append(direction.capitalize())

    print('Your available directions are: {}'.format(', '.join(available_directions)))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print_directions()

while game_running:
    # this prevents the room descript from printing after every action
    if current_room != previous_room:
        clear()
        print(rooms[current_room]["description"])
        previous_room = current_room

    user_in = input('> ')
    # splits input on the first whitespace to separate
    # the verb and the remaining input
    words = user_in.lower().lower().split()

    if not words:
        print('You did not give me a command. Please try again.')
        continue
    elif len(words) == 2:
        verb = words[0]
        noun = words[1]
    else:
        verb = words[0]
        noun = ''

    if verb.lower() == 'exit':
        print("Exiting the game. Goodbye!")
        game_running = False
    elif verb.lower() == 'take':
        print('handle_take')
    elif verb.lower() == 'go':
        print('handle_go')
    elif verb.lower() == 'inventory':
        print('handle_inventory')
    elif verb.lower() == 'look':
        if noun == '':
            print('handle_look_around')
        else:
            print('handle_look_obj')
    elif verb.lower() == 'use':
        print('handle_use')
    elif verb.lower() == 'help':
        print('handle_help')
    elif verb.lower() == 'map':
        print('handle_map')
    else:
        print("I don't understand what you want me to do.")
