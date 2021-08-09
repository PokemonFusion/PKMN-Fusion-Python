def onModifyMove (move, attacker, defender):
	"""function (move, attacker, defender) {
			if (attacker.species.baseSpecies !== 'Aegislash' || attacker.transformed)
				return;
			if (move.category === 'Status' && move.id !== 'kingsshield')
				return;
			var targetForme = (move.id === 'kingsshield' ? 'Aegislash' : 'Aegislash-Blade');
			if (attacker.species.name !== targetForme)
				attacker.formeChange(targetForme);
		}
	""" 
	pass