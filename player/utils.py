from .models import FirstName, LastName, Gear, Skill, PhysicalDetail, Personality, Clothing, Secret, Background,\
    MeleeWeapon, Appearance
from django.db import transaction

@transaction.atomic
def populate_names():
    first_names = [
        ['Adelaide', 'Alvin', 'Constance', 'Fox', 'Virginia', 'Terrance'],
        ['Alma', 'Balthazaar', 'Fern', 'Jasper', 'Tuesday', 'William'],
        ['Beatrice', 'E.B.', 'Jilly', 'Merrick', 'Vivian', 'J.T.'],
        ['Charlene', 'Francis', 'Vera', 'Quentin', 'Mabel', 'Caleb'],
        ['Rick', 'Ezekial', 'Harriet', 'Saul', 'Rose', 'Thomas'],
        ['Eleanor', 'Doc', 'Pepper', 'Samuel', 'Silas', 'Wyatt']
    ]

    last_names = [
        ['Barrow', 'Coffin', 'Brown', 'Knibbs', 'McCarty', 'Vandermeer'],
        ['Bullock', 'Culpepper', 'Farnum', 'Holliday', 'McDonald', 'Webb'],
        ['Calaver', 'Dreggs', 'Fernsby', 'Goodnight', 'Packhurst', 'Wexley'],
        ['Garrett', 'Dunlow', 'Espinosa', 'Foss', 'Smith', 'Tarwater'],
        ['Cochran', 'Burns', 'Girdwood', 'Pestle', 'Swearinger', 'White'],
        ['Cribbs', 'Bonney', 'Courtright', 'Jones', 'Southwark', 'Young']
    ]

    melee_weapons = [
        ['Antlers', 'Club', 'Fists', 'Rocks', 'Sickle', 'Tomahawk'],
        ['Bare hands', 'Hatchet', 'Metal Baton', 'Rusty Mace', 'Sledgehammer', 'Walking Stick'],
        ['Brass knuckles', 'Iron Club', 'MorningStar', 'Pitchfork', 'Spear', 'Hammer'],
        ['Bronze Dagger', 'Jagged knife', 'Pickaxe', 'Sacrifical Blade', 'Sword', 'Wooden Cross'],
        ['Chains', 'Lead pipe', 'Quarterstaff', 'Shovel', 'Hunting Knife', 'Woodsman Axe'],
        ['Cleaver', 'Maul', 'Rapier', 'Silver Gauntlet', 'Fence Post', 'Whip']
    ]

    ranged_weapons = [
        ['Ball bearings', 'Colt Paterson', 'Hunting Bow', 'Javelin', 'Pocket Pistol', 'Riding Shotgun'],
        ['Blowgun', 'Deringer', 'Hand Axes', 'Longbow', 'Revolver', 'Throwing Axe'],
        ['Bola', 'Double-barrel', 'Hand Crossbow', 'Long Darts', 'Rifle', 'Throwing Knives'],
        ['Boomerang', 'Glaive', 'Peacemaker', 'Muzzleloader', 'Shortbow', 'Throwing Stars'],
        ['Carbine', 'Spear', 'Lasso', 'Mystical Rocks', 'Shotgun', 'Winchester'],
        ['Colt 45', 'Holy Water', 'Large Crossbow', 'Peacemaker', 'Sling & rocks', 'Varmint Rifle']
    ]

    gears = [
        ['Acid', 'Crowbar', 'Hacksaw', 'Lock and key', 'Grease', 'Steel Wire'],
        ['Animal Scent', 'Fiddle', 'Hammer', 'Lock picks', 'Mirror', 'Ten Foot Pole'],
        ['Bear Trap', 'Fishing gear', 'Horn', 'Manacles', 'Poison', 'Tinderbox'],
        ['Bedroll', 'Fishing Net', 'Iron Spikes', 'Marbles', 'Rations (3)', 'Torch'],
        ['Chain (10ft)', 'Glue', 'Lantern and oil', 'Medicine (3)', 'Rope (50ft)', 'Waterskin'],
        ['Chalk', 'Grappling Hook', 'Large sack', 'Metal File', 'Shovel', 'Wine']
    ]

    skills = [
        ['Alchemy', 'Climbing', 'Engineering', 'Investigation', 'Nature', 'Sleight of Hand'],
        ['Acrobatics', 'Craft', 'Escape', 'Juggling', 'Performance', 'Stealth'],
        ['Athletics', 'Deception', 'Handle Animal', 'Languages', 'Persuasion', 'Survival'],
        ['Blacksmithing', 'Diplomacy', 'Gambling', 'Leather-making', 'Religion', 'Swimming'],
        ['Bluffing', 'Disable Device', 'History', 'Medicine', 'Riding', 'Teaching'],
        ['Carpentry', 'Disguise', 'Intimidate', 'Music', 'Sailing', 'Weaponry']
    ]

    appearances = [
        ['Athletic', 'Bull-necked', 'Furrowed', 'Petite', 'Sinewy', 'Towering'],
        ['Barrel-Chested', 'Chiseled', 'Giant', 'Pudgy', 'Slender', 'Trim'],
        ['Beautiful', 'Craggy', 'Haggard', 'Red-faced', 'Slumped', 'Weathered'],
        ['Bony', 'Delicate', 'Handsome', 'Ripped', 'Solid', 'Willowy'],
        ['Brawny', 'Gorgeous', 'Hideous', 'Scrawny', 'Square-jawed', 'Wirey'],
        ['Brutish', 'Grizzled', 'Lanky', 'Short', 'Statuesque', 'Wrinkled']
    ]

    physical_details = [
        ['Acid Scars', 'Bronze skinned', 'Dreadlocks', 'Huge beard', 'Muttonchops', 'Ritual scars'],
        ['Battle Scars', 'Body piercings', 'Exotic accent', 'Long Hair', 'Nine fingers', 'Sallow skin'],
        ['Birthmark', 'Burn scars', 'Flogging scars', 'Matted hair', 'Oiled hair', 'Shaved head'],
        ['Braided hair', 'Bushy eyebrows', 'Freckles', 'Missing ear', 'One-eyed', 'Sunburned'],
        ['Brand mark', 'Curly hair', 'Gold tooth', 'Missing teeth', 'Pale skinned', 'Tangled hair'],
        ['Broken nose', 'Dark skinned', 'Hoarse voice', 'Mustache', 'Piercing Eyes', 'Tattoos']
    ]

    personalities = [
        ['Bitter', 'Cowardly', 'Heartless', 'Lazy', 'Righteous', 'Spacey'],
        ['Brave', 'Cunning', 'Honor-bound', 'Loyal', 'Rude', 'Stoic'],
        ['Cautious', 'Driven', 'Hotheaded', 'Menacing', 'Sarcastic', 'Stubborn'],
        ['Chill', 'Entitled', 'Inquisitive', 'Mopey', 'Savage', 'Stuck-up'],
        ['Chipper', 'Gregarious', 'Jolly', 'Nervous', 'Scheming', 'Suspicious'],
        ['Contrary', 'Grumpy', 'Know-it-all', 'Protective', 'Serene', 'Wisecracking']
    ]

    clothing = [
        ['Antique', 'Dated', 'Flamboyant', 'Goofy', 'Oversized', 'Stylish'],
        ['Animal Furs', 'Grimy', 'Food-stained', 'Lacey', 'Patched', 'Tailored'],
        ['Battle-torn', 'Eccentric', 'Formal', 'Military Uniform', 'Practical', 'Tasteless'],
        ['Blood-stained', 'Elegant', 'Frayed', 'Mud-stained', 'Revealing', 'Undersized'],
        ['Brightly-Colored', 'Exotic', 'Frumpy', 'Ostentatious', 'Rumpled', 'Wine-stained'],
        ['Ceremonial', 'Fashionable', 'Garish', 'Outlandish', 'Singed', 'Worn Out']
    ]

    secrets = [
        ['Addicted', 'Cultist', 'Fugitive', 'Insurrectionist', 'Ghost', 'Serial killer'],
        ['Artificial', 'Counterspy', 'Cursed', 'Low born', 'Has a child', 'Smuggler'],
        ['Assassin', 'Demigod', 'Non-human', 'Married', 'Heretic', 'Spy'],
        ['Alien', 'Evil lineage', 'Polygamist', 'Mad prophet', 'High born', 'Time traveler'],
        ['Bankrupt', 'Exiled', 'Protects relic', 'Hunted', 'Huge fortune', 'Transformed'],
        ['Beholden', 'Fence', 'Scandalous birth', 'Monster hunter', 'Illusion', 'War criminal']
    ]

    backgrounds = [
        ['Banker', 'Contortionist', 'Drifter', 'Gambler', 'Oil Man', 'Shop Owner'],
        ['Bank Robber', 'Conman', 'Engineer', 'Horse Trader', 'Peddler', 'Soldier'],
        ['Blackmailer', 'Cook', 'Farmer', 'Kidnapper', 'Performer', 'Speculator'],
        ['Bounty hunter', 'Debt-collector', 'Fence', 'Lawman', 'Pickpocket', 'Teacher'],
        ['Card Shark', 'Deserter', 'Golddigger', 'Mercenary', 'Salesman', 'Trapper'],
        ['Cattleman', 'Doctor', 'Fortuneteller', 'Musician', 'Railworker', 'Writer']
    ]

    # Populate first name model
    for row, name_list in enumerate(first_names):
        for col, name in enumerate(name_list):
            first_name = FirstName(name=name, row=row+1, column=col+1)
            first_name.save()

    # Populate last name model
    for row, name_list in enumerate(last_names):
        for col, name in enumerate(name_list):
            last_name = LastName(name=name, row=row+1, column=col+1)
            last_name.save()

    for row, name_list in enumerate(appearances):
        for col, name in enumerate(name_list):
            appearance = Appearance(name=name, row=row + 1, column=col + 1)
            appearance.save()

    # PhysicalDetail
    for row, name_list in enumerate(physical_details):
        for col, name in enumerate(name_list):
            physical_detail = PhysicalDetail(name=name, row=row + 1, column=col + 1)
            physical_detail.save()

    # Personality
    for row, name_list in enumerate(personalities):
        for col, name in enumerate(name_list):
            personality = Personality(name=name, row=row + 1, column=col + 1)
            personality.save()

    # Clothing
    for row, name_list in enumerate(clothing):
        for col, name in enumerate(name_list):
            clothing_item = Clothing(name=name, row=row + 1, column=col + 1)
            clothing_item.save()

    # Secret
    for row, name_list in enumerate(secrets):
        for col, name in enumerate(name_list):
            secret = Secret(name=name, row=row + 1, column=col + 1)
            secret.save()

    # Background
    for row, name_list in enumerate(backgrounds):
        for col, name in enumerate(name_list):
            background = Background(name=name, row=row + 1, column=col + 1)
            background.save()

    for row, name_list in enumerate(melee_weapons):
        for col, name in enumerate(name_list):
            melee_weapon = MeleeWeapon(name=name, row=row + 1, column=col + 1)
            melee_weapon.save()

    for row, name_list in enumerate(skills):
        for col, name in enumerate(name_list):
            skill = Skill(name=name, row=row + 1, column=col + 1)
            skill.save()