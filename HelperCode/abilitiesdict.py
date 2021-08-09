BattleAbilities = {"noability": {
	"isNonstandard": "Past",
	"name": "No Ability",
	"rating": 0.1,
	"num": 0
  },
  "adaptability": {
	"onModifyMove": "function (move) {\n\t\t\tmove.stab = 2;\n\t\t}",
	"name": "Adaptability",
	"rating": 4,
	"num": 91
  },
  "aerilate": {
	"onModifyTypePriority": -1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tvar noModifyType = [\n\t\t\t\t'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',\n\t\t\t];\n\t\t\tif (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {\n\t\t\t\tmove.type = 'Flying';\n\t\t\t\tmove.aerilateBoosted = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.aerilateBoosted)\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t}",
	"name": "Aerilate",
	"rating": 4,
	"num": 184
  },
  "aftermath": {
	"name": "Aftermath",
	"onDamagingHitOrder": 1,
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (!target.hp && this.checkMoveMakesContact(move, source, target, True)) {\n\t\t\t\tthis.damage(source.baseMaxhp / 4, source, target);\n\t\t\t}\n\t\t}",
	"rating": 2.5,
	"num": 106
  },
  "airlock": {
	"onSwitchIn": "function (pokemon) {\n\t\t\tthis.effectState.switchingIn = True;\n\t\t}",
	"onStart": "function (pokemon) {\n\t\t\t// Air Lock does not activate when Skill Swapped or when Neutralizing Gas leaves the field\n\t\t\tif (!this.effectState.switchingIn)\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Air Lock');\n\t\t\tthis.effectState.switchingIn = False;\n\t\t}",
	"suppressWeather": True,
	"name": "Air Lock",
	"rating": 2,
	"num": 76
  },
  "analytic": {
	"onBasePowerPriority": 21,
	"onBasePower": "function (basePower, pokemon) {\n\t\t\tvar boosted = True;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target === pokemon)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (this.queue.willMove(target)) {\n\t\t\t\t\tboosted = False;\n\t\t\t\t\tbreak;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (boosted) {\n\t\t\t\tthis.debug('Analytic boost');\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Analytic",
	"rating": 2.5,
	"num": 148
  },
  "angerpoint": {
	"onHit": "function (target, source, move) {\n\t\t\tif (!target.hp)\n\t\t\t\treturn;\n\t\t\tif ((move === null || move === void 0 ? void 0 : move.effectType) === 'Move' && target.getMoveHitData(move).crit) {\n\t\t\t\ttarget.setBoost({ atk: 6 });\n\t\t\t\tthis.add('-setboost', target, 'atk', 12, '[from] ability: Anger Point');\n\t\t\t}\n\t\t}",
	"name": "Anger Point",
	"rating": 1.5,
	"num": 83
  },
  "anticipation": {
	"onStart": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tfor (var _b = 0, _c = target.moveSlots; _b < _c.length; _b++) {\n\t\t\t\t\tvar moveSlot = _c[_b];\n\t\t\t\t\tvar move = this.dex.moves.get(moveSlot.move);\n\t\t\t\t\tif (move.category === 'Status')\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tvar moveType = move.id === 'hiddenpower' ? target.hpType : move.type;\n\t\t\t\t\tif (this.dex.getImmunity(moveType, pokemon) && this.dex.getEffectiveness(moveType, pokemon) > 0 ||\n\t\t\t\t\t\tmove.ohko) {\n\t\t\t\t\t\tthis.add('-ability', pokemon, 'Anticipation');\n\t\t\t\t\t\treturn;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Anticipation",
	"rating": 0.5,
	"num": 107
  },
  "arenatrap": {
	"onFoeTrapPokemon": "function (pokemon) {\n\t\t\tif (!pokemon.isAdjacent(this.effectState.target))\n\t\t\t\treturn;\n\t\t\tif (pokemon.isGrounded()) {\n\t\t\t\tpokemon.tryTrap(True);\n\t\t\t}\n\t\t}",
	"onFoeMaybeTrapPokemon": "function (pokemon, source) {\n\t\t\tif (!source)\n\t\t\t\tsource = this.effectState.target;\n\t\t\tif (!source || !pokemon.isAdjacent(source))\n\t\t\t\treturn;\n\t\t\tif (pokemon.isGrounded(!pokemon.knownType)) { // Negate immunity if the type is unknown\n\t\t\t\tpokemon.maybeTrapped = True;\n\t\t\t}\n\t\t}",
	"name": "Arena Trap",
	"rating": 5,
	"num": 71
  },
  "aromaveil": {
	"onAllyTryAddVolatile": "function (status, target, source, effect) {\n\t\t\tif (['attract', 'disable', 'encore', 'healblock', 'taunt', 'torment'].includes(status.id)) {\n\t\t\t\tif (effect.effectType === 'Move') {\n\t\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\t\tthis.add('-block', target, 'ability: Aroma Veil', '[of] ' + effectHolder);\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Aroma Veil",
	"rating": 2,
	"num": 165
  },
  "asoneglastrier": {
	"onPreStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'As One');\n\t\t\tthis.add('-ability', pokemon, 'Unnerve');\n\t\t\tthis.effectState.unnerved = True;\n\t\t}",
	"onEnd": "function () {\n\t\t\tthis.effectState.unnerved = False;\n\t\t}",
	"onFoeTryEatItem": "function () {\n\t\t\treturn !this.effectState.unnerved;\n\t\t}",
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tthis.boost({ atk: length }, source, source, this.dex.abilities.get('chillingneigh'));\n\t\t\t}\n\t\t}",
	"isPermanent": True,
	"name": "As One (Glastrier)",
	"rating": 3.5,
	"num": 266
  },
  "asonespectrier": {
	"onPreStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'As One');\n\t\t\tthis.add('-ability', pokemon, 'Unnerve');\n\t\t\tthis.effectState.unnerved = True;\n\t\t}",
	"onEnd": "function () {\n\t\t\tthis.effectState.unnerved = False;\n\t\t}",
	"onFoeTryEatItem": "function () {\n\t\t\treturn !this.effectState.unnerved;\n\t\t}",
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tthis.boost({ spa: length }, source, source, this.dex.abilities.get('grimneigh'));\n\t\t\t}\n\t\t}",
	"isPermanent": True,
	"name": "As One (Spectrier)",
	"rating": 3.5,
	"num": 267
  },
  "aurabreak": {
	"onStart": "function (pokemon) {\n\t\t\tif (this.suppressingAbility(pokemon))\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Aura Break');\n\t\t}",
	"onAnyTryPrimaryHit": "function (target, source, move) {\n\t\t\tif (target === source || move.category === 'Status')\n\t\t\t\treturn;\n\t\t\tmove.hasAuraBreak = True;\n\t\t}",
	"isBreakable": True,
	"name": "Aura Break",
	"rating": 1,
	"num": 188
  },
  "baddreams": {
	"onResidualOrder": 28,
	"onResidualSubOrder": 2,
	"onResidual": "function (pokemon) {\n\t\t\tif (!pokemon.hp)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target.status === 'slp' || target.hasAbility('comatose')) {\n\t\t\t\t\tthis.damage(target.baseMaxhp / 8, target, pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Bad Dreams",
	"rating": 1.5,
	"num": 123
  },
  "ballfetch": {
	"name": "Ball Fetch",
	"rating": 0,
	"num": 237
  },
  "battery": {
	"onAllyBasePowerPriority": 22,
	"onAllyBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (attacker !== this.effectState.target && move.category === 'Special') {\n\t\t\t\tthis.debug('Battery boost');\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Battery",
	"rating": 0,
	"num": 217
  },
  "battlearmor": {
	"onCriticalHit": False,
	"isBreakable": True,
	"name": "Battle Armor",
	"rating": 1,
	"num": 4
  },
  "battlebond": {
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) !== 'Move') {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (source.species.id === 'greninja' && source.hp && !source.transformed && source.side.foePokemonLeft()) {\n\t\t\t\tthis.add('-activate', source, 'ability: Battle Bond');\n\t\t\t\tsource.formeChange('Greninja-Ash', this.effect, True);\n\t\t\t}\n\t\t}",
	"onModifyMovePriority": -1,
	"onModifyMove": "function (move, attacker) {\n\t\t\tif (move.id === 'watershuriken' && attacker.species.name === 'Greninja-Ash') {\n\t\t\t\tmove.multihit = 3;\n\t\t\t}\n\t\t}",
	"isPermanent": True,
	"name": "Battle Bond",
	"rating": 4,
	"num": 210
  },
  "beastboost": {
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tvar statName = 'atk';\n\t\t\t\tvar bestStat = 0;\n\t\t\t\tvar s = void 0;\n\t\t\t\tfor (s in source.storedStats) {\n\t\t\t\t\tif (source.storedStats[s] > bestStat) {\n\t\t\t\t\t\tstatName = s;\n\t\t\t\t\t\tbestStat = source.storedStats[s];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tthis.boost((_a = {}, _a[statName] = length, _a), source);\n\t\t\t}\n\t\t}",
	"name": "Beast Boost",
	"rating": 3.5,
	"num": 224
  },
  "berserk": {
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect.effectType === \"Move\" &&\n\t\t\t\t!effect.multihit &&\n\t\t\t\t(!effect.negateSecondary && !(effect.hasSheerForce && source.hasAbility('sheerforce')))) {\n\t\t\t\ttarget.abilityState.checkedBerserk = False;\n\t\t\t}\n\t\t\telse {\n\t\t\t\ttarget.abilityState.checkedBerserk = True;\n\t\t\t}\n\t\t}",
	"onTryEatItem": "function (item, pokemon) {\n\t\t\tvar healingItems = [\n\t\t\t\t'aguavberry', 'enigmaberry', 'figyberry', 'iapapaberry', 'magoberry', 'sitrusberry', 'wikiberry', 'oranberry', 'berryjuice',\n\t\t\t];\n\t\t\tif (healingItems.includes(item.id)) {\n\t\t\t\treturn pokemon.abilityState.checkedBerserk;\n\t\t\t}\n\t\t\treturn True;\n\t\t}",
	"onAfterMoveSecondary": "function (target, source, move) {\n\t\t\ttarget.abilityState.checkedBerserk = True;\n\t\t\tif (!source || source === target || !target.hp || !move.totalDamage)\n\t\t\t\treturn;\n\t\t\tvar lastAttackedBy = target.getLastAttackedBy();\n\t\t\tif (!lastAttackedBy)\n\t\t\t\treturn;\n\t\t\tvar damage = move.multihit ? move.totalDamage : lastAttackedBy.damage;\n\t\t\tif (target.hp <= target.maxhp / 2 && target.hp + damage > target.maxhp / 2) {\n\t\t\t\tthis.boost({ spa: 1 });\n\t\t\t}\n\t\t}",
	"name": "Berserk",
	"rating": 2,
	"num": 201
  },
  "bigpecks": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tif (boost.def && boost.def < 0) {\n\t\t\t\tdelete boost.def;\n\t\t\t\tif (!effect.secondaries && effect.id !== 'octolock') {\n\t\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"Defense\", \"[from] ability: Big Pecks\", \"[of] \" + target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Big Pecks",
	"rating": 0.5,
	"num": 145
  },
  "blaze": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Fire' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Blaze boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Fire' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Blaze boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Blaze",
	"rating": 2,
	"num": 66
  },
  "bulletproof": {
	"onTryHit": "function (pokemon, target, move) {\n\t\t\tif (move.flags['bullet']) {\n\t\t\t\tthis.add('-immune', pokemon, '[from] ability: Bulletproof');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Bulletproof",
	"rating": 3,
	"num": 171
  },
  "cheekpouch": {
	"onEatItem": "function (item, pokemon) {\n\t\t\tthis.heal(pokemon.baseMaxhp / 3);\n\t\t}",
	"name": "Cheek Pouch",
	"rating": 2,
	"num": 167
  },
  "chillingneigh": {
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tthis.boost({ atk: length }, source);\n\t\t\t}\n\t\t}",
	"name": "Chilling Neigh",
	"rating": 3,
	"num": 264
  },
  "chlorophyll": {
	"onModifySpe": "function (spe, pokemon) {\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Chlorophyll",
	"rating": 3,
	"num": 34
  },
  "clearbody": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tvar showMsg = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tdelete boost[i];\n\t\t\t\t\tshowMsg = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (showMsg && !effect.secondaries && effect.id !== 'octolock') {\n\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"[from] ability: Clear Body\", \"[of] \" + target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Clear Body",
	"rating": 2,
	"num": 29
  },
  "cloudnine": {
	"onSwitchIn": "function (pokemon) {\n\t\t\tthis.effectState.switchingIn = True;\n\t\t}",
	"onStart": "function (pokemon) {\n\t\t\t// Cloud Nine does not activate when Skill Swapped or when Neutralizing Gas leaves the field\n\t\t\tif (!this.effectState.switchingIn)\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Cloud Nine');\n\t\t\tthis.effectState.switchingIn = False;\n\t\t}",
	"suppressWeather": True,
	"name": "Cloud Nine",
	"rating": 2,
	"num": 13
  },
  "colorchange": {
	"onAfterMoveSecondary": "function (target, source, move) {\n\t\t\tif (!target.hp)\n\t\t\t\treturn;\n\t\t\tvar type = move.type;\n\t\t\tif (target.isActive && move.effectType === 'Move' && move.category !== 'Status' &&\n\t\t\t\ttype !== '???' && !target.hasType(type)) {\n\t\t\t\tif (!target.setType(type))\n\t\t\t\t\treturn False;\n\t\t\t\tthis.add('-start', target, 'typechange', type, '[from] ability: Color Change');\n\t\t\t\tif (target.side.active.length === 2 && target.position === 1) {\n\t\t\t\t\t// Curse Glitch\n\t\t\t\t\tvar action = this.queue.willMove(target);\n\t\t\t\t\tif (action && action.move.id === 'curse') {\n\t\t\t\t\t\taction.targetLoc = -1;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Color Change",
	"rating": 0,
	"num": 16
  },
  "comatose": {
	"onStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Comatose');\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Comatose');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isPermanent": True,
	"name": "Comatose",
	"rating": 4,
	"num": 213
  },
  "competitive": {
	"onAfterEachBoost": "function (boost, target, source, effect) {\n\t\t\tif (!source || target.isAlly(source)) {\n\t\t\t\tif (effect.id === 'stickyweb') {\n\t\t\t\t\tthis.hint(\"Court Change Sticky Web counts as lowering your own Speed, and Competitive only affects stats lowered by foes.\", True, source.side);\n\t\t\t\t}\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar statsLowered = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tstatsLowered = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (statsLowered) {\n\t\t\t\tthis.add('-ability', target, 'Competitive');\n\t\t\t\tthis.boost({ spa: 2 }, target, target, null, True);\n\t\t\t}\n\t\t}",
	"name": "Competitive",
	"rating": 2.5,
	"num": 172
  },
  "compoundeyes": {
	"onSourceModifyAccuracyPriority": -1,
	"onSourceModifyAccuracy": "function (accuracy) {\n\t\t\tif (typeof accuracy !== 'number')\n\t\t\t\treturn;\n\t\t\tthis.debug('compoundeyes - enhancing accuracy');\n\t\t\treturn this.chainModify([5325, 4096]);\n\t\t}",
	"name": "Compound Eyes",
	"rating": 3,
	"num": 14
  },
  "contrary": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect && effect.id === 'zpower')\n\t\t\t\treturn;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tboost[i] *= -1;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Contrary",
	"rating": 4.5,
	"num": 126
  },
  "corrosion": {
	"name": "Corrosion",
	"rating": 2.5,
	"num": 212
  },
  "cottondown": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tvar activated = False;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (pokemon === target || pokemon.fainted)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (!activated) {\n\t\t\t\t\tthis.add('-ability', target, 'Cotton Down');\n\t\t\t\t\tactivated = True;\n\t\t\t\t}\n\t\t\t\tthis.boost({ spe: -1 }, pokemon, target, null, True);\n\t\t\t}\n\t\t}",
	"name": "Cotton Down",
	"rating": 2,
	"num": 238
  },
  "curiousmedicine": {
	"onStart": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.adjacentAllies(); _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tally.clearBoosts();\n\t\t\t\tthis.add('-clearboost', ally, '[from] ability: Curious Medicine', '[of] ' + pokemon);\n\t\t\t}\n\t\t}",
	"name": "Curious Medicine",
	"rating": 0,
	"num": 261
  },
  "cursedbody": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (source.volatiles['disable'])\n\t\t\t\treturn;\n\t\t\tif (!move.isMax && !move.isFutureMove && move.id !== 'struggle') {\n\t\t\t\tif (this.randomChance(3, 10)) {\n\t\t\t\t\tsource.addVolatile('disable', this.effectState.target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Cursed Body",
	"rating": 2,
	"num": 130
  },
  "cutecharm": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\tif (this.randomChance(3, 10)) {\n\t\t\t\t\tsource.addVolatile('attract', this.effectState.target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Cute Charm",
	"rating": 0.5,
	"num": 56
  },
  "damp": {
	"onAnyTryMove": "function (target, source, effect) {\n\t\t\tif (['explosion', 'mindblown', 'mistyexplosion', 'selfdestruct'].includes(effect.id)) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('cant', this.effectState.target, 'ability: Damp', effect, '[of] ' + target);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"onAnyDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect && effect.id === 'aftermath') {\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Damp",
	"rating": 1,
	"num": 6
  },
  "dancer": {
	"name": "Dancer",
	"rating": 1.5,
	"num": 216
  },
  "darkaura": {
	"onStart": "function (pokemon) {\n\t\t\tif (this.suppressingAbility(pokemon))\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Dark Aura');\n\t\t}",
	"onAnyBasePowerPriority": 20,
	"onAnyBasePower": "function (basePower, source, target, move) {\n\t\t\tif (target === source || move.category === 'Status' || move.type !== 'Dark')\n\t\t\t\treturn;\n\t\t\tif (!move.auraBooster)\n\t\t\t\tmove.auraBooster = this.effectState.target;\n\t\t\tif (move.auraBooster !== this.effectState.target)\n\t\t\t\treturn;\n\t\t\treturn this.chainModify([move.hasAuraBreak ? 3072 : 5448, 4096]);\n\t\t}",
	"isBreakable": True,
	"name": "Dark Aura",
	"rating": 3,
	"num": 186
  },
  "dauntlessshield": {
	"onStart": "function (pokemon) {\n\t\t\tthis.boost({ def: 1 }, pokemon);\n\t\t}",
	"name": "Dauntless Shield",
	"rating": 3.5,
	"num": 235
  },
  "dazzling": {
	"onFoeTryMove": "function (target, source, move) {\n\t\t\tvar targetAllExceptions = ['perishsong', 'flowershield', 'rototiller'];\n\t\t\tif (move.target === 'foeSide' || (move.target === 'all' && !targetAllExceptions.includes(move.id))) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar dazzlingHolder = this.effectState.target;\n\t\t\tif ((source.isAlly(dazzlingHolder) || move.target === 'all') && move.priority > 0.1) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('cant', dazzlingHolder, 'ability: Dazzling', move, '[of] ' + target);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Dazzling",
	"rating": 2.5,
	"num": 219
  },
  "defeatist": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, pokemon) {\n\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, pokemon) {\n\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"name": "Defeatist",
	"rating": -1,
	"num": 129
  },
  "defiant": {
	"onAfterEachBoost": "function (boost, target, source, effect) {\n\t\t\tif (!source || target.isAlly(source)) {\n\t\t\t\tif (effect.id === 'stickyweb') {\n\t\t\t\t\tthis.hint(\"Court Change Sticky Web counts as lowering your own Speed, and Defiant only affects stats lowered by foes.\", True, source.side);\n\t\t\t\t}\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar statsLowered = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tstatsLowered = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (statsLowered) {\n\t\t\t\tthis.add('-ability', target, 'Defiant');\n\t\t\t\tthis.boost({ atk: 2 }, target, target, null, True);\n\t\t\t}\n\t\t}",
	"name": "Defiant",
	"rating": 2.5,
	"num": 128
  },
  "deltastream": {
	"onStart": "function (source) {\n\t\t\tthis.field.setWeather('deltastream');\n\t\t}",
	"onAnySetWeather": "function (target, source, weather) {\n\t\t\tvar strongWeathers = ['desolateland', 'primordialsea', 'deltastream'];\n\t\t\tif (this.field.getWeather().id === 'deltastream' && !strongWeathers.includes(weather.id))\n\t\t\t\treturn False;\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tif (this.field.weatherState.source !== pokemon)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target === pokemon)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (target.hasAbility('deltastream')) {\n\t\t\t\t\tthis.field.weatherState.source = target;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.field.clearWeather();\n\t\t}",
	"name": "Delta Stream",
	"rating": 4,
	"num": 191
  },
  "desolateland": {
	"onStart": "function (source) {\n\t\t\tthis.field.setWeather('desolateland');\n\t\t}",
	"onAnySetWeather": "function (target, source, weather) {\n\t\t\tvar strongWeathers = ['desolateland', 'primordialsea', 'deltastream'];\n\t\t\tif (this.field.getWeather().id === 'desolateland' && !strongWeathers.includes(weather.id))\n\t\t\t\treturn False;\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tif (this.field.weatherState.source !== pokemon)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target === pokemon)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (target.hasAbility('desolateland')) {\n\t\t\t\t\tthis.field.weatherState.source = target;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.field.clearWeather();\n\t\t}",
	"name": "Desolate Land",
	"rating": 4.5,
	"num": 190
  },
  "disguise": {
	"onDamagePriority": 1,
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move' &&\n\t\t\t\t['mimikyu', 'mimikyutotem'].includes(target.species.id) && !target.transformed) {\n\t\t\t\tthis.add('-activate', target, 'ability: Disguise');\n\t\t\t\tthis.effectState.busted = True;\n\t\t\t\treturn 0;\n\t\t\t}\n\t\t}",
	"onCriticalHit": "function (target, source, move) {\n\t\t\tif (!target)\n\t\t\t\treturn;\n\t\t\tif (!['mimikyu', 'mimikyutotem'].includes(target.species.id) || target.transformed) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);\n\t\t\tif (hitSub)\n\t\t\t\treturn;\n\t\t\tif (!target.runImmunity(move.type))\n\t\t\t\treturn;\n\t\t\treturn False;\n\t\t}",
	"onEffectiveness": "function (typeMod, target, type, move) {\n\t\t\tif (!target || move.category === 'Status')\n\t\t\t\treturn;\n\t\t\tif (!['mimikyu', 'mimikyutotem'].includes(target.species.id) || target.transformed) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);\n\t\t\tif (hitSub)\n\t\t\t\treturn;\n\t\t\tif (!target.runImmunity(move.type))\n\t\t\t\treturn;\n\t\t\treturn 0;\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (['mimikyu', 'mimikyutotem'].includes(pokemon.species.id) && this.effectState.busted) {\n\t\t\t\tvar speciesid = pokemon.species.id === 'mimikyutotem' ? 'Mimikyu-Busted-Totem' : 'Mimikyu-Busted';\n\t\t\t\tpokemon.formeChange(speciesid, this.effect, True);\n\t\t\t\tthis.damage(pokemon.baseMaxhp / 8, pokemon, pokemon, this.dex.species.get(speciesid));\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"isPermanent": True,
	"name": "Disguise",
	"rating": 3.5,
	"num": 209
  },
  "download": {
	"onStart": "function (pokemon) {\n\t\t\tvar totaldef = 0;\n\t\t\tvar totalspd = 0;\n\t\t\tfor (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\ttotaldef += target.getStat('def', False, True);\n\t\t\t\ttotalspd += target.getStat('spd', False, True);\n\t\t\t}\n\t\t\tif (totaldef && totaldef >= totalspd) {\n\t\t\t\tthis.boost({ spa: 1 });\n\t\t\t}\n\t\t\telse if (totalspd) {\n\t\t\t\tthis.boost({ atk: 1 });\n\t\t\t}\n\t\t}",
	"name": "Download",
	"rating": 3.5,
	"num": 88
  },
  "dragonsmaw": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Dragon') {\n\t\t\t\tthis.debug('Dragon's Maw boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Dragon') {\n\t\t\t\tthis.debug('Dragon's Maw boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Dragon's Maw",
	"rating": 3.5,
	"num": 263
  },
  "drizzle": {
	"onStart": "function (source) {\n\t\t\tfor (var _i = 0, _a = this.queue; _i < _a.length; _i++) {\n\t\t\t\tvar action = _a[_i];\n\t\t\t\tif (action.choice === 'runPrimal' && action.pokemon === source && source.species.id === 'kyogre')\n\t\t\t\t\treturn;\n\t\t\t\tif (action.choice !== 'runSwitch' && action.choice !== 'runPrimal')\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\tthis.field.setWeather('raindance');\n\t\t}",
	"name": "Drizzle",
	"rating": 4,
	"num": 2
  },
  "drought": {
	"onStart": "function (source) {\n\t\t\tfor (var _i = 0, _a = this.queue; _i < _a.length; _i++) {\n\t\t\t\tvar action = _a[_i];\n\t\t\t\tif (action.choice === 'runPrimal' && action.pokemon === source && source.species.id === 'groudon')\n\t\t\t\t\treturn;\n\t\t\t\tif (action.choice !== 'runSwitch' && action.choice !== 'runPrimal')\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\tthis.field.setWeather('sunnyday');\n\t\t}",
	"name": "Drought",
	"rating": 4,
	"num": 70
  },
  "dryskin": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Water') {\n\t\t\t\tif (!this.heal(target.baseMaxhp / 4)) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Dry Skin');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onFoeBasePowerPriority": 17,
	"onFoeBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (this.effectState.target !== defender)\n\t\t\t\treturn;\n\t\t\tif (move.type === 'Fire') {\n\t\t\t\treturn this.chainModify(1.25);\n\t\t\t}\n\t\t}",
	"onWeather": "function (target, source, effect) {\n\t\t\tif (target.hasItem('utilityumbrella'))\n\t\t\t\treturn;\n\t\t\tif (effect.id === 'raindance' || effect.id === 'primordialsea') {\n\t\t\t\tthis.heal(target.baseMaxhp / 8);\n\t\t\t}\n\t\t\telse if (effect.id === 'sunnyday' || effect.id === 'desolateland') {\n\t\t\t\tthis.damage(target.baseMaxhp / 8, target, target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Dry Skin",
	"rating": 3,
	"num": 87
  },
  "earlybird": {
	"name": "Early Bird",
	"rating": 1.5,
	"num": 48
  },
  "effectspore": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target) && !source.status && source.runStatusImmunity('powder')) {\n\t\t\t\tvar r = this.random(100);\n\t\t\t\tif (r < 11) {\n\t\t\t\t\tsource.setStatus('slp', target);\n\t\t\t\t}\n\t\t\t\telse if (r < 21) {\n\t\t\t\t\tsource.setStatus('par', target);\n\t\t\t\t}\n\t\t\t\telse if (r < 30) {\n\t\t\t\t\tsource.setStatus('psn', target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Effect Spore",
	"rating": 2,
	"num": 27
  },
  "electricsurge": {
	"onStart": "function (source) {\n\t\t\tthis.field.setTerrain('electricterrain');\n\t\t}",
	"name": "Electric Surge",
	"rating": 4,
	"num": 226
  },
  "emergencyexit": {
	"onEmergencyExit": "function (target) {\n\t\t\tif (!this.canSwitch(target.side) || target.forceSwitchFlag || target.switchFlag)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = this.sides; _i < _a.length; _i++) {\n\t\t\t\tvar side = _a[_i];\n\t\t\t\tfor (var _b = 0, _c = side.active; _b < _c.length; _b++) {\n\t\t\t\t\tvar active = _c[_b];\n\t\t\t\t\tactive.switchFlag = False;\n\t\t\t\t}\n\t\t\t}\n\t\t\ttarget.switchFlag = True;\n\t\t\tthis.add('-activate', target, 'ability: Emergency Exit');\n\t\t}",
	"name": "Emergency Exit",
	"rating": 1,
	"num": 194
  },
  "fairyaura": {
	"onStart": "function (pokemon) {\n\t\t\tif (this.suppressingAbility(pokemon))\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Fairy Aura');\n\t\t}",
	"onAnyBasePowerPriority": 20,
	"onAnyBasePower": "function (basePower, source, target, move) {\n\t\t\tif (target === source || move.category === 'Status' || move.type !== 'Fairy')\n\t\t\t\treturn;\n\t\t\tif (!move.auraBooster)\n\t\t\t\tmove.auraBooster = this.effectState.target;\n\t\t\tif (move.auraBooster !== this.effectState.target)\n\t\t\t\treturn;\n\t\t\treturn this.chainModify([move.hasAuraBreak ? 3072 : 5448, 4096]);\n\t\t}",
	"isBreakable": True,
	"name": "Fairy Aura",
	"rating": 3,
	"num": 187
  },
  "filter": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.getMoveHitData(move).typeMod > 0) {\n\t\t\t\tthis.debug('Filter neutralize');\n\t\t\t\treturn this.chainModify(0.75);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Filter",
	"rating": 3,
	"num": 111
  },
  "flamebody": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\tif (this.randomChance(3, 10)) {\n\t\t\t\t\tsource.trySetStatus('brn', target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Flame Body",
	"rating": 2,
	"num": 49
  },
  "flareboost": {
	"onBasePowerPriority": 19,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (attacker.status === 'brn' && move.category === 'Special') {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Flare Boost",
	"rating": 2,
	"num": 138
  },
  "flashfire": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Fire') {\n\t\t\t\tmove.accuracy = True;\n\t\t\t\tif (!target.addVolatile('flashfire')) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Flash Fire');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tpokemon.removeVolatile('flashfire');\n\t\t}",
	"condition": {
	  "noCopy": True,
	  "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'ability: Flash Fire');\n\t\t\t}",
	  "onModifyAtkPriority": 5,
	  "onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Fire' && attacker.hasAbility('flashfire')) {\n\t\t\t\t\tthis.debug('Flash Fire boost');\n\t\t\t\t\treturn this.chainModify(1.5);\n\t\t\t\t}\n\t\t\t}",
	  "onModifySpAPriority": 5,
	  "onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Fire' && attacker.hasAbility('flashfire')) {\n\t\t\t\t\tthis.debug('Flash Fire boost');\n\t\t\t\t\treturn this.chainModify(1.5);\n\t\t\t\t}\n\t\t\t}",
	  "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'ability: Flash Fire', '[silent]');\n\t\t\t}"
	},
	"isBreakable": True,
	"name": "Flash Fire",
	"rating": 3.5,
	"num": 18
  },
  "flowergift": {
	"onStart": "function (pokemon) {\n\t\t\tdelete this.effectState.forme;\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (!pokemon.isActive || pokemon.baseSpecies.baseSpecies !== 'Cherrim' || pokemon.transformed)\n\t\t\t\treturn;\n\t\t\tif (!pokemon.hp)\n\t\t\t\treturn;\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {\n\t\t\t\tif (pokemon.species.id !== 'cherrimsunshine') {\n\t\t\t\t\tpokemon.formeChange('Cherrim-Sunshine', this.effect, False, '[msg]');\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (pokemon.species.id === 'cherrimsunshine') {\n\t\t\t\t\tpokemon.formeChange('Cherrim', this.effect, False, '[msg]');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onAllyModifyAtkPriority": 3,
	"onAllyModifyAtk": "function (atk, pokemon) {\n\t\t\tif (this.effectState.target.baseSpecies.baseSpecies !== 'Cherrim')\n\t\t\t\treturn;\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onAllyModifySpDPriority": 4,
	"onAllyModifySpD": "function (spd, pokemon) {\n\t\t\tif (this.effectState.target.baseSpecies.baseSpecies !== 'Cherrim')\n\t\t\t\treturn;\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Flower Gift",
	"rating": 1,
	"num": 122
  },
  "flowerveil": {
	"onAllyBoost": "function (boost, target, source, effect) {\n\t\t\tif ((source && target === source) || !target.hasType('Grass'))\n\t\t\t\treturn;\n\t\t\tvar showMsg = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tdelete boost[i];\n\t\t\t\t\tshowMsg = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (showMsg && !effect.secondaries) {\n\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\tthis.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);\n\t\t\t}\n\t\t}",
	"onAllySetStatus": "function (status, target, source, effect) {\n\t\t\tif (target.hasType('Grass') && source && target !== source && effect && effect.id !== 'yawn') {\n\t\t\t\tthis.debug('interrupting setStatus with Flower Veil');\n\t\t\t\tif (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {\n\t\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\t\tthis.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAllyTryAddVolatile": "function (status, target) {\n\t\t\tif (target.hasType('Grass') && status.id === 'yawn') {\n\t\t\t\tthis.debug('Flower Veil blocking yawn');\n\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\tthis.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Flower Veil",
	"rating": 0,
	"num": 166
  },
  "fluffy": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tvar mod = 1;\n\t\t\tif (move.type === 'Fire')\n\t\t\t\tmod *= 2;\n\t\t\tif (move.flags['contact'])\n\t\t\t\tmod /= 2;\n\t\t\treturn this.chainModify(mod);\n\t\t}",
	"isBreakable": True,
	"name": "Fluffy",
	"rating": 3.5,
	"num": 218
  },
  "forecast": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Castform' || pokemon.transformed)\n\t\t\t\treturn;\n\t\t\tvar forme = null;\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tif (pokemon.species.id !== 'castformsunny')\n\t\t\t\t\t\tforme = 'Castform-Sunny';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\t\tif (pokemon.species.id !== 'castformrainy')\n\t\t\t\t\t\tforme = 'Castform-Rainy';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'hail':\n\t\t\t\t\tif (pokemon.species.id !== 'castformsnowy')\n\t\t\t\t\t\tforme = 'Castform-Snowy';\n\t\t\t\t\tbreak;\n\t\t\t\tdefault:\n\t\t\t\t\tif (pokemon.species.id !== 'castform')\n\t\t\t\t\t\tforme = 'Castform';\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\tif (pokemon.isActive && forme) {\n\t\t\t\tpokemon.formeChange(forme, this.effect, False, '[msg]');\n\t\t\t}\n\t\t}",
	"name": "Forecast",
	"rating": 2,
	"num": 59
  },
  "forewarn": {
	"onStart": "function (pokemon) {\n\t\t\tvar warnMoves = [];\n\t\t\tvar warnBp = 1;\n\t\t\tfor (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tfor (var _b = 0, _c = target.moveSlots; _b < _c.length; _b++) {\n\t\t\t\t\tvar moveSlot = _c[_b];\n\t\t\t\t\tvar move = this.dex.moves.get(moveSlot.move);\n\t\t\t\t\tvar bp = move.basePower;\n\t\t\t\t\tif (move.ohko)\n\t\t\t\t\t\tbp = 150;\n\t\t\t\t\tif (move.id === 'counter' || move.id === 'metalburst' || move.id === 'mirrorcoat')\n\t\t\t\t\t\tbp = 120;\n\t\t\t\t\tif (bp === 1)\n\t\t\t\t\t\tbp = 80;\n\t\t\t\t\tif (!bp && move.category !== 'Status')\n\t\t\t\t\t\tbp = 80;\n\t\t\t\t\tif (bp > warnBp) {\n\t\t\t\t\t\twarnMoves = [[move, target]];\n\t\t\t\t\t\twarnBp = bp;\n\t\t\t\t\t}\n\t\t\t\t\telse if (bp === warnBp) {\n\t\t\t\t\t\twarnMoves.push([move, target]);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!warnMoves.length)\n\t\t\t\treturn;\n\t\t\tvar _d = this.sample(warnMoves), warnMoveName = _d[0], warnTarget = _d[1];\n\t\t\tthis.add('-activate', pokemon, 'ability: Forewarn', warnMoveName, '[of] ' + warnTarget);\n\t\t}",
	"name": "Forewarn",
	"rating": 0.5,
	"num": 108
  },
  "friendguard": {
	"name": "Friend Guard",
	"onAnyModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target !== this.effectState.target && target.isAlly(this.effectState.target)) {\n\t\t\t\tthis.debug('Friend Guard weaken');\n\t\t\t\treturn this.chainModify(0.75);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"rating": 0,
	"num": 132
  },
  "frisk": {
	"onStart": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target.item) {\n\t\t\t\t\tthis.add('-item', target, target.getItem().name, '[from] ability: Frisk', '[of] ' + pokemon, '[identify]');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Frisk",
	"rating": 1.5,
	"num": 119
  },
  "fullmetalbody": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tvar showMsg = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tdelete boost[i];\n\t\t\t\t\tshowMsg = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (showMsg && !effect.secondaries && effect.id !== 'octolock') {\n\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"[from] ability: Full Metal Body\", \"[of] \" + target);\n\t\t\t}\n\t\t}",
	"name": "Full Metal Body",
	"rating": 2,
	"num": 230
  },
  "furcoat": {
	"onModifyDefPriority": 6,
	"onModifyDef": "function (def) {\n\t\t\treturn this.chainModify(2);\n\t\t}",
	"isBreakable": True,
	"name": "Fur Coat",
	"rating": 4,
	"num": 169
  },
  "galewings": {
	"onModifyPriority": "function (priority, pokemon, target, move) {\n\t\t\tif ((move === null || move === void 0 ? void 0 : move.type) === 'Flying' && pokemon.hp === pokemon.maxhp)\n\t\t\t\treturn priority + 1;\n\t\t}",
	"name": "Gale Wings",
	"rating": 3,
	"num": 177
  },
  "galvanize": {
	"onModifyTypePriority": -1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tvar noModifyType = [\n\t\t\t\t'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',\n\t\t\t];\n\t\t\tif (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {\n\t\t\t\tmove.type = 'Electric';\n\t\t\t\tmove.galvanizeBoosted = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.galvanizeBoosted)\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t}",
	"name": "Galvanize",
	"rating": 4,
	"num": 206
  },
  "gluttony": {
	"name": "Gluttony",
	"rating": 1.5,
	"num": 82
  },
  "gooey": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target, True)) {\n\t\t\t\tthis.add('-ability', target, 'Gooey');\n\t\t\t\tthis.boost({ spe: -1 }, source, target, null, True);\n\t\t\t}\n\t\t}",
	"name": "Gooey",
	"rating": 2,
	"num": 183
  },
  "gorillatactics": {
	"onStart": "function (pokemon) {\n\t\t\tpokemon.abilityState.choiceLock = \"\";\n\t\t}",
	"onBeforeMove": "function (pokemon, target, move) {\n\t\t\tif (move.isZOrMaxPowered || move.id === 'struggle')\n\t\t\t\treturn;\n\t\t\tif (pokemon.abilityState.choiceLock && pokemon.abilityState.choiceLock !== move.id) {\n\t\t\t\t// Fails unless ability is being ignored (these events will not run), no PP lost.\n\t\t\t\tthis.addMove('move', pokemon, move.name);\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.debug(\"Disabled by Gorilla Tactics\");\n\t\t\t\tthis.add('-fail', pokemon);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"onModifyMove": "function (move, pokemon) {\n\t\t\tif (pokemon.abilityState.choiceLock || move.isZOrMaxPowered || move.id === 'struggle')\n\t\t\t\treturn;\n\t\t\tpokemon.abilityState.choiceLock = move.id;\n\t\t}",
	"onModifyAtkPriority": 1,
	"onModifyAtk": "function (atk, pokemon) {\n\t\t\tif (pokemon.volatiles['dynamax'])\n\t\t\t\treturn;\n\t\t\t// PLACEHOLDER\n\t\t\tthis.debug('Gorilla Tactics Atk Boost');\n\t\t\treturn this.chainModify(1.5);\n\t\t}",
	"onDisableMove": "function (pokemon) {\n\t\t\tif (!pokemon.abilityState.choiceLock)\n\t\t\t\treturn;\n\t\t\tif (pokemon.volatiles['dynamax'])\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\tif (moveSlot.id !== pokemon.abilityState.choiceLock) {\n\t\t\t\t\tpokemon.disableMove(moveSlot.id, False, this.effectState.sourceEffect);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tpokemon.abilityState.choiceLock = \"\";\n\t\t}",
	"name": "Gorilla Tactics",
	"rating": 4.5,
	"num": 255
  },
  "grasspelt": {
	"onModifyDefPriority": 6,
	"onModifyDef": "function (pokemon) {\n\t\t\tif (this.field.isTerrain('grassyterrain'))\n\t\t\t\treturn this.chainModify(1.5);\n\t\t}",
	"isBreakable": True,
	"name": "Grass Pelt",
	"rating": 0.5,
	"num": 179
  },
  "grassysurge": {
	"onStart": "function (source) {\n\t\t\tthis.field.setTerrain('grassyterrain');\n\t\t}",
	"name": "Grassy Surge",
	"rating": 4,
	"num": 229
  },
  "grimneigh": {
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tthis.boost({ spa: length }, source);\n\t\t\t}\n\t\t}",
	"name": "Grim Neigh",
	"rating": 3,
	"num": 265
  },
  "gulpmissile": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (!source.hp || !source.isActive || target.transformed || target.isSemiInvulnerable())\n\t\t\t\treturn;\n\t\t\tif (['cramorantgulping', 'cramorantgorging'].includes(target.species.id)) {\n\t\t\t\tthis.damage(source.baseMaxhp / 4, source, target);\n\t\t\t\tif (target.species.id === 'cramorantgulping') {\n\t\t\t\t\tthis.boost({ def: -1 }, source, target, null, True);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tsource.trySetStatus('par', target, move);\n\t\t\t\t}\n\t\t\t\ttarget.formeChange('cramorant', move);\n\t\t\t}\n\t\t}",
	"onSourceTryPrimaryHit": "function (target, source, effect) {\n\t\t\tif (effect && effect.id === 'surf' && source.hasAbility('gulpmissile') &&\n\t\t\t\tsource.species.name === 'Cramorant' && !source.transformed) {\n\t\t\t\tvar forme = source.hp <= source.maxhp / 2 ? 'cramorantgorging' : 'cramorantgulping';\n\t\t\t\tsource.formeChange(forme, effect);\n\t\t\t}\n\t\t}",
	"isPermanent": True,
	"name": "Gulp Missile",
	"rating": 2.5,
	"num": 241
  },
  "guts": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, pokemon) {\n\t\t\tif (pokemon.status) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Guts",
	"rating": 3,
	"num": 62
  },
  "harvest": {
	"name": "Harvest",
	"onResidualOrder": 28,
	"onResidualSubOrder": 2,
	"onResidual": "function (pokemon) {\n\t\t\tif (this.field.isWeather(['sunnyday', 'desolateland']) || this.randomChance(1, 2)) {\n\t\t\t\tif (pokemon.hp && !pokemon.item && this.dex.items.get(pokemon.lastItem).isBerry) {\n\t\t\t\t\tpokemon.setItem(pokemon.lastItem);\n\t\t\t\t\tpokemon.lastItem = '';\n\t\t\t\t\tthis.add('-item', pokemon, pokemon.getItem(), '[from] ability: Harvest');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"rating": 2.5,
	"num": 139
  },
  "healer": {
	"name": "Healer",
	"onResidualOrder": 5,
	"onResidualSubOrder": 3,
	"onResidual": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.adjacentAllies(); _i < _a.length; _i++) {\n\t\t\t\tvar allyActive = _a[_i];\n\t\t\t\tif (allyActive.status && this.randomChance(3, 10)) {\n\t\t\t\t\tthis.add('-activate', pokemon, 'ability: Healer');\n\t\t\t\t\tallyActive.cureStatus();\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"rating": 0,
	"num": 131
  },
  "heatproof": {
	"onSourceBasePowerPriority": 18,
	"onSourceBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.type === 'Fire') {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect && effect.id === 'brn') {\n\t\t\t\treturn damage / 2;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Heatproof",
	"rating": 2,
	"num": 85
  },
  "heavymetal": {
	"onModifyWeightPriority": 1,
	"onModifyWeight": "function (weighthg) {\n\t\t\treturn weighthg * 2;\n\t\t}",
	"isBreakable": True,
	"name": "Heavy Metal",
	"rating": 0,
	"num": 134
  },
  "honeygather": {
	"name": "Honey Gather",
	"rating": 0,
	"num": 118
  },
  "hugepower": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk) {\n\t\t\treturn this.chainModify(2);\n\t\t}",
	"name": "Huge Power",
	"rating": 5,
	"num": 37
  },
  "hungerswitch": {
	"onResidualOrder": 29,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.species.baseSpecies !== 'Morpeko' || pokemon.transformed)\n\t\t\t\treturn;\n\t\t\tvar targetForme = pokemon.species.name === 'Morpeko' ? 'Morpeko-Hangry' : 'Morpeko';\n\t\t\tpokemon.formeChange(targetForme);\n\t\t}",
	"name": "Hunger Switch",
	"rating": 1,
	"num": 258
  },
  "hustle": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk) {\n\t\t\treturn this.modify(atk, 1.5);\n\t\t}",
	"onSourceModifyAccuracyPriority": -1,
	"onSourceModifyAccuracy": "function (accuracy, target, source, move) {\n\t\t\tif (move.category === 'Physical' && typeof accuracy === 'number') {\n\t\t\t\treturn this.chainModify([3277, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Hustle",
	"rating": 3.5,
	"num": 55
  },
  "hydration": {
	"onResidualOrder": 5,
	"onResidualSubOrder": 3,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.status && ['raindance', 'primordialsea'].includes(pokemon.effectiveWeather())) {\n\t\t\t\tthis.debug('hydration');\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Hydration');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"name": "Hydration",
	"rating": 1.5,
	"num": 93
  },
  "hypercutter": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tif (boost.atk && boost.atk < 0) {\n\t\t\t\tdelete boost.atk;\n\t\t\t\tif (!effect.secondaries) {\n\t\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"Attack\", \"[from] ability: Hyper Cutter\", \"[of] \" + target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Hyper Cutter",
	"rating": 1.5,
	"num": 52
  },
  "icebody": {
	"onWeather": "function (target, source, effect) {\n\t\t\tif (effect.id === 'hail') {\n\t\t\t\tthis.heal(target.baseMaxhp / 16);\n\t\t\t}\n\t\t}",
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'hail')\n\t\t\t\treturn False;\n\t\t}",
	"name": "Ice Body",
	"rating": 1,
	"num": 115
  },
  "iceface": {
	"onStart": "function (pokemon) {\n\t\t\tif (this.field.isWeather('hail') && pokemon.species.id === 'eiscuenoice' && !pokemon.transformed) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Ice Face');\n\t\t\t\tthis.effectState.busted = False;\n\t\t\t\tpokemon.formeChange('Eiscue', this.effect, True);\n\t\t\t}\n\t\t}",
	"onDamagePriority": 1,
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move' && effect.category === 'Physical' &&\n\t\t\t\ttarget.species.id === 'eiscue' && !target.transformed) {\n\t\t\t\tthis.add('-activate', target, 'ability: Ice Face');\n\t\t\t\tthis.effectState.busted = True;\n\t\t\t\treturn 0;\n\t\t\t}\n\t\t}",
	"onCriticalHit": "function (target, type, move) {\n\t\t\tif (!target)\n\t\t\t\treturn;\n\t\t\tif (move.category !== 'Physical' || target.species.id !== 'eiscue' || target.transformed)\n\t\t\t\treturn;\n\t\t\tif (target.volatiles['substitute'] && !(move.flags['authentic'] || move.infiltrates))\n\t\t\t\treturn;\n\t\t\tif (!target.runImmunity(move.type))\n\t\t\t\treturn;\n\t\t\treturn False;\n\t\t}",
	"onEffectiveness": "function (typeMod, target, type, move) {\n\t\t\tif (!target)\n\t\t\t\treturn;\n\t\t\tif (move.category !== 'Physical' || target.species.id !== 'eiscue' || target.transformed)\n\t\t\t\treturn;\n\t\t\tvar hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);\n\t\t\tif (hitSub)\n\t\t\t\treturn;\n\t\t\tif (!target.runImmunity(move.type))\n\t\t\t\treturn;\n\t\t\treturn 0;\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.species.id === 'eiscue' && this.effectState.busted) {\n\t\t\t\tpokemon.formeChange('Eiscue-Noice', this.effect, True);\n\t\t\t}\n\t\t}",
	"onAnyWeatherStart": "function () {\n\t\t\tvar pokemon = this.effectState.target;\n\t\t\tif (!pokemon.hp)\n\t\t\t\treturn;\n\t\t\tif (this.field.isWeather('hail') && pokemon.species.id === 'eiscuenoice' && !pokemon.transformed) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Ice Face');\n\t\t\t\tthis.effectState.busted = False;\n\t\t\t\tpokemon.formeChange('Eiscue', this.effect, True);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"isPermanent": True,
	"name": "Ice Face",
	"rating": 3,
	"num": 248
  },
  "icescales": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (move.category === 'Special') {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Ice Scales",
	"rating": 4,
	"num": 246
  },
  "illuminate": {
	"name": "Illuminate",
	"rating": 0,
	"num": 35
  },
  "illusion": {
	"onBeforeSwitchIn": "function (pokemon) {\n\t\t\tpokemon.illusion = null;\n\t\t\t// yes, you can Illusion an active pokemon but only if it's to your right\n\t\t\tfor (var i = pokemon.side.pokemon.length - 1; i > pokemon.position; i--) {\n\t\t\t\tvar possibleTarget = pokemon.side.pokemon[i];\n\t\t\t\tif (!possibleTarget.fainted) {\n\t\t\t\t\tpokemon.illusion = possibleTarget;\n\t\t\t\t\tbreak;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (target.illusion) {\n\t\t\t\tthis.singleEvent('End', this.dex.abilities.get('Illusion'), target.abilityState, target, source, move);\n\t\t\t}\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tif (pokemon.illusion) {\n\t\t\t\tthis.debug('illusion cleared');\n\t\t\t\tpokemon.illusion = null;\n\t\t\t\tvar details = pokemon.species.name + (pokemon.level === 100 ? '' : ', L' + pokemon.level) +\n\t\t\t\t\t(pokemon.gender === '' ? '' : ', ' + pokemon.gender) + (pokemon.set.shiny ? ', shiny' : '');\n\t\t\t\tthis.add('replace', pokemon, details);\n\t\t\t\tthis.add('-end', pokemon, 'Illusion');\n\t\t\t}\n\t\t}",
	"onFaint": "function (pokemon) {\n\t\t\tpokemon.illusion = null;\n\t\t}",
	"name": "Illusion",
	"rating": 4.5,
	"num": 149
  },
  "immunity": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'psn' || pokemon.status === 'tox') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Immunity');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'psn' && status.id !== 'tox')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Immunity');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Immunity",
	"rating": 2,
	"num": 17
  },
  "imposter": {
	"onSwitchIn": "function (pokemon) {\n\t\t\tthis.effectState.switchingIn = True;\n\t\t}",
	"onStart": "function (pokemon) {\n\t\t\t// Imposter does not activate when Skill Swapped or when Neutralizing Gas leaves the field\n\t\t\tif (!this.effectState.switchingIn)\n\t\t\t\treturn;\n\t\t\t// copies across in doubles/triples\n\t\t\t// (also copies across in multibattle and diagonally in free-for-all,\n\t\t\t// but side.foe already takes care of those)\n\t\t\tvar target = pokemon.side.foe.active[pokemon.side.foe.active.length - 1 - pokemon.position];\n\t\t\tif (target) {\n\t\t\t\tpokemon.transformInto(target, this.dex.abilities.get('imposter'));\n\t\t\t}\n\t\t\tthis.effectState.switchingIn = False;\n\t\t}",
	"name": "Imposter",
	"rating": 5,
	"num": 150
  },
  "infiltrator": {
	"onModifyMove": "function (move) {\n\t\t\tmove.infiltrates = True;\n\t\t}",
	"name": "Infiltrator",
	"rating": 2.5,
	"num": 151
  },
  "innardsout": {
	"name": "Innards Out",
	"onDamagingHitOrder": 1,
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (!target.hp) {\n\t\t\t\tthis.damage(target.getUndynamaxedHP(damage), source, target);\n\t\t\t}\n\t\t}",
	"rating": 4,
	"num": 215
  },
  "innerfocus": {
	"onTryAddVolatile": "function (status, pokemon) {\n\t\t\tif (status.id === 'flinch')\n\t\t\t\treturn null;\n\t\t}",
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect.id === 'intimidate') {\n\t\t\t\tdelete boost.atk;\n\t\t\t\tthis.add('-fail', target, 'unboost', 'Attack', '[from] ability: Inner Focus', '[of] ' + target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Inner Focus",
	"rating": 1.5,
	"num": 39
  },
  "insomnia": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'slp') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Insomnia');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'slp')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Insomnia');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Insomnia",
	"rating": 2,
	"num": 15
  },
  "intimidate": {
	"onStart": "function (pokemon) {\n\t\t\tvar activated = False;\n\t\t\tfor (var _i = 0, _a = pokemon.adjacentFoes(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (!activated) {\n\t\t\t\t\tthis.add('-ability', pokemon, 'Intimidate', 'boost');\n\t\t\t\t\tactivated = True;\n\t\t\t\t}\n\t\t\t\tif (target.volatiles['substitute']) {\n\t\t\t\t\tthis.add('-immune', target);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.boost({ atk: -1 }, target, pokemon, null, True);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Intimidate",
	"rating": 3.5,
	"num": 22
  },
  "intrepidsword": {
	"onStart": "function (pokemon) {\n\t\t\tthis.boost({ atk: 1 }, pokemon);\n\t\t}",
	"name": "Intrepid Sword",
	"rating": 4,
	"num": 234
  },
  "ironbarbs": {
	"onDamagingHitOrder": 1,
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target, True)) {\n\t\t\t\tthis.damage(source.baseMaxhp / 8, source, target);\n\t\t\t}\n\t\t}",
	"name": "Iron Barbs",
	"rating": 2.5,
	"num": 160
  },
  "ironfist": {
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.flags['punch']) {\n\t\t\t\tthis.debug('Iron Fist boost');\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Iron Fist",
	"rating": 3,
	"num": 89
  },
  "justified": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (move.type === 'Dark') {\n\t\t\t\tthis.boost({ atk: 1 });\n\t\t\t}\n\t\t}",
	"name": "Justified",
	"rating": 2.5,
	"num": 154
  },
  "keeneye": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tif (boost.accuracy && boost.accuracy < 0) {\n\t\t\t\tdelete boost.accuracy;\n\t\t\t\tif (!effect.secondaries) {\n\t\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"accuracy\", \"[from] ability: Keen Eye\", \"[of] \" + target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onModifyMove": "function (move) {\n\t\t\tmove.ignoreEvasion = True;\n\t\t}",
	"isBreakable": True,
	"name": "Keen Eye",
	"rating": 0.5,
	"num": 51
  },
  "klutz": {
	"name": "Klutz",
	"rating": -1,
	"num": 103
  },
  "leafguard": {
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (['sunnyday', 'desolateland'].includes(target.effectiveWeather())) {\n\t\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Leaf Guard');\n\t\t\t\t}\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"onTryAddVolatile": "function (status, target) {\n\t\t\tif (status.id === 'yawn' && ['sunnyday', 'desolateland'].includes(target.effectiveWeather())) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Leaf Guard');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Leaf Guard",
	"rating": 0.5,
	"num": 102
  },
  "levitate": {
	"isBreakable": True,
	"name": "Levitate",
	"rating": 3.5,
	"num": 26
  },
  "libero": {
	"onPrepareHit": "function (source, target, move) {\n\t\t\tif (move.hasBounced || move.sourceEffect === 'snatch')\n\t\t\t\treturn;\n\t\t\tvar type = move.type;\n\t\t\tif (type && type !== '???' && source.getTypes().join() !== type) {\n\t\t\t\tif (!source.setType(type))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-start', source, 'typechange', type, '[from] ability: Libero');\n\t\t\t}\n\t\t}",
	"name": "Libero",
	"rating": 4.5,
	"num": 236
  },
  "lightmetal": {
	"onModifyWeight": "function (weighthg) {\n\t\t\treturn this.trunc(weighthg / 2);\n\t\t}",
	"isBreakable": True,
	"name": "Light Metal",
	"rating": 1,
	"num": 135
  },
  "lightningrod": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Electric') {\n\t\t\t\tif (!this.boost({ spa: 1 })) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Lightning Rod');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAnyRedirectTarget": "function (target, source, source2, move) {\n\t\t\tif (move.type !== 'Electric' || ['firepledge', 'grasspledge', 'waterpledge'].includes(move.id))\n\t\t\t\treturn;\n\t\t\tvar redirectTarget = ['randomNormal', 'adjacentFoe'].includes(move.target) ? 'normal' : move.target;\n\t\t\tif (this.validTarget(this.effectState.target, source, redirectTarget)) {\n\t\t\t\tif (move.smartTarget)\n\t\t\t\t\tmove.smartTarget = False;\n\t\t\t\tif (this.effectState.target !== target) {\n\t\t\t\t\tthis.add('-activate', this.effectState.target, 'ability: Lightning Rod');\n\t\t\t\t}\n\t\t\t\treturn this.effectState.target;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Lightning Rod",
	"rating": 3,
	"num": 31
  },
  "limber": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'par') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Limber');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'par')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Limber');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Limber",
	"rating": 2,
	"num": 7
  },
  "liquidooze": {
	"onSourceTryHeal": "function (damage, target, source, effect) {\n\t\t\tthis.debug(\"Heal is occurring: \" + target + \" <- \" + source + \" :: \" + effect.id);\n\t\t\tvar canOoze = ['drain', 'leechseed', 'strengthsap'];\n\t\t\tif (canOoze.includes(effect.id)) {\n\t\t\t\tthis.damage(damage);\n\t\t\t\treturn 0;\n\t\t\t}\n\t\t}",
	"name": "Liquid Ooze",
	"rating": 1.5,
	"num": 64
  },
  "liquidvoice": {
	"onModifyTypePriority": -1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tif (move.flags['sound'] && !pokemon.volatiles['dynamax']) { // hardcode\n\t\t\t\tmove.type = 'Water';\n\t\t\t}\n\t\t}",
	"name": "Liquid Voice",
	"rating": 1.5,
	"num": 204
  },
  "longreach": {
	"onModifyMove": "function (move) {\n\t\t\tdelete move.flags['contact'];\n\t\t}",
	"name": "Long Reach",
	"rating": 1,
	"num": 203
  },
  "magicbounce": {
	"name": "Magic Bounce",
	"onTryHitPriority": 1,
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target === source || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\tnewMove.hasBounced = True;\n\t\t\tnewMove.pranksterBoosted = False;\n\t\t\tthis.actions.useMove(newMove, target, source);\n\t\t\treturn null;\n\t\t}",
	"onAllyTryHitSide": "function (target, source, move) {\n\t\t\tif (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\tnewMove.hasBounced = True;\n\t\t\tnewMove.pranksterBoosted = False;\n\t\t\tthis.actions.useMove(newMove, this.effectState.target, source);\n\t\t\treturn null;\n\t\t}",
	"condition": {
	  "duration": 1
	},
	"isBreakable": True,
	"rating": 4,
	"num": 156
  },
  "magicguard": {
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect.effectType !== 'Move') {\n\t\t\t\tif (effect.effectType === 'Ability')\n\t\t\t\t\tthis.add('-activate', source, 'ability: ' + effect.name);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"name": "Magic Guard",
	"rating": 4,
	"num": 98
  },
  "magician": {
	"onAfterMoveSecondarySelf": "function (source, target, move) {\n\t\t\tif (!move || !target)\n\t\t\t\treturn;\n\t\t\tif (target !== source && move.category !== 'Status') {\n\t\t\t\tif (source.item || source.volatiles['gem'] || move.id === 'fling')\n\t\t\t\t\treturn;\n\t\t\t\tvar yourItem = target.takeItem(source);\n\t\t\t\tif (!yourItem)\n\t\t\t\t\treturn;\n\t\t\t\tif (!source.setItem(yourItem)) {\n\t\t\t\t\ttarget.item = yourItem.id; // bypass setItem so we don't break choicelock or anything\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.add('-item', source, yourItem, '[from] ability: Magician', '[of] ' + target);\n\t\t\t}\n\t\t}",
	"name": "Magician",
	"rating": 1.5,
	"num": 170
  },
  "magmaarmor": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'frz') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Magma Armor');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'frz')\n\t\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Magma Armor",
	"rating": 1,
	"num": 40
  },
  "magnetpull": {
	"onFoeTrapPokemon": "function (pokemon) {\n\t\t\tif (pokemon.hasType('Steel') && pokemon.isAdjacent(this.effectState.target)) {\n\t\t\t\tpokemon.tryTrap(True);\n\t\t\t}\n\t\t}",
	"onFoeMaybeTrapPokemon": "function (pokemon, source) {\n\t\t\tif (!source)\n\t\t\t\tsource = this.effectState.target;\n\t\t\tif (!source || !pokemon.isAdjacent(source))\n\t\t\t\treturn;\n\t\t\tif (!pokemon.knownType || pokemon.hasType('Steel')) {\n\t\t\t\tpokemon.maybeTrapped = True;\n\t\t\t}\n\t\t}",
	"name": "Magnet Pull",
	"rating": 4,
	"num": 42
  },
  "marvelscale": {
	"onModifyDefPriority": 6,
	"onModifyDef": "function (def, pokemon) {\n\t\t\tif (pokemon.status) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Marvel Scale",
	"rating": 2.5,
	"num": 63
  },
  "megalauncher": {
	"onBasePowerPriority": 19,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.flags['pulse']) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Mega Launcher",
	"rating": 3,
	"num": 178
  },
  "merciless": {
	"onModifyCritRatio": "function (critRatio, source, target) {\n\t\t\tif (target && ['psn', 'tox'].includes(target.status))\n\t\t\t\treturn 5;\n\t\t}",
	"name": "Merciless",
	"rating": 1.5,
	"num": 196
  },
  "mimicry": {
	"onStart": "function (pokemon) {\n\t\t\tif (this.field.terrain) {\n\t\t\t\tpokemon.addVolatile('mimicry');\n\t\t\t}\n\t\t\telse {\n\t\t\t\tvar types = pokemon.baseSpecies.types;\n\t\t\t\tif (pokemon.getTypes().join() === types.join() || !pokemon.setType(types))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-start', pokemon, 'typechange', types.join('/'), '[from] ability: Mimicry');\n\t\t\t\tthis.hint(\"Transform Mimicry changes you to your original un-transformed types.\");\n\t\t\t}\n\t\t}",
	"onAnyTerrainStart": "function () {\n\t\t\tvar pokemon = this.effectState.target;\n\t\t\tdelete pokemon.volatiles['mimicry'];\n\t\t\tpokemon.addVolatile('mimicry');\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tdelete pokemon.volatiles['mimicry'];\n\t\t}",
	"condition": {
	  "onStart": "function (pokemon) {\n\t\t\t\tvar newType;\n\t\t\t\tswitch (this.field.terrain) {\n\t\t\t\t\tcase 'electricterrain':\n\t\t\t\t\t\tnewType = 'Electric';\n\t\t\t\t\t\tbreak;\n\t\t\t\t\tcase 'grassyterrain':\n\t\t\t\t\t\tnewType = 'Grass';\n\t\t\t\t\t\tbreak;\n\t\t\t\t\tcase 'mistyterrain':\n\t\t\t\t\t\tnewType = 'Fairy';\n\t\t\t\t\t\tbreak;\n\t\t\t\t\tcase 'psychicterrain':\n\t\t\t\t\t\tnewType = 'Psychic';\n\t\t\t\t\t\tbreak;\n\t\t\t\t}\n\t\t\t\tif (!newType || pokemon.getTypes().join() === newType || !pokemon.setType(newType))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-start', pokemon, 'typechange', newType, '[from] ability: Mimicry');\n\t\t\t}",
	  "onUpdate": "function (pokemon) {\n\t\t\t\tif (!this.field.terrain) {\n\t\t\t\t\tvar types = pokemon.species.types;\n\t\t\t\t\tif (pokemon.getTypes().join() === types.join() || !pokemon.setType(types))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tthis.add('-activate', pokemon, 'ability: Mimicry');\n\t\t\t\t\tthis.add('-end', pokemon, 'typechange', '[silent]');\n\t\t\t\t\tpokemon.removeVolatile('mimicry');\n\t\t\t\t}\n\t\t\t}"
	},
	"name": "Mimicry",
	"rating": 0.5,
	"num": 250
  },
  "minus": {
	"onModifySpAPriority": 5,
	"onModifySpA": "function (spa, pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.allies(); _i < _a.length; _i++) {\n\t\t\t\tvar allyActive = _a[_i];\n\t\t\t\tif (allyActive.hasAbility(['minus', 'plus'])) {\n\t\t\t\t\treturn this.chainModify(1.5);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Minus",
	"rating": 0,
	"num": 58
  },
  "mirrorarmor": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\t// Don't bounce self stat changes, or boosts that have already bounced\n\t\t\tif (target === source || !boost || effect.id === 'mirrorarmor')\n\t\t\t\treturn;\n\t\t\tvar b;\n\t\t\tfor (b in boost) {\n\t\t\t\tif (boost[b] < 0) {\n\t\t\t\t\tif (target.boosts[b] === -6)\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tvar negativeBoost = {};\n\t\t\t\t\tnegativeBoost[b] = boost[b];\n\t\t\t\t\tdelete boost[b];\n\t\t\t\t\tthis.add('-ability', target, 'Mirror Armor');\n\t\t\t\t\tthis.boost(negativeBoost, source, target, null, True);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Mirror Armor",
	"rating": 2,
	"num": 240
  },
  "mistysurge": {
	"onStart": "function (source) {\n\t\t\tthis.field.setTerrain('mistyterrain');\n\t\t}",
	"name": "Misty Surge",
	"rating": 3.5,
	"num": 228
  },
  "moldbreaker": {
	"onStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Mold Breaker');\n\t\t}",
	"onModifyMove": "function (move) {\n\t\t\tmove.ignoreAbility = True;\n\t\t}",
	"name": "Mold Breaker",
	"rating": 3.5,
	"num": 104
  },
  "moody": {
	"onResidualOrder": 28,
	"onResidualSubOrder": 2,
	"onResidual": "function (pokemon) {\n\t\t\tvar stats = [];\n\t\t\tvar boost = {};\n\t\t\tvar statPlus;\n\t\t\tfor (statPlus in pokemon.boosts) {\n\t\t\t\tif (statPlus === 'accuracy' || statPlus === 'evasion')\n\t\t\t\t\tcontinue;\n\t\t\t\tif (pokemon.boosts[statPlus] < 6) {\n\t\t\t\t\tstats.push(statPlus);\n\t\t\t\t}\n\t\t\t}\n\t\t\tvar randomStat = stats.length ? this.sample(stats) : undefined;\n\t\t\tif (randomStat)\n\t\t\t\tboost[randomStat] = 2;\n\t\t\tstats = [];\n\t\t\tvar statMinus;\n\t\t\tfor (statMinus in pokemon.boosts) {\n\t\t\t\tif (statMinus === 'accuracy' || statMinus === 'evasion')\n\t\t\t\t\tcontinue;\n\t\t\t\tif (pokemon.boosts[statMinus] > -6 && statMinus !== randomStat) {\n\t\t\t\t\tstats.push(statMinus);\n\t\t\t\t}\n\t\t\t}\n\t\t\trandomStat = stats.length ? this.sample(stats) : undefined;\n\t\t\tif (randomStat)\n\t\t\t\tboost[randomStat] = -1;\n\t\t\tthis.boost(boost);\n\t\t}",
	"name": "Moody",
	"rating": 5,
	"num": 141
  },
  "motordrive": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Electric') {\n\t\t\t\tif (!this.boost({ spe: 1 })) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Motor Drive');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Motor Drive",
	"rating": 3,
	"num": 78
  },
  "moxie": {
	"onSourceAfterFaint": "function (length, target, source, effect) {\n\t\t\tif (effect && effect.effectType === 'Move') {\n\t\t\t\tthis.boost({ atk: length }, source);\n\t\t\t}\n\t\t}",
	"name": "Moxie",
	"rating": 3,
	"num": 153
  },
  "multiscale": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.hp >= target.maxhp) {\n\t\t\t\tthis.debug('Multiscale weaken');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Multiscale",
	"rating": 3.5,
	"num": 136
  },
  "multitype": {
	"isPermanent": True,
	"name": "Multitype",
	"rating": 4,
	"num": 121
  },
  "mummy": {
	"name": "Mummy",
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tvar sourceAbility = source.getAbility();\n\t\t\tif (sourceAbility.isPermanent || sourceAbility.id === 'mummy') {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (this.checkMoveMakesContact(move, source, target, !source.isAlly(target))) {\n\t\t\t\tvar oldAbility = source.setAbility('mummy', target);\n\t\t\t\tif (oldAbility) {\n\t\t\t\t\tthis.add('-activate', target, 'ability: Mummy', this.dex.abilities.get(oldAbility).name, '[of] ' + source);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"rating": 2,
	"num": 152
  },
  "naturalcure": {
	"onCheckShow": "function (pokemon) {\n\t\t\t// This is complicated\n\t\t\t// For the most part, in-game, it's obvious whether or not Natural Cure activated,\n\t\t\t// since you can see how many of your opponent's pokemon are statused.\n\t\t\t// The only ambiguous situation happens in Doubles/Triples, where multiple pokemon\n\t\t\t// that could have Natural Cure switch out, but only some of them get cured.\n\t\t\tif (pokemon.side.active.length === 1)\n\t\t\t\treturn;\n\t\t\tif (pokemon.showCure === True || pokemon.showCure === False)\n\t\t\t\treturn;\n\t\t\tvar cureList = [];\n\t\t\tvar noCureCount = 0;\n\t\t\tfor (var _i = 0, _a = pokemon.side.active; _i < _a.length; _i++) {\n\t\t\t\tvar curPoke = _a[_i];\n\t\t\t\t// pokemon not statused\n\t\t\t\tif (!(curPoke === null || curPoke === void 0 ? void 0 : curPoke.status)) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" skipped: not statused or doesn't exist\");\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (curPoke.showCure) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" skipped: Natural Cure already known\");\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tvar species = curPoke.species;\n\t\t\t\t// pokemon can't get Natural Cure\n\t\t\t\tif (!Object.values(species.abilities).includes('Natural Cure')) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" skipped: no Natural Cure\");\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\t// pokemon's ability is known to be Natural Cure\n\t\t\t\tif (!species.abilities['1'] && !species.abilities['H']) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" skipped: only one ability\");\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\t// pokemon isn't switching this turn\n\t\t\t\tif (curPoke !== pokemon && !this.queue.willSwitch(curPoke)) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" skipped: not switching\");\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (curPoke.hasAbility('naturalcure')) {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" confirmed: could be Natural Cure (and is)\");\n\t\t\t\t\tcureList.push(curPoke);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\t// this.add('-message', \"\" + curPoke + \" confirmed: could be Natural Cure (but isn't)\");\n\t\t\t\t\tnoCureCount++;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!cureList.length || !noCureCount) {\n\t\t\t\t// It's possible to know what pokemon were cured\n\t\t\t\tfor (var _b = 0, cureList_1 = cureList; _b < cureList_1.length; _b++) {\n\t\t\t\t\tvar pkmn = cureList_1[_b];\n\t\t\t\t\tpkmn.showCure = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\t// It's not possible to know what pokemon were cured\n\t\t\t\t// Unlike a -hint, this is real information that battlers need, so we use a -message\n\t\t\t\tthis.add('-message', \"(\" + cureList.length + \" of \" + pokemon.side.name + \"'s pokemon \" + (cureList.length === 1 ? \"was\" : \"were\") + \" cured by Natural Cure.)\");\n\t\t\t\tfor (var _c = 0, cureList_2 = cureList; _c < cureList_2.length; _c++) {\n\t\t\t\t\tvar pkmn = cureList_2[_c];\n\t\t\t\t\tpkmn.showCure = False;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onSwitchOut": "function (pokemon) {\n\t\t\tif (!pokemon.status)\n\t\t\t\treturn;\n\t\t\t// if pokemon.showCure is undefined, it was skipped because its ability\n\t\t\t// is known\n\t\t\tif (pokemon.showCure === undefined)\n\t\t\t\tpokemon.showCure = True;\n\t\t\tif (pokemon.showCure)\n\t\t\t\tthis.add('-curestatus', pokemon, pokemon.status, '[from] ability: Natural Cure');\n\t\t\tpokemon.setStatus('');\n\t\t\t// only reset .showCure if it's False\n\t\t\t// (once you know a Pokemon has Natural Cure, its cures are always known)\n\t\t\tif (!pokemon.showCure)\n\t\t\t\tpokemon.showCure = undefined;\n\t\t}",
	"name": "Natural Cure",
	"rating": 2.5,
	"num": 30
  },
  "neuroforce": {
	"onModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (move && target.getMoveHitData(move).typeMod > 0) {\n\t\t\t\treturn this.chainModify([5120, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Neuroforce",
	"rating": 2.5,
	"num": 233
  },
  "neutralizinggas": {
	"onPreStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Neutralizing Gas');\n\t\t\tpokemon.abilityState.ending = False;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target.illusion) {\n\t\t\t\t\tthis.singleEvent('End', this.dex.abilities.get('Illusion'), target.abilityState, target, pokemon, 'neutralizinggas');\n\t\t\t\t}\n\t\t\t\tif (target.volatiles['slowstart']) {\n\t\t\t\t\tdelete target.volatiles['slowstart'];\n\t\t\t\t\tthis.add('-end', target, 'Slow Start', '[silent]');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onEnd": "function (source) {\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (pokemon !== source && pokemon.hasAbility('Neutralizing Gas')) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.add('-end', source, 'ability: Neutralizing Gas');\n\t\t\t// FIXME this happens before the pokemon switches out, should be the opposite order.\n\t\t\t// Not an easy fix since we cant use a supported event. Would need some kind of special event that\n\t\t\t// gathers events to run after the switch and then runs them when the ability is no longer accessible.\n\t\t\t// (If you're tackling this, do note extreme weathers have the same issue)\n\t\t\t// Mark this pokemon's ability as ending so Pokemon#ignoringAbility skips it\n\t\t\tif (source.abilityState.ending)\n\t\t\t\treturn;\n\t\t\tsource.abilityState.ending = True;\n\t\t\tvar sortedActive = this.getAllActive();\n\t\t\tthis.speedSort(sortedActive);\n\t\t\tfor (var _b = 0, sortedActive_1 = sortedActive; _b < sortedActive_1.length; _b++) {\n\t\t\t\tvar pokemon = sortedActive_1[_b];\n\t\t\t\tif (pokemon !== source) {\n\t\t\t\t\t// Will be suppressed by Pokemon#ignoringAbility if needed\n\t\t\t\t\tthis.singleEvent('Start', pokemon.getAbility(), pokemon.abilityState, pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Neutralizing Gas",
	"rating": 4,
	"num": 256
  },
  "noguard": {
	"onAnyInvulnerabilityPriority": 1,
	"onAnyInvulnerability": "function (target, source, move) {\n\t\t\tif (move && (source === this.effectState.target || target === this.effectState.target))\n\t\t\t\treturn 0;\n\t\t}",
	"onAnyAccuracy": "function (accuracy, target, source, move) {\n\t\t\tif (move && (source === this.effectState.target || target === this.effectState.target)) {\n\t\t\t\treturn True;\n\t\t\t}\n\t\t\treturn accuracy;\n\t\t}",
	"name": "No Guard",
	"rating": 4,
	"num": 99
  },
  "normalize": {
	"onModifyTypePriority": 1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tvar noModifyType = [\n\t\t\t\t'hiddenpower', 'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'struggle', 'technoblast', 'terrainpulse', 'weatherball',\n\t\t\t];\n\t\t\tif (!(move.isZ && move.category !== 'Status') && !noModifyType.includes(move.id)) {\n\t\t\t\tmove.type = 'Normal';\n\t\t\t\tmove.normalizeBoosted = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.normalizeBoosted)\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t}",
	"name": "Normalize",
	"rating": 0,
	"num": 96
  },
  "oblivious": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['attract']) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Oblivious');\n\t\t\t\tpokemon.removeVolatile('attract');\n\t\t\t\tthis.add('-end', pokemon, 'move: Attract', '[from] ability: Oblivious');\n\t\t\t}\n\t\t\tif (pokemon.volatiles['taunt']) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Oblivious');\n\t\t\t\tpokemon.removeVolatile('taunt');\n\t\t\t\t// Taunt's volatile already sends the -end message when removed\n\t\t\t}\n\t\t}",
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'attract')\n\t\t\t\treturn False;\n\t\t}",
	"onTryHit": "function (pokemon, target, move) {\n\t\t\tif (move.id === 'attract' || move.id === 'captivate' || move.id === 'taunt') {\n\t\t\t\tthis.add('-immune', pokemon, '[from] ability: Oblivious');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect.id === 'intimidate') {\n\t\t\t\tdelete boost.atk;\n\t\t\t\tthis.add('-fail', target, 'unboost', 'Attack', '[from] ability: Oblivious', '[of] ' + target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Oblivious",
	"rating": 1.5,
	"num": 12
  },
  "overcoat": {
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'sandstorm' || type === 'hail' || type === 'powder')\n\t\t\t\treturn False;\n\t\t}",
	"onTryHitPriority": 1,
	"onTryHit": "function (target, source, move) {\n\t\t\tif (move.flags['powder'] && target !== source && this.dex.getImmunity('powder', target)) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Overcoat');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Overcoat",
	"rating": 2,
	"num": 142
  },
  "overgrow": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Grass' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Overgrow boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Grass' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Overgrow boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Overgrow",
	"rating": 2,
	"num": 65
  },
  "owntempo": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['confusion']) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Own Tempo');\n\t\t\t\tpokemon.removeVolatile('confusion');\n\t\t\t}\n\t\t}",
	"onTryAddVolatile": "function (status, pokemon) {\n\t\t\tif (status.id === 'confusion')\n\t\t\t\treturn null;\n\t\t}",
	"onHit": "function (target, source, move) {\n\t\t\tif ((move === null || move === void 0 ? void 0 : move.volatileStatus) === 'confusion') {\n\t\t\t\tthis.add('-immune', target, 'confusion', '[from] ability: Own Tempo');\n\t\t\t}\n\t\t}",
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect.id === 'intimidate') {\n\t\t\t\tdelete boost.atk;\n\t\t\t\tthis.add('-fail', target, 'unboost', 'Attack', '[from] ability: Own Tempo', '[of] ' + target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Own Tempo",
	"rating": 1.5,
	"num": 20
  },
  "parentalbond": {
	"onPrepareHit": "function (source, target, move) {\n\t\t\tif (move.category === 'Status' || move.selfdestruct || move.multihit)\n\t\t\t\treturn;\n\t\t\tif (['endeavor', 'fling', 'iceball', 'rollout'].includes(move.id))\n\t\t\t\treturn;\n\t\t\tif (!move.flags['charge'] && !move.spreadHit && !move.isZ && !move.isMax) {\n\t\t\t\tmove.multihit = 2;\n\t\t\t\tmove.multihitType = 'parentalbond';\n\t\t\t}\n\t\t}",
	"onSourceModifySecondaries": "function (secondaries, target, source, move) {\n\t\t\tif (move.multihitType === 'parentalbond' && move.id === 'secretpower' && move.hit < 2) {\n\t\t\t\t// hack to prevent accidentally suppressing King's Rock/Razor Fang\n\t\t\t\treturn secondaries.filter(function (effect) { return effect.volatileStatus === 'flinch'; });\n\t\t\t}\n\t\t}",
	"name": "Parental Bond",
	"rating": 4.5,
	"num": 185
  },
  "pastelveil": {
	"onStart": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tif (['psn', 'tox'].includes(ally.status)) {\n\t\t\t\t\tthis.add('-activate', pokemon, 'ability: Pastel Veil');\n\t\t\t\t\tally.cureStatus();\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (['psn', 'tox'].includes(pokemon.status)) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Pastel Veil');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onAllySwitchIn": "function (pokemon) {\n\t\t\tif (['psn', 'tox'].includes(pokemon.status)) {\n\t\t\t\tthis.add('-activate', this.effectState.target, 'ability: Pastel Veil');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (!['psn', 'tox'].includes(status.id))\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Pastel Veil');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"onAllySetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (!['psn', 'tox'].includes(status.id))\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\tthis.add('-block', target, 'ability: Pastel Veil', '[of] ' + effectHolder);\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Pastel Veil",
	"rating": 2,
	"num": 257
  },
  "perishbody": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (!this.checkMoveMakesContact(move, source, target))\n\t\t\t\treturn;\n\t\t\tvar announced = False;\n\t\t\tfor (var _i = 0, _a = [target, source]; _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (pokemon.volatiles['perishsong'])\n\t\t\t\t\tcontinue;\n\t\t\t\tif (!announced) {\n\t\t\t\t\tthis.add('-ability', target, 'Perish Body');\n\t\t\t\t\tannounced = True;\n\t\t\t\t}\n\t\t\t\tpokemon.addVolatile('perishsong');\n\t\t\t}\n\t\t}",
	"name": "Perish Body",
	"rating": 1,
	"num": 253
  },
  "pickpocket": {
	"onAfterMoveSecondary": "function (target, source, move) {\n\t\t\tif (source && source !== target && (move === null || move === void 0 ? void 0 : move.flags['contact'])) {\n\t\t\t\tif (target.item || target.switchFlag || target.forceSwitchFlag || source.switchFlag === True) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tvar yourItem = source.takeItem(target);\n\t\t\t\tif (!yourItem) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (!target.setItem(yourItem)) {\n\t\t\t\t\tsource.item = yourItem.id;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.add('-enditem', source, yourItem, '[silent]', '[from] ability: Pickpocket', '[of] ' + source);\n\t\t\t\tthis.add('-item', target, yourItem, '[from] ability: Pickpocket', '[of] ' + source);\n\t\t\t}\n\t\t}",
	"name": "Pickpocket",
	"rating": 1,
	"num": 124
  },
  "pickup": {
	"onResidualOrder": 28,
	"onResidualSubOrder": 2,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.item)\n\t\t\t\treturn;\n\t\t\tvar pickupTargets = this.getAllActive().filter(function (target) { return (target.lastItem && target.usedItemThisTurn && pokemon.isAdjacent(target)); });\n\t\t\tif (!pickupTargets.length)\n\t\t\t\treturn;\n\t\t\tvar randomTarget = this.sample(pickupTargets);\n\t\t\tvar item = randomTarget.lastItem;\n\t\t\trandomTarget.lastItem = '';\n\t\t\tthis.add('-item', pokemon, this.dex.items.get(item), '[from] ability: Pickup');\n\t\t\tpokemon.setItem(item);\n\t\t}",
	"name": "Pickup",
	"rating": 0.5,
	"num": 53
  },
  "pixilate": {
	"onModifyTypePriority": -1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tvar noModifyType = [\n\t\t\t\t'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',\n\t\t\t];\n\t\t\tif (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {\n\t\t\t\tmove.type = 'Fairy';\n\t\t\t\tmove.pixilateBoosted = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.pixilateBoosted)\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t}",
	"name": "Pixilate",
	"rating": 4,
	"num": 182
  },
  "plus": {
	"onModifySpAPriority": 5,
	"onModifySpA": "function (spa, pokemon) {\n\t\t\tfor (var _i = 0, _a = pokemon.allies(); _i < _a.length; _i++) {\n\t\t\t\tvar allyActive = _a[_i];\n\t\t\t\tif (allyActive.hasAbility(['minus', 'plus'])) {\n\t\t\t\t\treturn this.chainModify(1.5);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Plus",
	"rating": 0,
	"num": 57
  },
  "poisonheal": {
	"onDamagePriority": 1,
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect.id === 'psn' || effect.id === 'tox') {\n\t\t\t\tthis.heal(target.baseMaxhp / 8);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"name": "Poison Heal",
	"rating": 4,
	"num": 90
  },
  "poisonpoint": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\tif (this.randomChance(3, 10)) {\n\t\t\t\t\tsource.trySetStatus('psn', target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Poison Point",
	"rating": 1.5,
	"num": 38
  },
  "poisontouch": {
	"onModifyMove": "function (move) {\n\t\t\tif (!(move === null || move === void 0 ? void 0 : move.flags['contact']) || move.target === 'self')\n\t\t\t\treturn;\n\t\t\tif (!move.secondaries) {\n\t\t\t\tmove.secondaries = [];\n\t\t\t}\n\t\t\tmove.secondaries.push({\n\t\t\t\tchance: 30,\n\t\t\t\tstatus: 'psn',\n\t\t\t\tability: this.dex.abilities.get('poisontouch'),\n\t\t\t});\n\t\t}",
	"name": "Poison Touch",
	"rating": 2,
	"num": 143
  },
  "powerconstruct": {
	"onResidualOrder": 29,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Zygarde' || pokemon.transformed || !pokemon.hp)\n\t\t\t\treturn;\n\t\t\tif (pokemon.species.id === 'zygardecomplete' || pokemon.hp > pokemon.maxhp / 2)\n\t\t\t\treturn;\n\t\t\tthis.add('-activate', pokemon, 'ability: Power Construct');\n\t\t\tpokemon.formeChange('Zygarde-Complete', this.effect, True);\n\t\t\tpokemon.baseMaxhp = Math.floor(Math.floor(2 * pokemon.species.baseStats['hp'] + pokemon.set.ivs['hp'] + Math.floor(pokemon.set.evs['hp'] / 4) + 100) * pokemon.level / 100 + 10);\n\t\t\tvar newMaxHP = pokemon.volatiles['dynamax'] ? (2 * pokemon.baseMaxhp) : pokemon.baseMaxhp;\n\t\t\tpokemon.hp = newMaxHP - (pokemon.maxhp - pokemon.hp);\n\t\t\tpokemon.maxhp = newMaxHP;\n\t\t\tthis.add('-heal', pokemon, pokemon.getHealth, '[silent]');\n\t\t}",
	"isPermanent": True,
	"name": "Power Construct",
	"rating": 5,
	"num": 211
  },
  "powerofalchemy": {
	"onAllyFaint": "function (target) {\n\t\t\tif (!this.effectState.target.hp)\n\t\t\t\treturn;\n\t\t\tvar ability = target.getAbility();\n\t\t\tvar additionalBannedAbilities = [\n\t\t\t\t'noability', 'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'wonderguard',\n\t\t\t];\n\t\t\tif (target.getAbility().isPermanent || additionalBannedAbilities.includes(target.ability))\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', this.effectState.target, ability, '[from] ability: Power of Alchemy', '[of] ' + target);\n\t\t\tthis.effectState.target.setAbility(ability);\n\t\t}",
	"name": "Power of Alchemy",
	"rating": 0,
	"num": 223
  },
  "powerspot": {
	"onAllyBasePowerPriority": 22,
	"onAllyBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (attacker !== this.effectState.target) {\n\t\t\t\tthis.debug('Power Spot boost');\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Power Spot",
	"rating": 1,
	"num": 249
  },
  "prankster": {
	"onModifyPriority": "function (priority, pokemon, target, move) {\n\t\t\tif ((move === null || move === void 0 ? void 0 : move.category) === 'Status') {\n\t\t\t\tmove.pranksterBoosted = True;\n\t\t\t\treturn priority + 1;\n\t\t\t}\n\t\t}",
	"name": "Prankster",
	"rating": 4,
	"num": 158
  },
  "pressure": {
	"onStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Pressure');\n\t\t}",
	"onDeductPP": "function (target, source) {\n\t\t\tif (target.isAlly(source))\n\t\t\t\treturn;\n\t\t\treturn 1;\n\t\t}",
	"name": "Pressure",
	"rating": 2.5,
	"num": 46
  },
  "primordialsea": {
	"onStart": "function (source) {\n\t\t\tthis.field.setWeather('primordialsea');\n\t\t}",
	"onAnySetWeather": "function (target, source, weather) {\n\t\t\tvar strongWeathers = ['desolateland', 'primordialsea', 'deltastream'];\n\t\t\tif (this.field.getWeather().id === 'primordialsea' && !strongWeathers.includes(weather.id))\n\t\t\t\treturn False;\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tif (this.field.weatherState.source !== pokemon)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar target = _a[_i];\n\t\t\t\tif (target === pokemon)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (target.hasAbility('primordialsea')) {\n\t\t\t\t\tthis.field.weatherState.source = target;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.field.clearWeather();\n\t\t}",
	"name": "Primordial Sea",
	"rating": 4.5,
	"num": 189
  },
  "prismarmor": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.getMoveHitData(move).typeMod > 0) {\n\t\t\t\tthis.debug('Prism Armor neutralize');\n\t\t\t\treturn this.chainModify(0.75);\n\t\t\t}\n\t\t}",
	"name": "Prism Armor",
	"rating": 3,
	"num": 232
  },
  "propellertail": {
	"onModifyMovePriority": 1,
	"onModifyMove": "function (move) {\n\t\t\t// most of the implementation is in Battle#getTarget\n\t\t\tmove.tracksTarget = move.target !== 'scripted';\n\t\t}",
	"name": "Propeller Tail",
	"rating": 0,
	"num": 239
  },
  "protean": {
	"onPrepareHit": "function (source, target, move) {\n\t\t\tif (move.hasBounced || move.sourceEffect === 'snatch')\n\t\t\t\treturn;\n\t\t\tvar type = move.type;\n\t\t\tif (type && type !== '???' && source.getTypes().join() !== type) {\n\t\t\t\tif (!source.setType(type))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-start', source, 'typechange', type, '[from] ability: Protean');\n\t\t\t}\n\t\t}",
	"name": "Protean",
	"rating": 4.5,
	"num": 168
  },
  "psychicsurge": {
	"onStart": "function (source) {\n\t\t\tthis.field.setTerrain('psychicterrain');\n\t\t}",
	"name": "Psychic Surge",
	"rating": 4,
	"num": 227
  },
  "punkrock": {
	"onBasePowerPriority": 7,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.flags['sound']) {\n\t\t\t\tthis.debug('Punk Rock boost');\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t}\n\t\t}",
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (move.flags['sound']) {\n\t\t\t\tthis.debug('Punk Rock weaken');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Punk Rock",
	"rating": 3.5,
	"num": 244
  },
  "purepower": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk) {\n\t\t\treturn this.chainModify(2);\n\t\t}",
	"name": "Pure Power",
	"rating": 5,
	"num": 74
  },
  "queenlymajesty": {
	"onFoeTryMove": "function (target, source, move) {\n\t\t\tvar targetAllExceptions = ['perishsong', 'flowershield', 'rototiller'];\n\t\t\tif (move.target === 'foeSide' || (move.target === 'all' && !targetAllExceptions.includes(move.id))) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar dazzlingHolder = this.effectState.target;\n\t\t\tif ((source.isAlly(dazzlingHolder) || move.target === 'all') && move.priority > 0.1) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('cant', dazzlingHolder, 'ability: Queenly Majesty', move, '[of] ' + target);\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Queenly Majesty",
	"rating": 2.5,
	"num": 214
  },
  "quickdraw": {
	"onFractionalPriorityPriority": -1,
	"onFractionalPriority": "function (priority, pokemon, target, move) {\n\t\t\tif (move.category !== \"Status\" && this.randomChance(3, 10)) {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Quick Draw');\n\t\t\t\treturn 0.1;\n\t\t\t}\n\t\t}",
	"name": "Quick Draw",
	"rating": 2.5,
	"num": 259
  },
  "quickfeet": {
	"onModifySpe": "function (spe, pokemon) {\n\t\t\tif (pokemon.status) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Quick Feet",
	"rating": 2.5,
	"num": 95
  },
  "raindish": {
	"onWeather": "function (target, source, effect) {\n\t\t\tif (target.hasItem('utilityumbrella'))\n\t\t\t\treturn;\n\t\t\tif (effect.id === 'raindance' || effect.id === 'primordialsea') {\n\t\t\t\tthis.heal(target.baseMaxhp / 16);\n\t\t\t}\n\t\t}",
	"name": "Rain Dish",
	"rating": 1.5,
	"num": 44
  },
  "rattled": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (['Dark', 'Bug', 'Ghost'].includes(move.type)) {\n\t\t\t\tthis.boost({ spe: 1 });\n\t\t\t}\n\t\t}",
	"onAfterBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect && effect.id === 'intimidate') {\n\t\t\t\tthis.boost({ spe: 1 });\n\t\t\t}\n\t\t}",
	"name": "Rattled",
	"rating": 1.5,
	"num": 155
  },
  "receiver": {
	"onAllyFaint": "function (target) {\n\t\t\tif (!this.effectState.target.hp)\n\t\t\t\treturn;\n\t\t\tvar ability = target.getAbility();\n\t\t\tvar additionalBannedAbilities = [\n\t\t\t\t'noability', 'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'wonderguard',\n\t\t\t];\n\t\t\tif (target.getAbility().isPermanent || additionalBannedAbilities.includes(target.ability))\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', this.effectState.target, ability, '[from] ability: Receiver', '[of] ' + target);\n\t\t\tthis.effectState.target.setAbility(ability);\n\t\t}",
	"name": "Receiver",
	"rating": 0,
	"num": 222
  },
  "reckless": {
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.recoil || move.hasCrashDamage) {\n\t\t\t\tthis.debug('Reckless boost');\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Reckless",
	"rating": 3,
	"num": 120
  },
  "refrigerate": {
	"onModifyTypePriority": -1,
	"onModifyType": "function (move, pokemon) {\n\t\t\tvar noModifyType = [\n\t\t\t\t'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',\n\t\t\t];\n\t\t\tif (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {\n\t\t\t\tmove.type = 'Ice';\n\t\t\t\tmove.refrigerateBoosted = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 23,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.refrigerateBoosted)\n\t\t\t\treturn this.chainModify([4915, 4096]);\n\t\t}",
	"name": "Refrigerate",
	"rating": 4,
	"num": 174
  },
  "regenerator": {
	"onSwitchOut": "function (pokemon) {\n\t\t\tpokemon.heal(pokemon.baseMaxhp / 3);\n\t\t}",
	"name": "Regenerator",
	"rating": 4.5,
	"num": 144
  },
  "ripen": {
	"onTryHeal": "function (damage, target, source, effect) {\n\t\t\tif (!effect)\n\t\t\t\treturn;\n\t\t\tif (effect.id === 'berryjuice' || effect.id === 'leftovers') {\n\t\t\t\tthis.add('-activate', target, 'ability: Ripen');\n\t\t\t}\n\t\t\tif (effect.isBerry)\n\t\t\t\treturn this.chainModify(2);\n\t\t}",
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect && effect.isBerry) {\n\t\t\t\tvar b = void 0;\n\t\t\t\tfor (b in boost) {\n\t\t\t\t\tboost[b] *= 2;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onSourceModifyDamagePriority": -1,
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.abilityState.berryWeaken) {\n\t\t\t\ttarget.abilityState.berryWeaken = False;\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onTryEatItemPriority": -1,
	"onTryEatItem": "function (item, pokemon) {\n\t\t\tthis.add('-activate', pokemon, 'ability: Ripen');\n\t\t}",
	"onEatItem": "function (item, pokemon) {\n\t\t\tvar weakenBerries = [\n\t\t\t\t'Babiri Berry', 'Charti Berry', 'Chilan Berry', 'Chople Berry', 'Coba Berry', 'Colbur Berry', 'Haban Berry', 'Kasib Berry', 'Kebia Berry', 'Occa Berry', 'Passho Berry', 'Payapa Berry', 'Rindo Berry', 'Roseli Berry', 'Shuca Berry', 'Tanga Berry', 'Wacan Berry', 'Yache Berry',\n\t\t\t];\n\t\t\t// Record if the pokemon ate a berry to resist the attack\n\t\t\tpokemon.abilityState.berryWeaken = weakenBerries.includes(item.name);\n\t\t}",
	"name": "Ripen",
	"rating": 2,
	"num": 247
  },
  "rivalry": {
	"onBasePowerPriority": 24,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (attacker.gender && defender.gender) {\n\t\t\t\tif (attacker.gender === defender.gender) {\n\t\t\t\t\tthis.debug('Rivalry boost');\n\t\t\t\t\treturn this.chainModify(1.25);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.debug('Rivalry weaken');\n\t\t\t\t\treturn this.chainModify(0.75);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Rivalry",
	"rating": 0,
	"num": 79
  },
  "rkssystem": {
	"isPermanent": True,
	"name": "RKS System",
	"rating": 4,
	"num": 225
  },
  "rockhead": {
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect.id === 'recoil') {\n\t\t\t\tif (!this.activeMove)\n\t\t\t\t\tthrow new Error(\"Battle.activeMove is null\");\n\t\t\t\tif (this.activeMove.id !== 'struggle')\n\t\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"name": "Rock Head",
	"rating": 3,
	"num": 69
  },
  "roughskin": {
	"onDamagingHitOrder": 1,
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target, True)) {\n\t\t\t\tthis.damage(source.baseMaxhp / 8, source, target);\n\t\t\t}\n\t\t}",
	"name": "Rough Skin",
	"rating": 2.5,
	"num": 24
  },
  "runaway": {
	"name": "Run Away",
	"rating": 0,
	"num": 50
  },
  "sandforce": {
	"onBasePowerPriority": 21,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (this.field.isWeather('sandstorm')) {\n\t\t\t\tif (move.type === 'Rock' || move.type === 'Ground' || move.type === 'Steel') {\n\t\t\t\t\tthis.debug('Sand Force boost');\n\t\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'sandstorm')\n\t\t\t\treturn False;\n\t\t}",
	"name": "Sand Force",
	"rating": 2,
	"num": 159
  },
  "sandrush": {
	"onModifySpe": "function (spe, pokemon) {\n\t\t\tif (this.field.isWeather('sandstorm')) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'sandstorm')\n\t\t\t\treturn False;\n\t\t}",
	"name": "Sand Rush",
	"rating": 3,
	"num": 146
  },
  "sandspit": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.field.getWeather().id !== 'sandstorm') {\n\t\t\t\tthis.field.setWeather('sandstorm');\n\t\t\t}\n\t\t}",
	"name": "Sand Spit",
	"rating": 2,
	"num": 245
  },
  "sandstream": {
	"onStart": "function (source) {\n\t\t\tthis.field.setWeather('sandstorm');\n\t\t}",
	"name": "Sand Stream",
	"rating": 4,
	"num": 45
  },
  "sandveil": {
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'sandstorm')\n\t\t\t\treturn False;\n\t\t}",
	"onModifyAccuracyPriority": -1,
	"onModifyAccuracy": "function (accuracy) {\n\t\t\tif (typeof accuracy !== 'number')\n\t\t\t\treturn;\n\t\t\tif (this.field.isWeather('sandstorm')) {\n\t\t\t\tthis.debug('Sand Veil - decreasing accuracy');\n\t\t\t\treturn this.chainModify([3277, 4096]);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Sand Veil",
	"rating": 1.5,
	"num": 8
  },
  "sapsipper": {
	"onTryHitPriority": 1,
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Grass') {\n\t\t\t\tif (!this.boost({ atk: 1 })) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Sap Sipper');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAllyTryHitSide": "function (target, source, move) {\n\t\t\tif (source === this.effectState.target || !target.isAlly(source))\n\t\t\t\treturn;\n\t\t\tif (move.type === 'Grass') {\n\t\t\t\tthis.boost({ atk: 1 }, this.effectState.target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Sap Sipper",
	"rating": 3,
	"num": 157
  },
  "schooling": {
	"onStart": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Wishiwashi' || pokemon.level < 20 || pokemon.transformed)\n\t\t\t\treturn;\n\t\t\tif (pokemon.hp > pokemon.maxhp / 4) {\n\t\t\t\tif (pokemon.species.id === 'wishiwashi') {\n\t\t\t\t\tpokemon.formeChange('Wishiwashi-School');\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (pokemon.species.id === 'wishiwashischool') {\n\t\t\t\t\tpokemon.formeChange('Wishiwashi');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onResidualOrder": 29,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Wishiwashi' || pokemon.level < 20 ||\n\t\t\t\tpokemon.transformed || !pokemon.hp)\n\t\t\t\treturn;\n\t\t\tif (pokemon.hp > pokemon.maxhp / 4) {\n\t\t\t\tif (pokemon.species.id === 'wishiwashi') {\n\t\t\t\t\tpokemon.formeChange('Wishiwashi-School');\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (pokemon.species.id === 'wishiwashischool') {\n\t\t\t\t\tpokemon.formeChange('Wishiwashi');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"isPermanent": True,
	"name": "Schooling",
	"rating": 3,
	"num": 208
  },
  "scrappy": {
	"onModifyMovePriority": -5,
	"onModifyMove": "function (move) {\n\t\t\tif (!move.ignoreImmunity)\n\t\t\t\tmove.ignoreImmunity = {};\n\t\t\tif (move.ignoreImmunity !== True) {\n\t\t\t\tmove.ignoreImmunity['Fighting'] = True;\n\t\t\t\tmove.ignoreImmunity['Normal'] = True;\n\t\t\t}\n\t\t}",
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect.id === 'intimidate') {\n\t\t\t\tdelete boost.atk;\n\t\t\t\tthis.add('-fail', target, 'unboost', 'Attack', '[from] ability: Scrappy', '[of] ' + target);\n\t\t\t}\n\t\t}",
	"name": "Scrappy",
	"rating": 3,
	"num": 113
  },
  "screencleaner": {
	"onStart": "function (pokemon) {\n\t\t\tvar activated = False;\n\t\t\tfor (var _i = 0, _a = ['reflect', 'lightscreen', 'auroraveil']; _i < _a.length; _i++) {\n\t\t\t\tvar sideCondition = _a[_i];\n\t\t\t\tfor (var _b = 0, _c = __spreadArrays([pokemon.side], pokemon.side.foeSidesWithConditions()); _b < _c.length; _b++) {\n\t\t\t\t\tvar side = _c[_b];\n\t\t\t\t\tif (side.getSideCondition(sideCondition)) {\n\t\t\t\t\t\tif (!activated) {\n\t\t\t\t\t\t\tthis.add('-activate', pokemon, 'ability: Screen Cleaner');\n\t\t\t\t\t\t\tactivated = True;\n\t\t\t\t\t\t}\n\t\t\t\t\t\tside.removeSideCondition(sideCondition);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Screen Cleaner",
	"rating": 2,
	"num": 251
  },
  "serenegrace": {
	"onModifyMovePriority": -2,
	"onModifyMove": "function (move) {\n\t\t\tvar _a;\n\t\t\tif (move.secondaries) {\n\t\t\t\tthis.debug('doubling secondary chance');\n\t\t\t\tfor (var _i = 0, _b = move.secondaries; _i < _b.length; _i++) {\n\t\t\t\t\tvar secondary = _b[_i];\n\t\t\t\t\tif (secondary.chance)\n\t\t\t\t\t\tsecondary.chance *= 2;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif ((_a = move.self) === null || _a === void 0 ? void 0 : _a.chance)\n\t\t\t\tmove.self.chance *= 2;\n\t\t}",
	"name": "Serene Grace",
	"rating": 3.5,
	"num": 32
  },
  "shadowshield": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.hp >= target.maxhp) {\n\t\t\t\tthis.debug('Shadow Shield weaken');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"name": "Shadow Shield",
	"rating": 3.5,
	"num": 231
  },
  "shadowtag": {
	"onFoeTrapPokemon": "function (pokemon) {\n\t\t\tif (!pokemon.hasAbility('shadowtag') && pokemon.isAdjacent(this.effectState.target)) {\n\t\t\t\tpokemon.tryTrap(True);\n\t\t\t}\n\t\t}",
	"onFoeMaybeTrapPokemon": "function (pokemon, source) {\n\t\t\tif (!source)\n\t\t\t\tsource = this.effectState.target;\n\t\t\tif (!source || !pokemon.isAdjacent(source))\n\t\t\t\treturn;\n\t\t\tif (!pokemon.hasAbility('shadowtag')) {\n\t\t\t\tpokemon.maybeTrapped = True;\n\t\t\t}\n\t\t}",
	"name": "Shadow Tag",
	"rating": 5,
	"num": 23
  },
  "shedskin": {
	"onResidualOrder": 5,
	"onResidualSubOrder": 3,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.hp && pokemon.status && this.randomChance(33, 100)) {\n\t\t\t\tthis.debug('shed skin');\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Shed Skin');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"name": "Shed Skin",
	"rating": 3,
	"num": 61
  },
  "sheerforce": {
	"onModifyMove": "function (move, pokemon) {\n\t\t\tif (move.secondaries) {\n\t\t\t\tdelete move.secondaries;\n\t\t\t\t// Technically not a secondary effect, but it is negated\n\t\t\t\tdelete move.self;\n\t\t\t\tif (move.id === 'clangoroussoulblaze')\n\t\t\t\t\tdelete move.selfBoost;\n\t\t\t\t// Actual negation of AfterMoveSecondary effects implemented in scripts.js\n\t\t\t\tmove.hasSheerForce = True;\n\t\t\t}\n\t\t}",
	"onBasePowerPriority": 21,
	"onBasePower": "function (basePower, pokemon, target, move) {\n\t\t\tif (move.hasSheerForce)\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t}",
	"name": "Sheer Force",
	"rating": 3.5,
	"num": 125
  },
  "shellarmor": {
	"onCriticalHit": False,
	"isBreakable": True,
	"name": "Shell Armor",
	"rating": 1,
	"num": 75
  },
  "shielddust": {
	"onModifySecondaries": "function (secondaries) {\n\t\t\tthis.debug('Shield Dust prevent secondary');\n\t\t\treturn secondaries.filter(function (effect) { return !!(effect.self || effect.dustproof); });\n\t\t}",
	"isBreakable": True,
	"name": "Shield Dust",
	"rating": 2,
	"num": 19
  },
  "shieldsdown": {
	"onStart": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Minior' || pokemon.transformed)\n\t\t\t\treturn;\n\t\t\tif (pokemon.hp > pokemon.maxhp / 2) {\n\t\t\t\tif (pokemon.species.forme !== 'Meteor') {\n\t\t\t\t\tpokemon.formeChange('Minior-Meteor');\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (pokemon.species.forme === 'Meteor') {\n\t\t\t\t\tpokemon.formeChange(pokemon.set.species);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onResidualOrder": 29,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Minior' || pokemon.transformed || !pokemon.hp)\n\t\t\t\treturn;\n\t\t\tif (pokemon.hp > pokemon.maxhp / 2) {\n\t\t\t\tif (pokemon.species.forme !== 'Meteor') {\n\t\t\t\t\tpokemon.formeChange('Minior-Meteor');\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (pokemon.species.forme === 'Meteor') {\n\t\t\t\t\tpokemon.formeChange(pokemon.set.species);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (target.species.id !== 'miniormeteor' || target.transformed)\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Shields Down');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"onTryAddVolatile": "function (status, target) {\n\t\t\tif (target.species.id !== 'miniormeteor' || target.transformed)\n\t\t\t\treturn;\n\t\t\tif (status.id !== 'yawn')\n\t\t\t\treturn;\n\t\t\tthis.add('-immune', target, '[from] ability: Shields Down');\n\t\t\treturn null;\n\t\t}",
	"isPermanent": True,
	"name": "Shields Down",
	"rating": 3,
	"num": 197
  },
  "simple": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (effect && effect.id === 'zpower')\n\t\t\t\treturn;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tboost[i] *= 2;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Simple",
	"rating": 4,
	"num": 86
  },
  "skilllink": {
	"onModifyMove": "function (move) {\n\t\t\tif (move.multihit && Array.isArray(move.multihit) && move.multihit.length) {\n\t\t\t\tmove.multihit = move.multihit[1];\n\t\t\t}\n\t\t\tif (move.multiaccuracy) {\n\t\t\t\tdelete move.multiaccuracy;\n\t\t\t}\n\t\t}",
	"name": "Skill Link",
	"rating": 3,
	"num": 92
  },
  "slowstart": {
	"onStart": "function (pokemon) {\n\t\t\tpokemon.addVolatile('slowstart');\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tdelete pokemon.volatiles['slowstart'];\n\t\t\tthis.add('-end', pokemon, 'Slow Start', '[silent]');\n\t\t}",
	"condition": {
	  "duration": 5,
	  "onResidualOrder": 28,
	  "onResidualSubOrder": 2,
	  "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'ability: Slow Start');\n\t\t\t}",
	  "onModifyAtkPriority": 5,
	  "onModifyAtk": "function (atk, pokemon) {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}",
	  "onModifySpe": "function (spe, pokemon) {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}",
	  "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Slow Start');\n\t\t\t}"
	},
	"name": "Slow Start",
	"rating": -1,
	"num": 112
  },
  "slushrush": {
	"onModifySpe": "function (spe, pokemon) {\n\t\t\tif (this.field.isWeather('hail')) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Slush Rush",
	"rating": 3,
	"num": 202
  },
  "sniper": {
	"onModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.getMoveHitData(move).crit) {\n\t\t\t\tthis.debug('Sniper boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Sniper",
	"rating": 2,
	"num": 97
  },
  "snowcloak": {
	"onImmunity": "function (type, pokemon) {\n\t\t\tif (type === 'hail')\n\t\t\t\treturn False;\n\t\t}",
	"onModifyAccuracyPriority": -1,
	"onModifyAccuracy": "function (accuracy) {\n\t\t\tif (typeof accuracy !== 'number')\n\t\t\t\treturn;\n\t\t\tif (this.field.isWeather('hail')) {\n\t\t\t\tthis.debug('Snow Cloak - decreasing accuracy');\n\t\t\t\treturn this.chainModify([3277, 4096]);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Snow Cloak",
	"rating": 1.5,
	"num": 81
  },
  "snowwarning": {
	"onStart": "function (source) {\n\t\t\tthis.field.setWeather('hail');\n\t\t}",
	"name": "Snow Warning",
	"rating": 4,
	"num": 117
  },
  "solarpower": {
	"onModifySpAPriority": 5,
	"onModifySpA": "function (spa, pokemon) {\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onWeather": "function (target, source, effect) {\n\t\t\tif (target.hasItem('utilityumbrella'))\n\t\t\t\treturn;\n\t\t\tif (effect.id === 'sunnyday' || effect.id === 'desolateland') {\n\t\t\t\tthis.damage(target.baseMaxhp / 8, target, target);\n\t\t\t}\n\t\t}",
	"name": "Solar Power",
	"rating": 2,
	"num": 94
  },
  "solidrock": {
	"onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.getMoveHitData(move).typeMod > 0) {\n\t\t\t\tthis.debug('Solid Rock neutralize');\n\t\t\t\treturn this.chainModify(0.75);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Solid Rock",
	"rating": 3,
	"num": 116
  },
  "soulheart": {
	"onAnyFaintPriority": 1,
	"onAnyFaint": "function () {\n\t\t\tthis.boost({ spa: 1 }, this.effectState.target);\n\t\t}",
	"name": "Soul-Heart",
	"rating": 3.5,
	"num": 220
  },
  "soundproof": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.flags['sound']) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Soundproof');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAllyTryHitSide": "function (target, source, move) {\n\t\t\tif (move.flags['sound']) {\n\t\t\t\tthis.add('-immune', this.effectState.target, '[from] ability: Soundproof');\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Soundproof",
	"rating": 1.5,
	"num": 43
  },
  "speedboost": {
	"onResidualOrder": 28,
	"onResidualSubOrder": 2,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.activeTurns) {\n\t\t\t\tthis.boost({ spe: 1 });\n\t\t\t}\n\t\t}",
	"name": "Speed Boost",
	"rating": 4.5,
	"num": 3
  },
  "stakeout": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender) {\n\t\t\tif (!defender.activeTurns) {\n\t\t\t\tthis.debug('Stakeout boost');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender) {\n\t\t\tif (!defender.activeTurns) {\n\t\t\t\tthis.debug('Stakeout boost');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Stakeout",
	"rating": 4.5,
	"num": 198
  },
  "stall": {
	"onFractionalPriority": -0.1,
	"name": "Stall",
	"rating": -1,
	"num": 100
  },
  "stalwart": {
	"onModifyMovePriority": 1,
	"onModifyMove": "function (move) {\n\t\t\t// most of the implementation is in Battle#getTarget\n\t\t\tmove.tracksTarget = move.target !== 'scripted';\n\t\t}",
	"name": "Stalwart",
	"rating": 0,
	"num": 242
  },
  "stamina": {
	"onDamagingHit": "function (damage, target, source, effect) {\n\t\t\tthis.boost({ def: 1 });\n\t\t}",
	"name": "Stamina",
	"rating": 3.5,
	"num": 192
  },
  "stancechange": {
	"onModifyMovePriority": 1,
	"onModifyMove": "function (move, attacker, defender) {\n\t\t\tif (attacker.species.baseSpecies !== 'Aegislash' || attacker.transformed)\n\t\t\t\treturn;\n\t\t\tif (move.category === 'Status' && move.id !== 'kingsshield')\n\t\t\t\treturn;\n\t\t\tvar targetForme = (move.id === 'kingsshield' ? 'Aegislash' : 'Aegislash-Blade');\n\t\t\tif (attacker.species.name !== targetForme)\n\t\t\t\tattacker.formeChange(targetForme);\n\t\t}",
	"isPermanent": True,
	"name": "Stance Change",
	"rating": 4,
	"num": 176
  },
  "static": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\tif (this.randomChance(3, 10)) {\n\t\t\t\t\tsource.trySetStatus('par', target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
	"name": "Static",
	"rating": 2,
	"num": 9
  },
  "steadfast": {
	"onFlinch": "function (pokemon) {\n\t\t\tthis.boost({ spe: 1 });\n\t\t}",
	"name": "Steadfast",
	"rating": 1,
	"num": 80
  },
  "steamengine": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (['Water', 'Fire'].includes(move.type)) {\n\t\t\t\tthis.boost({ spe: 6 });\n\t\t\t}\n\t\t}",
	"name": "Steam Engine",
	"rating": 2,
	"num": 243
  },
  "steelworker": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Steel') {\n\t\t\t\tthis.debug('Steelworker boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Steel') {\n\t\t\t\tthis.debug('Steelworker boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Steelworker",
	"rating": 3.5,
	"num": 200
  },
  "steelyspirit": {
	"onAllyBasePowerPriority": 22,
	"onAllyBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.type === 'Steel') {\n\t\t\t\tthis.debug('Steely Spirit boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Steely Spirit",
	"rating": 3.5,
	"num": 252
  },
  "stench": {
	"onModifyMovePriority": -1,
	"onModifyMove": "function (move) {\n\t\t\tif (move.category !== \"Status\") {\n\t\t\t\tthis.debug('Adding Stench flinch');\n\t\t\t\tif (!move.secondaries)\n\t\t\t\t\tmove.secondaries = [];\n\t\t\t\tfor (var _i = 0, _a = move.secondaries; _i < _a.length; _i++) {\n\t\t\t\t\tvar secondary = _a[_i];\n\t\t\t\t\tif (secondary.volatileStatus === 'flinch')\n\t\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tmove.secondaries.push({\n\t\t\t\t\tchance: 10,\n\t\t\t\t\tvolatileStatus: 'flinch',\n\t\t\t\t});\n\t\t\t}\n\t\t}",
	"name": "Stench",
	"rating": 0.5,
	"num": 1
  },
  "stickyhold": {
	"onTakeItem": "function (item, pokemon, source) {\n\t\t\tif (!this.activeMove)\n\t\t\t\tthrow new Error(\"Battle.activeMove is null\");\n\t\t\tif (!pokemon.hp || pokemon.item === 'stickybarb')\n\t\t\t\treturn;\n\t\t\tif ((source && source !== pokemon) || this.activeMove.id === 'knockoff') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Sticky Hold');\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Sticky Hold",
	"rating": 2,
	"num": 60
  },
  "stormdrain": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Water') {\n\t\t\t\tif (!this.boost({ spa: 1 })) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Storm Drain');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAnyRedirectTarget": "function (target, source, source2, move) {\n\t\t\tif (move.type !== 'Water' || ['firepledge', 'grasspledge', 'waterpledge'].includes(move.id))\n\t\t\t\treturn;\n\t\t\tvar redirectTarget = ['randomNormal', 'adjacentFoe'].includes(move.target) ? 'normal' : move.target;\n\t\t\tif (this.validTarget(this.effectState.target, source, redirectTarget)) {\n\t\t\t\tif (move.smartTarget)\n\t\t\t\t\tmove.smartTarget = False;\n\t\t\t\tif (this.effectState.target !== target) {\n\t\t\t\t\tthis.add('-activate', this.effectState.target, 'ability: Storm Drain');\n\t\t\t\t}\n\t\t\t\treturn this.effectState.target;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Storm Drain",
	"rating": 3,
	"num": 114
  },
  "strongjaw": {
	"onBasePowerPriority": 19,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.flags['bite']) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Strong Jaw",
	"rating": 3,
	"num": 173
  },
  "sturdy": {
	"onTryHit": "function (pokemon, target, move) {\n\t\t\tif (move.ohko) {\n\t\t\t\tthis.add('-immune', pokemon, '[from] ability: Sturdy');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onDamagePriority": -30,
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (target.hp === target.maxhp && damage >= target.hp && effect && effect.effectType === 'Move') {\n\t\t\t\tthis.add('-ability', target, 'Sturdy');\n\t\t\t\treturn target.hp - 1;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Sturdy",
	"rating": 3,
	"num": 5
  },
  "suctioncups": {
	"onDragOutPriority": 1,
	"onDragOut": "function (pokemon) {\n\t\t\tthis.add('-activate', pokemon, 'ability: Suction Cups');\n\t\t\treturn null;\n\t\t}",
	"isBreakable": True,
	"name": "Suction Cups",
	"rating": 1,
	"num": 21
  },
  "superluck": {
	"onModifyCritRatio": "function (critRatio) {\n\t\t\treturn critRatio + 1;\n\t\t}",
	"name": "Super Luck",
	"rating": 1.5,
	"num": 105
  },
  "surgesurfer": {
	"onModifySpe": "function (spe) {\n\t\t\tif (this.field.isTerrain('electricterrain')) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Surge Surfer",
	"rating": 3,
	"num": 207
  },
  "swarm": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Bug' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Swarm boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Bug' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Swarm boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Swarm",
	"rating": 2,
	"num": 68
  },
  "sweetveil": {
	"name": "Sweet Veil",
	"onAllySetStatus": "function (status, target, source, effect) {\n\t\t\tif (status.id === 'slp') {\n\t\t\t\tthis.debug('Sweet Veil interrupts sleep');\n\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\tthis.add('-block', target, 'ability: Sweet Veil', '[of] ' + effectHolder);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"onAllyTryAddVolatile": "function (status, target) {\n\t\t\tif (status.id === 'yawn') {\n\t\t\t\tthis.debug('Sweet Veil blocking yawn');\n\t\t\t\tvar effectHolder = this.effectState.target;\n\t\t\t\tthis.add('-block', target, 'ability: Sweet Veil', '[of] ' + effectHolder);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"rating": 2,
	"num": 175
  },
  "swiftswim": {
	"onModifySpe": "function (spe, pokemon) {\n\t\t\tif (['raindance', 'primordialsea'].includes(pokemon.effectiveWeather())) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Swift Swim",
	"rating": 3,
	"num": 33
  },
  "symbiosis": {
	"onAllyAfterUseItem": "function (item, pokemon) {\n\t\t\tif (pokemon.switchFlag)\n\t\t\t\treturn;\n\t\t\tvar source = this.effectState.target;\n\t\t\tvar myItem = source.takeItem();\n\t\t\tif (!myItem)\n\t\t\t\treturn;\n\t\t\tif (!this.singleEvent('TakeItem', myItem, source.itemState, pokemon, source, this.effect, myItem) ||\n\t\t\t\t!pokemon.setItem(myItem)) {\n\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-activate', source, 'ability: Symbiosis', myItem, '[of] ' + pokemon);\n\t\t}",
	"name": "Symbiosis",
	"rating": 0,
	"num": 180
  },
  "synchronize": {
	"onAfterSetStatus": "function (status, target, source, effect) {\n\t\t\tif (!source || source === target)\n\t\t\t\treturn;\n\t\t\tif (effect && effect.id === 'toxicspikes')\n\t\t\t\treturn;\n\t\t\tif (status.id === 'slp' || status.id === 'frz')\n\t\t\t\treturn;\n\t\t\tthis.add('-activate', target, 'ability: Synchronize');\n\t\t\t// Hack to make status-prevention abilities think Synchronize is a status move\n\t\t\t// and show messages when activating against it.\n\t\t\tsource.trySetStatus(status, target, { status: status.id, id: 'synchronize' });\n\t\t}",
	"name": "Synchronize",
	"rating": 2,
	"num": 28
  },
  "tangledfeet": {
	"onModifyAccuracyPriority": -1,
	"onModifyAccuracy": "function (accuracy, target) {\n\t\t\tif (typeof accuracy !== 'number')\n\t\t\t\treturn;\n\t\t\tif (target === null || target === void 0 ? void 0 : target.volatiles['confusion']) {\n\t\t\t\tthis.debug('Tangled Feet - decreasing accuracy');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Tangled Feet",
	"rating": 1,
	"num": 77
  },
  "tanglinghair": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (this.checkMoveMakesContact(move, source, target, True)) {\n\t\t\t\tthis.add('-ability', target, 'Tangling Hair');\n\t\t\t\tthis.boost({ spe: -1 }, source, target, null, True);\n\t\t\t}\n\t\t}",
	"name": "Tangling Hair",
	"rating": 2,
	"num": 221
  },
  "technician": {
	"onBasePowerPriority": 30,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tvar basePowerAfterMultiplier = this.modify(basePower, this.event.modifier);\n\t\t\tthis.debug('Base Power: ' + basePowerAfterMultiplier);\n\t\t\tif (basePowerAfterMultiplier <= 60) {\n\t\t\t\tthis.debug('Technician boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Technician",
	"rating": 3.5,
	"num": 101
  },
  "telepathy": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && target.isAlly(source) && move.category !== 'Status') {\n\t\t\t\tthis.add('-activate', target, 'ability: Telepathy');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Telepathy",
	"rating": 0,
	"num": 140
  },
  "teravolt": {
	"onStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Teravolt');\n\t\t}",
	"onModifyMove": "function (move) {\n\t\t\tmove.ignoreAbility = True;\n\t\t}",
	"name": "Teravolt",
	"rating": 3.5,
	"num": 164
  },
  "thickfat": {
	"onSourceModifyAtkPriority": 6,
	"onSourceModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Ice' || move.type === 'Fire') {\n\t\t\t\tthis.debug('Thick Fat weaken');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onSourceModifySpAPriority": 5,
	"onSourceModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Ice' || move.type === 'Fire') {\n\t\t\t\tthis.debug('Thick Fat weaken');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Thick Fat",
	"rating": 3.5,
	"num": 47
  },
  "tintedlens": {
	"onModifyDamage": "function (damage, source, target, move) {\n\t\t\tif (target.getMoveHitData(move).typeMod < 0) {\n\t\t\t\tthis.debug('Tinted Lens boost');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"name": "Tinted Lens",
	"rating": 4,
	"num": 110
  },
  "torrent": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Water' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Torrent boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Water' && attacker.hp <= attacker.maxhp / 3) {\n\t\t\t\tthis.debug('Torrent boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Torrent",
	"rating": 2,
	"num": 67
  },
  "toughclaws": {
	"onBasePowerPriority": 21,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif (move.flags['contact']) {\n\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Tough Claws",
	"rating": 3.5,
	"num": 181
  },
  "toxicboost": {
	"onBasePowerPriority": 19,
	"onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\tif ((attacker.status === 'psn' || attacker.status === 'tox') && move.category === 'Physical') {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Toxic Boost",
	"rating": 2.5,
	"num": 137
  },
  "trace": {
	"onStart": "function (pokemon) {\n\t\t\t// n.b. only affects Hackmons\n\t\t\t// interaction with No Ability is complicated: https://www.smogon.com/forums/threads/pokemon-sun-moon-battle-mechanics-research.3586701/page-76#post-7790209\n\t\t\tif (pokemon.adjacentFoes().some(function (foeActive) { return foeActive.ability === 'noability'; })) {\n\t\t\t\tthis.effectState.gaveUp = True;\n\t\t\t}\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (!pokemon.isStarted || this.effectState.gaveUp)\n\t\t\t\treturn;\n\t\t\tvar additionalBannedAbilities = [\n\t\t\t\t// Zen Mode included here for compatability with Gen 5-6\n\t\t\t\t'noability', 'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'zenmode',\n\t\t\t];\n\t\t\tvar possibleTargets = pokemon.adjacentFoes().filter(function (target) { return (!target.getAbility().isPermanent && !additionalBannedAbilities.includes(target.ability)); });\n\t\t\tif (!possibleTargets.length)\n\t\t\t\treturn;\n\t\t\tvar target = this.sample(possibleTargets);\n\t\t\tvar ability = target.getAbility();\n\t\t\tthis.add('-ability', pokemon, ability, '[from] ability: Trace', '[of] ' + target);\n\t\t\tpokemon.setAbility(ability);\n\t\t}",
	"name": "Trace",
	"rating": 2.5,
	"num": 36
  },
  "transistor": {
	"onModifyAtkPriority": 5,
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Electric') {\n\t\t\t\tthis.debug('Transistor boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"onModifySpAPriority": 5,
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Electric') {\n\t\t\t\tthis.debug('Transistor boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
	"name": "Transistor",
	"rating": 3.5,
	"num": 262
  },
  "triage": {
	"onModifyPriority": "function (priority, pokemon, target, move) {\n\t\t\tif (move === null || move === void 0 ? void 0 : move.flags['heal'])\n\t\t\t\treturn priority + 3;\n\t\t}",
	"name": "Triage",
	"rating": 3.5,
	"num": 205
  },
  "truant": {
	"onStart": "function (pokemon) {\n\t\t\tpokemon.removeVolatile('truant');\n\t\t\tif (pokemon.activeTurns && (pokemon.moveThisTurnResult !== undefined || !this.queue.willMove(pokemon))) {\n\t\t\t\tpokemon.addVolatile('truant');\n\t\t\t}\n\t\t}",
	"onBeforeMovePriority": 9,
	"onBeforeMove": "function (pokemon) {\n\t\t\tif (pokemon.removeVolatile('truant')) {\n\t\t\t\tthis.add('cant', pokemon, 'ability: Truant');\n\t\t\t\treturn False;\n\t\t\t}\n\t\t\tpokemon.addVolatile('truant');\n\t\t}",
	"condition": {},
	"name": "Truant",
	"rating": -1,
	"num": 54
  },
  "turboblaze": {
	"onStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Turboblaze');\n\t\t}",
	"onModifyMove": "function (move) {\n\t\t\tmove.ignoreAbility = True;\n\t\t}",
	"name": "Turboblaze",
	"rating": 3.5,
	"num": 163
  },
  "unaware": {
	"name": "Unaware",
	"onAnyModifyBoost": "function (boosts, pokemon) {\n\t\t\tvar unawareUser = this.effectState.target;\n\t\t\tif (unawareUser === pokemon)\n\t\t\t\treturn;\n\t\t\tif (unawareUser === this.activePokemon && pokemon === this.activeTarget) {\n\t\t\t\tboosts['def'] = 0;\n\t\t\t\tboosts['spd'] = 0;\n\t\t\t\tboosts['evasion'] = 0;\n\t\t\t}\n\t\t\tif (pokemon === this.activePokemon && unawareUser === this.activeTarget) {\n\t\t\t\tboosts['atk'] = 0;\n\t\t\t\tboosts['def'] = 0;\n\t\t\t\tboosts['spa'] = 0;\n\t\t\t\tboosts['accuracy'] = 0;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"rating": 4,
	"num": 109
  },
  "unburden": {
	"onAfterUseItem": "function (item, pokemon) {\n\t\t\tif (pokemon !== this.effectState.target)\n\t\t\t\treturn;\n\t\t\tpokemon.addVolatile('unburden');\n\t\t}",
	"onTakeItem": "function (item, pokemon) {\n\t\t\tpokemon.addVolatile('unburden');\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tpokemon.removeVolatile('unburden');\n\t\t}",
	"condition": {
	  "onModifySpe": "function (spe, pokemon) {\n\t\t\t\tif (!pokemon.item && !pokemon.ignoringAbility()) {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
	},
	"name": "Unburden",
	"rating": 3.5,
	"num": 84
  },
  "unnerve": {
	"onPreStart": "function (pokemon) {\n\t\t\tthis.add('-ability', pokemon, 'Unnerve');\n\t\t\tthis.effectState.unnerved = True;\n\t\t}",
	"onStart": "function (pokemon) {\n\t\t\tif (this.effectState.unnerved)\n\t\t\t\treturn;\n\t\t\tthis.add('-ability', pokemon, 'Unnerve');\n\t\t\tthis.effectState.unnerved = True;\n\t\t}",
	"onEnd": "function () {\n\t\t\tthis.effectState.unnerved = False;\n\t\t}",
	"onFoeTryEatItem": "function () {\n\t\t\treturn !this.effectState.unnerved;\n\t\t}",
	"name": "Unnerve",
	"rating": 1.5,
	"num": 127
  },
  "unseenfist": {
	"onModifyMove": "function (move) {\n\t\t\tif (move.flags['contact'])\n\t\t\t\tdelete move.flags['protect'];\n\t\t}",
	"name": "Unseen Fist",
	"rating": 2,
	"num": 260
  },
  "victorystar": {
	"onAnyModifyAccuracyPriority": -1,
	"onAnyModifyAccuracy": "function (accuracy, target, source) {\n\t\t\tif (source.isAlly(this.effectState.target) && typeof accuracy === 'number') {\n\t\t\t\treturn this.chainModify([4506, 4096]);\n\t\t\t}\n\t\t}",
	"name": "Victory Star",
	"rating": 2,
	"num": 162
  },
  "vitalspirit": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'slp') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Vital Spirit');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'slp')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Vital Spirit');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Vital Spirit",
	"rating": 2,
	"num": 72
  },
  "voltabsorb": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Electric') {\n\t\t\t\tif (!this.heal(target.baseMaxhp / 4)) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Volt Absorb');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Volt Absorb",
	"rating": 3.5,
	"num": 10
  },
  "wanderingspirit": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tvar additionalBannedAbilities = ['hungerswitch', 'illusion', 'neutralizinggas', 'wonderguard'];\n\t\t\tif (source.getAbility().isPermanent || additionalBannedAbilities.includes(source.ability) ||\n\t\t\t\ttarget.volatiles['dynamax']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\tvar sourceAbility = source.setAbility('wanderingspirit', target);\n\t\t\t\tif (!sourceAbility)\n\t\t\t\t\treturn;\n\t\t\t\tif (target.isAlly(source)) {\n\t\t\t\t\tthis.add('-activate', target, 'Skill Swap', '', '', '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'ability: Wandering Spirit', this.dex.abilities.get(sourceAbility).name, 'Wandering Spirit', '[of] ' + source);\n\t\t\t\t}\n\t\t\t\ttarget.setAbility(sourceAbility);\n\t\t\t}\n\t\t}",
	"name": "Wandering Spirit",
	"rating": 2.5,
	"num": 254
  },
  "waterabsorb": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target !== source && move.type === 'Water') {\n\t\t\t\tif (!this.heal(target.baseMaxhp / 4)) {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Water Absorb');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Water Absorb",
	"rating": 3.5,
	"num": 11
  },
  "waterbubble": {
	"onSourceModifyAtkPriority": 5,
	"onSourceModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Fire') {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onSourceModifySpAPriority": 5,
	"onSourceModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Fire') {\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
	"onModifyAtk": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Water') {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"onModifySpA": "function (atk, attacker, defender, move) {\n\t\t\tif (move.type === 'Water') {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'brn') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Water Bubble');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'brn')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Water Bubble');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Water Bubble",
	"rating": 4.5,
	"num": 199
  },
  "watercompaction": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (move.type === 'Water') {\n\t\t\t\tthis.boost({ def: 2 });\n\t\t\t}\n\t\t}",
	"name": "Water Compaction",
	"rating": 1.5,
	"num": 195
  },
  "waterveil": {
	"onUpdate": "function (pokemon) {\n\t\t\tif (pokemon.status === 'brn') {\n\t\t\t\tthis.add('-activate', pokemon, 'ability: Water Veil');\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}\n\t\t}",
	"onSetStatus": "function (status, target, source, effect) {\n\t\t\tvar _a;\n\t\t\tif (status.id !== 'brn')\n\t\t\t\treturn;\n\t\t\tif ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Water Veil');\n\t\t\t}\n\t\t\treturn False;\n\t\t}",
	"isBreakable": True,
	"name": "Water Veil",
	"rating": 2,
	"num": 41
  },
  "weakarmor": {
	"onDamagingHit": "function (damage, target, source, move) {\n\t\t\tif (move.category === 'Physical') {\n\t\t\t\tthis.boost({ def: -1, spe: 2 }, target, target);\n\t\t\t}\n\t\t}",
	"name": "Weak Armor",
	"rating": 1,
	"num": 133
  },
  "whitesmoke": {
	"onBoost": "function (boost, target, source, effect) {\n\t\t\tif (source && target === source)\n\t\t\t\treturn;\n\t\t\tvar showMsg = False;\n\t\t\tvar i;\n\t\t\tfor (i in boost) {\n\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\tdelete boost[i];\n\t\t\t\t\tshowMsg = True;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (showMsg && !effect.secondaries && effect.id !== 'octolock') {\n\t\t\t\tthis.add(\"-fail\", target, \"unboost\", \"[from] ability: White Smoke\", \"[of] \" + target);\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "White Smoke",
	"rating": 2,
	"num": 73
  },
  "wimpout": {
	"onEmergencyExit": "function (target) {\n\t\t\tif (!this.canSwitch(target.side) || target.forceSwitchFlag || target.switchFlag)\n\t\t\t\treturn;\n\t\t\tfor (var _i = 0, _a = this.sides; _i < _a.length; _i++) {\n\t\t\t\tvar side = _a[_i];\n\t\t\t\tfor (var _b = 0, _c = side.active; _b < _c.length; _b++) {\n\t\t\t\t\tvar active = _c[_b];\n\t\t\t\t\tactive.switchFlag = False;\n\t\t\t\t}\n\t\t\t}\n\t\t\ttarget.switchFlag = True;\n\t\t\tthis.add('-activate', target, 'ability: Wimp Out');\n\t\t}",
	"name": "Wimp Out",
	"rating": 1,
	"num": 193
  },
  "wonderguard": {
	"onTryHit": "function (target, source, move) {\n\t\t\tif (target === source || move.category === 'Status' || move.type === '???' || move.id === 'struggle')\n\t\t\t\treturn;\n\t\t\tif (move.id === 'skydrop' && !source.volatiles['skydrop'])\n\t\t\t\treturn;\n\t\t\tthis.debug('Wonder Guard immunity: ' + move.id);\n\t\t\tif (target.runEffectiveness(move) <= 0) {\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = False;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-immune', target, '[from] ability: Wonder Guard');\n\t\t\t\t}\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Wonder Guard",
	"rating": 5,
	"num": 25
  },
  "wonderskin": {
	"onModifyAccuracyPriority": 10,
	"onModifyAccuracy": "function (accuracy, target, source, move) {\n\t\t\tif (move.category === 'Status' && typeof accuracy === 'number') {\n\t\t\t\tthis.debug('Wonder Skin - setting accuracy to 50');\n\t\t\t\treturn 50;\n\t\t\t}\n\t\t}",
	"isBreakable": True,
	"name": "Wonder Skin",
	"rating": 2,
	"num": 147
  },
  "zenmode": {
	"onResidualOrder": 29,
	"onResidual": "function (pokemon) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies !== 'Darmanitan' || pokemon.transformed) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (pokemon.hp <= pokemon.maxhp / 2 && !['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {\n\t\t\t\tpokemon.addVolatile('zenmode');\n\t\t\t}\n\t\t\telse if (pokemon.hp > pokemon.maxhp / 2 && ['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {\n\t\t\t\tpokemon.addVolatile('zenmode'); // in case of base Darmanitan-Zen\n\t\t\t\tpokemon.removeVolatile('zenmode');\n\t\t\t}\n\t\t}",
	"onEnd": "function (pokemon) {\n\t\t\tif (!pokemon.volatiles['zenmode'] || !pokemon.hp)\n\t\t\t\treturn;\n\t\t\tpokemon.transformed = False;\n\t\t\tdelete pokemon.volatiles['zenmode'];\n\t\t\tif (pokemon.species.baseSpecies === 'Darmanitan' && pokemon.species.battleOnly) {\n\t\t\t\tpokemon.formeChange(pokemon.species.battleOnly, this.effect, False, '[silent]');\n\t\t\t}\n\t\t}",
	"condition": {
	  "onStart": "function (pokemon) {\n\t\t\t\tif (!pokemon.species.name.includes('Galar')) {\n\t\t\t\t\tif (pokemon.species.id !== 'darmanitanzen')\n\t\t\t\t\t\tpokemon.formeChange('Darmanitan-Zen');\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tif (pokemon.species.id !== 'darmanitangalarzen')\n\t\t\t\t\t\tpokemon.formeChange('Darmanitan-Galar-Zen');\n\t\t\t\t}\n\t\t\t}",
	  "onEnd": "function (pokemon) {\n\t\t\t\tif (['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {\n\t\t\t\t\tpokemon.formeChange(pokemon.species.battleOnly);\n\t\t\t\t}\n\t\t\t}"
	},
	"isPermanent": True,
	"name": "Zen Mode",
	"rating": 0,
	"num": 161
  },
  "mountaineer": {
	"onDamage": "function (damage, target, source, effect) {\n\t\t\tif (effect && effect.id === 'stealthrock') {\n\t\t\t\treturn False;\n\t\t\t}\n\t\t}",
	"onTryHit": "function (target, source, move) {\n\t\t\tif (move.type === 'Rock' && !target.activeTurns) {\n\t\t\t\tthis.add('-immune', target, '[from] ability: Mountaineer');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
	"isNonstandard": "CAP",
	"isBreakable": True,
	"name": "Mountaineer",
	"rating": 3,
	"num": -2
  },
  "rebound": {
	"isNonstandard": "CAP",
	"name": "Rebound",
	"onTryHitPriority": 1,
	"onTryHit": "function (target, source, move) {\n\t\t\tif (this.effectState.target.activeTurns)\n\t\t\t\treturn;\n\t\t\tif (target === source || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\tnewMove.hasBounced = True;\n\t\t\tthis.actions.useMove(newMove, target, source);\n\t\t\treturn null;\n\t\t}",
	"onAllyTryHitSide": "function (target, source, move) {\n\t\t\tif (this.effectState.target.activeTurns)\n\t\t\t\treturn;\n\t\t\tif (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\tnewMove.hasBounced = True;\n\t\t\tthis.actions.useMove(newMove, this.effectState.target, source);\n\t\t\treturn null;\n\t\t}",
	"condition": {
	  "duration": 1
	},
	"isBreakable": True,
	"rating": 3,
	"num": -3
  },
  "persistent": {
	"isNonstandard": "CAP",
	"name": "Persistent",
	"rating": 3,
	"num": -4
  }
}