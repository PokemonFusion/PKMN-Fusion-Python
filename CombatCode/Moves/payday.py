def onHit(**bvalues):
	"""When this move hits, add or increment payday value on pokemon.
	"""
	# instead of adding it to the field, just add the value to the pokemon
	pokemon = bvalues["pokemon"]
	result = bvalues["result"]
	attname = bvalues["attname"]
	if not hasattr(pokemon, 'payday'):
		pokemon.payday = 0

	pokemon.payday += 1
	result.text.append(F"{attname} throws coins!")
