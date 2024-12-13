import utility
import user_action

from rooms import rooms

game_state = {
    'destroyed_wall': False,
    'inventory': [],
    'current_room': "Mort'ton",
}

game_running = True
current_room = game_state['current_room']
previous_room = current_room
directions = ['north', 'south', 'east', 'west', 'enter', 'down']

utility.start_credits()
print(rooms[current_room]['description'])

while game_running:
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
    elif verb.lower() == 'clear':
        utility.clear()
    elif verb.lower() == 'go':
        user_action.handle_go(noun, rooms, game_state, game_state['current_room'])
    elif verb.lower() == 'inventory':
        utility.handle_inventory(game_state)
    elif verb.lower() == 'look':
        if noun == '' or noun == 'around':
            user_action.handle_look_around(game_state['current_room'], rooms)
        else:
            print('handle_look_obj')
    elif verb.lower() == 'use':
        user_action.handle_use(noun, game_state['current_room'], game_state)
    elif verb.lower() == 'help':
        utility.handle_help(game_state['inventory'])
    elif verb.lower() == 'map':
        print('handle_map')
    else:
        print("I don't understand what you want me to do.")
