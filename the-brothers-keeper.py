rooms = {
    'mortton': {
        'enter': 'crypt_of_fallen'
    },
    ####################################################
    'crypt_of_fallen': {
        'north': 'ahrims_tomb',
        'south': 'veracs_tomb',
        'west': 'chamber_to_guthan_torag',
        'east': 'chamber_to_dharok',
    },
    ####################################################
    'chamber_to_guthan_torag': {
        'north': 'torags_tomb',
        'west': 'guthans_tomb',
    },
    ####################################################
    'guthans_tomb': {
        'east': 'chamber_to_guthan_torag',
        'item': 'guthans_helm'
    },
    ####################################################
    'torags_tomb': {
        'south': 'chamber_to_guthan_torag',
        'item': 'torag_gauntlets'
    },
    ####################################################
    'veracs_tomb': {
        'north': 'crypt_of_fallen',
        'west': 'chamber_to_karil',
        'item': 'veracs_brassard'
    },
    ####################################################
    'chamber_to_karil': {
        'south': 'karils_tomb',
        'west': 'kv_dead_end',
    },
    ####################################################
    'kv_dead_end': {
        'east': 'chamber_to_karil',
    },
    ####################################################
    'karils_tomb': {
        'north': 'chamber_to_karil',
        'item': 'karils_dhide_boots'
    },
    ####################################################
    'chamber_to_dharok': {
        'south': 'dharok_dead_end',
        'east': 'dharoks_chamber',
    },
    ####################################################
    'dharok_dead_end': {
        'north': 'the_forgotten_shrine',
    },
    ####################################################
    'dharoks_tomb': {
        'south': 'the_forgotten_shrine',
        'west': 'chamber_to_dharok',
        'item': 'dharoks_greataxe'
    },
    #######################################################
    'the_forgotten_shrine': {
        'north': 'dharoks_tomb',
        'item': 'steel_pickaxe'
    },
    #################################################
    'ahrims_tomb': {
        'down': 'the_point_of_no_return',
        'item': 'ahrims_ward'
    },
    ####################################################
    'the_point_of_no_return': {
        'north': 'the_blighted_sepulcher',
    },
    ####################################################
    'hidden_chamber': {
        'west': 'hidden_chamber',
        'item': 'amulet_of_the_damned'
    },
    ####################################################
    'the_blighted_sepulcher': {
        'direction': 'room',
    }
}
