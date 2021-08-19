import json
import string
import sys

import CombatCode.parsed_learnset as pl
import CombatCode.learnsets as learnsets

# Each move is defined as follows, with the first character being the generation number:
#	T - Move is learned via Move Tutor
#	L - Move is learned by levelling up, the level is the following character(s)
#	E - Move is an egg move.
#	M - Move is a TM move
#	S - Event move
#   V - Imported from another version

def create_move_tables():
    i = 0
    previous = "!"
    parsed_learnset = {}
    gen = ["7", "8"]
    learnset = learnsets.BattleLearnsets
    for pokemon in learnset:
        # Make sure we don't get any alternate-form pokemon, like Alolan or like Luchador Pikachu.
        # Also make sure Porygon and Kabuto are okay, as the both fit into a similar format.
        if previous in pokemon[:len(previous)] and previous != "porygon" and previous != "kabuto": continue
        # Prevent going past 898, Calyrex
        #if i > 898: continue
        if "alola" not in pokemon:
            leveledmoves = []
            # Create the entries and everything immediately
            parsed_learnset.update({pokemon: {}})
            parsed_learnset[pokemon].update({"tutor": []})
            parsed_learnset[pokemon].update({"egg": []})
            parsed_learnset[pokemon].update({"tm": []})
            parsed_learnset[pokemon].update({"level": {}})
            # print(f"Learnset of {pokemon}: {learnset[pokemon]['learnset']}")

            if not learnset[pokemon].get("learnset", None): continue
            for move in learnset[pokemon]['learnset']:
                for method in learnset[pokemon]['learnset'][move]:
                    if (method[0] in gen):
                        if ("T" in method):
                            if move in parsed_learnset[pokemon]["tutor"]: continue
                            parsed_learnset[pokemon]["tutor"].append(move)
                        if ("L" in method):
                            if move not in leveledmoves:
                                leveledmoves.append(move)
                                move_level = method[method.find("L") + 1:]
                                try:
                                    parsed_learnset[pokemon]["level"][f"{move_level}"] += f", {move}"
                                except KeyError:
                                    parsed_learnset[pokemon]["level"].update({move_level: move})
                        if ("E" in method):
                            if move in parsed_learnset[pokemon]["egg"]: continue
                            parsed_learnset[pokemon]["egg"].append(move)
                        if ("M" in method):
                            if move in parsed_learnset[pokemon]["tm"]: continue
                            parsed_learnset[pokemon]["tm"].append(move)
            previous = pokemon
            i += 1
    learnset_text = "pfLearnset = " + json.dumps(parsed_learnset, separators=(',', ':'), indent=4)
    f = open("parsed_learnset.py", "w")
    f.write(learnset_text)
    f.close()


def can_learn_move(pokemon, move, method):
    learnset = pl.pfLearnset
    if (move.lower() in learnset[pokemon.lower()][method.lower()]):
        return True
    else:
        return False


def level_moves(pokemon, level):
    learnset = pl.pfLearnset
    moveList = {}
    try:
        target = learnset[pokemon.lower()]['level']
        for i in range(1, level):
            try:
                if "," in target[f'{i}']:
                    atkList = target[f'{i}'].split(",")
                    moveList.update({i: atkList})
                else:
                    moveList.update({i: [target[f'{i}']]})
            except KeyError:
                continue
    except KeyError:
        return ['None','None','None','None']
    return moveList


if __name__ == "__main__":
    create_move_tables()
