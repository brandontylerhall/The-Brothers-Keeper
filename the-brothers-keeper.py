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
        'enter': 'Crypt of the Fallen',
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'Crypt of the Fallen': {
        'north': 'Ahrim\'s Tomb',
        'south': 'Verac\'s Tomb',
        'west': 'chamber_to_guthan_torag',
        'east': 'chamber_to_dharok',
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    ####################################################
    'chamber_to_guthan_torag': {
        'north': 'Torag\'s Tomb',
        'west': 'Guthan\'s Tomb',
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
        'east': 'chamber_to_guthan_torag',
        'item': 'Guthan\'s Helm',
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
        'south': 'chamber_to_guthan_torag',
        'item': 'Torag\'s Gauntlets',
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
        'north': 'Crypt of the Fallen',
        'west': 'chamber_to_karil',
        'item': 'Verac\'s Flail',
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
        'south': 'Karil\'s Tomb',
        'west': 'kv_dead_end',
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
        'east': 'chamber_to_karil',
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
        'north': 'chamber_to_karil',
        'item': 'Karil\'s Dragonhide Boots',
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
        'south': 'dharok_dead_end',
        'east': 'Dharok\'s Tomb',
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
        'north': 'chamber_to_dharok',
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
        'south': 'The Forgotten Shrine',
        'west': 'chamber_to_dharok',
        'item': 'Dharok\'s Platebody',
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    #######################################################
    'The Forgotten Shrine': {
        'north': 'Dharok\'s Tomb',
        'item': 'steel pickaxe',
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    },
    #################################################
    'Ahrim\'s Tomb': {
        'down': 'The Point of No Return',
        'item': 'Ahrim\'s Ward',
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
        'north': 'The Blighted Sepulcher',
        'west': 'Hidden Chamber',
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
        'east': 'The Point of No Return',
        'item': 'Amulet of the Damned',
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
        'description': '',
        'object': {
            'around': '',
            'obj1': '',
            'obj2': '',
            'obj3': '',
        },
    }
}
