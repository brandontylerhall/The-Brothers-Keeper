rooms = {
    "Mort'ton": {
        # Direction(s)
        'inside': 'Crypt of the Fallen',
        # Lore
        'description':
            'You stand at your CAMP, a modest setup of a TENT and a FIREPIT, nestled just beyond the eerie marshes \n'
            'that border the Barrows. The air hangs heavy with mist, carrying the faint stench of decay from the \n'
            'crypts ahead. Your supplies are sparse, having been nearly exhausted after your long journey from \n'
            'Lumbridge. A foreboding hill looms in the distance, its entrance marked by ancient stones and an \n'
            'unsettling stillness. The only way forward is to go INSIDE the barrows.',
        'object': {
            'around':
                'Your CAMP feels hastily put together, as if you intended to rest here only briefly. The FIREPIT has \n'
                'long gone cold, and the TENT sags from overuse. From here, the barrows rise like a dark monument to \n'
                'your goal, the entrance beckoning ominously.',
            'camp':
                "Your CAMP is a simple setup meant for resting between arduous travels. \n"
                "It's clear you didn't plan to stay long, given how sparse and disorganized it looks.",
            'tent':
                "The TENT is weathered and barely holding together, a cheap purchase from the Varrock General Store \n"
                "that you now regret. It's a far cry from the sturdy tents you'd hoped for, though you barely have \n"
                "enough GP for anything better. Inside, there's little more than a thin bedroll and an empty pack.",
            'firepit':
                "The FIREPIT is surrounded by scattered stones, its ashes long cold. A half-eaten tuna lies next to \n"
                "it—something you started nibbling on but couldn't finish. The nerves of your upcoming adventure made \n"
                "it impossible to stomach much."
        }
    },
    ####################################################
    'Crypt of the Fallen': {
        # Direction(s)
        'north': "Ahrim's Tomb",
        'south': "Verac's Tomb",
        'west': 'Western Antechamber',
        'east': 'Eastern Antechamber',
        # Lore
        'description':
            'You stand in the center of a somber crypt. The air is thick with decay and echoes of the past. Along the \n'
            'walls are MURALS and STATUES, each immortalizing one of the six brothers in their prime — warriors who \n'
            'fell to ambition and dark magic. The only way forward lies deeper into the labyrinth, but the weight of \n'
            'history seems to demand your attention first.',

        'object': {
            'around':
                'The air here is thick and heavy, the weight of history and sorrow palpable. The walls of the crypt \n'
                'are adorned with intricately carved MURALS depicting the brothers in moments of their past lives. \n'
                'Life-sized STATUES stand in solemn vigil around the chamber, each one expertly crafted to capture \n'
                'the likeness of the brothers. The barrows ENTRANCE looms behind you, \n'
                'a reminder of the journey yet to come.',
            'murals':
                'The murals depict the brothers by name as they were in life: AHRIM the tactician, DHAROK the \n'
                'berserker, GUTHAN the healer, KARIL the scout, TORAG the craftsman, and VERAC the zealot. Each panel \n'
                'tells a story of heroism and tragedy, a life lived in honor but ultimately marred by betrayal and \n'
                'death. The scenes are vivid, almost alive in their detail.',
            'statues':
                'The statues are magnificent in their craftsmanship, each capturing the unique essence of the \n'
                'brothers. AHRIM stands tall with an air of wisdom and sorrow; DHAROK grips his axe with grim \n'
                'determination; GUTHAN exudes a sense of quiet strength; KARIL appears agile and vigilant; TORAG \n'
                'seems steadfast and resolute; VERAC, the youngest, is youthful and brimming with zeal.',
            'entrance':
                'The way back to the surface is dark and foreboding, the heavy stone doors reminding you of the world \n'
                'above. Yet the pull to uncover the secrets within keeps you from turning back.',
            'ahrim':
                'The eldest brother, Ahrim, was known for his intelligence and mastery of magic. In life, he was a \n'
                'tactician, using his wits to protect his family and homeland. The statue captures his thoughtful \n'
                'gaze, hinting at the burden of his wisdom.',
            'dharok':
                'Dharok, the second eldest, was a fearsome warrior whose strength was unmatched. His great axe, \n'
                'larger than most men, was a symbol of his unyielding power. The statue shows him poised to strike, \n'
                'his expression grim and resolute.',
            'guthan':
                'Guthan was a healer and protector, a man of quiet strength and compassion. His spear was both a '
                'weapon and a tool of mercy. The statue depicts him standing tall, his eyes reflecting a sense of '
                'duty and care.',
            'karil':
                'Karil, the fleet-footed, was an expert marksman and scout. In life, his keen eyes and unmatched \n'
                'speed made him a vital asset to the brothers. The statue portrays him in mid-motion, his bow at the \n'
                'ready, ever watchful.',
            'torag':
                'Torag, the craftsman, was as skilled with a hammer as he was on the battlefield. Known for his \n'
                'unshakable resolve, he forged weapons and armor to protect his family. The statue shows him holding \n'
                'his hammers, his stance unyielding.',
            'verac':
                'The youngest of the brothers, Verac, was full of zeal and determination. His flail was both a symbol \n'
                'of his faith and his fervor. The statue captures his youthful energy and the fiery passion that \n'
                'defined him.'
        },
    },
    ####################################################
    'Western Antechamber': {
        # Direction(s)
        'north': "Torag's Tomb",
        'west': "Guthan's Tomb",
        'east': 'Crypt of the Fallen',
        # Lore
        'description':
            "You enter a dimly lit antechamber. The air is heavy with the scent of dust and decay. \n"
            "Cobwebs cling to the corners of the room, and the stone walls are cold and damp to the touch. \n"
            "An ornate ARCHWAY leads NORTH to Torag's Tomb, and another to the WEST, leading to Guthan's Tomb. \n"
            "To the EAST, the way leads back to the Crypt of the Fallen. A large, ornately carved \n"
            "CHEST sits against the wall, its surface covered in intricate designs, but its lid hangs open. \n"
            "A shattered remnant of a once-proud STATUE lies broken on the floor.",
        'object': {
            'around':
                'The antechamber is sparsely furnished, with only the open CHEST and the broken STATUE remnant. \n'
                'Sunlight peers weakly through GRATES high in the walls, casting long, eerie shadows across the room.',
            'chest':
                'The chest is made of dark wood, bound with iron bands. \n'
                'It appears to have been forced open long ago, its contents long gone. \n'
                'Splintered wood and broken hinges speak of a desperate struggle.',
            'grates':
                'The grates are set high in the walls, offering glimpses of the outside world. \n'
                'They are too small to climb through, but you can see the sky beyond.',
            'statue':
                "The statue lies in pieces scattered across the floor. "
                "It's impossible to tell who it once depicted, but the craftsmanship suggests it was once \n"
                "a masterpiece. You notice a strange SYMBOL etched into the base of the largest fragment."
        },
    },
    ####################################################
    "Guthan's Tomb": {
        # Direction(s)
        'east': 'Western Antechamber',
        # Item
        'item': 'spear',
        # Lore
        'description':
            "You step through the ornate archway into Guthan's Tomb. The air is filled with the scent of herbs and \n"
            "incense. Before you lies a vast chamber dominated by Guthan's SARCOPHAGUS. The walls are lined with \n"
            "HERBS and medical TOOLS, a testament to Guthan's life as a healer. In the center of the room, \n"
            "a massive ALTAR dominates the space, and atop it rests Guthan's SPEAR. The only exit is back EAST.",
        'object': {
            'around': {
                'before_take_spear':
                    "Sunlight filters through an OPENING in the ceiling, illuminating the room with a soft, \n"
                    "warm glow. GUTHAN'S SARCOPHAGUS is ornately carved with scenes of a valiant life.",
                'after_take_spear':
                    "Sunlight filters through an OPENING in the ceiling, illuminating the room with a soft, \n"
                    "warm glow. GUTHAN'S SARCOPHAGUS is ornately carved with scenes of a valiant life. The altar \n"
                    "now stands bare, the spear's ethereal glow replaced by an unsettling emptiness."
            },
            'sarcophagus':
                "Guthan's sarcophagus is carved from white marble, its surface depicting scenes of him healing the \n"
                "sick and wielding his spear in battle. The spear is adorned with symbols of healing and protection.",
            'altar': {
                'before_take_spear':
                    "The altar is made of polished wood, its surface inlaid with silver symbols that seem to radiate \n"
                    "a gentle warmth. Unlike the other altars, this one feels more like a place of healing than \n"
                    "sacrifice.",
                'after_take_spear':
                    "The altar is made of polished wood, its surface inlaid with silver symbols that now seem \n"
                    "strangely cold. The absence of the spear leaves a palpable void."
            },
            "spear":
                "The spear rests atop the altar, its haft crafted from polished wood and its head forged from \n"
                "gleaming silver. Runes are etched along the blade, pulsing with a soft, white light.",
            'herbs':
                "Vials and pouches filled with dried herbs and powders line the walls, their labels long faded. You \n"
                "recognize some of the plants as having healing properties.",
            'tools':
                "Scalpels, forceps, and other medical instruments are neatly arranged on shelves along the walls. \n"
                "They are all made of silver and show little sign of age.",
            'opening':
                "The opening in the ceiling is small, but it allows a beam of sunlight to illuminate the room, \n"
                "creating a sense of peace and tranquility."
        },
    },
    ####################################################
    "Torag's Tomb": {
        # Direction(s)
        'south': 'Western Antechamber',
        # Item
        'item': 'gauntlets',
        # Lore
        'description':
            "You pass through the ornate archway into Torag's Tomb. The air is thick with the smell of iron and stone \n"
            "dust. Before you lies a large chamber dominated by Torag's SARCOPHAGUS. The walls are lined with \n"
            "FURNACES and ANVILS, tools of the master craftsman. In the center of the room, a massive stone ALTAR \n"
            "stands tall, and upon it rests Torag's GAUNTLETS, radiating an aura of immense strength. The only exit \n"
            "is back SOUTH.",
        'object': {
            'around': {
                'before_take_gauntlets':
                    "The room is dimly lit by a few flickering torches, casting long shadows on the walls. Torag's \n"
                    "SARCOPHAGUS is ornately carved with scenes of creation and battle.",
                'after_take_gauntlets':
                    "The room is dimly lit by a few flickering torches, casting long shadows on the walls. Torag's \n"
                    "SARCOPHAGUS is ornately carved with scenes of creation and battle. The altar now stands bare, \n"
                    "the absence of the gauntlets leaving a noticeable void."
            },
            'sarcophagus':
                "Torag's sarcophagus is carved from granite, its surface depicting scenes of him forging weapons and \n"
                "armor, and wielding his hammers in battle. He is shown dual-wielding his hammers, their intricate \n"
                "designs and flawless craftsmanship a testament to his skill.",
            'altar': {
                'before_take_gauntlets':
                    "The altar is made of rough-hewn stone, its surface scarred with the marks of countless hammer \n"
                    "blows. It feels sturdy and unyielding, a fitting tribute to Torag's unwavering resolve.",
                'after_take_gauntlets':
                    "The altar is made of rough-hewn stone, its surface scarred with the marks of countless hammer \n"
                    "blows. Without the gauntlets, it seems colder and less imposing."
            },
            "gauntlets":
                "The gauntlets rest atop the altar, crafted from thick plates of steel. They are etched with runes of \n"
                "power, radiating an aura of immense strength.",
            'furnaces':
                "The furnaces are cold and empty now, but you can still see the remnants of coal and ash within. They \n"
                "stand as a testament to Torag's tireless work ethic.",
            'anvils':
                "The anvils are worn smooth from countless hours of hammering. Each one bears the mark of Torag's \n"
                "craftsmanship, a symbol of his dedication to his craft.",
            'torches':
                "The torches flicker weakly, casting an eerie glow on the surrounding walls. They seem to struggle \n"
                "against the oppressive atmosphere of the tomb."
        },
    },
    ####################################################
    "Verac's Tomb": {
        # Direction(s)
        'north': 'Crypt of the Fallen',
        'west': 'Southern Passage',
        # Item
        'item': 'brassard',
        # Lore
        'description':
            "You enter Verac's Tomb, and a wave of tranquility washes over you. The air is still and \n"
            "quiet, imbued with a sense of peace. Before you stands Verac's SARCOPHAGUS, its serene \n"
            "beauty captivating. The walls are adorned with TAPESTRIES and PRAYER RUGS, reflecting \n"
            "Verac's devout nature. In the center of the room, a simple wooden ALTAR holds VERAC'S \n"
            "BRASSARD, emanating a soft, warm light. NORTH lies the Crypt of the Fallen, and WEST is a \n"
            "passage leading further into the tomb.",
        'object': {
            'around': {
                'before_take_brassard':
                    "The room is bathed in a soft, warm glow emanating from RUNES etched into the walls. VERAC'S \n"
                    "SARCOPHAGUS is intricately carved with scenes of peaceful worship and righteous fury.",
                'after_take_brassard':
                    "The room is bathed in a soft, warm glow emanating from RUNES etched into the walls. VERAC'S \n"
                    "SARCOPHAGUS is intricately carved with scenes of peaceful worship and righteous fury. The altar \n"
                    "now stands bare, the brassard's warm light replaced by an unsettling stillness."
            },
            'sarcophagus':
                "Verac's sarcophagus is made of polished obsidian, its surface depicting scenes of him leading \n"
                "prayers and wielding his flail in battle against injustice. The flail is adorned with symbols of \n"
                "faith and purity, including the unmistakable mark of Saradomin.",
            'altar': {
                'before_take_brassard':
                    "The altar is crafted from plain oak, its surface bare except for a single inscription: 'Faith is \n"
                    "my shield, truth is my weapon.' It emanates a sense of serenity and unwavering belief.",
                'after_take_brassard':
                    "The altar is crafted from plain oak, its surface bare except for a single inscription: 'Faith is \n"
                    "my shield, truth is my weapon.'  Without the brassard, the inscription seems to mock your \n"
                    "intrusion."
            },
            "brassard":
                "The brassard rests atop the altar, crafted from gleaming silver. It is etched with holy \n"
                "symbols, radiating a soft, warm light that fills the tomb with a sense of peace.",
            'tapestries':
                "The tapestries depict scenes of religious ceremonies and acts of charity, showcasing \n"
                "Verac's compassion and devotion to his faith.",
            'rugs':
                "The prayer rugs are woven with intricate patterns and symbols, their colors still vibrant despite \n"
                "their age. They speak of countless hours spent in meditation and prayer.",
            'runes':
                "The runes etched into the walls glow with a warm, golden light, illuminating the tomb with a \n"
                "sense of peace and tranquility. They seem to hum with a gentle energy, filling the air with a \n"
                "feeling of much needed calmness."
        },
    },
    ####################################################
    'Southern Passage': {
        # Direction(s)
        'south': "Karil's Tomb",
        'west': 'Shadowed Alcove',
        'east': "Verac's Tomb",
        # Lore
        'description':
            "Leaving Verac's Tomb, you enter a narrow passage. The air is heavy with the stench of decay, \n"
            "and the silence is broken only by the skittering of RATS. Ornate archways lie to the EAST and SOUTH, \n"
            "while a path leads WEST.",
        'object': {
            'around':
                "The passage is lined with cracked and crumbling STONE. PUDDLES of stagnant water gather in the \n"
                "uneven floor, reflecting the dim light.",
            'rats':
                "The rats are large and fearless, their eyes glowing ominously in the dim light. They scurry amongst \n"
                "the puddles, seemingly undisturbed by your presence.",
            'stone':
                "The stone lining the passage is old and weathered, with cracks running through it like veins. It \n"
                "feels unstable, as if it could collapse at any moment.",
            'puddles':
                "The puddles are murky and foul-smelling, filled with decaying debris. You can see the reflection of \n"
                "the flickering torches distorted in their surface."
        },
    },
    ####################################################
    'Shadowed Alcove': {
        # Direction(s)
        'east': 'Southern Passage',
        # Item
        'item': 'map',
        # Lore
        'description':
            "You step into a small, shadowed alcove. The air is still and heavy, with a faint metallic scent \n"
            "lingering in the air. A SKELETON lies slumped against the wall, clutching a MAP in its bony fingers. \n"
            "The only exit is back EAST.",
        'object': {
            'around': {
                'before_take_map':
                    "The alcove is shrouded in shadows. An overturned TORCH lies on the floor, its flame long \n"
                    "extinguished. A thick layer of DUST coats every surface.",
                'after_take_map':
                    "The alcove is shrouded in shadows. An overturned TORCH lies on the floor, its flame long \n"
                    "extinguished. A thick layer of DUST coats every surface. The skeleton's hand lies empty, \n"
                    "its grip finally loosened."
            },
            'skeleton': {
                'before_take_map':
                    "The skeleton is clad in the tattered remnants of leather armor, its skeletal fingers still \n"
                    "gripping the piece of paper.",
                'after_take_map':
                    "The skeleton is clad in the tattered remnants of leather armor, its skeletal hand now empty."
            },
            # TODO: after the player looks at the paper for the first time, this will change to 'map'
            'paper':
                "The paper is worn and brittle, but you can make out faint lines and markings. Upon closer \n"
                "inspection, you realize it's an incomplete MAP of the Barrows.",
            'map':
                "The map is worn and incomplete, with several sections left blank. It appears to be the work of a \n"
                "previous adventurer who never finished charting the Barrows. You recognize some of the landmarks, \n"
                "but others are unfamiliar.",
            'dust':
                "A thick layer of dust covers every surface in the alcove, disturbed only by the skeleton's presence. \n"
                "It speaks of years of undisturbed solitude.",
            'torch':
                "The torch is old and rusted, its handle broken. Perhaps the skeleton's last desperate attempt to \n"
                "light the alcove?"
        },
    },
    ####################################################
    "Karil's Tomb": {
        # Direction(s)
        'north': 'Southern Passage',
        # Item
        'item': 'boots',
        # Lore
        'description':
            "You step through the archway into Karil's Tomb. The air is strangely still, with an almost unnatural \n"
            "silence hanging in the air. Before you lies a vast chamber dominated by Karil's SARCOPHAGUS. The walls \n"
            "are lined with TARGETS and BOLTS, remnants of Karil's days as a master archer. In the center of the \n"
            "room, a sleek obsidian ALTAR holds Karil's BOOTS, which seem to shimmer with a faint, ethereal glow. The \n"
            "only exit is back NORTH.",
        'object': {
            'around': {
                'before_take_boots':
                    "The room is dimly lit by a single shaft of light emanating from a CRYSTAL embedded in the \n"
                    "ceiling. KARIL'S SARCOPHAGUS is intricately carved with scenes of the hunt and marksmanship.",
                'after_take_boots':
                    "The room is dimly lit by a single shaft of light emanating from a CRYSTAL embedded in the \n"
                    "ceiling. KARIL'S SARCOPHAGUS is intricately carved with scenes of the hunt and marksmanship. \n"
                    "The altar now stands bare, the boots' ethereal glow replaced by an unsettling stillness."
            },
            'sarcophagus':
                "Karil's sarcophagus is made of polished onyx, its surface depicting scenes of him stalking prey \n"
                "through the forest and loosing bolts with deadly accuracy. He is shown wielding his signature \n"
                "crossbow, adorned with dragonhide and runes of swiftness.",
            'altar': {
                'before_take_boots':
                    "The altar is crafted from smooth obsidian, its surface cool to the touch. It seems to absorb the \n"
                    "light, creating an atmosphere of stealth and shadows.",
                'after_take_boots':
                    "The altar is crafted from smooth obsidian, its surface cool to the touch. Without the boots, \n"
                    "it seems to exude a sense of loss and vulnerability."
            },
            'boots':
                "The boots rest atop the altar, crafted from supple dragonhide and imbued with a magical lightness. \n"
                "They seem to whisper promises of speed and agility.",
            'targets':
                "The targets are riddled with holes, evidence of Karil's exceptional marksmanship. Some bolts still \n"
                "protrude from the targets, their shafts crafted from dark metal.",
            'bolts':
                "The bolts are stacked neatly in piles, their tips gleaming menacingly in the dim light. You can \n"
                "almost hear the whirring sound they made as they flew through the air.",
            'crystal':
                "The crystal pulsates with a soft, inner light, casting an eerie glow upon the tomb. It seems to hum \n"
                "with a subtle energy, as if holding some ancient power."
        },
    },
    ####################################################
    'Eastern Antechamber': {
        # Direction(s)
        'south': 'Forsaken Hollow',
        'east': "Dharok's Tomb",
        # Lore
        'description':
            "You enter the Eastern Antechamber, a spacious hall with an air of faded grandeur. The walls are lined \n"
            "with empty weapon RACKS and crumbling display cases, hinting at a time when this room held treasures and \n"
            "trophies. ARCHWAYS lead EAST and WEST, while a dark passage descends SOUTH. A large, cracked MOSAIC \n"
            "dominates the far wall, depicting a battle scene.",
        'object': {
            'around':
                "The room is filled with an eerie silence, broken only by the occasional drip of water from the \n"
                "ceiling. Dust covers every surface, and cobwebs cling to the corners. The MOSAIC is the only \n"
                "source of color in the otherwise drab chamber.",
            'mosaic':
                "The mosaic depicts an epic battle with the six brothers fighting side-by-side. Despite the damage, \n"
                "you can still make out the details: Ahrim wielding his staff, Dharok with his axe, Guthan with his \n"
                "spear, Karil with his crossbow, Torag with his hammers, and Verac with his flail. They stand united \n"
                "against a horde of shadowy figures.",
            'racks':
                "The weapon racks are empty, their metal frames rusted and twisted. You can almost imagine the \n"
                "gleaming swords and axes that once hung here.",
            'cases':
                "The display cases are shattered, their glass shards scattered across the floor. It's impossible to \n"
                "tell what treasures they once held, but the remnants of velvet linings hint at valuable artifacts."
        },
    },
    ####################################################
    'Forsaken Hollow': {
        # Direction(s)
        'north': 'Eastern Antechamber',
        # Lore
        'description':
            "You descend into the Forsaken Hollow, a damp and claustrophobic chamber. The air is thick with the smell \n"
            "of mildew and decay, and the silence is oppressive. The only exit is back NORTH.",
        'object': {
            'around':
                "The walls are lined with cracked and crumbling STONE, and PUDDLES of stagnant water gather in the \n"
                "uneven floor. A sense of dread hangs heavy in the air.",
            'stone':
                "The stone is cold and damp to the touch, covered in moss and lichen. It seems to absorb what little \n"
                "light there is, making the hollow feel even more oppressive.",
            'puddles':
                "The puddles are murky and foul-smelling, filled with decaying debris. You can see the reflection of \n"
                "your own fear in their dark depths.",
            'ceiling':
                "The ceiling is low and uneven, with jagged rocks jutting down at odd angles. It feels as though the \n"
                "hollow could collapse at any moment, burying you alive."
        },
    },
    ####################################################
    "Dharok's Tomb": {
        # Direction(s)
        'south': 'The Forgotten Shrine',
        'west': 'Eastern Antechamber',
        # Item
        'item': 'helm',
        # Lore
        'description':
            "You enter Dharok's Tomb, a cavernous chamber filled with the echoes of past battles. The air is thick \n"
            "with the scent of blood and iron. Before you stands his SARCOPHAGUS, its imposing presence \n"
            "dominating the room. The walls are lined with weapon RACKS and dented ARMOR, testaments to Dharok's \n"
            "ferocity. In the center of the room, a massive stone ALTAR holds Dharok's HELM, radiating an aura of \n"
            "power. WEST lies the Eastern Antechamber, and SOUTH a passage leads deeper into the tomb.",
        'object': {
            'around': {
                'before_take_helm':
                    "The room is dimly lit by flickering TORCHES, casting long shadows that dance and writhe on the \n"
                    "walls. DHAROK'S SARCOPHAGUS is intricately carved with scenes of brutal combat.",
                'after_take_helm':
                    "The room is dimly lit by flickering TORCHES, casting long shadows that dance and writhe on the \n"
                    "walls. DHAROK'S SARCOPHAGUS is intricately carved with scenes of brutal combat. The altar now \n"
                    "stands bare, the helm's aura of power replaced by an eerie silence."
            },
            'sarcophagus':
                "Dharok's sarcophagus is made of black marble, its surface depicting scenes of him cleaving through \n"
                "enemies with his mighty axe. He is shown wielding his axe, its blade stained with the blood of his \n"
                "foes, and his eyes burning with an insatiable rage.",
            'altar': {
                'before_take_helm':
                    "The altar is crafted from a single block of granite, its surface scarred with countless battle \n"
                    "wounds. It stands as a symbol of Dharok's unwavering strength and resilience.",
                'after_take_helm':
                    "The altar is crafted from a single block of granite, its surface scarred with countless battle \n"
                    "wounds. Without the helm, it seems less imposing, as if a part of Dharok's spirit has departed."
            },
            'helm':
                "The helm rests atop the altar, its brutal design reflecting Dharok's bloodthirsty nature. A single \n"
                "spike juts from the crown, and the faceplate is etched with a fearsome grimace.",
            'racks':
                "The weapon racks are filled with rusted and broken weapons, remnants of Dharok's countless \n"
                "victories. Swords, axes, and maces are all represented, each bearing the marks of brutal combat.",
            'armor':
                "The armor is dented and scarred, its once-gleaming surface now dull and lifeless. It speaks of the \n"
                "ferocity of the battles Dharok fought, and the hardiness that allowed him to emerge victorious.",
            'torches':
                "The torches flicker erratically, their flames casting an eerie glow on the surrounding walls. They \n"
                "seem to struggle against the oppressive atmosphere of the tomb, as if even the light fears Dharok's \n"
                "presence."
        },
    },
    ####################################################
    'The Forgotten Shrine': {
        # Direction(s)
        'north': "Dharok's Tomb",
        # Item
        'item': 'pickaxe',
        # Lore
        'description':
            "You enter the Forgotten Shrine, a small chamber filled with an atmosphere of reverence and decay. The \n"
            "walls are lined with ancient SCROLLS and crumbling TEXTS, their wisdom lost to time. In the center of \n"
            "the room, a weathered ALTAR holds a simple PICKAXE, its handle worn smooth with use. The only exit is \n"
            "NORTH, back to Dharok's Tomb.",
        'object': {
            'around': {
                'before_take_pickaxe':
                    "Dust covers every surface, and cobwebs cling to the corners. An eerie silence hangs in the air, \n"
                    "broken only by the occasional creak of the aging structure. A sense of peace and sacrifice "
                    "pervades the air.",
                'after_take_pickaxe':
                    "Dust covers every surface, and cobwebs cling to the corners. An eerie silence hangs in the air, \n"
                    "broken only by the occasional creak of the aging structure. The altar now stands bare, \n"
                    "the absence of the pickaxe leaving a noticeable void."
            },
            'altar': {
                'before_take_pickaxe':
                    "The altar is made of cracked and weathered stone, its surface etched with faded inscriptions \n"
                    "that seem to speak of offerings and sacrifice. It appears to have once been a place of worship, \n"
                    "but now it's just a forgotten relic.",
                'after_take_pickaxe':
                    "The altar is made of cracked and weathered stone, its surface etched with faded inscriptions \n"
                    "that seem to speak of offerings and sacrifice. With the pickaxe gone, the altar feels strangely \n"
                    "incomplete, as if its purpose has yet to be fulfilled."
            },
            'pickaxe':
                "The pickaxe is old and sturdy, its head made of iron and its handle crafted from oak. It shows \n"
                "signs of heavy use, but it's still in good condition. It seems to have been placed carefully on the \n"
                "altar, as if it were an offering.",
            'scrolls':
                "The scrolls are brittle and faded, their writing indecipherable. They seem to contain ancient \n"
                "knowledge and rituals, perhaps related to the offerings made at the shrine.",
            'texts':
                "The texts are crumbling and incomplete, their pages scattered across the floor. You can make out \n"
                "fragments of prayers and incantations, possibly invoking the power of the shrine."
        },
    },
    ####################################################
    "Ahrim's Tomb": {
        # Direction(s)
        'down': 'The Point of No Return',
        'south': 'Crypt of the Fallen',
        # Item
        'item': 'ward',
        # Lore
        'description':
            "You enter Ahrim's Tomb, a chilling chamber filled with an oppressive silence. The air crackles with \n"
            "unseen energy, and the faint scent of ozone hangs heavy in the air. Before you stands AHRIM'S \n"
            "SARCOPHAGUS, its lid cast aside, revealing a gaping darkness within. The walls are lined with dusty \n"
            "TOMES and ancient SCROLLS, remnants of Ahrim's vast magical knowledge. In the center of the room, \n"
            "a dark obsidian ALTAR holds AHRIM'S WARD, pulsating with a soft, ethereal glow. A chilling DRAFT rises \n"
            "from the depths of the open sarcophagus, beckoning you DOWN.",
        'object': {
            'around': {
                'before_take_ward':
                    "The room is shrouded in an unnatural darkness, the shadows seeming to writhe and twist as if \n"
                    "alive. The DRAFT emanating from the sarcophagus whispers of untold depths and hidden dangers.",
                'after_take_ward':
                    "The room is shrouded in an unnatural darkness, the shadows seeming to writhe and twist as if \n"
                    "alive. The DRAFT emanating from the sarcophagus whispers of untold depths and hidden dangers. \n"
                    "The altar now stands bare, the ward's ethereal glow replaced by an ominous void."
            },
            'sarcophagus':
                "Ahrim's sarcophagus lies open, its interior shrouded in impenetrable darkness. A rickety LADDER \n"
                "descends into the abyss, its rungs worn and treacherous. The chilling DRAFT seems to emanate from \n"
                "the depths, beckoning you towards the unknown.",
            'altar': {
                'before_take_ward':
                    "The altar is crafted from a single block of obsidian, its surface cold and smooth to the touch. \n"
                    "It seems to hum with a subtle energy, as if channeling the power of the tomb itself.",
                'after_take_ward':
                    "The altar is crafted from a single block of obsidian, its surface cold and smooth to the touch. \n"
                    "Without the ward, it seems to radiate a chilling aura, as if Ahrim's spirit lingers nearby."
            },
            'ward':
                "The ward rests atop the altar, crafted from polished silver and etched with runes of protection. It \n"
                "pulsates with a soft, ethereal glow, radiating an aura of arcane power.",
            'tomes':
                "The tomes are bound in leather and filled with faded script and intricate diagrams. They seem to \n"
                "contain powerful spells and forbidden knowledge, but their secrets are guarded by Ahrim's lingering \n"
                "magic.",
            'scrolls':
                "The scrolls are brittle and fragile, their edges crumbling with age. They are covered in cryptic \n"
                "symbols and arcane formulas, hinting at the depth of Ahrim's magical mastery.",
            'draft':
                "The chilling DRAFT rising from the sarcophagus seems to whisper promises of adventure and danger. \n"
                "It tugs at your curiosity, urging you to explore the depths below.",
            'note': "The note is barely intact, but you can make out a desperate plea: "
                    "\n'He stands vigilant, a final guardian. Without the relic, your fate is sealed.'"
        },
    },
    ####################################################
    'The Point of No Return': {
        # Direction(s)
        'north': 'The Blighted Sepulcher',
        'west': 'Hidden Chamber',
        # Lore
        'description':
            "You find yourself in a damp and narrow passage. The air is thick with the smell of mildew and decay, \n"
            "and the silence is broken only by the echo of your own heartbeat.  A crumbling STONE WALL blocks the \n"
            "path to the WEST. To the NORTH, a path leads deeper into the darkness, but an oppressive aura hangs over \n"
            "it, promising danger.",
        'object': {
            'around': {
                'before_break_wall':
                    "The passage is lined with ancient BRICKS, their surface worn smooth by the passage of countless \n"
                    "feet. The air is heavy with a sense of foreboding.",
                'after_break_wall':
                    "The passage is lined with ancient BRICKS, their surface worn smooth by the passage of countless \n"
                    "feet. A gaping hole in the wall leads NORTH, revealing a chamber bathed in an eerie glow."
            },
            'wall':
                {
                    'wall_not_broken':
                        "The wall is made of crumbling stone, held together by crumbling mortar. It \n"
                        "looks unstable and precarious, as if it could collapse at any moment. \n"
                        "Through the gaps in the stone, you can make out a faint glow on the ground in \n"
                        "the distance. You might be able to break through it with the right tools.",
                    'wall_broken':
                        'A gaping hole now mars the wall, revealing the chamber beyond. The faint glow \n'
                        'emanates from within, beckoning you WEST.'
                },
            'bricks':
                "The bricks lining the passage are cold and damp, etched with strange symbols and markings. Some are \n"
                "loose, and you can hear the scuttling of rats behind them.",
            'ceiling':
                "The ceiling is low and oppressive, with cracks running through it like veins. Water drips from the \n"
                "cracks, forming puddles on the floor."
        },
    },
    ####################################################
    'Hidden Chamber': {
        # Direction(s)
        'east': 'The Point of No Return',
        # Item
        'item': 'amulet',
        # Lore
        'description':
            "You emerge into a hidden chamber, the air thick with the scent of ancient magic. A soft, ethereal glow \n"
            "emanates from the AMULET of the Damned, resting atop a stone PEDESTAL in the center of the room. The \n"
            "walls are adorned with intricate RUNES that pulse with power.",
        'object': {
            'around': {
                'amulet_not_taken':
                    "The chamber is surprisingly spacious, with a high, vaulted ceiling. An eerie \n"
                    "silence hangs in the air, broken only by the soft hum of magical energy.",
                'amulet_taken':
                    "The chamber feels strangely empty now, the silence even more profound with the \n"
                    "amulet gone."
            },
            'amulet':
                "The amulet rests atop the pedestal, its surface etched with intricate symbols that seem to shift and \n"
                "writhe before your eyes. It pulsates with a soft, ethereal glow, radiating an aura of immense power.",
            'pedestal':
                "The pedestal is made of smooth, polished stone, its surface cool to the touch. It seems to hum with \n"
                "a subtle energy, as if channeling the power of the amulet.",
            'runes':
                "The runes etched into the walls glow with an otherworldly light, their patterns shifting and \n"
                "changing as you watch. They seem to hum with a deep, resonant power, filling the chamber with an \n"
                "aura of ancient magic."
        },
    },
    ####################################################
    'The Blighted Sepulcher': {
        'description':
            "You stumble into the Blighted Sepulcher, a vast chamber pulsating with dark energy. The air is heavy \n"
            "with the stench of decay and corrupted Zarosian magic. AHRIM, his eyes glowing with an eerie purple \n"
            "light, stands before you, a puppet of the ancient, malevolent forces that now control him. He raises \n"
            "his staff, and the shadows around him begin to writhe and take shape.",
        'object': {
            'no_helm':
                "AHRIM's gaze falls upon your unprotected head, and a sneer curls his lip. 'Foolish mortal,'\n"
                "he whispers, 'to face me without adequate protection.'  He raises his staff, and a bolt of \n"
                "dark energy strikes you down.",
            'no_brassard':
                "AHRIM's eyes narrow as he notices your exposed arms. 'Such vulnerability...' he mutters, \n"
                "'an invitation to pain.'  He flicks his wrist, and shadowy tendrils wrap around your limbs, \n"
                "crushing them with unimaginable force.",
            'no_ward':
                "AHRIM's staff glows with an eerie light as he senses your lack of magical defenses. 'Your spirit \n"
                "is weak,' he intones, 'a mere wisp in the face of my power.'  He unleashes a torrent of arcane \n"
                "energy, tearing your soul from your body.",
            'no_gauntlets':
                "AHRIM's gaze falls upon your bare hands, and a cruel smile spreads across his face. 'Unarmed and \n"
                "unprepared,' he mocks, 'you are no match for me.'  He clenches his fist, and your weapons \n"
                "crumble into dust.",
            'no_spear':
                "AHRIM's eyes gleam with amusement as he observes your lack of a proper weapon. 'A warrior \n"
                "without a spear?' he scoffs. 'You are but a child playing at war.'  He summons a whirlwind of \n"
                "shadows, tearing you apart limb from limb.",
            'no_boots':
                "AHRIM's eyes flicker with disdain as he notices your exposed feet. 'So slow and clumsy,'\n"
                "he chides, 'you cannot hope to escape my wrath.'  He stamps his foot, and the ground beneath \n"
                "you erupts, swallowing you whole.",
            'no_amulet':
                "AHRIM raises his staff, and the shadows surge towards you, their forms twisting into monstrous \n"
                "shapes with gaping maws and razor-sharp claws. You raise your weapons in a desperate attempt to \n"
                "defend yourself, but the shadows overwhelm you, tearing at your flesh and consuming your soul. \n"
                "Your vision fades to black as you hear Ahrim's chilling laughter echo through the chamber.",
            'has_all':
                "AHRIM's eyes widen in surprise as he sees you approach, fully equipped and radiating an aura of \n"
                "power. He raises his staff, and the shadows around him begin to writhe and take shape, \n"
                "ready to defend his brothers' legacy. The battle begins!",
            'battle':
                "The chamber erupts in a chaotic dance of light and shadow as you clash with AHRIM. His staff \n"
                "crackles with corrupted energy, unleashing devastating spells. But you stand your ground, \n"
                "your own weapons imbued with the power of the fallen brothers. The Amulet of the Damned pulses \n"
                "with a warm light, dispelling the shadows that attempt to ensnare you. The battle rages on, \n"
                "each strike bringing you closer to victory.",
            'win':
                "With a final, desperate blow, you vanquish AHRIM. His form dissolves into wisps of dark energy, \n"
                "and the shadows dissipate, revealing the ancient stones of the sepulcher. You have overcome the \n"
                "Barrows' final guardian, claiming its treasures for your own."
        }
    },
}
