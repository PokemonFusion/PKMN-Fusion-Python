import json
import string
import parsed_learnset as pl
import learnsets

# Each move is defined as follows, with the first character being the generation number:
#	T - Move is learned via Move Tutor
#	L - Move is learned by levelling up, the level is the following character(s)
#	E - Move is an egg move.
#	M - Move is a TM move
#	S - Event move

def create_move_tables():
	i = 0
	previous = "!"
	learnset = {}
	parsed_learnset = {}
	m_moves = {}
	t_moves = {}
	l_moves = {}
	e_moves = {}
	learnset = learnsets.BattleLearnsets
	for pokemon in learnset:
		# Make sure we don't get any alternate-form pokemon, like Alolan or like Luchador Pikachu.
		# Also make sure Porygon and Kabuto are okay, as the both fit into a similar format.
		if previous in pokemon[:len(previous)] and previous != "porygon" and previous != "kabuto": continue
		# Prevent going past 806, Zeraora
		if i > 806: continue
		if "alola" not in pokemon:
			# Create the entries and everything immediately
			parsed_learnset.update({pokemon: {}})
			parsed_learnset[pokemon].update({"tutor": []})
			parsed_learnset[pokemon].update({"egg": []})
			parsed_learnset[pokemon].update({"tm": []})
			parsed_learnset[pokemon].update({"level": {}})
			# print(f"Learnset of {pokemon}: {learnset[pokemon]['learnset']}")
			for move in learnset[pokemon]['learnset']:
				for method in learnset[pokemon]['learnset'][move]:
					if(method[0] == "7"):
						if("T" in method):
							parsed_learnset[pokemon]["tutor"].append(move)
						if("L" in method):
							move_level = method[method.find("L")+1:]
							try:
								parsed_learnset[pokemon]["level"][f"{move_level}"] += f", {move}"
							except KeyError: parsed_learnset[pokemon]["level"].update({move_level: move})
						if("E" in method):
							parsed_learnset[pokemon]["egg"].append(move)
						if("M" in method):
							parsed_learnset[pokemon]["tm"].append(move)
			previous = pokemon
			i+=1
	learnset_text = "pfLearnset = " + json.dumps(parsed_learnset, separators=(',',':'), indent=4)
	f = open("parsed_learnset.py", "w")
	f.write(learnset_text)
	f.close()

def can_learn_move(pokemon, move, method):
	learnset = pl.pfLearnset
	if(move.lower() in learnset[pokemon.lower()][method.lower()]): return True
	else: return False

def level_moves(pokemon, level):
	learnset = pl.pfLearnset
	moveList = {}
	target = learnset[pokemon.lower()]['level']
	for i in range(1,level):
		try:
			if("," in target[f'{i}']):
				atkList = target[f'{i}'].split(",")
				moveList.update({i: atkList})
			else: moveList.update({i: [target[f'{i}']]})
		except KeyError:
			continue
	return moveList