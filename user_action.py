import random
import time

from PIL import Image


def handle_take(noun, current_room, rooms, game_state):
    inventory = game_state["inventory"]

    if noun == "":
        print("You need to be more specific.")
    elif 'item' in rooms[current_room].keys() and rooms[current_room]["item"] == noun.lower():
        inventory.append(rooms[current_room]["item"])
        print(f'You take the {noun}.')
        del rooms[current_room]["item"]
        del rooms[current_room]['object'][noun]
    else:
        print(f'You look around and you don\'t see one of those.')


def handle_use(noun, current_room, game_state):
    inventory = game_state["inventory"]

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


def handle_look_obj(noun, current_room, rooms):
    if noun in rooms[current_room]["object"]:
        print(rooms[current_room]["object"][noun])
    else:
        print(f"I don't see a {noun} to look at.")


def handle_go(noun, rooms, game_state, current_room):
    if noun == '':
        print("You need to be more specific.")
    elif noun in rooms[current_room].keys():
        new_room = rooms[current_room][noun]

        # Check for pickaxe if entering Hidden Chamber
        if new_room == 'Hidden Chamber' and not game_state['destroyed_wall']:
            if 'pickaxe' not in game_state['inventory']:
                print("You need a tool to break through this wall!")
                return

        # Check for required items if entering The Blighted Sepulcher
        if new_room == 'The Blighted Sepulcher':
            required_items = ['helm', 'brassard', 'ward', 'gauntlets', 'spear', 'boots', 'amulet']
            missing_items = [item for item in required_items if item not in game_state['inventory']]
            if missing_items:
                if len(missing_items) > 1:
                    missing_item = random.choice(missing_items)
                    print(rooms[new_room]['object'][f'no_{missing_item}'])
                else:
                    missing_item = missing_items[0]
                    print(rooms[new_room]['object'][f'no_{missing_item}'])
                return
            else:
                print(rooms[new_room]['object']['battle'])
                print()
                print(rooms[new_room]['object']['win'])
                time.sleep(15)
                game_state['game_running'] = False
                return


        # Update current room in game_state
        game_state['current_room'] = new_room

        # Update conditional lore text
        if 'object' in rooms[new_room]:
            for obj_name, obj_data in rooms[new_room]['object'].items():
                if isinstance(obj_data, dict) and any(
                        key.startswith('before_') or key.startswith('after_') for key in obj_data.keys()):
                    # Determine the correct key based on game state or inventory
                    condition_key = None
                    if obj_name == 'around' and new_room == 'Shadowed Alcove':
                        condition_key = 'before_take_map' if 'map' not in game_state['inventory'] else 'after_take_map'
                    elif obj_name == 'around' and new_room == 'The Point of No Return':
                        condition_key = 'before_break_wall' if not game_state['destroyed_wall'] else 'after_break_wall'
                    elif obj_name == 'altar' and new_room in ['Guthan\'s Tomb', 'Torag\'s Tomb', 'Verac\'s Tomb',
                                                              'Dharok\'s Tomb', 'Karil\'s Tomb', 'Ahrim\'s Tomb']:
                        item_name = rooms[new_room].get('item')
                        condition_key = f'before_take_{item_name}' if item_name not in game_state[
                            'inventory'] else f'after_take_{item_name}'

                    # Print the appropriate description
                    if condition_key:
                        print(obj_data[condition_key])

        print(rooms[game_state['current_room']]['description'])

    else:
        print('I can\'t go that way.')


def handle_map():
    Image.open('map.png').show()
    print('Pulling out the map.')
