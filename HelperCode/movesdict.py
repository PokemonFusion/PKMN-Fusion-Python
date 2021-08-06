BattleMovedex = {
  "10000000voltthunderbolt": {
    "num": 719,
    "accuracy": true,
    "basePower": 195,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "10,000,000 Volt Thunderbolt",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "pikashuniumz",
    "critRatio": 3,
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "absorb": {
    "num": 71,
    "accuracy": 100,
    "basePower": 20,
    "category": "Special",
    "name": "Absorb",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Clever"
  },
  "accelerock": {
    "num": 709,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Accelerock",
    "pp": 20,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Cool"
  },
  "acid": {
    "num": 51,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Acid",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Poison",
    "contestType": "Clever"
  },
  "acidarmor": {
    "num": 151,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Acid Armor",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Poison",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "aciddownpour": {
    "num": 628,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Acid Downpour",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "poisoniumz",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "contestType": "Cool"
  },
  "acidspray": {
    "num": 491,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Acid Spray",
    "pp": 20,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spd": -2
      }
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Beautiful"
  },
  "acrobatics": {
    "num": 512,
    "accuracy": 100,
    "basePower": 55,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (!pokemon.item) {\n\t\t\t\tthis.debug(\"Power doubled for no item\");\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Acrobatics",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "acupressure": {
    "num": 367,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Acupressure",
    "pp": 30,
    "priority": 0,
    "flags": {},
    "onHit": "function (target) {\n\t\t\tvar stats = [];\n\t\t\tvar stat;\n\t\t\tfor (stat in target.boosts) {\n\t\t\t\tif (target.boosts[stat] < 6) {\n\t\t\t\t\tstats.push(stat);\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (stats.length) {\n\t\t\t\tvar randomStat = this.sample(stats);\n\t\t\t\tvar boost = {};\n\t\t\t\tboost[randomStat] = 2;\n\t\t\t\tthis.boost(boost);\n\t\t\t}\n\t\t\telse {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "adjacentAllyOrSelf",
    "type": "Normal",
    "zMove": {
      "effect": "crit2"
    },
    "contestType": "Tough"
  },
  "aerialace": {
    "num": 332,
    "accuracy": true,
    "basePower": 60,
    "category": "Physical",
    "name": "Aerial Ace",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "aeroblast": {
    "num": 177,
    "accuracy": 95,
    "basePower": 100,
    "category": "Special",
    "name": "Aeroblast",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "afteryou": {
    "num": 495,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "After You",
    "pp": 15,
    "priority": 0,
    "flags": {
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.side.active.length < 2)\n\t\t\t\treturn false; // fails in singles\n\t\t\tvar action = this.queue.willMove(target);\n\t\t\tif (action) {\n\t\t\t\tthis.queue.prioritizeAction(action);\n\t\t\t\tthis.add('-activate', target, 'move: After You');\n\t\t\t}\n\t\t\telse {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "agility": {
    "num": 97,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Agility",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spe": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cool"
  },
  "aircutter": {
    "num": 314,
    "accuracy": 95,
    "basePower": 60,
    "category": "Special",
    "name": "Air Cutter",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Flying",
    "contestType": "Cool"
  },
  "airslash": {
    "num": 403,
    "accuracy": 95,
    "basePower": 75,
    "category": "Special",
    "name": "Air Slash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "alloutpummeling": {
    "num": 624,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "All-Out Pummeling",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "fightiniumz",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "allyswitch": {
    "num": 502,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Ally Switch",
    "pp": 15,
    "priority": 2,
    "flags": {},
    "onTryHit": "function (source) {\n\t\t\tif (source.side.active.length === 1)\n\t\t\t\treturn false;\n\t\t\tif (source.side.active.length === 3 && source.position === 1)\n\t\t\t\treturn false;\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tvar newPosition = (pokemon.position === 0 ? pokemon.side.active.length - 1 : 0);\n\t\t\tif (!pokemon.side.active[newPosition])\n\t\t\t\treturn false;\n\t\t\tif (pokemon.side.active[newPosition].fainted)\n\t\t\t\treturn false;\n\t\t\tthis.swapPosition(pokemon, newPosition, '[from] move: Ally Switch');\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "amnesia": {
    "num": 133,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Amnesia",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spd": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "anchorshot": {
    "num": 677,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Anchor Shot",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "onHit": "function (target, source, move) {\n\t\t\t\tif (source.isActive)\n\t\t\t\t\ttarget.addVolatile('trapped', source, move, 'trapper');\n\t\t\t}"
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Tough"
  },
  "ancientpower": {
    "num": 246,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "name": "Ancient Power",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "self": {
        "boosts": {
          "atk": 1,
          "def": 1,
          "spa": 1,
          "spd": 1,
          "spe": 1
        }
      }
    },
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "appleacid": {
    "num": 787,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Apple Acid",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Grass"
  },
  "aquajet": {
    "num": 453,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Aqua Jet",
    "pp": 20,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "aquaring": {
    "num": 392,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Aqua Ring",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "aquaring",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Aqua Ring');\n\t\t\t}",
      "onResidualOrder": 6,
      "onResidual": "function (pokemon) {\n\t\t\t\tthis.heal(pokemon.baseMaxhp / 16);\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Water",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Beautiful"
  },
  "aquatail": {
    "num": 401,
    "accuracy": 90,
    "basePower": 90,
    "category": "Physical",
    "name": "Aqua Tail",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "armthrust": {
    "num": 292,
    "accuracy": 100,
    "basePower": 15,
    "category": "Physical",
    "name": "Arm Thrust",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "aromatherapy": {
    "num": 312,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Aromatherapy",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "distance": 1
    },
    "onHit": "function (pokemon, source, move) {\n\t\t\tthis.add('-activate', source, 'move: Aromatherapy');\n\t\t\tvar success = false;\n\t\t\tfor (var _i = 0, _a = pokemon.side.pokemon; _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tif (ally !== source && ((ally.hasAbility('sapsipper')) ||\n\t\t\t\t\t(ally.volatiles['substitute'] && !move.infiltrates))) {\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (ally.cureStatus())\n\t\t\t\t\tsuccess = true;\n\t\t\t}\n\t\t\treturn success;\n\t\t}",
    "target": "allyTeam",
    "type": "Grass",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Clever"
  },
  "aromaticmist": {
    "num": 597,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Aromatic Mist",
    "pp": 20,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "boosts": {
      "spd": 1
    },
    "secondary": null,
    "target": "adjacentAlly",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "spd": 2
      }
    },
    "contestType": "Beautiful"
  },
  "assist": {
    "num": 274,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Assist",
    "pp": 20,
    "priority": 0,
    "flags": {},
    "onHit": "function (target) {\n\t\t\tvar noAssist = [\n\t\t\t\t'assist', 'banefulbunker', 'beakblast', 'belch', 'bestow', 'bounce', 'celebrate', 'chatter', 'circlethrow', 'copycat', 'counter', 'covet', 'destinybond', 'detect', 'dig', 'dive', 'dragontail', 'endure', 'feint', 'fly', 'focuspunch', 'followme', 'helpinghand', 'holdhands', 'kingsshield', 'matblock', 'mefirst', 'metronome', 'mimic', 'mirrorcoat', 'mirrormove', 'naturepower', 'phantomforce', 'protect', 'ragepowder', 'roar', 'shadowforce', 'shelltrap', 'sketch', 'skydrop', 'sleeptalk', 'snatch', 'spikyshield', 'spotlight', 'struggle', 'switcheroo', 'thief', 'transform', 'trick', 'whirlwind',\n\t\t\t];\n\t\t\tvar moves = [];\n\t\t\tfor (var _i = 0, _a = target.side.pokemon; _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (pokemon === target)\n\t\t\t\t\tcontinue;\n\t\t\t\tfor (var _b = 0, _c = pokemon.moveSlots; _b < _c.length; _b++) {\n\t\t\t\t\tvar moveSlot = _c[_b];\n\t\t\t\t\tvar moveid = moveSlot.id;\n\t\t\t\t\tif (noAssist.includes(moveid))\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tvar move = this.dex.moves.get(moveid);\n\t\t\t\t\tif (move.isZ || move.isMax) {\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\t}\n\t\t\t\t\tmoves.push(moveid);\n\t\t\t\t}\n\t\t\t}\n\t\t\tvar randomMove = '';\n\t\t\tif (moves.length)\n\t\t\t\trandomMove = this.sample(moves);\n\t\t\tif (!randomMove) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.actions.useMove(randomMove, target);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "contestType": "Cute"
  },
  "assurance": {
    "num": 372,
    "accuracy": 100,
    "basePower": 60,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.hurtThisTurn) {\n\t\t\t\tthis.debug('Boosted for being damaged this turn');\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Assurance",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "astonish": {
    "num": 310,
    "accuracy": 100,
    "basePower": 30,
    "category": "Physical",
    "name": "Astonish",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cute"
  },
  "astralbarrage": {
    "num": 825,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "name": "Astral Barrage",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Ghost"
  },
  "attackorder": {
    "num": 454,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Attack Order",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Clever"
  },
  "attract": {
    "num": 213,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Attract",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "attract",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon, source, effect) {\n\t\t\t\tif (!(pokemon.gender === 'M' && source.gender === 'F') && !(pokemon.gender === 'F' && source.gender === 'M')) {\n\t\t\t\t\tthis.debug('incompatible gender');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tif (!this.runEvent('Attract', pokemon, source)) {\n\t\t\t\t\tthis.debug('Attract event failed');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tif (effect.id === 'cutecharm') {\n\t\t\t\t\tthis.add('-start', pokemon, 'Attract', '[from] ability: Cute Charm', '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse if (effect.id === 'destinyknot') {\n\t\t\t\t\tthis.add('-start', pokemon, 'Attract', '[from] item: Destiny Knot', '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-start', pokemon, 'Attract');\n\t\t\t\t}\n\t\t\t}",
      "onUpdate": "function (pokemon) {\n\t\t\t\tif (this.effectState.source && !this.effectState.source.isActive && pokemon.volatiles['attract']) {\n\t\t\t\t\tthis.debug('Removing Attract volatile on ' + pokemon);\n\t\t\t\t\tpokemon.removeVolatile('attract');\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 2,
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tthis.add('-activate', pokemon, 'move: Attract', '[of] ' + this.effectState.source);\n\t\t\t\tif (this.randomChance(1, 2)) {\n\t\t\t\t\tthis.add('cant', pokemon, 'Attract');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'Attract', '[silent]');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "aurasphere": {
    "num": 396,
    "accuracy": true,
    "basePower": 80,
    "category": "Special",
    "name": "Aura Sphere",
    "pp": 20,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "pulse": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Fighting",
    "contestType": "Beautiful"
  },
  "aurawheel": {
    "num": 783,
    "accuracy": 100,
    "basePower": 110,
    "category": "Physical",
    "name": "Aura Wheel",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "self": {
        "boosts": {
          "spe": 1
        }
      }
    },
    "onTry": "function (source) {\n\t\t\tif (source.species.baseSpecies === 'Morpeko') {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.attrLastMove('[still]');\n\t\t\tthis.add('-fail', source, 'move: Aura Wheel');\n\t\t\tthis.hint(\"Only a Pokemon whose form is Morpeko or Morpeko-Hangry can use this move.\");\n\t\t\treturn null;\n\t\t}",
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (pokemon.species.name === 'Morpeko-Hangry') {\n\t\t\t\tmove.type = 'Dark';\n\t\t\t}\n\t\t\telse {\n\t\t\t\tmove.type = 'Electric';\n\t\t\t}\n\t\t}",
    "target": "normal",
    "type": "Electric"
  },
  "aurorabeam": {
    "num": 62,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Aurora Beam",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "atk": -1
      }
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "auroraveil": {
    "num": 694,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Aurora Veil",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "auroraveil",
    "onTry": "function () {\n\t\t\treturn this.field.isWeather('hail');\n\t\t}",
    "condition": {
      "duration": 5,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('lightclay')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onAnyModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (target !== source && this.effectState.target.hasAlly(target)) {\n\t\t\t\t\tif ((target.side.getSideCondition('reflect') && this.getCategory(move) === 'Physical') ||\n\t\t\t\t\t\t(target.side.getSideCondition('lightscreen') && this.getCategory(move) === 'Special')) {\n\t\t\t\t\t\treturn;\n\t\t\t\t\t}\n\t\t\t\t\tif (!target.getMoveHitData(move).crit && !move.infiltrates) {\n\t\t\t\t\t\tthis.debug('Aurora Veil weaken');\n\t\t\t\t\t\tif (this.activePerHalf > 1)\n\t\t\t\t\t\t\treturn this.chainModify([2732, 4096]);\n\t\t\t\t\t\treturn this.chainModify(0.5);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Aurora Veil');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 10,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'move: Aurora Veil');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Ice",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "autotomize": {
    "num": 475,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Autotomize",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onTryHit": "function (pokemon) {\n\t\t\tvar hasContrary = pokemon.hasAbility('contrary');\n\t\t\tif ((!hasContrary && pokemon.boosts.spe === 6) || (hasContrary && pokemon.boosts.spe === -6)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "boosts": {
      "spe": 2
    },
    "onHit": "function (pokemon) {\n\t\t\tif (pokemon.weighthg > 1) {\n\t\t\t\tpokemon.weighthg = Math.max(1, pokemon.weighthg - 1000);\n\t\t\t\tthis.add('-start', pokemon, 'Autotomize');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Steel",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "avalanche": {
    "num": 419,
    "accuracy": 100,
    "basePower": 60,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tvar damagedByTarget = pokemon.attackedBy.some(function (p) { return p.source === target && p.damage > 0 && p.thisTurn; });\n\t\t\tif (damagedByTarget) {\n\t\t\t\tthis.debug('Boosted for getting hit by ' + target);\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Avalanche",
    "pp": 10,
    "priority": -4,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "babydolleyes": {
    "num": 608,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Baby-Doll Eyes",
    "pp": 30,
    "priority": 1,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "boosts": {
      "atk": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "baddybad": {
    "num": 737,
    "accuracy": 95,
    "basePower": 80,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Baddy Bad",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "self": {
      "sideCondition": "reflect"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "banefulbunker": {
    "num": 661,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Baneful Bunker",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "banefulbunker",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Protect');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect']) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Protect');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tsource.trySetStatus('psn', target);\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tsource.trySetStatus('psn', target);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "barrage": {
    "num": 140,
    "accuracy": 85,
    "basePower": 15,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Barrage",
    "pp": 20,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "barrier": {
    "num": 112,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Barrier",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cool"
  },
  "batonpass": {
    "num": 226,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Baton Pass",
    "pp": 40,
    "priority": 0,
    "flags": {},
    "self": {
      "onHit": "function (source) {\n\t\t\t\tsource.skipBeforeSwitchOutEventFlag = true;\n\t\t\t}"
    },
    "selfSwitch": "copyvolatile",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "beakblast": {
    "num": 690,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Beak Blast",
    "pp": 15,
    "priority": -3,
    "flags": {
      "bullet": 1,
      "protect": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tpokemon.addVolatile('beakblast');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'move: Beak Blast');\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tsource.trySetStatus('brn', target);\n\t\t\t\t}\n\t\t\t}"
    },
    "onAfterMove": "function (pokemon) {\n\t\t\tpokemon.removeVolatile('beakblast');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "contestType": "Tough"
  },
  "beatup": {
    "num": 251,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn 5 + Math.floor(move.allies.shift().species.baseStats.atk / 10);\n\t\t}",
    "category": "Physical",
    "name": "Beat Up",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onModifyMove": "function (move, pokemon) {\n\t\t\tmove.allies = pokemon.side.pokemon.filter(function (ally) { return ally === pokemon || !ally.fainted && !ally.status; });\n\t\t\tmove.multihit = move.allies.length;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "behemothbash": {
    "num": 782,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Behemoth Bash",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel"
  },
  "behemothblade": {
    "num": 781,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Behemoth Blade",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel"
  },
  "belch": {
    "num": 562,
    "accuracy": 90,
    "basePower": 120,
    "category": "Special",
    "name": "Belch",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "bellydrum": {
    "num": 187,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Belly Drum",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.hp <= target.maxhp / 2 || target.boosts.atk >= 6 || target.maxhp === 1) { // Shedinja clause\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.directDamage(target.maxhp / 2);\n\t\t\tthis.boost({ atk: 12 }, target);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Cute"
  },
  "bestow": {
    "num": 516,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Bestow",
    "pp": 15,
    "priority": 0,
    "flags": {
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tif (target.item) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tvar myItem = source.takeItem();\n\t\t\tif (!myItem)\n\t\t\t\treturn false;\n\t\t\tif (!this.singleEvent('TakeItem', myItem, source.itemState, target, source, move, myItem) || !target.setItem(myItem)) {\n\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.add('-item', target, myItem.name, '[from] move: Bestow', '[of] ' + source);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Cute"
  },
  "bide": {
    "num": 117,
    "accuracy": true,
    "basePower": 0,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Bide",
    "pp": 10,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1
    },
    "volatileStatus": "bide",
    "ignoreImmunity": true,
    "beforeMoveCallback": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['bide'])\n\t\t\t\treturn true;\n\t\t}",
    "condition": {
      "duration": 3,
      "onLockMove": "bide",
      "onStart": "function (pokemon) {\n\t\t\t\tthis.effectState.totalDamage = 0;\n\t\t\t\tthis.add('-start', pokemon, 'move: Bide');\n\t\t\t}",
      "onDamagePriority": -101,
      "onDamage": "function (damage, target, source, move) {\n\t\t\t\tif (!move || move.effectType !== 'Move' || !source)\n\t\t\t\t\treturn;\n\t\t\t\tthis.effectState.totalDamage += damage;\n\t\t\t\tthis.effectState.lastDamageSource = source;\n\t\t\t}",
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tif (this.effectState.duration === 1) {\n\t\t\t\t\tthis.add('-end', pokemon, 'move: Bide');\n\t\t\t\t\ttarget = this.effectState.lastDamageSource;\n\t\t\t\t\tif (!target || !this.effectState.totalDamage) {\n\t\t\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\t\t\tthis.add('-fail', pokemon);\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t\tif (!target.isActive) {\n\t\t\t\t\t\tvar possibleTarget = this.getRandomTarget(pokemon, this.dex.moves.get('pound'));\n\t\t\t\t\t\tif (!possibleTarget) {\n\t\t\t\t\t\t\tthis.add('-miss', pokemon);\n\t\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t}\n\t\t\t\t\t\ttarget = possibleTarget;\n\t\t\t\t\t}\n\t\t\t\t\tvar moveData = {\n\t\t\t\t\t\tid: 'bide',\n\t\t\t\t\t\tname: \"Bide\",\n\t\t\t\t\t\taccuracy: true,\n\t\t\t\t\t\tdamage: this.effectState.totalDamage * 2,\n\t\t\t\t\t\tcategory: \"Physical\",\n\t\t\t\t\t\tpriority: 1,\n\t\t\t\t\t\tflags: { contact: 1, protect: 1 },\n\t\t\t\t\t\teffectType: 'Move',\n\t\t\t\t\t\ttype: 'Normal',\n\t\t\t\t\t};\n\t\t\t\t\tthis.actions.tryMoveHit(target, pokemon, moveData);\n\t\t\t\t\tpokemon.removeVolatile('bide');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tthis.add('-activate', pokemon, 'move: Bide');\n\t\t\t}",
      "onMoveAborted": "function (pokemon) {\n\t\t\t\tpokemon.removeVolatile('bide');\n\t\t\t}",
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'move: Bide', '[silent]');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "contestType": "Tough"
  },
  "bind": {
    "num": 20,
    "accuracy": 85,
    "basePower": 15,
    "category": "Physical",
    "name": "Bind",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "bite": {
    "num": 44,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Bite",
    "pp": 25,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Dark",
    "contestType": "Tough"
  },
  "blackholeeclipse": {
    "num": 654,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Black Hole Eclipse",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "darkiniumz",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Cool"
  },
  "blastburn": {
    "num": 307,
    "accuracy": 90,
    "basePower": 150,
    "category": "Special",
    "name": "Blast Burn",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "blazekick": {
    "num": 299,
    "accuracy": 90,
    "basePower": 85,
    "category": "Physical",
    "name": "Blaze Kick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Cool"
  },
  "blizzard": {
    "num": 59,
    "accuracy": 70,
    "basePower": 110,
    "category": "Special",
    "name": "Blizzard",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyMove": "function (move) {\n\t\t\tif (this.field.isWeather('hail'))\n\t\t\t\tmove.accuracy = true;\n\t\t}",
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "allAdjacentFoes",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "block": {
    "num": 335,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Block",
    "pp": 5,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\treturn target.addVolatile('trapped', source, move, 'trapper');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "bloomdoom": {
    "num": 644,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Bloom Doom",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "grassiumz",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "blueflare": {
    "num": 551,
    "accuracy": 85,
    "basePower": 130,
    "category": "Special",
    "name": "Blue Flare",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "bodypress": {
    "num": 776,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Body Press",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "useSourceDefensiveAsOffensive": true,
    "secondary": null,
    "target": "normal",
    "type": "Fighting"
  },
  "bodyslam": {
    "num": 34,
    "accuracy": 100,
    "basePower": 85,
    "category": "Physical",
    "name": "Body Slam",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "boltbeak": {
    "num": 754,
    "accuracy": 100,
    "basePower": 85,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.newlySwitched || this.queue.willMove(target)) {\n\t\t\t\tthis.debug('Bolt Beak damage boost');\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\tthis.debug('Bolt Beak NOT boosted');\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Bolt Beak",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric"
  },
  "boltstrike": {
    "num": 550,
    "accuracy": 85,
    "basePower": 130,
    "category": "Physical",
    "name": "Bolt Strike",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Beautiful"
  },
  "boneclub": {
    "num": 125,
    "accuracy": 85,
    "basePower": 65,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Bone Club",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "bonemerang": {
    "num": 155,
    "accuracy": 90,
    "basePower": 50,
    "category": "Physical",
    "name": "Bonemerang",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "bonerush": {
    "num": 198,
    "accuracy": 90,
    "basePower": 25,
    "category": "Physical",
    "name": "Bone Rush",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "boomburst": {
    "num": 586,
    "accuracy": 100,
    "basePower": 140,
    "category": "Special",
    "name": "Boomburst",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": null,
    "target": "allAdjacent",
    "type": "Normal",
    "contestType": "Tough"
  },
  "bounce": {
    "num": 340,
    "accuracy": 85,
    "basePower": 85,
    "category": "Physical",
    "name": "Bounce",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1,
      "distance": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onInvulnerability": "function (target, source, move) {\n\t\t\t\tif (['gust', 'twister', 'skyuppercut', 'thunder', 'hurricane', 'smackdown', 'thousandarrows'].includes(move.id)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onSourceBasePower": "function (basePower, target, source, move) {\n\t\t\t\tif (move.id === 'gust' || move.id === 'twister') {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Cute"
  },
  "bouncybubble": {
    "num": 733,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Bouncy Bubble",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Clever"
  },
  "branchpoke": {
    "num": 785,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Branch Poke",
    "pp": 40,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass"
  },
  "bravebird": {
    "num": 413,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Brave Bird",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "recoil": [
      33,
      100
    ],
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "breakingswipe": {
    "num": 784,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Breaking Swipe",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "atk": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Dragon"
  },
  "breakneckblitz": {
    "num": 622,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Breakneck Blitz",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "normaliumz",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "brickbreak": {
    "num": 280,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Brick Break",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (pokemon) {\n\t\t\t// will shatter screens through sub, before you hit\n\t\t\tpokemon.side.removeSideCondition('reflect');\n\t\t\tpokemon.side.removeSideCondition('lightscreen');\n\t\t\tpokemon.side.removeSideCondition('auroraveil');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "brine": {
    "num": 362,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Brine",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon, target) {\n\t\t\tif (target.hp * 2 <= target.maxhp) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "brutalswing": {
    "num": 693,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Brutal Swing",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacent",
    "type": "Dark",
    "contestType": "Tough"
  },
  "bubble": {
    "num": 145,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Bubble",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spe": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Water",
    "contestType": "Cute"
  },
  "bubblebeam": {
    "num": 61,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Bubble Beam",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "bugbite": {
    "num": 450,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Bug Bite",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar item = target.getItem();\n\t\t\tif (source.hp && item.isBerry && target.takeItem(source)) {\n\t\t\t\tthis.add('-enditem', target, item.name, '[from] stealeat', '[move] Bug Bite', '[of] ' + source);\n\t\t\t\tif (this.singleEvent('Eat', item, null, source, null, null)) {\n\t\t\t\t\tthis.runEvent('EatItem', source, null, null, item);\n\t\t\t\t\tif (item.id === 'leppaberry')\n\t\t\t\t\t\ttarget.staleness = 'external';\n\t\t\t\t}\n\t\t\t\tif (item.onEat)\n\t\t\t\t\tsource.ateBerry = true;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "bugbuzz": {
    "num": 405,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Bug Buzz",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Bug",
    "contestType": "Beautiful"
  },
  "bulkup": {
    "num": 339,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Bulk Up",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1,
      "def": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Fighting",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cool"
  },
  "bulldoze": {
    "num": 523,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Bulldoze",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "allAdjacent",
    "type": "Ground",
    "contestType": "Tough"
  },
  "bulletpunch": {
    "num": 418,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Bullet Punch",
    "pp": 30,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Tough"
  },
  "bulletseed": {
    "num": 331,
    "accuracy": 100,
    "basePower": 25,
    "category": "Physical",
    "name": "Bullet Seed",
    "pp": 30,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "burningjealousy": {
    "num": 807,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Burning Jealousy",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "onHit": "function (target, source, move) {\n\t\t\t\tif (target === null || target === void 0 ? void 0 : target.statsRaisedThisTurn) {\n\t\t\t\t\ttarget.trySetStatus('brn', source, move);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "allAdjacentFoes",
    "type": "Fire",
    "contestType": "Tough"
  },
  "burnup": {
    "num": 682,
    "accuracy": 100,
    "basePower": 130,
    "category": "Special",
    "name": "Burn Up",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "onTryMove": "function (pokemon, target, move) {\n\t\t\tif (pokemon.hasType('Fire'))\n\t\t\t\treturn;\n\t\t\tthis.add('-fail', pokemon, 'move: Burn Up');\n\t\t\tthis.attrLastMove('[still]');\n\t\t\treturn null;\n\t\t}",
    "self": {
      "onHit": "function (pokemon) {\n\t\t\t\tpokemon.setType(pokemon.getTypes(true).map(function (type) { return type === \"Fire\" ? \"???\" : type; }));\n\t\t\t\tthis.add('-start', pokemon, 'typechange', pokemon.types.join('/'), '[from] move: Burn Up');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Clever"
  },
  "buzzybuzz": {
    "num": 734,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Buzzy Buzz",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "secondary": {
      "chance": 100,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Clever"
  },
  "calmmind": {
    "num": 347,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Calm Mind",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spa": 1,
      "spd": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "camouflage": {
    "num": 293,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Camouflage",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onHit": "function (target) {\n\t\t\tvar newType = 'Normal';\n\t\t\tif (this.field.isTerrain('electricterrain')) {\n\t\t\t\tnewType = 'Electric';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('grassyterrain')) {\n\t\t\t\tnewType = 'Grass';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('mistyterrain')) {\n\t\t\t\tnewType = 'Fairy';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('psychicterrain')) {\n\t\t\t\tnewType = 'Psychic';\n\t\t\t}\n\t\t\tif (target.getTypes().join() === newType || !target.setType(newType))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', target, 'typechange', newType);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Clever"
  },
  "captivate": {
    "num": 445,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Captivate",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "onTryImmunity": "function (pokemon, source) {\n\t\t\treturn (pokemon.gender === 'M' && source.gender === 'F') || (pokemon.gender === 'F' && source.gender === 'M');\n\t\t}",
    "boosts": {
      "spa": -2
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 2
      }
    },
    "contestType": "Cute"
  },
  "catastropika": {
    "num": 658,
    "accuracy": true,
    "basePower": 210,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Catastropika",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "pikaniumz",
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "celebrate": {
    "num": 606,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Celebrate",
    "pp": 40,
    "priority": 0,
    "flags": {},
    "onTryHit": "function (target, source) {\n\t\t\tthis.add('-activate', target, 'move: Celebrate');\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "charge": {
    "num": 268,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Charge",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "charge",
    "onHit": "function (pokemon) {\n\t\t\tthis.add('-activate', pokemon, 'move: Charge');\n\t\t}",
    "condition": {
      "duration": 2,
      "onRestart": "function (pokemon) {\n\t\t\t\tthis.effectState.duration = 2;\n\t\t\t}",
      "onBasePowerPriority": 9,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Electric') {\n\t\t\t\t\tthis.debug('charge boost');\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
    },
    "boosts": {
      "spd": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "chargebeam": {
    "num": 451,
    "accuracy": 90,
    "basePower": 50,
    "category": "Special",
    "name": "Charge Beam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 70,
      "self": {
        "boosts": {
          "spa": 1
        }
      }
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Beautiful"
  },
  "charm": {
    "num": 204,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Charm",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "boosts": {
      "atk": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "chatter": {
    "num": 448,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Chatter",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "distance": 1,
      "authentic": 1
    },
    "noSketch": true,
    "secondary": {
      "chance": 100,
      "volatileStatus": "confusion"
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Cute"
  },
  "chipaway": {
    "num": 498,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Chip Away",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ignoreDefensive": true,
    "ignoreEvasion": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "circlethrow": {
    "num": 509,
    "accuracy": 90,
    "basePower": 60,
    "category": "Physical",
    "name": "Circle Throw",
    "pp": 10,
    "priority": -6,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "forceSwitch": true,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "clamp": {
    "num": 128,
    "accuracy": 85,
    "basePower": 35,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Clamp",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "clangingscales": {
    "num": 691,
    "accuracy": 100,
    "basePower": 110,
    "category": "Special",
    "name": "Clanging Scales",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "selfBoost": {
      "boosts": {
        "def": -1
      }
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Dragon",
    "contestType": "Tough"
  },
  "clangoroussoul": {
    "num": 775,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Clangorous Soul",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "sound": 1,
      "dance": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.hp <= (source.maxhp * 33 / 100) || source.maxhp === 1)\n\t\t\t\treturn false;\n\t\t}",
    "onTryHit": "function (pokemon, target, move) {\n\t\t\tif (!this.boost(move.boosts))\n\t\t\t\treturn null;\n\t\t\tdelete move.boosts;\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tthis.directDamage(pokemon.maxhp * 33 / 100);\n\t\t}",
    "boosts": {
      "atk": 1,
      "def": 1,
      "spa": 1,
      "spd": 1,
      "spe": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Dragon"
  },
  "clangoroussoulblaze": {
    "num": 728,
    "accuracy": true,
    "basePower": 185,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Clangorous Soulblaze",
    "pp": 1,
    "priority": 0,
    "flags": {
      "sound": 1,
      "authentic": 1
    },
    "selfBoost": {
      "boosts": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "isZ": "kommoniumz",
    "secondary": {},
    "target": "allAdjacentFoes",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "clearsmog": {
    "num": 499,
    "accuracy": true,
    "basePower": 50,
    "category": "Special",
    "name": "Clear Smog",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target) {\n\t\t\ttarget.clearBoosts();\n\t\t\tthis.add('-clearboost', target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "contestType": "Beautiful"
  },
  "closecombat": {
    "num": 370,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Close Combat",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "def": -1,
        "spd": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "coaching": {
    "num": 811,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Coaching",
    "pp": 10,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "secondary": null,
    "boosts": {
      "atk": 1,
      "def": 1
    },
    "target": "adjacentAlly",
    "type": "Fighting"
  },
  "coil": {
    "num": 489,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Coil",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1,
      "def": 1,
      "accuracy": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Poison",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "cometpunch": {
    "num": 4,
    "accuracy": 85,
    "basePower": 18,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Comet Punch",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "maxMove": {
      "basePower": 100
    },
    "contestType": "Tough"
  },
  "confide": {
    "num": 590,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Confide",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "boosts": {
      "spa": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "confuseray": {
    "num": 109,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Confuse Ray",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "confusion",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "confusion": {
    "num": 93,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Confusion",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "constrict": {
    "num": 132,
    "accuracy": 100,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Constrict",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "continentalcrush": {
    "num": 632,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Continental Crush",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "rockiumz",
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Cool"
  },
  "conversion": {
    "num": 160,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Conversion",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onHit": "function (target) {\n\t\t\tvar type = this.dex.moves.get(target.moveSlots[0].id).type;\n\t\t\tif (target.hasType(type) || !target.setType(type))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', target, 'typechange', type);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "conversion2": {
    "num": 176,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Conversion 2",
    "pp": 30,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (!target.lastMoveUsed) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tvar possibleTypes = [];\n\t\t\tvar attackType = target.lastMoveUsed.type;\n\t\t\tfor (var _i = 0, _a = this.dex.types.names(); _i < _a.length; _i++) {\n\t\t\t\tvar type = _a[_i];\n\t\t\t\tif (source.hasType(type))\n\t\t\t\t\tcontinue;\n\t\t\t\tvar typeCheck = this.dex.types.get(type).damageTaken[attackType];\n\t\t\t\tif (typeCheck === 2 || typeCheck === 3) {\n\t\t\t\t\tpossibleTypes.push(type);\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!possibleTypes.length) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tvar randomType = this.sample(possibleTypes);\n\t\t\tif (!source.setType(randomType))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', source, 'typechange', randomType);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Beautiful"
  },
  "copycat": {
    "num": 383,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Copycat",
    "pp": 20,
    "priority": 0,
    "flags": {},
    "onHit": "function (pokemon) {\n\t\t\tvar noCopycat = [\n\t\t\t\t'assist', 'banefulbunker', 'beakblast', 'behemothbash', 'behemothblade', 'belch', 'bestow', 'celebrate', 'chatter', 'circlethrow', 'copycat', 'counter', 'covet', 'craftyshield', 'destinybond', 'detect', 'dragontail', 'dynamaxcannon', 'endure', 'feint', 'focuspunch', 'followme', 'helpinghand', 'holdhands', 'kingsshield', 'matblock', 'mefirst', 'metronome', 'mimic', 'mirrorcoat', 'mirrormove', 'naturepower', 'obstruct', 'protect', 'ragepowder', 'roar', 'shelltrap', 'sketch', 'sleeptalk', 'snatch', 'spikyshield', 'spotlight', 'struggle', 'switcheroo', 'thief', 'transform', 'trick', 'whirlwind',\n\t\t\t];\n\t\t\tvar move = this.lastMove;\n\t\t\tif (!move)\n\t\t\t\treturn;\n\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\tif (noCopycat.includes(move.id) || move.isZ || move.isMax) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.actions.useMove(move.id, pokemon);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cute"
  },
  "coreenforcer": {
    "num": 687,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Core Enforcer",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.getAbility().isPermanent)\n\t\t\t\treturn;\n\t\t\tif (target.newlySwitched || this.queue.willMove(target))\n\t\t\t\treturn;\n\t\t\ttarget.addVolatile('gastroacid');\n\t\t}",
    "onAfterSubDamage": "function (damage, target) {\n\t\t\tif (target.getAbility().isPermanent)\n\t\t\t\treturn;\n\t\t\tif (target.newlySwitched || this.queue.willMove(target))\n\t\t\t\treturn;\n\t\t\ttarget.addVolatile('gastroacid');\n\t\t}",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Dragon",
    "zMove": {
      "basePower": 140
    },
    "contestType": "Tough"
  },
  "corkscrewcrash": {
    "num": 638,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Corkscrew Crash",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "steeliumz",
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "corrosivegas": {
    "num": 810,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Corrosive Gas",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar item = target.takeItem(source);\n\t\t\tif (item) {\n\t\t\t\tthis.add('-enditem', target, item.name, '[from] move: Corrosive Gas', '[of] ' + source);\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-fail', target, 'move: Corrosive Gas');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Poison"
  },
  "cosmicpower": {
    "num": 322,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Cosmic Power",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 1,
      "spd": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Beautiful"
  },
  "cottonguard": {
    "num": 538,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Cotton Guard",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 3
    },
    "secondary": null,
    "target": "self",
    "type": "Grass",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "cottonspore": {
    "num": 178,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Cotton Spore",
    "pp": 40,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "spe": -2
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Grass",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "counter": {
    "num": 68,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon) {\n\t\t\tif (!pokemon.volatiles['counter'])\n\t\t\t\treturn 0;\n\t\t\treturn pokemon.volatiles['counter'].damage || 1;\n\t\t}",
    "category": "Physical",
    "name": "Counter",
    "pp": 20,
    "priority": -5,
    "flags": {
      "contact": 1,
      "protect": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tpokemon.addVolatile('counter');\n\t\t}",
    "onTryHit": "function (target, source, move) {\n\t\t\tif (!source.volatiles['counter'])\n\t\t\t\treturn false;\n\t\t\tif (source.volatiles['counter'].slot === null)\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "duration": 1,
      "noCopy": true,
      "onStart": "function (target, source, move) {\n\t\t\t\tthis.effectState.slot = null;\n\t\t\t\tthis.effectState.damage = 0;\n\t\t\t}",
      "onRedirectTargetPriority": -1,
      "onRedirectTarget": "function (target, source, source2, move) {\n\t\t\t\tif (move.id !== 'counter')\n\t\t\t\t\treturn;\n\t\t\t\tif (source !== this.effectState.target || !this.effectState.slot)\n\t\t\t\t\treturn;\n\t\t\t\treturn this.getAtSlot(this.effectState.slot);\n\t\t\t}",
      "onDamagingHit": "function (damage, target, source, move) {\n\t\t\t\tif (!source.isAlly(target) && this.getCategory(move) === 'Physical') {\n\t\t\t\t\tthis.effectState.slot = source.getSlot();\n\t\t\t\t\tthis.effectState.damage = 2 * damage;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "scripted",
    "type": "Fighting",
    "maxMove": {
      "basePower": 75
    },
    "contestType": "Tough"
  },
  "courtchange": {
    "num": 756,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Court Change",
    "pp": 10,
    "priority": 0,
    "flags": {
      "mirror": 1
    },
    "onHitField": "function (target, source) {\n\t\t\tvar _a, _b;\n\t\t\tvar sideConditions = [\n\t\t\t\t'mist', 'lightscreen', 'reflect', 'spikes', 'safeguard', 'tailwind', 'toxicspikes', 'stealthrock', 'waterpledge', 'firepledge', 'grasspledge', 'stickyweb', 'auroraveil', 'gmaxsteelsurge', 'gmaxcannonade', 'gmaxvinelash', 'gmaxwildfire',\n\t\t\t];\n\t\t\tvar success = false;\n\t\t\tif (this.gameType === \"freeforall\") {\n\t\t\t\t// random integer from 1-3 inclusive\n\t\t\t\tvar offset = this.random(3) + 1;\n\t\t\t\t// the list of all sides in counterclockwise order\n\t\t\t\tvar sides = [this.sides[0], this.sides[2], this.sides[1], this.sides[3]];\n\t\t\t\tfor (var _i = 0, sideConditions_1 = sideConditions; _i < sideConditions_1.length; _i++) {\n\t\t\t\t\tvar id = sideConditions_1[_i];\n\t\t\t\t\tvar effectName = this.dex.conditions.get(id).name;\n\t\t\t\t\tvar rotatedSides = [];\n\t\t\t\t\tvar someCondition = false;\n\t\t\t\t\tfor (var i = 0; i < 4; i++) {\n\t\t\t\t\t\tvar sourceSide = sides[i];\n\t\t\t\t\t\tvar targetSide = sides[(i + offset) % 4]; // the next side in rotation\n\t\t\t\t\t\trotatedSides.push(targetSide.sideConditions[id]);\n\t\t\t\t\t\tif (sourceSide.sideConditions[id]) {\n\t\t\t\t\t\t\tthis.add('-sideend', sourceSide, effectName, '[silent]');\n\t\t\t\t\t\t\tsomeCondition = true;\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t\tif (!someCondition)\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\t_a = __spreadArrays(rotatedSides), sides[0].sideConditions[id] = _a[0], sides[1].sideConditions[id] = _a[1], sides[2].sideConditions[id] = _a[2], sides[3].sideConditions[id] = _a[3];\n\t\t\t\t\tfor (var _c = 0, sides_1 = sides; _c < sides_1.length; _c++) {\n\t\t\t\t\t\tvar side = sides_1[_c];\n\t\t\t\t\t\tif (side.sideConditions[id]) {\n\t\t\t\t\t\t\tvar layers = side.sideConditions[id].layers || 1;\n\t\t\t\t\t\t\tfor (; layers > 0; layers--)\n\t\t\t\t\t\t\t\tthis.add('-sidestart', side, effectName, '[silent]');\n\t\t\t\t\t\t}\n\t\t\t\t\t\telse {\n\t\t\t\t\t\t\tdelete side.sideConditions[id];\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t\tsuccess = true;\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tvar sourceSide = source.side;\n\t\t\t\tvar targetSide = source.side.foe;\n\t\t\t\tfor (var _d = 0, sideConditions_2 = sideConditions; _d < sideConditions_2.length; _d++) {\n\t\t\t\t\tvar id = sideConditions_2[_d];\n\t\t\t\t\tvar effectName = this.dex.conditions.get(id).name;\n\t\t\t\t\tif (sourceSide.sideConditions[id] && targetSide.sideConditions[id]) {\n\t\t\t\t\t\t_b = [\n\t\t\t\t\t\t\ttargetSide.sideConditions[id], sourceSide.sideConditions[id],\n\t\t\t\t\t\t], sourceSide.sideConditions[id] = _b[0], targetSide.sideConditions[id] = _b[1];\n\t\t\t\t\t\tthis.add('-sideend', sourceSide, effectName, '[silent]');\n\t\t\t\t\t\tthis.add('-sideend', targetSide, effectName, '[silent]');\n\t\t\t\t\t}\n\t\t\t\t\telse if (sourceSide.sideConditions[id] && !targetSide.sideConditions[id]) {\n\t\t\t\t\t\ttargetSide.sideConditions[id] = sourceSide.sideConditions[id];\n\t\t\t\t\t\tdelete sourceSide.sideConditions[id];\n\t\t\t\t\t\tthis.add('-sideend', sourceSide, effectName, '[silent]');\n\t\t\t\t\t}\n\t\t\t\t\telse if (targetSide.sideConditions[id] && !sourceSide.sideConditions[id]) {\n\t\t\t\t\t\tsourceSide.sideConditions[id] = targetSide.sideConditions[id];\n\t\t\t\t\t\tdelete targetSide.sideConditions[id];\n\t\t\t\t\t\tthis.add('-sideend', targetSide, effectName, '[silent]');\n\t\t\t\t\t}\n\t\t\t\t\telse {\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\t}\n\t\t\t\t\tvar sourceLayers = sourceSide.sideConditions[id] ? (sourceSide.sideConditions[id].layers || 1) : 0;\n\t\t\t\t\tvar targetLayers = targetSide.sideConditions[id] ? (targetSide.sideConditions[id].layers || 1) : 0;\n\t\t\t\t\tfor (; sourceLayers > 0; sourceLayers--) {\n\t\t\t\t\t\tthis.add('-sidestart', sourceSide, effectName, '[silent]');\n\t\t\t\t\t}\n\t\t\t\t\tfor (; targetLayers > 0; targetLayers--) {\n\t\t\t\t\t\tthis.add('-sidestart', targetSide, effectName, '[silent]');\n\t\t\t\t\t}\n\t\t\t\t\tsuccess = true;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!success)\n\t\t\t\treturn false;\n\t\t\tthis.add('-activate', source, 'move: Court Change');\n\t\t}",
    "secondary": null,
    "target": "all",
    "type": "Normal"
  },
  "covet": {
    "num": 343,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Covet",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onAfterHit": "function (target, source, move) {\n\t\t\tif (source.item || source.volatiles['gem']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar yourItem = target.takeItem(source);\n\t\t\tif (!yourItem) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (!this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem) ||\n\t\t\t\t!source.setItem(yourItem)) {\n\t\t\t\ttarget.item = yourItem.id; // bypass setItem so we don't break choicelock or anything\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-item', source, yourItem, '[from] move: Covet', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "crabhammer": {
    "num": 152,
    "accuracy": 90,
    "basePower": 100,
    "category": "Physical",
    "name": "Crabhammer",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "craftyshield": {
    "num": 578,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Crafty Shield",
    "pp": 10,
    "priority": 3,
    "flags": {},
    "sideCondition": "craftyshield",
    "onTry": "function () {\n\t\t\treturn !!this.queue.willAct();\n\t\t}",
    "condition": {
      "duration": 1,
      "onSideStart": "function (target, source) {\n\t\t\t\tthis.add('-singleturn', source, 'Crafty Shield');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (['self', 'all'].includes(move.target) || move.category !== 'Status')\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-activate', target, 'move: Crafty Shield');\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "crosschop": {
    "num": 238,
    "accuracy": 80,
    "basePower": 100,
    "category": "Physical",
    "name": "Cross Chop",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "crosspoison": {
    "num": 440,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Cross Poison",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "psn"
    },
    "critRatio": 2,
    "target": "normal",
    "type": "Poison",
    "contestType": "Cool"
  },
  "crunch": {
    "num": 242,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Crunch",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Dark",
    "contestType": "Tough"
  },
  "crushclaw": {
    "num": 306,
    "accuracy": 95,
    "basePower": 75,
    "category": "Physical",
    "name": "Crush Claw",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "crushgrip": {
    "num": 462,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\treturn Math.floor(Math.floor((120 * (100 * Math.floor(target.hp * 4096 / target.maxhp)) + 2048 - 1) / 4096) / 100) || 1;\n\t\t}",
    "category": "Physical",
    "name": "Crush Grip",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 190
    },
    "maxMove": {
      "basePower": 140
    },
    "contestType": "Tough"
  },
  "curse": {
    "num": 174,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Curse",
    "pp": 10,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "volatileStatus": "curse",
    "onModifyMove": "function (move, source, target) {\n\t\t\tif (!source.hasType('Ghost')) {\n\t\t\t\tmove.target = move.nonGhostTarget;\n\t\t\t}\n\t\t}",
    "onTryHit": "function (target, source, move) {\n\t\t\tif (!source.hasType('Ghost')) {\n\t\t\t\tdelete move.volatileStatus;\n\t\t\t\tdelete move.onHit;\n\t\t\t\tmove.self = { boosts: { spe: -1, atk: 1, def: 1 } };\n\t\t\t}\n\t\t\telse if (move.volatileStatus && target.volatiles['curse']) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tthis.directDamage(source.maxhp / 2, source, source);\n\t\t}",
    "condition": {
      "onStart": "function (pokemon, source) {\n\t\t\t\tthis.add('-start', pokemon, 'Curse', '[of] ' + source);\n\t\t\t}",
      "onResidualOrder": 12,
      "onResidual": "function (pokemon) {\n\t\t\t\tthis.damage(pokemon.baseMaxhp / 4);\n\t\t\t}"
    },
    "secondary": null,
    "target": "randomNormal",
    "nonGhostTarget": "self",
    "type": "Ghost",
    "zMove": {
      "effect": "curse"
    },
    "contestType": "Tough"
  },
  "cut": {
    "num": 15,
    "accuracy": 95,
    "basePower": 50,
    "category": "Physical",
    "name": "Cut",
    "pp": 30,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "darkestlariat": {
    "num": 663,
    "accuracy": 100,
    "basePower": 85,
    "category": "Physical",
    "name": "Darkest Lariat",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ignoreEvasion": true,
    "ignoreDefensive": true,
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Cool"
  },
  "darkpulse": {
    "num": 399,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Dark Pulse",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "pulse": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "any",
    "type": "Dark",
    "contestType": "Cool"
  },
  "darkvoid": {
    "num": 464,
    "accuracy": 50,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Dark Void",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "slp",
    "onTry": "function (source, target, move) {\n\t\t\tif (source.species.name === 'Darkrai' || move.hasBounced) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-fail', source, 'move: Dark Void');\n\t\t\tthis.hint(\"Only a Pokemon whose form is Darkrai can use this move.\");\n\t\t\treturn null;\n\t\t}",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Dark",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "dazzlinggleam": {
    "num": 605,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Dazzling Gleam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Fairy",
    "contestType": "Beautiful"
  },
  "decorate": {
    "num": 777,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Decorate",
    "pp": 15,
    "priority": 0,
    "flags": {
      "mystery": 1
    },
    "secondary": null,
    "boosts": {
      "atk": 2,
      "spa": 2
    },
    "target": "normal",
    "type": "Fairy"
  },
  "defendorder": {
    "num": 455,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Defend Order",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 1,
      "spd": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Bug",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "defensecurl": {
    "num": 111,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Defense Curl",
    "pp": 40,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 1
    },
    "volatileStatus": "defensecurl",
    "condition": {
      "noCopy": true
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cute"
  },
  "defog": {
    "num": 432,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Defog",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tvar success = false;\n\t\t\tif (!target.volatiles['substitute'] || move.infiltrates)\n\t\t\t\tsuccess = !!this.boost({ evasion: -1 });\n\t\t\tvar removeTarget = [\n\t\t\t\t'reflect', 'lightscreen', 'auroraveil', 'safeguard', 'mist', 'spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge',\n\t\t\t];\n\t\t\tvar removeAll = [\n\t\t\t\t'spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge',\n\t\t\t];\n\t\t\tfor (var _i = 0, removeTarget_1 = removeTarget; _i < removeTarget_1.length; _i++) {\n\t\t\t\tvar targetCondition = removeTarget_1[_i];\n\t\t\t\tif (target.side.removeSideCondition(targetCondition)) {\n\t\t\t\t\tif (!removeAll.includes(targetCondition))\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tthis.add('-sideend', target.side, this.dex.conditions.get(targetCondition).name, '[from] move: Defog', '[of] ' + source);\n\t\t\t\t\tsuccess = true;\n\t\t\t\t}\n\t\t\t}\n\t\t\tfor (var _a = 0, removeAll_1 = removeAll; _a < removeAll_1.length; _a++) {\n\t\t\t\tvar sideCondition = removeAll_1[_a];\n\t\t\t\tif (source.side.removeSideCondition(sideCondition)) {\n\t\t\t\t\tthis.add('-sideend', source.side, this.dex.conditions.get(sideCondition).name, '[from] move: Defog', '[of] ' + source);\n\t\t\t\t\tsuccess = true;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.field.clearTerrain();\n\t\t\treturn success;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cool"
  },
  "destinybond": {
    "num": 194,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Destiny Bond",
    "pp": 5,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "volatileStatus": "destinybond",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !pokemon.removeVolatile('destinybond');\n\t\t}",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singlemove', pokemon, 'Destiny Bond');\n\t\t\t}",
      "onFaint": "function (target, source, effect) {\n\t\t\t\tif (!source || !effect || target.isAlly(source))\n\t\t\t\t\treturn;\n\t\t\t\tif (effect.effectType === 'Move' && !effect.isFutureMove) {\n\t\t\t\t\tif (source.volatiles['dynamax']) {\n\t\t\t\t\t\tthis.add('-hint', \"Dynamaxed Pokémon are immune to Destiny Bond.\");\n\t\t\t\t\t\treturn;\n\t\t\t\t\t}\n\t\t\t\t\tthis.add('-activate', target, 'move: Destiny Bond');\n\t\t\t\t\tsource.faint();\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": -1,
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tif (move.id === 'destinybond')\n\t\t\t\t\treturn;\n\t\t\t\tthis.debug('removing Destiny Bond before attack');\n\t\t\t\tpokemon.removeVolatile('destinybond');\n\t\t\t}",
      "onMoveAborted": "function (pokemon, target, move) {\n\t\t\t\tpokemon.removeVolatile('destinybond');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Ghost",
    "zMove": {
      "effect": "redirect"
    },
    "contestType": "Clever"
  },
  "detect": {
    "num": 197,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Detect",
    "pp": 5,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "protect",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Fighting",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Cool"
  },
  "devastatingdrake": {
    "num": 652,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Devastating Drake",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "dragoniumz",
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "diamondstorm": {
    "num": 591,
    "accuracy": 95,
    "basePower": 100,
    "category": "Physical",
    "name": "Diamond Storm",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "chance": 50,
      "boosts": {
        "def": 2
      }
    },
    "secondary": {},
    "target": "allAdjacentFoes",
    "type": "Rock",
    "contestType": "Beautiful"
  },
  "dig": {
    "num": 91,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Dig",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onImmunity": "function (type, pokemon) {\n\t\t\t\tif (type === 'sandstorm' || type === 'hail')\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onInvulnerability": "function (target, source, move) {\n\t\t\t\tif (['earthquake', 'magnitude'].includes(move.id)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (move.id === 'earthquake' || move.id === 'magnitude') {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "disable": {
    "num": 50,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Disable",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "disable",
    "onTryHit": "function (target) {\n\t\t\tif (!target.lastMove || target.lastMove.isZ || target.lastMove.isMax || target.lastMove.id === 'struggle') {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 5,
      "noCopy": true,
      "onStart": "function (pokemon, source, effect) {\n\t\t\t\t// The target hasn't taken its turn, or Cursed Body activated and the move was not used through Dancer or Instruct\n\t\t\t\tif (this.queue.willMove(pokemon) ||\n\t\t\t\t\t(pokemon === this.activePokemon && this.activeMove && !this.activeMove.isExternal)) {\n\t\t\t\t\tthis.effectState.duration--;\n\t\t\t\t}\n\t\t\t\tif (!pokemon.lastMove) {\n\t\t\t\t\tthis.debug(\"Pokemon hasn't moved yet\");\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (moveSlot.id === pokemon.lastMove.id) {\n\t\t\t\t\t\tif (!moveSlot.pp) {\n\t\t\t\t\t\t\tthis.debug('Move out of PP');\n\t\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (effect.effectType === 'Ability') {\n\t\t\t\t\tthis.add('-start', pokemon, 'Disable', pokemon.lastMove.name, '[from] ability: Cursed Body', '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-start', pokemon, 'Disable', pokemon.lastMove.name);\n\t\t\t\t}\n\t\t\t\tthis.effectState.move = pokemon.lastMove.id;\n\t\t\t}",
      "onResidualOrder": 17,
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'Disable');\n\t\t\t}",
      "onBeforeMovePriority": 7,
      "onBeforeMove": "function (attacker, defender, move) {\n\t\t\t\tif (!move.isZ && move.id === this.effectState.move) {\n\t\t\t\t\tthis.add('cant', attacker, 'Disable', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (moveSlot.id === this.effectState.move) {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "disarmingvoice": {
    "num": 574,
    "accuracy": true,
    "basePower": 40,
    "category": "Special",
    "name": "Disarming Voice",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Fairy",
    "contestType": "Cute"
  },
  "discharge": {
    "num": 435,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Discharge",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "allAdjacent",
    "type": "Electric",
    "contestType": "Beautiful"
  },
  "dive": {
    "num": 291,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Dive",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (attacker.hasAbility('gulpmissile') && attacker.species.name === 'Cramorant' && !attacker.transformed) {\n\t\t\t\tvar forme = attacker.hp <= attacker.maxhp / 2 ? 'cramorantgorging' : 'cramorantgulping';\n\t\t\t\tattacker.formeChange(forme, move);\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onImmunity": "function (type, pokemon) {\n\t\t\t\tif (type === 'sandstorm' || type === 'hail')\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onInvulnerability": "function (target, source, move) {\n\t\t\t\tif (['surf', 'whirlpool'].includes(move.id)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (move.id === 'surf' || move.id === 'whirlpool') {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "dizzypunch": {
    "num": 146,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Dizzy Punch",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "doomdesire": {
    "num": 353,
    "accuracy": 100,
    "basePower": 140,
    "category": "Special",
    "name": "Doom Desire",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isFutureMove": true,
    "onTry": "function (source, target) {\n\t\t\tif (!target.side.addSlotCondition(target, 'futuremove'))\n\t\t\t\treturn false;\n\t\t\tObject.assign(target.side.slotConditions[target.position]['futuremove'], {\n\t\t\t\tmove: 'doomdesire',\n\t\t\t\tsource: source,\n\t\t\t\tmoveData: {\n\t\t\t\t\tid: 'doomdesire',\n\t\t\t\t\tname: \"Doom Desire\",\n\t\t\t\t\taccuracy: 100,\n\t\t\t\t\tbasePower: 140,\n\t\t\t\t\tcategory: \"Special\",\n\t\t\t\t\tpriority: 0,\n\t\t\t\t\tflags: {},\n\t\t\t\t\teffectType: 'Move',\n\t\t\t\t\tisFutureMove: true,\n\t\t\t\t\ttype: 'Steel',\n\t\t\t\t},\n\t\t\t});\n\t\t\tthis.add('-start', source, 'Doom Desire');\n\t\t\treturn this.NOT_FAIL;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Beautiful"
  },
  "doubleedge": {
    "num": 38,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Double-Edge",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      33,
      100
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "doublehit": {
    "num": 458,
    "accuracy": 90,
    "basePower": 35,
    "category": "Physical",
    "name": "Double Hit",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 120
    },
    "contestType": "Cool"
  },
  "doubleironbash": {
    "num": 742,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Double Iron Bash",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "multihit": 2,
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Steel",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 140
    },
    "contestType": "Clever"
  },
  "doublekick": {
    "num": 24,
    "accuracy": 100,
    "basePower": 30,
    "category": "Physical",
    "name": "Double Kick",
    "pp": 30,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "maxMove": {
      "basePower": 80
    },
    "contestType": "Cool"
  },
  "doubleslap": {
    "num": 3,
    "accuracy": 85,
    "basePower": 15,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Double Slap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "doubleteam": {
    "num": 104,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Double Team",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "evasion": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cool"
  },
  "dracometeor": {
    "num": 434,
    "accuracy": 90,
    "basePower": 130,
    "category": "Special",
    "name": "Draco Meteor",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spa": -2
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Beautiful"
  },
  "dragonascent": {
    "num": 620,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Dragon Ascent",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "self": {
      "boosts": {
        "def": -1,
        "spd": -1
      }
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Beautiful"
  },
  "dragonbreath": {
    "num": 225,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "name": "Dragon Breath",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "dragonclaw": {
    "num": 337,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Dragon Claw",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "dragondance": {
    "num": 349,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Dragon Dance",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "dance": 1
    },
    "boosts": {
      "atk": 1,
      "spe": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Dragon",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cool"
  },
  "dragondarts": {
    "num": 751,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Dragon Darts",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "smartTarget": true,
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "maxMove": {
      "basePower": 130
    }
  },
  "dragonenergy": {
    "num": 820,
    "accuracy": 100,
    "basePower": 150,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn move.basePower * pokemon.hp / pokemon.maxhp;\n\t\t}",
    "category": "Special",
    "name": "Dragon Energy",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Dragon"
  },
  "dragonhammer": {
    "num": 692,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Dragon Hammer",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Tough"
  },
  "dragonpulse": {
    "num": 406,
    "accuracy": 100,
    "basePower": 85,
    "category": "Special",
    "name": "Dragon Pulse",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "pulse": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Dragon",
    "contestType": "Beautiful"
  },
  "dragonrage": {
    "num": 82,
    "accuracy": 100,
    "basePower": 0,
    "damage": 40,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Dragon Rage",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "dragonrush": {
    "num": 407,
    "accuracy": 75,
    "basePower": 100,
    "category": "Physical",
    "name": "Dragon Rush",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Dragon",
    "contestType": "Tough"
  },
  "dragontail": {
    "num": 525,
    "accuracy": 90,
    "basePower": 60,
    "category": "Physical",
    "name": "Dragon Tail",
    "pp": 10,
    "priority": -6,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "forceSwitch": true,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Tough"
  },
  "drainingkiss": {
    "num": 577,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Draining Kiss",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      3,
      4
    ],
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Cute"
  },
  "drainpunch": {
    "num": 409,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Drain Punch",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "dreameater": {
    "num": 138,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Dream Eater",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "onTryImmunity": "function (target) {\n\t\t\treturn target.status === 'slp' || target.hasAbility('comatose');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "drillpeck": {
    "num": 65,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Drill Peck",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "drillrun": {
    "num": 529,
    "accuracy": 95,
    "basePower": 80,
    "category": "Physical",
    "name": "Drill Run",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "drumbeating": {
    "num": 778,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Drum Beating",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Grass"
  },
  "dualchop": {
    "num": 530,
    "accuracy": 90,
    "basePower": 40,
    "category": "Physical",
    "name": "Dual Chop",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "dualwingbeat": {
    "num": 814,
    "accuracy": 90,
    "basePower": 40,
    "category": "Physical",
    "name": "Dual Wingbeat",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "maxMove": {
      "basePower": 130
    }
  },
  "dynamaxcannon": {
    "num": 744,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Dynamax Cannon",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon"
  },
  "dynamicpunch": {
    "num": 223,
    "accuracy": 50,
    "basePower": 100,
    "category": "Physical",
    "name": "Dynamic Punch",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 100,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "earthpower": {
    "num": 414,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Earth Power",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Ground",
    "contestType": "Beautiful"
  },
  "earthquake": {
    "num": 89,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Earthquake",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": null,
    "target": "allAdjacent",
    "type": "Ground",
    "contestType": "Tough"
  },
  "echoedvoice": {
    "num": 497,
    "accuracy": 100,
    "basePower": 40,
    "basePowerCallback": "function () {\n\t\t\tif (this.field.pseudoWeather.echoedvoice) {\n\t\t\t\treturn 40 * this.field.pseudoWeather.echoedvoice.multiplier;\n\t\t\t}\n\t\t\treturn 40;\n\t\t}",
    "category": "Special",
    "name": "Echoed Voice",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "onTry": "function () {\n\t\t\tthis.field.addPseudoWeather('echoedvoice');\n\t\t}",
    "condition": {
      "duration": 2,
      "onFieldStart": "function () {\n\t\t\t\tthis.effectState.multiplier = 1;\n\t\t\t}",
      "onFieldRestart": "function () {\n\t\t\t\tif (this.effectState.duration !== 2) {\n\t\t\t\t\tthis.effectState.duration = 2;\n\t\t\t\t\tif (this.effectState.multiplier < 5) {\n\t\t\t\t\t\tthis.effectState.multiplier++;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "eerieimpulse": {
    "num": 598,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Eerie Impulse",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "spa": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "eeriespell": {
    "num": 826,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Eerie Spell",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": {
      "chance": 100,
      "onHit": "function (target) {\n\t\t\t\tif (!target.hp)\n\t\t\t\t\treturn;\n\t\t\t\tvar move = target.lastMove;\n\t\t\t\tif (!move || move.isZ)\n\t\t\t\t\treturn;\n\t\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\t\tvar ppDeducted = target.deductPP(move.id, 3);\n\t\t\t\tif (!ppDeducted)\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-activate', target, 'move: Eerie Spell', move.name, ppDeducted);\n\t\t\t}"
    },
    "target": "normal",
    "type": "Psychic"
  },
  "eggbomb": {
    "num": 121,
    "accuracy": 75,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Egg Bomb",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "electricterrain": {
    "num": 604,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Electric Terrain",
    "pp": 10,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "terrain": "electricterrain",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onSetStatus": "function (status, target, source, effect) {\n\t\t\t\tif (status.id === 'slp' && target.isGrounded() && !target.isSemiInvulnerable()) {\n\t\t\t\t\tif (effect.id === 'yawn' || (effect.effectType === 'Move' && !effect.secondaries)) {\n\t\t\t\t\t\tthis.add('-activate', target, 'move: Electric Terrain');\n\t\t\t\t\t}\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onTryAddVolatile": "function (status, target) {\n\t\t\t\tif (!target.isGrounded() || target.isSemiInvulnerable())\n\t\t\t\t\treturn;\n\t\t\t\tif (status.id === 'yawn') {\n\t\t\t\t\tthis.add('-activate', target, 'move: Electric Terrain');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}",
      "onBasePowerPriority": 6,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Electric' && attacker.isGrounded() && !attacker.isSemiInvulnerable()) {\n\t\t\t\t\tthis.debug('electric terrain boost');\n\t\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t\t}\n\t\t\t}",
      "onFieldStart": "function (field, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Electric Terrain', '[from] ability: ' + effect, '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Electric Terrain');\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 7,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Electric Terrain');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "electrify": {
    "num": 582,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Electrify",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "volatileStatus": "electrify",
    "onTryHit": "function (target) {\n\t\t\tif (!this.queue.willMove(target) && target.activeTurns)\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Electrify');\n\t\t\t}",
      "onModifyTypePriority": -2,
      "onModifyType": "function (move) {\n\t\t\t\tif (move.id !== 'struggle') {\n\t\t\t\t\tthis.debug('Electrify making move type electric');\n\t\t\t\t\tmove.type = 'Electric';\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "electroball": {
    "num": 486,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar ratio = Math.floor(pokemon.getStat('spe') / target.getStat('spe'));\n\t\t\tif (!isFinite(ratio))\n\t\t\t\tratio = 0;\n\t\t\tvar bp = [40, 60, 80, 120, 150][Math.min(ratio, 4)];\n\t\t\tthis.debug(bp + \" bp\");\n\t\t\treturn bp;\n\t\t}",
    "category": "Special",
    "name": "Electro Ball",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "electroweb": {
    "num": 527,
    "accuracy": 95,
    "basePower": 55,
    "category": "Special",
    "name": "Electroweb",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Electric",
    "contestType": "Beautiful"
  },
  "embargo": {
    "num": 373,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Embargo",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "embargo",
    "condition": {
      "duration": 5,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Embargo');\n\t\t\t}",
      "onResidualOrder": 21,
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'Embargo');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "ember": {
    "num": 52,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Ember",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Cute"
  },
  "encore": {
    "num": 227,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Encore",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "encore",
    "condition": {
      "duration": 3,
      "noCopy": true,
      "onStart": "function (target) {\n\t\t\t\tvar noEncore = [\n\t\t\t\t\t'assist', 'copycat', 'encore', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'sketch', 'sleeptalk', 'struggle', 'transform',\n\t\t\t\t];\n\t\t\t\tvar move = target.lastMove;\n\t\t\t\tif (!move || target.volatiles['dynamax'])\n\t\t\t\t\treturn false;\n\t\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\t\tvar moveIndex = target.moves.indexOf(move.id);\n\t\t\t\tif (move.isZ || noEncore.includes(move.id) || !target.moveSlots[moveIndex] || target.moveSlots[moveIndex].pp <= 0) {\n\t\t\t\t\t// it failed\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tthis.effectState.move = move.id;\n\t\t\t\tthis.add('-start', target, 'Encore');\n\t\t\t\tif (!this.queue.willMove(target)) {\n\t\t\t\t\tthis.effectState.duration++;\n\t\t\t\t}\n\t\t\t}",
      "onOverrideAction": "function (pokemon, target, move) {\n\t\t\t\tif (move.id !== this.effectState.move)\n\t\t\t\t\treturn this.effectState.move;\n\t\t\t}",
      "onResidualOrder": 16,
      "onResidual": "function (target) {\n\t\t\t\tif (target.moves.includes(this.effectState.move) &&\n\t\t\t\t\ttarget.moveSlots[target.moves.indexOf(this.effectState.move)].pp <= 0) {\n\t\t\t\t\t// early termination if you run out of PP\n\t\t\t\t\ttarget.removeVolatile('encore');\n\t\t\t\t}\n\t\t\t}",
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Encore');\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tif (!this.effectState.move || !pokemon.hasMove(this.effectState.move)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (moveSlot.id !== this.effectState.move) {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "endeavor": {
    "num": 283,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon, target) {\n\t\t\treturn target.getUndynamaxedHP() - pokemon.hp;\n\t\t}",
    "category": "Physical",
    "name": "Endeavor",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryImmunity": "function (target, pokemon) {\n\t\t\treturn pokemon.hp < target.hp;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "endure": {
    "num": 203,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Endure",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "endure",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Endure');\n\t\t\t}",
      "onDamagePriority": -10,
      "onDamage": "function (damage, target, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Move' && damage >= target.hp) {\n\t\t\t\t\tthis.add('-activate', target, 'move: Endure');\n\t\t\t\t\treturn target.hp - 1;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "energyball": {
    "num": 412,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Energy Ball",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "entrainment": {
    "num": 494,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Entrainment",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onTryHit": "function (target, source) {\n\t\t\tif (target === source || target.volatiles['dynamax'])\n\t\t\t\treturn false;\n\t\t\tvar additionalBannedSourceAbilities = [\n\t\t\t\t// Zen Mode included here for compatability with Gen 5-6\n\t\t\t\t'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'zenmode',\n\t\t\t];\n\t\t\tif (target.ability === source.ability ||\n\t\t\t\ttarget.getAbility().isPermanent || target.ability === 'truant' ||\n\t\t\t\tsource.getAbility().isPermanent || additionalBannedSourceAbilities.includes(source.ability)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tvar oldAbility = target.setAbility(source.ability);\n\t\t\tif (oldAbility) {\n\t\t\t\tthis.add('-ability', target, target.getAbility().name, '[from] move: Entrainment');\n\t\t\t\tif (!target.isAlly(source))\n\t\t\t\t\ttarget.volatileStaleness = 'external';\n\t\t\t\treturn;\n\t\t\t}\n\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "eruption": {
    "num": 284,
    "accuracy": 100,
    "basePower": 150,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn move.basePower * pokemon.hp / pokemon.maxhp;\n\t\t}",
    "category": "Special",
    "name": "Eruption",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "eternabeam": {
    "num": 795,
    "accuracy": 90,
    "basePower": 160,
    "category": "Special",
    "name": "Eternabeam",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon"
  },
  "expandingforce": {
    "num": 797,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Expanding Force",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, source) {\n\t\t\tif (this.field.isTerrain('psychicterrain') && source.isGrounded()) {\n\t\t\t\tthis.debug('terrain buff');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move, source, target) {\n\t\t\tif (this.field.isTerrain('psychicterrain') && source.isGrounded()) {\n\t\t\t\tmove.target = 'allAdjacentFoes';\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic"
  },
  "explosion": {
    "num": 153,
    "accuracy": 100,
    "basePower": 250,
    "category": "Physical",
    "name": "Explosion",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "selfdestruct": "always",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "extrasensory": {
    "num": 326,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Extrasensory",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "extremeevoboost": {
    "num": 702,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Extreme Evoboost",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "eeviumz",
    "boosts": {
      "atk": 2,
      "def": 2,
      "spa": 2,
      "spd": 2,
      "spe": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "extremespeed": {
    "num": 245,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Extreme Speed",
    "pp": 5,
    "priority": 2,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "facade": {
    "num": 263,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Facade",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon) {\n\t\t\tif (pokemon.status && pokemon.status !== 'slp') {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "fairylock": {
    "num": 587,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Fairy Lock",
    "pp": 10,
    "priority": 0,
    "flags": {
      "mirror": 1,
      "authentic": 1
    },
    "pseudoWeather": "fairylock",
    "condition": {
      "duration": 2,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-fieldactivate', 'move: Fairy Lock');\n\t\t\t}",
      "onTrapPokemon": "function (pokemon) {\n\t\t\t\tpokemon.tryTrap();\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "fairywind": {
    "num": 584,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Fairy Wind",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Beautiful"
  },
  "fakeout": {
    "num": 252,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Fake Out",
    "pp": 10,
    "priority": 3,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.activeMoveActions > 1) {\n\t\t\t\tthis.hint(\"Fake Out only works on your first turn out.\");\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 100,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "faketears": {
    "num": 313,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Fake Tears",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "boosts": {
      "spd": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Cute"
  },
  "falsesurrender": {
    "num": 793,
    "accuracy": true,
    "basePower": 80,
    "category": "Physical",
    "name": "False Surrender",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark"
  },
  "falseswipe": {
    "num": 206,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "False Swipe",
    "pp": 40,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onDamagePriority": -20,
    "onDamage": "function (damage, target, source, effect) {\n\t\t\tif (damage >= target.hp)\n\t\t\t\treturn target.hp - 1;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "featherdance": {
    "num": 297,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Feather Dance",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1,
      "dance": 1
    },
    "boosts": {
      "atk": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Beautiful"
  },
  "feint": {
    "num": 364,
    "accuracy": 100,
    "basePower": 30,
    "category": "Physical",
    "name": "Feint",
    "pp": 10,
    "priority": 2,
    "flags": {
      "mirror": 1
    },
    "breaksProtect": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Clever"
  },
  "feintattack": {
    "num": 185,
    "accuracy": true,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Feint Attack",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "fellstinger": {
    "num": 565,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Fell Stinger",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onAfterMoveSecondarySelf": "function (pokemon, target, move) {\n\t\t\tif (!target || target.fainted || target.hp <= 0)\n\t\t\t\tthis.boost({ atk: 3 }, pokemon, pokemon, move);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cool"
  },
  "fierydance": {
    "num": 552,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Fiery Dance",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "dance": 1
    },
    "secondary": {
      "chance": 50,
      "self": {
        "boosts": {
          "spa": 1
        }
      }
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "fierywrath": {
    "num": 822,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Fiery Wrath",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "allAdjacentFoes",
    "type": "Dark"
  },
  "finalgambit": {
    "num": 515,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon) {\n\t\t\tvar damage = pokemon.hp;\n\t\t\tpokemon.faint();\n\t\t\treturn damage;\n\t\t}",
    "category": "Special",
    "name": "Final Gambit",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "selfdestruct": "ifHit",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "zMove": {
      "basePower": 180
    },
    "contestType": "Tough"
  },
  "fireblast": {
    "num": 126,
    "accuracy": 85,
    "basePower": 110,
    "category": "Special",
    "name": "Fire Blast",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "firefang": {
    "num": 424,
    "accuracy": 95,
    "basePower": 65,
    "category": "Physical",
    "name": "Fire Fang",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondaries": [
      {
        "chance": 10,
        "status": "brn"
      },
      {
        "chance": 10,
        "volatileStatus": "flinch"
      }
    ],
    "target": "normal",
    "type": "Fire",
    "contestType": "Cool"
  },
  "firelash": {
    "num": 680,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Fire Lash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Cute"
  },
  "firepledge": {
    "num": 519,
    "accuracy": 100,
    "basePower": 80,
    "basePowerCallback": "function (target, source, move) {\n\t\t\tif (['grasspledge', 'waterpledge'].includes(move.sourceEffect)) {\n\t\t\t\tthis.add('-combine');\n\t\t\t\treturn 150;\n\t\t\t}\n\t\t\treturn 80;\n\t\t}",
    "category": "Special",
    "name": "Fire Pledge",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onPrepareHit": "function (target, source, move) {\n\t\t\tvar _a;\n\t\t\tfor (var _i = 0, _b = this.queue.list; _i < _b.length; _i++) {\n\t\t\t\tvar action = _b[_i];\n\t\t\t\tif (!action.move || !((_a = action.pokemon) === null || _a === void 0 ? void 0 : _a.isActive) ||\n\t\t\t\t\taction.pokemon.fainted || action.maxMove || action.zmove) {\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (action.pokemon.isAlly(source) && ['grasspledge', 'waterpledge'].includes(action.move.id)) {\n\t\t\t\t\tthis.queue.prioritizeAction(action, move);\n\t\t\t\t\tthis.add('-waiting', source, action.pokemon);\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move) {\n\t\t\tif (move.sourceEffect === 'waterpledge') {\n\t\t\t\tmove.type = 'Water';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.self = { sideCondition: 'waterpledge' };\n\t\t\t}\n\t\t\tif (move.sourceEffect === 'grasspledge') {\n\t\t\t\tmove.type = 'Fire';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.sideCondition = 'firepledge';\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'Fire Pledge');\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 1,
      "onResidual": "function (pokemon) {\n\t\t\t\tif (!pokemon.hasType('Fire'))\n\t\t\t\t\tthis.damage(pokemon.baseMaxhp / 8, pokemon);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 8,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'Fire Pledge');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "firepunch": {
    "num": 7,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Fire Punch",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Tough"
  },
  "firespin": {
    "num": 83,
    "accuracy": 85,
    "basePower": 35,
    "category": "Special",
    "name": "Fire Spin",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "firstimpression": {
    "num": 660,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "First Impression",
    "pp": 10,
    "priority": 2,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.activeMoveActions > 1) {\n\t\t\t\tthis.hint(\"First Impression only works on your first turn out.\");\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "fishiousrend": {
    "num": 755,
    "accuracy": 100,
    "basePower": 85,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.newlySwitched || this.queue.willMove(target)) {\n\t\t\t\tthis.debug('Fishious Rend damage boost');\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\tthis.debug('Fishious Rend NOT boosted');\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Fishious Rend",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water"
  },
  "fissure": {
    "num": 90,
    "accuracy": 30,
    "basePower": 0,
    "category": "Physical",
    "name": "Fissure",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "ohko": true,
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "flail": {
    "num": 175,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar ratio = pokemon.hp * 48 / pokemon.maxhp;\n\t\t\tif (ratio < 2) {\n\t\t\t\treturn 200;\n\t\t\t}\n\t\t\tif (ratio < 5) {\n\t\t\t\treturn 150;\n\t\t\t}\n\t\t\tif (ratio < 10) {\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (ratio < 17) {\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (ratio < 33) {\n\t\t\t\treturn 40;\n\t\t\t}\n\t\t\treturn 20;\n\t\t}",
    "category": "Physical",
    "name": "Flail",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cute"
  },
  "flameburst": {
    "num": 481,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Flame Burst",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tfor (var _i = 0, _a = target.adjacentAllies(); _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tthis.damage(ally.baseMaxhp / 16, ally, source, this.dex.conditions.get('Flame Burst'));\n\t\t\t}\n\t\t}",
    "onAfterSubDamage": "function (damage, target, source, move) {\n\t\t\tfor (var _i = 0, _a = target.adjacentAllies(); _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tthis.damage(ally.baseMaxhp / 16, ally, source, this.dex.conditions.get('Flame Burst'));\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "flamecharge": {
    "num": 488,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Flame Charge",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "self": {
        "boosts": {
          "spe": 1
        }
      }
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Cool"
  },
  "flamewheel": {
    "num": 172,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Flame Wheel",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "flamethrower": {
    "num": 53,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Flamethrower",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "flareblitz": {
    "num": 394,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Flare Blitz",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "recoil": [
      33,
      100
    ],
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Cool"
  },
  "flash": {
    "num": 148,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Flash",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "accuracy": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Beautiful"
  },
  "flashcannon": {
    "num": 430,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Flash Cannon",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Beautiful"
  },
  "flatter": {
    "num": 260,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Flatter",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "volatileStatus": "confusion",
    "boosts": {
      "spa": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "fleurcannon": {
    "num": 705,
    "accuracy": 90,
    "basePower": 130,
    "category": "Special",
    "name": "Fleur Cannon",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spa": -2
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Beautiful"
  },
  "fling": {
    "num": 374,
    "accuracy": 100,
    "basePower": 0,
    "category": "Physical",
    "name": "Fling",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onPrepareHit": "function (target, source, move) {\n\t\t\tif (source.ignoringItem())\n\t\t\t\treturn false;\n\t\t\tvar item = source.getItem();\n\t\t\tif (!this.singleEvent('TakeItem', item, source.itemState, source, source, move, item))\n\t\t\t\treturn false;\n\t\t\tif (!item.fling)\n\t\t\t\treturn false;\n\t\t\tmove.basePower = item.fling.basePower;\n\t\t\tif (item.isBerry) {\n\t\t\t\tmove.onHit = function (foe) {\n\t\t\t\t\tif (this.singleEvent('Eat', item, null, foe, null, null)) {\n\t\t\t\t\t\tthis.runEvent('EatItem', foe, null, null, item);\n\t\t\t\t\t\tif (item.id === 'leppaberry')\n\t\t\t\t\t\t\tfoe.staleness = 'external';\n\t\t\t\t\t}\n\t\t\t\t\tif (item.onEat)\n\t\t\t\t\t\tfoe.ateBerry = true;\n\t\t\t\t};\n\t\t\t}\n\t\t\telse if (item.fling.effect) {\n\t\t\t\tmove.onHit = item.fling.effect;\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (!move.secondaries)\n\t\t\t\t\tmove.secondaries = [];\n\t\t\t\tif (item.fling.status) {\n\t\t\t\t\tmove.secondaries.push({ status: item.fling.status });\n\t\t\t\t}\n\t\t\t\telse if (item.fling.volatileStatus) {\n\t\t\t\t\tmove.secondaries.push({ volatileStatus: item.fling.volatileStatus });\n\t\t\t\t}\n\t\t\t}\n\t\t\tsource.addVolatile('fling');\n\t\t}",
    "condition": {
      "onUpdate": "function (pokemon) {\n\t\t\t\tvar item = pokemon.getItem();\n\t\t\t\tpokemon.setItem('');\n\t\t\t\tpokemon.lastItem = item.id;\n\t\t\t\tpokemon.usedItemThisTurn = true;\n\t\t\t\tthis.add('-enditem', pokemon, item.name, '[from] move: Fling');\n\t\t\t\tthis.runEvent('AfterUseItem', pokemon, null, null, item);\n\t\t\t\tpokemon.removeVolatile('fling');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Cute"
  },
  "flipturn": {
    "num": 812,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Flip Turn",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "selfSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Water"
  },
  "floatyfall": {
    "num": 731,
    "accuracy": 95,
    "basePower": 90,
    "category": "Physical",
    "isNonstandard": "LGPE",
    "name": "Floaty Fall",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "gravity": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Flying",
    "contestType": "Cool"
  },
  "floralhealing": {
    "num": 666,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Floral Healing",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "heal": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar success = false;\n\t\t\tif (this.field.isTerrain('grassyterrain')) {\n\t\t\t\tsuccess = !!this.heal(this.modify(target.baseMaxhp, 0.667));\n\t\t\t}\n\t\t\telse {\n\t\t\t\tsuccess = !!this.heal(Math.ceil(target.baseMaxhp * 0.5));\n\t\t\t}\n\t\t\tif (success && !target.isAlly(source)) {\n\t\t\t\ttarget.staleness = 'external';\n\t\t\t}\n\t\t\treturn success;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "flowershield": {
    "num": 579,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Flower Shield",
    "pp": 10,
    "priority": 0,
    "flags": {
      "distance": 1
    },
    "onHitField": "function (t, source, move) {\n\t\t\tvar targets = [];\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (pokemon.hasType('Grass') &&\n\t\t\t\t\t(!pokemon.volatiles['maxguard'] ||\n\t\t\t\t\t\tthis.runEvent('TryHit', pokemon, source, move))) {\n\t\t\t\t\t// This move affects every Grass-type Pokemon in play.\n\t\t\t\t\ttargets.push(pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t\tvar success = false;\n\t\t\tfor (var _b = 0, targets_1 = targets; _b < targets_1.length; _b++) {\n\t\t\t\tvar target = targets_1[_b];\n\t\t\t\tsuccess = this.boost({ def: 1 }, target, source, move) || success;\n\t\t\t}\n\t\t\treturn success;\n\t\t}",
    "secondary": null,
    "target": "all",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Beautiful"
  },
  "fly": {
    "num": 19,
    "accuracy": 95,
    "basePower": 90,
    "category": "Physical",
    "name": "Fly",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1,
      "distance": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onInvulnerability": "function (target, source, move) {\n\t\t\t\tif (['gust', 'twister', 'skyuppercut', 'thunder', 'hurricane', 'smackdown', 'thousandarrows'].includes(move.id)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (move.id === 'gust' || move.id === 'twister') {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Clever"
  },
  "flyingpress": {
    "num": 560,
    "accuracy": 95,
    "basePower": 100,
    "category": "Physical",
    "name": "Flying Press",
    "pp": 10,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1,
      "distance": 1,
      "nonsky": 1
    },
    "onEffectiveness": "function (typeMod, target, type, move) {\n\t\t\treturn typeMod + this.dex.getEffectiveness('Flying', type);\n\t\t}",
    "priority": 0,
    "secondary": null,
    "target": "any",
    "type": "Fighting",
    "zMove": {
      "basePower": 170
    },
    "contestType": "Tough"
  },
  "focusblast": {
    "num": 411,
    "accuracy": 70,
    "basePower": 120,
    "category": "Special",
    "name": "Focus Blast",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "focusenergy": {
    "num": 116,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Focus Energy",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "focusenergy",
    "condition": {
      "onStart": "function (target, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') {\n\t\t\t\t\tthis.add('-start', target, 'move: Focus Energy', '[zeffect]');\n\t\t\t\t}\n\t\t\t\telse if (effect && (['imposter', 'psychup', 'transform'].includes(effect.id))) {\n\t\t\t\t\tthis.add('-start', target, 'move: Focus Energy', '[silent]');\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-start', target, 'move: Focus Energy');\n\t\t\t\t}\n\t\t\t}",
      "onModifyCritRatio": "function (critRatio) {\n\t\t\t\treturn critRatio + 2;\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cool"
  },
  "focuspunch": {
    "num": 264,
    "accuracy": 100,
    "basePower": 150,
    "category": "Physical",
    "name": "Focus Punch",
    "pp": 20,
    "priority": -3,
    "flags": {
      "contact": 1,
      "protect": 1,
      "punch": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tpokemon.addVolatile('focuspunch');\n\t\t}",
    "beforeMoveCallback": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['focuspunch'] && pokemon.volatiles['focuspunch'].lostFocus) {\n\t\t\t\tthis.add('cant', pokemon, 'Focus Punch', 'Focus Punch');\n\t\t\t\treturn true;\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'move: Focus Punch');\n\t\t\t}",
      "onHit": "function (pokemon, source, move) {\n\t\t\t\tif (move.category !== 'Status') {\n\t\t\t\t\tpokemon.volatiles['focuspunch'].lostFocus = true;\n\t\t\t\t}\n\t\t\t}",
      "onTryAddVolatile": "function (status, pokemon) {\n\t\t\t\tif (status.id === 'flinch')\n\t\t\t\t\treturn null;\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "followme": {
    "num": 266,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Follow Me",
    "pp": 20,
    "priority": 2,
    "flags": {},
    "volatileStatus": "followme",
    "onTry": "function (source) {\n\t\t\treturn this.activePerHalf > 1;\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') {\n\t\t\t\t\tthis.add('-singleturn', target, 'move: Follow Me', '[zeffect]');\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-singleturn', target, 'move: Follow Me');\n\t\t\t\t}\n\t\t\t}",
      "onFoeRedirectTargetPriority": 1,
      "onFoeRedirectTarget": "function (target, source, source2, move) {\n\t\t\t\tif (!this.effectState.target.isSkyDropped() && this.validTarget(this.effectState.target, source, move.target)) {\n\t\t\t\t\tif (move.smartTarget)\n\t\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t\tthis.debug(\"Follow Me redirected target of move\");\n\t\t\t\t\treturn this.effectState.target;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "forcepalm": {
    "num": 395,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Force Palm",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "foresight": {
    "num": 193,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Foresight",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "foresight",
    "onTryHit": "function (target) {\n\t\t\tif (target.volatiles['miracleeye'])\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Foresight');\n\t\t\t}",
      "onNegateImmunity": "function (pokemon, type) {\n\t\t\t\tif (pokemon.hasType('Ghost') && ['Normal', 'Fighting'].includes(type))\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onModifyBoost": "function (boosts) {\n\t\t\t\tif (boosts.evasion && boosts.evasion > 0) {\n\t\t\t\t\tboosts.evasion = 0;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "crit2"
    },
    "contestType": "Clever"
  },
  "forestscurse": {
    "num": 571,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Forest's Curse",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.hasType('Grass'))\n\t\t\t\treturn false;\n\t\t\tif (!target.addType('Grass'))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', target, 'typeadd', 'Grass', '[from] move: Forest's Curse');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "foulplay": {
    "num": 492,
    "accuracy": 100,
    "basePower": 95,
    "category": "Physical",
    "name": "Foul Play",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "useTargetOffensive": true,
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "freezedry": {
    "num": 573,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Freeze-Dry",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onEffectiveness": "function (typeMod, target, type) {\n\t\t\tif (type === 'Water')\n\t\t\t\treturn 1;\n\t\t}",
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "freezeshock": {
    "num": 553,
    "accuracy": 90,
    "basePower": 140,
    "category": "Physical",
    "name": "Freeze Shock",
    "pp": 5,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "freezingglare": {
    "num": 821,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Freezing Glare",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "normal",
    "type": "Psychic"
  },
  "freezyfrost": {
    "num": 739,
    "accuracy": 90,
    "basePower": 100,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Freezy Frost",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "onHit": "function () {\n\t\t\tthis.add('-clearallboost');\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tpokemon.clearBoosts();\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Clever"
  },
  "frenzyplant": {
    "num": 338,
    "accuracy": 90,
    "basePower": 150,
    "category": "Special",
    "name": "Frenzy Plant",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "frostbreath": {
    "num": 524,
    "accuracy": 90,
    "basePower": 60,
    "category": "Special",
    "name": "Frost Breath",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "willCrit": true,
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "frustration": {
    "num": 218,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon) {\n\t\t\treturn Math.floor(((255 - pokemon.happiness) * 10) / 25) || 1;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Frustration",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cute"
  },
  "furyattack": {
    "num": 31,
    "accuracy": 85,
    "basePower": 15,
    "category": "Physical",
    "name": "Fury Attack",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "furycutter": {
    "num": 210,
    "accuracy": 95,
    "basePower": 40,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (!pokemon.volatiles['furycutter'] || move.hit === 1) {\n\t\t\t\tpokemon.addVolatile('furycutter');\n\t\t\t}\n\t\t\treturn this.clampIntRange(move.basePower * pokemon.volatiles['furycutter'].multiplier, 1, 160);\n\t\t}",
    "category": "Physical",
    "name": "Fury Cutter",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "condition": {
      "duration": 2,
      "onStart": "function () {\n\t\t\t\tthis.effectState.multiplier = 1;\n\t\t\t}",
      "onRestart": "function () {\n\t\t\t\tif (this.effectState.multiplier < 4) {\n\t\t\t\t\tthis.effectState.multiplier <<= 1;\n\t\t\t\t}\n\t\t\t\tthis.effectState.duration = 2;\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cool"
  },
  "furyswipes": {
    "num": 154,
    "accuracy": 80,
    "basePower": 18,
    "category": "Physical",
    "name": "Fury Swipes",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "maxMove": {
      "basePower": 100
    },
    "contestType": "Tough"
  },
  "fusionbolt": {
    "num": 559,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Fusion Bolt",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon) {\n\t\t\tif (this.lastSuccessfulMoveThisTurn === 'fusionflare') {\n\t\t\t\tthis.debug('double power');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "fusionflare": {
    "num": 558,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Fusion Flare",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "onBasePower": "function (basePower, pokemon) {\n\t\t\tif (this.lastSuccessfulMoveThisTurn === 'fusionbolt') {\n\t\t\t\tthis.debug('double power');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "futuresight": {
    "num": 248,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "name": "Future Sight",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "ignoreImmunity": true,
    "isFutureMove": true,
    "onTry": "function (source, target) {\n\t\t\tif (!target.side.addSlotCondition(target, 'futuremove'))\n\t\t\t\treturn false;\n\t\t\tObject.assign(target.side.slotConditions[target.position]['futuremove'], {\n\t\t\t\tduration: 3,\n\t\t\t\tmove: 'futuresight',\n\t\t\t\tsource: source,\n\t\t\t\tmoveData: {\n\t\t\t\t\tid: 'futuresight',\n\t\t\t\t\tname: \"Future Sight\",\n\t\t\t\t\taccuracy: 100,\n\t\t\t\t\tbasePower: 120,\n\t\t\t\t\tcategory: \"Special\",\n\t\t\t\t\tpriority: 0,\n\t\t\t\t\tflags: {},\n\t\t\t\t\tignoreImmunity: false,\n\t\t\t\t\teffectType: 'Move',\n\t\t\t\t\tisFutureMove: true,\n\t\t\t\t\ttype: 'Psychic',\n\t\t\t\t},\n\t\t\t});\n\t\t\tthis.add('-start', source, 'move: Future Sight');\n\t\t\treturn this.NOT_FAIL;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "gastroacid": {
    "num": 380,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Gastro Acid",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "volatileStatus": "gastroacid",
    "onTryHit": "function (target) {\n\t\t\tif (target.getAbility().isPermanent) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-endability', pokemon);\n\t\t\t\tthis.singleEvent('End', pokemon.getAbility(), pokemon.abilityState, pokemon, pokemon, 'gastroacid');\n\t\t\t}",
      "onCopy": "function (pokemon) {\n\t\t\t\tif (pokemon.getAbility().isPermanent)\n\t\t\t\t\tpokemon.removeVolatile('gastroacid');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Tough"
  },
  "geargrind": {
    "num": 544,
    "accuracy": 85,
    "basePower": 50,
    "category": "Physical",
    "name": "Gear Grind",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Clever"
  },
  "gearup": {
    "num": 674,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Gear Up",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "authentic": 1
    },
    "onHitSide": "function (side, source, move) {\n\t\t\tvar _this = this;\n\t\t\tvar targets = side.allies().filter(function (target) { return (target.hasAbility(['plus', 'minus']) &&\n\t\t\t\t(!target.volatiles['maxguard'] || _this.runEvent('TryHit', target, source, move))); });\n\t\t\tif (!targets.length)\n\t\t\t\treturn false;\n\t\t\tvar didSomething = false;\n\t\t\tfor (var _i = 0, targets_2 = targets; _i < targets_2.length; _i++) {\n\t\t\t\tvar target = targets_2[_i];\n\t\t\t\tdidSomething = this.boost({ atk: 1, spa: 1 }, target, source, move, false, true) || didSomething;\n\t\t\t}\n\t\t\treturn didSomething;\n\t\t}",
    "secondary": null,
    "target": "allySide",
    "type": "Steel",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "genesissupernova": {
    "num": 703,
    "accuracy": true,
    "basePower": 185,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Genesis Supernova",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "mewniumz",
    "secondary": {
      "chance": 100,
      "self": {
        "onHit": "function () {\n\t\t\t\t\tthis.field.setTerrain('psychicterrain');\n\t\t\t\t}"
      }
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "geomancy": {
    "num": 601,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Geomancy",
    "pp": 10,
    "priority": 0,
    "flags": {
      "charge": 1,
      "nonsky": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "boosts": {
      "spa": 2,
      "spd": 2,
      "spe": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "gigadrain": {
    "num": 202,
    "accuracy": 100,
    "basePower": 75,
    "category": "Special",
    "name": "Giga Drain",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Clever"
  },
  "gigaimpact": {
    "num": 416,
    "accuracy": 90,
    "basePower": 150,
    "category": "Physical",
    "name": "Giga Impact",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "gigavolthavoc": {
    "num": 646,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Gigavolt Havoc",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "electriumz",
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "glaciallance": {
    "num": 824,
    "accuracy": 100,
    "basePower": 130,
    "category": "Physical",
    "name": "Glacial Lance",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Ice"
  },
  "glaciate": {
    "num": 549,
    "accuracy": 95,
    "basePower": 65,
    "category": "Special",
    "name": "Glaciate",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "glare": {
    "num": 137,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Glare",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "par",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Tough"
  },
  "glitzyglow": {
    "num": 736,
    "accuracy": 95,
    "basePower": 80,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Glitzy Glow",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "self": {
      "sideCondition": "lightscreen"
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "gmaxbefuddle": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Befuddle",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Butterfree",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tvar result = this.random(3);\n\t\t\t\t\tif (result === 0) {\n\t\t\t\t\t\tpokemon.trySetStatus('slp', source);\n\t\t\t\t\t}\n\t\t\t\t\telse if (result === 1) {\n\t\t\t\t\t\tpokemon.trySetStatus('par', source);\n\t\t\t\t\t}\n\t\t\t\t\telse {\n\t\t\t\t\t\tpokemon.trySetStatus('psn', source);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Bug",
    "contestType": "Cool"
  },
  "gmaxcannonade": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Cannonade",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Blastoise",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('gmaxcannonade');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'G-Max Cannonade');\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 1,
      "onResidual": "function (target) {\n\t\t\t\tif (!target.hasType('Water'))\n\t\t\t\t\tthis.damage(target.baseMaxhp / 6, target);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 11,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'G-Max Cannonade');\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "gmaxcentiferno": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Centiferno",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Centiskorch",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('partiallytrapped', source, this.dex.getActiveMove('G-Max Centiferno'));\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fire",
    "contestType": "Cool"
  },
  "gmaxchistrike": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Chi Strike",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Machamp",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('gmaxchistrike');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "noCopy": true,
      "onStart": "function (target, source, effect) {\n\t\t\t\tthis.effectState.layers = 1;\n\t\t\t\tif (!['imposter', 'psychup', 'transform'].includes(effect === null || effect === void 0 ? void 0 : effect.id)) {\n\t\t\t\t\tthis.add('-start', target, 'move: G-Max Chi Strike');\n\t\t\t\t}\n\t\t\t}",
      "onRestart": "function (target, source, effect) {\n\t\t\t\tif (this.effectState.layers >= 3)\n\t\t\t\t\treturn false;\n\t\t\t\tthis.effectState.layers++;\n\t\t\t\tif (!['imposter', 'psychup', 'transform'].includes(effect === null || effect === void 0 ? void 0 : effect.id)) {\n\t\t\t\t\tthis.add('-start', target, 'move: G-Max Chi Strike');\n\t\t\t\t}\n\t\t\t}",
      "onModifyCritRatio": "function (critRatio) {\n\t\t\t\treturn critRatio + this.effectState.layers;\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "gmaxcuddle": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Cuddle",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Eevee",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('attract');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Normal",
    "contestType": "Cool"
  },
  "gmaxdepletion": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Depletion",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Duraludon",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tvar move = pokemon.lastMove;\n\t\t\t\t\tif (!move || move.isZ)\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\t\t\tvar ppDeducted = pokemon.deductPP(move.id, 2);\n\t\t\t\t\tif (ppDeducted) {\n\t\t\t\t\t\tthis.add(\"-activate\", pokemon, 'move: G-Max Depletion', move.name, ppDeducted);\n\t\t\t\t\t\t// Don't return here because returning early doesn't trigger\n\t\t\t\t\t\t// activation text for the second Pokemon in doubles\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "gmaxdrumsolo": {
    "num": 1000,
    "accuracy": true,
    "basePower": 160,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Drum Solo",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Rillaboom",
    "ignoreAbility": true,
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Grass",
    "contestType": "Cool"
  },
  "gmaxfinale": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Finale",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Alcremie",
    "self": {
      "onHit": "function (target, source, move) {\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.heal(pokemon.maxhp / 6, pokemon, source, move);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fairy",
    "contestType": "Cool"
  },
  "gmaxfireball": {
    "num": 1000,
    "accuracy": true,
    "basePower": 160,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Fireball",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Cinderace",
    "ignoreAbility": true,
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fire",
    "contestType": "Cool"
  },
  "gmaxfoamburst": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Foam Burst",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Kingler",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spe: -2 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "gmaxgoldrush": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Gold Rush",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Meowth",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('confusion');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Normal",
    "contestType": "Cool"
  },
  "gmaxgravitas": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Gravitas",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Orbeetle",
    "self": {
      "pseudoWeather": "gravity"
    },
    "target": "adjacentFoe",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "gmaxhydrosnipe": {
    "num": 1000,
    "accuracy": true,
    "basePower": 160,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Hydrosnipe",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Inteleon",
    "ignoreAbility": true,
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "gmaxmalodor": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Malodor",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Garbodor",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.trySetStatus('psn', source);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Poison",
    "contestType": "Cool"
  },
  "gmaxmeltdown": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Meltdown",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Melmetal",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tif (!pokemon.volatiles['dynamax'])\n\t\t\t\t\t\tpokemon.addVolatile('torment');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Steel",
    "contestType": "Cool"
  },
  "gmaxoneblow": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max One Blow",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Urshifu",
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Dark",
    "contestType": "Cool"
  },
  "gmaxrapidflow": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Rapid Flow",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Urshifu-Rapid-Strike",
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "gmaxreplenish": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Replenish",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Snorlax",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (this.random(2) === 0)\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tif (pokemon.item)\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tif (pokemon.lastItem && this.dex.items.get(pokemon.lastItem).isBerry) {\n\t\t\t\t\t\tvar item = pokemon.lastItem;\n\t\t\t\t\t\tpokemon.lastItem = '';\n\t\t\t\t\t\tthis.add('-item', pokemon, this.dex.items.get(item), '[from] move: G-Max Replenish');\n\t\t\t\t\t\tpokemon.setItem(item);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Normal",
    "contestType": "Cool"
  },
  "gmaxresonance": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Resonance",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Lapras",
    "self": {
      "sideCondition": "auroraveil"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Ice",
    "contestType": "Cool"
  },
  "gmaxsandblast": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Sandblast",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Sandaconda",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('partiallytrapped', source, this.dex.getActiveMove('G-Max Sandblast'));\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Ground",
    "contestType": "Cool"
  },
  "gmaxsmite": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Smite",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Hatterene",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('confusion', source);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fairy",
    "contestType": "Cool"
  },
  "gmaxsnooze": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Snooze",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Grimmsnarl",
    "onHit": "function (target) {\n\t\t\tif (target.status || !target.runStatusImmunity('slp'))\n\t\t\t\treturn;\n\t\t\tif (this.random(2) === 0)\n\t\t\t\treturn;\n\t\t\ttarget.addVolatile('yawn');\n\t\t}",
    "onAfterSubDamage": "function (damage, target) {\n\t\t\tif (target.status || !target.runStatusImmunity('slp'))\n\t\t\t\treturn;\n\t\t\tif (this.random(2) === 0)\n\t\t\t\treturn;\n\t\t\ttarget.addVolatile('yawn');\n\t\t}",
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Dark",
    "contestType": "Cool"
  },
  "gmaxsteelsurge": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Steelsurge",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Copperajah",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('gmaxsteelsurge');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: G-Max Steelsurge');\n\t\t\t}",
      "onSwitchIn": "function (pokemon) {\n\t\t\t\tif (pokemon.hasItem('heavydutyboots'))\n\t\t\t\t\treturn;\n\t\t\t\t// Ice Face and Disguise correctly get typed damage from Stealth Rock\n\t\t\t\t// because Stealth Rock bypasses Substitute.\n\t\t\t\t// They don't get typed damage from Steelsurge because Steelsurge doesn't,\n\t\t\t\t// so we're going to test the damage of a Steel-type Stealth Rock instead.\n\t\t\t\tvar steelHazard = this.dex.getActiveMove('Stealth Rock');\n\t\t\t\tsteelHazard.type = 'Steel';\n\t\t\t\tvar typeMod = this.clampIntRange(pokemon.runEffectiveness(steelHazard), -6, 6);\n\t\t\t\tthis.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Steel",
    "contestType": "Cool"
  },
  "gmaxstonesurge": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Stonesurge",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "isMax": "Drednaw",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('stealthrock');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "gmaxstunshock": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Stun Shock",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Toxtricity",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tvar result = this.random(2);\n\t\t\t\t\tif (result === 0) {\n\t\t\t\t\t\tpokemon.trySetStatus('par', source);\n\t\t\t\t\t}\n\t\t\t\t\telse {\n\t\t\t\t\t\tpokemon.trySetStatus('psn', source);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Electric",
    "contestType": "Cool"
  },
  "gmaxsweetness": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Sweetness",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Appletun",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.pokemon; _i < _a.length; _i++) {\n\t\t\t\t\tvar ally = _a[_i];\n\t\t\t\t\tally.cureStatus();\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Grass",
    "contestType": "Cool"
  },
  "gmaxtartness": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Tartness",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Flapple",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ evasion: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Grass",
    "contestType": "Cool"
  },
  "gmaxterror": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Terror",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Gengar",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.addVolatile('trapped', source, null, 'trapper');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "gmaxvinelash": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Vine Lash",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Venusaur",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('gmaxvinelash');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'G-Max Vine Lash');\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 1,
      "onResidual": "function (target) {\n\t\t\t\tif (!target.hasType('Grass'))\n\t\t\t\t\tthis.damage(target.baseMaxhp / 6, target);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 11,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'G-Max Vine Lash');\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Grass",
    "contestType": "Cool"
  },
  "gmaxvolcalith": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Volcalith",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Coalossal",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('gmaxvolcalith');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'G-Max Volcalith');\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 1,
      "onResidual": "function (target) {\n\t\t\t\tif (!target.hasType('Rock'))\n\t\t\t\t\tthis.damage(target.baseMaxhp / 6, target);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 11,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'G-Max Volcalith');\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Rock",
    "contestType": "Cool"
  },
  "gmaxvoltcrash": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Volt Crash",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Pikachu",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tpokemon.trySetStatus('par', source);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Electric",
    "contestType": "Cool"
  },
  "gmaxwildfire": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Wildfire",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Charizard",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tfor (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {\n\t\t\t\t\tvar side = _a[_i];\n\t\t\t\t\tside.addSideCondition('gmaxwildfire');\n\t\t\t\t}\n\t\t\t}"
    },
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'G-Max Wildfire');\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 1,
      "onResidual": "function (target) {\n\t\t\t\tif (!target.hasType('Fire'))\n\t\t\t\t\tthis.damage(target.baseMaxhp / 6, target);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 11,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'G-Max Wildfire');\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Fire",
    "contestType": "Cool"
  },
  "gmaxwindrage": {
    "num": 1000,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "isNonstandard": "Gigantamax",
    "name": "G-Max Wind Rage",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": "Corviknight",
    "self": {
      "onHit": "function (source) {\n\t\t\t\tvar success = false;\n\t\t\t\tvar removeTarget = [\n\t\t\t\t\t'reflect', 'lightscreen', 'auroraveil', 'safeguard', 'mist', 'spikes', 'toxicspikes', 'stealthrock', 'stickyweb',\n\t\t\t\t];\n\t\t\t\tvar removeAll = ['spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge'];\n\t\t\t\tfor (var _i = 0, removeTarget_2 = removeTarget; _i < removeTarget_2.length; _i++) {\n\t\t\t\t\tvar targetCondition = removeTarget_2[_i];\n\t\t\t\t\tif (source.side.foe.removeSideCondition(targetCondition)) {\n\t\t\t\t\t\tif (!removeAll.includes(targetCondition))\n\t\t\t\t\t\t\tcontinue;\n\t\t\t\t\t\tthis.add('-sideend', source.side.foe, this.dex.conditions.get(targetCondition).name, '[from] move: G-Max Wind Rage', '[of] ' + source);\n\t\t\t\t\t\tsuccess = true;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tfor (var _a = 0, removeAll_2 = removeAll; _a < removeAll_2.length; _a++) {\n\t\t\t\t\tvar sideCondition = removeAll_2[_a];\n\t\t\t\t\tif (source.side.removeSideCondition(sideCondition)) {\n\t\t\t\t\t\tthis.add('-sideend', source.side, this.dex.conditions.get(sideCondition).name, '[from] move: G-Max Wind Rage', '[of] ' + source);\n\t\t\t\t\t\tsuccess = true;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tthis.field.clearTerrain();\n\t\t\t\treturn success;\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Flying",
    "contestType": "Cool"
  },
  "grassknot": {
    "num": 447,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar targetWeight = target.getWeight();\n\t\t\tif (targetWeight >= 2000) {\n\t\t\t\tthis.debug('120 bp');\n\t\t\t\treturn 120;\n\t\t\t}\n\t\t\tif (targetWeight >= 1000) {\n\t\t\t\tthis.debug('100 bp');\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (targetWeight >= 500) {\n\t\t\t\tthis.debug('80 bp');\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (targetWeight >= 250) {\n\t\t\t\tthis.debug('60 bp');\n\t\t\t\treturn 60;\n\t\t\t}\n\t\t\tif (targetWeight >= 100) {\n\t\t\t\tthis.debug('40 bp');\n\t\t\t\treturn 40;\n\t\t\t}\n\t\t\tthis.debug('20 bp');\n\t\t\treturn 20;\n\t\t}",
    "category": "Special",
    "name": "Grass Knot",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onTryHit": "function (target, source, move) {\n\t\t\tif (target.volatiles['dynamax']) {\n\t\t\t\tthis.add('-fail', source, 'move: Grass Knot', '[from] Dynamax');\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cute"
  },
  "grasspledge": {
    "num": 520,
    "accuracy": 100,
    "basePower": 80,
    "basePowerCallback": "function (target, source, move) {\n\t\t\tif (['waterpledge', 'firepledge'].includes(move.sourceEffect)) {\n\t\t\t\tthis.add('-combine');\n\t\t\t\treturn 150;\n\t\t\t}\n\t\t\treturn 80;\n\t\t}",
    "category": "Special",
    "name": "Grass Pledge",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onPrepareHit": "function (target, source, move) {\n\t\t\tvar _a;\n\t\t\tfor (var _i = 0, _b = this.queue.list; _i < _b.length; _i++) {\n\t\t\t\tvar action = _b[_i];\n\t\t\t\tif (!action.move || !((_a = action.pokemon) === null || _a === void 0 ? void 0 : _a.isActive) ||\n\t\t\t\t\taction.pokemon.fainted || action.maxMove || action.zmove) {\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (action.pokemon.isAlly(source) && ['waterpledge', 'firepledge'].includes(action.move.id)) {\n\t\t\t\t\tthis.queue.prioritizeAction(action, move);\n\t\t\t\t\tthis.add('-waiting', source, action.pokemon);\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move) {\n\t\t\tif (move.sourceEffect === 'waterpledge') {\n\t\t\t\tmove.type = 'Grass';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.sideCondition = 'grasspledge';\n\t\t\t}\n\t\t\tif (move.sourceEffect === 'firepledge') {\n\t\t\t\tmove.type = 'Fire';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.sideCondition = 'firepledge';\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'Grass Pledge');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 9,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'Grass Pledge');\n\t\t\t}",
      "onModifySpe": "function (spe, pokemon) {\n\t\t\t\treturn this.chainModify(0.25);\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "grasswhistle": {
    "num": 320,
    "accuracy": 55,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Grass Whistle",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "grassyglide": {
    "num": 803,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Grassy Glide",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mystery": 1
    },
    "onModifyPriority": "function (priority, source, target, move) {\n\t\t\tif (this.field.isTerrain('grassyterrain') && source.isGrounded()) {\n\t\t\t\treturn priority + 1;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "grassyterrain": {
    "num": 580,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Grassy Terrain",
    "pp": 10,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "terrain": "grassyterrain",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onBasePowerPriority": 6,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tvar weakenedMoves = ['earthquake', 'bulldoze', 'magnitude'];\n\t\t\t\tif (weakenedMoves.includes(move.id) && defender.isGrounded() && !defender.isSemiInvulnerable()) {\n\t\t\t\t\tthis.debug('move weakened by grassy terrain');\n\t\t\t\t\treturn this.chainModify(0.5);\n\t\t\t\t}\n\t\t\t\tif (move.type === 'Grass' && attacker.isGrounded()) {\n\t\t\t\t\tthis.debug('grassy terrain boost');\n\t\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t\t}\n\t\t\t}",
      "onFieldStart": "function (field, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Grassy Terrain', '[from] ability: ' + effect, '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Grassy Terrain');\n\t\t\t\t}\n\t\t\t}",
      "onResidualOrder": 5,
      "onResidualSubOrder": 2,
      "onResidual": "function (pokemon) {\n\t\t\t\tif (pokemon.isGrounded() && !pokemon.isSemiInvulnerable()) {\n\t\t\t\t\tthis.heal(pokemon.baseMaxhp / 16, pokemon, pokemon);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.debug(\"Pokemon semi-invuln or not grounded; Grassy Terrain skipped\");\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 7,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Grassy Terrain');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Grass",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Beautiful"
  },
  "gravapple": {
    "num": 788,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Grav Apple",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower) {\n\t\t\tif (this.field.getPseudoWeather('gravity')) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 100,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Grass"
  },
  "gravity": {
    "num": 356,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Gravity",
    "pp": 5,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "pseudoWeather": "gravity",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onFieldStart": "function () {\n\t\t\t\tthis.add('-fieldstart', 'move: Gravity');\n\t\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tvar applies = false;\n\t\t\t\t\tif (pokemon.removeVolatile('bounce') || pokemon.removeVolatile('fly')) {\n\t\t\t\t\t\tapplies = true;\n\t\t\t\t\t\tthis.queue.cancelMove(pokemon);\n\t\t\t\t\t\tpokemon.removeVolatile('twoturnmove');\n\t\t\t\t\t}\n\t\t\t\t\tif (pokemon.volatiles['skydrop']) {\n\t\t\t\t\t\tapplies = true;\n\t\t\t\t\t\tthis.queue.cancelMove(pokemon);\n\t\t\t\t\t\tif (pokemon.volatiles['skydrop'].source) {\n\t\t\t\t\t\t\tthis.add('-end', pokemon.volatiles['twoturnmove'].source, 'Sky Drop', '[interrupt]');\n\t\t\t\t\t\t}\n\t\t\t\t\t\tpokemon.removeVolatile('skydrop');\n\t\t\t\t\t\tpokemon.removeVolatile('twoturnmove');\n\t\t\t\t\t}\n\t\t\t\t\tif (pokemon.volatiles['magnetrise']) {\n\t\t\t\t\t\tapplies = true;\n\t\t\t\t\t\tdelete pokemon.volatiles['magnetrise'];\n\t\t\t\t\t}\n\t\t\t\t\tif (pokemon.volatiles['telekinesis']) {\n\t\t\t\t\t\tapplies = true;\n\t\t\t\t\t\tdelete pokemon.volatiles['telekinesis'];\n\t\t\t\t\t}\n\t\t\t\t\tif (applies)\n\t\t\t\t\t\tthis.add('-activate', pokemon, 'move: Gravity');\n\t\t\t\t}\n\t\t\t}",
      "onModifyAccuracy": "function (accuracy) {\n\t\t\t\tif (typeof accuracy !== 'number')\n\t\t\t\t\treturn;\n\t\t\t\treturn this.chainModify([6840, 4096]);\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (this.dex.moves.get(moveSlot.id).flags['gravity']) {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 6,
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tif (move.flags['gravity'] && !move.isZ) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Gravity', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onModifyMove": "function (move, pokemon, target) {\n\t\t\t\tif (move.flags['gravity'] && !move.isZ) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Gravity', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 2,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Gravity');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "growl": {
    "num": 45,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Growl",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "boosts": {
      "atk": -1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "growth": {
    "num": 74,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Growth",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onModifyMove": "function (move, pokemon) {\n\t\t\tif (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather()))\n\t\t\t\tmove.boosts = { atk: 2, spa: 2 };\n\t\t}",
    "boosts": {
      "atk": 1,
      "spa": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Beautiful"
  },
  "grudge": {
    "num": 288,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Grudge",
    "pp": 5,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "volatileStatus": "grudge",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singlemove', pokemon, 'Grudge');\n\t\t\t}",
      "onFaint": "function (target, source, effect) {\n\t\t\t\tif (!source || source.fainted || !effect)\n\t\t\t\t\treturn;\n\t\t\t\tif (effect.effectType === 'Move' && !effect.isFutureMove && source.lastMove) {\n\t\t\t\t\tvar move = source.lastMove;\n\t\t\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\t\t\tfor (var _i = 0, _a = source.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\t\tif (moveSlot.id === move.id) {\n\t\t\t\t\t\t\tmoveSlot.pp = 0;\n\t\t\t\t\t\t\tthis.add('-activate', source, 'move: Grudge', move.name);\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 100,
      "onBeforeMove": "function (pokemon) {\n\t\t\t\tthis.debug('removing Grudge before attack');\n\t\t\t\tpokemon.removeVolatile('grudge');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Ghost",
    "zMove": {
      "effect": "redirect"
    },
    "contestType": "Tough"
  },
  "guardianofalola": {
    "num": 698,
    "accuracy": true,
    "basePower": 0,
    "damageCallback": "function (pokemon, target) {\n\t\t\tvar hp75 = Math.floor(target.getUndynamaxedHP() * 3 / 4);\n\t\t\tif (target.volatiles['protect'] || target.volatiles['banefulbunker'] || target.volatiles['kingsshield'] ||\n\t\t\t\ttarget.volatiles['spikyshield'] || target.side.getSideCondition('matblock')) {\n\t\t\t\tthis.add('-zbroken', target);\n\t\t\t\treturn this.clampIntRange(Math.ceil(hp75 / 4 - 0.5), 1);\n\t\t\t}\n\t\t\treturn this.clampIntRange(hp75, 1);\n\t\t}",
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Guardian of Alola",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "tapuniumz",
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Tough"
  },
  "guardsplit": {
    "num": 470,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Guard Split",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar newdef = Math.floor((target.storedStats.def + source.storedStats.def) / 2);\n\t\t\ttarget.storedStats.def = newdef;\n\t\t\tsource.storedStats.def = newdef;\n\t\t\tvar newspd = Math.floor((target.storedStats.spd + source.storedStats.spd) / 2);\n\t\t\ttarget.storedStats.spd = newspd;\n\t\t\tsource.storedStats.spd = newspd;\n\t\t\tthis.add('-activate', source, 'move: Guard Split', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "guardswap": {
    "num": 385,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Guard Swap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar targetBoosts = {};\n\t\t\tvar sourceBoosts = {};\n\t\t\tvar defSpd = ['def', 'spd'];\n\t\t\tfor (var _i = 0, defSpd_1 = defSpd; _i < defSpd_1.length; _i++) {\n\t\t\t\tvar stat = defSpd_1[_i];\n\t\t\t\ttargetBoosts[stat] = target.boosts[stat];\n\t\t\t\tsourceBoosts[stat] = source.boosts[stat];\n\t\t\t}\n\t\t\tsource.setBoost(targetBoosts);\n\t\t\ttarget.setBoost(sourceBoosts);\n\t\t\tthis.add('-swapboost', source, target, 'def, spd', '[from] move: Guard Swap');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "guillotine": {
    "num": 12,
    "accuracy": 30,
    "basePower": 0,
    "category": "Physical",
    "name": "Guillotine",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ohko": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "gunkshot": {
    "num": 441,
    "accuracy": 80,
    "basePower": 120,
    "category": "Physical",
    "name": "Gunk Shot",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "gust": {
    "num": 16,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Gust",
    "pp": 35,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Clever"
  },
  "gyroball": {
    "num": 360,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar power = Math.floor(25 * target.getStat('spe') / pokemon.getStat('spe')) + 1;\n\t\t\tif (!isFinite(power))\n\t\t\t\tpower = 1;\n\t\t\tif (power > 150)\n\t\t\t\tpower = 150;\n\t\t\tthis.debug(power + \" bp\");\n\t\t\treturn power;\n\t\t}",
    "category": "Physical",
    "name": "Gyro Ball",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "hail": {
    "num": 258,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Hail",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "weather": "hail",
    "secondary": null,
    "target": "all",
    "type": "Ice",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "hammerarm": {
    "num": 359,
    "accuracy": 90,
    "basePower": 100,
    "category": "Physical",
    "name": "Hammer Arm",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "self": {
      "boosts": {
        "spe": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "happyhour": {
    "num": 603,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Happy Hour",
    "pp": 30,
    "priority": 0,
    "flags": {},
    "onTryHit": "function (target, source) {\n\t\t\tthis.add('-activate', target, 'move: Happy Hour');\n\t\t}",
    "secondary": null,
    "target": "allySide",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "harden": {
    "num": 106,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Harden",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "haze": {
    "num": 114,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Haze",
    "pp": 30,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "onHitField": "function () {\n\t\t\tthis.add('-clearallboost');\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tpokemon.clearBoosts();\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "all",
    "type": "Ice",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Beautiful"
  },
  "headbutt": {
    "num": 29,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Headbutt",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "headcharge": {
    "num": 543,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Head Charge",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      4
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "headsmash": {
    "num": 457,
    "accuracy": 80,
    "basePower": 150,
    "category": "Physical",
    "name": "Head Smash",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "healbell": {
    "num": 215,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Heal Bell",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "sound": 1,
      "distance": 1,
      "authentic": 1
    },
    "onHit": "function (pokemon, source) {\n\t\t\tthis.add('-activate', source, 'move: Heal Bell');\n\t\t\tvar side = pokemon.side;\n\t\t\tvar success = false;\n\t\t\tfor (var _i = 0, _a = side.pokemon; _i < _a.length; _i++) {\n\t\t\t\tvar ally = _a[_i];\n\t\t\t\tif (ally !== source && ally.hasAbility('soundproof'))\n\t\t\t\t\tcontinue;\n\t\t\t\tif (ally.cureStatus())\n\t\t\t\t\tsuccess = true;\n\t\t\t}\n\t\t\treturn success;\n\t\t}",
    "target": "allyTeam",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Beautiful"
  },
  "healblock": {
    "num": 377,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Heal Block",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "healblock",
    "condition": {
      "duration": 5,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onStart": "function (pokemon, source) {\n\t\t\t\tthis.add('-start', pokemon, 'move: Heal Block');\n\t\t\t\tsource.moveThisTurnResult = true;\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (this.dex.moves.get(moveSlot.id).flags['heal']) {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 6,
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tif (move.flags['heal'] && !move.isZ && !move.isMax) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Heal Block', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onModifyMove": "function (move, pokemon, target) {\n\t\t\t\tif (move.flags['heal'] && !move.isZ && !move.isMax) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Heal Block', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onResidualOrder": 20,
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'move: Heal Block');\n\t\t\t}",
      "onTryHeal": "function (damage, target, source, effect) {\n\t\t\t\tif (((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') || this.effectState.isZ)\n\t\t\t\t\treturn damage;\n\t\t\t\treturn false;\n\t\t\t}",
      "onRestart": "function (target, source) {\n\t\t\t\tthis.add('-fail', target, 'move: Heal Block'); // Succeeds to supress downstream messages\n\t\t\t\tif (!source.moveThisTurnResult) {\n\t\t\t\t\tsource.moveThisTurnResult = false;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 2
      }
    },
    "contestType": "Clever"
  },
  "healingwish": {
    "num": 361,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Healing Wish",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onTryHit": "function (pokemon, target, move) {\n\t\t\tif (!this.canSwitch(pokemon.side)) {\n\t\t\t\tdelete move.selfdestruct;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "selfdestruct": "ifHit",
    "slotCondition": "healingwish",
    "condition": {
      "onSwap": "function (target) {\n\t\t\t\tif (!target.fainted && (target.hp < target.maxhp || target.status)) {\n\t\t\t\t\ttarget.heal(target.maxhp);\n\t\t\t\t\ttarget.setStatus('');\n\t\t\t\t\tthis.add('-heal', target, target.getHealth, '[from] move: Healing Wish');\n\t\t\t\t\ttarget.side.removeSlotCondition(target, 'healingwish');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "contestType": "Beautiful"
  },
  "healorder": {
    "num": 456,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Heal Order",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "secondary": null,
    "target": "self",
    "type": "Bug",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "healpulse": {
    "num": 505,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Heal Pulse",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "pulse": 1,
      "reflectable": 1,
      "distance": 1,
      "heal": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar success = false;\n\t\t\tif (source.hasAbility('megalauncher')) {\n\t\t\t\tsuccess = !!this.heal(this.modify(target.baseMaxhp, 0.75));\n\t\t\t}\n\t\t\telse {\n\t\t\t\tsuccess = !!this.heal(Math.ceil(target.baseMaxhp * 0.5));\n\t\t\t}\n\t\t\tif (success && !target.isAlly(source)) {\n\t\t\t\ttarget.staleness = 'external';\n\t\t\t}\n\t\t\treturn success;\n\t\t}",
    "secondary": null,
    "target": "any",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "heartstamp": {
    "num": 531,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Heart Stamp",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cute"
  },
  "heartswap": {
    "num": 391,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Heart Swap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar targetBoosts = {};\n\t\t\tvar sourceBoosts = {};\n\t\t\tvar i;\n\t\t\tfor (i in target.boosts) {\n\t\t\t\ttargetBoosts[i] = target.boosts[i];\n\t\t\t\tsourceBoosts[i] = source.boosts[i];\n\t\t\t}\n\t\t\ttarget.setBoost(sourceBoosts);\n\t\t\tsource.setBoost(targetBoosts);\n\t\t\tthis.add('-swapboost', source, target, '[from] move: Heart Swap');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "effect": "crit2"
    },
    "contestType": "Clever"
  },
  "heatcrash": {
    "num": 535,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar targetWeight = target.getWeight();\n\t\t\tvar pokemonWeight = pokemon.getWeight();\n\t\t\tif (pokemonWeight >= targetWeight * 5) {\n\t\t\t\treturn 120;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 4) {\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 3) {\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 2) {\n\t\t\t\treturn 60;\n\t\t\t}\n\t\t\treturn 40;\n\t\t}",
    "category": "Physical",
    "name": "Heat Crash",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onTryHit": "function (target, pokemon, move) {\n\t\t\tif (target.volatiles['dynamax']) {\n\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "heatwave": {
    "num": 257,
    "accuracy": 90,
    "basePower": 95,
    "category": "Special",
    "name": "Heat Wave",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "allAdjacentFoes",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "heavyslam": {
    "num": 484,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar targetWeight = target.getWeight();\n\t\t\tvar pokemonWeight = pokemon.getWeight();\n\t\t\tif (pokemonWeight >= targetWeight * 5) {\n\t\t\t\treturn 120;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 4) {\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 3) {\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (pokemonWeight >= targetWeight * 2) {\n\t\t\t\treturn 60;\n\t\t\t}\n\t\t\treturn 40;\n\t\t}",
    "category": "Physical",
    "name": "Heavy Slam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onTryHit": "function (target, pokemon, move) {\n\t\t\tif (target.volatiles['dynamax']) {\n\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "helpinghand": {
    "num": 270,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Helping Hand",
    "pp": 20,
    "priority": 5,
    "flags": {
      "authentic": 1
    },
    "volatileStatus": "helpinghand",
    "onTryHit": "function (target) {\n\t\t\tif (!target.newlySwitched && !this.queue.willMove(target))\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target, source) {\n\t\t\t\tthis.effectState.multiplier = 1.5;\n\t\t\t\tthis.add('-singleturn', target, 'Helping Hand', '[of] ' + source);\n\t\t\t}",
      "onRestart": "function (target, source) {\n\t\t\t\tthis.effectState.multiplier *= 1.5;\n\t\t\t\tthis.add('-singleturn', target, 'Helping Hand', '[of] ' + source);\n\t\t\t}",
      "onBasePowerPriority": 10,
      "onBasePower": "function (basePower) {\n\t\t\t\tthis.debug('Boosting from Helping Hand: ' + this.effectState.multiplier);\n\t\t\t\treturn this.chainModify(this.effectState.multiplier);\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentAlly",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "hex": {
    "num": 506,
    "accuracy": 100,
    "basePower": 65,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.status || target.hasAbility('comatose'))\n\t\t\t\treturn move.basePower * 2;\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Special",
    "name": "Hex",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "zMove": {
      "basePower": 160
    },
    "contestType": "Clever"
  },
  "hiddenpower": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Hidden Power",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tmove.type = pokemon.hpType || 'Dark';\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Clever"
  },
  "hiddenpowerbug": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Bug",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Clever"
  },
  "hiddenpowerdark": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Dark",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "hiddenpowerdragon": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Dragon",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Clever"
  },
  "hiddenpowerelectric": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Electric",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Clever"
  },
  "hiddenpowerfighting": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Fighting",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Clever"
  },
  "hiddenpowerfire": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Fire",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Clever"
  },
  "hiddenpowerflying": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Flying",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "contestType": "Clever"
  },
  "hiddenpowerghost": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Ghost",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "hiddenpowergrass": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Grass",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Clever"
  },
  "hiddenpowerground": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Ground",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Clever"
  },
  "hiddenpowerice": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Ice",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Clever"
  },
  "hiddenpowerpoison": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Poison",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "contestType": "Clever"
  },
  "hiddenpowerpsychic": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Psychic",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "hiddenpowerrock": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Rock",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Clever"
  },
  "hiddenpowersteel": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Steel",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Clever"
  },
  "hiddenpowerwater": {
    "num": 237,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "realMove": "Hidden Power",
    "isNonstandard": "Past",
    "name": "Hidden Power Water",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Clever"
  },
  "highhorsepower": {
    "num": 667,
    "accuracy": 95,
    "basePower": 95,
    "category": "Physical",
    "name": "High Horsepower",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "highjumpkick": {
    "num": 136,
    "accuracy": 90,
    "basePower": 130,
    "category": "Physical",
    "name": "High Jump Kick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1
    },
    "hasCrashDamage": true,
    "onMoveFail": "function (target, source, move) {\n\t\t\tthis.damage(source.baseMaxhp / 2, source, source, this.dex.conditions.get('High Jump Kick'));\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "holdback": {
    "num": 610,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Hold Back",
    "pp": 40,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onDamagePriority": -20,
    "onDamage": "function (damage, target, source, effect) {\n\t\t\tif (damage >= target.hp)\n\t\t\t\treturn target.hp - 1;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "holdhands": {
    "num": 607,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Hold Hands",
    "pp": 40,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "secondary": null,
    "target": "adjacentAlly",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "honeclaws": {
    "num": 468,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Hone Claws",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1,
      "accuracy": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Dark",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cute"
  },
  "hornattack": {
    "num": 30,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "name": "Horn Attack",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "horndrill": {
    "num": 32,
    "accuracy": 30,
    "basePower": 0,
    "category": "Physical",
    "name": "Horn Drill",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ohko": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "hornleech": {
    "num": 532,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Horn Leech",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Tough"
  },
  "howl": {
    "num": 336,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Howl",
    "pp": 40,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "sound": 1
    },
    "boosts": {
      "atk": 1
    },
    "secondary": null,
    "target": "allies",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cool"
  },
  "hurricane": {
    "num": 542,
    "accuracy": 70,
    "basePower": 110,
    "category": "Special",
    "name": "Hurricane",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "onModifyMove": "function (move, pokemon, target) {\n\t\t\tswitch (target === null || target === void 0 ? void 0 : target.effectiveWeather()) {\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\t\tmove.accuracy = true;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tmove.accuracy = 50;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 30,
      "volatileStatus": "confusion"
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Tough"
  },
  "hydrocannon": {
    "num": 308,
    "accuracy": 90,
    "basePower": 150,
    "category": "Special",
    "name": "Hydro Cannon",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "hydropump": {
    "num": 56,
    "accuracy": 80,
    "basePower": 110,
    "category": "Special",
    "name": "Hydro Pump",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "hydrovortex": {
    "num": 642,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Hydro Vortex",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "wateriumz",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "hyperbeam": {
    "num": 63,
    "accuracy": 90,
    "basePower": 150,
    "category": "Special",
    "name": "Hyper Beam",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "hyperfang": {
    "num": 158,
    "accuracy": 90,
    "basePower": 80,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Hyper Fang",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "hyperspacefury": {
    "num": 621,
    "accuracy": true,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Hyperspace Fury",
    "pp": 5,
    "priority": 0,
    "flags": {
      "mirror": 1,
      "authentic": 1
    },
    "breaksProtect": true,
    "onTry": "function (source) {\n\t\t\tif (source.species.name === 'Hoopa-Unbound') {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.hint(\"Only a Pokemon whose form is Hoopa Unbound can use this move.\");\n\t\t\tif (source.species.name === 'Hoopa') {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('-fail', source, 'move: Hyperspace Fury', '[forme]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t\tthis.attrLastMove('[still]');\n\t\t\tthis.add('-fail', source, 'move: Hyperspace Fury');\n\t\t\treturn null;\n\t\t}",
    "self": {
      "boosts": {
        "def": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Tough"
  },
  "hyperspacehole": {
    "num": 593,
    "accuracy": true,
    "basePower": 80,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Hyperspace Hole",
    "pp": 5,
    "priority": 0,
    "flags": {
      "mirror": 1,
      "authentic": 1
    },
    "breaksProtect": true,
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "hypervoice": {
    "num": 304,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Hyper Voice",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "contestType": "Cool"
  },
  "hypnosis": {
    "num": 95,
    "accuracy": 60,
    "basePower": 0,
    "category": "Status",
    "name": "Hypnosis",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "iceball": {
    "num": 301,
    "accuracy": 90,
    "basePower": 30,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tvar bp = move.basePower;\n\t\t\tif (pokemon.volatiles['iceball'] && pokemon.volatiles['iceball'].hitCount) {\n\t\t\t\tbp *= Math.pow(2, pokemon.volatiles['iceball'].hitCount);\n\t\t\t}\n\t\t\tif (pokemon.status !== 'slp')\n\t\t\t\tpokemon.addVolatile('iceball');\n\t\t\tif (pokemon.volatiles['defensecurl']) {\n\t\t\t\tbp *= 2;\n\t\t\t}\n\t\t\tthis.debug(\"Ice Ball bp: \" + bp);\n\t\t\treturn bp;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Ice Ball",
    "pp": 20,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "condition": {
      "duration": 2,
      "onLockMove": "iceball",
      "onStart": "function () {\n\t\t\t\tthis.effectState.hitCount = 1;\n\t\t\t}",
      "onRestart": "function () {\n\t\t\t\tthis.effectState.hitCount++;\n\t\t\t\tif (this.effectState.hitCount < 5) {\n\t\t\t\t\tthis.effectState.duration = 2;\n\t\t\t\t}\n\t\t\t}",
      "onResidual": "function (target) {\n\t\t\t\tif (target.lastMove && target.lastMove.id === 'struggle') {\n\t\t\t\t\t// don't lock\n\t\t\t\t\tdelete target.volatiles['iceball'];\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "icebeam": {
    "num": 58,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Ice Beam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "iceburn": {
    "num": 554,
    "accuracy": 90,
    "basePower": 140,
    "category": "Special",
    "name": "Ice Burn",
    "pp": 5,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "icefang": {
    "num": 423,
    "accuracy": 95,
    "basePower": 65,
    "category": "Physical",
    "name": "Ice Fang",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondaries": [
      {
        "chance": 10,
        "status": "frz"
      },
      {
        "chance": 10,
        "volatileStatus": "flinch"
      }
    ],
    "target": "normal",
    "type": "Ice",
    "contestType": "Cool"
  },
  "icehammer": {
    "num": 665,
    "accuracy": 90,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Ice Hammer",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "self": {
      "boosts": {
        "spe": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Tough"
  },
  "icepunch": {
    "num": 8,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Ice Punch",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "iceshard": {
    "num": 420,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Ice Shard",
    "pp": 30,
    "priority": 1,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "iciclecrash": {
    "num": 556,
    "accuracy": 90,
    "basePower": 85,
    "category": "Physical",
    "name": "Icicle Crash",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "iciclespear": {
    "num": 333,
    "accuracy": 100,
    "basePower": 25,
    "category": "Physical",
    "name": "Icicle Spear",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Beautiful"
  },
  "icywind": {
    "num": 196,
    "accuracy": 95,
    "basePower": 55,
    "category": "Special",
    "name": "Icy Wind",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "imprison": {
    "num": 286,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Imprison",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "authentic": 1
    },
    "volatileStatus": "imprison",
    "condition": {
      "noCopy": true,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'move: Imprison');\n\t\t\t}",
      "onFoeDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = this.effectState.source.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (moveSlot.id === 'struggle')\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tpokemon.disableMove(moveSlot.id, 'hidden');\n\t\t\t\t}\n\t\t\t\tpokemon.maybeDisabled = true;\n\t\t\t}",
      "onFoeBeforeMovePriority": 4,
      "onFoeBeforeMove": "function (attacker, defender, move) {\n\t\t\t\tif (move.id !== 'struggle' && this.effectState.source.hasMove(move.id) && !move.isZ && !move.isMax) {\n\t\t\t\t\tthis.add('cant', attacker, 'move: Imprison', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "pressureTarget": "foeSide",
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 2
      }
    },
    "contestType": "Clever"
  },
  "incinerate": {
    "num": 510,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "name": "Incinerate",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (pokemon, source) {\n\t\t\tvar item = pokemon.getItem();\n\t\t\tif ((item.isBerry || item.isGem) && pokemon.takeItem(source)) {\n\t\t\t\tthis.add('-enditem', pokemon, item.name, '[from] move: Incinerate');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Fire",
    "contestType": "Tough"
  },
  "inferno": {
    "num": 517,
    "accuracy": 50,
    "basePower": 100,
    "category": "Special",
    "name": "Inferno",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "infernooverdrive": {
    "num": 640,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Inferno Overdrive",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "firiumz",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Cool"
  },
  "infestation": {
    "num": 611,
    "accuracy": 100,
    "basePower": 20,
    "category": "Special",
    "name": "Infestation",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "ingrain": {
    "num": 275,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Ingrain",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "nonsky": 1
    },
    "volatileStatus": "ingrain",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'move: Ingrain');\n\t\t\t}",
      "onResidualOrder": 7,
      "onResidual": "function (pokemon) {\n\t\t\t\tthis.heal(pokemon.baseMaxhp / 16);\n\t\t\t}",
      "onTrapPokemon": "function (pokemon) {\n\t\t\t\tpokemon.tryTrap();\n\t\t\t}",
      "onDragOut": "function (pokemon) {\n\t\t\t\tthis.add('-activate', pokemon, 'move: Ingrain');\n\t\t\t\treturn null;\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Grass",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "instruct": {
    "num": 689,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Instruct",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (!target.lastMove || target.volatiles['dynamax'])\n\t\t\t\treturn false;\n\t\t\tvar lastMove = target.lastMove;\n\t\t\tvar moveIndex = target.moves.indexOf(lastMove.id);\n\t\t\tvar noInstruct = [\n\t\t\t\t'assist', 'beakblast', 'belch', 'bide', 'celebrate', 'copycat', 'dynamaxcannon', 'focuspunch', 'iceball', 'instruct', 'kingsshield', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'obstruct', 'outrage', 'petaldance', 'rollout', 'shelltrap', 'sketch', 'sleeptalk', 'struggle', 'thrash', 'transform', 'uproar',\n\t\t\t];\n\t\t\tif (noInstruct.includes(lastMove.id) || lastMove.isZ || lastMove.isMax ||\n\t\t\t\tlastMove.flags['charge'] || lastMove.flags['recharge'] ||\n\t\t\t\ttarget.volatiles['beakblast'] || target.volatiles['focuspunch'] || target.volatiles['shelltrap'] ||\n\t\t\t\t(target.moveSlots[moveIndex] && target.moveSlots[moveIndex].pp <= 0)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.add('-singleturn', target, 'move: Instruct', '[of] ' + source);\n\t\t\tthis.actions.runMove(target.lastMove.id, target, target.lastMoveTargetLoc);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "iondeluge": {
    "num": 569,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Ion Deluge",
    "pp": 25,
    "priority": 1,
    "flags": {},
    "pseudoWeather": "iondeluge",
    "condition": {
      "duration": 1,
      "onStart": "function (target, source, sourceEffect) {\n\t\t\t\tthis.add('-fieldactivate', 'move: Ion Deluge');\n\t\t\t\tthis.hint(\"Normal-type moves become Electric-type after using \" + sourceEffect + \".\");\n\t\t\t}",
      "onModifyTypePriority": -2,
      "onModifyType": "function (move) {\n\t\t\t\tif (move.type === 'Normal') {\n\t\t\t\t\tmove.type = 'Electric';\n\t\t\t\t\tthis.debug(move.name + \"'s type changed to Electric\");\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Beautiful"
  },
  "irondefense": {
    "num": 334,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Iron Defense",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Steel",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "ironhead": {
    "num": 442,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Iron Head",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Tough"
  },
  "irontail": {
    "num": 231,
    "accuracy": 75,
    "basePower": 100,
    "category": "Physical",
    "name": "Iron Tail",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "jawlock": {
    "num": 746,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Jaw Lock",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tsource.addVolatile('trapped', target, move, 'trapper');\n\t\t\ttarget.addVolatile('trapped', source, move, 'trapper');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark"
  },
  "judgment": {
    "num": 449,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Judgment",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (pokemon.ignoringItem())\n\t\t\t\treturn;\n\t\t\tvar item = pokemon.getItem();\n\t\t\tif (item.id && item.onPlate && !item.zMove) {\n\t\t\t\tmove.type = item.onPlate;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "jumpkick": {
    "num": 26,
    "accuracy": 95,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Jump Kick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1
    },
    "hasCrashDamage": true,
    "onMoveFail": "function (target, source, move) {\n\t\t\tthis.damage(source.baseMaxhp / 2, source, source, this.dex.conditions.get('Jump Kick'));\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "junglehealing": {
    "num": 816,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Jungle Healing",
    "pp": 10,
    "priority": 0,
    "flags": {
      "heal": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tvar success = !!this.heal(this.modify(pokemon.maxhp, 0.25));\n\t\t\treturn pokemon.cureStatus() || success;\n\t\t}",
    "secondary": null,
    "target": "allies",
    "type": "Grass"
  },
  "karatechop": {
    "num": 2,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Karate Chop",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "kinesis": {
    "num": 134,
    "accuracy": 80,
    "basePower": 0,
    "category": "Status",
    "name": "Kinesis",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "accuracy": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Clever"
  },
  "kingsshield": {
    "num": 588,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "King's Shield",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "kingsshield",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'Protect');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect'] || move.category === 'Status') {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Protect');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.boost({ atk: -1 }, source, target, this.dex.getActiveMove(\"King's Shield\"));\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.boost({ atk: -1 }, source, target, this.dex.getActiveMove(\"King's Shield\"));\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Steel",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cool"
  },
  "knockoff": {
    "num": 282,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "name": "Knock Off",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, source, target, move) {\n\t\t\tvar item = target.getItem();\n\t\t\tif (!this.singleEvent('TakeItem', item, target.itemState, target, target, move, item))\n\t\t\t\treturn;\n\t\t\tif (item.id) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
    "onAfterHit": "function (target, source) {\n\t\t\tif (source.hp) {\n\t\t\t\tvar item = target.takeItem();\n\t\t\t\tif (item) {\n\t\t\t\t\tthis.add('-enditem', target, item.name, '[from] move: Knock Off', '[of] ' + source);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "landswrath": {
    "num": 616,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Land's Wrath",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Ground",
    "zMove": {
      "basePower": 185
    },
    "contestType": "Beautiful"
  },
  "laserfocus": {
    "num": 673,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Laser Focus",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "laserfocus",
    "condition": {
      "duration": 2,
      "onStart": "function (pokemon, source, effect) {\n\t\t\t\tif (effect && (['imposter', 'psychup', 'transform'].includes(effect.id))) {\n\t\t\t\t\tthis.add('-start', pokemon, 'move: Laser Focus', '[silent]');\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-start', pokemon, 'move: Laser Focus');\n\t\t\t\t}\n\t\t\t}",
      "onRestart": "function (pokemon) {\n\t\t\t\tthis.effectState.duration = 2;\n\t\t\t\tthis.add('-start', pokemon, 'move: Laser Focus');\n\t\t\t}",
      "onModifyCritRatio": "function (critRatio) {\n\t\t\t\treturn 5;\n\t\t\t}",
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'move: Laser Focus', '[silent]');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cool"
  },
  "lashout": {
    "num": 808,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Lash Out",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, source) {\n\t\t\tif (source.statsLoweredThisTurn) {\n\t\t\t\tthis.debug('lashout buff');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark"
  },
  "lastresort": {
    "num": 387,
    "accuracy": 100,
    "basePower": 140,
    "category": "Physical",
    "name": "Last Resort",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.moveSlots.length < 2)\n\t\t\t\treturn false; // Last Resort fails unless the user knows at least 2 moves\n\t\t\tvar hasLastResort = false; // User must actually have Last Resort for it to succeed\n\t\t\tfor (var _i = 0, _a = source.moveSlots; _i < _a.length; _i++) {\n\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\tif (moveSlot.id === 'lastresort') {\n\t\t\t\t\thasLastResort = true;\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (!moveSlot.used)\n\t\t\t\t\treturn false;\n\t\t\t}\n\t\t\treturn hasLastResort;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "lavaplume": {
    "num": 436,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Lava Plume",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "allAdjacent",
    "type": "Fire",
    "contestType": "Tough"
  },
  "leafage": {
    "num": 670,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Leafage",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Tough"
  },
  "leafblade": {
    "num": 348,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Leaf Blade",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "leafstorm": {
    "num": 437,
    "accuracy": 90,
    "basePower": 130,
    "category": "Special",
    "name": "Leaf Storm",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spa": -2
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "leaftornado": {
    "num": 536,
    "accuracy": 90,
    "basePower": 65,
    "category": "Special",
    "name": "Leaf Tornado",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "leechlife": {
    "num": 141,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Leech Life",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Clever"
  },
  "leechseed": {
    "num": 73,
    "accuracy": 90,
    "basePower": 0,
    "category": "Status",
    "name": "Leech Seed",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "leechseed",
    "condition": {
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'move: Leech Seed');\n\t\t\t}",
      "onResidualOrder": 8,
      "onResidual": "function (pokemon) {\n\t\t\t\tvar target = this.getAtSlot(pokemon.volatiles['leechseed'].sourceSlot);\n\t\t\t\tif (!target || target.fainted || target.hp <= 0) {\n\t\t\t\t\tthis.debug('Nothing to leech into');\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tvar damage = this.damage(pokemon.baseMaxhp / 8, pokemon, target);\n\t\t\t\tif (damage) {\n\t\t\t\t\tthis.heal(damage, target, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "onTryImmunity": "function (target) {\n\t\t\treturn !target.hasType('Grass');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "leer": {
    "num": 43,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Leer",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "def": -1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cool"
  },
  "letssnuggleforever": {
    "num": 726,
    "accuracy": true,
    "basePower": 190,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Let's Snuggle Forever",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "mimikiumz",
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Cool"
  },
  "lick": {
    "num": 122,
    "accuracy": 100,
    "basePower": 30,
    "category": "Physical",
    "name": "Lick",
    "pp": 30,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cute"
  },
  "lifedew": {
    "num": 791,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Life Dew",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1,
      "authentic": 1
    },
    "heal": [
      1,
      4
    ],
    "secondary": null,
    "target": "allies",
    "type": "Water"
  },
  "lightofruin": {
    "num": 617,
    "accuracy": 90,
    "basePower": 140,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Light of Ruin",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Beautiful"
  },
  "lightscreen": {
    "num": 113,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Light Screen",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "lightscreen",
    "condition": {
      "duration": 5,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('lightclay')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onAnyModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (target !== source && this.effectState.target.hasAlly(target) && this.getCategory(move) === 'Special') {\n\t\t\t\t\tif (!target.getMoveHitData(move).crit && !move.infiltrates) {\n\t\t\t\t\t\tthis.debug('Light Screen weaken');\n\t\t\t\t\t\tif (this.activePerHalf > 1)\n\t\t\t\t\t\t\treturn this.chainModify([2732, 4096]);\n\t\t\t\t\t\treturn this.chainModify(0.5);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Light Screen');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 2,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'move: Light Screen');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Beautiful"
  },
  "lightthatburnsthesky": {
    "num": 723,
    "accuracy": true,
    "basePower": 200,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Light That Burns the Sky",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "onModifyMove": "function (move, pokemon) {\n\t\t\tif (pokemon.getStat('atk', false, true) > pokemon.getStat('spa', false, true))\n\t\t\t\tmove.category = 'Physical';\n\t\t}",
    "ignoreAbility": true,
    "isZ": "ultranecroziumz",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "liquidation": {
    "num": 710,
    "accuracy": 100,
    "basePower": 85,
    "category": "Physical",
    "name": "Liquidation",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "lockon": {
    "num": 199,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Lock-On",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, source) {\n\t\t\tif (source.volatiles['lockon'])\n\t\t\t\treturn false;\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tsource.addVolatile('lockon', target);\n\t\t\tthis.add('-activate', source, 'move: Lock-On', '[of] ' + target);\n\t\t}",
    "condition": {
      "noCopy": true,
      "duration": 2,
      "onSourceInvulnerabilityPriority": 1,
      "onSourceInvulnerability": "function (target, source, move) {\n\t\t\t\tif (move && source === this.effectState.target && target === this.effectState.source)\n\t\t\t\t\treturn 0;\n\t\t\t}",
      "onSourceAccuracy": "function (accuracy, target, source, move) {\n\t\t\t\tif (move && source === this.effectState.target && target === this.effectState.source)\n\t\t\t\t\treturn true;\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "lovelykiss": {
    "num": 142,
    "accuracy": 75,
    "basePower": 0,
    "category": "Status",
    "name": "Lovely Kiss",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "lowkick": {
    "num": 67,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar targetWeight = target.getWeight();\n\t\t\tif (targetWeight >= 2000) {\n\t\t\t\treturn 120;\n\t\t\t}\n\t\t\tif (targetWeight >= 1000) {\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (targetWeight >= 500) {\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (targetWeight >= 250) {\n\t\t\t\treturn 60;\n\t\t\t}\n\t\t\tif (targetWeight >= 100) {\n\t\t\t\treturn 40;\n\t\t\t}\n\t\t\treturn 20;\n\t\t}",
    "category": "Physical",
    "name": "Low Kick",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, pokemon, move) {\n\t\t\tif (target.volatiles['dynamax']) {\n\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "zMove": {
      "basePower": 160
    },
    "contestType": "Tough"
  },
  "lowsweep": {
    "num": 490,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "name": "Low Sweep",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Clever"
  },
  "luckychant": {
    "num": 381,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Lucky Chant",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "luckychant",
    "condition": {
      "duration": 5,
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Lucky Chant'); // \"The Lucky Chant shielded [side.name]'s team from critical hits!\"\n\t\t\t}",
      "onCriticalHit": false,
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 6,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'move: Lucky Chant'); // \"[side.name]'s team's Lucky Chant wore off!\"\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Normal",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Cute"
  },
  "lunardance": {
    "num": 461,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Lunar Dance",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1,
      "dance": 1
    },
    "onTryHit": "function (pokemon, target, move) {\n\t\t\tif (!this.canSwitch(pokemon.side)) {\n\t\t\t\tdelete move.selfdestruct;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "selfdestruct": "ifHit",
    "slotCondition": "lunardance",
    "condition": {
      "onSwap": "function (target) {\n\t\t\t\tif (!target.fainted && (target.hp < target.maxhp ||\n\t\t\t\t\ttarget.status ||\n\t\t\t\t\ttarget.moveSlots.some(function (moveSlot) { return moveSlot.pp < moveSlot.maxpp; }))) {\n\t\t\t\t\ttarget.heal(target.maxhp);\n\t\t\t\t\ttarget.setStatus('');\n\t\t\t\t\tfor (var _i = 0, _a = target.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\t\tmoveSlot.pp = moveSlot.maxpp;\n\t\t\t\t\t}\n\t\t\t\t\tthis.add('-heal', target, target.getHealth, '[from] move: Lunar Dance');\n\t\t\t\t\ttarget.side.removeSlotCondition(target, 'lunardance');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "contestType": "Beautiful"
  },
  "lunge": {
    "num": 679,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Lunge",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "atk": -1
      }
    },
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "lusterpurge": {
    "num": 295,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Luster Purge",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "machpunch": {
    "num": 183,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Mach Punch",
    "pp": 30,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "magicalleaf": {
    "num": 345,
    "accuracy": true,
    "basePower": 60,
    "category": "Special",
    "name": "Magical Leaf",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "magiccoat": {
    "num": 277,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Magic Coat",
    "pp": 15,
    "priority": 4,
    "flags": {},
    "volatileStatus": "magiccoat",
    "condition": {
      "duration": 1,
      "onStart": "function (target, source, effect) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Magic Coat');\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Move') {\n\t\t\t\t\tthis.effectState.pranksterBoosted = effect.pranksterBoosted;\n\t\t\t\t}\n\t\t\t}",
      "onTryHitPriority": 2,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (target === source || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\t\tnewMove.hasBounced = true;\n\t\t\t\tnewMove.pranksterBoosted = this.effectState.pranksterBoosted;\n\t\t\t\tthis.actions.useMove(newMove, target, source);\n\t\t\t\treturn null;\n\t\t\t}",
      "onAllyTryHitSide": "function (target, source, move) {\n\t\t\t\tif (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tvar newMove = this.dex.getActiveMove(move.id);\n\t\t\t\tnewMove.hasBounced = true;\n\t\t\t\tnewMove.pranksterBoosted = false;\n\t\t\t\tthis.actions.useMove(newMove, this.effectState.target, source);\n\t\t\t\treturn null;\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 2
      }
    },
    "contestType": "Beautiful"
  },
  "magicpowder": {
    "num": 750,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Magic Powder",
    "pp": 20,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.getTypes().join() === 'Psychic' || !target.setType('Psychic'))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', target, 'typechange', 'Psychic');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic"
  },
  "magicroom": {
    "num": 478,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Magic Room",
    "pp": 10,
    "priority": 0,
    "flags": {
      "mirror": 1
    },
    "pseudoWeather": "magicroom",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onFieldStart": "function (target, source) {\n\t\t\t\tthis.add('-fieldstart', 'move: Magic Room', '[of] ' + source);\n\t\t\t}",
      "onFieldRestart": "function (target, source) {\n\t\t\t\tthis.field.removePseudoWeather('magicroom');\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 6,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Magic Room', '[of] ' + this.effectState.source);\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "magmastorm": {
    "num": 463,
    "accuracy": 75,
    "basePower": 100,
    "category": "Special",
    "name": "Magma Storm",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Tough"
  },
  "magnetbomb": {
    "num": 443,
    "accuracy": true,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Magnet Bomb",
    "pp": 20,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "magneticflux": {
    "num": 602,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Magnetic Flux",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "distance": 1,
      "authentic": 1
    },
    "onHitSide": "function (side, source, move) {\n\t\t\tvar _this = this;\n\t\t\tvar targets = side.allies().filter(function (ally) { return (ally.hasAbility(['plus', 'minus']) &&\n\t\t\t\t(!ally.volatiles['maxguard'] || _this.runEvent('TryHit', ally, source, move))); });\n\t\t\tif (!targets.length)\n\t\t\t\treturn false;\n\t\t\tvar didSomething = false;\n\t\t\tfor (var _i = 0, targets_3 = targets; _i < targets_3.length; _i++) {\n\t\t\t\tvar target = targets_3[_i];\n\t\t\t\tdidSomething = this.boost({ def: 1, spd: 1 }, target, source, move, false, true) || didSomething;\n\t\t\t}\n\t\t\treturn didSomething;\n\t\t}",
    "secondary": null,
    "target": "allySide",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "magnetrise": {
    "num": 393,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Magnet Rise",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "gravity": 1
    },
    "volatileStatus": "magnetrise",
    "onTry": "function (source, target, move) {\n\t\t\tif (target.volatiles['smackdown'] || target.volatiles['ingrain'])\n\t\t\t\treturn false;\n\t\t\t// Additional Gravity check for Z-move variant\n\t\t\tif (this.field.getPseudoWeather('Gravity')) {\n\t\t\t\tthis.add('cant', source, 'move: Gravity', move);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 5,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'Magnet Rise');\n\t\t\t}",
      "onImmunity": "function (type) {\n\t\t\t\tif (type === 'Ground')\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onResidualOrder": 18,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Magnet Rise');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Electric",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Clever"
  },
  "magnitude": {
    "num": 222,
    "accuracy": 100,
    "basePower": 0,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Magnitude",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onModifyMove": "function (move, pokemon) {\n\t\t\tvar i = this.random(100);\n\t\t\tif (i < 5) {\n\t\t\t\tmove.magnitude = 4;\n\t\t\t\tmove.basePower = 10;\n\t\t\t}\n\t\t\telse if (i < 15) {\n\t\t\t\tmove.magnitude = 5;\n\t\t\t\tmove.basePower = 30;\n\t\t\t}\n\t\t\telse if (i < 35) {\n\t\t\t\tmove.magnitude = 6;\n\t\t\t\tmove.basePower = 50;\n\t\t\t}\n\t\t\telse if (i < 65) {\n\t\t\t\tmove.magnitude = 7;\n\t\t\t\tmove.basePower = 70;\n\t\t\t}\n\t\t\telse if (i < 85) {\n\t\t\t\tmove.magnitude = 8;\n\t\t\t\tmove.basePower = 90;\n\t\t\t}\n\t\t\telse if (i < 95) {\n\t\t\t\tmove.magnitude = 9;\n\t\t\t\tmove.basePower = 110;\n\t\t\t}\n\t\t\telse {\n\t\t\t\tmove.magnitude = 10;\n\t\t\t\tmove.basePower = 150;\n\t\t\t}\n\t\t}",
    "onUseMoveMessage": "function (pokemon, target, move) {\n\t\t\tthis.add('-activate', pokemon, 'move: Magnitude', move.magnitude);\n\t\t}",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Ground",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 140
    },
    "contestType": "Tough"
  },
  "maliciousmoonsault": {
    "num": 696,
    "accuracy": true,
    "basePower": 180,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Malicious Moonsault",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "inciniumz",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Cool"
  },
  "matblock": {
    "num": 561,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Mat Block",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "nonsky": 1
    },
    "stallingMove": true,
    "sideCondition": "matblock",
    "onTry": "function (source) {\n\t\t\tif (source.activeMoveActions > 1) {\n\t\t\t\tthis.hint(\"Mat Block only works on your first turn out.\");\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\treturn !!this.queue.willAct();\n\t\t}",
    "condition": {
      "duration": 1,
      "onSideStart": "function (target, source) {\n\t\t\t\tthis.add('-singleturn', source, 'Mat Block');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect']) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move && (move.target === 'self' || move.category === 'Status'))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-activate', target, 'move: Mat Block', move.name);\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Fighting",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cool"
  },
  "maxairstream": {
    "num": 766,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Airstream",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spe: 1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Flying",
    "contestType": "Cool"
  },
  "maxdarkness": {
    "num": 772,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Darkness",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spd: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Dark",
    "contestType": "Cool"
  },
  "maxflare": {
    "num": 757,
    "accuracy": true,
    "basePower": 100,
    "category": "Physical",
    "name": "Max Flare",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setWeather('sunnyday');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Fire",
    "contestType": "Cool"
  },
  "maxflutterby": {
    "num": 758,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Flutterby",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spa: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Bug",
    "contestType": "Cool"
  },
  "maxgeyser": {
    "num": 765,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Geyser",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setWeather('raindance');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Water",
    "contestType": "Cool"
  },
  "maxguard": {
    "num": 743,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Max Guard",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "isMax": true,
    "stallingMove": true,
    "volatileStatus": "maxguard",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'Max Guard');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\treturn;\n\t\t\t\t/** moves blocked by Max Guard but not Protect */\n\t\t\t\tvar overrideBypassProtect = [\n\t\t\t\t\t'block', 'flowershield', 'gearup', 'magneticflux', 'phantomforce', 'psychup', 'shadowforce', 'teatime', 'transform',\n\t\t\t\t];\n\t\t\t\tvar blockedByMaxGuard = (this.dex.moves.get(move.id).flags['protect'] ||\n\t\t\t\t\tmove.isZ || move.isMax || overrideBypassProtect.includes(move.id));\n\t\t\t\tif (!blockedByMaxGuard) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Max Guard');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "contestType": "Cool"
  },
  "maxhailstorm": {
    "num": 763,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Hailstorm",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setWeather('hail');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Ice",
    "contestType": "Cool"
  },
  "maxknuckle": {
    "num": 761,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Knuckle",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ atk: 1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "maxlightning": {
    "num": 759,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Lightning",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setTerrain('electricterrain');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Electric",
    "contestType": "Cool"
  },
  "maxmindstorm": {
    "num": 769,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Mindstorm",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setTerrain('psychicterrain');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "maxooze": {
    "num": 764,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Ooze",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spa: 1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Poison",
    "contestType": "Cool"
  },
  "maxovergrowth": {
    "num": 773,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Overgrowth",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setTerrain('grassyterrain');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Grass",
    "contestType": "Cool"
  },
  "maxphantasm": {
    "num": 762,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Phantasm",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ def: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "maxquake": {
    "num": 771,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Quake",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spd: 1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Ground",
    "contestType": "Cool"
  },
  "maxrockfall": {
    "num": 770,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Rockfall",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setWeather('sandstorm');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Rock",
    "contestType": "Cool"
  },
  "maxstarfall": {
    "num": 767,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Starfall",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tthis.field.setTerrain('mistyterrain');\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Fairy",
    "contestType": "Cool"
  },
  "maxsteelspike": {
    "num": 774,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Steelspike",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ def: 1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Steel",
    "contestType": "Cool"
  },
  "maxstrike": {
    "num": 760,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Strike",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ spe: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Normal",
    "contestType": "Cool"
  },
  "maxwyrmwind": {
    "num": 768,
    "accuracy": true,
    "basePower": 10,
    "category": "Physical",
    "name": "Max Wyrmwind",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "isMax": true,
    "self": {
      "onHit": "function (source) {\n\t\t\t\tif (!source.volatiles['dynamax'])\n\t\t\t\t\treturn;\n\t\t\t\tfor (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {\n\t\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\t\tthis.boost({ atk: -1 }, pokemon);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "adjacentFoe",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "meanlook": {
    "num": 212,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Mean Look",
    "pp": 5,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\treturn target.addVolatile('trapped', source, move, 'trapper');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Beautiful"
  },
  "meditate": {
    "num": 96,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Meditate",
    "pp": 40,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Beautiful"
  },
  "mefirst": {
    "num": 382,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Me First",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "authentic": 1
    },
    "onTryHit": "function (target, pokemon) {\n\t\t\tvar action = this.queue.willMove(target);\n\t\t\tif (!action)\n\t\t\t\treturn false;\n\t\t\tvar noMeFirst = [\n\t\t\t\t'beakblast', 'chatter', 'counter', 'covet', 'focuspunch', 'mefirst', 'metalburst', 'mirrorcoat', 'shelltrap', 'struggle', 'thief',\n\t\t\t];\n\t\t\tvar move = this.dex.getActiveMove(action.move.id);\n\t\t\tif (action.zmove || move.isZ || move.isMax)\n\t\t\t\treturn false;\n\t\t\tif (target.volatiles['mustrecharge'])\n\t\t\t\treturn false;\n\t\t\tif (move.category === 'Status' || noMeFirst.includes(move.id))\n\t\t\t\treturn false;\n\t\t\tpokemon.addVolatile('mefirst');\n\t\t\tthis.actions.useMove(move, pokemon, target);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 1,
      "onBasePowerPriority": 12,
      "onBasePower": "function (basePower) {\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}"
    },
    "secondary": null,
    "target": "adjacentFoe",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "megadrain": {
    "num": 72,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Mega Drain",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "basePower": 120
    },
    "contestType": "Clever"
  },
  "megahorn": {
    "num": 224,
    "accuracy": 85,
    "basePower": 120,
    "category": "Physical",
    "name": "Megahorn",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cool"
  },
  "megakick": {
    "num": 25,
    "accuracy": 75,
    "basePower": 120,
    "category": "Physical",
    "name": "Mega Kick",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "megapunch": {
    "num": 5,
    "accuracy": 85,
    "basePower": 80,
    "category": "Physical",
    "name": "Mega Punch",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "memento": {
    "num": 262,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Memento",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "boosts": {
      "atk": -2,
      "spa": -2
    },
    "selfdestruct": "ifHit",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "effect": "healreplacement"
    },
    "contestType": "Tough"
  },
  "menacingmoonrazemaelstrom": {
    "num": 725,
    "accuracy": true,
    "basePower": 200,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Menacing Moonraze Maelstrom",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "lunaliumz",
    "ignoreAbility": true,
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "metalburst": {
    "num": 368,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon) {\n\t\t\tvar lastDamagedBy = pokemon.getLastDamagedBy(true);\n\t\t\tif (lastDamagedBy !== undefined) {\n\t\t\t\treturn (lastDamagedBy.damage * 1.5) || 1;\n\t\t\t}\n\t\t\treturn 0;\n\t\t}",
    "category": "Physical",
    "name": "Metal Burst",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, source, move) {\n\t\t\tvar lastDamagedBy = source.getLastDamagedBy(true);\n\t\t\tif (lastDamagedBy === undefined || !lastDamagedBy.thisTurn)\n\t\t\t\treturn false;\n\t\t}",
    "onModifyTarget": "function (targetRelayVar, source, target, move) {\n\t\t\tvar lastDamagedBy = source.getLastDamagedBy(true);\n\t\t\tif (lastDamagedBy) {\n\t\t\t\ttargetRelayVar.target = this.getAtSlot(lastDamagedBy.slot);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "scripted",
    "type": "Steel",
    "contestType": "Cool"
  },
  "metalclaw": {
    "num": 232,
    "accuracy": 95,
    "basePower": 50,
    "category": "Physical",
    "name": "Metal Claw",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "self": {
        "boosts": {
          "atk": 1
        }
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "metalsound": {
    "num": 319,
    "accuracy": 85,
    "basePower": 0,
    "category": "Status",
    "name": "Metal Sound",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1,
      "mystery": 1
    },
    "boosts": {
      "spd": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "meteorassault": {
    "num": 794,
    "accuracy": 100,
    "basePower": 150,
    "category": "Physical",
    "name": "Meteor Assault",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "recharge": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting"
  },
  "meteorbeam": {
    "num": 800,
    "accuracy": 90,
    "basePower": 120,
    "category": "Special",
    "name": "Meteor Beam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tthis.boost({ spa: 1 }, attacker, attacker, move);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Rock"
  },
  "meteormash": {
    "num": 309,
    "accuracy": 90,
    "basePower": 90,
    "category": "Physical",
    "name": "Meteor Mash",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 20,
      "self": {
        "boosts": {
          "atk": 1
        }
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "metronome": {
    "num": 118,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Metronome",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "noMetronome": [
      "After You",
      "Apple Acid",
      "Assist",
      "Astral Barrage",
      "Aura Wheel",
      "Baneful Bunker",
      "Beak Blast",
      "Behemoth Bash",
      "Behemoth Blade",
      "Belch",
      "Bestow",
      "Body Press",
      "Branch Poke",
      "Breaking Swipe",
      "Celebrate",
      "Chatter",
      "Clangorous Soul",
      "Copycat",
      "Counter",
      "Covet",
      "Crafty Shield",
      "Decorate",
      "Destiny Bond",
      "Detect",
      "Diamond Storm",
      "Double Iron Bash",
      "Dragon Ascent",
      "Dragon Energy",
      "Drum Beating",
      "Dynamax Cannon",
      "Endure",
      "Eternabeam",
      "False Surrender",
      "Feint",
      "Fiery Wrath",
      "Fleur Cannon",
      "Focus Punch",
      "Follow Me",
      "Freeze Shock",
      "Freezing Glare",
      "Glacial Lance",
      "Grav Apple",
      "Helping Hand",
      "Hold Hands",
      "Hyperspace Fury",
      "Hyperspace Hole",
      "Ice Burn",
      "Instruct",
      "Jungle Healing",
      "King's Shield",
      "Life Dew",
      "Light of Ruin",
      "Mat Block",
      "Me First",
      "Meteor Assault",
      "Metronome",
      "Mimic",
      "Mind Blown",
      "Mirror Coat",
      "Mirror Move",
      "Moongeist Beam",
      "Nature Power",
      "Nature's Madness",
      "Obstruct",
      "Origin Pulse",
      "Overdrive",
      "Photon Geyser",
      "Plasma Fists",
      "Precipice Blades",
      "Protect",
      "Pyro Ball",
      "Quash",
      "Quick Guard",
      "Rage Powder",
      "Relic Song",
      "Secret Sword",
      "Shell Trap",
      "Sketch",
      "Sleep Talk",
      "Snap Trap",
      "Snarl",
      "Snatch",
      "Snore",
      "Spectral Thief",
      "Spiky Shield",
      "Spirit Break",
      "Spotlight",
      "Steam Eruption",
      "Steel Beam",
      "Strange Steam",
      "Struggle",
      "Sunsteel Strike",
      "Surging Strikes",
      "Switcheroo",
      "Techno Blast",
      "Thief",
      "Thousand Arrows",
      "Thousand Waves",
      "Thunder Cage",
      "Thunderous Kick",
      "Transform",
      "Trick",
      "V-create",
      "Wicked Blow",
      "Wide Guard"
    ],
    "onHit": "function (target, source, effect) {\n\t\t\tvar moves = [];\n\t\t\tfor (var id in exports.Moves) {\n\t\t\t\tvar move = exports.Moves[id];\n\t\t\t\tif (move.realMove)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (move.isZ || move.isMax || move.isNonstandard)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (effect.noMetronome.includes(move.name))\n\t\t\t\t\tcontinue;\n\t\t\t\tif (this.dex.moves.get(id).gen > this.gen)\n\t\t\t\t\tcontinue;\n\t\t\t\tmoves.push(move);\n\t\t\t}\n\t\t\tvar randomMove = '';\n\t\t\tif (moves.length) {\n\t\t\t\tmoves.sort(function (a, b) { return a.num - b.num; });\n\t\t\t\trandomMove = this.sample(moves).name;\n\t\t\t}\n\t\t\tif (!randomMove) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.actions.useMove(randomMove, target);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "contestType": "Cute"
  },
  "milkdrink": {
    "num": 208,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Milk Drink",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "mimic": {
    "num": 102,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Mimic",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar disallowedMoves = ['chatter', 'mimic', 'sketch', 'struggle', 'transform'];\n\t\t\tvar move = target.lastMove;\n\t\t\tif (source.transformed || !move || disallowedMoves.includes(move.id) || source.moves.includes(move.id)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tif (move.isZ || move.isMax)\n\t\t\t\treturn false;\n\t\t\tvar mimicIndex = source.moves.indexOf('mimic');\n\t\t\tif (mimicIndex < 0)\n\t\t\t\treturn false;\n\t\t\tsource.moveSlots[mimicIndex] = {\n\t\t\t\tmove: move.name,\n\t\t\t\tid: move.id,\n\t\t\t\tpp: move.pp,\n\t\t\t\tmaxpp: move.pp,\n\t\t\t\ttarget: move.target,\n\t\t\t\tdisabled: false,\n\t\t\t\tused: false,\n\t\t\t\tvirtual: true,\n\t\t\t};\n\t\t\tthis.add('-start', source, 'Mimic', move.name);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cute"
  },
  "mindblown": {
    "num": 720,
    "accuracy": 100,
    "basePower": 150,
    "category": "Special",
    "name": "Mind Blown",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "mindBlownRecoil": true,
    "onAfterMove": "function (pokemon, target, move) {\n\t\t\tif (move.mindBlownRecoil && !move.multihit) {\n\t\t\t\tthis.damage(Math.round(pokemon.maxhp / 2), pokemon, pokemon, this.dex.conditions.get('Mind Blown'), true);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Fire",
    "contestType": "Cool"
  },
  "mindreader": {
    "num": 170,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Mind Reader",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, source) {\n\t\t\tif (source.volatiles['lockon'])\n\t\t\t\treturn false;\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tsource.addVolatile('lockon', target);\n\t\t\tthis.add('-activate', source, 'move: Mind Reader', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "minimize": {
    "num": 107,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Minimize",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "minimize",
    "condition": {
      "noCopy": true,
      "onSourceModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tvar boostedMoves = [\n\t\t\t\t\t'stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault',\n\t\t\t\t];\n\t\t\t\tif (boostedMoves.includes(move.id)) {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}",
      "onAccuracy": "function (accuracy, target, source, move) {\n\t\t\t\tvar boostedMoves = [\n\t\t\t\t\t'stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault',\n\t\t\t\t];\n\t\t\t\tif (boostedMoves.includes(move.id)) {\n\t\t\t\t\treturn true;\n\t\t\t\t}\n\t\t\t\treturn accuracy;\n\t\t\t}"
    },
    "boosts": {
      "evasion": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "miracleeye": {
    "num": 357,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Miracle Eye",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "miracleeye",
    "onTryHit": "function (target) {\n\t\t\tif (target.volatiles['foresight'])\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Miracle Eye');\n\t\t\t}",
      "onNegateImmunity": "function (pokemon, type) {\n\t\t\t\tif (pokemon.hasType('Dark') && type === 'Psychic')\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onModifyBoost": "function (boosts) {\n\t\t\t\tif (boosts.evasion && boosts.evasion > 0) {\n\t\t\t\t\tboosts.evasion = 0;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "mirrorcoat": {
    "num": 243,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon) {\n\t\t\tif (!pokemon.volatiles['mirrorcoat'])\n\t\t\t\treturn 0;\n\t\t\treturn pokemon.volatiles['mirrorcoat'].damage || 1;\n\t\t}",
    "category": "Special",
    "name": "Mirror Coat",
    "pp": 20,
    "priority": -5,
    "flags": {
      "protect": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tpokemon.addVolatile('mirrorcoat');\n\t\t}",
    "onTryHit": "function (target, source, move) {\n\t\t\tif (!source.volatiles['mirrorcoat'])\n\t\t\t\treturn false;\n\t\t\tif (source.volatiles['mirrorcoat'].slot === null)\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "duration": 1,
      "noCopy": true,
      "onStart": "function (target, source, move) {\n\t\t\t\tthis.effectState.slot = null;\n\t\t\t\tthis.effectState.damage = 0;\n\t\t\t}",
      "onRedirectTargetPriority": -1,
      "onRedirectTarget": "function (target, source, source2, move) {\n\t\t\t\tif (move.id !== 'mirrorcoat')\n\t\t\t\t\treturn;\n\t\t\t\tif (source !== this.effectState.target || !this.effectState.slot)\n\t\t\t\t\treturn;\n\t\t\t\treturn this.getAtSlot(this.effectState.slot);\n\t\t\t}",
      "onDamagingHit": "function (damage, target, source, move) {\n\t\t\t\tif (!source.isAlly(target) && this.getCategory(move) === 'Special') {\n\t\t\t\t\tthis.effectState.slot = source.getSlot();\n\t\t\t\t\tthis.effectState.damage = 2 * damage;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "scripted",
    "type": "Psychic",
    "contestType": "Beautiful"
  },
  "mirrormove": {
    "num": 119,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Mirror Move",
    "pp": 20,
    "priority": 0,
    "flags": {},
    "onTryHit": "function (target, pokemon) {\n\t\t\tvar move = target.lastMove;\n\t\t\tif (!(move === null || move === void 0 ? void 0 : move.flags['mirror']) || move.isZ || move.isMax) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.actions.useMove(move.id, pokemon, target);\n\t\t\treturn null;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "zMove": {
      "boost": {
        "atk": 2
      }
    },
    "contestType": "Clever"
  },
  "mirrorshot": {
    "num": 429,
    "accuracy": 85,
    "basePower": 65,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Mirror Shot",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Beautiful"
  },
  "mist": {
    "num": 54,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Mist",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "mist",
    "condition": {
      "duration": 5,
      "onBoost": "function (boost, target, source, effect) {\n\t\t\t\tif (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))\n\t\t\t\t\treturn;\n\t\t\t\tif (source && target !== source) {\n\t\t\t\t\tvar showMsg = false;\n\t\t\t\t\tvar i = void 0;\n\t\t\t\t\tfor (i in boost) {\n\t\t\t\t\t\tif (boost[i] < 0) {\n\t\t\t\t\t\t\tdelete boost[i];\n\t\t\t\t\t\t\tshowMsg = true;\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t\tif (showMsg && !effect.secondaries) {\n\t\t\t\t\t\tthis.add('-activate', target, 'move: Mist');\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'Mist');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 4,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'Mist');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Ice",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Beautiful"
  },
  "mistball": {
    "num": 296,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Mist Ball",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "spa": -1
      }
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "mistyexplosion": {
    "num": 802,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Misty Explosion",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "selfdestruct": "always",
    "onBasePower": "function (basePower, source) {\n\t\t\tif (this.field.isTerrain('mistyterrain') && source.isGrounded()) {\n\t\t\t\tthis.debug('misty terrain boost');\n\t\t\t\treturn this.chainModify(1.5);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Fairy"
  },
  "mistyterrain": {
    "num": 581,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Misty Terrain",
    "pp": 10,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "terrain": "mistyterrain",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onSetStatus": "function (status, target, source, effect) {\n\t\t\t\tif (!target.isGrounded() || target.isSemiInvulnerable())\n\t\t\t\t\treturn;\n\t\t\t\tif (effect && (effect.status || effect.id === 'yawn')) {\n\t\t\t\t\tthis.add('-activate', target, 'move: Misty Terrain');\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onTryAddVolatile": "function (status, target, source, effect) {\n\t\t\t\tif (!target.isGrounded() || target.isSemiInvulnerable())\n\t\t\t\t\treturn;\n\t\t\t\tif (status.id === 'confusion') {\n\t\t\t\t\tif (effect.effectType === 'Move' && !effect.secondaries)\n\t\t\t\t\t\tthis.add('-activate', target, 'move: Misty Terrain');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}",
      "onBasePowerPriority": 6,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Dragon' && defender.isGrounded() && !defender.isSemiInvulnerable()) {\n\t\t\t\t\tthis.debug('misty terrain weaken');\n\t\t\t\t\treturn this.chainModify(0.5);\n\t\t\t\t}\n\t\t\t}",
      "onFieldStart": "function (field, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Misty Terrain', '[from] ability: ' + effect, '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Misty Terrain');\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 7,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'Misty Terrain');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Beautiful"
  },
  "moonblast": {
    "num": 585,
    "accuracy": 100,
    "basePower": 95,
    "category": "Special",
    "name": "Moonblast",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "boosts": {
        "spa": -1
      }
    },
    "target": "normal",
    "type": "Fairy",
    "contestType": "Beautiful"
  },
  "moongeistbeam": {
    "num": 714,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Moongeist Beam",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "ignoreAbility": true,
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "moonlight": {
    "num": 236,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Moonlight",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tvar factor = 0.5;\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tfactor = 0.667;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\tcase 'sandstorm':\n\t\t\t\tcase 'hail':\n\t\t\t\t\tfactor = 0.25;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, factor));\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Fairy",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "morningsun": {
    "num": 234,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Morning Sun",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tvar factor = 0.5;\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tfactor = 0.667;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\tcase 'sandstorm':\n\t\t\t\tcase 'hail':\n\t\t\t\t\tfactor = 0.25;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, factor));\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "mudbomb": {
    "num": 426,
    "accuracy": 85,
    "basePower": 65,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Mud Bomb",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Ground",
    "contestType": "Cute"
  },
  "mudshot": {
    "num": 341,
    "accuracy": 95,
    "basePower": 55,
    "category": "Special",
    "name": "Mud Shot",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "mudslap": {
    "num": 189,
    "accuracy": 100,
    "basePower": 20,
    "category": "Special",
    "name": "Mud-Slap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Ground",
    "contestType": "Cute"
  },
  "mudsport": {
    "num": 300,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Mud Sport",
    "pp": 15,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "pseudoWeather": "mudsport",
    "condition": {
      "duration": 5,
      "onFieldStart": "function (field, source) {\n\t\t\t\tthis.add('-fieldstart', 'move: Mud Sport', '[of] ' + source);\n\t\t\t}",
      "onBasePowerPriority": 1,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Electric') {\n\t\t\t\t\tthis.debug('mud sport weaken');\n\t\t\t\t\treturn this.chainModify([1352, 4096]);\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 4,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Mud Sport');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Ground",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "muddywater": {
    "num": 330,
    "accuracy": 85,
    "basePower": 90,
    "category": "Special",
    "name": "Muddy Water",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": {
      "chance": 30,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Water",
    "contestType": "Tough"
  },
  "multiattack": {
    "num": 718,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Multi-Attack",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (pokemon.ignoringItem())\n\t\t\t\treturn;\n\t\t\tmove.type = this.runEvent('Memory', pokemon, null, move, 'Normal');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 185
    },
    "maxMove": {
      "basePower": 95
    },
    "contestType": "Tough"
  },
  "mysticalfire": {
    "num": 595,
    "accuracy": 100,
    "basePower": 75,
    "category": "Special",
    "name": "Mystical Fire",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spa": -1
      }
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "nastyplot": {
    "num": 417,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Nasty Plot",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spa": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Dark",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "naturalgift": {
    "num": 363,
    "accuracy": 100,
    "basePower": 0,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Natural Gift",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (pokemon.ignoringItem())\n\t\t\t\treturn;\n\t\t\tvar item = pokemon.getItem();\n\t\t\tif (!item.naturalGift)\n\t\t\t\treturn;\n\t\t\tmove.type = item.naturalGift.type;\n\t\t}",
    "onPrepareHit": "function (target, pokemon, move) {\n\t\t\tif (pokemon.ignoringItem())\n\t\t\t\treturn false;\n\t\t\tvar item = pokemon.getItem();\n\t\t\tif (!item.naturalGift)\n\t\t\t\treturn false;\n\t\t\tmove.basePower = item.naturalGift.basePower;\n\t\t\tpokemon.setItem('');\n\t\t\tpokemon.lastItem = item.id;\n\t\t\tpokemon.usedItemThisTurn = true;\n\t\t\tthis.runEvent('AfterUseItem', pokemon, null, null, item);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Clever"
  },
  "naturepower": {
    "num": 267,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Nature Power",
    "pp": 20,
    "priority": 0,
    "flags": {},
    "onTryHit": "function (target, pokemon) {\n\t\t\tvar move = 'triattack';\n\t\t\tif (this.field.isTerrain('electricterrain')) {\n\t\t\t\tmove = 'thunderbolt';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('grassyterrain')) {\n\t\t\t\tmove = 'energyball';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('mistyterrain')) {\n\t\t\t\tmove = 'moonblast';\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('psychicterrain')) {\n\t\t\t\tmove = 'psychic';\n\t\t\t}\n\t\t\tthis.actions.useMove(move, pokemon, target);\n\t\t\treturn null;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "naturesmadness": {
    "num": 717,
    "accuracy": 90,
    "basePower": 0,
    "damageCallback": "function (pokemon, target) {\n\t\t\treturn this.clampIntRange(Math.floor(target.getUndynamaxedHP() / 2), 1);\n\t\t}",
    "category": "Special",
    "name": "Nature's Madness",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Tough"
  },
  "needlearm": {
    "num": 302,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Needle Arm",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Grass",
    "contestType": "Clever"
  },
  "neverendingnightmare": {
    "num": 636,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Never-Ending Nightmare",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "ghostiumz",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "nightdaze": {
    "num": 539,
    "accuracy": 95,
    "basePower": 85,
    "category": "Special",
    "name": "Night Daze",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 40,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Dark",
    "contestType": "Cool"
  },
  "nightmare": {
    "num": 171,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Nightmare",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "nightmare",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon) {\n\t\t\t\tif (pokemon.status !== 'slp' && !pokemon.hasAbility('comatose')) {\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tthis.add('-start', pokemon, 'Nightmare');\n\t\t\t}",
      "onResidualOrder": 11,
      "onResidual": "function (pokemon) {\n\t\t\t\tthis.damage(pokemon.baseMaxhp / 4);\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "nightshade": {
    "num": 101,
    "accuracy": 100,
    "basePower": 0,
    "damage": "level",
    "category": "Special",
    "name": "Night Shade",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "nightslash": {
    "num": 400,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Night Slash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Cool"
  },
  "nobleroar": {
    "num": 568,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Noble Roar",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "boosts": {
      "atk": -1,
      "spa": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "noretreat": {
    "num": 748,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "No Retreat",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "noretreat",
    "onTry": "function (source, target, move) {\n\t\t\tif (source.volatiles['noretreat'])\n\t\t\t\treturn false;\n\t\t\tif (source.volatiles['trapped']) {\n\t\t\t\tdelete move.volatileStatus;\n\t\t\t}\n\t\t}",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'move: No Retreat');\n\t\t\t}",
      "onTrapPokemon": "function (pokemon) {\n\t\t\t\tpokemon.tryTrap();\n\t\t\t}"
    },
    "boosts": {
      "atk": 1,
      "def": 1,
      "spa": 1,
      "spd": 1,
      "spe": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Fighting"
  },
  "nuzzle": {
    "num": 609,
    "accuracy": 100,
    "basePower": 20,
    "category": "Physical",
    "name": "Nuzzle",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cute"
  },
  "oblivionwing": {
    "num": 613,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Oblivion Wing",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "distance": 1,
      "heal": 1
    },
    "drain": [
      3,
      4
    ],
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "obstruct": {
    "num": 792,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Obstruct",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "obstruct",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'Protect');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect'] || move.category === 'Status') {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Protect');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.boost({ def: -2 }, source, target, this.dex.getActiveMove(\"Obstruct\"));\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.boost({ def: -2 }, source, target, this.dex.getActiveMove(\"Obstruct\"));\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Dark"
  },
  "oceanicoperetta": {
    "num": 697,
    "accuracy": true,
    "basePower": 195,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Oceanic Operetta",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "primariumz",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "octazooka": {
    "num": 190,
    "accuracy": 85,
    "basePower": 65,
    "category": "Special",
    "name": "Octazooka",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "accuracy": -1
      }
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "octolock": {
    "num": 753,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Octolock",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryImmunity": "function (target) {\n\t\t\treturn this.dex.getImmunity('trapped', target);\n\t\t}",
    "volatileStatus": "octolock",
    "condition": {
      "onStart": "function (pokemon, source) {\n\t\t\t\tthis.add('-start', pokemon, 'move: Octolock', '[of] ' + source);\n\t\t\t}",
      "onResidualOrder": 14,
      "onResidual": "function (pokemon) {\n\t\t\t\tvar source = this.effectState.source;\n\t\t\t\tif (source && (!source.isActive || source.hp <= 0 || !source.activeTurns)) {\n\t\t\t\t\tdelete pokemon.volatiles['octolock'];\n\t\t\t\t\tthis.add('-end', pokemon, 'Octolock', '[partiallytrapped]', '[silent]');\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.boost({ def: -1, spd: -1 }, pokemon, source, this.dex.getActiveMove('octolock'));\n\t\t\t}",
      "onTrapPokemon": "function (pokemon) {\n\t\t\t\tif (this.effectState.source && this.effectState.source.isActive)\n\t\t\t\t\tpokemon.tryTrap();\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting"
  },
  "odorsleuth": {
    "num": 316,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Odor Sleuth",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "volatileStatus": "foresight",
    "onTryHit": "function (target) {\n\t\t\tif (target.volatiles['miracleeye'])\n\t\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Clever"
  },
  "ominouswind": {
    "num": 466,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Ominous Wind",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "self": {
        "boosts": {
          "atk": 1,
          "def": 1,
          "spa": 1,
          "spd": 1,
          "spe": 1
        }
      }
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Beautiful"
  },
  "originpulse": {
    "num": 618,
    "accuracy": 85,
    "basePower": 110,
    "category": "Special",
    "name": "Origin Pulse",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "pulse": 1,
      "mirror": 1
    },
    "target": "allAdjacentFoes",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "outrage": {
    "num": 200,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Outrage",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "lockedmove"
    },
    "onAfterMove": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['lockedmove'] && pokemon.volatiles['lockedmove'].duration === 1) {\n\t\t\t\tpokemon.removeVolatile('lockedmove');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "randomNormal",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "overdrive": {
    "num": 786,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Overdrive",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Electric"
  },
  "overheat": {
    "num": 315,
    "accuracy": 90,
    "basePower": 130,
    "category": "Special",
    "name": "Overheat",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spa": -2
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "painsplit": {
    "num": 220,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Pain Split",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target, pokemon) {\n\t\t\tvar targetHP = target.getUndynamaxedHP();\n\t\t\tvar averagehp = Math.floor((targetHP + pokemon.hp) / 2) || 1;\n\t\t\tvar targetChange = targetHP - averagehp;\n\t\t\ttarget.sethp(target.hp - targetChange);\n\t\t\tthis.add('-sethp', target, target.getHealth, '[from] move: Pain Split', '[silent]');\n\t\t\tpokemon.sethp(averagehp);\n\t\t\tthis.add('-sethp', pokemon, pokemon.getHealth, '[from] move: Pain Split');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "paleowave": {
    "num": 0,
    "accuracy": 100,
    "basePower": 85,
    "category": "Special",
    "isNonstandard": "CAP",
    "name": "Paleo Wave",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "boosts": {
        "atk": -1
      }
    },
    "target": "normal",
    "type": "Rock",
    "contestType": "Beautiful"
  },
  "paraboliccharge": {
    "num": 570,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Parabolic Charge",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "heal": 1
    },
    "drain": [
      1,
      2
    ],
    "secondary": null,
    "target": "allAdjacent",
    "type": "Electric",
    "contestType": "Clever"
  },
  "partingshot": {
    "num": 575,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Parting Shot",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tvar success = this.boost({ atk: -1, spa: -1 }, target, source);\n\t\t\tif (!success && !target.hasAbility('mirrorarmor')) {\n\t\t\t\tdelete move.selfSwitch;\n\t\t\t}\n\t\t}",
    "selfSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "effect": "healreplacement"
    },
    "contestType": "Cool"
  },
  "payback": {
    "num": 371,
    "accuracy": 100,
    "basePower": 50,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.newlySwitched || this.queue.willMove(target)) {\n\t\t\t\tthis.debug('Payback NOT boosted');\n\t\t\t\treturn move.basePower;\n\t\t\t}\n\t\t\tthis.debug('Payback damage boost');\n\t\t\treturn move.basePower * 2;\n\t\t}",
    "category": "Physical",
    "name": "Payback",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Tough"
  },
  "payday": {
    "num": 6,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Pay Day",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function () {\n\t\t\tthis.add('-fieldactivate', 'move: Pay Day');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Clever"
  },
  "peck": {
    "num": 64,
    "accuracy": 100,
    "basePower": 35,
    "category": "Physical",
    "name": "Peck",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "perishsong": {
    "num": 195,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Perish Song",
    "pp": 5,
    "priority": 0,
    "flags": {
      "sound": 1,
      "distance": 1,
      "authentic": 1
    },
    "onHitField": "function (target, source, move) {\n\t\t\tvar result = false;\n\t\t\tvar message = false;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (this.runEvent('Invulnerability', pokemon, source, move) === false) {\n\t\t\t\t\tthis.add('-miss', source, pokemon);\n\t\t\t\t\tresult = true;\n\t\t\t\t}\n\t\t\t\telse if (this.runEvent('TryHit', pokemon, source, move) === null) {\n\t\t\t\t\tresult = true;\n\t\t\t\t}\n\t\t\t\telse if (!pokemon.volatiles['perishsong']) {\n\t\t\t\t\tpokemon.addVolatile('perishsong');\n\t\t\t\t\tthis.add('-start', pokemon, 'perish3', '[silent]');\n\t\t\t\t\tresult = true;\n\t\t\t\t\tmessage = true;\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!result)\n\t\t\t\treturn false;\n\t\t\tif (message)\n\t\t\t\tthis.add('-fieldactivate', 'move: Perish Song');\n\t\t}",
    "condition": {
      "duration": 4,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-start', target, 'perish0');\n\t\t\t\ttarget.faint();\n\t\t\t}",
      "onResidualOrder": 24,
      "onResidual": "function (pokemon) {\n\t\t\t\tvar duration = pokemon.volatiles['perishsong'].duration;\n\t\t\t\tthis.add('-start', pokemon, 'perish' + duration);\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "petalblizzard": {
    "num": 572,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Petal Blizzard",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacent",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "petaldance": {
    "num": 80,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "name": "Petal Dance",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "dance": 1
    },
    "self": {
      "volatileStatus": "lockedmove"
    },
    "onAfterMove": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['lockedmove'] && pokemon.volatiles['lockedmove'].duration === 1) {\n\t\t\t\tpokemon.removeVolatile('lockedmove');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "randomNormal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "phantomforce": {
    "num": 566,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Phantom Force",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "mirror": 1
    },
    "breaksProtect": true,
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onInvulnerability": false
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "photongeyser": {
    "num": 722,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Photon Geyser",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyMove": "function (move, pokemon) {\n\t\t\tif (pokemon.getStat('atk', false, true) > pokemon.getStat('spa', false, true))\n\t\t\t\tmove.category = 'Physical';\n\t\t}",
    "ignoreAbility": true,
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "pikapapow": {
    "num": 732,
    "accuracy": true,
    "basePower": 0,
    "basePowerCallback": "function (pokemon) {\n\t\t\treturn Math.floor((pokemon.happiness * 10) / 25) || 1;\n\t\t}",
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Pika Papow",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cute"
  },
  "pinmissile": {
    "num": 42,
    "accuracy": 95,
    "basePower": 25,
    "category": "Physical",
    "name": "Pin Missile",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "plasmafists": {
    "num": 721,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Plasma Fists",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "pseudoWeather": "iondeluge",
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "playnice": {
    "num": 589,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Play Nice",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "boosts": {
      "atk": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "playrough": {
    "num": 583,
    "accuracy": 90,
    "basePower": 90,
    "category": "Physical",
    "name": "Play Rough",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "atk": -1
      }
    },
    "target": "normal",
    "type": "Fairy",
    "contestType": "Cute"
  },
  "pluck": {
    "num": 365,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Pluck",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar item = target.getItem();\n\t\t\tif (source.hp && item.isBerry && target.takeItem(source)) {\n\t\t\t\tthis.add('-enditem', target, item.name, '[from] stealeat', '[move] Pluck', '[of] ' + source);\n\t\t\t\tif (this.singleEvent('Eat', item, null, source, null, null)) {\n\t\t\t\t\tthis.runEvent('EatItem', source, null, null, item);\n\t\t\t\t\tif (item.id === 'leppaberry')\n\t\t\t\t\t\ttarget.staleness = 'external';\n\t\t\t\t}\n\t\t\t\tif (item.onEat)\n\t\t\t\t\tsource.ateBerry = true;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cute"
  },
  "poisonfang": {
    "num": 305,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Poison Fang",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "status": "tox"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Clever"
  },
  "poisongas": {
    "num": 139,
    "accuracy": 90,
    "basePower": 0,
    "category": "Status",
    "name": "Poison Gas",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "psn",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "poisonjab": {
    "num": 398,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Poison Jab",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "poisonpowder": {
    "num": 77,
    "accuracy": 75,
    "basePower": 0,
    "category": "Status",
    "name": "Poison Powder",
    "pp": 35,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "psn",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "poisonsting": {
    "num": 40,
    "accuracy": 100,
    "basePower": 15,
    "category": "Physical",
    "name": "Poison Sting",
    "pp": 35,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Clever"
  },
  "poisontail": {
    "num": 342,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Poison Tail",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": {
      "chance": 10,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Clever"
  },
  "pollenpuff": {
    "num": 676,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Pollen Puff",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, source, move) {\n\t\t\tif (source.isAlly(target)) {\n\t\t\t\tmove.basePower = 0;\n\t\t\t\tmove.infiltrates = true;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tif (source.isAlly(target)) {\n\t\t\t\tif (!this.heal(Math.floor(target.baseMaxhp * 0.5))) {\n\t\t\t\t\tthis.add('-immune', target);\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "poltergeist": {
    "num": 809,
    "accuracy": 90,
    "basePower": 110,
    "category": "Physical",
    "name": "Poltergeist",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function (source, target) {\n\t\t\treturn !!target.item;\n\t\t}",
    "onTryHit": "function (target, source, move) {\n\t\t\tthis.add('-activate', target, 'move: Poltergeist', this.dex.items.get(target.item).name);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Ghost"
  },
  "pound": {
    "num": 1,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Pound",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "powder": {
    "num": 600,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Powder",
    "pp": 20,
    "priority": 1,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "powder",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'Powder');\n\t\t\t}",
      "onTryMovePriority": -1,
      "onTryMove": "function (pokemon, target, move) {\n\t\t\t\tif (move.type === 'Fire') {\n\t\t\t\t\tthis.add('-activate', pokemon, 'move: Powder');\n\t\t\t\t\tthis.damage(this.clampIntRange(Math.round(pokemon.maxhp / 4), 1));\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "zMove": {
      "boost": {
        "spd": 2
      }
    },
    "contestType": "Clever"
  },
  "powdersnow": {
    "num": 181,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Powder Snow",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "frz"
    },
    "target": "allAdjacentFoes",
    "type": "Ice",
    "contestType": "Beautiful"
  },
  "powergem": {
    "num": 408,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Power Gem",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Beautiful"
  },
  "powersplit": {
    "num": 471,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Power Split",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar newatk = Math.floor((target.storedStats.atk + source.storedStats.atk) / 2);\n\t\t\ttarget.storedStats.atk = newatk;\n\t\t\tsource.storedStats.atk = newatk;\n\t\t\tvar newspa = Math.floor((target.storedStats.spa + source.storedStats.spa) / 2);\n\t\t\ttarget.storedStats.spa = newspa;\n\t\t\tsource.storedStats.spa = newspa;\n\t\t\tthis.add('-activate', source, 'move: Power Split', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "powerswap": {
    "num": 384,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Power Swap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar targetBoosts = {};\n\t\t\tvar sourceBoosts = {};\n\t\t\tvar atkSpa = ['atk', 'spa'];\n\t\t\tfor (var _i = 0, atkSpa_1 = atkSpa; _i < atkSpa_1.length; _i++) {\n\t\t\t\tvar stat = atkSpa_1[_i];\n\t\t\t\ttargetBoosts[stat] = target.boosts[stat];\n\t\t\t\tsourceBoosts[stat] = source.boosts[stat];\n\t\t\t}\n\t\t\tsource.setBoost(targetBoosts);\n\t\t\ttarget.setBoost(sourceBoosts);\n\t\t\tthis.add('-swapboost', source, target, 'atk, spa', '[from] move: Power Swap');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "powertrick": {
    "num": 379,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Power Trick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "volatileStatus": "powertrick",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Power Trick');\n\t\t\t\tvar newatk = pokemon.storedStats.def;\n\t\t\t\tvar newdef = pokemon.storedStats.atk;\n\t\t\t\tpokemon.storedStats.atk = newatk;\n\t\t\t\tpokemon.storedStats.def = newdef;\n\t\t\t}",
      "onCopy": "function (pokemon) {\n\t\t\t\tvar newatk = pokemon.storedStats.def;\n\t\t\t\tvar newdef = pokemon.storedStats.atk;\n\t\t\t\tpokemon.storedStats.atk = newatk;\n\t\t\t\tpokemon.storedStats.def = newdef;\n\t\t\t}",
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'Power Trick');\n\t\t\t\tvar newatk = pokemon.storedStats.def;\n\t\t\t\tvar newdef = pokemon.storedStats.atk;\n\t\t\t\tpokemon.storedStats.atk = newatk;\n\t\t\t\tpokemon.storedStats.def = newdef;\n\t\t\t}",
      "onRestart": "function (pokemon) {\n\t\t\t\tpokemon.removeVolatile('Power Trick');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Clever"
  },
  "powertrip": {
    "num": 681,
    "accuracy": 100,
    "basePower": 20,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn move.basePower + 20 * pokemon.positiveBoosts();\n\t\t}",
    "category": "Physical",
    "name": "Power Trip",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Clever"
  },
  "poweruppunch": {
    "num": 612,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Power-Up Punch",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 100,
      "self": {
        "boosts": {
          "atk": 1
        }
      }
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "powerwhip": {
    "num": 438,
    "accuracy": 85,
    "basePower": 120,
    "category": "Physical",
    "name": "Power Whip",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Tough"
  },
  "precipiceblades": {
    "num": 619,
    "accuracy": 85,
    "basePower": 120,
    "category": "Physical",
    "name": "Precipice Blades",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "target": "allAdjacentFoes",
    "type": "Ground",
    "contestType": "Cool"
  },
  "present": {
    "num": 217,
    "accuracy": 90,
    "basePower": 0,
    "category": "Physical",
    "name": "Present",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyMove": "function (move, pokemon, target) {\n\t\t\tvar rand = this.random(10);\n\t\t\tif (rand < 2) {\n\t\t\t\tmove.heal = [1, 4];\n\t\t\t\tmove.infiltrates = true;\n\t\t\t}\n\t\t\telse if (rand < 6) {\n\t\t\t\tmove.basePower = 40;\n\t\t\t}\n\t\t\telse if (rand < 9) {\n\t\t\t\tmove.basePower = 80;\n\t\t\t}\n\t\t\telse {\n\t\t\t\tmove.basePower = 120;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "prismaticlaser": {
    "num": 711,
    "accuracy": 100,
    "basePower": 160,
    "category": "Special",
    "name": "Prismatic Laser",
    "pp": 10,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "protect": {
    "num": 182,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Protect",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "protect",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'Protect');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect']) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Protect');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "psybeam": {
    "num": 60,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Psybeam",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Beautiful"
  },
  "psychup": {
    "num": 244,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Psych Up",
    "pp": 10,
    "priority": 0,
    "flags": {
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar i;\n\t\t\tfor (i in target.boosts) {\n\t\t\t\tsource.boosts[i] = target.boosts[i];\n\t\t\t}\n\t\t\tvar volatilesToCopy = ['focusenergy', 'gmaxchistrike', 'laserfocus'];\n\t\t\tfor (var _i = 0, volatilesToCopy_1 = volatilesToCopy; _i < volatilesToCopy_1.length; _i++) {\n\t\t\t\tvar volatile = volatilesToCopy_1[_i];\n\t\t\t\tif (target.volatiles[volatile]) {\n\t\t\t\t\tsource.addVolatile(volatile);\n\t\t\t\t\tif (volatile === 'gmaxchistrike')\n\t\t\t\t\t\tsource.volatiles[volatile].layers = target.volatiles[volatile].layers;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tsource.removeVolatile(volatile);\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.add('-copyboost', source, target, '[from] move: Psych Up');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Clever"
  },
  "psychic": {
    "num": 94,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Psychic",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "psychicfangs": {
    "num": 706,
    "accuracy": 100,
    "basePower": 85,
    "category": "Physical",
    "name": "Psychic Fangs",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (pokemon) {\n\t\t\t// will shatter screens through sub, before you hit\n\t\t\tpokemon.side.removeSideCondition('reflect');\n\t\t\tpokemon.side.removeSideCondition('lightscreen');\n\t\t\tpokemon.side.removeSideCondition('auroraveil');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "psychicterrain": {
    "num": 678,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Psychic Terrain",
    "pp": 10,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "terrain": "psychicterrain",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onTryHitPriority": 4,
      "onTryHit": "function (target, source, effect) {\n\t\t\t\tif (effect && (effect.priority <= 0.1 || effect.target === 'self')) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (target.isSemiInvulnerable() || target.isAlly(source))\n\t\t\t\t\treturn;\n\t\t\t\tif (!target.isGrounded()) {\n\t\t\t\t\tvar baseMove = this.dex.moves.get(effect.id);\n\t\t\t\t\tif (baseMove.priority > 0) {\n\t\t\t\t\t\tthis.hint(\"Psychic Terrain doesn't affect Pokémon immune to Ground.\");\n\t\t\t\t\t}\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.add('-activate', target, 'move: Psychic Terrain');\n\t\t\t\treturn null;\n\t\t\t}",
      "onBasePowerPriority": 6,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Psychic' && attacker.isGrounded() && !attacker.isSemiInvulnerable()) {\n\t\t\t\t\tthis.debug('psychic terrain boost');\n\t\t\t\t\treturn this.chainModify([5325, 4096]);\n\t\t\t\t}\n\t\t\t}",
      "onFieldStart": "function (field, source, effect) {\n\t\t\t\tif ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Psychic Terrain', '[from] ability: ' + effect, '[of] ' + source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-fieldstart', 'move: Psychic Terrain');\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 7,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Psychic Terrain');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "psychoboost": {
    "num": 354,
    "accuracy": 90,
    "basePower": 140,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Psycho Boost",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spa": -2
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "psychocut": {
    "num": 427,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Psycho Cut",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "psychoshift": {
    "num": 375,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Psycho Shift",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryHit": "function (target, source, move) {\n\t\t\tif (!source.status)\n\t\t\t\treturn false;\n\t\t\tmove.status = source.status;\n\t\t}",
    "self": {
      "onHit": "function (pokemon) {\n\t\t\t\tpokemon.cureStatus();\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 2
      }
    },
    "contestType": "Clever"
  },
  "psyshock": {
    "num": 473,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "defensiveCategory": "Physical",
    "name": "Psyshock",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Beautiful"
  },
  "psystrike": {
    "num": 540,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "defensiveCategory": "Physical",
    "name": "Psystrike",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "psywave": {
    "num": 149,
    "accuracy": 100,
    "basePower": 0,
    "damageCallback": "function (pokemon) {\n\t\t\treturn (this.random(50, 151) * pokemon.level) / 100;\n\t\t}",
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Psywave",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "pulverizingpancake": {
    "num": 701,
    "accuracy": true,
    "basePower": 210,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Pulverizing Pancake",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "snorliumz",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "punishment": {
    "num": 386,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar power = 60 + 20 * target.positiveBoosts();\n\t\t\tif (power > 200)\n\t\t\t\tpower = 200;\n\t\t\treturn power;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Punishment",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "purify": {
    "num": 685,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Purify",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "heal": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (!target.cureStatus())\n\t\t\t\treturn false;\n\t\t\tthis.heal(Math.ceil(source.maxhp * 0.5), source);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "pursuit": {
    "num": 228,
    "accuracy": 100,
    "basePower": 40,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\t// You can't get here unless the pursuit succeeds\n\t\t\tif (target.beingCalledBack || target.switchFlag) {\n\t\t\t\tthis.debug('Pursuit damage boost');\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Pursuit",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tfor (var _i = 0, _a = this.sides; _i < _a.length; _i++) {\n\t\t\t\tvar side = _a[_i];\n\t\t\t\tif (side.hasAlly(pokemon))\n\t\t\t\t\tcontinue;\n\t\t\t\tside.addSideCondition('pursuit', pokemon);\n\t\t\t\tvar data = side.getSideConditionData('pursuit');\n\t\t\t\tif (!data.sources) {\n\t\t\t\t\tdata.sources = [];\n\t\t\t\t}\n\t\t\t\tdata.sources.push(pokemon);\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move, source, target) {\n\t\t\tif ((target === null || target === void 0 ? void 0 : target.beingCalledBack) || (target === null || target === void 0 ? void 0 : target.switchFlag))\n\t\t\t\tmove.accuracy = true;\n\t\t}",
    "onTryHit": "function (target, pokemon) {\n\t\t\ttarget.side.removeSideCondition('pursuit');\n\t\t}",
    "condition": {
      "duration": 1,
      "onBeforeSwitchOut": "function (pokemon) {\n\t\t\t\tthis.debug('Pursuit start');\n\t\t\t\tvar alreadyAdded = false;\n\t\t\t\tpokemon.removeVolatile('destinybond');\n\t\t\t\tfor (var _i = 0, _a = this.effectState.sources; _i < _a.length; _i++) {\n\t\t\t\t\tvar source = _a[_i];\n\t\t\t\t\tif (!this.queue.cancelMove(source) || !source.hp)\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\tif (!alreadyAdded) {\n\t\t\t\t\t\tthis.add('-activate', pokemon, 'move: Pursuit');\n\t\t\t\t\t\talreadyAdded = true;\n\t\t\t\t\t}\n\t\t\t\t\t// Run through each action in queue to check if the Pursuit user is supposed to Mega Evolve this turn.\n\t\t\t\t\t// If it is, then Mega Evolve before moving.\n\t\t\t\t\tif (source.canMegaEvo || source.canUltraBurst) {\n\t\t\t\t\t\tfor (var _b = 0, _c = this.queue.entries(); _b < _c.length; _b++) {\n\t\t\t\t\t\t\tvar _d = _c[_b], actionIndex = _d[0], action = _d[1];\n\t\t\t\t\t\t\tif (action.pokemon === source && action.choice === 'megaEvo') {\n\t\t\t\t\t\t\t\tthis.actions.runMegaEvo(source);\n\t\t\t\t\t\t\t\tthis.queue.list.splice(actionIndex, 1);\n\t\t\t\t\t\t\t\tbreak;\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t\tthis.actions.runMove('pursuit', source, source.getLocOf(pokemon));\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "pyroball": {
    "num": 780,
    "accuracy": 90,
    "basePower": 120,
    "category": "Physical",
    "name": "Pyro Ball",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1,
      "bullet": 1
    },
    "secondary": {
      "chance": 10,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire"
  },
  "quash": {
    "num": 511,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Quash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target) {\n\t\t\tif (this.activePerHalf === 1)\n\t\t\t\treturn false; // fails in singles\n\t\t\tvar action = this.queue.willMove(target);\n\t\t\tif (!action)\n\t\t\t\treturn false;\n\t\t\taction.order = 201;\n\t\t\tthis.add('-activate', target, 'move: Quash');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "quickattack": {
    "num": 98,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Quick Attack",
    "pp": 30,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "quickguard": {
    "num": 501,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Quick Guard",
    "pp": 15,
    "priority": 3,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "quickguard",
    "onTry": "function () {\n\t\t\treturn !!this.queue.willAct();\n\t\t}",
    "onHitSide": "function (side, source) {\n\t\t\tsource.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onSideStart": "function (target, source) {\n\t\t\t\tthis.add('-singleturn', source, 'Quick Guard');\n\t\t\t}",
      "onTryHitPriority": 4,
      "onTryHit": "function (target, source, move) {\n\t\t\t\t// Quick Guard blocks moves with positive priority, even those given increased priority by Prankster or Gale Wings.\n\t\t\t\t// (e.g. it blocks 0 priority moves boosted by Prankster or Gale Wings; Quick Claw/Custap Berry do not count)\n\t\t\t\tif (move.priority <= 0.1)\n\t\t\t\t\treturn;\n\t\t\t\tif (!move.flags['protect']) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.add('-activate', target, 'move: Quick Guard');\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Fighting",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cool"
  },
  "quiverdance": {
    "num": 483,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Quiver Dance",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "dance": 1
    },
    "boosts": {
      "spa": 1,
      "spd": 1,
      "spe": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Bug",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "rage": {
    "num": 99,
    "accuracy": 100,
    "basePower": 20,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Rage",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "rage"
    },
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singlemove', pokemon, 'Rage');\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (target !== source && move.category !== 'Status') {\n\t\t\t\t\tthis.boost({ atk: 1 });\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 100,
      "onBeforeMove": "function (pokemon) {\n\t\t\t\tthis.debug('removing Rage before attack');\n\t\t\t\tpokemon.removeVolatile('rage');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "ragepowder": {
    "num": 476,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Rage Powder",
    "pp": 20,
    "priority": 2,
    "flags": {
      "powder": 1
    },
    "volatileStatus": "ragepowder",
    "onTry": "function (source) {\n\t\t\treturn this.activePerHalf > 1;\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'move: Rage Powder');\n\t\t\t}",
      "onFoeRedirectTargetPriority": 1,
      "onFoeRedirectTarget": "function (target, source, source2, move) {\n\t\t\t\tvar ragePowderUser = this.effectState.target;\n\t\t\t\tif (ragePowderUser.isSkyDropped())\n\t\t\t\t\treturn;\n\t\t\t\tif (source.runStatusImmunity('powder') && this.validTarget(ragePowderUser, source, move.target)) {\n\t\t\t\t\tif (move.smartTarget)\n\t\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t\tthis.debug(\"Rage Powder redirected target of move\");\n\t\t\t\t\treturn ragePowderUser;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Bug",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "raindance": {
    "num": 240,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Rain Dance",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "weather": "RainDance",
    "secondary": null,
    "target": "all",
    "type": "Water",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "rapidspin": {
    "num": 229,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Rapid Spin",
    "pp": 40,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onAfterHit": "function (target, pokemon) {\n\t\t\tif (pokemon.hp && pokemon.removeVolatile('leechseed')) {\n\t\t\t\tthis.add('-end', pokemon, 'Leech Seed', '[from] move: Rapid Spin', '[of] ' + pokemon);\n\t\t\t}\n\t\t\tvar sideConditions = ['spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge'];\n\t\t\tfor (var _i = 0, sideConditions_3 = sideConditions; _i < sideConditions_3.length; _i++) {\n\t\t\t\tvar condition = sideConditions_3[_i];\n\t\t\t\tif (pokemon.hp && pokemon.side.removeSideCondition(condition)) {\n\t\t\t\t\tthis.add('-sideend', pokemon.side, this.dex.conditions.get(condition).name, '[from] move: Rapid Spin', '[of] ' + pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (pokemon.hp && pokemon.volatiles['partiallytrapped']) {\n\t\t\t\tpokemon.removeVolatile('partiallytrapped');\n\t\t\t}\n\t\t}",
    "onAfterSubDamage": "function (damage, target, pokemon) {\n\t\t\tif (pokemon.hp && pokemon.removeVolatile('leechseed')) {\n\t\t\t\tthis.add('-end', pokemon, 'Leech Seed', '[from] move: Rapid Spin', '[of] ' + pokemon);\n\t\t\t}\n\t\t\tvar sideConditions = ['spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge'];\n\t\t\tfor (var _i = 0, sideConditions_4 = sideConditions; _i < sideConditions_4.length; _i++) {\n\t\t\t\tvar condition = sideConditions_4[_i];\n\t\t\t\tif (pokemon.hp && pokemon.side.removeSideCondition(condition)) {\n\t\t\t\t\tthis.add('-sideend', pokemon.side, this.dex.conditions.get(condition).name, '[from] move: Rapid Spin', '[of] ' + pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (pokemon.hp && pokemon.volatiles['partiallytrapped']) {\n\t\t\t\tpokemon.removeVolatile('partiallytrapped');\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 100,
      "self": {
        "boosts": {
          "spe": 1
        }
      }
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "razorleaf": {
    "num": 75,
    "accuracy": 95,
    "basePower": 55,
    "category": "Physical",
    "name": "Razor Leaf",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Grass",
    "contestType": "Cool"
  },
  "razorshell": {
    "num": 534,
    "accuracy": 95,
    "basePower": 75,
    "category": "Physical",
    "name": "Razor Shell",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "razorwind": {
    "num": 13,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Razor Wind",
    "pp": 10,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "critRatio": 2,
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "contestType": "Cool"
  },
  "recover": {
    "num": 105,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Recover",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "recycle": {
    "num": 278,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Recycle",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tif (pokemon.item || !pokemon.lastItem)\n\t\t\t\treturn false;\n\t\t\tvar item = pokemon.lastItem;\n\t\t\tpokemon.lastItem = '';\n\t\t\tthis.add('-item', pokemon, this.dex.items.get(item), '[from] move: Recycle');\n\t\t\tpokemon.setItem(item);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "reflect": {
    "num": 115,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Reflect",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "reflect",
    "condition": {
      "duration": 5,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasItem('lightclay')) {\n\t\t\t\t\treturn 8;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onAnyModifyDamage": "function (damage, source, target, move) {\n\t\t\t\tif (target !== source && this.effectState.target.hasAlly(target) && this.getCategory(move) === 'Physical') {\n\t\t\t\t\tif (!target.getMoveHitData(move).crit && !move.infiltrates) {\n\t\t\t\t\t\tthis.debug('Reflect weaken');\n\t\t\t\t\t\tif (this.activePerHalf > 1)\n\t\t\t\t\t\t\treturn this.chainModify([2732, 4096]);\n\t\t\t\t\t\treturn this.chainModify(0.5);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'Reflect');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 1,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'Reflect');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "reflecttype": {
    "num": 513,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Reflect Type",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (source.species && (source.species.num === 493 || source.species.num === 773))\n\t\t\t\treturn false;\n\t\t\tvar newBaseTypes = target.getTypes(true).filter(function (type) { return type !== '???'; });\n\t\t\tif (!newBaseTypes.length) {\n\t\t\t\tif (target.addedType) {\n\t\t\t\t\tnewBaseTypes = ['Normal'];\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}\n\t\t\tthis.add('-start', source, 'typechange', '[from] move: Reflect Type', '[of] ' + target);\n\t\t\tsource.setType(newBaseTypes);\n\t\t\tsource.addedType = target.addedType;\n\t\t\tsource.knownType = target.isAlly(source) && target.knownType;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "refresh": {
    "num": 287,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Refresh",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tif (['', 'slp', 'frz'].includes(pokemon.status))\n\t\t\t\treturn false;\n\t\t\tpokemon.cureStatus();\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Cute"
  },
  "relicsong": {
    "num": 547,
    "accuracy": 100,
    "basePower": 75,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Relic Song",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": {
      "chance": 10,
      "status": "slp"
    },
    "onHit": "function (target, pokemon, move) {\n\t\t\tif (pokemon.baseSpecies.baseSpecies === 'Meloetta' && !pokemon.transformed) {\n\t\t\t\tmove.willChangeForme = true;\n\t\t\t}\n\t\t}",
    "onAfterMoveSecondarySelf": "function (pokemon, target, move) {\n\t\t\tif (move.willChangeForme) {\n\t\t\t\tvar meloettaForme = pokemon.species.id === 'meloettapirouette' ? '' : '-Pirouette';\n\t\t\t\tpokemon.formeChange('Meloetta' + meloettaForme, this.effect, false, '[msg]');\n\t\t\t}\n\t\t}",
    "target": "allAdjacentFoes",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "rest": {
    "num": 156,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Rest",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.status === 'slp' || source.hasAbility('comatose'))\n\t\t\t\treturn false;\n\t\t\tif (source.hp === source.maxhp) {\n\t\t\t\tthis.add('-fail', source, 'heal');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t\tif (source.hasAbility(['insomnia', 'vitalspirit'])) {\n\t\t\t\tthis.add('-fail', source, '[from] ability: ' + source.getAbility().name, '[of] ' + source);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source, move) {\n\t\t\tif (!target.setStatus('slp', source, move))\n\t\t\t\treturn false;\n\t\t\ttarget.statusState.time = 3;\n\t\t\ttarget.statusState.startTime = 3;\n\t\t\tthis.heal(target.maxhp); // Aesthetic only as the healing happens after you fall asleep in-game\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "retaliate": {
    "num": 514,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Retaliate",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon) {\n\t\t\tif (pokemon.side.faintedLastTurn) {\n\t\t\t\tthis.debug('Boosted for a faint last turn');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "return": {
    "num": 216,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon) {\n\t\t\treturn Math.floor((pokemon.happiness * 10) / 25) || 1;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Return",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cute"
  },
  "revelationdance": {
    "num": 686,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Revelation Dance",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "dance": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tvar type = pokemon.getTypes()[0];\n\t\t\tif (type === \"Bird\")\n\t\t\t\ttype = \"???\";\n\t\t\tmove.type = type;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "revenge": {
    "num": 279,
    "accuracy": 100,
    "basePower": 60,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tvar damagedByTarget = pokemon.attackedBy.some(function (p) { return p.source === target && p.damage > 0 && p.thisTurn; });\n\t\t\tif (damagedByTarget) {\n\t\t\t\tthis.debug('Boosted for getting hit by ' + target);\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Revenge",
    "pp": 10,
    "priority": -4,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "reversal": {
    "num": 179,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\tvar ratio = pokemon.hp * 48 / pokemon.maxhp;\n\t\t\tif (ratio < 2) {\n\t\t\t\treturn 200;\n\t\t\t}\n\t\t\tif (ratio < 5) {\n\t\t\t\treturn 150;\n\t\t\t}\n\t\t\tif (ratio < 10) {\n\t\t\t\treturn 100;\n\t\t\t}\n\t\t\tif (ratio < 17) {\n\t\t\t\treturn 80;\n\t\t\t}\n\t\t\tif (ratio < 33) {\n\t\t\t\treturn 40;\n\t\t\t}\n\t\t\treturn 20;\n\t\t}",
    "category": "Physical",
    "name": "Reversal",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "zMove": {
      "basePower": 160
    },
    "contestType": "Cool"
  },
  "risingvoltage": {
    "num": 804,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Rising Voltage",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon, target) {\n\t\t\tif (this.field.isTerrain('electricterrain') && target.isGrounded()) {\n\t\t\t\tthis.debug('terrain buff');\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "maxMove": {
      "basePower": 140
    }
  },
  "roar": {
    "num": 46,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Roar",
    "pp": 20,
    "priority": -6,
    "flags": {
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1,
      "mystery": 1
    },
    "forceSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cool"
  },
  "roaroftime": {
    "num": 459,
    "accuracy": 90,
    "basePower": 150,
    "category": "Special",
    "name": "Roar of Time",
    "pp": 5,
    "priority": 0,
    "flags": {
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Beautiful"
  },
  "rockblast": {
    "num": 350,
    "accuracy": 90,
    "basePower": 25,
    "category": "Physical",
    "name": "Rock Blast",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Tough"
  },
  "rockclimb": {
    "num": 431,
    "accuracy": 85,
    "basePower": 90,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Rock Climb",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "rockpolish": {
    "num": 397,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Rock Polish",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spe": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Rock",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "rockslide": {
    "num": 157,
    "accuracy": 90,
    "basePower": 75,
    "category": "Physical",
    "name": "Rock Slide",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "allAdjacentFoes",
    "type": "Rock",
    "contestType": "Tough"
  },
  "rocksmash": {
    "num": 249,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Rock Smash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "rockthrow": {
    "num": 88,
    "accuracy": 90,
    "basePower": 50,
    "category": "Physical",
    "name": "Rock Throw",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "rocktomb": {
    "num": 317,
    "accuracy": 95,
    "basePower": 60,
    "category": "Physical",
    "name": "Rock Tomb",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spe": -1
      }
    },
    "target": "normal",
    "type": "Rock",
    "contestType": "Clever"
  },
  "rockwrecker": {
    "num": 439,
    "accuracy": 90,
    "basePower": 150,
    "category": "Physical",
    "name": "Rock Wrecker",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "recharge": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "mustrecharge"
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "roleplay": {
    "num": 272,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Role Play",
    "pp": 10,
    "priority": 0,
    "flags": {
      "authentic": 1,
      "mystery": 1
    },
    "onTryHit": "function (target, source) {\n\t\t\tif (target.ability === source.ability)\n\t\t\t\treturn false;\n\t\t\tvar additionalBannedTargetAbilities = [\n\t\t\t\t// Zen Mode included here for compatability with Gen 5-6\n\t\t\t\t'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'wonderguard', 'zenmode',\n\t\t\t];\n\t\t\tif (target.getAbility().isPermanent || additionalBannedTargetAbilities.includes(target.ability) ||\n\t\t\t\tsource.getAbility().isPermanent) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tvar oldAbility = source.setAbility(target.ability);\n\t\t\tif (oldAbility) {\n\t\t\t\tthis.add('-ability', source, source.getAbility().name, '[from] move: Role Play', '[of] ' + target);\n\t\t\t\treturn;\n\t\t\t}\n\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "rollingkick": {
    "num": 27,
    "accuracy": 85,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Rolling Kick",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "rollout": {
    "num": 205,
    "accuracy": 90,
    "basePower": 30,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tvar bp = move.basePower;\n\t\t\tif (pokemon.volatiles['rollout'] && pokemon.volatiles['rollout'].hitCount) {\n\t\t\t\tbp *= Math.pow(2, pokemon.volatiles['rollout'].hitCount);\n\t\t\t}\n\t\t\tif (pokemon.status !== 'slp')\n\t\t\t\tpokemon.addVolatile('rollout');\n\t\t\tif (pokemon.volatiles['defensecurl']) {\n\t\t\t\tbp *= 2;\n\t\t\t}\n\t\t\tthis.debug(\"Rollout bp: \" + bp);\n\t\t\treturn bp;\n\t\t}",
    "category": "Physical",
    "name": "Rollout",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "condition": {
      "duration": 2,
      "onLockMove": "rollout",
      "onStart": "function () {\n\t\t\t\tthis.effectState.hitCount = 1;\n\t\t\t}",
      "onRestart": "function () {\n\t\t\t\tthis.effectState.hitCount++;\n\t\t\t\tif (this.effectState.hitCount < 5) {\n\t\t\t\t\tthis.effectState.duration = 2;\n\t\t\t\t}\n\t\t\t}",
      "onResidual": "function (target) {\n\t\t\t\tif (target.lastMove && target.lastMove.id === 'struggle') {\n\t\t\t\t\t// don't lock\n\t\t\t\t\tdelete target.volatiles['rollout'];\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Cute"
  },
  "roost": {
    "num": 355,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Roost",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "self": {
      "volatileStatus": "roost"
    },
    "condition": {
      "duration": 1,
      "onResidualOrder": 25,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Roost');\n\t\t\t}",
      "onTypePriority": -1,
      "onType": "function (types, pokemon) {\n\t\t\t\tthis.effectState.typeWas = types;\n\t\t\t\treturn types.filter(function (type) { return type !== 'Flying'; });\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Flying",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "rototiller": {
    "num": 563,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Rototiller",
    "pp": 10,
    "priority": 0,
    "flags": {
      "distance": 1,
      "nonsky": 1
    },
    "onHitField": "function (target, source) {\n\t\t\tvar targets = [];\n\t\t\tvar anyAirborne = false;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar pokemon = _a[_i];\n\t\t\t\tif (!pokemon.runImmunity('Ground')) {\n\t\t\t\t\tthis.add('-immune', pokemon);\n\t\t\t\t\tanyAirborne = true;\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (pokemon.hasType('Grass')) {\n\t\t\t\t\t// This move affects every grounded Grass-type Pokemon in play.\n\t\t\t\t\ttargets.push(pokemon);\n\t\t\t\t}\n\t\t\t}\n\t\t\tif (!targets.length && !anyAirborne)\n\t\t\t\treturn false; // Fails when there are no grounded Grass types or airborne Pokemon\n\t\t\tfor (var _b = 0, targets_4 = targets; _b < targets_4.length; _b++) {\n\t\t\t\tvar pokemon = targets_4[_b];\n\t\t\t\tthis.boost({ atk: 1, spa: 1 }, pokemon, source);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "all",
    "type": "Ground",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Tough"
  },
  "round": {
    "num": 496,
    "accuracy": 100,
    "basePower": 60,
    "basePowerCallback": "function (target, source, move) {\n\t\t\tif (move.sourceEffect === 'round') {\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Special",
    "name": "Round",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "onTry": "function (source, target, move) {\n\t\t\tfor (var _i = 0, _a = this.queue.list; _i < _a.length; _i++) {\n\t\t\t\tvar action = _a[_i];\n\t\t\t\tif (!action.pokemon || !action.move || action.maxMove || action.zmove)\n\t\t\t\t\tcontinue;\n\t\t\t\tif (action.move.id === 'round') {\n\t\t\t\t\tthis.queue.prioritizeAction(action, move);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "sacredfire": {
    "num": 221,
    "accuracy": 95,
    "basePower": 100,
    "category": "Physical",
    "name": "Sacred Fire",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "secondary": {
      "chance": 50,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Beautiful"
  },
  "sacredsword": {
    "num": 533,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Sacred Sword",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ignoreEvasion": true,
    "ignoreDefensive": true,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "safeguard": {
    "num": 219,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Safeguard",
    "pp": 25,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "safeguard",
    "condition": {
      "duration": 5,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onSetStatus": "function (status, target, source, effect) {\n\t\t\t\tif (!effect || !source)\n\t\t\t\t\treturn;\n\t\t\t\tif (effect.id === 'yawn')\n\t\t\t\t\treturn;\n\t\t\t\tif (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))\n\t\t\t\t\treturn;\n\t\t\t\tif (target !== source) {\n\t\t\t\t\tthis.debug('interrupting setStatus');\n\t\t\t\t\tif (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {\n\t\t\t\t\t\tthis.add('-activate', target, 'move: Safeguard');\n\t\t\t\t\t}\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}",
      "onTryAddVolatile": "function (status, target, source, effect) {\n\t\t\t\tif (!effect || !source)\n\t\t\t\t\treturn;\n\t\t\t\tif (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))\n\t\t\t\t\treturn;\n\t\t\t\tif ((status.id === 'confusion' || status.id === 'yawn') && target !== source) {\n\t\t\t\t\tif (effect.effectType === 'Move' && !effect.secondaries)\n\t\t\t\t\t\tthis.add('-activate', target, 'move: Safeguard');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'Safeguard');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 3,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'Safeguard');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "sandattack": {
    "num": 28,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Sand Attack",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "accuracy": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Cute"
  },
  "sandstorm": {
    "num": 201,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Sandstorm",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "weather": "Sandstorm",
    "secondary": null,
    "target": "all",
    "type": "Rock",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Tough"
  },
  "sandtomb": {
    "num": 328,
    "accuracy": 85,
    "basePower": 35,
    "category": "Physical",
    "name": "Sand Tomb",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Clever"
  },
  "sappyseed": {
    "num": 738,
    "accuracy": 90,
    "basePower": 100,
    "category": "Physical",
    "isNonstandard": "LGPE",
    "name": "Sappy Seed",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (target.hasType('Grass'))\n\t\t\t\treturn null;\n\t\t\ttarget.addVolatile('leechseed', source);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Clever"
  },
  "savagespinout": {
    "num": 634,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Savage Spin-Out",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "buginiumz",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cool"
  },
  "scald": {
    "num": 503,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Scald",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "thawsTarget": true,
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "scaleshot": {
    "num": 799,
    "accuracy": 90,
    "basePower": 25,
    "category": "Physical",
    "name": "Scale Shot",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "selfBoost": {
      "boosts": {
        "def": -1,
        "spe": 1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    }
  },
  "scaryface": {
    "num": 184,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Scary Face",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "boosts": {
      "spe": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Tough"
  },
  "scorchingsands": {
    "num": 815,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Scorching Sands",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "thawsTarget": true,
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "normal",
    "type": "Ground"
  },
  "scratch": {
    "num": 10,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Scratch",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "screech": {
    "num": 103,
    "accuracy": 85,
    "basePower": 0,
    "category": "Status",
    "name": "Screech",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1,
      "mystery": 1
    },
    "boosts": {
      "def": -2
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Clever"
  },
  "searingshot": {
    "num": 545,
    "accuracy": 100,
    "basePower": 100,
    "category": "Special",
    "name": "Searing Shot",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "allAdjacent",
    "type": "Fire",
    "contestType": "Cool"
  },
  "searingsunrazesmash": {
    "num": 724,
    "accuracy": true,
    "basePower": 200,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Searing Sunraze Smash",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "solganiumz",
    "ignoreAbility": true,
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "secretpower": {
    "num": 290,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Secret Power",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyMove": "function (move, pokemon) {\n\t\t\tif (this.field.isTerrain(''))\n\t\t\t\treturn;\n\t\t\tmove.secondaries = [];\n\t\t\tif (this.field.isTerrain('electricterrain')) {\n\t\t\t\tmove.secondaries.push({\n\t\t\t\t\tchance: 30,\n\t\t\t\t\tstatus: 'par',\n\t\t\t\t});\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('grassyterrain')) {\n\t\t\t\tmove.secondaries.push({\n\t\t\t\t\tchance: 30,\n\t\t\t\t\tstatus: 'slp',\n\t\t\t\t});\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('mistyterrain')) {\n\t\t\t\tmove.secondaries.push({\n\t\t\t\t\tchance: 30,\n\t\t\t\t\tboosts: {\n\t\t\t\t\t\tspa: -1,\n\t\t\t\t\t},\n\t\t\t\t});\n\t\t\t}\n\t\t\telse if (this.field.isTerrain('psychicterrain')) {\n\t\t\t\tmove.secondaries.push({\n\t\t\t\t\tchance: 30,\n\t\t\t\t\tboosts: {\n\t\t\t\t\t\tspe: -1,\n\t\t\t\t\t},\n\t\t\t\t});\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Clever"
  },
  "secretsword": {
    "num": 548,
    "accuracy": 100,
    "basePower": 85,
    "category": "Special",
    "defensiveCategory": "Physical",
    "name": "Secret Sword",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Beautiful"
  },
  "seedbomb": {
    "num": 402,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Seed Bomb",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Tough"
  },
  "seedflare": {
    "num": 465,
    "accuracy": 85,
    "basePower": 120,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Seed Flare",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 40,
      "boosts": {
        "spd": -2
      }
    },
    "target": "normal",
    "type": "Grass",
    "contestType": "Beautiful"
  },
  "seismictoss": {
    "num": 69,
    "accuracy": 100,
    "basePower": 0,
    "damage": "level",
    "category": "Physical",
    "name": "Seismic Toss",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "maxMove": {
      "basePower": 75
    },
    "contestType": "Tough"
  },
  "selfdestruct": {
    "num": 120,
    "accuracy": 100,
    "basePower": 200,
    "category": "Physical",
    "name": "Self-Destruct",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "selfdestruct": "always",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "shadowball": {
    "num": 247,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Shadow Ball",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "boosts": {
        "spd": -1
      }
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "shadowbone": {
    "num": 708,
    "accuracy": 100,
    "basePower": 85,
    "category": "Physical",
    "name": "Shadow Bone",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "shadowclaw": {
    "num": 421,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Shadow Claw",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "shadowforce": {
    "num": 467,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Shadow Force",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "mirror": 1
    },
    "breaksProtect": true,
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "condition": {
      "duration": 2,
      "onInvulnerability": false
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "shadowpunch": {
    "num": 325,
    "accuracy": true,
    "basePower": 60,
    "category": "Physical",
    "name": "Shadow Punch",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "shadowsneak": {
    "num": 425,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Shadow Sneak",
    "pp": 30,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "shadowstrike": {
    "num": 0,
    "accuracy": 95,
    "basePower": 80,
    "category": "Physical",
    "isNonstandard": "CAP",
    "name": "Shadow Strike",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 50,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Clever"
  },
  "sharpen": {
    "num": 159,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Sharpen",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cute"
  },
  "shatteredpsyche": {
    "num": 648,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Shattered Psyche",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "psychiumz",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "contestType": "Cool"
  },
  "sheercold": {
    "num": 329,
    "accuracy": 30,
    "basePower": 0,
    "category": "Special",
    "name": "Sheer Cold",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "ohko": "Ice",
    "target": "normal",
    "type": "Ice",
    "zMove": {
      "basePower": 180
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Beautiful"
  },
  "shellsidearm": {
    "num": 801,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Shell Side Arm",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onPrepareHit": "function (target, source, move) {\n\t\t\tif (!source.isAlly(target)) {\n\t\t\t\tthis.attrLastMove('[anim] Shell Side Arm ' + move.category);\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move, pokemon, target) {\n\t\t\tif (!target)\n\t\t\t\treturn;\n\t\t\tvar atk = pokemon.getStat('atk', false, true);\n\t\t\tvar spa = pokemon.getStat('spa', false, true);\n\t\t\tvar def = target.getStat('def', false, true);\n\t\t\tvar spd = target.getStat('spd', false, true);\n\t\t\tvar physical = Math.floor(Math.floor(Math.floor(Math.floor(2 * pokemon.level / 5 + 2) * 90 * atk) / def) / 50);\n\t\t\tvar special = Math.floor(Math.floor(Math.floor(Math.floor(2 * pokemon.level / 5 + 2) * 90 * spa) / spd) / 50);\n\t\t\tif (physical > special || (physical === special && this.random(2) === 0)) {\n\t\t\t\tmove.category = 'Physical';\n\t\t\t\tmove.flags.contact = 1;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source, move) {\n\t\t\t// Shell Side Arm normally reveals its category via animation on cart, but doesn't play either custom animation against allies\n\t\t\tif (!source.isAlly(target))\n\t\t\t\tthis.hint(move.category + \" Shell Side Arm\");\n\t\t}",
    "onAfterSubDamage": "function (damage, target, source, move) {\n\t\t\tif (!source.isAlly(target))\n\t\t\t\tthis.hint(move.category + \" Shell Side Arm\");\n\t\t}",
    "secondary": {
      "chance": 20,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison"
  },
  "shellsmash": {
    "num": 504,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Shell Smash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": -1,
      "spd": -1,
      "atk": 2,
      "spa": 2,
      "spe": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "shelltrap": {
    "num": 704,
    "accuracy": 100,
    "basePower": 150,
    "category": "Special",
    "name": "Shell Trap",
    "pp": 5,
    "priority": -3,
    "flags": {
      "protect": 1
    },
    "beforeTurnCallback": "function (pokemon) {\n\t\t\tpokemon.addVolatile('shelltrap');\n\t\t}",
    "onTryMove": "function (pokemon) {\n\t\t\tvar _a;\n\t\t\tif (!((_a = pokemon.volatiles['shelltrap']) === null || _a === void 0 ? void 0 : _a.gotHit)) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('cant', pokemon, 'Shell Trap', 'Shell Trap');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'move: Shell Trap');\n\t\t\t}",
      "onHit": "function (pokemon, source, move) {\n\t\t\t\tif (!pokemon.isAlly(source) && move.category === 'Physical') {\n\t\t\t\t\tpokemon.volatiles['shelltrap'].gotHit = true;\n\t\t\t\t\tvar action = this.queue.willMove(pokemon);\n\t\t\t\t\tif (action) {\n\t\t\t\t\t\tthis.queue.prioritizeAction(action);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Fire",
    "contestType": "Tough"
  },
  "shiftgear": {
    "num": 508,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Shift Gear",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spe": 2,
      "atk": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Steel",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "shockwave": {
    "num": 351,
    "accuracy": true,
    "basePower": 60,
    "category": "Special",
    "name": "Shock Wave",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "shoreup": {
    "num": 659,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Shore Up",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tvar factor = 0.5;\n\t\t\tif (this.field.isWeather('sandstorm')) {\n\t\t\t\tfactor = 0.667;\n\t\t\t}\n\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, factor));\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Ground",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "signalbeam": {
    "num": 324,
    "accuracy": 100,
    "basePower": 75,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Signal Beam",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Bug",
    "contestType": "Beautiful"
  },
  "silverwind": {
    "num": 318,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Silver Wind",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "self": {
        "boosts": {
          "atk": 1,
          "def": 1,
          "spa": 1,
          "spd": 1,
          "spe": 1
        }
      }
    },
    "target": "normal",
    "type": "Bug",
    "contestType": "Beautiful"
  },
  "simplebeam": {
    "num": 493,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Simple Beam",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onTryHit": "function (target) {\n\t\t\tif (target.getAbility().isPermanent || target.ability === 'simple' || target.ability === 'truant') {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tvar oldAbility = pokemon.setAbility('simple');\n\t\t\tif (oldAbility) {\n\t\t\t\tthis.add('-ability', pokemon, 'Simple', '[from] move: Simple Beam');\n\t\t\t\treturn;\n\t\t\t}\n\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Cute"
  },
  "sing": {
    "num": 47,
    "accuracy": 55,
    "basePower": 0,
    "category": "Status",
    "name": "Sing",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "sinisterarrowraid": {
    "num": 695,
    "accuracy": true,
    "basePower": 180,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Sinister Arrow Raid",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "decidiumz",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "sizzlyslide": {
    "num": 735,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "LGPE",
    "name": "Sizzly Slide",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "defrost": 1
    },
    "secondary": {
      "chance": 100,
      "status": "brn"
    },
    "target": "normal",
    "type": "Fire",
    "contestType": "Clever"
  },
  "sketch": {
    "num": 166,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Sketch",
    "pp": 1,
    "noPPBoosts": true,
    "priority": 0,
    "flags": {
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar disallowedMoves = ['chatter', 'sketch', 'struggle'];\n\t\t\tvar move = target.lastMove;\n\t\t\tif (source.transformed || !move || source.moves.includes(move.id))\n\t\t\t\treturn false;\n\t\t\tif (disallowedMoves.includes(move.id) || move.isZ || move.isMax)\n\t\t\t\treturn false;\n\t\t\tvar sketchIndex = source.moves.indexOf('sketch');\n\t\t\tif (sketchIndex < 0)\n\t\t\t\treturn false;\n\t\t\tvar sketchedMove = {\n\t\t\t\tmove: move.name,\n\t\t\t\tid: move.id,\n\t\t\t\tpp: move.pp,\n\t\t\t\tmaxpp: move.pp,\n\t\t\t\ttarget: move.target,\n\t\t\t\tdisabled: false,\n\t\t\t\tused: false,\n\t\t\t};\n\t\t\tsource.moveSlots[sketchIndex] = sketchedMove;\n\t\t\tsource.baseMoveSlots[sketchIndex] = sketchedMove;\n\t\t\tthis.add('-activate', source, 'move: Sketch', move.name);\n\t\t}",
    "noSketch": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "skillswap": {
    "num": 285,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Skill Swap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onTryHit": "function (target, source) {\n\t\t\tvar additionalBannedAbilities = ['hungerswitch', 'illusion', 'neutralizinggas', 'wonderguard'];\n\t\t\tif (target.volatiles['dynamax'] ||\n\t\t\t\ttarget.getAbility().isPermanent || source.getAbility().isPermanent ||\n\t\t\t\tadditionalBannedAbilities.includes(target.ability) || additionalBannedAbilities.includes(source.ability)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source, move) {\n\t\t\tvar targetAbility = target.getAbility();\n\t\t\tvar sourceAbility = source.getAbility();\n\t\t\tif (target.isAlly(source)) {\n\t\t\t\tthis.add('-activate', source, 'move: Skill Swap', '', '', '[of] ' + target);\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-activate', source, 'move: Skill Swap', targetAbility, sourceAbility, '[of] ' + target);\n\t\t\t}\n\t\t\tthis.singleEvent('End', sourceAbility, source.abilityState, source);\n\t\t\tthis.singleEvent('End', targetAbility, target.abilityState, target);\n\t\t\tsource.ability = targetAbility.id;\n\t\t\ttarget.ability = sourceAbility.id;\n\t\t\tsource.abilityState = { id: this.toID(source.ability), target: source };\n\t\t\ttarget.abilityState = { id: this.toID(target.ability), target: target };\n\t\t\tif (!target.isAlly(source))\n\t\t\t\ttarget.volatileStaleness = 'external';\n\t\t\tthis.singleEvent('Start', targetAbility, source.abilityState, source);\n\t\t\tthis.singleEvent('Start', sourceAbility, target.abilityState, target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "skittersmack": {
    "num": 806,
    "accuracy": 90,
    "basePower": 70,
    "category": "Physical",
    "name": "Skitter Smack",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spa": -1
      }
    },
    "target": "normal",
    "type": "Bug"
  },
  "skullbash": {
    "num": 130,
    "accuracy": 100,
    "basePower": 130,
    "category": "Physical",
    "name": "Skull Bash",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tthis.boost({ def: 1 }, attacker, attacker, move);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "skyattack": {
    "num": 143,
    "accuracy": 90,
    "basePower": 140,
    "category": "Physical",
    "name": "Sky Attack",
    "pp": 5,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "critRatio": 2,
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "skydrop": {
    "num": 507,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Sky Drop",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1,
      "gravity": 1,
      "distance": 1
    },
    "onModifyMove": "function (move, source) {\n\t\t\tif (!source.volatiles['skydrop']) {\n\t\t\t\tmove.accuracy = true;\n\t\t\t\tmove.flags.contact = 0;\n\t\t\t}\n\t\t}",
    "onMoveFail": "function (target, source) {\n\t\t\tif (source.volatiles['twoturnmove'] && source.volatiles['twoturnmove'].duration === 1) {\n\t\t\t\tsource.removeVolatile('skydrop');\n\t\t\t\tsource.removeVolatile('twoturnmove');\n\t\t\t\tif (target === this.effectState.target) {\n\t\t\t\t\tthis.add('-end', target, 'Sky Drop', '[interrupt]');\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "onTry": "function (source, target) {\n\t\t\treturn !target.fainted;\n\t\t}",
    "onTryHit": "function (target, source, move) {\n\t\t\tif (source.removeVolatile(move.id)) {\n\t\t\t\tif (target !== source.volatiles['twoturnmove'].source)\n\t\t\t\t\treturn false;\n\t\t\t\tif (target.hasType('Flying')) {\n\t\t\t\t\tthis.add('-immune', target);\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\tif (target.volatiles['substitute'] || target.isAlly(source)) {\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tif (target.getWeight() >= 2000) {\n\t\t\t\t\tthis.add('-fail', target, 'move: Sky Drop', '[heavy]');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t\tthis.add('-prepare', source, move.name, target);\n\t\t\t\tsource.addVolatile('twoturnmove', target);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "onHit": "function (target, source) {\n\t\t\tif (target.hp)\n\t\t\t\tthis.add('-end', target, 'Sky Drop');\n\t\t}",
    "condition": {
      "duration": 2,
      "onAnyDragOut": "function (pokemon) {\n\t\t\t\tif (pokemon === this.effectState.target || pokemon === this.effectState.source)\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onFoeTrapPokemonPriority": -15,
      "onFoeTrapPokemon": "function (defender) {\n\t\t\t\tif (defender !== this.effectState.source)\n\t\t\t\t\treturn;\n\t\t\t\tdefender.trapped = true;\n\t\t\t}",
      "onFoeBeforeMovePriority": 12,
      "onFoeBeforeMove": "function (attacker, defender, move) {\n\t\t\t\tif (attacker === this.effectState.source) {\n\t\t\t\t\tattacker.activeMoveActions--;\n\t\t\t\t\tthis.debug('Sky drop nullifying.');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}",
      "onRedirectTargetPriority": 99,
      "onRedirectTarget": "function (target, source, source2) {\n\t\t\t\tif (source !== this.effectState.target)\n\t\t\t\t\treturn;\n\t\t\t\tif (this.effectState.source.fainted)\n\t\t\t\t\treturn;\n\t\t\t\treturn this.effectState.source;\n\t\t\t}",
      "onAnyInvulnerability": "function (target, source, move) {\n\t\t\t\tif (target !== this.effectState.target && target !== this.effectState.source) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (source === this.effectState.target && target === this.effectState.source) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (['gust', 'twister', 'skyuppercut', 'thunder', 'hurricane', 'smackdown', 'thousandarrows'].includes(move.id)) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\treturn false;\n\t\t\t}",
      "onAnyBasePower": "function (basePower, target, source, move) {\n\t\t\t\tif (target !== this.effectState.target && target !== this.effectState.source) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (source === this.effectState.target && target === this.effectState.source) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.id === 'gust' || move.id === 'twister') {\n\t\t\t\t\treturn this.chainModify(2);\n\t\t\t\t}\n\t\t\t}",
      "onFaint": "function (target) {\n\t\t\t\tif (target.volatiles['skydrop'] && target.volatiles['twoturnmove'].source) {\n\t\t\t\t\tthis.add('-end', target.volatiles['twoturnmove'].source, 'Sky Drop', '[interrupt]');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Tough"
  },
  "skyuppercut": {
    "num": 327,
    "accuracy": 90,
    "basePower": 85,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Sky Uppercut",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "slackoff": {
    "num": 303,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Slack Off",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "slam": {
    "num": 21,
    "accuracy": 75,
    "basePower": 80,
    "category": "Physical",
    "name": "Slam",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "slash": {
    "num": 163,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Slash",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "sleeppowder": {
    "num": 79,
    "accuracy": 75,
    "basePower": 0,
    "category": "Status",
    "name": "Sleep Powder",
    "pp": 15,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "sleeptalk": {
    "num": 214,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Sleep Talk",
    "pp": 10,
    "priority": 0,
    "flags": {},
    "sleepUsable": true,
    "onTry": "function (source) {\n\t\t\treturn source.status === 'slp' || source.hasAbility('comatose');\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tvar noSleepTalk = [\n\t\t\t\t'assist', 'beakblast', 'belch', 'bide', 'celebrate', 'chatter', 'copycat', 'dynamaxcannon', 'focuspunch', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'shelltrap', 'sketch', 'sleeptalk', 'uproar',\n\t\t\t];\n\t\t\tvar moves = [];\n\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\tvar moveid = moveSlot.id;\n\t\t\t\tif (!moveid)\n\t\t\t\t\tcontinue;\n\t\t\t\tvar move = this.dex.moves.get(moveid);\n\t\t\t\tif (noSleepTalk.includes(moveid) || move.flags['charge'] || (move.isZ && move.basePower !== 1)) {\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tmoves.push(moveid);\n\t\t\t}\n\t\t\tvar randomMove = '';\n\t\t\tif (moves.length)\n\t\t\t\trandomMove = this.sample(moves);\n\t\t\tif (!randomMove) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.actions.useMove(randomMove, pokemon);\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "crit2"
    },
    "contestType": "Cute"
  },
  "sludge": {
    "num": 124,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Sludge",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "sludgebomb": {
    "num": 188,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Sludge Bomb",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "sludgewave": {
    "num": 482,
    "accuracy": 100,
    "basePower": 95,
    "category": "Special",
    "name": "Sludge Wave",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "psn"
    },
    "target": "allAdjacent",
    "type": "Poison",
    "contestType": "Tough"
  },
  "smackdown": {
    "num": 479,
    "accuracy": 100,
    "basePower": 50,
    "category": "Physical",
    "name": "Smack Down",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "volatileStatus": "smackdown",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon) {\n\t\t\t\tvar applies = false;\n\t\t\t\tif (pokemon.hasType('Flying') || pokemon.hasAbility('levitate'))\n\t\t\t\t\tapplies = true;\n\t\t\t\tif (pokemon.hasItem('ironball') || pokemon.volatiles['ingrain'] ||\n\t\t\t\t\tthis.field.getPseudoWeather('gravity'))\n\t\t\t\t\tapplies = false;\n\t\t\t\tif (pokemon.removeVolatile('fly') || pokemon.removeVolatile('bounce')) {\n\t\t\t\t\tapplies = true;\n\t\t\t\t\tthis.queue.cancelMove(pokemon);\n\t\t\t\t\tpokemon.removeVolatile('twoturnmove');\n\t\t\t\t}\n\t\t\t\tif (pokemon.volatiles['magnetrise']) {\n\t\t\t\t\tapplies = true;\n\t\t\t\t\tdelete pokemon.volatiles['magnetrise'];\n\t\t\t\t}\n\t\t\t\tif (pokemon.volatiles['telekinesis']) {\n\t\t\t\t\tapplies = true;\n\t\t\t\t\tdelete pokemon.volatiles['telekinesis'];\n\t\t\t\t}\n\t\t\t\tif (!applies)\n\t\t\t\t\treturn false;\n\t\t\t\tthis.add('-start', pokemon, 'Smack Down');\n\t\t\t}",
      "onRestart": "function (pokemon) {\n\t\t\t\tif (pokemon.removeVolatile('fly') || pokemon.removeVolatile('bounce')) {\n\t\t\t\t\tthis.queue.cancelMove(pokemon);\n\t\t\t\t\tthis.add('-start', pokemon, 'Smack Down');\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "smartstrike": {
    "num": 684,
    "accuracy": true,
    "basePower": 70,
    "category": "Physical",
    "name": "Smart Strike",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "smellingsalts": {
    "num": 265,
    "accuracy": 100,
    "basePower": 70,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.status === 'par')\n\t\t\t\treturn move.basePower * 2;\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Smelling Salts",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.status === 'par')\n\t\t\t\ttarget.cureStatus();\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "smog": {
    "num": 123,
    "accuracy": 70,
    "basePower": 30,
    "category": "Special",
    "name": "Smog",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 40,
      "status": "psn"
    },
    "target": "normal",
    "type": "Poison",
    "contestType": "Tough"
  },
  "smokescreen": {
    "num": 108,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Smokescreen",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "accuracy": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "evasion": 1
      }
    },
    "contestType": "Clever"
  },
  "snaptrap": {
    "num": 779,
    "accuracy": 100,
    "basePower": 35,
    "category": "Physical",
    "name": "Snap Trap",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Grass"
  },
  "snarl": {
    "num": 555,
    "accuracy": 95,
    "basePower": 55,
    "category": "Special",
    "name": "Snarl",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spa": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Dark",
    "contestType": "Tough"
  },
  "snatch": {
    "num": 289,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Snatch",
    "pp": 10,
    "priority": 4,
    "flags": {
      "authentic": 1
    },
    "volatileStatus": "snatch",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'Snatch');\n\t\t\t}",
      "onAnyPrepareHitPriority": -1,
      "onAnyPrepareHit": "function (source, target, move) {\n\t\t\t\tvar snatchUser = this.effectState.source;\n\t\t\t\tif (snatchUser.isSkyDropped())\n\t\t\t\t\treturn;\n\t\t\t\tif (!move || move.isZ || move.isMax || !move.flags['snatch'] || move.sourceEffect === 'snatch') {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tsnatchUser.removeVolatile('snatch');\n\t\t\t\tthis.add('-activate', snatchUser, 'move: Snatch', '[of] ' + source);\n\t\t\t\tthis.actions.useMove(move.id, snatchUser);\n\t\t\t\treturn null;\n\t\t\t}"
    },
    "secondary": null,
    "pressureTarget": "foeSide",
    "target": "self",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "snipeshot": {
    "num": 745,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Snipe Shot",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "tracksTarget": true,
    "secondary": null,
    "target": "normal",
    "type": "Water"
  },
  "snore": {
    "num": 173,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Snore",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "sleepUsable": true,
    "onTry": "function (source) {\n\t\t\treturn source.status === 'slp' || source.hasAbility('comatose');\n\t\t}",
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "soak": {
    "num": 487,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Soak",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.getTypes().join() === 'Water' || !target.setType('Water')) {\n\t\t\t\t// Soak should animate even when it fails.\n\t\t\t\t// Returning false would suppress the animation.\n\t\t\t\tthis.add('-fail', target);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t\tthis.add('-start', target, 'typechange', 'Water');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Cute"
  },
  "softboiled": {
    "num": 135,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Soft-Boiled",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "heal": [
      1,
      2
    ],
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "solarbeam": {
    "num": 76,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "name": "Solar Beam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (['sunnyday', 'desolateland'].includes(attacker.effectiveWeather())) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.addMove('-anim', attacker, move.name, defender);\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "onBasePower": "function (basePower, pokemon, target) {\n\t\t\tif (['raindance', 'primordialsea', 'sandstorm', 'hail'].includes(pokemon.effectiveWeather())) {\n\t\t\t\tthis.debug('weakened by weather');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "solarblade": {
    "num": 669,
    "accuracy": 100,
    "basePower": 125,
    "category": "Physical",
    "name": "Solar Blade",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "charge": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTryMove": "function (attacker, defender, move) {\n\t\t\tif (attacker.removeVolatile(move.id)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-prepare', attacker, move.name);\n\t\t\tif (['sunnyday', 'desolateland'].includes(attacker.effectiveWeather())) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.addMove('-anim', attacker, move.name, defender);\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (!this.runEvent('ChargeMove', attacker, defender, move)) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tattacker.addVolatile('twoturnmove', defender);\n\t\t\treturn null;\n\t\t}",
    "onBasePower": "function (basePower, pokemon, target) {\n\t\t\tif (['raindance', 'primordialsea', 'sandstorm', 'hail'].includes(pokemon.effectiveWeather())) {\n\t\t\t\tthis.debug('weakened by weather');\n\t\t\t\treturn this.chainModify(0.5);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "sonicboom": {
    "num": 49,
    "accuracy": 90,
    "basePower": 0,
    "damage": 20,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Sonic Boom",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "soulstealing7starstrike": {
    "num": 699,
    "accuracy": true,
    "basePower": 195,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Soul-Stealing 7-Star Strike",
    "pp": 1,
    "priority": 0,
    "flags": {
      "contact": 1
    },
    "isZ": "marshadiumz",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "spacialrend": {
    "num": 460,
    "accuracy": 95,
    "basePower": 100,
    "category": "Special",
    "name": "Spacial Rend",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Dragon",
    "contestType": "Beautiful"
  },
  "spark": {
    "num": 209,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "name": "Spark",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "sparklingaria": {
    "num": 664,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Sparkling Aria",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "secondary": {
      "dustproof": true,
      "chance": 100,
      "onHit": "function (target) {\n\t\t\t\tif (target.status === 'brn')\n\t\t\t\t\ttarget.cureStatus();\n\t\t\t}"
    },
    "target": "allAdjacent",
    "type": "Water",
    "contestType": "Tough"
  },
  "sparklyswirl": {
    "num": 740,
    "accuracy": 85,
    "basePower": 120,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Sparkly Swirl",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "self": {
      "onHit": "function (pokemon, source, move) {\n\t\t\t\tthis.add('-activate', source, 'move: Aromatherapy');\n\t\t\t\tfor (var _i = 0, _a = source.side.pokemon; _i < _a.length; _i++) {\n\t\t\t\t\tvar ally = _a[_i];\n\t\t\t\t\tif (ally !== source && (ally.volatiles['substitute'] && !move.infiltrates)) {\n\t\t\t\t\t\tcontinue;\n\t\t\t\t\t}\n\t\t\t\t\tally.cureStatus();\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Clever"
  },
  "spectralthief": {
    "num": 712,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Spectral Thief",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "authentic": 1
    },
    "stealsBoosts": true,
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "contestType": "Cool"
  },
  "speedswap": {
    "num": 683,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Speed Swap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "onHit": "function (target, source) {\n\t\t\tvar targetSpe = target.storedStats.spe;\n\t\t\ttarget.storedStats.spe = source.storedStats.spe;\n\t\t\tsource.storedStats.spe = targetSpe;\n\t\t\tthis.add('-activate', source, 'move: Speed Swap', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "spiderweb": {
    "num": 169,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Spider Web",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\treturn target.addVolatile('trapped', source, move, 'trapper');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "spikecannon": {
    "num": 131,
    "accuracy": 100,
    "basePower": 20,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Spike Cannon",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "maxMove": {
      "basePower": 120
    },
    "contestType": "Cool"
  },
  "spikes": {
    "num": 191,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Spikes",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "nonsky": 1
    },
    "sideCondition": "spikes",
    "condition": {
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'Spikes');\n\t\t\t\tthis.effectState.layers = 1;\n\t\t\t}",
      "onSideRestart": "function (side) {\n\t\t\t\tif (this.effectState.layers >= 3)\n\t\t\t\t\treturn false;\n\t\t\t\tthis.add('-sidestart', side, 'Spikes');\n\t\t\t\tthis.effectState.layers++;\n\t\t\t}",
      "onSwitchIn": "function (pokemon) {\n\t\t\t\tif (!pokemon.isGrounded())\n\t\t\t\t\treturn;\n\t\t\t\tif (pokemon.hasItem('heavydutyboots'))\n\t\t\t\t\treturn;\n\t\t\t\tvar damageAmounts = [0, 3, 4, 6]; // 1/8, 1/6, 1/4\n\t\t\t\tthis.damage(damageAmounts[this.effectState.layers] * pokemon.maxhp / 24);\n\t\t\t}"
    },
    "secondary": null,
    "target": "foeSide",
    "type": "Ground",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "spikyshield": {
    "num": 596,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Spiky Shield",
    "pp": 10,
    "priority": 4,
    "flags": {},
    "stallingMove": true,
    "volatileStatus": "spikyshield",
    "onPrepareHit": "function (pokemon) {\n\t\t\treturn !!this.queue.willAct() && this.runEvent('StallMove', pokemon);\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tpokemon.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-singleturn', target, 'move: Protect');\n\t\t\t}",
      "onTryHitPriority": 3,
      "onTryHit": "function (target, source, move) {\n\t\t\t\tif (!move.flags['protect']) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\tif (move.isZ || move.isMax)\n\t\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.smartTarget) {\n\t\t\t\t\tmove.smartTarget = false;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Protect');\n\t\t\t\t}\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.damage(source.baseMaxhp / 8, source, target);\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}",
      "onHit": "function (target, source, move) {\n\t\t\t\tif (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {\n\t\t\t\t\tthis.damage(source.baseMaxhp / 8, source, target);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Grass",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "spiritbreak": {
    "num": 789,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Spirit Break",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spa": -1
      }
    },
    "target": "normal",
    "type": "Fairy"
  },
  "spiritshackle": {
    "num": 662,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Spirit Shackle",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "onHit": "function (target, source, move) {\n\t\t\t\tif (source.isActive)\n\t\t\t\t\ttarget.addVolatile('trapped', source, move, 'trapper');\n\t\t\t}"
    },
    "target": "normal",
    "type": "Ghost",
    "contestType": "Tough"
  },
  "spitup": {
    "num": 255,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon) {\n\t\t\tvar _a;\n\t\t\tif (!((_a = pokemon.volatiles['stockpile']) === null || _a === void 0 ? void 0 : _a.layers))\n\t\t\t\treturn false;\n\t\t\treturn pokemon.volatiles['stockpile'].layers * 100;\n\t\t}",
    "category": "Special",
    "name": "Spit Up",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "onTry": "function (source) {\n\t\t\treturn !!source.volatiles['stockpile'];\n\t\t}",
    "onAfterMove": "function (pokemon) {\n\t\t\tpokemon.removeVolatile('stockpile');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "spite": {
    "num": 180,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Spite",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "onHit": "function (target) {\n\t\t\tvar move = target.lastMove;\n\t\t\tif (!move || move.isZ)\n\t\t\t\treturn false;\n\t\t\tif (move.isMax && move.baseMove)\n\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n\t\t\tvar ppDeducted = target.deductPP(move.id, 4);\n\t\t\tif (!ppDeducted)\n\t\t\t\treturn false;\n\t\t\tthis.add(\"-activate\", target, 'move: Spite', move.name, ppDeducted);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Tough"
  },
  "splash": {
    "num": 150,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Splash",
    "pp": 40,
    "priority": 0,
    "flags": {
      "gravity": 1
    },
    "onTry": "function (source, target, move) {\n\t\t\t// Additional Gravity check for Z-move variant\n\t\t\tif (this.field.getPseudoWeather('Gravity')) {\n\t\t\t\tthis.add('cant', source, 'move: Gravity', move);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "onTryHit": "function (target, source) {\n\t\t\tthis.add('-nothing');\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 3
      }
    },
    "contestType": "Cute"
  },
  "splinteredstormshards": {
    "num": 727,
    "accuracy": true,
    "basePower": 190,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Splintered Stormshards",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "onHit": "function () {\n\t\t\tthis.field.clearTerrain();\n\t\t}",
    "onAfterSubDamage": "function () {\n\t\t\tthis.field.clearTerrain();\n\t\t}",
    "isZ": "lycaniumz",
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Cool"
  },
  "splishysplash": {
    "num": 730,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "isNonstandard": "LGPE",
    "name": "Splishy Splash",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1
    },
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "allAdjacentFoes",
    "type": "Water",
    "contestType": "Cool"
  },
  "spore": {
    "num": 147,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Spore",
    "pp": 15,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "slp",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "spotlight": {
    "num": 671,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Spotlight",
    "pp": 15,
    "priority": 3,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mystery": 1
    },
    "volatileStatus": "spotlight",
    "onTryHit": "function (target) {\n\t\t\tif (this.activePerHalf === 1)\n\t\t\t\treturn false;\n\t\t}",
    "condition": {
      "duration": 1,
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-singleturn', pokemon, 'move: Spotlight');\n\t\t\t}",
      "onFoeRedirectTargetPriority": 2,
      "onFoeRedirectTarget": "function (target, source, source2, move) {\n\t\t\t\tif (this.validTarget(this.effectState.target, source, move.target)) {\n\t\t\t\t\tthis.debug(\"Spotlight redirected target of move\");\n\t\t\t\t\treturn this.effectState.target;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "stealthrock": {
    "num": 446,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Stealth Rock",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1
    },
    "sideCondition": "stealthrock",
    "condition": {
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Stealth Rock');\n\t\t\t}",
      "onSwitchIn": "function (pokemon) {\n\t\t\t\tif (pokemon.hasItem('heavydutyboots'))\n\t\t\t\t\treturn;\n\t\t\t\tvar typeMod = this.clampIntRange(pokemon.runEffectiveness(this.dex.getActiveMove('stealthrock')), -6, 6);\n\t\t\t\tthis.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);\n\t\t\t}"
    },
    "secondary": null,
    "target": "foeSide",
    "type": "Rock",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cool"
  },
  "steameruption": {
    "num": 592,
    "accuracy": 95,
    "basePower": 110,
    "category": "Special",
    "name": "Steam Eruption",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "defrost": 1
    },
    "thawsTarget": true,
    "secondary": {
      "chance": 30,
      "status": "brn"
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "steamroller": {
    "num": 537,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Steamroller",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Bug",
    "contestType": "Tough"
  },
  "steelbeam": {
    "num": 796,
    "accuracy": 95,
    "basePower": 140,
    "category": "Special",
    "name": "Steel Beam",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "mindBlownRecoil": true,
    "onAfterMove": "function (pokemon, target, move) {\n\t\t\tif (move.mindBlownRecoil && !move.multihit) {\n\t\t\t\tthis.damage(Math.round(pokemon.maxhp / 2), pokemon, pokemon, this.dex.conditions.get('Steel Beam'), true);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Steel"
  },
  "steelroller": {
    "num": 798,
    "accuracy": 100,
    "basePower": 130,
    "category": "Physical",
    "name": "Steel Roller",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function () {\n\t\t\treturn !this.field.isTerrain('');\n\t\t}",
    "onHit": "function () {\n\t\t\tthis.field.clearTerrain();\n\t\t}",
    "onAfterSubDamage": "function () {\n\t\t\tthis.field.clearTerrain();\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Steel"
  },
  "steelwing": {
    "num": 211,
    "accuracy": 90,
    "basePower": 70,
    "category": "Physical",
    "name": "Steel Wing",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "self": {
        "boosts": {
          "def": 1
        }
      }
    },
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "stickyweb": {
    "num": 564,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Sticky Web",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1
    },
    "sideCondition": "stickyweb",
    "condition": {
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Sticky Web');\n\t\t\t}",
      "onSwitchIn": "function (pokemon) {\n\t\t\t\tif (!pokemon.isGrounded())\n\t\t\t\t\treturn;\n\t\t\t\tif (pokemon.hasItem('heavydutyboots'))\n\t\t\t\t\treturn;\n\t\t\t\tthis.add('-activate', pokemon, 'move: Sticky Web');\n\t\t\t\tthis.boost({ spe: -1 }, pokemon, this.effectState.source, this.dex.getActiveMove('stickyweb'));\n\t\t\t}"
    },
    "secondary": null,
    "pressureTarget": "self",
    "target": "foeSide",
    "type": "Bug",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Tough"
  },
  "stockpile": {
    "num": 254,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Stockpile",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onTry": "function (source) {\n\t\t\tif (source.volatiles['stockpile'] && source.volatiles['stockpile'].layers >= 3)\n\t\t\t\treturn false;\n\t\t}",
    "volatileStatus": "stockpile",
    "condition": {
      "noCopy": true,
      "onStart": "function (target) {\n\t\t\t\tthis.effectState.layers = 1;\n\t\t\t\tthis.effectState.def = 0;\n\t\t\t\tthis.effectState.spd = 0;\n\t\t\t\tthis.add('-start', target, 'stockpile' + this.effectState.layers);\n\t\t\t\tvar _a = [target.boosts.def, target.boosts.spd], curDef = _a[0], curSpD = _a[1];\n\t\t\t\tthis.boost({ def: 1, spd: 1 }, target, target);\n\t\t\t\tif (curDef !== target.boosts.def)\n\t\t\t\t\tthis.effectState.def--;\n\t\t\t\tif (curSpD !== target.boosts.spd)\n\t\t\t\t\tthis.effectState.spd--;\n\t\t\t}",
      "onRestart": "function (target) {\n\t\t\t\tif (this.effectState.layers >= 3)\n\t\t\t\t\treturn false;\n\t\t\t\tthis.effectState.layers++;\n\t\t\t\tthis.add('-start', target, 'stockpile' + this.effectState.layers);\n\t\t\t\tvar curDef = target.boosts.def;\n\t\t\t\tvar curSpD = target.boosts.spd;\n\t\t\t\tthis.boost({ def: 1, spd: 1 }, target, target);\n\t\t\t\tif (curDef !== target.boosts.def)\n\t\t\t\t\tthis.effectState.def--;\n\t\t\t\tif (curSpD !== target.boosts.spd)\n\t\t\t\t\tthis.effectState.spd--;\n\t\t\t}",
      "onEnd": "function (target) {\n\t\t\t\tif (this.effectState.def || this.effectState.spd) {\n\t\t\t\t\tvar boosts = {};\n\t\t\t\t\tif (this.effectState.def)\n\t\t\t\t\t\tboosts.def = this.effectState.def;\n\t\t\t\t\tif (this.effectState.spd)\n\t\t\t\t\t\tboosts.spd = this.effectState.spd;\n\t\t\t\t\tthis.boost(boosts, target, target);\n\t\t\t\t}\n\t\t\t\tthis.add('-end', target, 'Stockpile');\n\t\t\t\tif (this.effectState.def !== this.effectState.layers * -1 || this.effectState.spd !== this.effectState.layers * -1) {\n\t\t\t\t\tthis.hint(\"In Gen 7, Stockpile keeps track of how many times it successfully altered each stat individually.\");\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Tough"
  },
  "stokedsparksurfer": {
    "num": 700,
    "accuracy": true,
    "basePower": 175,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Stoked Sparksurfer",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "aloraichiumz",
    "secondary": {
      "chance": 100,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "stomp": {
    "num": 23,
    "accuracy": 100,
    "basePower": 65,
    "category": "Physical",
    "name": "Stomp",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "stompingtantrum": {
    "num": 707,
    "accuracy": 100,
    "basePower": 75,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (pokemon.moveLastTurnResult === false) {\n\t\t\t\tthis.debug('doubling Stomping Tantrum BP due to previous move failure');\n\t\t\t\treturn move.basePower * 2;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "name": "Stomping Tantrum",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Tough"
  },
  "stoneedge": {
    "num": 444,
    "accuracy": 80,
    "basePower": 100,
    "category": "Physical",
    "name": "Stone Edge",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "critRatio": 2,
    "secondary": null,
    "target": "normal",
    "type": "Rock",
    "contestType": "Tough"
  },
  "storedpower": {
    "num": 500,
    "accuracy": 100,
    "basePower": 20,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn move.basePower + 20 * pokemon.positiveBoosts();\n\t\t}",
    "category": "Special",
    "name": "Stored Power",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Clever"
  },
  "stormthrow": {
    "num": 480,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Storm Throw",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "willCrit": true,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "strangesteam": {
    "num": 790,
    "accuracy": 95,
    "basePower": 90,
    "category": "Special",
    "name": "Strange Steam",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "confusion"
    },
    "target": "normal",
    "type": "Fairy"
  },
  "strength": {
    "num": 70,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Strength",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "strengthsap": {
    "num": 668,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Strength Sap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "heal": 1
    },
    "onHit": "function (target, source) {\n\t\t\tif (target.boosts.atk === -6)\n\t\t\t\treturn false;\n\t\t\tvar atk = target.getStat('atk', false, true);\n\t\t\tvar success = this.boost({ atk: -1 }, target, source, null, false, true);\n\t\t\treturn !!(this.heal(atk, source, target) || success);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "stringshot": {
    "num": 81,
    "accuracy": 95,
    "basePower": 0,
    "category": "Status",
    "name": "String Shot",
    "pp": 40,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "spe": -2
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Bug",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "struggle": {
    "num": 165,
    "accuracy": true,
    "basePower": 50,
    "category": "Physical",
    "name": "Struggle",
    "pp": 1,
    "noPPBoosts": true,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1
    },
    "noSketch": true,
    "onModifyMove": "function (move, pokemon, target) {\n\t\t\tmove.type = '???';\n\t\t\tthis.add('-activate', pokemon, 'move: Struggle');\n\t\t}",
    "struggleRecoil": true,
    "secondary": null,
    "target": "randomNormal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "strugglebug": {
    "num": 522,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Struggle Bug",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "spa": -1
      }
    },
    "target": "allAdjacentFoes",
    "type": "Bug",
    "contestType": "Cute"
  },
  "stuffcheeks": {
    "num": 747,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Stuff Cheeks",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "onTry": "function (source) {\n\t\t\tvar item = source.getItem();\n\t\t\tif (item.isBerry && source.eatItem(true)) {\n\t\t\t\tthis.boost({ def: 2 }, source, null, null, false, true);\n\t\t\t}\n\t\t\telse {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal"
  },
  "stunspore": {
    "num": 78,
    "accuracy": 75,
    "basePower": 0,
    "category": "Status",
    "name": "Stun Spore",
    "pp": 30,
    "priority": 0,
    "flags": {
      "powder": 1,
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "par",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "submission": {
    "num": 66,
    "accuracy": 80,
    "basePower": 80,
    "category": "Physical",
    "name": "Submission",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      4
    ],
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "substitute": {
    "num": 164,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Substitute",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "nonsky": 1
    },
    "volatileStatus": "substitute",
    "onTryHit": "function (target) {\n\t\t\tif (target.volatiles['substitute']) {\n\t\t\t\tthis.add('-fail', target, 'move: Substitute');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t\tif (target.hp <= target.maxhp / 4 || target.maxhp === 1) { // Shedinja clause\n\t\t\t\tthis.add('-fail', target, 'move: Substitute', '[weak]');\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "onHit": "function (target) {\n\t\t\tthis.directDamage(target.maxhp / 4);\n\t\t}",
    "condition": {
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'Substitute');\n\t\t\t\tthis.effectState.hp = Math.floor(target.maxhp / 4);\n\t\t\t\tif (target.volatiles['partiallytrapped']) {\n\t\t\t\t\tthis.add('-end', target, target.volatiles['partiallytrapped'].sourceEffect, '[partiallytrapped]', '[silent]');\n\t\t\t\t\tdelete target.volatiles['partiallytrapped'];\n\t\t\t\t}\n\t\t\t}",
      "onTryPrimaryHitPriority": -1,
      "onTryPrimaryHit": "function (target, source, move) {\n\t\t\t\tif (target === source || move.flags['authentic'] || move.infiltrates) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tvar damage = this.actions.getDamage(source, target, move);\n\t\t\t\tif (!damage && damage !== 0) {\n\t\t\t\t\tthis.add('-fail', source);\n\t\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t\tdamage = this.runEvent('SubDamage', target, source, move, damage);\n\t\t\t\tif (!damage) {\n\t\t\t\t\treturn damage;\n\t\t\t\t}\n\t\t\t\tif (damage > target.volatiles['substitute'].hp) {\n\t\t\t\t\tdamage = target.volatiles['substitute'].hp;\n\t\t\t\t}\n\t\t\t\ttarget.volatiles['substitute'].hp -= damage;\n\t\t\t\tsource.lastDamage = damage;\n\t\t\t\tif (target.volatiles['substitute'].hp <= 0) {\n\t\t\t\t\tif (move.ohko)\n\t\t\t\t\t\tthis.add('-ohko');\n\t\t\t\t\ttarget.removeVolatile('substitute');\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tthis.add('-activate', target, 'move: Substitute', '[damage]');\n\t\t\t\t}\n\t\t\t\tif (move.recoil) {\n\t\t\t\t\tthis.damage(this.actions.calcRecoilDamage(damage, move), source, target, 'recoil');\n\t\t\t\t}\n\t\t\t\tif (move.drain) {\n\t\t\t\t\tthis.heal(Math.ceil(damage * move.drain[0] / move.drain[1]), source, target, 'drain');\n\t\t\t\t}\n\t\t\t\tthis.singleEvent('AfterSubDamage', move, null, target, source, move, damage);\n\t\t\t\tthis.runEvent('AfterSubDamage', target, source, move, damage);\n\t\t\t\treturn this.HIT_SUBSTITUTE;\n\t\t\t}",
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Substitute');\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "subzeroslammer": {
    "num": 650,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Subzero Slammer",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "iciumz",
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "contestType": "Cool"
  },
  "suckerpunch": {
    "num": 389,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Sucker Punch",
    "pp": 5,
    "priority": 1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onTry": "function (source, target) {\n\t\t\tvar action = this.queue.willMove(target);\n\t\t\tvar move = (action === null || action === void 0 ? void 0 : action.choice) === 'move' ? action.move : null;\n\t\t\tif (!move || (move.category === 'Status' && move.id !== 'mefirst') || target.volatiles['mustrecharge']) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "sunnyday": {
    "num": 241,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Sunny Day",
    "pp": 5,
    "priority": 0,
    "flags": {},
    "weather": "sunnyday",
    "secondary": null,
    "target": "all",
    "type": "Fire",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Beautiful"
  },
  "sunsteelstrike": {
    "num": 713,
    "accuracy": 100,
    "basePower": 100,
    "category": "Physical",
    "name": "Sunsteel Strike",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "ignoreAbility": true,
    "secondary": null,
    "target": "normal",
    "type": "Steel",
    "contestType": "Cool"
  },
  "superfang": {
    "num": 162,
    "accuracy": 90,
    "basePower": 0,
    "damageCallback": "function (pokemon, target) {\n\t\t\treturn this.clampIntRange(target.getUndynamaxedHP() / 2, 1);\n\t\t}",
    "category": "Physical",
    "name": "Super Fang",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "superpower": {
    "num": 276,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Superpower",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "atk": -1,
        "def": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "supersonic": {
    "num": 48,
    "accuracy": 55,
    "basePower": 0,
    "category": "Status",
    "name": "Supersonic",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "volatileStatus": "confusion",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "supersonicskystrike": {
    "num": 626,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Supersonic Skystrike",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "flyiniumz",
    "secondary": null,
    "target": "normal",
    "type": "Flying",
    "contestType": "Cool"
  },
  "surf": {
    "num": 57,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Surf",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "secondary": null,
    "target": "allAdjacent",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "surgingstrikes": {
    "num": 818,
    "accuracy": 100,
    "basePower": 25,
    "category": "Physical",
    "name": "Surging Strikes",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "punch": 1,
      "mirror": 1
    },
    "willCrit": true,
    "multihit": 3,
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    }
  },
  "swagger": {
    "num": 207,
    "accuracy": 85,
    "basePower": 0,
    "category": "Status",
    "name": "Swagger",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "volatileStatus": "confusion",
    "boosts": {
      "atk": 2
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Cute"
  },
  "swallow": {
    "num": 256,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Swallow",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onTry": "function (source) {\n\t\t\treturn !!source.volatiles['stockpile'];\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tvar healAmount = [0.25, 0.5, 1];\n\t\t\tvar healedBy = this.heal(this.modify(pokemon.maxhp, healAmount[(pokemon.volatiles['stockpile'].layers - 1)]));\n\t\t\tpokemon.removeVolatile('stockpile');\n\t\t\treturn !!healedBy;\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Tough"
  },
  "sweetkiss": {
    "num": 186,
    "accuracy": 75,
    "basePower": 0,
    "category": "Status",
    "name": "Sweet Kiss",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "confusion",
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Cute"
  },
  "sweetscent": {
    "num": 230,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Sweet Scent",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "evasion": -2
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Cute"
  },
  "swift": {
    "num": 129,
    "accuracy": true,
    "basePower": 60,
    "category": "Special",
    "name": "Swift",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "contestType": "Cool"
  },
  "switcheroo": {
    "num": 415,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Switcheroo",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onTryImmunity": "function (target) {\n\t\t\treturn !target.hasAbility('stickyhold');\n\t\t}",
    "onHit": "function (target, source, move) {\n\t\t\tvar yourItem = target.takeItem(source);\n\t\t\tvar myItem = source.takeItem();\n\t\t\tif (target.item || source.item || (!yourItem && !myItem)) {\n\t\t\t\tif (yourItem)\n\t\t\t\t\ttarget.item = yourItem.id;\n\t\t\t\tif (myItem)\n\t\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tif ((myItem && !this.singleEvent('TakeItem', myItem, source.itemState, target, source, move, myItem)) ||\n\t\t\t\t(yourItem && !this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem))) {\n\t\t\t\tif (yourItem)\n\t\t\t\t\ttarget.item = yourItem.id;\n\t\t\t\tif (myItem)\n\t\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.add('-activate', source, 'move: Trick', '[of] ' + target);\n\t\t\tif (myItem) {\n\t\t\t\ttarget.setItem(myItem);\n\t\t\t\tthis.add('-item', target, myItem, '[from] move: Switcheroo');\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-enditem', target, yourItem, '[silent]', '[from] move: Switcheroo');\n\t\t\t}\n\t\t\tif (yourItem) {\n\t\t\t\tsource.setItem(yourItem);\n\t\t\t\tthis.add('-item', source, yourItem, '[from] move: Switcheroo');\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-enditem', source, myItem, '[silent]', '[from] move: Switcheroo');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "swordsdance": {
    "num": 14,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Swords Dance",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "dance": 1
    },
    "boosts": {
      "atk": 2
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "synchronoise": {
    "num": 485,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Synchronoise",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onTryImmunity": "function (target, source) {\n\t\t\treturn target.hasType(source.getTypes());\n\t\t}",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "synthesis": {
    "num": 235,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Synthesis",
    "pp": 5,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "onHit": "function (pokemon) {\n\t\t\tvar factor = 0.5;\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tfactor = 0.667;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\tcase 'sandstorm':\n\t\t\t\tcase 'hail':\n\t\t\t\t\tfactor = 0.25;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, factor));\n\t\t}",
    "secondary": null,
    "target": "self",
    "type": "Grass",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Clever"
  },
  "tackle": {
    "num": 33,
    "accuracy": 100,
    "basePower": 40,
    "category": "Physical",
    "name": "Tackle",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "tailglow": {
    "num": 294,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Tail Glow",
    "pp": 20,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "spa": 3
    },
    "secondary": null,
    "target": "self",
    "type": "Bug",
    "zMove": {
      "effect": "clearnegativeboost"
    },
    "contestType": "Beautiful"
  },
  "tailslap": {
    "num": 541,
    "accuracy": 85,
    "basePower": 25,
    "category": "Physical",
    "name": "Tail Slap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 140
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cute"
  },
  "tailwhip": {
    "num": 39,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Tail Whip",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "def": -1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Cute"
  },
  "tailwind": {
    "num": 366,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Tailwind",
    "pp": 15,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "tailwind",
    "condition": {
      "duration": 4,
      "durationCallback": "function (target, source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 6;\n\t\t\t\t}\n\t\t\t\treturn 4;\n\t\t\t}",
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Tailwind');\n\t\t\t}",
      "onModifySpe": "function (spe, pokemon) {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 5,
      "onSideEnd": "function (side) {\n\t\t\t\tthis.add('-sideend', side, 'move: Tailwind');\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Flying",
    "zMove": {
      "effect": "crit2"
    },
    "contestType": "Cool"
  },
  "takedown": {
    "num": 36,
    "accuracy": 85,
    "basePower": 90,
    "category": "Physical",
    "name": "Take Down",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      4
    ],
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "tarshot": {
    "num": 749,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Tar Shot",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "tarshot",
    "condition": {
      "onStart": "function (pokemon) {\n\t\t\t\tthis.add('-start', pokemon, 'Tar Shot');\n\t\t\t}",
      "onEffectivenessPriority": -2,
      "onEffectiveness": "function (typeMod, target, type, move) {\n\t\t\t\tif (move.type !== 'Fire')\n\t\t\t\t\treturn;\n\t\t\t\tif (!target)\n\t\t\t\t\treturn;\n\t\t\t\tif (type !== target.getTypes()[0])\n\t\t\t\t\treturn;\n\t\t\t\treturn typeMod + 1;\n\t\t\t}"
    },
    "boosts": {
      "spe": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Rock"
  },
  "taunt": {
    "num": 269,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Taunt",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "taunt",
    "condition": {
      "duration": 3,
      "onStart": "function (target) {\n\t\t\t\tif (target.activeTurns && !this.queue.willMove(target)) {\n\t\t\t\t\tthis.effectState.duration++;\n\t\t\t\t}\n\t\t\t\tthis.add('-start', target, 'move: Taunt');\n\t\t\t}",
      "onResidualOrder": 15,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'move: Taunt');\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tvar move = this.dex.moves.get(moveSlot.id);\n\t\t\t\t\tif (move.category === 'Status' && move.id !== 'mefirst') {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 5,
      "onBeforeMove": "function (attacker, defender, move) {\n\t\t\t\tif (!move.isZ && !move.isMax && move.category === 'Status' && move.id !== 'mefirst') {\n\t\t\t\t\tthis.add('cant', attacker, 'move: Taunt', move);\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Clever"
  },
  "tearfullook": {
    "num": 715,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Tearful Look",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "mirror": 1
    },
    "boosts": {
      "atk": -1,
      "spa": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "teatime": {
    "num": 752,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Teatime",
    "pp": 10,
    "priority": 0,
    "flags": {
      "authentic": 1
    },
    "onHitField": "function (target, source, move) {\n\t\t\tvar result = false;\n\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {\n\t\t\t\tvar active = _a[_i];\n\t\t\t\tif (this.runEvent('Invulnerability', active, source, move) === false) {\n\t\t\t\t\tthis.add('-miss', source, active);\n\t\t\t\t\tresult = true;\n\t\t\t\t}\n\t\t\t\telse if (this.runEvent('TryHit', active, source, move)) {\n\t\t\t\t\tvar item = active.getItem();\n\t\t\t\t\tif (active.hp && item.isBerry) {\n\t\t\t\t\t\t// bypasses Unnerve\n\t\t\t\t\t\tactive.eatItem(true);\n\t\t\t\t\t\tresult = true;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t\treturn result;\n\t\t}",
    "secondary": null,
    "target": "all",
    "type": "Normal"
  },
  "technoblast": {
    "num": 546,
    "accuracy": 100,
    "basePower": 120,
    "category": "Special",
    "name": "Techno Blast",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (pokemon.ignoringItem())\n\t\t\t\treturn;\n\t\t\tmove.type = this.runEvent('Drive', pokemon, null, move, 'Normal');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cool"
  },
  "tectonicrage": {
    "num": 630,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Tectonic Rage",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "groundiumz",
    "secondary": null,
    "target": "normal",
    "type": "Ground",
    "contestType": "Cool"
  },
  "teeterdance": {
    "num": 298,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Teeter Dance",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "dance": 1
    },
    "volatileStatus": "confusion",
    "secondary": null,
    "target": "allAdjacent",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Cute"
  },
  "telekinesis": {
    "num": 477,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Telekinesis",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "gravity": 1,
      "mystery": 1
    },
    "volatileStatus": "telekinesis",
    "onTry": "function (source, target, move) {\n\t\t\t// Additional Gravity check for Z-move variant\n\t\t\tif (this.field.getPseudoWeather('Gravity')) {\n\t\t\t\tthis.attrLastMove('[still]');\n\t\t\t\tthis.add('cant', source, 'move: Gravity', move);\n\t\t\t\treturn null;\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 3,
      "onStart": "function (target) {\n\t\t\t\tif (['Diglett', 'Dugtrio', 'Palossand', 'Sandygast'].includes(target.baseSpecies.baseSpecies) ||\n\t\t\t\t\ttarget.baseSpecies.name === 'Gengar-Mega') {\n\t\t\t\t\tthis.add('-immune', target);\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t\tif (target.volatiles['smackdown'] || target.volatiles['ingrain'])\n\t\t\t\t\treturn false;\n\t\t\t\tthis.add('-start', target, 'Telekinesis');\n\t\t\t}",
      "onAccuracyPriority": -1,
      "onAccuracy": "function (accuracy, target, source, move) {\n\t\t\t\tif (move && !move.ohko)\n\t\t\t\t\treturn true;\n\t\t\t}",
      "onImmunity": "function (type) {\n\t\t\t\tif (type === 'Ground')\n\t\t\t\t\treturn false;\n\t\t\t}",
      "onUpdate": "function (pokemon) {\n\t\t\t\tif (pokemon.baseSpecies.name === 'Gengar-Mega') {\n\t\t\t\t\tdelete pokemon.volatiles['telekinesis'];\n\t\t\t\t\tthis.add('-end', pokemon, 'Telekinesis', '[silent]');\n\t\t\t\t}\n\t\t\t}",
      "onResidualOrder": 19,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Telekinesis');\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spa": 1
      }
    },
    "contestType": "Clever"
  },
  "teleport": {
    "num": 100,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Teleport",
    "pp": 20,
    "priority": -6,
    "flags": {},
    "selfSwitch": true,
    "onTryHit": true,
    "secondary": null,
    "target": "self",
    "type": "Psychic",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Cool"
  },
  "terrainpulse": {
    "num": 805,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Terrain Pulse",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "pulse": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tif (!pokemon.isGrounded())\n\t\t\t\treturn;\n\t\t\tswitch (this.field.terrain) {\n\t\t\t\tcase 'electricterrain':\n\t\t\t\t\tmove.type = 'Electric';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'grassyterrain':\n\t\t\t\t\tmove.type = 'Grass';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'mistyterrain':\n\t\t\t\t\tmove.type = 'Fairy';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'psychicterrain':\n\t\t\t\t\tmove.type = 'Psychic';\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move, pokemon) {\n\t\t\tif (this.field.terrain && pokemon.isGrounded()) {\n\t\t\t\tmove.basePower *= 2;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    }
  },
  "thief": {
    "num": 168,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Thief",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onAfterHit": "function (target, source, move) {\n\t\t\tif (source.item || source.volatiles['gem']) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tvar yourItem = target.takeItem(source);\n\t\t\tif (!yourItem) {\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tif (!this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem) ||\n\t\t\t\t!source.setItem(yourItem)) {\n\t\t\t\ttarget.item = yourItem.id; // bypass setItem so we don't break choicelock or anything\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tthis.add('-enditem', target, yourItem, '[silent]', '[from] move: Thief', '[of] ' + source);\n\t\t\tthis.add('-item', source, yourItem, '[from] move: Thief', '[of] ' + target);\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "contestType": "Tough"
  },
  "thousandarrows": {
    "num": 614,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Thousand Arrows",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onEffectiveness": "function (typeMod, target, type, move) {\n\t\t\tif (move.type !== 'Ground')\n\t\t\t\treturn;\n\t\t\tif (!target)\n\t\t\t\treturn; // avoid crashing when called from a chat plugin\n\t\t\t// ignore effectiveness if the target is Flying type and immune to Ground\n\t\t\tif (!target.runImmunity('Ground')) {\n\t\t\t\tif (target.hasType('Flying'))\n\t\t\t\t\treturn 0;\n\t\t\t}\n\t\t}",
    "volatileStatus": "smackdown",
    "ignoreImmunity": {
      "Ground": true
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Ground",
    "zMove": {
      "basePower": 180
    },
    "contestType": "Beautiful"
  },
  "thousandwaves": {
    "num": 615,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Thousand Waves",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tif (source.isActive)\n\t\t\t\ttarget.addVolatile('trapped', source, move, 'trapper');\n\t\t}",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Ground",
    "contestType": "Tough"
  },
  "thrash": {
    "num": 37,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Thrash",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "volatileStatus": "lockedmove"
    },
    "onAfterMove": "function (pokemon) {\n\t\t\tif (pokemon.volatiles['lockedmove'] && pokemon.volatiles['lockedmove'].duration === 1) {\n\t\t\t\tpokemon.removeVolatile('lockedmove');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "randomNormal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "throatchop": {
    "num": 675,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Throat Chop",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "condition": {
      "duration": 2,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'Throat Chop', '[silent]');\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {\n\t\t\t\t\tvar moveSlot = _a[_i];\n\t\t\t\t\tif (this.dex.moves.get(moveSlot.id).flags['sound']) {\n\t\t\t\t\t\tpokemon.disableMove(moveSlot.id);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}",
      "onBeforeMovePriority": 6,
      "onBeforeMove": "function (pokemon, target, move) {\n\t\t\t\tif (!move.isZ && !move.isMax && move.flags['sound']) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Throat Chop');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onModifyMove": "function (move, pokemon, target) {\n\t\t\t\tif (!move.isZ && !move.isMax && move.flags['sound']) {\n\t\t\t\t\tthis.add('cant', pokemon, 'move: Throat Chop');\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t}",
      "onResidualOrder": 22,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Throat Chop', '[silent]');\n\t\t\t}"
    },
    "secondary": {
      "chance": 100,
      "onHit": "function (target) {\n\t\t\t\ttarget.addVolatile('throatchop');\n\t\t\t}"
    },
    "target": "normal",
    "type": "Dark",
    "contestType": "Clever"
  },
  "thunder": {
    "num": 87,
    "accuracy": 70,
    "basePower": 110,
    "category": "Special",
    "name": "Thunder",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onModifyMove": "function (move, pokemon, target) {\n\t\t\tswitch (target === null || target === void 0 ? void 0 : target.effectiveWeather()) {\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\t\tmove.accuracy = true;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tmove.accuracy = 50;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t}",
    "secondary": {
      "chance": 30,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "thunderbolt": {
    "num": 85,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Thunderbolt",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "thundercage": {
    "num": 819,
    "accuracy": 90,
    "basePower": 80,
    "category": "Special",
    "name": "Thunder Cage",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Electric"
  },
  "thunderfang": {
    "num": 422,
    "accuracy": 95,
    "basePower": 65,
    "category": "Physical",
    "name": "Thunder Fang",
    "pp": 15,
    "priority": 0,
    "flags": {
      "bite": 1,
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondaries": [
      {
        "chance": 10,
        "status": "par"
      },
      {
        "chance": 10,
        "volatileStatus": "flinch"
      }
    ],
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "thunderouskick": {
    "num": 823,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Thunderous Kick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "def": -1
      }
    },
    "target": "normal",
    "type": "Fighting"
  },
  "thunderpunch": {
    "num": 9,
    "accuracy": 100,
    "basePower": 75,
    "category": "Physical",
    "name": "Thunder Punch",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "punch": 1
    },
    "secondary": {
      "chance": 10,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "thundershock": {
    "num": 84,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Thunder Shock",
    "pp": 30,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 10,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "thunderwave": {
    "num": 86,
    "accuracy": 90,
    "basePower": 0,
    "category": "Status",
    "name": "Thunder Wave",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "par",
    "ignoreImmunity": false,
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cool"
  },
  "tickle": {
    "num": 321,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Tickle",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "boosts": {
      "atk": -1,
      "def": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "topsyturvy": {
    "num": 576,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Topsy-Turvy",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tvar success = false;\n\t\t\tvar i;\n\t\t\tfor (i in target.boosts) {\n\t\t\t\tif (target.boosts[i] === 0)\n\t\t\t\t\tcontinue;\n\t\t\t\ttarget.boosts[i] = -target.boosts[i];\n\t\t\t\tsuccess = true;\n\t\t\t}\n\t\t\tif (!success)\n\t\t\t\treturn false;\n\t\t\tthis.add('-invertboost', target, '[from] move: Topsy-Turvy');\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Clever"
  },
  "torment": {
    "num": 259,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Torment",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1
    },
    "volatileStatus": "torment",
    "condition": {
      "noCopy": true,
      "onStart": "function (pokemon) {\n\t\t\t\tif (pokemon.volatiles['dynamax']) {\n\t\t\t\t\tdelete pokemon.volatiles['torment'];\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\t\tthis.add('-start', pokemon, 'Torment');\n\t\t\t}",
      "onEnd": "function (pokemon) {\n\t\t\t\tthis.add('-end', pokemon, 'Torment');\n\t\t\t}",
      "onDisableMove": "function (pokemon) {\n\t\t\t\tif (pokemon.lastMove && pokemon.lastMove.id !== 'struggle')\n\t\t\t\t\tpokemon.disableMove(pokemon.lastMove.id);\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Dark",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "toxic": {
    "num": 92,
    "accuracy": 90,
    "basePower": 0,
    "category": "Status",
    "name": "Toxic",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "tox",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "toxicspikes": {
    "num": 390,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Toxic Spikes",
    "pp": 20,
    "priority": 0,
    "flags": {
      "reflectable": 1,
      "nonsky": 1
    },
    "sideCondition": "toxicspikes",
    "condition": {
      "onSideStart": "function (side) {\n\t\t\t\tthis.add('-sidestart', side, 'move: Toxic Spikes');\n\t\t\t\tthis.effectState.layers = 1;\n\t\t\t}",
      "onSideRestart": "function (side) {\n\t\t\t\tif (this.effectState.layers >= 2)\n\t\t\t\t\treturn false;\n\t\t\t\tthis.add('-sidestart', side, 'move: Toxic Spikes');\n\t\t\t\tthis.effectState.layers++;\n\t\t\t}",
      "onSwitchIn": "function (pokemon) {\n\t\t\t\tif (!pokemon.isGrounded())\n\t\t\t\t\treturn;\n\t\t\t\tif (pokemon.hasType('Poison')) {\n\t\t\t\t\tthis.add('-sideend', pokemon.side, 'move: Toxic Spikes', '[of] ' + pokemon);\n\t\t\t\t\tpokemon.side.removeSideCondition('toxicspikes');\n\t\t\t\t}\n\t\t\t\telse if (pokemon.hasType('Steel') || pokemon.hasItem('heavydutyboots')) {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\telse if (this.effectState.layers >= 2) {\n\t\t\t\t\tpokemon.trySetStatus('tox', pokemon.side.foe.active[0]);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tpokemon.trySetStatus('psn', pokemon.side.foe.active[0]);\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "foeSide",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "toxicthread": {
    "num": 672,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Toxic Thread",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "psn",
    "boosts": {
      "spe": -1
    },
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Tough"
  },
  "transform": {
    "num": 144,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Transform",
    "pp": 10,
    "priority": 0,
    "flags": {
      "mystery": 1
    },
    "onHit": "function (target, pokemon) {\n\t\t\tif (!pokemon.transformInto(target)) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "effect": "heal"
    },
    "contestType": "Clever"
  },
  "triattack": {
    "num": 161,
    "accuracy": 100,
    "basePower": 80,
    "category": "Special",
    "name": "Tri Attack",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "onHit": "function (target, source) {\n\t\t\t\tvar result = this.random(3);\n\t\t\t\tif (result === 0) {\n\t\t\t\t\ttarget.trySetStatus('brn', source);\n\t\t\t\t}\n\t\t\t\telse if (result === 1) {\n\t\t\t\t\ttarget.trySetStatus('par', source);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\ttarget.trySetStatus('frz', source);\n\t\t\t\t}\n\t\t\t}"
    },
    "target": "normal",
    "type": "Normal",
    "contestType": "Beautiful"
  },
  "trick": {
    "num": 271,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Trick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onTryImmunity": "function (target) {\n\t\t\treturn !target.hasAbility('stickyhold');\n\t\t}",
    "onHit": "function (target, source, move) {\n\t\t\tvar yourItem = target.takeItem(source);\n\t\t\tvar myItem = source.takeItem();\n\t\t\tif (target.item || source.item || (!yourItem && !myItem)) {\n\t\t\t\tif (yourItem)\n\t\t\t\t\ttarget.item = yourItem.id;\n\t\t\t\tif (myItem)\n\t\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tif ((myItem && !this.singleEvent('TakeItem', myItem, source.itemState, target, source, move, myItem)) ||\n\t\t\t\t(yourItem && !this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem))) {\n\t\t\t\tif (yourItem)\n\t\t\t\t\ttarget.item = yourItem.id;\n\t\t\t\tif (myItem)\n\t\t\t\t\tsource.item = myItem.id;\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\tthis.add('-activate', source, 'move: Trick', '[of] ' + target);\n\t\t\tif (myItem) {\n\t\t\t\ttarget.setItem(myItem);\n\t\t\t\tthis.add('-item', target, myItem, '[from] move: Trick');\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-enditem', target, yourItem, '[silent]', '[from] move: Trick');\n\t\t\t}\n\t\t\tif (yourItem) {\n\t\t\t\tsource.setItem(yourItem);\n\t\t\t\tthis.add('-item', source, yourItem, '[from] move: Trick');\n\t\t\t}\n\t\t\telse {\n\t\t\t\tthis.add('-enditem', source, myItem, '[silent]', '[from] move: Trick');\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spe": 2
      }
    },
    "contestType": "Clever"
  },
  "trickortreat": {
    "num": 567,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Trick-or-Treat",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.hasType('Ghost'))\n\t\t\t\treturn false;\n\t\t\tif (!target.addType('Ghost'))\n\t\t\t\treturn false;\n\t\t\tthis.add('-start', target, 'typeadd', 'Ghost', '[from] move: Trick-or-Treat');\n\t\t\tif (target.side.active.length === 2 && target.position === 1) {\n\t\t\t\t// Curse Glitch\n\t\t\t\tvar action = this.queue.willMove(target);\n\t\t\t\tif (action && action.move.id === 'curse') {\n\t\t\t\t\taction.targetLoc = -1;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Ghost",
    "zMove": {
      "boost": {
        "atk": 1,
        "def": 1,
        "spa": 1,
        "spd": 1,
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "trickroom": {
    "num": 433,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Trick Room",
    "pp": 5,
    "priority": -7,
    "flags": {
      "mirror": 1
    },
    "pseudoWeather": "trickroom",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onFieldStart": "function (target, source) {\n\t\t\t\tthis.add('-fieldstart', 'move: Trick Room', '[of] ' + source);\n\t\t\t}",
      "onFieldRestart": "function (target, source) {\n\t\t\t\tthis.field.removePseudoWeather('trickroom');\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 1,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Trick Room');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "accuracy": 1
      }
    },
    "contestType": "Clever"
  },
  "tripleaxel": {
    "num": 813,
    "accuracy": 90,
    "basePower": 20,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn 20 * move.hit;\n\t\t}",
    "category": "Physical",
    "name": "Triple Axel",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 3,
    "multiaccuracy": true,
    "secondary": null,
    "target": "normal",
    "type": "Ice",
    "zMove": {
      "basePower": 120
    },
    "maxMove": {
      "basePower": 140
    }
  },
  "triplekick": {
    "num": 167,
    "accuracy": 90,
    "basePower": 10,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn 10 * move.hit;\n\t\t}",
    "category": "Physical",
    "name": "Triple Kick",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "multihit": 3,
    "multiaccuracy": true,
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "zMove": {
      "basePower": 120
    },
    "maxMove": {
      "basePower": 80
    },
    "contestType": "Cool"
  },
  "tropkick": {
    "num": 688,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "Trop Kick",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "boosts": {
        "atk": -1
      }
    },
    "target": "normal",
    "type": "Grass",
    "contestType": "Cute"
  },
  "trumpcard": {
    "num": 376,
    "accuracy": true,
    "basePower": 0,
    "basePowerCallback": "function (source, target, move) {\n\t\t\tvar callerMoveId = move.sourceEffect || move.id;\n\t\t\tvar moveSlot = callerMoveId === 'instruct' ? source.getMoveData(move.id) : source.getMoveData(callerMoveId);\n\t\t\tif (!moveSlot)\n\t\t\t\treturn 40;\n\t\t\tswitch (moveSlot.pp) {\n\t\t\t\tcase 0:\n\t\t\t\t\treturn 200;\n\t\t\t\tcase 1:\n\t\t\t\t\treturn 80;\n\t\t\t\tcase 2:\n\t\t\t\t\treturn 60;\n\t\t\t\tcase 3:\n\t\t\t\t\treturn 50;\n\t\t\t\tdefault:\n\t\t\t\t\treturn 40;\n\t\t\t}\n\t\t}",
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Trump Card",
    "pp": 5,
    "noPPBoosts": true,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Cool"
  },
  "twineedle": {
    "num": 41,
    "accuracy": 100,
    "basePower": 25,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Twineedle",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": 2,
    "secondary": {
      "chance": 20,
      "status": "psn"
    },
    "target": "normal",
    "type": "Bug",
    "maxMove": {
      "basePower": 100
    },
    "contestType": "Cool"
  },
  "twinkletackle": {
    "num": 656,
    "accuracy": true,
    "basePower": 1,
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Twinkle Tackle",
    "pp": 1,
    "priority": 0,
    "flags": {},
    "isZ": "fairiumz",
    "secondary": null,
    "target": "normal",
    "type": "Fairy",
    "contestType": "Cool"
  },
  "twister": {
    "num": 239,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Twister",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "allAdjacentFoes",
    "type": "Dragon",
    "contestType": "Cool"
  },
  "uturn": {
    "num": 369,
    "accuracy": 100,
    "basePower": 70,
    "category": "Physical",
    "name": "U-turn",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "selfSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cute"
  },
  "uproar": {
    "num": 253,
    "accuracy": 100,
    "basePower": 90,
    "category": "Special",
    "name": "Uproar",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "sound": 1,
      "authentic": 1
    },
    "self": {
      "volatileStatus": "uproar"
    },
    "onTryHit": "function (target) {\n\t\t\tvar activeTeam = target.side.activeTeam();\n\t\t\tvar foeActiveTeam = target.side.foe.activeTeam();\n\t\t\tfor (var _i = 0, _a = activeTeam.entries(); _i < _a.length; _i++) {\n\t\t\t\tvar _b = _a[_i], i = _b[0], allyActive = _b[1];\n\t\t\t\tif (allyActive && allyActive.status === 'slp')\n\t\t\t\t\tallyActive.cureStatus();\n\t\t\t\tvar foeActive = foeActiveTeam[i];\n\t\t\t\tif (foeActive && foeActive.status === 'slp')\n\t\t\t\t\tfoeActive.cureStatus();\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 3,
      "onStart": "function (target) {\n\t\t\t\tthis.add('-start', target, 'Uproar');\n\t\t\t}",
      "onResidual": "function (target) {\n\t\t\t\tif (target.volatiles['throatchop']) {\n\t\t\t\t\ttarget.removeVolatile('uproar');\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (target.lastMove && target.lastMove.id === 'struggle') {\n\t\t\t\t\t// don't lock\n\t\t\t\t\tdelete target.volatiles['uproar'];\n\t\t\t\t}\n\t\t\t\tthis.add('-start', target, 'Uproar', '[upkeep]');\n\t\t\t}",
      "onResidualOrder": 28,
      "onResidualSubOrder": 1,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'Uproar');\n\t\t\t}",
      "onLockMove": "uproar",
      "onAnySetStatus": "function (status, pokemon) {\n\t\t\t\tif (status.id === 'slp') {\n\t\t\t\t\tif (pokemon === this.effectState.target) {\n\t\t\t\t\t\tthis.add('-fail', pokemon, 'slp', '[from] Uproar', '[msg]');\n\t\t\t\t\t}\n\t\t\t\t\telse {\n\t\t\t\t\t\tthis.add('-fail', pokemon, 'slp', '[from] Uproar');\n\t\t\t\t\t}\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "randomNormal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "vacuumwave": {
    "num": 410,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Vacuum Wave",
    "pp": 30,
    "priority": 1,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "vcreate": {
    "num": 557,
    "accuracy": 95,
    "basePower": 180,
    "category": "Physical",
    "name": "V-create",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "self": {
      "boosts": {
        "spe": -1,
        "def": -1,
        "spd": -1
      }
    },
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "zMove": {
      "basePower": 220
    },
    "contestType": "Cool"
  },
  "veeveevolley": {
    "num": 741,
    "accuracy": true,
    "basePower": 0,
    "basePowerCallback": "function (pokemon) {\n\t\t\treturn Math.floor((pokemon.happiness * 10) / 25) || 1;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "LGPE",
    "name": "Veevee Volley",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Cute"
  },
  "venomdrench": {
    "num": 599,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Venom Drench",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "onHit": "function (target, source, move) {\n\t\t\tif (target.status === 'psn' || target.status === 'tox') {\n\t\t\t\treturn !!this.boost({ atk: -1, spa: -1, spe: -1 }, target, source, move);\n\t\t\t}\n\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Poison",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Clever"
  },
  "venoshock": {
    "num": 474,
    "accuracy": 100,
    "basePower": 65,
    "category": "Special",
    "name": "Venoshock",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "onBasePower": "function (basePower, pokemon, target) {\n\t\t\tif (target.status === 'psn' || target.status === 'tox') {\n\t\t\t\treturn this.chainModify(2);\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Poison",
    "contestType": "Beautiful"
  },
  "vinewhip": {
    "num": 22,
    "accuracy": 100,
    "basePower": 45,
    "category": "Physical",
    "name": "Vine Whip",
    "pp": 25,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Cool"
  },
  "visegrip": {
    "num": 11,
    "accuracy": 100,
    "basePower": 55,
    "category": "Physical",
    "name": "Vise Grip",
    "pp": 30,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "vitalthrow": {
    "num": 233,
    "accuracy": true,
    "basePower": 70,
    "category": "Physical",
    "name": "Vital Throw",
    "pp": 10,
    "priority": -1,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Cool"
  },
  "voltswitch": {
    "num": 521,
    "accuracy": 100,
    "basePower": 70,
    "category": "Special",
    "name": "Volt Switch",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "selfSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "volttackle": {
    "num": 344,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Volt Tackle",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      33,
      100
    ],
    "secondary": {
      "chance": 10,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "wakeupslap": {
    "num": 358,
    "accuracy": 100,
    "basePower": 70,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (target.status === 'slp' || target.hasAbility('comatose'))\n\t\t\t\treturn move.basePower * 2;\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Physical",
    "isNonstandard": "Past",
    "name": "Wake-Up Slap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "onHit": "function (target) {\n\t\t\tif (target.status === 'slp')\n\t\t\t\ttarget.cureStatus();\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Fighting",
    "contestType": "Tough"
  },
  "waterfall": {
    "num": 127,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Waterfall",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Water",
    "contestType": "Tough"
  },
  "watergun": {
    "num": 55,
    "accuracy": 100,
    "basePower": 40,
    "category": "Special",
    "name": "Water Gun",
    "pp": 25,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Cute"
  },
  "waterpledge": {
    "num": 518,
    "accuracy": 100,
    "basePower": 80,
    "basePowerCallback": "function (target, source, move) {\n\t\t\tif (['firepledge', 'grasspledge'].includes(move.sourceEffect)) {\n\t\t\t\tthis.add('-combine');\n\t\t\t\treturn 150;\n\t\t\t}\n\t\t\treturn 80;\n\t\t}",
    "category": "Special",
    "name": "Water Pledge",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1,
      "nonsky": 1
    },
    "onPrepareHit": "function (target, source, move) {\n\t\t\tfor (var _i = 0, _a = this.queue; _i < _a.length; _i++) {\n\t\t\t\tvar action = _a[_i];\n\t\t\t\tif (action.choice !== 'move')\n\t\t\t\t\tcontinue;\n\t\t\t\tvar otherMove = action.move;\n\t\t\t\tvar otherMoveUser = action.pokemon;\n\t\t\t\tif (!otherMove || !action.pokemon || !otherMoveUser.isActive ||\n\t\t\t\t\totherMoveUser.fainted || action.maxMove || action.zmove) {\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tif (otherMoveUser.isAlly(source) && ['firepledge', 'grasspledge'].includes(otherMove.id)) {\n\t\t\t\t\tthis.queue.prioritizeAction(action, move);\n\t\t\t\t\tthis.add('-waiting', source, otherMoveUser);\n\t\t\t\t\treturn null;\n\t\t\t\t}\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move) {\n\t\t\tif (move.sourceEffect === 'grasspledge') {\n\t\t\t\tmove.type = 'Grass';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.sideCondition = 'grasspledge';\n\t\t\t}\n\t\t\tif (move.sourceEffect === 'firepledge') {\n\t\t\t\tmove.type = 'Water';\n\t\t\t\tmove.forceSTAB = true;\n\t\t\t\tmove.self = { sideCondition: 'waterpledge' };\n\t\t\t}\n\t\t}",
    "condition": {
      "duration": 4,
      "onSideStart": "function (targetSide) {\n\t\t\t\tthis.add('-sidestart', targetSide, 'Water Pledge');\n\t\t\t}",
      "onSideResidualOrder": 26,
      "onSideResidualSubOrder": 7,
      "onSideEnd": "function (targetSide) {\n\t\t\t\tthis.add('-sideend', targetSide, 'Water Pledge');\n\t\t\t}",
      "onModifyMove": "function (move, pokemon) {\n\t\t\t\tvar _a;\n\t\t\t\tif (move.secondaries && move.id !== 'secretpower') {\n\t\t\t\t\tthis.debug('doubling secondary chance');\n\t\t\t\t\tfor (var _i = 0, _b = move.secondaries; _i < _b.length; _i++) {\n\t\t\t\t\t\tvar secondary = _b[_i];\n\t\t\t\t\t\tif (pokemon.hasAbility('serenegrace') && secondary.volatileStatus === 'flinch')\n\t\t\t\t\t\t\tcontinue;\n\t\t\t\t\t\tif (secondary.chance)\n\t\t\t\t\t\t\tsecondary.chance *= 2;\n\t\t\t\t\t}\n\t\t\t\t\tif ((_a = move.self) === null || _a === void 0 ? void 0 : _a.chance)\n\t\t\t\t\t\tmove.self.chance *= 2;\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "waterpulse": {
    "num": 352,
    "accuracy": 100,
    "basePower": 60,
    "category": "Special",
    "name": "Water Pulse",
    "pp": 20,
    "priority": 0,
    "flags": {
      "protect": 1,
      "pulse": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "confusion"
    },
    "target": "any",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "watershuriken": {
    "num": 594,
    "accuracy": 100,
    "basePower": 15,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\tif (pokemon.species.name === 'Greninja-Ash' && pokemon.hasAbility('battlebond')) {\n\t\t\t\treturn move.basePower + 5;\n\t\t\t}\n\t\t\treturn move.basePower;\n\t\t}",
    "category": "Special",
    "name": "Water Shuriken",
    "pp": 20,
    "priority": 1,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "multihit": [
      2,
      5
    ],
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Cool"
  },
  "watersport": {
    "num": 346,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "isNonstandard": "Past",
    "name": "Water Sport",
    "pp": 15,
    "priority": 0,
    "flags": {
      "nonsky": 1
    },
    "pseudoWeather": "watersport",
    "condition": {
      "duration": 5,
      "onFieldStart": "function (field, source) {\n\t\t\t\tthis.add('-fieldstart', 'move: Water Sport', '[of] ' + source);\n\t\t\t}",
      "onBasePowerPriority": 1,
      "onBasePower": "function (basePower, attacker, defender, move) {\n\t\t\t\tif (move.type === 'Fire') {\n\t\t\t\t\tthis.debug('water sport weaken');\n\t\t\t\t\treturn this.chainModify([1352, 4096]);\n\t\t\t\t}\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 3,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Water Sport');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Water",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "waterspout": {
    "num": 323,
    "accuracy": 100,
    "basePower": 150,
    "basePowerCallback": "function (pokemon, target, move) {\n\t\t\treturn move.basePower * pokemon.hp / pokemon.maxhp;\n\t\t}",
    "category": "Special",
    "name": "Water Spout",
    "pp": 5,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "allAdjacentFoes",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "weatherball": {
    "num": 311,
    "accuracy": 100,
    "basePower": 50,
    "category": "Special",
    "name": "Weather Ball",
    "pp": 10,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "onModifyType": "function (move, pokemon) {\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tmove.type = 'Fire';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\t\tmove.type = 'Water';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'sandstorm':\n\t\t\t\t\tmove.type = 'Rock';\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'hail':\n\t\t\t\t\tmove.type = 'Ice';\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t}",
    "onModifyMove": "function (move, pokemon) {\n\t\t\tswitch (pokemon.effectiveWeather()) {\n\t\t\t\tcase 'sunnyday':\n\t\t\t\tcase 'desolateland':\n\t\t\t\t\tmove.basePower *= 2;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'raindance':\n\t\t\t\tcase 'primordialsea':\n\t\t\t\t\tmove.basePower *= 2;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'sandstorm':\n\t\t\t\t\tmove.basePower *= 2;\n\t\t\t\t\tbreak;\n\t\t\t\tcase 'hail':\n\t\t\t\t\tmove.basePower *= 2;\n\t\t\t\t\tbreak;\n\t\t\t}\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 160
    },
    "maxMove": {
      "basePower": 130
    },
    "contestType": "Beautiful"
  },
  "whirlpool": {
    "num": 250,
    "accuracy": 85,
    "basePower": 35,
    "category": "Special",
    "name": "Whirlpool",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Water",
    "contestType": "Beautiful"
  },
  "whirlwind": {
    "num": 18,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Whirlwind",
    "pp": 20,
    "priority": -6,
    "flags": {
      "reflectable": 1,
      "mirror": 1,
      "authentic": 1,
      "mystery": 1
    },
    "forceSwitch": true,
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "wickedblow": {
    "num": 817,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Wicked Blow",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "punch": 1,
      "mirror": 1
    },
    "willCrit": true,
    "secondary": null,
    "target": "normal",
    "type": "Dark"
  },
  "wideguard": {
    "num": 469,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Wide Guard",
    "pp": 10,
    "priority": 3,
    "flags": {
      "snatch": 1
    },
    "sideCondition": "wideguard",
    "onTry": "function () {\n\t\t\treturn !!this.queue.willAct();\n\t\t}",
    "onHitSide": "function (side, source) {\n\t\t\tsource.addVolatile('stall');\n\t\t}",
    "condition": {
      "duration": 1,
      "onSideStart": "function (target, source) {\n\t\t\t\tthis.add('-singleturn', source, 'Wide Guard');\n\t\t\t}",
      "onTryHitPriority": 4,
      "onTryHit": "function (target, source, move) {\n\t\t\t\t// Wide Guard blocks all spread moves\n\t\t\t\tif ((move === null || move === void 0 ? void 0 : move.target) !== 'allAdjacent' && move.target !== 'allAdjacentFoes') {\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tif (move.isZ || move.isMax) {\n\t\t\t\t\tif (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))\n\t\t\t\t\t\treturn;\n\t\t\t\t\ttarget.getMoveHitData(move).zBrokeProtect = true;\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t\tthis.add('-activate', target, 'move: Wide Guard');\n\t\t\t\tvar lockedmove = source.getVolatile('lockedmove');\n\t\t\t\tif (lockedmove) {\n\t\t\t\t\t// Outrage counter is reset\n\t\t\t\t\tif (source.volatiles['lockedmove'].duration === 2) {\n\t\t\t\t\t\tdelete source.volatiles['lockedmove'];\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\treturn this.NOT_FAIL;\n\t\t\t}"
    },
    "secondary": null,
    "target": "allySide",
    "type": "Rock",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Tough"
  },
  "wildcharge": {
    "num": 528,
    "accuracy": 100,
    "basePower": 90,
    "category": "Physical",
    "name": "Wild Charge",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      1,
      4
    ],
    "secondary": null,
    "target": "normal",
    "type": "Electric",
    "contestType": "Tough"
  },
  "willowisp": {
    "num": 261,
    "accuracy": 85,
    "basePower": 0,
    "category": "Status",
    "name": "Will-O-Wisp",
    "pp": 15,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "status": "brn",
    "secondary": null,
    "target": "normal",
    "type": "Fire",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Beautiful"
  },
  "wingattack": {
    "num": 17,
    "accuracy": 100,
    "basePower": 60,
    "category": "Physical",
    "name": "Wing Attack",
    "pp": 35,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1,
      "distance": 1
    },
    "secondary": null,
    "target": "any",
    "type": "Flying",
    "contestType": "Cool"
  },
  "wish": {
    "num": 273,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Wish",
    "pp": 10,
    "priority": 0,
    "flags": {
      "snatch": 1,
      "heal": 1
    },
    "slotCondition": "Wish",
    "condition": {
      "duration": 2,
      "onStart": "function (pokemon, source) {\n\t\t\t\tthis.effectState.hp = source.maxhp / 2;\n\t\t\t}",
      "onResidualOrder": 4,
      "onEnd": "function (target) {\n\t\t\t\tif (target && !target.fainted) {\n\t\t\t\t\tvar damage = this.heal(this.effectState.hp, target, target);\n\t\t\t\t\tif (damage) {\n\t\t\t\t\t\tthis.add('-heal', target, target.getHealth, '[from] move: Wish', '[wisher] ' + this.effectState.source.name);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Cute"
  },
  "withdraw": {
    "num": 110,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Withdraw",
    "pp": 40,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "def": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Water",
    "zMove": {
      "boost": {
        "def": 1
      }
    },
    "contestType": "Cute"
  },
  "wonderroom": {
    "num": 472,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Wonder Room",
    "pp": 10,
    "priority": 0,
    "flags": {
      "mirror": 1
    },
    "pseudoWeather": "wonderroom",
    "condition": {
      "duration": 5,
      "durationCallback": "function (source, effect) {\n\t\t\t\tif (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {\n\t\t\t\t\tthis.add('-activate', source, 'ability: Persistent', effect);\n\t\t\t\t\treturn 7;\n\t\t\t\t}\n\t\t\t\treturn 5;\n\t\t\t}",
      "onFieldStart": "function (field, source) {\n\t\t\t\tthis.add('-fieldstart', 'move: Wonder Room', '[of] ' + source);\n\t\t\t}",
      "onFieldRestart": "function (target, source) {\n\t\t\t\tthis.field.removePseudoWeather('wonderroom');\n\t\t\t}",
      "onFieldResidualOrder": 27,
      "onFieldResidualSubOrder": 5,
      "onFieldEnd": "function () {\n\t\t\t\tthis.add('-fieldend', 'move: Wonder Room');\n\t\t\t}"
    },
    "secondary": null,
    "target": "all",
    "type": "Psychic",
    "zMove": {
      "boost": {
        "spd": 1
      }
    },
    "contestType": "Clever"
  },
  "woodhammer": {
    "num": 452,
    "accuracy": 100,
    "basePower": 120,
    "category": "Physical",
    "name": "Wood Hammer",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "recoil": [
      33,
      100
    ],
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "contestType": "Tough"
  },
  "workup": {
    "num": 526,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Work Up",
    "pp": 30,
    "priority": 0,
    "flags": {
      "snatch": 1
    },
    "boosts": {
      "atk": 1,
      "spa": 1
    },
    "secondary": null,
    "target": "self",
    "type": "Normal",
    "zMove": {
      "boost": {
        "atk": 1
      }
    },
    "contestType": "Tough"
  },
  "worryseed": {
    "num": 388,
    "accuracy": 100,
    "basePower": 0,
    "category": "Status",
    "name": "Worry Seed",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1,
      "mystery": 1
    },
    "onTryImmunity": "function (target) {\n\t\t\t// Truant and Insomnia have special treatment; they fail before\n\t\t\t// checking accuracy and will double Stomping Tantrum's BP\n\t\t\tif (target.ability === 'truant' || target.ability === 'insomnia') {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onTryHit": "function (target) {\n\t\t\tif (target.getAbility().isPermanent) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "onHit": "function (pokemon) {\n\t\t\tvar oldAbility = pokemon.setAbility('insomnia');\n\t\t\tif (oldAbility) {\n\t\t\t\tthis.add('-ability', pokemon, 'Insomnia', '[from] move: Worry Seed');\n\t\t\t\tif (pokemon.status === 'slp') {\n\t\t\t\t\tpokemon.cureStatus();\n\t\t\t\t}\n\t\t\t\treturn;\n\t\t\t}\n\t\t\treturn false;\n\t\t}",
    "secondary": null,
    "target": "normal",
    "type": "Grass",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Clever"
  },
  "wrap": {
    "num": 35,
    "accuracy": 90,
    "basePower": 15,
    "category": "Physical",
    "name": "Wrap",
    "pp": 20,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "volatileStatus": "partiallytrapped",
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "contestType": "Tough"
  },
  "wringout": {
    "num": 378,
    "accuracy": 100,
    "basePower": 0,
    "basePowerCallback": "function (pokemon, target) {\n\t\t\treturn Math.floor(Math.floor((120 * (100 * Math.floor(target.hp * 4096 / target.maxhp)) + 2048 - 1) / 4096) / 100) || 1;\n\t\t}",
    "category": "Special",
    "isNonstandard": "Past",
    "name": "Wring Out",
    "pp": 5,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "basePower": 190
    },
    "maxMove": {
      "basePower": 140
    },
    "contestType": "Tough"
  },
  "xscissor": {
    "num": 404,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "X-Scissor",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": null,
    "target": "normal",
    "type": "Bug",
    "contestType": "Cool"
  },
  "yawn": {
    "num": 281,
    "accuracy": true,
    "basePower": 0,
    "category": "Status",
    "name": "Yawn",
    "pp": 10,
    "priority": 0,
    "flags": {
      "protect": 1,
      "reflectable": 1,
      "mirror": 1
    },
    "volatileStatus": "yawn",
    "onTryHit": "function (target) {\n\t\t\tif (target.status || !target.runStatusImmunity('slp')) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}",
    "condition": {
      "noCopy": true,
      "duration": 2,
      "onStart": "function (target, source) {\n\t\t\t\tthis.add('-start', target, 'move: Yawn', '[of] ' + source);\n\t\t\t}",
      "onResidualOrder": 23,
      "onEnd": "function (target) {\n\t\t\t\tthis.add('-end', target, 'move: Yawn', '[silent]');\n\t\t\t\ttarget.trySetStatus('slp', this.effectState.source);\n\t\t\t}"
    },
    "secondary": null,
    "target": "normal",
    "type": "Normal",
    "zMove": {
      "boost": {
        "spe": 1
      }
    },
    "contestType": "Cute"
  },
  "zapcannon": {
    "num": 192,
    "accuracy": 50,
    "basePower": 120,
    "category": "Special",
    "name": "Zap Cannon",
    "pp": 5,
    "priority": 0,
    "flags": {
      "bullet": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 100,
      "status": "par"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "zenheadbutt": {
    "num": 428,
    "accuracy": 90,
    "basePower": 80,
    "category": "Physical",
    "name": "Zen Headbutt",
    "pp": 15,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 20,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Psychic",
    "contestType": "Clever"
  },
  "zingzap": {
    "num": 716,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "name": "Zing Zap",
    "pp": 10,
    "priority": 0,
    "flags": {
      "contact": 1,
      "protect": 1,
      "mirror": 1
    },
    "secondary": {
      "chance": 30,
      "volatileStatus": "flinch"
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  },
  "zippyzap": {
    "num": 729,
    "accuracy": 100,
    "basePower": 80,
    "category": "Physical",
    "isNonstandard": "LGPE",
    "name": "Zippy Zap",
    "pp": 10,
    "priority": 2,
    "flags": {
      "contact": 1,
      "protect": 1
    },
    "secondary": {
      "chance": 100,
      "self": {
        "boosts": {
          "evasion": 1
        }
      }
    },
    "target": "normal",
    "type": "Electric",
    "contestType": "Cool"
  }
}