game_state = {
    'has_pickaxe': False,
    'inventory': [],
    'current_room': 'Mort\'ton',
}

game_running = True
current_room = game_state['current_room']
previous_room = current_room
directions = ['north', 'south', 'east', 'west', 'enter', 'down']

rooms = {
    'Mort\'ton': {
        # Direction(s)
        'enter': 'Crypt of the Fallen',
        # Lore
        'description':
            'You stand at your CAMP, a modest setup of a TENT and a FIREPIT, nestled just beyond the eerie marshes that border the Barrows. The air hangs heavy with mist, carrying the faint stench of decay from the crypts ahead. Your supplies are sparse, having been nearly exhausted after your long journey from Lumbridge. A foreboding hill looms in the distance, its entrance marked by ancient stones and an unsettling stillness. The only way forward is to ENTER the barrows.',
        'object': {
            'around':
                'Your camp feels hastily put together, as if you intended to rest here only briefly. The FIREPIT has long gone cold, and the TENT sags from overuse. From here, the BARROWS rise like a dark monument to your goal, the entrance beckoning ominously.',
            'camp':
                'Your camp is a simple setup meant for resting between arduous travels. It’s clear you didn’t plan to stay long, given how sparse and disorganized it looks.',
            'tent':
                'The TENT is weathered and barely holding together, a cheap purchase from the Varrock General Store that you now regret. It’s a far cry from the sturdy tents you’d hoped for, though you barely have enough GP for anything better. Inside, there’s little more than a thin bedroll and an empty pack.',
            'firepit':
                'The FIREPIT is surrounded by scattered stones, its ashes long cold. A half-eaten tuna lies next to it—something you started nibbling on but couldn’t finish. The nerves of your upcoming adventure made it impossible to stomach much.'
        }
    },
    ####################################################
    'Crypt of the Fallen': {
        # Direction(s)
        'north': 'Ahrim\'s Tomb',
        'south': 'Verac\'s Tomb',
        'west': 'chamber_to_guthan_torag',
        'east': 'chamber_to_dharok',
        # Lore
        'description': '',
        'object': {
            'around':
                'The air here is thick and heavy, the weight of history and sorrow palpable. The walls of the crypt are adorned with intricately carved MURALS depicting the brothers in moments of their past lives. Life-sized STATUES stand in solemn vigil around the chamber, each one expertly crafted to capture the likeness of the brothers: AHRIM, DHAROK, GUTHAN, KARIL, TORAG, and VERAC. The BARROWS ENTRANCE looms behind you, a reminder of the journey yet to come.',
            'murals':
                'The murals depict the brothers by name as they were in life: Ahrim the tactician, Dharok the berserker, Guthan the healer, Karil the scout, Torag the craftsman, and Verac the zealot. Each panel tells a story of heroism and tragedy, a life lived in honor but ultimately marred by betrayal and death. The scenes are vivid, almost alive in their detail.',
            'statues':
                'The statues are magnificent in their craftsmanship, each capturing the unique essence of the brothers. Ahrim stands tall with an air of wisdom and sorrow; Dharok grips his axe with grim determination; Guthan exudes a sense of quiet strength; Karil appears agile and vigilant; Torag seems steadfast and resolute; Verac, the youngest, is youthful and brimming with zeal.',
            'barrows entrance':
                'The way back to the surface is dark and foreboding, the heavy stone doors reminding you of the world above. Yet the pull to uncover the secrets within keeps you from turning back.',
            'ahrim':
                'The eldest brother, Ahrim, was known for his intelligence and mastery of magic. In life, he was a tactician, using his wits to protect his family and homeland. The statue captures his thoughtful gaze, hinting at the burden of his wisdom.',
            'dharok':
                'Dharok, the second eldest, was a fearsome warrior whose strength was unmatched. His great axe, larger than most men, was a symbol of his unyielding power. The statue shows him poised to strike, his expression grim and resolute.',
            'guthan':
                'Guthan was a healer and protector, a man of quiet strength and compassion. His spear was both a weapon and a tool of mercy. The statue depicts him standing tall, his eyes reflecting a sense of duty and care.',
            'karil':
                'Karil, the fleet-footed, was an expert marksman and scout. In life, his keen eyes and unmatched speed made him a vital asset to the brothers. The statue portrays him in mid-motion, his bow at the ready, ever watchful.',
            'torag':
                'Torag, the craftsman, was as skilled with a hammer as he was on the battlefield. Known for his unshakable resolve, he forged weapons and armor to protect his family. The statue shows him holding his hammers, his stance unyielding.',
            'verac':
                'The youngest of the brothers, Verac, was full of zeal and determination. His flail was both a symbol of his faith and his fervor. The statue captures his youthful energy and the fiery passion that defined him.'
        },

    },
    ####################################################
    'chamber_to_guthan_torag': {
        # Direction(s)
        'north': 'Torag\'s Tomb',
        'west': 'Guthan\'s Tomb',
        'east': 'Crypt of the Fallen',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Guthan\'s Tomb': {
        # Direction(s)
        'east': 'chamber_to_guthan_torag',
        # Item
        'item': 'Guthan\'s Helm',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Torag\'s Tomb': {
        # Direction(s)
        'south': 'chamber_to_guthan_torag',
        # Item
        'item': 'Torag\'s Gauntlets',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Verac\'s Tomb': {
        # Direction(s)
        'north': 'Crypt of the Fallen',
        'west': 'chamber_to_karil',
        # Item
        'item': 'Verac\'s Flail',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'chamber_to_karil': {
        # Direction(s)
        'south': 'Karil\'s Tomb',
        'west': 'kv_dead_end',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'kv_dead_end': {
        # Direction(s)
        'east': 'chamber_to_karil',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Karil\'s Tomb': {
        # Direction(s)
        'north': 'chamber_to_karil',
        # Item
        'item': 'Karil\'s Dragonhide Boots',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'chamber_to_dharok': {
        # Direction(s)
        'south': 'dharok_dead_end',
        'east': 'Dharok\'s Tomb',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'dharok_dead_end': {
        # Direction(s)
        'north': 'chamber_to_dharok',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Dharok\'s Tomb': {
        # Direction(s)
        'south': 'The Forgotten Shrine',
        'west': 'chamber_to_dharok',
        # Item
        'item': 'Dharok\'s Platebody',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'The Forgotten Shrine': {
        # Direction(s)
        'north': 'Dharok\'s Tomb',
        # Item
        'item': 'steel pickaxe',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Ahrim\'s Tomb': {
        # Direction(s)
        'down': 'The Point of No Return',
        # Item
        'item': 'Ahrim\'s Ward',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'The Point of No Return': {
        # Direction(s)
        'north': 'The Blighted Sepulcher',
        'west': 'Hidden Chamber',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Hidden Chamber': {
        # Direction(s)
        'east': 'The Point of No Return',
        # Item
        'item': 'Amulet of the Damned',
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'The Blighted Sepulcher': {
        # Lore
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    }
    ####################################################
}


def print_directions():
    room = game_state['current_room']
    room_directions = list(rooms.get(room).keys())
    available_directions = []

    print(f"You're currently in: {game_state['current_room']}")

    for direction in directions:
        if direction in room_directions:
            available_directions.append(direction.capitalize())

    print('Your available directions are: {}'.format(', '.join(available_directions)))


print_directions()
while game_running:
    user_in = input("What is your move: ")
    words = user_in.lower().lower().split()

    # If the user pressed enter without any text, then it tells them to stop being bad.
    if not words:
        print('You did not give me a command. Please try again.')
        continue
    elif len(words) == 2:
        verb = words[0]
        noun = words[1]
    else:
        verb = words[0]
        noun = ''

    if verb == 'enter' and game_state['current_room'] == 'Mort\'ton':
        game_state['current_room'] = 'Crypt of the Fallen'
        print_directions()
    # This if block will be replaced with a "handle_go" function in the full game, but it checks
    # what room the player is currently in (game_state['current_room']) against the dictionary of all rooms,
    # and if that room both exists and has a direction that matches what the user input, it changes the room.
    elif verb == 'go' and noun in rooms[game_state['current_room']]:
        game_state['current_room'] = rooms[game_state['current_room']][noun]
        print_directions()
    elif verb == 'exit':
        break
    else:
        print("I can't do that. Try telling me to go somewhere.")
