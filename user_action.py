from PIL import Image


def handle_take(noun, current_room, rooms, game_state):
    inventory = game_state["inventory"]

    if noun == "":
        print("You need to be more specific.")
    elif 'item' in rooms[current_room].keys() and rooms[current_room]["item"] == noun.lower():
        inventory.append(rooms[current_room]["item"])
        print(f'You take the {noun}.')
        del rooms[current_room]["item"]
    else:
        print(f'You look around and you don\'t see one of those.')


def handle_use(noun, current_room, game_state):
    inventory = game_state["inventory"]
    print(noun)
    print(current_room)

    if noun == "pickaxe" and current_room == 'The Point of No Return':
        if 'pickaxe' in inventory:
            print('You swing the pickaxe with all your might, and the wall crumbles before you!')
            game_state['destroyed_wall'] = True
        else:
            print("You don't have a pickaxe to use.")
    else:
        print('Nothing interesting happens.')


def handle_look_around(current_room, rooms):
    print(rooms[current_room]['object']["around"])


def handle_look_obj(noun, current_room, rooms, game_state):
    try:
        # Use the game_state dictionary to check if the items have been delivered
        if noun in rooms[current_room]["object"]:
            if noun == 'bed':
                # Check if all items have been delivered using the game_state dictionary
                if not game_state["items_delivered"]:
                    print('The bed looks mad comfy but it isn\'t time for sleep yet! '
                          'I still need to get dad his beer.')
                else:
                    print(rooms[current_room]["object"][noun])
            elif noun in ['cigar case', 'box']:
                if game_state.get('cigar_case_unlocked', False):
                    print(rooms[current_room]["object"][noun]['unlocked'])
                else:
                    print(rooms[current_room]["object"][noun]['locked'])
            else:
                print(rooms[current_room]["object"][noun])
    except KeyError:
        print(f"I don't see a {noun} to look at.")


def handle_go(noun, rooms, game_state, current_room):
    if noun == '':
        print("You need to be more specific.")
    elif noun in rooms[current_room].keys():
        game_state['current_room'] = rooms[current_room][noun]
        print(rooms[game_state['current_room']]['description'])
    else:
        print('I can\'t go that way.')


def handle_map():
    Image.open('map.png').show()
    print('Pulling out the map.')
