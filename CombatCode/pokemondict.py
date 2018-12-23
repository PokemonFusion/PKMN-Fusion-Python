import copy, random
import pokemondex as dex

# skeleton dict for pokemon
# we use this instead of constructing dictionaries on the fly to simplify defaults
# 
# if you need to create a pokemon dict without using the standard pokemon creation
# funcs, be sure to import copy and call copy.deepcopy(POKEDICT)
# otherwise everything might go to hell
# ( assignment doesn't copy in python, everything's a pointer )

# note that this dict only stores stuff relevant outside of battle
# since battling pokemon have a lot of additional information that goes away as soon
# as the battle ends, it'd be wiser to make battling pokemon their own data structre
# that references this one
POKEDICT = {
    # Pokemon species, as a dict key
    # this should always be set in actual Pokemon, as a lot of info is derived directly
    # from species definitions
    'species': None,

    # the pokemon's nickname, as a string
    # if None, then the displayed name should be the species's display name
    'nickname': None,

    # gender as a string
    # like in species definitions, should be 'M', 'F', or 'N'
    'gender': None,
    # nature, as a string
    'nature': "Hardy",
    # ability, as a string
    # like in species definitions, should be '0', '1', or 'H'
    # note that species without second or hidden abilities should still be able to
    # get '1' and 'H', as evolutions will inherit this
    # a getter function below will handle translating these into actual ability keys
    'ability': '0',
    
    # ot, as a dbref
    # this could also be turned into a string of numbers like in the games,
    # but that's probably not needed and poor in the long-term
    'ot': None,
    # ball caught in, as a ???
    # probably will just be a string set to the used ball's display name, but
    # that can be decided when items are
    # ( this might not even see use due to card system )
    'ball': None,
    # "met at" statement, as a string
    # displayed as-is, since this doesn't need to hold any real meaning
    # ( might also not see use due to card system )
    'met': None,
    
    # level, as an int
    'level': 1,
    # experience points, as an int
    'xp': 0,
    # friendship, as an int
    'friendship': 0,
    # bond, as an int
    # this is assuming that nufusion's fusion mechanics are the same
    # so this might not stick
    'bond': 0,
    # affection, as an int
    # if bond sticks, this might just be replaced with bond
    'affection': 0,
    # moves known, as a dict of dicts
    # each move should have a key of its move data key,
    # with values for current pp and pp ups applied i.e.
    # absorb: {pp: 20, pp_ups: 0}
    # the rest of the data will be drawn from the move data
    # this may just become a list of move keys depending on out-of-battle mechanics
    'moves': {},
    # movesets, as a list of lists
    # each list should be composed of move keys
    # because of the dynamic nature of python data structures, an arbitrary amount of
    # movesets with 1 to 4 moves could be allowed for each pokemon
    # however, for starting simple, let's just stick to 4 lists of 4 entries,
    # similar to how it's currently done
    'move_sets': [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ],
    # ivs, as a dict
    # uses the same keys as base stats, for simpler stat calculations
    'iv': {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    },
    # evs, as a dict
    # see note about ivs
    # note that the pokemon's actual stats aren't stored, as they can always be calculated
    # on the fly from ivs, evs, and nature
    'ev': {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    },
    
    # hold item, as a ???
    # as of writing, items don't exist nor have a planned way of handling them
    # so for now, this is just a "for future use" thing
    'hold_item': None,
    
    # current hp, as an int
    'hp': 0,
    # current status, as a ???
    # only includes statuses that persist out of battle,
    # like sleep, burn, freeze, etc.
    # this and hp may go unused if pokemon automatically heal after battle
    'status': None,
}

# dict of all the natures and their stat bonuses
# there's nothing preventing the addition of natures that modify hp,
# or more than two stats, or have a different bonuses from +10% and -10%.
NATURES = {
    "Hardy":     None,
    "Lonely":    {'atk': 1.1, 'def': 0.9},
    "Brave":     {'atk': 1.1, 'spe': 0.9},
    "Adamant":   {'atk': 1.1, 'spa': 0.9},
    "Naughty":   {'atk': 1.1, 'spd': 0.9},
    "Bold":      {'def': 1.1, 'atk': 0.9},
    "Docile":    None,
    "Relaxed":   {'def': 1.1, 'spe': 0.9},
    "Impish":    {'def': 1.1, 'spa': 0.9},
    "Lax":       {'def': 1.1, 'spd': 0.9},
    "Timid":     {'spe': 1.1, 'atk': 0.9},
    "Hasty":     {'spe': 1.1, 'def': 0.9},
    "Serious":   None,
    "Jolly":     {'spe': 1.1, 'spa': 0.9},
    "Naive":     {'spe': 1.1, 'spd': 0.9},
    "Modest":    {'spa': 1.1, 'atk': 0.9},
    "Mild":      {'spa': 1.1, 'def': 0.9},
    "Quiet":     {'spa': 1.1, 'spe': 0.9},
    "Bashful":   None,
    "Rash":      {'spa': 1.1, 'spd': 0.9},
    "Calm":      {'spd': 1.1, 'atk': 0.9},
    "Gentle":    {'spd': 1.1, 'def': 0.9},
    "Sassy":     {'spd': 1.1, 'spe': 0.9},
    "Careful":   {'spd': 1.1, 'spa': 0.9},
    "Quirky":    None,
}

# a special getter function that makes sure that a pokemon has a species, and that species
# has data
# if neither is the case, then the pokemon's data is too malformed to do most things
def get_species_data(pokemon):
    species = pokemon.get('species')
    
    # if we don't have a proper value for species, then the pokemon is malformed beyond use
    if species is None:
        return None
    
    return dex.BattlePokedex.get(species)

# returns a dict of all of pokemon's current stats
def get_pokemon_stats(pokemon):
    return {
        'hp': calculate_pokemon_stat(pokemon, 'hp'),
        'atk': calculate_pokemon_stat(pokemon, 'atk'),
        'def': calculate_pokemon_stat(pokemon, 'def'),
        'spa': calculate_pokemon_stat(pokemon, 'spa'),
        'spd': calculate_pokemon_stat(pokemon, 'spd'),
        'spe': calculate_pokemon_stat(pokemon, 'spe')
    }

# calculates and return the value of a pokemon's specific stat, derived from its
# base stats, ivs, evs, and nature
def calculate_pokemon_stat(pokemon, stat):
    # if we don't have a proper value for species, then the pokemon is malformed beyond use
    # and stats are impossible to calculate anyway
    species_data = get_species_data(pokemon)
    
    if species_data is None:
        return 0
        
    # meanwhile we just assume the base stat is 0 if the species data lacks this info
    try:
        base_stat = species_data['baseStats'][stat]
    except(AttributeError, KeyError):
        base_stat = 0
    
    # get the rest of the stuff necessary for calculations
    try:
        iv = pokemon['iv'][stat]
    except(AttributeError, KeyError, TypeError):
        iv = 0

    try:
        ev = pokemon['ev'][stat]
    except(AttributeError, KeyError, TypeError):
        ev = 0

    level = pokemon.get('level', 1)
    nature = pokemon.get('nature', 'Hardy')
    try:
        nature_mult = NATURES[nature][stat]
    except(AttributeError, KeyError, TypeError):
        nature_mult = 1.0
    
    # now for math
    # evs are always quartered
    # and all stats use the same base formula
    ev /= 4
    stat = (((2 * base_stat) + iv + ev) * level) / 100
    
    # hp has different "bonus" values
    if stat == 'hp':
        stat += level + 10
    else:
        stat += 5
    
    # tech hp doesn't have a nature bonus
    # but that doesn't mean we need to not support it incase we add custom natures
    stat = int(stat) * nature_mult
    
    return int(stat)
    
def get_pokemon_ability(pokemon):
    # make sure the pokemon has an ability
    # if it somehow doesn't, then ... it doesn't
    ability = pokemon.get('ability')
    
    if ability is None:
        return None
    
    # need to have a species and proper species data for the ability value to mean anything
    species_data = get_species_data(pokemon)
    
    if species_data is None:
        return None
    
    # ... and that species data needs ability data, too
    ability_data = species_data.get('abilities')
    
    if ability_data is None:
        return None
    
    # if everything's properly formed, then we get the ability stored in the species data
    # that has the key stored in the pokemon's data
    real_ability = ability_data.get(ability)
    
    # but the species doesn't have an ability of that key, then return its '0' key ability
    # don't "fix" its ability value, though; evolutions with an ability of that key will
    # retain the key and get that ability
    if real_ability is None:
        return ability_data.get('0')
    
    return real_ability

# the big daddy function for creating pokemon
# should handle all cases, but if it somehow doesn't, all you need to do to create a pokemon otherwise is copy.deepcopy(POKEDICT) and set the values manually

# by the way, this version has like 0 exception handling
# so Bad Stuff could happen if you don't have kwargs of the proper type
def create_pokemon(species, **kwargs):
    # don't bother with a pokemon that somehow has None passed as its species
    if species is None:
        return None

    # we don't need to check if the species is invalid, however - we don't want screw ups
    # elsewhere causing players to miss out on otherwise valid pokemon
    # we probably do want to add in a check later on if we add admin logs or w/e tho
    # that way we can more easily track screw-ups
    
    # set up the pokemon's personal dict, based off of the skeleton
    pokemon = copy.deepcopy(POKEDICT)
    
    pokemon['species'] = species
    
    # if we're not manually setting the ability, have it randomly pick from '0' or '1'
    # remember, the ability value is just a key for the pokemon's species data
    pokemon['ability'] = kwargs.get('ability') or random.choice(['0', '1'])
    
    # do similarly for nature, but instead pick from NATURES
    pokemon['nature'] = kwargs.get('nature') or random.choice(list(NATURES))
    
    # setting level and xp through kwargs are mutually exclusive
    # for the sake of it, we'll get xp priority since if you're actually defining the
    # pokemon's xp manually, it's almost certainly for a reason
    if kwargs.get('xp'):
        pokemon['xp'] = kwargs.get('xp')
        # calculate level from xp here once we get growth rates and xp tables
    elif kwargs.get('level'):
        pokemon['level'] = kwargs.get('level')
        # calculate xp from level here once we get growth rates and xp tables
        
    # for ease, we'll support partial iv and ev dicts as kwargs
    # since we need to generate ivs that aren't included, we need a list of those
    ivs_to_gen = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
    if kwargs.get('iv'):
        for k, v in kwargs['iv'].items():
            # we could just do pokemon.iv[k] = v
            # but this keeps bad keys from being inserted
            if k in pokemon['iv']:
                pokemon['iv'][k] = v
                
                # remove the stat from the list of ivs to generate
                ivs_to_gen.remove(k)
    
    # then, generate the ivs
    for stat in ivs_to_gen:
        pokemon['iv'][stat] = random.randint(0, 31)

    if kwargs.get('ev'):
        for k, v in kwargs['ev'].items():
            # we could just do pokemon.ev[k] = v
            # but this keeps bad keys from being inserted
            if k in pokemon['ev']:
                pokemon['ev'][k] = v
                
    # now that we have ivs, evs, and level all set up
    # we can set the pokemon's hp value to 100% its max hp if we don't have a kwargs for it
    pokemon['hp'] = kwargs.get('hp') or calculate_pokemon_stat(pokemon, 'hp')
    
    # these all require specific data from the species data
    # since that's incomplete, most of this stuff will be half-functional
    species_data = get_species_data(pokemon)
    
    # friendship is simple; just take the species's value straight if None
    pokemon['friendship'] = kwargs.get('friendship')
    
    if pokemon.get('friendship') is None:
        # i'm guessing at the key name here, so it'll probably need to be changed
        pokemon['friendship'] = species_data.get('friendliness', 0)
        
    # gender is perfectly doable, but for sanity requires a weighted pick function
    # so i'll come back to doing it properly when i have my repo set up
    pokemon['gender'] = kwargs.get('gender') or None
    
    if pokemon['gender'] is None:
        gender_ratio = species_data.get('genderRatio')
        
        if gender_ratio is None:
            # this handling means that None gender is possible
            # but that's probably for the best, as it means that gender getters can
            # try to repair it
            pokemon['gender'] = species_data.get('gender')
        else:
            # choices expects the choices and the weights in separate lists
            # and, specifically, lists
            # so convert the dict storing ratios into two separate lists
            genders = []
            ratios = []
            for gender, ratio in gender_ratio.items():
                genders.append(gender)
                ratios.append(ratio)
            
            # choices returns a list, so we grab the first element of it
            pokemon['gender'] = random.choices(genders, weights=ratios)[0]

    # moves are ... undoable, given that we don't have them set up at all
    # we'll have an additional kwargs key named 'handle_learnset'
    # that when true, handles the pokemon's natural moves on its own
    # even if we're including special moves i.e. event or egg pokemon
    if not kwargs.get('moves') or kwargs.get('handle_learnset', False) is True:
        # put actual move logic here
        pass
    
    if kwargs.get('moves'):
        for k, v in kwargs['moves'].items():
            add_move_to_pokemon(pokemon, k, pp = v.get('pp'), pp_ups = v.get('pp_ups'))
    
    # now to finish with some easy stuff
    # a bunch of values that can just use the skeleton's default
    pokemon['bond'] = kwargs.get('bond', pokemon['bond'])
    pokemon['affection'] = kwargs.get('affection', pokemon['affection'])
    # this'll probably need to be populated naturally later but let's leave that for when
    # we actually have learnsets
    pokemon['move_sets'] = kwargs.get('move_sets', pokemon['move_sets']) 
        
    # a bunch of values that don't need special handling - None is acceptable for them
    pokemon['nickname'] = kwargs.get('nickname')
    pokemon['ot'] = kwargs.get('ot')
    pokemon['ball'] = kwargs.get('ball')
    pokemon['met'] = kwargs.get('met')
    pokemon['status'] = kwargs.get('status')
    # i was about to put hold_item here but, it needs handling for wild pokemon held items, huh?
    # well, we can burn that bridge when we get to it
    
    return pokemon
    
def add_move_to_pokemon(pokemon, move, **kwargs):
    move_dict = None
    
    # if a pokemon's move dict somehow got destroyed, at least restore a blank one
    if not pokemon.get('moves'):
        pokemon['moves'] = {}
    
    # add the move to the move dict if isn't already there
    if move not in pokemon['moves']:
        pokemon['moves'][move] = {}
    
    # get the move's dict 
    move_dict = pokemon['moves'].get(move)
    
    # handle pp ups
    move_dict['pp_ups'] = kwargs.get('pp_ups') or move_dict.get('pp_ups') or 0
    
    # now handle pp, since we have our total pp
    move_dict['pp'] = kwargs.get('pp') or move_dict.get('pp') or 0
    
    # 0 in this case should be the max pp of the move, but we'll handle that later
