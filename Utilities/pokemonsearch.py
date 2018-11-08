from CombatCode.pokemondex import BattlePokedex

#This Will Be The Search Function To Find Pokemon By Type, Name, Number, Move (To Do), etc

def pokenumsearch(pokenum):
    try:
        pokenum = int(pokenum)
    except ValueError:
        print('This Must Be A Valid Number')
        return

    results = pokesearch('num', pokenum)
    print(results)

def poketypesearch(poketype):
    poketype = poketype.capitalize()
    results = pokesearch('types', poketype)
    print(results)

def pokesearch(category, lookingFor):
    #We Will Assume The Category & LookingFor Will Be Formatted Correctly
    result = []
    for key in BattlePokedex:
        if isinstance(BattlePokedex[key][category], int) or isinstance(BattlePokedex[key][category], str):
            val = BattlePokedex[key][category]
            if val == lookingFor:
                result.append(BattlePokedex[key]['species'])
        if isinstance(BattlePokedex[key][category], dict) or isinstance(BattlePokedex[key][category], list):
            for val in BattlePokedex[key][category]:
                if val == lookingFor:
                    result.append(BattlePokedex[key]['species'])

    return result

def pokemovesearch(pokemove):
    pokemove = pokemove.capitalize()
    results = pokemove('moves', pokemove)
    print(results)

