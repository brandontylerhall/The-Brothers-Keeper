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
            'You stand at your CAMP, a modest setup of a TENT and a FIREPIT, nestled just beyond the eerie marshes '
            'that border the Barrows. The air hangs heavy with mist, carrying the faint stench of decay from the '
            'crypts ahead. Your supplies are sparse, having been nearly exhausted after your long journey from '
            'Lumbridge. A foreboding hill looms in the distance, its entrance marked by ancient stones and an '
            'unsettling stillness. The only way forward is to ENTER the barrows.',
        'object': {
            'around':
                'Your camp feels hastily put together, as if you intended to rest here only briefly. The FIREPIT has '
                'long gone cold, and the TENT sags from overuse. From here, the BARROWS rise like a dark monument to '
                'your goal, the entrance beckoning ominously.',
            'camp':
                'Your camp is a simple setup meant for resting between arduous travels. '
                'It\'s clear you didn\'t plan to stay long, given how sparse and disorganized it looks.',
            'tent':
                'The TENT is weathered and barely holding together, a cheap purchase from the Varrock General Store '
                'that you now regret. It\'s a far cry from the sturdy tents you\'d hoped for, though you barely have '
                'enough GP for anything better. Inside, there\'s little more than a thin bedroll and an empty pack.',
            'firepit':
                'The FIREPIT is surrounded by scattered stones, its ashes long cold. A half-eaten tuna lies next to '
                'it—something you started nibbling on but couldn\'t finish. The nerves of your upcoming adventure made '
                'it impossible to stomach much.'
        }
    },
    ####################################################
    'Crypt of the Fallen': {
        # Direction(s)
        'north': 'Ahrim\'s Tomb',
        'south': 'Verac\'s Tomb',
        'west': 'Western Antechamber',
        'east': 'Eastern Antechamber',
        # Lore
        'description':
            'You stand in the center of a somber crypt. The air is thick with decay and echoes of the past. Along the '
            'walls are MURALS and STATUES, each immortalizing one of the six brothers in their prime — warriors who '
            'fell to ambition and dark magic. The only way forward lies deeper into the labyrinth, but the weight of '
            'history seems to demand your attention first.',

        'object': {
            'around':
                'The air here is thick and heavy, the weight of history and sorrow palpable. The walls of the crypt '
                'are adorned with intricately carved MURALS depicting the brothers in moments of their past lives. '
                'Life-sized STATUES stand in solemn vigil around the chamber, each one expertly crafted to capture '
                'the likeness of the brothers. The barrows ENTRANCE looms behind you, '
                'a reminder of the journey yet to come.',
            'murals':
                'The murals depict the brothers by name as they were in life: AHRIM the tactician, DHAROK the '
                'berserker, GUTHAN the healer, KARIL the scout, TORAG the craftsman, and VERAC the zealot. Each panel '
                'tells a story of heroism and tragedy, a life lived in honor but ultimately marred by betrayal and '
                'death. The scenes are vivid, almost alive in their detail.',
            'statues':
                'The statues are magnificent in their craftsmanship, each capturing the unique essence of the '
                'brothers. AHRIM stands tall with an air of wisdom and sorrow; DHAROK grips his axe with grim '
                'determination; GUTHAN exudes a sense of quiet strength; KARIL appears agile and vigilant; TORAG '
                'seems steadfast and resolute; VERAC, the youngest, is youthful and brimming with zeal.',
            'entrance':
                'The way back to the surface is dark and foreboding, the heavy stone doors reminding you of the world '
                'above. Yet the pull to uncover the secrets within keeps you from turning back.',
            'ahrim':
                'The eldest brother, Ahrim, was known for his intelligence and mastery of magic. In life, he was a '
                'tactician, using his wits to protect his family and homeland. The statue captures his thoughtful '
                'gaze, hinting at the burden of his wisdom.',
            'dharok':
                'Dharok, the second eldest, was a fearsome warrior whose strength was unmatched. His great axe, '
                'larger than most men, was a symbol of his unyielding power. The statue shows him poised to strike, '
                'his expression grim and resolute.',
            'guthan':
                'Guthan was a healer and protector, a man of quiet strength and compassion. His spear was both a '
                'weapon and a tool of mercy. The statue depicts him standing tall, his eyes reflecting a sense of '
                'duty and care.',
            'karil':
                'Karil, the fleet-footed, was an expert marksman and scout. In life, his keen eyes and unmatched '
                'speed made him a vital asset to the brothers. The statue portrays him in mid-motion, his bow at the '
                'ready, ever watchful.',
            'torag':
                'Torag, the craftsman, was as skilled with a hammer as he was on the battlefield. Known for his '
                'unshakable resolve, he forged weapons and armor to protect his family. The statue shows him holding '
                'his hammers, his stance unyielding.',
            'verac':
                'The youngest of the brothers, Verac, was full of zeal and determination. His flail was both a symbol '
                'of his faith and his fervor. The statue captures his youthful energy and the fiery passion that '
                'defined him.'
        },
    },
    ####################################################
    'Western Antechamber': {
        # Direction(s)
        'north': 'Torag\'s Tomb',
        'west': 'Guthan\'s Tomb',
        'east': 'Crypt of the Fallen',
        # Lore
        'description':
            'You enter a dimly lit antechamber. The air is heavy with the scent of dust and decay. '
            'Cobwebs cling to the corners of the room, and the stone walls are cold and damp to the touch. '
            'An ornate ARCHWAY leads NORTH to Torag\'s Tomb, and another to the WEST, leading to Guthan\'s Tomb. '
            'To the EAST, the way leads back to the Crypt of the Fallen. A large, ornately carved '
            'CHEST sits against the wall, its surface covered in intricate designs, but its lid hangs open. '
            'A shattered remnant of a once-proud STATUE lies broken on the floor.',
        'object': {
            'around':
                'The antechamber is sparsely furnished, with only the open CHEST and the broken STATUE remnant. '
                'Sunlight peers weakly through GRATES high in the walls, casting long, eerie shadows across the room.',
            'chest':
                'The chest is made of dark wood, bound with iron bands. '
                'It appears to have been forced open long ago, its contents long gone. '
                'Splintered wood and broken hinges speak of a desperate struggle.',
            'grates':
                'The grates are set high in the walls, offering glimpses of the outside world. '
                'They are too small to climb through, but you can see the sky beyond.',
            'statue':
                'The statue lies in pieces scattered across the floor. '
                'It\'s impossible to tell who it once depicted, but the craftsmanship suggests it was once '
                'a masterpiece. You notice a strange SYMBOL etched into the base of the largest fragment.'
        },
    },
    ####################################################
    'Guthan\'s Tomb': {
        # Direction(s)
        'east': 'Western Antechamber',
        # Item
        'item': 'spear',
        # Lore
        'description':
            "You step through the ornate archway into Guthan's Tomb. The air is filled with the scent of herbs and "
            "incense. Before you lies a vast chamber dominated by Guthan's SARCOPHAGUS. The walls are lined with "
            "HERBS and medical TOOLS, a testament to Guthan's life as a healer. In the center of the room, "
            "a massive ALTAR dominates the space, and atop it rests Guthan's SPEAR. The only exit is back EAST.",
        'object': {
            'around':
                "Sunlight filters through an OPENING in the ceiling, illuminating the room with a soft, warm glow. "
                "GUTHAN'S SARCOPHAGUS is ornately carved with scenes of a valiant life.",
            'sarcophagus':
                "Guthan's sarcophagus is carved from white marble, its surface depicting scenes of him healing the "
                "sick and wielding his spear in battle. The spear is adorned with symbols of healing and protection.",
            'altar':
                "The altar is made of polished wood, its surface inlaid with silver symbols that seem to radiate a "
                "gentle warmth. Unlike the other altars, this one feels more like a place of healing than sacrifice.",
            "spear":
                "The spear rests atop the altar, its haft crafted from polished wood and its head forged from "
                "gleaming silver. Runes are etched along the blade, pulsing with a soft, white light.",
            'herbs':
                "Vials and pouches filled with dried herbs and powders line the walls, their labels long faded. You "
                "recognize some of the plants as having healing properties.",
            'tools':
                "Scalpels, forceps, and other medical instruments are neatly arranged on shelves along the walls. "
                "They are all made of silver and show little sign of age.",
            'opening':
                "The opening in the ceiling is small, but it allows a beam of sunlight to illuminate the room, "
                "creating a sense of peace and tranquility."
        },
    },
    ####################################################
    'Torag\'s Tomb': {
        # Direction(s)
        'south': 'Western Antechamber',
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
        'west': 'Southern Passage',
        # Item
        'item': 'Verac\'s Brassard',
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
    'Southern Passage': {
        # Direction(s)
        'south': 'Karil\'s Tomb',
        'west': 'Shadowed Alcove',
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
    'Shadowed Alcove': {
        # Direction(s)
        'east': 'Southern Passage',
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
        'north': 'Southern Passage',
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
    'Eastern Antechamber': {
        # Direction(s)
        'south': 'Forsaken Hollow',
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
    'Forsaken Hollow': {
        # Direction(s)
        'north': 'Eastern Antechamber',
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
        'west': 'Eastern Antechamber',
        # Item
        'item': 'Dharok\'s Helm',
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
