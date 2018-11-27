def onAfterDamage (damage, target, source, move):
    if (source and source != target and move and move.flags['contact'] and not target.hp):
	    damage(source.maxhp / 4, source, target)
	