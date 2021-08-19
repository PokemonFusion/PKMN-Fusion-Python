BattleMovedex = {'10000000voltthunderbolt': {'accuracy': True,
                             'basePower': 195,
                             'category': 'Special',
                             'contestType': 'Cool',
                             'critRatio': 3,
                             'flags': {},
                             'isNonstandard': 'Past',
                             'isZ': 'pikashuniumz',
                             'name': '10,000,000 Volt Thunderbolt',
                             'num': 719,
                             'pp': 1,
                             'priority': 0,
                             'secondary': None,
                             'target': 'normal',
                             'type': 'Electric'},
 'absorb': {'accuracy': 100,
            'basePower': 20,
            'category': 'Special',
            'contestType': 'Clever',
            'drain': [1, 2],
            'flags': {'heal': 1, 'mirror': 1, 'protect': 1},
            'name': 'Absorb',
            'num': 71,
            'pp': 25,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Grass'},
 'accelerock': {'accuracy': 100,
                'basePower': 40,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Accelerock',
                'num': 709,
                'pp': 20,
                'priority': 1,
                'secondary': None,
                'target': 'normal',
                'type': 'Rock'},
 'acid': {'accuracy': 100,
          'basePower': 40,
          'category': 'Special',
          'contestType': 'Clever',
          'flags': {'mirror': 1, 'protect': 1},
          'name': 'Acid',
          'num': 51,
          'pp': 30,
          'priority': 0,
          'secondary': {'boosts': {'spd': -1}, 'chance': 10},
          'target': 'allAdjacentFoes',
          'type': 'Poison'},
 'acidarmor': {'accuracy': True,
               'basePower': 0,
               'boosts': {'def': 2},
               'category': 'Status',
               'contestType': 'Tough',
               'flags': {'snatch': 1},
               'name': 'Acid Armor',
               'num': 151,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Poison',
               'zMove': {'effect': 'clearnegativeboost'}},
 'aciddownpour': {'accuracy': True,
                  'basePower': 1,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isNonstandard': 'Past',
                  'isZ': 'poisoniumz',
                  'name': 'Acid Downpour',
                  'num': 628,
                  'pp': 1,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Poison'},
 'acidspray': {'accuracy': 100,
               'basePower': 40,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
               'name': 'Acid Spray',
               'num': 491,
               'pp': 20,
               'priority': 0,
               'secondary': {'boosts': {'spd': -2}, 'chance': 100},
               'target': 'normal',
               'type': 'Poison'},
 'acrobatics': {'accuracy': 100,
                'basePower': 55,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     '\t\t\tif (!pokemon.item) {\n'
                                     '\t\t\t\tthis.debug("Power doubled for no '
                                     'item");\n'
                                     '\t\t\t\treturn move.basePower * 2;\n'
                                     '\t\t\t}\n'
                                     '\t\t\treturn move.basePower;\n'
                                     '\t\t}',
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1,
                          'distance': 1,
                          'mirror': 1,
                          'protect': 1},
                'name': 'Acrobatics',
                'num': 512,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'any',
                'type': 'Flying'},
 'acupressure': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Tough',
                 'flags': {},
                 'name': 'Acupressure',
                 'num': 367,
                 'onHit': 'function (target) {\n'
                          '\t\t\tvar stats = [];\n'
                          '\t\t\tvar stat;\n'
                          '\t\t\tfor (stat in target.boosts) {\n'
                          '\t\t\t\tif (target.boosts[stat] < 6) {\n'
                          '\t\t\t\t\tstats.push(stat);\n'
                          '\t\t\t\t}\n'
                          '\t\t\t}\n'
                          '\t\t\tif (stats.length) {\n'
                          '\t\t\t\tvar randomStat = this.sample(stats);\n'
                          '\t\t\t\tvar boost = {};\n'
                          '\t\t\t\tboost[randomStat] = 2;\n'
                          '\t\t\t\tthis.boost(boost);\n'
                          '\t\t\t}\n'
                          '\t\t\telse {\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 30,
                 'priority': 0,
                 'secondary': None,
                 'target': 'adjacentAllyOrSelf',
                 'type': 'Normal',
                 'zMove': {'effect': 'crit2'}},
 'aerialace': {'accuracy': True,
               'basePower': 60,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1,
                         'distance': 1,
                         'mirror': 1,
                         'protect': 1},
               'name': 'Aerial Ace',
               'num': 332,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'any',
               'type': 'Flying'},
 'aeroblast': {'accuracy': 95,
               'basePower': 100,
               'category': 'Special',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'distance': 1, 'mirror': 1, 'protect': 1},
               'name': 'Aeroblast',
               'num': 177,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'any',
               'type': 'Flying'},
 'afteryou': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'authentic': 1, 'mystery': 1},
              'name': 'After You',
              'num': 495,
              'onHit': 'function (target) {\n'
                       '\t\t\tif (target.side.active.length < 2)\n'
                       '\t\t\t\treturn false; // fails in singles\n'
                       '\t\t\tvar action = this.queue.willMove(target);\n'
                       '\t\t\tif (action) {\n'
                       '\t\t\t\tthis.queue.prioritizeAction(action);\n'
                       "\t\t\t\tthis.add('-activate', target, 'move: After "
                       "You');\n"
                       '\t\t\t}\n'
                       '\t\t\telse {\n'
                       '\t\t\t\treturn false;\n'
                       '\t\t\t}\n'
                       '\t\t}',
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'boost': {'spe': 1}}},
 'agility': {'accuracy': True,
             'basePower': 0,
             'boosts': {'spe': 2},
             'category': 'Status',
             'contestType': 'Cool',
             'flags': {'snatch': 1},
             'name': 'Agility',
             'num': 97,
             'pp': 30,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Psychic',
             'zMove': {'effect': 'clearnegativeboost'}},
 'aircutter': {'accuracy': 95,
               'basePower': 60,
               'category': 'Special',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Air Cutter',
               'num': 314,
               'pp': 25,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Flying'},
 'airslash': {'accuracy': 95,
              'basePower': 75,
              'category': 'Special',
              'contestType': 'Cool',
              'flags': {'distance': 1, 'mirror': 1, 'protect': 1},
              'name': 'Air Slash',
              'num': 403,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
              'target': 'any',
              'type': 'Flying'},
 'alloutpummeling': {'accuracy': True,
                     'basePower': 1,
                     'category': 'Physical',
                     'contestType': 'Cool',
                     'flags': {},
                     'isNonstandard': 'Past',
                     'isZ': 'fightiniumz',
                     'name': 'All-Out Pummeling',
                     'num': 624,
                     'pp': 1,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Fighting'},
 'allyswitch': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {},
                'name': 'Ally Switch',
                'num': 502,
                'onHit': 'function (pokemon) {\n'
                         '\t\t\tvar newPosition = (pokemon.position === 0 ? '
                         'pokemon.side.active.length - 1 : 0);\n'
                         '\t\t\tif (!pokemon.side.active[newPosition])\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\tif (pokemon.side.active[newPosition].fainted)\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\tthis.swapPosition(pokemon, newPosition, '
                         "'[from] move: Ally Switch');\n"
                         '\t\t}',
                'onTryHit': 'function (source) {\n'
                            '\t\t\tif (source.side.active.length === 1)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\tif (source.side.active.length === 3 && '
                            'source.position === 1)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 15,
                'priority': 2,
                'secondary': None,
                'target': 'self',
                'type': 'Psychic',
                'zMove': {'boost': {'spe': 2}}},
 'amnesia': {'accuracy': True,
             'basePower': 0,
             'boosts': {'spd': 2},
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {'snatch': 1},
             'name': 'Amnesia',
             'num': 133,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Psychic',
             'zMove': {'effect': 'clearnegativeboost'}},
 'anchorshot': {'accuracy': 100,
                'basePower': 80,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Anchor Shot',
                'num': 677,
                'pp': 20,
                'priority': 0,
                'secondary': {'chance': 100,
                              'onHit': 'function (target, source, move) {\n'
                                       '\t\t\t\tif (source.isActive)\n'
                                       '\t\t\t\t\t'
                                       "target.addVolatile('trapped', source, "
                                       "move, 'trapper');\n"
                                       '\t\t\t}'},
                'target': 'normal',
                'type': 'Steel'},
 'ancientpower': {'accuracy': 100,
                  'basePower': 60,
                  'category': 'Special',
                  'contestType': 'Tough',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Ancient Power',
                  'num': 246,
                  'pp': 5,
                  'priority': 0,
                  'secondary': {'chance': 10,
                                'self': {'boosts': {'atk': 1,
                                                    'def': 1,
                                                    'spa': 1,
                                                    'spd': 1,
                                                    'spe': 1}}},
                  'target': 'normal',
                  'type': 'Rock'},
 'appleacid': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Apple Acid',
               'num': 787,
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'spd': -1}, 'chance': 100},
               'target': 'normal',
               'type': 'Grass'},
 'aquajet': {'accuracy': 100,
             'basePower': 40,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Aqua Jet',
             'num': 453,
             'pp': 20,
             'priority': 1,
             'secondary': None,
             'target': 'normal',
             'type': 'Water'},
 'aquaring': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'onResidual': 'function (pokemon) {\n'
                                          '\t\t\t\tthis.heal(pokemon.baseMaxhp '
                                          '/ 16);\n'
                                          '\t\t\t}',
                            'onResidualOrder': 6,
                            'onStart': 'function (pokemon) {\n'
                                       "\t\t\t\tthis.add('-start', pokemon, "
                                       "'Aqua Ring');\n"
                                       '\t\t\t}'},
              'contestType': 'Beautiful',
              'flags': {'snatch': 1},
              'name': 'Aqua Ring',
              'num': 392,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Water',
              'volatileStatus': 'aquaring',
              'zMove': {'boost': {'def': 1}}},
 'aquatail': {'accuracy': 90,
              'basePower': 90,
              'category': 'Physical',
              'contestType': 'Beautiful',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Aqua Tail',
              'num': 401,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Water'},
 'armthrust': {'accuracy': 100,
               'basePower': 15,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'multihit': [2, 5],
               'name': 'Arm Thrust',
               'num': 292,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fighting'},
 'aromatherapy': {'accuracy': True,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'distance': 1, 'snatch': 1},
                  'name': 'Aromatherapy',
                  'num': 312,
                  'onHit': 'function (pokemon, source, move) {\n'
                           "\t\t\tthis.add('-activate', source, 'move: "
                           "Aromatherapy');\n"
                           '\t\t\tvar success = false;\n'
                           '\t\t\tfor (var _i = 0, _a = pokemon.side.pokemon; '
                           '_i < _a.length; _i++) {\n'
                           '\t\t\t\tvar ally = _a[_i];\n'
                           '\t\t\t\tif (ally !== source && '
                           "((ally.hasAbility('sapsipper')) ||\n"
                           "\t\t\t\t\t(ally.volatiles['substitute'] && "
                           '!move.infiltrates))) {\n'
                           '\t\t\t\t\tcontinue;\n'
                           '\t\t\t\t}\n'
                           '\t\t\t\tif (ally.cureStatus())\n'
                           '\t\t\t\t\tsuccess = true;\n'
                           '\t\t\t}\n'
                           '\t\t\treturn success;\n'
                           '\t\t}',
                  'pp': 5,
                  'priority': 0,
                  'target': 'allyTeam',
                  'type': 'Grass',
                  'zMove': {'effect': 'heal'}},
 'aromaticmist': {'accuracy': True,
                  'basePower': 0,
                  'boosts': {'spd': 1},
                  'category': 'Status',
                  'contestType': 'Beautiful',
                  'flags': {'authentic': 1},
                  'name': 'Aromatic Mist',
                  'num': 597,
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'adjacentAlly',
                  'type': 'Fairy',
                  'zMove': {'boost': {'spd': 2}}},
 'assist': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Cute',
            'flags': {},
            'isNonstandard': 'Past',
            'name': 'Assist',
            'num': 274,
            'onHit': 'function (target) {\n'
                     '\t\t\tvar noAssist = [\n'
                     "\t\t\t\t'assist', 'banefulbunker', 'beakblast', 'belch', "
                     "'bestow', 'bounce', 'celebrate', 'chatter', "
                     "'circlethrow', 'copycat', 'counter', 'covet', "
                     "'destinybond', 'detect', 'dig', 'dive', 'dragontail', "
                     "'endure', 'feint', 'fly', 'focuspunch', 'followme', "
                     "'helpinghand', 'holdhands', 'kingsshield', 'matblock', "
                     "'mefirst', 'metronome', 'mimic', 'mirrorcoat', "
                     "'mirrormove', 'naturepower', 'phantomforce', 'protect', "
                     "'ragepowder', 'roar', 'shadowforce', 'shelltrap', "
                     "'sketch', 'skydrop', 'sleeptalk', 'snatch', "
                     "'spikyshield', 'spotlight', 'struggle', 'switcheroo', "
                     "'thief', 'transform', 'trick', 'whirlwind',\n"
                     '\t\t\t];\n'
                     '\t\t\tvar moves = [];\n'
                     '\t\t\tfor (var _i = 0, _a = target.side.pokemon; _i < '
                     '_a.length; _i++) {\n'
                     '\t\t\t\tvar pokemon = _a[_i];\n'
                     '\t\t\t\tif (pokemon === target)\n'
                     '\t\t\t\t\tcontinue;\n'
                     '\t\t\t\tfor (var _b = 0, _c = pokemon.moveSlots; _b < '
                     '_c.length; _b++) {\n'
                     '\t\t\t\t\tvar moveSlot = _c[_b];\n'
                     '\t\t\t\t\tvar moveid = moveSlot.id;\n'
                     '\t\t\t\t\tif (noAssist.includes(moveid))\n'
                     '\t\t\t\t\t\tcontinue;\n'
                     '\t\t\t\t\tvar move = this.dex.moves.get(moveid);\n'
                     '\t\t\t\t\tif (move.isZ || move.isMax) {\n'
                     '\t\t\t\t\t\tcontinue;\n'
                     '\t\t\t\t\t}\n'
                     '\t\t\t\t\tmoves.push(moveid);\n'
                     '\t\t\t\t}\n'
                     '\t\t\t}\n'
                     "\t\t\tvar randomMove = '';\n"
                     '\t\t\tif (moves.length)\n'
                     '\t\t\t\trandomMove = this.sample(moves);\n'
                     '\t\t\tif (!randomMove) {\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\t}\n'
                     '\t\t\tthis.actions.useMove(randomMove, target);\n'
                     '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Normal'},
 'assurance': {'accuracy': 100,
               'basePower': 60,
               'basePowerCallback': 'function (pokemon, target, move) {\n'
                                    '\t\t\tif (target.hurtThisTurn) {\n'
                                    "\t\t\t\tthis.debug('Boosted for being "
                                    "damaged this turn');\n"
                                    '\t\t\t\treturn move.basePower * 2;\n'
                                    '\t\t\t}\n'
                                    '\t\t\treturn move.basePower;\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Clever',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Assurance',
               'num': 372,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Dark'},
 'astonish': {'accuracy': 100,
              'basePower': 30,
              'category': 'Physical',
              'contestType': 'Cute',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Astonish',
              'num': 310,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
              'target': 'normal',
              'type': 'Ghost'},
 'astralbarrage': {'accuracy': 100,
                   'basePower': 120,
                   'category': 'Special',
                   'flags': {'mirror': 1, 'protect': 1},
                   'name': 'Astral Barrage',
                   'num': 825,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'target': 'allAdjacentFoes',
                   'type': 'Ghost'},
 'attackorder': {'accuracy': 100,
                 'basePower': 90,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'critRatio': 2,
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Attack Order',
                 'num': 454,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Bug'},
 'attract': {'accuracy': 100,
             'basePower': 0,
             'category': 'Status',
             'condition': {'noCopy': True,
                           'onBeforeMove': 'function (pokemon, target, move) '
                                           '{\n'
                                           "\t\t\t\tthis.add('-activate', "
                                           "pokemon, 'move: Attract', '[of] ' "
                                           '+ this.effectState.source);\n'
                                           '\t\t\t\tif (this.randomChance(1, '
                                           '2)) {\n'
                                           "\t\t\t\t\tthis.add('cant', "
                                           "pokemon, 'Attract');\n"
                                           '\t\t\t\t\treturn false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                           'onBeforeMovePriority': 2,
                           'onEnd': 'function (pokemon) {\n'
                                    "\t\t\t\tthis.add('-end', pokemon, "
                                    "'Attract', '[silent]');\n"
                                    '\t\t\t}',
                           'onStart': 'function (pokemon, source, effect) {\n'
                                      "\t\t\t\tif (!(pokemon.gender === 'M' && "
                                      "source.gender === 'F') && "
                                      "!(pokemon.gender === 'F' && "
                                      "source.gender === 'M')) {\n"
                                      "\t\t\t\t\tthis.debug('incompatible "
                                      "gender');\n"
                                      '\t\t\t\t\treturn false;\n'
                                      '\t\t\t\t}\n'
                                      "\t\t\t\tif (!this.runEvent('Attract', "
                                      'pokemon, source)) {\n'
                                      "\t\t\t\t\tthis.debug('Attract event "
                                      "failed');\n"
                                      '\t\t\t\t\treturn false;\n'
                                      '\t\t\t\t}\n'
                                      "\t\t\t\tif (effect.id === 'cutecharm') "
                                      '{\n'
                                      "\t\t\t\t\tthis.add('-start', pokemon, "
                                      "'Attract', '[from] ability: Cute "
                                      "Charm', '[of] ' + source);\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t\telse if (effect.id === '
                                      "'destinyknot') {\n"
                                      "\t\t\t\t\tthis.add('-start', pokemon, "
                                      "'Attract', '[from] item: Destiny Knot', "
                                      "'[of] ' + source);\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t\telse {\n'
                                      "\t\t\t\t\tthis.add('-start', pokemon, "
                                      "'Attract');\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                           'onUpdate': 'function (pokemon) {\n'
                                       '\t\t\t\tif (this.effectState.source && '
                                       '!this.effectState.source.isActive && '
                                       "pokemon.volatiles['attract']) {\n"
                                       "\t\t\t\t\tthis.debug('Removing Attract "
                                       "volatile on ' + pokemon);\n"
                                       '\t\t\t\t\t'
                                       "pokemon.removeVolatile('attract');\n"
                                       '\t\t\t\t}\n'
                                       '\t\t\t}'},
             'contestType': 'Cute',
             'flags': {'authentic': 1,
                       'mirror': 1,
                       'protect': 1,
                       'reflectable': 1},
             'name': 'Attract',
             'num': 213,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'volatileStatus': 'attract',
             'zMove': {'effect': 'clearnegativeboost'}},
 'aurasphere': {'accuracy': True,
                'basePower': 80,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'bullet': 1,
                          'distance': 1,
                          'mirror': 1,
                          'protect': 1,
                          'pulse': 1},
                'name': 'Aura Sphere',
                'num': 396,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'any',
                'type': 'Fighting'},
 'aurawheel': {'accuracy': 100,
               'basePower': 110,
               'category': 'Physical',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Aura Wheel',
               'num': 783,
               'onModifyType': 'function (move, pokemon) {\n'
                               '\t\t\tif (pokemon.species.name === '
                               "'Morpeko-Hangry') {\n"
                               "\t\t\t\tmove.type = 'Dark';\n"
                               '\t\t\t}\n'
                               '\t\t\telse {\n'
                               "\t\t\t\tmove.type = 'Electric';\n"
                               '\t\t\t}\n'
                               '\t\t}',
               'onTry': 'function (source) {\n'
                        "\t\t\tif (source.species.baseSpecies === 'Morpeko') "
                        '{\n'
                        '\t\t\t\treturn;\n'
                        '\t\t\t}\n'
                        "\t\t\tthis.attrLastMove('[still]');\n"
                        "\t\t\tthis.add('-fail', source, 'move: Aura Wheel');\n"
                        '\t\t\tthis.hint("Only a Pokemon whose form is Morpeko '
                        'or Morpeko-Hangry can use this move.");\n'
                        '\t\t\treturn null;\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 100, 'self': {'boosts': {'spe': 1}}},
               'target': 'normal',
               'type': 'Electric'},
 'aurorabeam': {'accuracy': 100,
                'basePower': 65,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Aurora Beam',
                'num': 62,
                'pp': 20,
                'priority': 0,
                'secondary': {'boosts': {'atk': -1}, 'chance': 10},
                'target': 'normal',
                'type': 'Ice'},
 'auroraveil': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 5,
                              'durationCallback': 'function (target, source, '
                                                  'effect) {\n'
                                                  '\t\t\t\tif (source === null '
                                                  '|| source === void 0 ? void '
                                                  '0 : '
                                                  "source.hasItem('lightclay')) "
                                                  '{\n'
                                                  '\t\t\t\t\treturn 8;\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t\treturn 5;\n'
                                                  '\t\t\t}',
                              'onAnyModifyDamage': 'function (damage, source, '
                                                   'target, move) {\n'
                                                   '\t\t\t\tif (target !== '
                                                   'source && '
                                                   'this.effectState.target.hasAlly(target)) '
                                                   '{\n'
                                                   '\t\t\t\t\tif '
                                                   "((target.side.getSideCondition('reflect') "
                                                   '&& this.getCategory(move) '
                                                   "=== 'Physical') ||\n"
                                                   '\t\t\t\t\t\t'
                                                   "(target.side.getSideCondition('lightscreen') "
                                                   '&& this.getCategory(move) '
                                                   "=== 'Special')) {\n"
                                                   '\t\t\t\t\t\treturn;\n'
                                                   '\t\t\t\t\t}\n'
                                                   '\t\t\t\t\tif '
                                                   '(!target.getMoveHitData(move).crit '
                                                   '&& !move.infiltrates) {\n'
                                                   '\t\t\t\t\t\t'
                                                   "this.debug('Aurora Veil "
                                                   "weaken');\n"
                                                   '\t\t\t\t\t\tif '
                                                   '(this.activePerHalf > 1)\n'
                                                   '\t\t\t\t\t\t\treturn '
                                                   'this.chainModify([2732, '
                                                   '4096]);\n'
                                                   '\t\t\t\t\t\treturn '
                                                   'this.chainModify(0.5);\n'
                                                   '\t\t\t\t\t}\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t}',
                              'onSideEnd': 'function (side) {\n'
                                           "\t\t\t\tthis.add('-sideend', side, "
                                           "'move: Aurora Veil');\n"
                                           '\t\t\t}',
                              'onSideResidualOrder': 26,
                              'onSideResidualSubOrder': 10,
                              'onSideStart': 'function (side) {\n'
                                             "\t\t\t\tthis.add('-sidestart', "
                                             "side, 'move: Aurora Veil');\n"
                                             '\t\t\t}'},
                'contestType': 'Beautiful',
                'flags': {'snatch': 1},
                'name': 'Aurora Veil',
                'num': 694,
                'onTry': 'function () {\n'
                         "\t\t\treturn this.field.isWeather('hail');\n"
                         '\t\t}',
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'sideCondition': 'auroraveil',
                'target': 'allySide',
                'type': 'Ice',
                'zMove': {'boost': {'spe': 1}}},
 'autotomize': {'accuracy': True,
                'basePower': 0,
                'boosts': {'spe': 2},
                'category': 'Status',
                'contestType': 'Beautiful',
                'flags': {'snatch': 1},
                'name': 'Autotomize',
                'num': 475,
                'onHit': 'function (pokemon) {\n'
                         '\t\t\tif (pokemon.weighthg > 1) {\n'
                         '\t\t\t\tpokemon.weighthg = Math.max(1, '
                         'pokemon.weighthg - 1000);\n'
                         "\t\t\t\tthis.add('-start', pokemon, 'Autotomize');\n"
                         '\t\t\t}\n'
                         '\t\t}',
                'onTryHit': 'function (pokemon) {\n'
                            '\t\t\tvar hasContrary = '
                            "pokemon.hasAbility('contrary');\n"
                            '\t\t\tif ((!hasContrary && pokemon.boosts.spe === '
                            '6) || (hasContrary && pokemon.boosts.spe === -6)) '
                            '{\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Steel',
                'zMove': {'effect': 'clearnegativeboost'}},
 'avalanche': {'accuracy': 100,
               'basePower': 60,
               'basePowerCallback': 'function (pokemon, target, move) {\n'
                                    '\t\t\tvar damagedByTarget = '
                                    'pokemon.attackedBy.some(function (p) { '
                                    'return p.source === target && p.damage > '
                                    '0 && p.thisTurn; });\n'
                                    '\t\t\tif (damagedByTarget) {\n'
                                    "\t\t\t\tthis.debug('Boosted for getting "
                                    "hit by ' + target);\n"
                                    '\t\t\t\treturn move.basePower * 2;\n'
                                    '\t\t\t}\n'
                                    '\t\t\treturn move.basePower;\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Beautiful',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Avalanche',
               'num': 419,
               'pp': 10,
               'priority': -4,
               'secondary': None,
               'target': 'normal',
               'type': 'Ice'},
 'babydolleyes': {'accuracy': 100,
                  'basePower': 0,
                  'boosts': {'atk': -1},
                  'category': 'Status',
                  'contestType': 'Cute',
                  'flags': {'mirror': 1,
                            'mystery': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': 'Baby-Doll Eyes',
                  'num': 608,
                  'pp': 30,
                  'priority': 1,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Fairy',
                  'zMove': {'boost': {'def': 1}}},
 'baddybad': {'accuracy': 95,
              'basePower': 80,
              'category': 'Special',
              'contestType': 'Clever',
              'flags': {'protect': 1},
              'isNonstandard': 'LGPE',
              'name': 'Baddy Bad',
              'num': 737,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'self': {'sideCondition': 'reflect'},
              'target': 'normal',
              'type': 'Dark'},
 'banefulbunker': {'accuracy': True,
                   'basePower': 0,
                   'category': 'Status',
                   'condition': {'duration': 1,
                                 'onHit': 'function (target, source, move) {\n'
                                          '\t\t\t\tif (move.isZOrMaxPowered && '
                                          'this.checkMoveMakesContact(move, '
                                          'source, target)) {\n'
                                          '\t\t\t\t\t'
                                          "source.trySetStatus('psn', "
                                          'target);\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t}',
                                 'onStart': 'function (target) {\n'
                                            "\t\t\t\tthis.add('-singleturn', "
                                            "target, 'move: Protect');\n"
                                            '\t\t\t}',
                                 'onTryHit': 'function (target, source, move) '
                                             '{\n'
                                             '\t\t\t\tif '
                                             "(!move.flags['protect']) {\n"
                                             "\t\t\t\t\tif (['gmaxoneblow', "
                                             "'gmaxrapidflow'].includes(move.id))\n"
                                             '\t\t\t\t\t\treturn;\n'
                                             '\t\t\t\t\tif (move.isZ || '
                                             'move.isMax)\n'
                                             '\t\t\t\t\t\t'
                                             'target.getMoveHitData(move).zBrokeProtect '
                                             '= true;\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\tif (move.smartTarget) {\n'
                                             '\t\t\t\t\tmove.smartTarget = '
                                             'false;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\telse {\n'
                                             "\t\t\t\t\tthis.add('-activate', "
                                             "target, 'move: Protect');\n"
                                             '\t\t\t\t}\n'
                                             '\t\t\t\tvar lockedmove = '
                                             "source.getVolatile('lockedmove');\n"
                                             '\t\t\t\tif (lockedmove) {\n'
                                             '\t\t\t\t\t// Outrage counter is '
                                             'reset\n'
                                             '\t\t\t\t\tif '
                                             "(source.volatiles['lockedmove'].duration "
                                             '=== 2) {\n'
                                             '\t\t\t\t\t\tdelete '
                                             "source.volatiles['lockedmove'];\n"
                                             '\t\t\t\t\t}\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\tif '
                                             '(this.checkMoveMakesContact(move, '
                                             'source, target)) {\n'
                                             '\t\t\t\t\t'
                                             "source.trySetStatus('psn', "
                                             'target);\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\treturn this.NOT_FAIL;\n'
                                             '\t\t\t}',
                                 'onTryHitPriority': 3},
                   'contestType': 'Tough',
                   'flags': {},
                   'name': 'Baneful Bunker',
                   'num': 661,
                   'onHit': 'function (pokemon) {\n'
                            "\t\t\tpokemon.addVolatile('stall');\n"
                            '\t\t}',
                   'onPrepareHit': 'function (pokemon) {\n'
                                   '\t\t\treturn !!this.queue.willAct() && '
                                   "this.runEvent('StallMove', pokemon);\n"
                                   '\t\t}',
                   'pp': 10,
                   'priority': 4,
                   'secondary': None,
                   'stallingMove': True,
                   'target': 'self',
                   'type': 'Poison',
                   'volatileStatus': 'banefulbunker',
                   'zMove': {'boost': {'def': 1}}},
 'barrage': {'accuracy': 85,
             'basePower': 15,
             'category': 'Physical',
             'contestType': 'Cute',
             'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'multihit': [2, 5],
             'name': 'Barrage',
             'num': 140,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal'},
 'barrier': {'accuracy': True,
             'basePower': 0,
             'boosts': {'def': 2},
             'category': 'Status',
             'contestType': 'Cool',
             'flags': {'snatch': 1},
             'isNonstandard': 'Past',
             'name': 'Barrier',
             'num': 112,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Psychic',
             'zMove': {'effect': 'clearnegativeboost'}},
 'batonpass': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {},
               'name': 'Baton Pass',
               'num': 226,
               'pp': 40,
               'priority': 0,
               'secondary': None,
               'self': {'onHit': 'function (source) {\n'
                                 '\t\t\t\tsource.skipBeforeSwitchOutEventFlag '
                                 '= true;\n'
                                 '\t\t\t}'},
               'selfSwitch': 'copyvolatile',
               'target': 'self',
               'type': 'Normal',
               'zMove': {'effect': 'clearnegativeboost'}},
 'beakblast': {'accuracy': 100,
               'basePower': 100,
               'beforeTurnCallback': 'function (pokemon) {\n'
                                     "\t\t\tpokemon.addVolatile('beakblast');\n"
                                     '\t\t}',
               'category': 'Physical',
               'condition': {'duration': 1,
                             'onHit': 'function (target, source, move) {\n'
                                      '\t\t\t\tif '
                                      '(this.checkMoveMakesContact(move, '
                                      'source, target)) {\n'
                                      "\t\t\t\t\tsource.trySetStatus('brn', "
                                      'target);\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                             'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-singleturn', "
                                        "pokemon, 'move: Beak Blast');\n"
                                        '\t\t\t}'},
               'contestType': 'Tough',
               'flags': {'bullet': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Beak Blast',
               'num': 690,
               'onAfterMove': 'function (pokemon) {\n'
                              "\t\t\tpokemon.removeVolatile('beakblast');\n"
                              '\t\t}',
               'pp': 15,
               'priority': -3,
               'secondary': None,
               'target': 'normal',
               'type': 'Flying'},
 'beatup': {'accuracy': 100,
            'basePower': 0,
            'basePowerCallback': 'function (pokemon, target, move) {\n'
                                 '\t\t\treturn 5 + '
                                 'Math.floor(move.allies.shift().species.baseStats.atk '
                                 '/ 10);\n'
                                 '\t\t}',
            'category': 'Physical',
            'contestType': 'Clever',
            'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
            'name': 'Beat Up',
            'num': 251,
            'onModifyMove': 'function (move, pokemon) {\n'
                            '\t\t\tmove.allies = '
                            'pokemon.side.pokemon.filter(function (ally) { '
                            'return ally === pokemon || !ally.fainted && '
                            '!ally.status; });\n'
                            '\t\t\tmove.multihit = move.allies.length;\n'
                            '\t\t}',
            'pp': 10,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Dark'},
 'behemothbash': {'accuracy': 100,
                  'basePower': 100,
                  'category': 'Physical',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Behemoth Bash',
                  'num': 782,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Steel'},
 'behemothblade': {'accuracy': 100,
                   'basePower': 100,
                   'category': 'Physical',
                   'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                   'name': 'Behemoth Blade',
                   'num': 781,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Steel'},
 'belch': {'accuracy': 90,
           'basePower': 120,
           'category': 'Special',
           'contestType': 'Tough',
           'flags': {'protect': 1},
           'name': 'Belch',
           'num': 562,
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Poison'},
 'bellydrum': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'snatch': 1},
               'name': 'Belly Drum',
               'num': 187,
               'onHit': 'function (target) {\n'
                        '\t\t\tif (target.hp <= target.maxhp / 2 || '
                        'target.boosts.atk >= 6 || target.maxhp === 1) { // '
                        'Shedinja clause\n'
                        '\t\t\t\treturn false;\n'
                        '\t\t\t}\n'
                        '\t\t\tthis.directDamage(target.maxhp / 2);\n'
                        '\t\t\tthis.boost({ atk: 12 }, target);\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Normal',
               'zMove': {'effect': 'heal'}},
 'bestow': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Cute',
            'flags': {'authentic': 1, 'mirror': 1, 'mystery': 1},
            'isNonstandard': 'Past',
            'name': 'Bestow',
            'num': 516,
            'onHit': 'function (target, source, move) {\n'
                     '\t\t\tif (target.item) {\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\t}\n'
                     '\t\t\tvar myItem = source.takeItem();\n'
                     '\t\t\tif (!myItem)\n'
                     '\t\t\t\treturn false;\n'
                     "\t\t\tif (!this.singleEvent('TakeItem', myItem, "
                     'source.itemState, target, source, move, myItem) || '
                     '!target.setItem(myItem)) {\n'
                     '\t\t\t\tsource.item = myItem.id;\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\t}\n'
                     "\t\t\tthis.add('-item', target, myItem.name, '[from] "
                     "move: Bestow', '[of] ' + source);\n"
                     '\t\t}',
            'pp': 15,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'zMove': {'boost': {'spe': 2}}},
 'bide': {'accuracy': True,
          'basePower': 0,
          'beforeMoveCallback': 'function (pokemon) {\n'
                                "\t\t\tif (pokemon.volatiles['bide'])\n"
                                '\t\t\t\treturn true;\n'
                                '\t\t}',
          'category': 'Physical',
          'condition': {'duration': 3,
                        'onBeforeMove': 'function (pokemon, target, move) {\n'
                                        '\t\t\t\tif (this.effectState.duration '
                                        '=== 1) {\n'
                                        "\t\t\t\t\tthis.add('-end', pokemon, "
                                        "'move: Bide');\n"
                                        '\t\t\t\t\ttarget = '
                                        'this.effectState.lastDamageSource;\n'
                                        '\t\t\t\t\tif (!target || '
                                        '!this.effectState.totalDamage) {\n'
                                        '\t\t\t\t\t\t'
                                        "this.attrLastMove('[still]');\n"
                                        "\t\t\t\t\t\tthis.add('-fail', "
                                        'pokemon);\n'
                                        '\t\t\t\t\t\treturn false;\n'
                                        '\t\t\t\t\t}\n'
                                        '\t\t\t\t\tif (!target.isActive) {\n'
                                        '\t\t\t\t\t\tvar possibleTarget = '
                                        'this.getRandomTarget(pokemon, '
                                        "this.dex.moves.get('pound'));\n"
                                        '\t\t\t\t\t\tif (!possibleTarget) {\n'
                                        "\t\t\t\t\t\t\tthis.add('-miss', "
                                        'pokemon);\n'
                                        '\t\t\t\t\t\t\treturn false;\n'
                                        '\t\t\t\t\t\t}\n'
                                        '\t\t\t\t\t\ttarget = possibleTarget;\n'
                                        '\t\t\t\t\t}\n'
                                        '\t\t\t\t\tvar moveData = {\n'
                                        "\t\t\t\t\t\tid: 'bide',\n"
                                        '\t\t\t\t\t\tname: "Bide",\n'
                                        '\t\t\t\t\t\taccuracy: true,\n'
                                        '\t\t\t\t\t\tdamage: '
                                        'this.effectState.totalDamage * 2,\n'
                                        '\t\t\t\t\t\tcategory: "Physical",\n'
                                        '\t\t\t\t\t\tpriority: 1,\n'
                                        '\t\t\t\t\t\tflags: { contact: 1, '
                                        'protect: 1 },\n'
                                        "\t\t\t\t\t\teffectType: 'Move',\n"
                                        "\t\t\t\t\t\ttype: 'Normal',\n"
                                        '\t\t\t\t\t};\n'
                                        '\t\t\t\t\t'
                                        'this.actions.tryMoveHit(target, '
                                        'pokemon, moveData);\n'
                                        '\t\t\t\t\t'
                                        "pokemon.removeVolatile('bide');\n"
                                        '\t\t\t\t\treturn false;\n'
                                        '\t\t\t\t}\n'
                                        "\t\t\t\tthis.add('-activate', "
                                        "pokemon, 'move: Bide');\n"
                                        '\t\t\t}',
                        'onDamage': 'function (damage, target, source, move) '
                                    '{\n'
                                    '\t\t\t\tif (!move || move.effectType !== '
                                    "'Move' || !source)\n"
                                    '\t\t\t\t\treturn;\n'
                                    '\t\t\t\tthis.effectState.totalDamage += '
                                    'damage;\n'
                                    '\t\t\t\tthis.effectState.lastDamageSource '
                                    '= source;\n'
                                    '\t\t\t}',
                        'onDamagePriority': -101,
                        'onEnd': 'function (pokemon) {\n'
                                 "\t\t\t\tthis.add('-end', pokemon, 'move: "
                                 "Bide', '[silent]');\n"
                                 '\t\t\t}',
                        'onLockMove': 'bide',
                        'onMoveAborted': 'function (pokemon) {\n'
                                         '\t\t\t\t'
                                         "pokemon.removeVolatile('bide');\n"
                                         '\t\t\t}',
                        'onStart': 'function (pokemon) {\n'
                                   '\t\t\t\tthis.effectState.totalDamage = 0;\n'
                                   "\t\t\t\tthis.add('-start', pokemon, 'move: "
                                   "Bide');\n"
                                   '\t\t\t}'},
          'contestType': 'Tough',
          'flags': {'contact': 1, 'protect': 1},
          'ignoreImmunity': True,
          'isNonstandard': 'Past',
          'name': 'Bide',
          'num': 117,
          'pp': 10,
          'priority': 1,
          'secondary': None,
          'target': 'self',
          'type': 'Normal',
          'volatileStatus': 'bide'},
 'bind': {'accuracy': 85,
          'basePower': 15,
          'category': 'Physical',
          'contestType': 'Tough',
          'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
          'name': 'Bind',
          'num': 20,
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Normal',
          'volatileStatus': 'partiallytrapped'},
 'bite': {'accuracy': 100,
          'basePower': 60,
          'category': 'Physical',
          'contestType': 'Tough',
          'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
          'name': 'Bite',
          'num': 44,
          'pp': 25,
          'priority': 0,
          'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
          'target': 'normal',
          'type': 'Dark'},
 'blackholeeclipse': {'accuracy': True,
                      'basePower': 1,
                      'category': 'Physical',
                      'contestType': 'Cool',
                      'flags': {},
                      'isNonstandard': 'Past',
                      'isZ': 'darkiniumz',
                      'name': 'Black Hole Eclipse',
                      'num': 654,
                      'pp': 1,
                      'priority': 0,
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Dark'},
 'blastburn': {'accuracy': 90,
               'basePower': 150,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
               'name': 'Blast Burn',
               'num': 307,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'self': {'volatileStatus': 'mustrecharge'},
               'target': 'normal',
               'type': 'Fire'},
 'blazekick': {'accuracy': 90,
               'basePower': 85,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Blaze Kick',
               'num': 299,
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 10, 'status': 'brn'},
               'target': 'normal',
               'type': 'Fire'},
 'blizzard': {'accuracy': 70,
              'basePower': 110,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Blizzard',
              'num': 59,
              'onModifyMove': 'function (move) {\n'
                              "\t\t\tif (this.field.isWeather('hail'))\n"
                              '\t\t\t\tmove.accuracy = true;\n'
                              '\t\t}',
              'pp': 5,
              'priority': 0,
              'secondary': {'chance': 10, 'status': 'frz'},
              'target': 'allAdjacentFoes',
              'type': 'Ice'},
 'block': {'accuracy': True,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Cute',
           'flags': {'mirror': 1, 'reflectable': 1},
           'name': 'Block',
           'num': 335,
           'onHit': 'function (target, source, move) {\n'
                    "\t\t\treturn target.addVolatile('trapped', source, move, "
                    "'trapper');\n"
                    '\t\t}',
           'pp': 5,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal',
           'zMove': {'boost': {'def': 1}}},
 'bloomdoom': {'accuracy': True,
               'basePower': 1,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {},
               'isNonstandard': 'Past',
               'isZ': 'grassiumz',
               'name': 'Bloom Doom',
               'num': 644,
               'pp': 1,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'blueflare': {'accuracy': 85,
               'basePower': 130,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Blue Flare',
               'num': 551,
               'pp': 5,
               'priority': 0,
               'secondary': {'chance': 20, 'status': 'brn'},
               'target': 'normal',
               'type': 'Fire'},
 'bodypress': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Body Press',
               'num': 776,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fighting',
               'useSourceDefensiveAsOffensive': True},
 'bodyslam': {'accuracy': 100,
              'basePower': 85,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
              'name': 'Body Slam',
              'num': 34,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 30, 'status': 'par'},
              'target': 'normal',
              'type': 'Normal'},
 'boltbeak': {'accuracy': 100,
              'basePower': 85,
              'basePowerCallback': 'function (pokemon, target, move) {\n'
                                   '\t\t\tif (target.newlySwitched || '
                                   'this.queue.willMove(target)) {\n'
                                   "\t\t\t\tthis.debug('Bolt Beak damage "
                                   "boost');\n"
                                   '\t\t\t\treturn move.basePower * 2;\n'
                                   '\t\t\t}\n'
                                   "\t\t\tthis.debug('Bolt Beak NOT "
                                   "boosted');\n"
                                   '\t\t\treturn move.basePower;\n'
                                   '\t\t}',
              'category': 'Physical',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Bolt Beak',
              'num': 754,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Electric'},
 'boltstrike': {'accuracy': 85,
                'basePower': 130,
                'category': 'Physical',
                'contestType': 'Beautiful',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Bolt Strike',
                'num': 550,
                'pp': 5,
                'priority': 0,
                'secondary': {'chance': 20, 'status': 'par'},
                'target': 'normal',
                'type': 'Electric'},
 'boneclub': {'accuracy': 85,
              'basePower': 65,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'mirror': 1, 'protect': 1},
              'isNonstandard': 'Past',
              'name': 'Bone Club',
              'num': 125,
              'pp': 20,
              'priority': 0,
              'secondary': {'chance': 10, 'volatileStatus': 'flinch'},
              'target': 'normal',
              'type': 'Ground'},
 'bonemerang': {'accuracy': 90,
                'basePower': 50,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 130},
                'multihit': 2,
                'name': 'Bonemerang',
                'num': 155,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ground'},
 'bonerush': {'accuracy': 90,
              'basePower': 25,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'mirror': 1, 'protect': 1},
              'maxMove': {'basePower': 130},
              'multihit': [2, 5],
              'name': 'Bone Rush',
              'num': 198,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Ground',
              'zMove': {'basePower': 140}},
 'boomburst': {'accuracy': 100,
               'basePower': 140,
               'category': 'Special',
               'contestType': 'Tough',
               'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
               'name': 'Boomburst',
               'num': 586,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacent',
               'type': 'Normal'},
 'bounce': {'accuracy': 85,
            'basePower': 85,
            'category': 'Physical',
            'condition': {'duration': 2,
                          'onInvulnerability': 'function (target, source, '
                                               'move) {\n'
                                               "\t\t\t\tif (['gust', "
                                               "'twister', 'skyuppercut', "
                                               "'thunder', 'hurricane', "
                                               "'smackdown', "
                                               "'thousandarrows'].includes(move.id)) "
                                               '{\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t\treturn false;\n'
                                               '\t\t\t}',
                          'onSourceBasePower': 'function (basePower, target, '
                                               'source, move) {\n'
                                               "\t\t\t\tif (move.id === 'gust' "
                                               "|| move.id === 'twister') {\n"
                                               '\t\t\t\t\treturn '
                                               'this.chainModify(2);\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}'},
            'contestType': 'Cute',
            'flags': {'charge': 1,
                      'contact': 1,
                      'distance': 1,
                      'gravity': 1,
                      'mirror': 1,
                      'protect': 1},
            'name': 'Bounce',
            'num': 340,
            'onTryMove': 'function (attacker, defender, move) {\n'
                         '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                         "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                         'defender, move)) {\n'
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tattacker.addVolatile('twoturnmove', "
                         'defender);\n'
                         '\t\t\treturn null;\n'
                         '\t\t}',
            'pp': 5,
            'priority': 0,
            'secondary': {'chance': 30, 'status': 'par'},
            'target': 'any',
            'type': 'Flying'},
 'bouncybubble': {'accuracy': 100,
                  'basePower': 60,
                  'category': 'Special',
                  'contestType': 'Clever',
                  'drain': [1, 2],
                  'flags': {'heal': 1, 'protect': 1},
                  'isNonstandard': 'LGPE',
                  'name': 'Bouncy Bubble',
                  'num': 733,
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Water'},
 'branchpoke': {'accuracy': 100,
                'basePower': 40,
                'category': 'Physical',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Branch Poke',
                'num': 785,
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Grass'},
 'bravebird': {'accuracy': 100,
               'basePower': 120,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1,
                         'distance': 1,
                         'mirror': 1,
                         'protect': 1},
               'name': 'Brave Bird',
               'num': 413,
               'pp': 15,
               'priority': 0,
               'recoil': [33, 100],
               'secondary': None,
               'target': 'any',
               'type': 'Flying'},
 'breakingswipe': {'accuracy': 100,
                   'basePower': 60,
                   'category': 'Physical',
                   'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                   'name': 'Breaking Swipe',
                   'num': 784,
                   'pp': 15,
                   'priority': 0,
                   'secondary': {'boosts': {'atk': -1}, 'chance': 100},
                   'target': 'allAdjacentFoes',
                   'type': 'Dragon'},
 'breakneckblitz': {'accuracy': True,
                    'basePower': 1,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'isNonstandard': 'Past',
                    'isZ': 'normaliumz',
                    'name': 'Breakneck Blitz',
                    'num': 622,
                    'pp': 1,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Normal'},
 'brickbreak': {'accuracy': 100,
                'basePower': 75,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Brick Break',
                'num': 280,
                'onTryHit': 'function (pokemon) {\n'
                            '\t\t\t// will shatter screens through sub, before '
                            'you hit\n'
                            '\t\t\t'
                            "pokemon.side.removeSideCondition('reflect');\n"
                            '\t\t\t'
                            "pokemon.side.removeSideCondition('lightscreen');\n"
                            '\t\t\t'
                            "pokemon.side.removeSideCondition('auroraveil');\n"
                            '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'brine': {'accuracy': 100,
           'basePower': 65,
           'category': 'Special',
           'contestType': 'Tough',
           'flags': {'mirror': 1, 'protect': 1},
           'name': 'Brine',
           'num': 362,
           'onBasePower': 'function (basePower, pokemon, target) {\n'
                          '\t\t\tif (target.hp * 2 <= target.maxhp) {\n'
                          '\t\t\t\treturn this.chainModify(2);\n'
                          '\t\t\t}\n'
                          '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Water'},
 'brutalswing': {'accuracy': 100,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Brutal Swing',
                 'num': 693,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'allAdjacent',
                 'type': 'Dark'},
 'bubble': {'accuracy': 100,
            'basePower': 40,
            'category': 'Special',
            'contestType': 'Cute',
            'flags': {'mirror': 1, 'protect': 1},
            'isNonstandard': 'Past',
            'name': 'Bubble',
            'num': 145,
            'pp': 30,
            'priority': 0,
            'secondary': {'boosts': {'spe': -1}, 'chance': 10},
            'target': 'allAdjacentFoes',
            'type': 'Water'},
 'bubblebeam': {'accuracy': 100,
                'basePower': 65,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Bubble Beam',
                'num': 61,
                'pp': 20,
                'priority': 0,
                'secondary': {'boosts': {'spe': -1}, 'chance': 10},
                'target': 'normal',
                'type': 'Water'},
 'bugbite': {'accuracy': 100,
             'basePower': 60,
             'category': 'Physical',
             'contestType': 'Cute',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Bug Bite',
             'num': 450,
             'onHit': 'function (target, source) {\n'
                      '\t\t\tvar item = target.getItem();\n'
                      '\t\t\tif (source.hp && item.isBerry && '
                      'target.takeItem(source)) {\n'
                      "\t\t\t\tthis.add('-enditem', target, item.name, '[from] "
                      "stealeat', '[move] Bug Bite', '[of] ' + source);\n"
                      "\t\t\t\tif (this.singleEvent('Eat', item, null, source, "
                      'null, null)) {\n'
                      "\t\t\t\t\tthis.runEvent('EatItem', source, null, null, "
                      'item);\n'
                      "\t\t\t\t\tif (item.id === 'leppaberry')\n"
                      "\t\t\t\t\t\ttarget.staleness = 'external';\n"
                      '\t\t\t\t}\n'
                      '\t\t\t\tif (item.onEat)\n'
                      '\t\t\t\t\tsource.ateBerry = true;\n'
                      '\t\t\t}\n'
                      '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Bug'},
 'bugbuzz': {'accuracy': 100,
             'basePower': 90,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
             'name': 'Bug Buzz',
             'num': 405,
             'pp': 10,
             'priority': 0,
             'secondary': {'boosts': {'spd': -1}, 'chance': 10},
             'target': 'normal',
             'type': 'Bug'},
 'bulkup': {'accuracy': True,
            'basePower': 0,
            'boosts': {'atk': 1, 'def': 1},
            'category': 'Status',
            'contestType': 'Cool',
            'flags': {'snatch': 1},
            'name': 'Bulk Up',
            'num': 339,
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Fighting',
            'zMove': {'boost': {'atk': 1}}},
 'bulldoze': {'accuracy': 100,
              'basePower': 60,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
              'name': 'Bulldoze',
              'num': 523,
              'pp': 20,
              'priority': 0,
              'secondary': {'boosts': {'spe': -1}, 'chance': 100},
              'target': 'allAdjacent',
              'type': 'Ground'},
 'bulletpunch': {'accuracy': 100,
                 'basePower': 40,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                 'name': 'Bullet Punch',
                 'num': 418,
                 'pp': 30,
                 'priority': 1,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Steel'},
 'bulletseed': {'accuracy': 100,
                'basePower': 25,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 130},
                'multihit': [2, 5],
                'name': 'Bullet Seed',
                'num': 331,
                'pp': 30,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Grass',
                'zMove': {'basePower': 140}},
 'burningjealousy': {'accuracy': 100,
                     'basePower': 70,
                     'category': 'Special',
                     'contestType': 'Tough',
                     'flags': {'mirror': 1, 'protect': 1},
                     'name': 'Burning Jealousy',
                     'num': 807,
                     'pp': 5,
                     'priority': 0,
                     'secondary': {'chance': 100,
                                   'onHit': 'function (target, source, move) '
                                            '{\n'
                                            '\t\t\t\tif (target === null || '
                                            'target === void 0 ? void 0 : '
                                            'target.statsRaisedThisTurn) {\n'
                                            '\t\t\t\t\t'
                                            "target.trySetStatus('brn', "
                                            'source, move);\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}'},
                     'target': 'allAdjacentFoes',
                     'type': 'Fire'},
 'burnup': {'accuracy': 100,
            'basePower': 130,
            'category': 'Special',
            'contestType': 'Clever',
            'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
            'name': 'Burn Up',
            'num': 682,
            'onTryMove': 'function (pokemon, target, move) {\n'
                         "\t\t\tif (pokemon.hasType('Fire'))\n"
                         '\t\t\t\treturn;\n'
                         "\t\t\tthis.add('-fail', pokemon, 'move: Burn Up');\n"
                         "\t\t\tthis.attrLastMove('[still]');\n"
                         '\t\t\treturn null;\n'
                         '\t\t}',
            'pp': 5,
            'priority': 0,
            'secondary': None,
            'self': {'onHit': 'function (pokemon) {\n'
                              '\t\t\t\t'
                              'pokemon.setType(pokemon.getTypes(true).map(function '
                              '(type) { return type === "Fire" ? "???" : type; '
                              '}));\n'
                              "\t\t\t\tthis.add('-start', pokemon, "
                              "'typechange', pokemon.types.join('/'), '[from] "
                              "move: Burn Up');\n"
                              '\t\t\t}'},
            'target': 'normal',
            'type': 'Fire'},
 'buzzybuzz': {'accuracy': 100,
               'basePower': 60,
               'category': 'Special',
               'contestType': 'Clever',
               'flags': {'protect': 1},
               'isNonstandard': 'LGPE',
               'name': 'Buzzy Buzz',
               'num': 734,
               'pp': 20,
               'priority': 0,
               'secondary': {'chance': 100, 'status': 'par'},
               'target': 'normal',
               'type': 'Electric'},
 'calmmind': {'accuracy': True,
              'basePower': 0,
              'boosts': {'spa': 1, 'spd': 1},
              'category': 'Status',
              'contestType': 'Clever',
              'flags': {'snatch': 1},
              'name': 'Calm Mind',
              'num': 347,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Psychic',
              'zMove': {'effect': 'clearnegativeboost'}},
 'camouflage': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'snatch': 1},
                'isNonstandard': 'Past',
                'name': 'Camouflage',
                'num': 293,
                'onHit': 'function (target) {\n'
                         "\t\t\tvar newType = 'Normal';\n"
                         "\t\t\tif (this.field.isTerrain('electricterrain')) "
                         '{\n'
                         "\t\t\t\tnewType = 'Electric';\n"
                         '\t\t\t}\n'
                         '\t\t\telse if '
                         "(this.field.isTerrain('grassyterrain')) {\n"
                         "\t\t\t\tnewType = 'Grass';\n"
                         '\t\t\t}\n'
                         "\t\t\telse if (this.field.isTerrain('mistyterrain')) "
                         '{\n'
                         "\t\t\t\tnewType = 'Fairy';\n"
                         '\t\t\t}\n'
                         '\t\t\telse if '
                         "(this.field.isTerrain('psychicterrain')) {\n"
                         "\t\t\t\tnewType = 'Psychic';\n"
                         '\t\t\t}\n'
                         '\t\t\tif (target.getTypes().join() === newType || '
                         '!target.setType(newType))\n'
                         '\t\t\t\treturn false;\n'
                         "\t\t\tthis.add('-start', target, 'typechange', "
                         'newType);\n'
                         '\t\t}',
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'boost': {'evasion': 1}}},
 'captivate': {'accuracy': 100,
               'basePower': 0,
               'boosts': {'spa': -2},
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'isNonstandard': 'Past',
               'name': 'Captivate',
               'num': 445,
               'onTryImmunity': 'function (pokemon, source) {\n'
                                "\t\t\treturn (pokemon.gender === 'M' && "
                                "source.gender === 'F') || (pokemon.gender === "
                                "'F' && source.gender === 'M');\n"
                                '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Normal',
               'zMove': {'boost': {'spd': 2}}},
 'catastropika': {'accuracy': True,
                  'basePower': 210,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {'contact': 1},
                  'isNonstandard': 'Past',
                  'isZ': 'pikaniumz',
                  'name': 'Catastropika',
                  'num': 658,
                  'pp': 1,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Electric'},
 'celebrate': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {},
               'name': 'Celebrate',
               'num': 606,
               'onTryHit': 'function (target, source) {\n'
                           "\t\t\tthis.add('-activate', target, 'move: "
                           "Celebrate');\n"
                           '\t\t}',
               'pp': 40,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Normal',
               'zMove': {'boost': {'atk': 1,
                                   'def': 1,
                                   'spa': 1,
                                   'spd': 1,
                                   'spe': 1}}},
 'charge': {'accuracy': True,
            'basePower': 0,
            'boosts': {'spd': 1},
            'category': 'Status',
            'condition': {'duration': 2,
                          'onBasePower': 'function (basePower, attacker, '
                                         'defender, move) {\n'
                                         '\t\t\t\tif (move.type === '
                                         "'Electric') {\n"
                                         "\t\t\t\t\tthis.debug('charge "
                                         "boost');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(2);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}',
                          'onBasePowerPriority': 9,
                          'onRestart': 'function (pokemon) {\n'
                                       '\t\t\t\tthis.effectState.duration = '
                                       '2;\n'
                                       '\t\t\t}'},
            'contestType': 'Clever',
            'flags': {'snatch': 1},
            'name': 'Charge',
            'num': 268,
            'onHit': 'function (pokemon) {\n'
                     "\t\t\tthis.add('-activate', pokemon, 'move: Charge');\n"
                     '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Electric',
            'volatileStatus': 'charge',
            'zMove': {'boost': {'spd': 1}}},
 'chargebeam': {'accuracy': 90,
                'basePower': 50,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Charge Beam',
                'num': 451,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 70, 'self': {'boosts': {'spa': 1}}},
                'target': 'normal',
                'type': 'Electric'},
 'charm': {'accuracy': 100,
           'basePower': 0,
           'boosts': {'atk': -2},
           'category': 'Status',
           'contestType': 'Cute',
           'flags': {'mirror': 1, 'mystery': 1, 'protect': 1, 'reflectable': 1},
           'name': 'Charm',
           'num': 204,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Fairy',
           'zMove': {'boost': {'def': 1}}},
 'chatter': {'accuracy': 100,
             'basePower': 65,
             'category': 'Special',
             'contestType': 'Cute',
             'flags': {'authentic': 1,
                       'distance': 1,
                       'mirror': 1,
                       'protect': 1,
                       'sound': 1},
             'isNonstandard': 'Past',
             'name': 'Chatter',
             'noSketch': True,
             'num': 448,
             'pp': 20,
             'priority': 0,
             'secondary': {'chance': 100, 'volatileStatus': 'confusion'},
             'target': 'any',
             'type': 'Flying'},
 'chipaway': {'accuracy': 100,
              'basePower': 70,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'ignoreDefensive': True,
              'ignoreEvasion': True,
              'isNonstandard': 'Past',
              'name': 'Chip Away',
              'num': 498,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'circlethrow': {'accuracy': 90,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'forceSwitch': True,
                 'name': 'Circle Throw',
                 'num': 509,
                 'pp': 10,
                 'priority': -6,
                 'target': 'normal',
                 'type': 'Fighting'},
 'clamp': {'accuracy': 85,
           'basePower': 35,
           'category': 'Physical',
           'contestType': 'Tough',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'isNonstandard': 'Past',
           'name': 'Clamp',
           'num': 128,
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Water',
           'volatileStatus': 'partiallytrapped'},
 'clangingscales': {'accuracy': 100,
                    'basePower': 110,
                    'category': 'Special',
                    'contestType': 'Tough',
                    'flags': {'authentic': 1,
                              'mirror': 1,
                              'protect': 1,
                              'sound': 1},
                    'name': 'Clanging Scales',
                    'num': 691,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'selfBoost': {'boosts': {'def': -1}},
                    'target': 'allAdjacentFoes',
                    'type': 'Dragon'},
 'clangoroussoul': {'accuracy': 100,
                    'basePower': 0,
                    'boosts': {'atk': 1,
                               'def': 1,
                               'spa': 1,
                               'spd': 1,
                               'spe': 1},
                    'category': 'Status',
                    'flags': {'dance': 1, 'snatch': 1, 'sound': 1},
                    'name': 'Clangorous Soul',
                    'num': 775,
                    'onHit': 'function (pokemon) {\n'
                             '\t\t\tthis.directDamage(pokemon.maxhp * 33 / '
                             '100);\n'
                             '\t\t}',
                    'onTry': 'function (source) {\n'
                             '\t\t\tif (source.hp <= (source.maxhp * 33 / 100) '
                             '|| source.maxhp === 1)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t}',
                    'onTryHit': 'function (pokemon, target, move) {\n'
                                '\t\t\tif (!this.boost(move.boosts))\n'
                                '\t\t\t\treturn null;\n'
                                '\t\t\tdelete move.boosts;\n'
                                '\t\t}',
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'target': 'self',
                    'type': 'Dragon'},
 'clangoroussoulblaze': {'accuracy': True,
                         'basePower': 185,
                         'category': 'Special',
                         'contestType': 'Cool',
                         'flags': {'authentic': 1, 'sound': 1},
                         'isNonstandard': 'Past',
                         'isZ': 'kommoniumz',
                         'name': 'Clangorous Soulblaze',
                         'num': 728,
                         'pp': 1,
                         'priority': 0,
                         'secondary': {},
                         'selfBoost': {'boosts': {'atk': 1,
                                                  'def': 1,
                                                  'spa': 1,
                                                  'spd': 1,
                                                  'spe': 1}},
                         'target': 'allAdjacentFoes',
                         'type': 'Dragon'},
 'clearsmog': {'accuracy': True,
               'basePower': 50,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Clear Smog',
               'num': 499,
               'onHit': 'function (target) {\n'
                        '\t\t\ttarget.clearBoosts();\n'
                        "\t\t\tthis.add('-clearboost', target);\n"
                        '\t\t}',
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Poison'},
 'closecombat': {'accuracy': 100,
                 'basePower': 120,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Close Combat',
                 'num': 370,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'boosts': {'def': -1, 'spd': -1}},
                 'target': 'normal',
                 'type': 'Fighting'},
 'coaching': {'accuracy': True,
              'basePower': 0,
              'boosts': {'atk': 1, 'def': 1},
              'category': 'Status',
              'flags': {'authentic': 1},
              'name': 'Coaching',
              'num': 811,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'adjacentAlly',
              'type': 'Fighting'},
 'coil': {'accuracy': True,
          'basePower': 0,
          'boosts': {'accuracy': 1, 'atk': 1, 'def': 1},
          'category': 'Status',
          'contestType': 'Tough',
          'flags': {'snatch': 1},
          'name': 'Coil',
          'num': 489,
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'target': 'self',
          'type': 'Poison',
          'zMove': {'effect': 'clearnegativeboost'}},
 'cometpunch': {'accuracy': 85,
                'basePower': 18,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                'isNonstandard': 'Past',
                'maxMove': {'basePower': 100},
                'multihit': [2, 5],
                'name': 'Comet Punch',
                'num': 4,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'confide': {'accuracy': True,
             'basePower': 0,
             'boosts': {'spa': -1},
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {'authentic': 1,
                       'mirror': 1,
                       'reflectable': 1,
                       'sound': 1},
             'name': 'Confide',
             'num': 590,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'zMove': {'boost': {'spd': 1}}},
 'confuseray': {'accuracy': 100,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                'name': 'Confuse Ray',
                'num': 109,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ghost',
                'volatileStatus': 'confusion',
                'zMove': {'boost': {'spa': 1}}},
 'confusion': {'accuracy': 100,
               'basePower': 50,
               'category': 'Special',
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Confusion',
               'num': 93,
               'pp': 25,
               'priority': 0,
               'secondary': {'chance': 10, 'volatileStatus': 'confusion'},
               'target': 'normal',
               'type': 'Psychic'},
 'constrict': {'accuracy': 100,
               'basePower': 10,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Constrict',
               'num': 132,
               'pp': 35,
               'priority': 0,
               'secondary': {'boosts': {'spe': -1}, 'chance': 10},
               'target': 'normal',
               'type': 'Normal'},
 'continentalcrush': {'accuracy': True,
                      'basePower': 1,
                      'category': 'Physical',
                      'contestType': 'Cool',
                      'flags': {},
                      'isNonstandard': 'Past',
                      'isZ': 'rockiumz',
                      'name': 'Continental Crush',
                      'num': 632,
                      'pp': 1,
                      'priority': 0,
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Rock'},
 'conversion': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Beautiful',
                'flags': {'snatch': 1},
                'name': 'Conversion',
                'num': 160,
                'onHit': 'function (target) {\n'
                         '\t\t\tvar type = '
                         'this.dex.moves.get(target.moveSlots[0].id).type;\n'
                         '\t\t\tif (target.hasType(type) || '
                         '!target.setType(type))\n'
                         '\t\t\t\treturn false;\n'
                         "\t\t\tthis.add('-start', target, 'typechange', "
                         'type);\n'
                         '\t\t}',
                'pp': 30,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'boost': {'atk': 1,
                                    'def': 1,
                                    'spa': 1,
                                    'spd': 1,
                                    'spe': 1}}},
 'conversion2': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {'authentic': 1},
                 'name': 'Conversion 2',
                 'num': 176,
                 'onHit': 'function (target, source) {\n'
                          '\t\t\tif (!target.lastMoveUsed) {\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t\tvar possibleTypes = [];\n'
                          '\t\t\tvar attackType = target.lastMoveUsed.type;\n'
                          '\t\t\tfor (var _i = 0, _a = this.dex.types.names(); '
                          '_i < _a.length; _i++) {\n'
                          '\t\t\t\tvar type = _a[_i];\n'
                          '\t\t\t\tif (source.hasType(type))\n'
                          '\t\t\t\t\tcontinue;\n'
                          '\t\t\t\tvar typeCheck = '
                          'this.dex.types.get(type).damageTaken[attackType];\n'
                          '\t\t\t\tif (typeCheck === 2 || typeCheck === 3) {\n'
                          '\t\t\t\t\tpossibleTypes.push(type);\n'
                          '\t\t\t\t}\n'
                          '\t\t\t}\n'
                          '\t\t\tif (!possibleTypes.length) {\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t\tvar randomType = this.sample(possibleTypes);\n'
                          '\t\t\tif (!source.setType(randomType))\n'
                          '\t\t\t\treturn false;\n'
                          "\t\t\tthis.add('-start', source, 'typechange', "
                          'randomType);\n'
                          '\t\t}',
                 'pp': 30,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'effect': 'heal'}},
 'copycat': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {},
             'name': 'Copycat',
             'num': 383,
             'onHit': 'function (pokemon) {\n'
                      '\t\t\tvar noCopycat = [\n'
                      "\t\t\t\t'assist', 'banefulbunker', 'beakblast', "
                      "'behemothbash', 'behemothblade', 'belch', 'bestow', "
                      "'celebrate', 'chatter', 'circlethrow', 'copycat', "
                      "'counter', 'covet', 'craftyshield', 'destinybond', "
                      "'detect', 'dragontail', 'dynamaxcannon', 'endure', "
                      "'feint', 'focuspunch', 'followme', 'helpinghand', "
                      "'holdhands', 'kingsshield', 'matblock', 'mefirst', "
                      "'metronome', 'mimic', 'mirrorcoat', 'mirrormove', "
                      "'naturepower', 'obstruct', 'protect', 'ragepowder', "
                      "'roar', 'shelltrap', 'sketch', 'sleeptalk', 'snatch', "
                      "'spikyshield', 'spotlight', 'struggle', 'switcheroo', "
                      "'thief', 'transform', 'trick', 'whirlwind',\n"
                      '\t\t\t];\n'
                      '\t\t\tvar move = this.lastMove;\n'
                      '\t\t\tif (!move)\n'
                      '\t\t\t\treturn;\n'
                      '\t\t\tif (move.isMax && move.baseMove)\n'
                      '\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n'
                      '\t\t\tif (noCopycat.includes(move.id) || move.isZ || '
                      'move.isMax) {\n'
                      '\t\t\t\treturn false;\n'
                      '\t\t\t}\n'
                      '\t\t\tthis.actions.useMove(move.id, pokemon);\n'
                      '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'boost': {'accuracy': 1}}},
 'coreenforcer': {'accuracy': 100,
                  'basePower': 100,
                  'category': 'Special',
                  'contestType': 'Tough',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Core Enforcer',
                  'num': 687,
                  'onAfterSubDamage': 'function (damage, target) {\n'
                                      '\t\t\tif '
                                      '(target.getAbility().isPermanent)\n'
                                      '\t\t\t\treturn;\n'
                                      '\t\t\tif (target.newlySwitched || '
                                      'this.queue.willMove(target))\n'
                                      '\t\t\t\treturn;\n'
                                      '\t\t\t'
                                      "target.addVolatile('gastroacid');\n"
                                      '\t\t}',
                  'onHit': 'function (target) {\n'
                           '\t\t\tif (target.getAbility().isPermanent)\n'
                           '\t\t\t\treturn;\n'
                           '\t\t\tif (target.newlySwitched || '
                           'this.queue.willMove(target))\n'
                           '\t\t\t\treturn;\n'
                           "\t\t\ttarget.addVolatile('gastroacid');\n"
                           '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allAdjacentFoes',
                  'type': 'Dragon',
                  'zMove': {'basePower': 140}},
 'corkscrewcrash': {'accuracy': True,
                    'basePower': 1,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'isNonstandard': 'Past',
                    'isZ': 'steeliumz',
                    'name': 'Corkscrew Crash',
                    'num': 638,
                    'pp': 1,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Steel'},
 'corrosivegas': {'accuracy': 100,
                  'basePower': 0,
                  'category': 'Status',
                  'flags': {'mirror': 1,
                            'mystery': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': 'Corrosive Gas',
                  'num': 810,
                  'onHit': 'function (target, source) {\n'
                           '\t\t\tvar item = target.takeItem(source);\n'
                           '\t\t\tif (item) {\n'
                           "\t\t\t\tthis.add('-enditem', target, item.name, "
                           "'[from] move: Corrosive Gas', '[of] ' + source);\n"
                           '\t\t\t}\n'
                           '\t\t\telse {\n'
                           "\t\t\t\tthis.add('-fail', target, 'move: Corrosive "
                           "Gas');\n"
                           '\t\t\t}\n'
                           '\t\t}',
                  'pp': 40,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allAdjacent',
                  'type': 'Poison'},
 'cosmicpower': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'def': 1, 'spd': 1},
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {'snatch': 1},
                 'name': 'Cosmic Power',
                 'num': 322,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Psychic',
                 'zMove': {'boost': {'spd': 1}}},
 'cottonguard': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'def': 3},
                 'category': 'Status',
                 'contestType': 'Cute',
                 'flags': {'snatch': 1},
                 'name': 'Cotton Guard',
                 'num': 538,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Grass',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'cottonspore': {'accuracy': 100,
                 'basePower': 0,
                 'boosts': {'spe': -2},
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1,
                           'powder': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'name': 'Cotton Spore',
                 'num': 178,
                 'pp': 40,
                 'priority': 0,
                 'secondary': None,
                 'target': 'allAdjacentFoes',
                 'type': 'Grass',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'counter': {'accuracy': 100,
             'basePower': 0,
             'beforeTurnCallback': 'function (pokemon) {\n'
                                   "\t\t\tpokemon.addVolatile('counter');\n"
                                   '\t\t}',
             'category': 'Physical',
             'condition': {'duration': 1,
                           'noCopy': True,
                           'onDamagingHit': 'function (damage, target, source, '
                                            'move) {\n'
                                            '\t\t\t\tif '
                                            '(!source.isAlly(target) && '
                                            'this.getCategory(move) === '
                                            "'Physical') {\n"
                                            '\t\t\t\t\tthis.effectState.slot = '
                                            'source.getSlot();\n'
                                            '\t\t\t\t\tthis.effectState.damage '
                                            '= 2 * damage;\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}',
                           'onRedirectTarget': 'function (target, source, '
                                               'source2, move) {\n'
                                               '\t\t\t\tif (move.id !== '
                                               "'counter')\n"
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\tif (source !== '
                                               'this.effectState.target || '
                                               '!this.effectState.slot)\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\treturn '
                                               'this.getAtSlot(this.effectState.slot);\n'
                                               '\t\t\t}',
                           'onRedirectTargetPriority': -1,
                           'onStart': 'function (target, source, move) {\n'
                                      '\t\t\t\tthis.effectState.slot = null;\n'
                                      '\t\t\t\tthis.effectState.damage = 0;\n'
                                      '\t\t\t}'},
             'contestType': 'Tough',
             'damageCallback': 'function (pokemon) {\n'
                               "\t\t\tif (!pokemon.volatiles['counter'])\n"
                               '\t\t\t\treturn 0;\n'
                               '\t\t\treturn '
                               "pokemon.volatiles['counter'].damage || 1;\n"
                               '\t\t}',
             'flags': {'contact': 1, 'protect': 1},
             'maxMove': {'basePower': 75},
             'name': 'Counter',
             'num': 68,
             'onTryHit': 'function (target, source, move) {\n'
                         "\t\t\tif (!source.volatiles['counter'])\n"
                         '\t\t\t\treturn false;\n'
                         "\t\t\tif (source.volatiles['counter'].slot === "
                         'null)\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t}',
             'pp': 20,
             'priority': -5,
             'secondary': None,
             'target': 'scripted',
             'type': 'Fighting'},
 'courtchange': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'flags': {'mirror': 1},
                 'name': 'Court Change',
                 'num': 756,
                 'onHitField': 'function (target, source) {\n'
                               '\t\t\tvar _a, _b;\n'
                               '\t\t\tvar sideConditions = [\n'
                               "\t\t\t\t'mist', 'lightscreen', 'reflect', "
                               "'spikes', 'safeguard', 'tailwind', "
                               "'toxicspikes', 'stealthrock', 'waterpledge', "
                               "'firepledge', 'grasspledge', 'stickyweb', "
                               "'auroraveil', 'gmaxsteelsurge', "
                               "'gmaxcannonade', 'gmaxvinelash', "
                               "'gmaxwildfire',\n"
                               '\t\t\t];\n'
                               '\t\t\tvar success = false;\n'
                               '\t\t\tif (this.gameType === "freeforall") {\n'
                               '\t\t\t\t// random integer from 1-3 inclusive\n'
                               '\t\t\t\tvar offset = this.random(3) + 1;\n'
                               '\t\t\t\t// the list of all sides in '
                               'counterclockwise order\n'
                               '\t\t\t\tvar sides = [this.sides[0], '
                               'this.sides[2], this.sides[1], this.sides[3]];\n'
                               '\t\t\t\tfor (var _i = 0, sideConditions_1 = '
                               'sideConditions; _i < sideConditions_1.length; '
                               '_i++) {\n'
                               '\t\t\t\t\tvar id = sideConditions_1[_i];\n'
                               '\t\t\t\t\tvar effectName = '
                               'this.dex.conditions.get(id).name;\n'
                               '\t\t\t\t\tvar rotatedSides = [];\n'
                               '\t\t\t\t\tvar someCondition = false;\n'
                               '\t\t\t\t\tfor (var i = 0; i < 4; i++) {\n'
                               '\t\t\t\t\t\tvar sourceSide = sides[i];\n'
                               '\t\t\t\t\t\tvar targetSide = sides[(i + '
                               'offset) % 4]; // the next side in rotation\n'
                               '\t\t\t\t\t\t'
                               'rotatedSides.push(targetSide.sideConditions[id]);\n'
                               '\t\t\t\t\t\tif (sourceSide.sideConditions[id]) '
                               '{\n'
                               "\t\t\t\t\t\t\tthis.add('-sideend', sourceSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t\t\tsomeCondition = true;\n'
                               '\t\t\t\t\t\t}\n'
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tif (!someCondition)\n'
                               '\t\t\t\t\t\tcontinue;\n'
                               '\t\t\t\t\t_a = __spreadArrays(rotatedSides), '
                               'sides[0].sideConditions[id] = _a[0], '
                               'sides[1].sideConditions[id] = _a[1], '
                               'sides[2].sideConditions[id] = _a[2], '
                               'sides[3].sideConditions[id] = _a[3];\n'
                               '\t\t\t\t\tfor (var _c = 0, sides_1 = sides; _c '
                               '< sides_1.length; _c++) {\n'
                               '\t\t\t\t\t\tvar side = sides_1[_c];\n'
                               '\t\t\t\t\t\tif (side.sideConditions[id]) {\n'
                               '\t\t\t\t\t\t\tvar layers = '
                               'side.sideConditions[id].layers || 1;\n'
                               '\t\t\t\t\t\t\tfor (; layers > 0; layers--)\n'
                               "\t\t\t\t\t\t\t\tthis.add('-sidestart', side, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t\t}\n'
                               '\t\t\t\t\t\telse {\n'
                               '\t\t\t\t\t\t\tdelete side.sideConditions[id];\n'
                               '\t\t\t\t\t\t}\n'
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tsuccess = true;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t}\n'
                               '\t\t\telse {\n'
                               '\t\t\t\tvar sourceSide = source.side;\n'
                               '\t\t\t\tvar targetSide = source.side.foe;\n'
                               '\t\t\t\tfor (var _d = 0, sideConditions_2 = '
                               'sideConditions; _d < sideConditions_2.length; '
                               '_d++) {\n'
                               '\t\t\t\t\tvar id = sideConditions_2[_d];\n'
                               '\t\t\t\t\tvar effectName = '
                               'this.dex.conditions.get(id).name;\n'
                               '\t\t\t\t\tif (sourceSide.sideConditions[id] && '
                               'targetSide.sideConditions[id]) {\n'
                               '\t\t\t\t\t\t_b = [\n'
                               '\t\t\t\t\t\t\ttargetSide.sideConditions[id], '
                               'sourceSide.sideConditions[id],\n'
                               '\t\t\t\t\t\t], sourceSide.sideConditions[id] = '
                               '_b[0], targetSide.sideConditions[id] = _b[1];\n'
                               "\t\t\t\t\t\tthis.add('-sideend', sourceSide, "
                               "effectName, '[silent]');\n"
                               "\t\t\t\t\t\tthis.add('-sideend', targetSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\telse if '
                               '(sourceSide.sideConditions[id] && '
                               '!targetSide.sideConditions[id]) {\n'
                               '\t\t\t\t\t\ttargetSide.sideConditions[id] = '
                               'sourceSide.sideConditions[id];\n'
                               '\t\t\t\t\t\tdelete '
                               'sourceSide.sideConditions[id];\n'
                               "\t\t\t\t\t\tthis.add('-sideend', sourceSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\telse if '
                               '(targetSide.sideConditions[id] && '
                               '!sourceSide.sideConditions[id]) {\n'
                               '\t\t\t\t\t\tsourceSide.sideConditions[id] = '
                               'targetSide.sideConditions[id];\n'
                               '\t\t\t\t\t\tdelete '
                               'targetSide.sideConditions[id];\n'
                               "\t\t\t\t\t\tthis.add('-sideend', targetSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\telse {\n'
                               '\t\t\t\t\t\tcontinue;\n'
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tvar sourceLayers = '
                               'sourceSide.sideConditions[id] ? '
                               '(sourceSide.sideConditions[id].layers || 1) : '
                               '0;\n'
                               '\t\t\t\t\tvar targetLayers = '
                               'targetSide.sideConditions[id] ? '
                               '(targetSide.sideConditions[id].layers || 1) : '
                               '0;\n'
                               '\t\t\t\t\tfor (; sourceLayers > 0; '
                               'sourceLayers--) {\n'
                               "\t\t\t\t\t\tthis.add('-sidestart', sourceSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tfor (; targetLayers > 0; '
                               'targetLayers--) {\n'
                               "\t\t\t\t\t\tthis.add('-sidestart', targetSide, "
                               "effectName, '[silent]');\n"
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tsuccess = true;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t}\n'
                               '\t\t\tif (!success)\n'
                               '\t\t\t\treturn false;\n'
                               "\t\t\tthis.add('-activate', source, 'move: "
                               "Court Change');\n"
                               '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'all',
                 'type': 'Normal'},
 'covet': {'accuracy': 100,
           'basePower': 60,
           'category': 'Physical',
           'contestType': 'Cute',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Covet',
           'num': 343,
           'onAfterHit': 'function (target, source, move) {\n'
                         "\t\t\tif (source.item || source.volatiles['gem']) {\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         '\t\t\tvar yourItem = target.takeItem(source);\n'
                         '\t\t\tif (!yourItem) {\n'
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tif (!this.singleEvent('TakeItem', yourItem, "
                         'target.itemState, source, target, move, yourItem) '
                         '||\n'
                         '\t\t\t\t!source.setItem(yourItem)) {\n'
                         '\t\t\t\ttarget.item = yourItem.id; // bypass setItem '
                         "so we don't break choicelock or anything\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tthis.add('-item', source, yourItem, '[from] "
                         "move: Covet', '[of] ' + target);\n"
                         '\t\t}',
           'pp': 25,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal'},
 'crabhammer': {'accuracy': 90,
                'basePower': 100,
                'category': 'Physical',
                'contestType': 'Tough',
                'critRatio': 2,
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Crabhammer',
                'num': 152,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Water'},
 'craftyshield': {'accuracy': True,
                  'basePower': 0,
                  'category': 'Status',
                  'condition': {'duration': 1,
                                'onSideStart': 'function (target, source) {\n'
                                               '\t\t\t\t'
                                               "this.add('-singleturn', "
                                               "source, 'Crafty Shield');\n"
                                               '\t\t\t}',
                                'onTryHit': 'function (target, source, move) '
                                            '{\n'
                                            "\t\t\t\tif (['self', "
                                            "'all'].includes(move.target) || "
                                            "move.category !== 'Status')\n"
                                            '\t\t\t\t\treturn;\n'
                                            "\t\t\t\tthis.add('-activate', "
                                            "target, 'move: Crafty Shield');\n"
                                            '\t\t\t\treturn this.NOT_FAIL;\n'
                                            '\t\t\t}',
                                'onTryHitPriority': 3},
                  'contestType': 'Clever',
                  'flags': {},
                  'name': 'Crafty Shield',
                  'num': 578,
                  'onTry': 'function () {\n'
                           '\t\t\treturn !!this.queue.willAct();\n'
                           '\t\t}',
                  'pp': 10,
                  'priority': 3,
                  'secondary': None,
                  'sideCondition': 'craftyshield',
                  'target': 'allySide',
                  'type': 'Fairy',
                  'zMove': {'boost': {'spd': 1}}},
 'crosschop': {'accuracy': 80,
               'basePower': 100,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Cross Chop',
               'num': 238,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fighting'},
 'crosspoison': {'accuracy': 100,
                 'basePower': 70,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'critRatio': 2,
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Cross Poison',
                 'num': 440,
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'chance': 10, 'status': 'psn'},
                 'target': 'normal',
                 'type': 'Poison'},
 'crunch': {'accuracy': 100,
            'basePower': 80,
            'category': 'Physical',
            'contestType': 'Tough',
            'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
            'name': 'Crunch',
            'num': 242,
            'pp': 15,
            'priority': 0,
            'secondary': {'boosts': {'def': -1}, 'chance': 20},
            'target': 'normal',
            'type': 'Dark'},
 'crushclaw': {'accuracy': 95,
               'basePower': 75,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Crush Claw',
               'num': 306,
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'def': -1}, 'chance': 50},
               'target': 'normal',
               'type': 'Normal'},
 'crushgrip': {'accuracy': 100,
               'basePower': 0,
               'basePowerCallback': 'function (pokemon, target) {\n'
                                    '\t\t\treturn Math.floor(Math.floor((120 * '
                                    '(100 * Math.floor(target.hp * 4096 / '
                                    'target.maxhp)) + 2048 - 1) / 4096) / 100) '
                                    '|| 1;\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 140},
               'name': 'Crush Grip',
               'num': 462,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'basePower': 190}},
 'curse': {'accuracy': True,
           'basePower': 0,
           'category': 'Status',
           'condition': {'onResidual': 'function (pokemon) {\n'
                                       '\t\t\t\tthis.damage(pokemon.baseMaxhp '
                                       '/ 4);\n'
                                       '\t\t\t}',
                         'onResidualOrder': 12,
                         'onStart': 'function (pokemon, source) {\n'
                                    "\t\t\t\tthis.add('-start', pokemon, "
                                    "'Curse', '[of] ' + source);\n"
                                    '\t\t\t}'},
           'contestType': 'Tough',
           'flags': {'authentic': 1},
           'name': 'Curse',
           'nonGhostTarget': 'self',
           'num': 174,
           'onHit': 'function (target, source) {\n'
                    '\t\t\tthis.directDamage(source.maxhp / 2, source, '
                    'source);\n'
                    '\t\t}',
           'onModifyMove': 'function (move, source, target) {\n'
                           "\t\t\tif (!source.hasType('Ghost')) {\n"
                           '\t\t\t\tmove.target = move.nonGhostTarget;\n'
                           '\t\t\t}\n'
                           '\t\t}',
           'onTryHit': 'function (target, source, move) {\n'
                       "\t\t\tif (!source.hasType('Ghost')) {\n"
                       '\t\t\t\tdelete move.volatileStatus;\n'
                       '\t\t\t\tdelete move.onHit;\n'
                       '\t\t\t\tmove.self = { boosts: { spe: -1, atk: 1, def: '
                       '1 } };\n'
                       '\t\t\t}\n'
                       '\t\t\telse if (move.volatileStatus && '
                       "target.volatiles['curse']) {\n"
                       '\t\t\t\treturn false;\n'
                       '\t\t\t}\n'
                       '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'randomNormal',
           'type': 'Ghost',
           'volatileStatus': 'curse',
           'zMove': {'effect': 'curse'}},
 'cut': {'accuracy': 95,
         'basePower': 50,
         'category': 'Physical',
         'contestType': 'Cool',
         'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
         'name': 'Cut',
         'num': 15,
         'pp': 30,
         'priority': 0,
         'secondary': None,
         'target': 'normal',
         'type': 'Normal'},
 'darkestlariat': {'accuracy': 100,
                   'basePower': 85,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                   'ignoreDefensive': True,
                   'ignoreEvasion': True,
                   'name': 'Darkest Lariat',
                   'num': 663,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Dark'},
 'darkpulse': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'distance': 1, 'mirror': 1, 'protect': 1, 'pulse': 1},
               'name': 'Dark Pulse',
               'num': 399,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
               'target': 'any',
               'type': 'Dark'},
 'darkvoid': {'accuracy': 50,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Clever',
              'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
              'isNonstandard': 'Past',
              'name': 'Dark Void',
              'num': 464,
              'onTry': 'function (source, target, move) {\n'
                       "\t\t\tif (source.species.name === 'Darkrai' || "
                       'move.hasBounced) {\n'
                       '\t\t\t\treturn;\n'
                       '\t\t\t}\n'
                       "\t\t\tthis.add('-fail', source, 'move: Dark Void');\n"
                       '\t\t\tthis.hint("Only a Pokemon whose form is Darkrai '
                       'can use this move.");\n'
                       '\t\t\treturn null;\n'
                       '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'status': 'slp',
              'target': 'allAdjacentFoes',
              'type': 'Dark',
              'zMove': {'effect': 'clearnegativeboost'}},
 'dazzlinggleam': {'accuracy': 100,
                   'basePower': 80,
                   'category': 'Special',
                   'contestType': 'Beautiful',
                   'flags': {'mirror': 1, 'protect': 1},
                   'name': 'Dazzling Gleam',
                   'num': 605,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'allAdjacentFoes',
                   'type': 'Fairy'},
 'decorate': {'accuracy': True,
              'basePower': 0,
              'boosts': {'atk': 2, 'spa': 2},
              'category': 'Status',
              'flags': {'mystery': 1},
              'name': 'Decorate',
              'num': 777,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Fairy'},
 'defendorder': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'def': 1, 'spd': 1},
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'snatch': 1},
                 'name': 'Defend Order',
                 'num': 455,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Bug',
                 'zMove': {'boost': {'def': 1}}},
 'defensecurl': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'def': 1},
                 'category': 'Status',
                 'condition': {'noCopy': True},
                 'contestType': 'Cute',
                 'flags': {'snatch': 1},
                 'name': 'Defense Curl',
                 'num': 111,
                 'pp': 40,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Normal',
                 'volatileStatus': 'defensecurl',
                 'zMove': {'boost': {'accuracy': 1}}},
 'defog': {'accuracy': True,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Cool',
           'flags': {'authentic': 1,
                     'mirror': 1,
                     'protect': 1,
                     'reflectable': 1},
           'name': 'Defog',
           'num': 432,
           'onHit': 'function (target, source, move) {\n'
                    '\t\t\tvar success = false;\n'
                    "\t\t\tif (!target.volatiles['substitute'] || "
                    'move.infiltrates)\n'
                    '\t\t\t\tsuccess = !!this.boost({ evasion: -1 });\n'
                    '\t\t\tvar removeTarget = [\n'
                    "\t\t\t\t'reflect', 'lightscreen', 'auroraveil', "
                    "'safeguard', 'mist', 'spikes', 'toxicspikes', "
                    "'stealthrock', 'stickyweb', 'gmaxsteelsurge',\n"
                    '\t\t\t];\n'
                    '\t\t\tvar removeAll = [\n'
                    "\t\t\t\t'spikes', 'toxicspikes', 'stealthrock', "
                    "'stickyweb', 'gmaxsteelsurge',\n"
                    '\t\t\t];\n'
                    '\t\t\tfor (var _i = 0, removeTarget_1 = removeTarget; _i '
                    '< removeTarget_1.length; _i++) {\n'
                    '\t\t\t\tvar targetCondition = removeTarget_1[_i];\n'
                    '\t\t\t\tif '
                    '(target.side.removeSideCondition(targetCondition)) {\n'
                    '\t\t\t\t\tif (!removeAll.includes(targetCondition))\n'
                    '\t\t\t\t\t\tcontinue;\n'
                    "\t\t\t\t\tthis.add('-sideend', target.side, "
                    "this.dex.conditions.get(targetCondition).name, '[from] "
                    "move: Defog', '[of] ' + source);\n"
                    '\t\t\t\t\tsuccess = true;\n'
                    '\t\t\t\t}\n'
                    '\t\t\t}\n'
                    '\t\t\tfor (var _a = 0, removeAll_1 = removeAll; _a < '
                    'removeAll_1.length; _a++) {\n'
                    '\t\t\t\tvar sideCondition = removeAll_1[_a];\n'
                    '\t\t\t\tif '
                    '(source.side.removeSideCondition(sideCondition)) {\n'
                    "\t\t\t\t\tthis.add('-sideend', source.side, "
                    "this.dex.conditions.get(sideCondition).name, '[from] "
                    "move: Defog', '[of] ' + source);\n"
                    '\t\t\t\t\tsuccess = true;\n'
                    '\t\t\t\t}\n'
                    '\t\t\t}\n'
                    '\t\t\tthis.field.clearTerrain();\n'
                    '\t\t\treturn success;\n'
                    '\t\t}',
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Flying',
           'zMove': {'boost': {'accuracy': 1}}},
 'destinybond': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'onBeforeMove': 'function (pokemon, target, '
                                               'move) {\n'
                                               '\t\t\t\tif (move.id === '
                                               "'destinybond')\n"
                                               '\t\t\t\t\treturn;\n'
                                               "\t\t\t\tthis.debug('removing "
                                               "Destiny Bond before attack');\n"
                                               '\t\t\t\t'
                                               "pokemon.removeVolatile('destinybond');\n"
                                               '\t\t\t}',
                               'onBeforeMovePriority': -1,
                               'onFaint': 'function (target, source, effect) '
                                          '{\n'
                                          '\t\t\t\tif (!source || !effect || '
                                          'target.isAlly(source))\n'
                                          '\t\t\t\t\treturn;\n'
                                          '\t\t\t\tif (effect.effectType === '
                                          "'Move' && !effect.isFutureMove) {\n"
                                          '\t\t\t\t\tif '
                                          "(source.volatiles['dynamax']) {\n"
                                          "\t\t\t\t\t\tthis.add('-hint', "
                                          '"Dynamaxed Pokemon are immune to '
                                          'Destiny Bond.");\n'
                                          '\t\t\t\t\t\treturn;\n'
                                          '\t\t\t\t\t}\n'
                                          "\t\t\t\t\tthis.add('-activate', "
                                          "target, 'move: Destiny Bond');\n"
                                          '\t\t\t\t\tsource.faint();\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t}',
                               'onMoveAborted': 'function (pokemon, target, '
                                                'move) {\n'
                                                '\t\t\t\t'
                                                "pokemon.removeVolatile('destinybond');\n"
                                                '\t\t\t}',
                               'onStart': 'function (pokemon) {\n'
                                          "\t\t\t\tthis.add('-singlemove', "
                                          "pokemon, 'Destiny Bond');\n"
                                          '\t\t\t}'},
                 'contestType': 'Clever',
                 'flags': {'authentic': 1},
                 'name': 'Destiny Bond',
                 'num': 194,
                 'onPrepareHit': 'function (pokemon) {\n'
                                 '\t\t\treturn '
                                 "!pokemon.removeVolatile('destinybond');\n"
                                 '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Ghost',
                 'volatileStatus': 'destinybond',
                 'zMove': {'effect': 'redirect'}},
 'detect': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Cool',
            'flags': {},
            'name': 'Detect',
            'num': 197,
            'onHit': 'function (pokemon) {\n'
                     "\t\t\tpokemon.addVolatile('stall');\n"
                     '\t\t}',
            'onPrepareHit': 'function (pokemon) {\n'
                            '\t\t\treturn !!this.queue.willAct() && '
                            "this.runEvent('StallMove', pokemon);\n"
                            '\t\t}',
            'pp': 5,
            'priority': 4,
            'secondary': None,
            'stallingMove': True,
            'target': 'self',
            'type': 'Fighting',
            'volatileStatus': 'protect',
            'zMove': {'boost': {'evasion': 1}}},
 'devastatingdrake': {'accuracy': True,
                      'basePower': 1,
                      'category': 'Physical',
                      'contestType': 'Cool',
                      'flags': {},
                      'isNonstandard': 'Past',
                      'isZ': 'dragoniumz',
                      'name': 'Devastating Drake',
                      'num': 652,
                      'pp': 1,
                      'priority': 0,
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Dragon'},
 'diamondstorm': {'accuracy': 95,
                  'basePower': 100,
                  'category': 'Physical',
                  'contestType': 'Beautiful',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Diamond Storm',
                  'num': 591,
                  'pp': 5,
                  'priority': 0,
                  'secondary': {},
                  'self': {'boosts': {'def': 2}, 'chance': 50},
                  'target': 'allAdjacentFoes',
                  'type': 'Rock'},
 'dig': {'accuracy': 100,
         'basePower': 80,
         'category': 'Physical',
         'condition': {'duration': 2,
                       'onImmunity': 'function (type, pokemon) {\n'
                                     "\t\t\t\tif (type === 'sandstorm' || type "
                                     "=== 'hail')\n"
                                     '\t\t\t\t\treturn false;\n'
                                     '\t\t\t}',
                       'onInvulnerability': 'function (target, source, move) '
                                            '{\n'
                                            "\t\t\t\tif (['earthquake', "
                                            "'magnitude'].includes(move.id)) "
                                            '{\n'
                                            '\t\t\t\t\treturn;\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t\treturn false;\n'
                                            '\t\t\t}',
                       'onSourceModifyDamage': 'function (damage, source, '
                                               'target, move) {\n'
                                               '\t\t\t\tif (move.id === '
                                               "'earthquake' || move.id === "
                                               "'magnitude') {\n"
                                               '\t\t\t\t\treturn '
                                               'this.chainModify(2);\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}'},
         'contestType': 'Tough',
         'flags': {'charge': 1,
                   'contact': 1,
                   'mirror': 1,
                   'nonsky': 1,
                   'protect': 1},
         'name': 'Dig',
         'num': 91,
         'onTryMove': 'function (attacker, defender, move) {\n'
                      '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                      '\t\t\t\treturn;\n'
                      '\t\t\t}\n'
                      "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                      "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                      'defender, move)) {\n'
                      '\t\t\t\treturn;\n'
                      '\t\t\t}\n'
                      "\t\t\tattacker.addVolatile('twoturnmove', defender);\n"
                      '\t\t\treturn null;\n'
                      '\t\t}',
         'pp': 10,
         'priority': 0,
         'secondary': None,
         'target': 'normal',
         'type': 'Ground'},
 'disable': {'accuracy': 100,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 5,
                           'noCopy': True,
                           'onBeforeMove': 'function (attacker, defender, '
                                           'move) {\n'
                                           '\t\t\t\tif (!move.isZ && move.id '
                                           '=== this.effectState.move) {\n'
                                           "\t\t\t\t\tthis.add('cant', "
                                           "attacker, 'Disable', move);\n"
                                           '\t\t\t\t\treturn false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                           'onBeforeMovePriority': 7,
                           'onDisableMove': 'function (pokemon) {\n'
                                            '\t\t\t\tfor (var _i = 0, _a = '
                                            'pokemon.moveSlots; _i < '
                                            '_a.length; _i++) {\n'
                                            '\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                            '\t\t\t\t\tif (moveSlot.id === '
                                            'this.effectState.move) {\n'
                                            '\t\t\t\t\t\t'
                                            'pokemon.disableMove(moveSlot.id);\n'
                                            '\t\t\t\t\t}\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}',
                           'onEnd': 'function (pokemon) {\n'
                                    "\t\t\t\tthis.add('-end', pokemon, "
                                    "'Disable');\n"
                                    '\t\t\t}',
                           'onResidualOrder': 17,
                           'onStart': 'function (pokemon, source, effect) {\n'
                                      "\t\t\t\t// The target hasn't taken its "
                                      'turn, or Cursed Body activated and the '
                                      'move was not used through Dancer or '
                                      'Instruct\n'
                                      '\t\t\t\tif '
                                      '(this.queue.willMove(pokemon) ||\n'
                                      '\t\t\t\t\t(pokemon === '
                                      'this.activePokemon && this.activeMove '
                                      '&& !this.activeMove.isExternal)) {\n'
                                      '\t\t\t\t\tthis.effectState.duration--;\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\tif (!pokemon.lastMove) {\n'
                                      '\t\t\t\t\tthis.debug("Pokemon hasn\'t '
                                      'moved yet");\n'
                                      '\t\t\t\t\treturn false;\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\tfor (var _i = 0, _a = '
                                      'pokemon.moveSlots; _i < _a.length; '
                                      '_i++) {\n'
                                      '\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                      '\t\t\t\t\tif (moveSlot.id === '
                                      'pokemon.lastMove.id) {\n'
                                      '\t\t\t\t\t\tif (!moveSlot.pp) {\n'
                                      "\t\t\t\t\t\t\tthis.debug('Move out of "
                                      "PP');\n"
                                      '\t\t\t\t\t\t\treturn false;\n'
                                      '\t\t\t\t\t\t}\n'
                                      '\t\t\t\t\t}\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\tif (effect.effectType === '
                                      "'Ability') {\n"
                                      "\t\t\t\t\tthis.add('-start', pokemon, "
                                      "'Disable', pokemon.lastMove.name, "
                                      "'[from] ability: Cursed Body', '[of] ' "
                                      '+ source);\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\telse {\n'
                                      "\t\t\t\t\tthis.add('-start', pokemon, "
                                      "'Disable', pokemon.lastMove.name);\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t\tthis.effectState.move = '
                                      'pokemon.lastMove.id;\n'
                                      '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'authentic': 1,
                       'mirror': 1,
                       'protect': 1,
                       'reflectable': 1},
             'name': 'Disable',
             'num': 50,
             'onTryHit': 'function (target) {\n'
                         '\t\t\tif (!target.lastMove || target.lastMove.isZ || '
                         'target.lastMove.isMax || target.lastMove.id === '
                         "'struggle') {\n"
                         '\t\t\t\treturn false;\n'
                         '\t\t\t}\n'
                         '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'volatileStatus': 'disable',
             'zMove': {'effect': 'clearnegativeboost'}},
 'disarmingvoice': {'accuracy': True,
                    'basePower': 40,
                    'category': 'Special',
                    'contestType': 'Cute',
                    'flags': {'authentic': 1,
                              'mirror': 1,
                              'protect': 1,
                              'sound': 1},
                    'name': 'Disarming Voice',
                    'num': 574,
                    'pp': 15,
                    'priority': 0,
                    'secondary': None,
                    'target': 'allAdjacentFoes',
                    'type': 'Fairy'},
 'discharge': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Discharge',
               'num': 435,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 30, 'status': 'par'},
               'target': 'allAdjacent',
               'type': 'Electric'},
 'dive': {'accuracy': 100,
          'basePower': 80,
          'category': 'Physical',
          'condition': {'duration': 2,
                        'onImmunity': 'function (type, pokemon) {\n'
                                      "\t\t\t\tif (type === 'sandstorm' || "
                                      "type === 'hail')\n"
                                      '\t\t\t\t\treturn false;\n'
                                      '\t\t\t}',
                        'onInvulnerability': 'function (target, source, move) '
                                             '{\n'
                                             "\t\t\t\tif (['surf', "
                                             "'whirlpool'].includes(move.id)) "
                                             '{\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\treturn false;\n'
                                             '\t\t\t}',
                        'onSourceModifyDamage': 'function (damage, source, '
                                                'target, move) {\n'
                                                '\t\t\t\tif (move.id === '
                                                "'surf' || move.id === "
                                                "'whirlpool') {\n"
                                                '\t\t\t\t\treturn '
                                                'this.chainModify(2);\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t}'},
          'contestType': 'Beautiful',
          'flags': {'charge': 1,
                    'contact': 1,
                    'mirror': 1,
                    'nonsky': 1,
                    'protect': 1},
          'name': 'Dive',
          'num': 291,
          'onTryMove': 'function (attacker, defender, move) {\n'
                       '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                       '\t\t\t\treturn;\n'
                       '\t\t\t}\n'
                       "\t\t\tif (attacker.hasAbility('gulpmissile') && "
                       "attacker.species.name === 'Cramorant' && "
                       '!attacker.transformed) {\n'
                       '\t\t\t\tvar forme = attacker.hp <= attacker.maxhp / 2 '
                       "? 'cramorantgorging' : 'cramorantgulping';\n"
                       '\t\t\t\tattacker.formeChange(forme, move);\n'
                       '\t\t\t}\n'
                       "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                       "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                       'defender, move)) {\n'
                       '\t\t\t\treturn;\n'
                       '\t\t\t}\n'
                       "\t\t\tattacker.addVolatile('twoturnmove', defender);\n"
                       '\t\t\treturn null;\n'
                       '\t\t}',
          'pp': 10,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Water'},
 'dizzypunch': {'accuracy': 100,
                'basePower': 70,
                'category': 'Physical',
                'contestType': 'Cute',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                'isNonstandard': 'Past',
                'name': 'Dizzy Punch',
                'num': 146,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 20, 'volatileStatus': 'confusion'},
                'target': 'normal',
                'type': 'Normal'},
 'doomdesire': {'accuracy': 100,
                'basePower': 140,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {},
                'isFutureMove': True,
                'name': 'Doom Desire',
                'num': 353,
                'onTry': 'function (source, target) {\n'
                         '\t\t\tif (!target.side.addSlotCondition(target, '
                         "'futuremove'))\n"
                         '\t\t\t\treturn false;\n'
                         '\t\t\t'
                         "Object.assign(target.side.slotConditions[target.position]['futuremove'], "
                         '{\n'
                         "\t\t\t\tmove: 'doomdesire',\n"
                         '\t\t\t\tsource: source,\n'
                         '\t\t\t\tmoveData: {\n'
                         "\t\t\t\t\tid: 'doomdesire',\n"
                         '\t\t\t\t\tname: "Doom Desire",\n'
                         '\t\t\t\t\taccuracy: 100,\n'
                         '\t\t\t\t\tbasePower: 140,\n'
                         '\t\t\t\t\tcategory: "Special",\n'
                         '\t\t\t\t\tpriority: 0,\n'
                         '\t\t\t\t\tflags: {},\n'
                         "\t\t\t\t\teffectType: 'Move',\n"
                         '\t\t\t\t\tisFutureMove: true,\n'
                         "\t\t\t\t\ttype: 'Steel',\n"
                         '\t\t\t\t},\n'
                         '\t\t\t});\n'
                         "\t\t\tthis.add('-start', source, 'Doom Desire');\n"
                         '\t\t\treturn this.NOT_FAIL;\n'
                         '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Steel'},
 'doubleedge': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Double-Edge',
                'num': 38,
                'pp': 15,
                'priority': 0,
                'recoil': [33, 100],
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'doublehit': {'accuracy': 90,
               'basePower': 35,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 120},
               'multihit': 2,
               'name': 'Double Hit',
               'num': 458,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'basePower': 140}},
 'doubleironbash': {'accuracy': 100,
                    'basePower': 60,
                    'category': 'Physical',
                    'contestType': 'Clever',
                    'flags': {'contact': 1,
                              'mirror': 1,
                              'protect': 1,
                              'punch': 1},
                    'maxMove': {'basePower': 140},
                    'multihit': 2,
                    'name': 'Double Iron Bash',
                    'num': 742,
                    'pp': 5,
                    'priority': 0,
                    'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                    'target': 'normal',
                    'type': 'Steel',
                    'zMove': {'basePower': 180}},
 'doublekick': {'accuracy': 100,
                'basePower': 30,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 80},
                'multihit': 2,
                'name': 'Double Kick',
                'num': 24,
                'pp': 30,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'doubleslap': {'accuracy': 85,
                'basePower': 15,
                'category': 'Physical',
                'contestType': 'Cute',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'multihit': [2, 5],
                'name': 'Double Slap',
                'num': 3,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'doubleteam': {'accuracy': True,
                'basePower': 0,
                'boosts': {'evasion': 1},
                'category': 'Status',
                'contestType': 'Cool',
                'flags': {'snatch': 1},
                'name': 'Double Team',
                'num': 104,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'effect': 'clearnegativeboost'}},
 'dracometeor': {'accuracy': 90,
                 'basePower': 130,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Draco Meteor',
                 'num': 434,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'boosts': {'spa': -2}},
                 'target': 'normal',
                 'type': 'Dragon'},
 'dragonascent': {'accuracy': 100,
                  'basePower': 120,
                  'category': 'Physical',
                  'contestType': 'Beautiful',
                  'flags': {'contact': 1,
                            'distance': 1,
                            'mirror': 1,
                            'protect': 1},
                  'name': 'Dragon Ascent',
                  'num': 620,
                  'pp': 5,
                  'priority': 0,
                  'self': {'boosts': {'def': -1, 'spd': -1}},
                  'target': 'any',
                  'type': 'Flying'},
 'dragonbreath': {'accuracy': 100,
                  'basePower': 60,
                  'category': 'Special',
                  'contestType': 'Cool',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Dragon Breath',
                  'num': 225,
                  'pp': 20,
                  'priority': 0,
                  'secondary': {'chance': 30, 'status': 'par'},
                  'target': 'normal',
                  'type': 'Dragon'},
 'dragonclaw': {'accuracy': 100,
                'basePower': 80,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Dragon Claw',
                'num': 337,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dragon'},
 'dragondance': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'atk': 1, 'spe': 1},
                 'category': 'Status',
                 'contestType': 'Cool',
                 'flags': {'dance': 1, 'snatch': 1},
                 'name': 'Dragon Dance',
                 'num': 349,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Dragon',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'dragondarts': {'accuracy': 100,
                 'basePower': 50,
                 'category': 'Physical',
                 'flags': {'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 130},
                 'multihit': 2,
                 'name': 'Dragon Darts',
                 'num': 751,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'smartTarget': True,
                 'target': 'normal',
                 'type': 'Dragon'},
 'dragonenergy': {'accuracy': 100,
                  'basePower': 150,
                  'basePowerCallback': 'function (pokemon, target, move) {\n'
                                       '\t\t\treturn move.basePower * '
                                       'pokemon.hp / pokemon.maxhp;\n'
                                       '\t\t}',
                  'category': 'Special',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Dragon Energy',
                  'num': 820,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allAdjacentFoes',
                  'type': 'Dragon'},
 'dragonhammer': {'accuracy': 100,
                  'basePower': 90,
                  'category': 'Physical',
                  'contestType': 'Tough',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Dragon Hammer',
                  'num': 692,
                  'pp': 15,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Dragon'},
 'dragonpulse': {'accuracy': 100,
                 'basePower': 85,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'distance': 1,
                           'mirror': 1,
                           'protect': 1,
                           'pulse': 1},
                 'name': 'Dragon Pulse',
                 'num': 406,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'any',
                 'type': 'Dragon'},
 'dragonrage': {'accuracy': 100,
                'basePower': 0,
                'category': 'Special',
                'contestType': 'Cool',
                'damage': 40,
                'flags': {'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Dragon Rage',
                'num': 82,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dragon'},
 'dragonrush': {'accuracy': 75,
                'basePower': 100,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Dragon Rush',
                'num': 407,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
                'target': 'normal',
                'type': 'Dragon'},
 'dragontail': {'accuracy': 90,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'forceSwitch': True,
                'name': 'Dragon Tail',
                'num': 525,
                'pp': 10,
                'priority': -6,
                'target': 'normal',
                'type': 'Dragon'},
 'drainingkiss': {'accuracy': 100,
                  'basePower': 50,
                  'category': 'Special',
                  'contestType': 'Cute',
                  'drain': [3, 4],
                  'flags': {'contact': 1, 'heal': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Draining Kiss',
                  'num': 577,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Fairy'},
 'drainpunch': {'accuracy': 100,
                'basePower': 75,
                'category': 'Physical',
                'contestType': 'Tough',
                'drain': [1, 2],
                'flags': {'contact': 1,
                          'heal': 1,
                          'mirror': 1,
                          'protect': 1,
                          'punch': 1},
                'name': 'Drain Punch',
                'num': 409,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'dreameater': {'accuracy': 100,
                'basePower': 100,
                'category': 'Special',
                'contestType': 'Clever',
                'drain': [1, 2],
                'flags': {'heal': 1, 'mirror': 1, 'protect': 1},
                'name': 'Dream Eater',
                'num': 138,
                'onTryImmunity': 'function (target) {\n'
                                 "\t\t\treturn target.status === 'slp' || "
                                 "target.hasAbility('comatose');\n"
                                 '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Psychic'},
 'drillpeck': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1,
                         'distance': 1,
                         'mirror': 1,
                         'protect': 1},
               'name': 'Drill Peck',
               'num': 65,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'any',
               'type': 'Flying'},
 'drillrun': {'accuracy': 95,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Tough',
              'critRatio': 2,
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Drill Run',
              'num': 529,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Ground'},
 'drumbeating': {'accuracy': 100,
                 'basePower': 80,
                 'category': 'Physical',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Drum Beating',
                 'num': 778,
                 'pp': 10,
                 'priority': 0,
                 'secondary': {'boosts': {'spe': -1}, 'chance': 100},
                 'target': 'normal',
                 'type': 'Grass'},
 'dualchop': {'accuracy': 90,
              'basePower': 40,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'maxMove': {'basePower': 130},
              'multihit': 2,
              'name': 'Dual Chop',
              'num': 530,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Dragon'},
 'dualwingbeat': {'accuracy': 90,
                  'basePower': 40,
                  'category': 'Physical',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'maxMove': {'basePower': 130},
                  'multihit': 2,
                  'name': 'Dual Wingbeat',
                  'num': 814,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Flying'},
 'dynamaxcannon': {'accuracy': 100,
                   'basePower': 100,
                   'category': 'Special',
                   'flags': {'protect': 1},
                   'name': 'Dynamax Cannon',
                   'num': 744,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Dragon'},
 'dynamicpunch': {'accuracy': 50,
                  'basePower': 100,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {'contact': 1,
                            'mirror': 1,
                            'protect': 1,
                            'punch': 1},
                  'name': 'Dynamic Punch',
                  'num': 223,
                  'pp': 5,
                  'priority': 0,
                  'secondary': {'chance': 100, 'volatileStatus': 'confusion'},
                  'target': 'normal',
                  'type': 'Fighting'},
 'earthpower': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                'name': 'Earth Power',
                'num': 414,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'spd': -1}, 'chance': 10},
                'target': 'normal',
                'type': 'Ground'},
 'earthquake': {'accuracy': 100,
                'basePower': 100,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                'name': 'Earthquake',
                'num': 89,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacent',
                'type': 'Ground'},
 'echoedvoice': {'accuracy': 100,
                 'basePower': 40,
                 'basePowerCallback': 'function () {\n'
                                      '\t\t\tif '
                                      '(this.field.pseudoWeather.echoedvoice) '
                                      '{\n'
                                      '\t\t\t\treturn 40 * '
                                      'this.field.pseudoWeather.echoedvoice.multiplier;\n'
                                      '\t\t\t}\n'
                                      '\t\t\treturn 40;\n'
                                      '\t\t}',
                 'category': 'Special',
                 'condition': {'duration': 2,
                               'onFieldRestart': 'function () {\n'
                                                 '\t\t\t\tif '
                                                 '(this.effectState.duration '
                                                 '!== 2) {\n'
                                                 '\t\t\t\t\t'
                                                 'this.effectState.duration = '
                                                 '2;\n'
                                                 '\t\t\t\t\tif '
                                                 '(this.effectState.multiplier '
                                                 '< 5) {\n'
                                                 '\t\t\t\t\t\t'
                                                 'this.effectState.multiplier++;\n'
                                                 '\t\t\t\t\t}\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t}',
                               'onFieldStart': 'function () {\n'
                                               '\t\t\t\t'
                                               'this.effectState.multiplier = '
                                               '1;\n'
                                               '\t\t\t}'},
                 'contestType': 'Beautiful',
                 'flags': {'authentic': 1,
                           'mirror': 1,
                           'protect': 1,
                           'sound': 1},
                 'name': 'Echoed Voice',
                 'num': 497,
                 'onTry': 'function () {\n'
                          "\t\t\tthis.field.addPseudoWeather('echoedvoice');\n"
                          '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'eerieimpulse': {'accuracy': 100,
                  'basePower': 0,
                  'boosts': {'spa': -2},
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                  'name': 'Eerie Impulse',
                  'num': 598,
                  'pp': 15,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Electric',
                  'zMove': {'boost': {'spd': 1}}},
 'eeriespell': {'accuracy': 100,
                'basePower': 80,
                'category': 'Special',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'protect': 1,
                          'sound': 1},
                'name': 'Eerie Spell',
                'num': 826,
                'pp': 5,
                'priority': 0,
                'secondary': {'chance': 100,
                              'onHit': 'function (target) {\n'
                                       '\t\t\t\tif (!target.hp)\n'
                                       '\t\t\t\t\treturn;\n'
                                       '\t\t\t\tvar move = target.lastMove;\n'
                                       '\t\t\t\tif (!move || move.isZ)\n'
                                       '\t\t\t\t\treturn;\n'
                                       '\t\t\t\tif (move.isMax && '
                                       'move.baseMove)\n'
                                       '\t\t\t\t\tmove = '
                                       'this.dex.moves.get(move.baseMove);\n'
                                       '\t\t\t\tvar ppDeducted = '
                                       'target.deductPP(move.id, 3);\n'
                                       '\t\t\t\tif (!ppDeducted)\n'
                                       '\t\t\t\t\treturn;\n'
                                       "\t\t\t\tthis.add('-activate', target, "
                                       "'move: Eerie Spell', move.name, "
                                       'ppDeducted);\n'
                                       '\t\t\t}'},
                'target': 'normal',
                'type': 'Psychic'},
 'eggbomb': {'accuracy': 75,
             'basePower': 100,
             'category': 'Physical',
             'contestType': 'Cute',
             'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Egg Bomb',
             'num': 121,
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal'},
 'electricterrain': {'accuracy': True,
                     'basePower': 0,
                     'category': 'Status',
                     'condition': {'duration': 5,
                                   'durationCallback': 'function (source, '
                                                       'effect) {\n'
                                                       '\t\t\t\tif (source === '
                                                       'null || source === '
                                                       'void 0 ? void 0 : '
                                                       "source.hasItem('terrainextender')) "
                                                       '{\n'
                                                       '\t\t\t\t\treturn 8;\n'
                                                       '\t\t\t\t}\n'
                                                       '\t\t\t\treturn 5;\n'
                                                       '\t\t\t}',
                                   'onBasePower': 'function (basePower, '
                                                  'attacker, defender, move) '
                                                  '{\n'
                                                  '\t\t\t\tif (move.type === '
                                                  "'Electric' && "
                                                  'attacker.isGrounded() && '
                                                  '!attacker.isSemiInvulnerable()) '
                                                  '{\n'
                                                  '\t\t\t\t\t'
                                                  "this.debug('electric "
                                                  "terrain boost');\n"
                                                  '\t\t\t\t\treturn '
                                                  'this.chainModify([5325, '
                                                  '4096]);\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t}',
                                   'onBasePowerPriority': 6,
                                   'onFieldEnd': 'function () {\n'
                                                 '\t\t\t\t'
                                                 "this.add('-fieldend', 'move: "
                                                 "Electric Terrain');\n"
                                                 '\t\t\t}',
                                   'onFieldResidualOrder': 27,
                                   'onFieldResidualSubOrder': 7,
                                   'onFieldStart': 'function (field, source, '
                                                   'effect) {\n'
                                                   '\t\t\t\tif ((effect === '
                                                   'null || effect === void 0 '
                                                   '? void 0 : '
                                                   'effect.effectType) === '
                                                   "'Ability') {\n"
                                                   '\t\t\t\t\t'
                                                   "this.add('-fieldstart', "
                                                   "'move: Electric Terrain', "
                                                   "'[from] ability: ' + "
                                                   "effect, '[of] ' + "
                                                   'source);\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t\telse {\n'
                                                   '\t\t\t\t\t'
                                                   "this.add('-fieldstart', "
                                                   "'move: Electric "
                                                   "Terrain');\n"
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t}',
                                   'onSetStatus': 'function (status, target, '
                                                  'source, effect) {\n'
                                                  '\t\t\t\tif (status.id === '
                                                  "'slp' && "
                                                  'target.isGrounded() && '
                                                  '!target.isSemiInvulnerable()) '
                                                  '{\n'
                                                  '\t\t\t\t\tif (effect.id === '
                                                  "'yawn' || "
                                                  '(effect.effectType === '
                                                  "'Move' && "
                                                  '!effect.secondaries)) {\n'
                                                  '\t\t\t\t\t\t'
                                                  "this.add('-activate', "
                                                  "target, 'move: Electric "
                                                  "Terrain');\n"
                                                  '\t\t\t\t\t}\n'
                                                  '\t\t\t\t\treturn false;\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t}',
                                   'onTryAddVolatile': 'function (status, '
                                                       'target) {\n'
                                                       '\t\t\t\tif '
                                                       '(!target.isGrounded() '
                                                       '|| '
                                                       'target.isSemiInvulnerable())\n'
                                                       '\t\t\t\t\treturn;\n'
                                                       '\t\t\t\tif (status.id '
                                                       "=== 'yawn') {\n"
                                                       '\t\t\t\t\t'
                                                       "this.add('-activate', "
                                                       "target, 'move: "
                                                       "Electric Terrain');\n"
                                                       '\t\t\t\t\treturn '
                                                       'null;\n'
                                                       '\t\t\t\t}\n'
                                                       '\t\t\t}'},
                     'contestType': 'Clever',
                     'flags': {'nonsky': 1},
                     'name': 'Electric Terrain',
                     'num': 604,
                     'pp': 10,
                     'priority': 0,
                     'secondary': None,
                     'target': 'all',
                     'terrain': 'electricterrain',
                     'type': 'Electric',
                     'zMove': {'boost': {'spe': 1}}},
 'electrify': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 1,
                             'onModifyType': 'function (move) {\n'
                                             '\t\t\t\tif (move.id !== '
                                             "'struggle') {\n"
                                             "\t\t\t\t\tthis.debug('Electrify "
                                             "making move type electric');\n"
                                             '\t\t\t\t\tmove.type = '
                                             "'Electric';\n"
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                             'onModifyTypePriority': -2,
                             'onStart': 'function (target) {\n'
                                        "\t\t\t\tthis.add('-singleturn', "
                                        "target, 'move: Electrify');\n"
                                        '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
               'name': 'Electrify',
               'num': 582,
               'onTryHit': 'function (target) {\n'
                           '\t\t\tif (!this.queue.willMove(target) && '
                           'target.activeTurns)\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Electric',
               'volatileStatus': 'electrify',
               'zMove': {'boost': {'spa': 1}}},
 'electroball': {'accuracy': 100,
                 'basePower': 0,
                 'basePowerCallback': 'function (pokemon, target) {\n'
                                      '\t\t\tvar ratio = '
                                      "Math.floor(pokemon.getStat('spe') / "
                                      "target.getStat('spe'));\n"
                                      '\t\t\tif (!isFinite(ratio))\n'
                                      '\t\t\t\tratio = 0;\n'
                                      '\t\t\tvar bp = [40, 60, 80, 120, '
                                      '150][Math.min(ratio, 4)];\n'
                                      '\t\t\tthis.debug(bp + " bp");\n'
                                      '\t\t\treturn bp;\n'
                                      '\t\t}',
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 130},
                 'name': 'Electro Ball',
                 'num': 486,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Electric',
                 'zMove': {'basePower': 160}},
 'electroweb': {'accuracy': 95,
                'basePower': 55,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Electroweb',
                'num': 527,
                'pp': 15,
                'priority': 0,
                'secondary': {'boosts': {'spe': -1}, 'chance': 100},
                'target': 'allAdjacentFoes',
                'type': 'Electric'},
 'embargo': {'accuracy': 100,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 5,
                           'onEnd': 'function (pokemon) {\n'
                                    "\t\t\t\tthis.add('-end', pokemon, "
                                    "'Embargo');\n"
                                    '\t\t\t}',
                           'onResidualOrder': 21,
                           'onStart': 'function (pokemon) {\n'
                                      "\t\t\t\tthis.add('-start', pokemon, "
                                      "'Embargo');\n"
                                      '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
             'isNonstandard': 'Past',
             'name': 'Embargo',
             'num': 373,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark',
             'volatileStatus': 'embargo',
             'zMove': {'boost': {'spa': 1}}},
 'ember': {'accuracy': 100,
           'basePower': 40,
           'category': 'Special',
           'contestType': 'Cute',
           'flags': {'mirror': 1, 'protect': 1},
           'name': 'Ember',
           'num': 52,
           'pp': 25,
           'priority': 0,
           'secondary': {'chance': 10, 'status': 'brn'},
           'target': 'normal',
           'type': 'Fire'},
 'encore': {'accuracy': 100,
            'basePower': 0,
            'category': 'Status',
            'condition': {'duration': 3,
                          'noCopy': True,
                          'onDisableMove': 'function (pokemon) {\n'
                                           '\t\t\t\tif (!this.effectState.move '
                                           '|| '
                                           '!pokemon.hasMove(this.effectState.move)) '
                                           '{\n'
                                           '\t\t\t\t\treturn;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tfor (var _i = 0, _a = '
                                           'pokemon.moveSlots; _i < _a.length; '
                                           '_i++) {\n'
                                           '\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                           '\t\t\t\t\tif (moveSlot.id !== '
                                           'this.effectState.move) {\n'
                                           '\t\t\t\t\t\t'
                                           'pokemon.disableMove(moveSlot.id);\n'
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                          'onEnd': 'function (target) {\n'
                                   "\t\t\t\tthis.add('-end', target, "
                                   "'Encore');\n"
                                   '\t\t\t}',
                          'onOverrideAction': 'function (pokemon, target, '
                                              'move) {\n'
                                              '\t\t\t\tif (move.id !== '
                                              'this.effectState.move)\n'
                                              '\t\t\t\t\treturn '
                                              'this.effectState.move;\n'
                                              '\t\t\t}',
                          'onResidual': 'function (target) {\n'
                                        '\t\t\t\tif '
                                        '(target.moves.includes(this.effectState.move) '
                                        '&&\n'
                                        '\t\t\t\t\t'
                                        'target.moveSlots[target.moves.indexOf(this.effectState.move)].pp '
                                        '<= 0) {\n'
                                        '\t\t\t\t\t// early termination if you '
                                        'run out of PP\n'
                                        '\t\t\t\t\t'
                                        "target.removeVolatile('encore');\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                          'onResidualOrder': 16,
                          'onStart': 'function (target) {\n'
                                     '\t\t\t\tvar noEncore = [\n'
                                     "\t\t\t\t\t'assist', 'copycat', 'encore', "
                                     "'mefirst', 'metronome', 'mimic', "
                                     "'mirrormove', 'naturepower', 'sketch', "
                                     "'sleeptalk', 'struggle', 'transform',\n"
                                     '\t\t\t\t];\n'
                                     '\t\t\t\tvar move = target.lastMove;\n'
                                     '\t\t\t\tif (!move || '
                                     "target.volatiles['dynamax'])\n"
                                     '\t\t\t\t\treturn false;\n'
                                     '\t\t\t\tif (move.isMax && '
                                     'move.baseMove)\n'
                                     '\t\t\t\t\tmove = '
                                     'this.dex.moves.get(move.baseMove);\n'
                                     '\t\t\t\tvar moveIndex = '
                                     'target.moves.indexOf(move.id);\n'
                                     '\t\t\t\tif (move.isZ || '
                                     'noEncore.includes(move.id) || '
                                     '!target.moveSlots[moveIndex] || '
                                     'target.moveSlots[moveIndex].pp <= 0) {\n'
                                     '\t\t\t\t\t// it failed\n'
                                     '\t\t\t\t\treturn false;\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t\tthis.effectState.move = '
                                     'move.id;\n'
                                     "\t\t\t\tthis.add('-start', target, "
                                     "'Encore');\n"
                                     '\t\t\t\tif '
                                     '(!this.queue.willMove(target)) {\n'
                                     '\t\t\t\t\tthis.effectState.duration++;\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
            'contestType': 'Cute',
            'flags': {'authentic': 1,
                      'mirror': 1,
                      'protect': 1,
                      'reflectable': 1},
            'name': 'Encore',
            'num': 227,
            'pp': 5,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'volatileStatus': 'encore',
            'zMove': {'boost': {'spe': 1}}},
 'endeavor': {'accuracy': 100,
              'basePower': 0,
              'category': 'Physical',
              'contestType': 'Tough',
              'damageCallback': 'function (pokemon, target) {\n'
                                '\t\t\treturn target.getUndynamaxedHP() - '
                                'pokemon.hp;\n'
                                '\t\t}',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'maxMove': {'basePower': 130},
              'name': 'Endeavor',
              'num': 283,
              'onTryImmunity': 'function (target, pokemon) {\n'
                               '\t\t\treturn pokemon.hp < target.hp;\n'
                               '\t\t}',
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'basePower': 160}},
 'endure': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'condition': {'duration': 1,
                          'onDamage': 'function (damage, target, source, '
                                      'effect) {\n'
                                      '\t\t\t\tif ((effect === null || effect '
                                      '=== void 0 ? void 0 : '
                                      "effect.effectType) === 'Move' && damage "
                                      '>= target.hp) {\n'
                                      "\t\t\t\t\tthis.add('-activate', target, "
                                      "'move: Endure');\n"
                                      '\t\t\t\t\treturn target.hp - 1;\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                          'onDamagePriority': -10,
                          'onStart': 'function (target) {\n'
                                     "\t\t\t\tthis.add('-singleturn', target, "
                                     "'move: Endure');\n"
                                     '\t\t\t}'},
            'contestType': 'Tough',
            'flags': {},
            'name': 'Endure',
            'num': 203,
            'onHit': 'function (pokemon) {\n'
                     "\t\t\tpokemon.addVolatile('stall');\n"
                     '\t\t}',
            'onPrepareHit': 'function (pokemon) {\n'
                            '\t\t\treturn !!this.queue.willAct() && '
                            "this.runEvent('StallMove', pokemon);\n"
                            '\t\t}',
            'pp': 10,
            'priority': 4,
            'secondary': None,
            'stallingMove': True,
            'target': 'self',
            'type': 'Normal',
            'volatileStatus': 'endure',
            'zMove': {'effect': 'clearnegativeboost'}},
 'energyball': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'name': 'Energy Ball',
                'num': 412,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'spd': -1}, 'chance': 10},
                'target': 'normal',
                'type': 'Grass'},
 'entrainment': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Cute',
                 'flags': {'mirror': 1,
                           'mystery': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'name': 'Entrainment',
                 'num': 494,
                 'onHit': 'function (target, source) {\n'
                          '\t\t\tvar oldAbility = '
                          'target.setAbility(source.ability);\n'
                          '\t\t\tif (oldAbility) {\n'
                          "\t\t\t\tthis.add('-ability', target, "
                          "target.getAbility().name, '[from] move: "
                          "Entrainment');\n"
                          '\t\t\t\tif (!target.isAlly(source))\n'
                          "\t\t\t\t\ttarget.volatileStaleness = 'external';\n"
                          '\t\t\t\treturn;\n'
                          '\t\t\t}\n'
                          '\t\t\treturn false;\n'
                          '\t\t}',
                 'onTryHit': 'function (target, source) {\n'
                             '\t\t\tif (target === source || '
                             "target.volatiles['dynamax'])\n"
                             '\t\t\t\treturn false;\n'
                             '\t\t\tvar additionalBannedSourceAbilities = [\n'
                             '\t\t\t\t// Zen Mode included here for '
                             'compatability with Gen 5-6\n'
                             "\t\t\t\t'flowergift', 'forecast', "
                             "'hungerswitch', 'illusion', 'imposter', "
                             "'neutralizinggas', 'powerofalchemy', 'receiver', "
                             "'trace', 'zenmode',\n"
                             '\t\t\t];\n'
                             '\t\t\tif (target.ability === source.ability ||\n'
                             '\t\t\t\ttarget.getAbility().isPermanent || '
                             "target.ability === 'truant' ||\n"
                             '\t\t\t\tsource.getAbility().isPermanent || '
                             'additionalBannedSourceAbilities.includes(source.ability)) '
                             '{\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'boost': {'spd': 1}}},
 'eruption': {'accuracy': 100,
              'basePower': 150,
              'basePowerCallback': 'function (pokemon, target, move) {\n'
                                   '\t\t\treturn move.basePower * pokemon.hp / '
                                   'pokemon.maxhp;\n'
                                   '\t\t}',
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Eruption',
              'num': 284,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'allAdjacentFoes',
              'type': 'Fire'},
 'eternabeam': {'accuracy': 90,
                'basePower': 160,
                'category': 'Special',
                'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
                'name': 'Eternabeam',
                'num': 795,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'volatileStatus': 'mustrecharge'},
                'target': 'normal',
                'type': 'Dragon'},
 'expandingforce': {'accuracy': 100,
                    'basePower': 80,
                    'category': 'Special',
                    'flags': {'mirror': 1, 'protect': 1},
                    'name': 'Expanding Force',
                    'num': 797,
                    'onBasePower': 'function (basePower, source) {\n'
                                   '\t\t\tif '
                                   "(this.field.isTerrain('psychicterrain') && "
                                   'source.isGrounded()) {\n'
                                   "\t\t\t\tthis.debug('terrain buff');\n"
                                   '\t\t\t\treturn this.chainModify(1.5);\n'
                                   '\t\t\t}\n'
                                   '\t\t}',
                    'onModifyMove': 'function (move, source, target) {\n'
                                    '\t\t\tif '
                                    "(this.field.isTerrain('psychicterrain') "
                                    '&& source.isGrounded()) {\n'
                                    "\t\t\t\tmove.target = 'allAdjacentFoes';\n"
                                    '\t\t\t}\n'
                                    '\t\t}',
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Psychic'},
 'explosion': {'accuracy': 100,
               'basePower': 250,
               'category': 'Physical',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Explosion',
               'num': 153,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'selfdestruct': 'always',
               'target': 'allAdjacent',
               'type': 'Normal'},
 'extrasensory': {'accuracy': 100,
                  'basePower': 80,
                  'category': 'Special',
                  'contestType': 'Cool',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Extrasensory',
                  'num': 326,
                  'pp': 20,
                  'priority': 0,
                  'secondary': {'chance': 10, 'volatileStatus': 'flinch'},
                  'target': 'normal',
                  'type': 'Psychic'},
 'extremeevoboost': {'accuracy': True,
                     'basePower': 0,
                     'boosts': {'atk': 2,
                                'def': 2,
                                'spa': 2,
                                'spd': 2,
                                'spe': 2},
                     'category': 'Status',
                     'contestType': 'Beautiful',
                     'flags': {},
                     'isNonstandard': 'Past',
                     'isZ': 'eeviumz',
                     'name': 'Extreme Evoboost',
                     'num': 702,
                     'pp': 1,
                     'priority': 0,
                     'secondary': None,
                     'target': 'self',
                     'type': 'Normal'},
 'extremespeed': {'accuracy': 100,
                  'basePower': 80,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Extreme Speed',
                  'num': 245,
                  'pp': 5,
                  'priority': 2,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Normal'},
 'facade': {'accuracy': 100,
            'basePower': 70,
            'category': 'Physical',
            'contestType': 'Cute',
            'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
            'name': 'Facade',
            'num': 263,
            'onBasePower': 'function (basePower, pokemon) {\n'
                           '\t\t\tif (pokemon.status && pokemon.status !== '
                           "'slp') {\n"
                           '\t\t\t\treturn this.chainModify(2);\n'
                           '\t\t\t}\n'
                           '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal'},
 'fairylock': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 2,
                             'onStart': 'function (target) {\n'
                                        "\t\t\t\tthis.add('-fieldactivate', "
                                        "'move: Fairy Lock');\n"
                                        '\t\t\t}',
                             'onTrapPokemon': 'function (pokemon) {\n'
                                              '\t\t\t\tpokemon.tryTrap();\n'
                                              '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'authentic': 1, 'mirror': 1},
               'name': 'Fairy Lock',
               'num': 587,
               'pp': 10,
               'priority': 0,
               'pseudoWeather': 'fairylock',
               'secondary': None,
               'target': 'all',
               'type': 'Fairy',
               'zMove': {'boost': {'def': 1}}},
 'fairywind': {'accuracy': 100,
               'basePower': 40,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Fairy Wind',
               'num': 584,
               'pp': 30,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fairy'},
 'fakeout': {'accuracy': 100,
             'basePower': 40,
             'category': 'Physical',
             'contestType': 'Cute',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Fake Out',
             'num': 252,
             'onTry': 'function (source) {\n'
                      '\t\t\tif (source.activeMoveActions > 1) {\n'
                      '\t\t\t\tthis.hint("Fake Out only works on your first '
                      'turn out.");\n'
                      '\t\t\t\treturn false;\n'
                      '\t\t\t}\n'
                      '\t\t}',
             'pp': 10,
             'priority': 3,
             'secondary': {'chance': 100, 'volatileStatus': 'flinch'},
             'target': 'normal',
             'type': 'Normal'},
 'faketears': {'accuracy': 100,
               'basePower': 0,
               'boosts': {'spd': -2},
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'mirror': 1,
                         'mystery': 1,
                         'protect': 1,
                         'reflectable': 1},
               'name': 'Fake Tears',
               'num': 313,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Dark',
               'zMove': {'boost': {'spa': 1}}},
 'falsesurrender': {'accuracy': True,
                    'basePower': 80,
                    'category': 'Physical',
                    'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                    'name': 'False Surrender',
                    'num': 793,
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Dark'},
 'falseswipe': {'accuracy': 100,
                'basePower': 40,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'False Swipe',
                'num': 206,
                'onDamage': 'function (damage, target, source, effect) {\n'
                            '\t\t\tif (damage >= target.hp)\n'
                            '\t\t\t\treturn target.hp - 1;\n'
                            '\t\t}',
                'onDamagePriority': -20,
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'featherdance': {'accuracy': 100,
                  'basePower': 0,
                  'boosts': {'atk': -2},
                  'category': 'Status',
                  'contestType': 'Beautiful',
                  'flags': {'dance': 1,
                            'mirror': 1,
                            'mystery': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': 'Feather Dance',
                  'num': 297,
                  'pp': 15,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Flying',
                  'zMove': {'boost': {'def': 1}}},
 'feint': {'accuracy': 100,
           'basePower': 30,
           'breaksProtect': True,
           'category': 'Physical',
           'contestType': 'Clever',
           'flags': {'mirror': 1},
           'name': 'Feint',
           'num': 364,
           'pp': 10,
           'priority': 2,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal'},
 'feintattack': {'accuracy': True,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Feint Attack',
                 'num': 185,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Dark'},
 'fellstinger': {'accuracy': 100,
                 'basePower': 50,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Fell Stinger',
                 'num': 565,
                 'onAfterMoveSecondarySelf': 'function (pokemon, target, move) '
                                             '{\n'
                                             '\t\t\tif (!target || '
                                             'target.fainted || target.hp <= '
                                             '0)\n'
                                             '\t\t\t\tthis.boost({ atk: 3 }, '
                                             'pokemon, pokemon, move);\n'
                                             '\t\t}',
                 'pp': 25,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Bug'},
 'fierydance': {'accuracy': 100,
                'basePower': 80,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'dance': 1, 'mirror': 1, 'protect': 1},
                'name': 'Fiery Dance',
                'num': 552,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 50, 'self': {'boosts': {'spa': 1}}},
                'target': 'normal',
                'type': 'Fire'},
 'fierywrath': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Fiery Wrath',
                'num': 822,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
                'target': 'allAdjacentFoes',
                'type': 'Dark'},
 'finalgambit': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Special',
                 'contestType': 'Tough',
                 'damageCallback': 'function (pokemon) {\n'
                                   '\t\t\tvar damage = pokemon.hp;\n'
                                   '\t\t\tpokemon.faint();\n'
                                   '\t\t\treturn damage;\n'
                                   '\t\t}',
                 'flags': {'protect': 1},
                 'name': 'Final Gambit',
                 'num': 515,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'selfdestruct': 'ifHit',
                 'target': 'normal',
                 'type': 'Fighting',
                 'zMove': {'basePower': 180}},
 'fireblast': {'accuracy': 85,
               'basePower': 110,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Fire Blast',
               'num': 126,
               'pp': 5,
               'priority': 0,
               'secondary': {'chance': 10, 'status': 'brn'},
               'target': 'normal',
               'type': 'Fire'},
 'firefang': {'accuracy': 95,
              'basePower': 65,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Fire Fang',
              'num': 424,
              'pp': 15,
              'priority': 0,
              'secondaries': [{'chance': 10, 'status': 'brn'},
                              {'chance': 10, 'volatileStatus': 'flinch'}],
              'target': 'normal',
              'type': 'Fire'},
 'firelash': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Cute',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Fire Lash',
              'num': 680,
              'pp': 15,
              'priority': 0,
              'secondary': {'boosts': {'def': -1}, 'chance': 100},
              'target': 'normal',
              'type': 'Fire'},
 'firepledge': {'accuracy': 100,
                'basePower': 80,
                'basePowerCallback': 'function (target, source, move) {\n'
                                     "\t\t\tif (['grasspledge', "
                                     "'waterpledge'].includes(move.sourceEffect)) "
                                     '{\n'
                                     "\t\t\t\tthis.add('-combine');\n"
                                     '\t\t\t\treturn 150;\n'
                                     '\t\t\t}\n'
                                     '\t\t\treturn 80;\n'
                                     '\t\t}',
                'category': 'Special',
                'condition': {'duration': 4,
                              'onResidual': 'function (pokemon) {\n'
                                            '\t\t\t\tif '
                                            "(!pokemon.hasType('Fire'))\n"
                                            '\t\t\t\t\t'
                                            'this.damage(pokemon.baseMaxhp / '
                                            '8, pokemon);\n'
                                            '\t\t\t}',
                              'onResidualOrder': 5,
                              'onResidualSubOrder': 1,
                              'onSideEnd': 'function (targetSide) {\n'
                                           "\t\t\t\tthis.add('-sideend', "
                                           "targetSide, 'Fire Pledge');\n"
                                           '\t\t\t}',
                              'onSideResidualOrder': 26,
                              'onSideResidualSubOrder': 8,
                              'onSideStart': 'function (targetSide) {\n'
                                             "\t\t\t\tthis.add('-sidestart', "
                                             "targetSide, 'Fire Pledge');\n"
                                             '\t\t\t}'},
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                'name': 'Fire Pledge',
                'num': 519,
                'onModifyMove': 'function (move) {\n'
                                '\t\t\tif (move.sourceEffect === '
                                "'waterpledge') {\n"
                                "\t\t\t\tmove.type = 'Water';\n"
                                '\t\t\t\tmove.forceSTAB = true;\n'
                                '\t\t\t\tmove.self = { sideCondition: '
                                "'waterpledge' };\n"
                                '\t\t\t}\n'
                                '\t\t\tif (move.sourceEffect === '
                                "'grasspledge') {\n"
                                "\t\t\t\tmove.type = 'Fire';\n"
                                '\t\t\t\tmove.forceSTAB = true;\n'
                                "\t\t\t\tmove.sideCondition = 'firepledge';\n"
                                '\t\t\t}\n'
                                '\t\t}',
                'onPrepareHit': 'function (target, source, move) {\n'
                                '\t\t\tvar _a;\n'
                                '\t\t\tfor (var _i = 0, _b = this.queue.list; '
                                '_i < _b.length; _i++) {\n'
                                '\t\t\t\tvar action = _b[_i];\n'
                                '\t\t\t\tif (!action.move || !((_a = '
                                'action.pokemon) === null || _a === void 0 ? '
                                'void 0 : _a.isActive) ||\n'
                                '\t\t\t\t\taction.pokemon.fainted || '
                                'action.maxMove || action.zmove) {\n'
                                '\t\t\t\t\tcontinue;\n'
                                '\t\t\t\t}\n'
                                '\t\t\t\tif (action.pokemon.isAlly(source) && '
                                "['grasspledge', "
                                "'waterpledge'].includes(action.move.id)) {\n"
                                '\t\t\t\t\tthis.queue.prioritizeAction(action, '
                                'move);\n'
                                "\t\t\t\t\tthis.add('-waiting', source, "
                                'action.pokemon);\n'
                                '\t\t\t\t\treturn null;\n'
                                '\t\t\t\t}\n'
                                '\t\t\t}\n'
                                '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fire'},
 'firepunch': {'accuracy': 100,
               'basePower': 75,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
               'name': 'Fire Punch',
               'num': 7,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 10, 'status': 'brn'},
               'target': 'normal',
               'type': 'Fire'},
 'firespin': {'accuracy': 85,
              'basePower': 35,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Fire Spin',
              'num': 83,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Fire',
              'volatileStatus': 'partiallytrapped'},
 'firstimpression': {'accuracy': 100,
                     'basePower': 90,
                     'category': 'Physical',
                     'contestType': 'Cute',
                     'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                     'name': 'First Impression',
                     'num': 660,
                     'onTry': 'function (source) {\n'
                              '\t\t\tif (source.activeMoveActions > 1) {\n'
                              '\t\t\t\tthis.hint("First Impression only works '
                              'on your first turn out.");\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t}',
                     'pp': 10,
                     'priority': 2,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Bug'},
 'fishiousrend': {'accuracy': 100,
                  'basePower': 85,
                  'basePowerCallback': 'function (pokemon, target, move) {\n'
                                       '\t\t\tif (target.newlySwitched || '
                                       'this.queue.willMove(target)) {\n'
                                       "\t\t\t\tthis.debug('Fishious Rend "
                                       "damage boost');\n"
                                       '\t\t\t\treturn move.basePower * 2;\n'
                                       '\t\t\t}\n'
                                       "\t\t\tthis.debug('Fishious Rend NOT "
                                       "boosted');\n"
                                       '\t\t\treturn move.basePower;\n'
                                       '\t\t}',
                  'category': 'Physical',
                  'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Fishious Rend',
                  'num': 755,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Water'},
 'fissure': {'accuracy': 30,
             'basePower': 0,
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
             'maxMove': {'basePower': 130},
             'name': 'Fissure',
             'num': 90,
             'ohko': True,
             'pp': 5,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Ground',
             'zMove': {'basePower': 180}},
 'flail': {'accuracy': 100,
           'basePower': 0,
           'basePowerCallback': 'function (pokemon, target) {\n'
                                '\t\t\tvar ratio = pokemon.hp * 48 / '
                                'pokemon.maxhp;\n'
                                '\t\t\tif (ratio < 2) {\n'
                                '\t\t\t\treturn 200;\n'
                                '\t\t\t}\n'
                                '\t\t\tif (ratio < 5) {\n'
                                '\t\t\t\treturn 150;\n'
                                '\t\t\t}\n'
                                '\t\t\tif (ratio < 10) {\n'
                                '\t\t\t\treturn 100;\n'
                                '\t\t\t}\n'
                                '\t\t\tif (ratio < 17) {\n'
                                '\t\t\t\treturn 80;\n'
                                '\t\t\t}\n'
                                '\t\t\tif (ratio < 33) {\n'
                                '\t\t\t\treturn 40;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn 20;\n'
                                '\t\t}',
           'category': 'Physical',
           'contestType': 'Cute',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'maxMove': {'basePower': 130},
           'name': 'Flail',
           'num': 175,
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal',
           'zMove': {'basePower': 160}},
 'flameburst': {'accuracy': 100,
                'basePower': 70,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Flame Burst',
                'num': 481,
                'onAfterSubDamage': 'function (damage, target, source, move) '
                                    '{\n'
                                    '\t\t\tfor (var _i = 0, _a = '
                                    'target.adjacentAllies(); _i < _a.length; '
                                    '_i++) {\n'
                                    '\t\t\t\tvar ally = _a[_i];\n'
                                    '\t\t\t\tthis.damage(ally.baseMaxhp / 16, '
                                    'ally, source, '
                                    "this.dex.conditions.get('Flame Burst'));\n"
                                    '\t\t\t}\n'
                                    '\t\t}',
                'onHit': 'function (target, source, move) {\n'
                         '\t\t\tfor (var _i = 0, _a = target.adjacentAllies(); '
                         '_i < _a.length; _i++) {\n'
                         '\t\t\t\tvar ally = _a[_i];\n'
                         '\t\t\t\tthis.damage(ally.baseMaxhp / 16, ally, '
                         "source, this.dex.conditions.get('Flame Burst'));\n"
                         '\t\t\t}\n'
                         '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fire'},
 'flamecharge': {'accuracy': 100,
                 'basePower': 50,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Flame Charge',
                 'num': 488,
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'chance': 100, 'self': {'boosts': {'spe': 1}}},
                 'target': 'normal',
                 'type': 'Fire'},
 'flamethrower': {'accuracy': 100,
                  'basePower': 90,
                  'category': 'Special',
                  'contestType': 'Beautiful',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Flamethrower',
                  'num': 53,
                  'pp': 15,
                  'priority': 0,
                  'secondary': {'chance': 10, 'status': 'brn'},
                  'target': 'normal',
                  'type': 'Fire'},
 'flamewheel': {'accuracy': 100,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Beautiful',
                'flags': {'contact': 1,
                          'defrost': 1,
                          'mirror': 1,
                          'protect': 1},
                'name': 'Flame Wheel',
                'num': 172,
                'pp': 25,
                'priority': 0,
                'secondary': {'chance': 10, 'status': 'brn'},
                'target': 'normal',
                'type': 'Fire'},
 'flareblitz': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1,
                          'defrost': 1,
                          'mirror': 1,
                          'protect': 1},
                'name': 'Flare Blitz',
                'num': 394,
                'pp': 15,
                'priority': 0,
                'recoil': [33, 100],
                'secondary': {'chance': 10, 'status': 'brn'},
                'target': 'normal',
                'type': 'Fire'},
 'flash': {'accuracy': 100,
           'basePower': 0,
           'boosts': {'accuracy': -1},
           'category': 'Status',
           'contestType': 'Beautiful',
           'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
           'isNonstandard': 'Past',
           'name': 'Flash',
           'num': 148,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal',
           'zMove': {'boost': {'evasion': 1}}},
 'flashcannon': {'accuracy': 100,
                 'basePower': 80,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Flash Cannon',
                 'num': 430,
                 'pp': 10,
                 'priority': 0,
                 'secondary': {'boosts': {'spd': -1}, 'chance': 10},
                 'target': 'normal',
                 'type': 'Steel'},
 'flatter': {'accuracy': 100,
             'basePower': 0,
             'boosts': {'spa': 1},
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'mirror': 1,
                       'mystery': 1,
                       'protect': 1,
                       'reflectable': 1},
             'name': 'Flatter',
             'num': 260,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark',
             'volatileStatus': 'confusion',
             'zMove': {'boost': {'spd': 1}}},
 'fleurcannon': {'accuracy': 90,
                 'basePower': 130,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Fleur Cannon',
                 'num': 705,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'boosts': {'spa': -2}},
                 'target': 'normal',
                 'type': 'Fairy'},
 'fling': {'accuracy': 100,
           'basePower': 0,
           'category': 'Physical',
           'condition': {'onUpdate': 'function (pokemon) {\n'
                                     '\t\t\t\tvar item = pokemon.getItem();\n'
                                     "\t\t\t\tpokemon.setItem('');\n"
                                     '\t\t\t\tpokemon.lastItem = item.id;\n'
                                     '\t\t\t\tpokemon.usedItemThisTurn = '
                                     'true;\n'
                                     "\t\t\t\tthis.add('-enditem', pokemon, "
                                     "item.name, '[from] move: Fling');\n"
                                     "\t\t\t\tthis.runEvent('AfterUseItem', "
                                     'pokemon, null, null, item);\n'
                                     '\t\t\t\t'
                                     "pokemon.removeVolatile('fling');\n"
                                     '\t\t\t}'},
           'contestType': 'Cute',
           'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
           'name': 'Fling',
           'num': 374,
           'onPrepareHit': 'function (target, source, move) {\n'
                           '\t\t\tif (source.ignoringItem())\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t\tvar item = source.getItem();\n'
                           "\t\t\tif (!this.singleEvent('TakeItem', item, "
                           'source.itemState, source, source, move, item))\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t\tif (!item.fling)\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t\tmove.basePower = item.fling.basePower;\n'
                           '\t\t\tif (item.isBerry) {\n'
                           '\t\t\t\tmove.onHit = function (foe) {\n'
                           "\t\t\t\t\tif (this.singleEvent('Eat', item, null, "
                           'foe, null, null)) {\n'
                           "\t\t\t\t\t\tthis.runEvent('EatItem', foe, null, "
                           'null, item);\n'
                           "\t\t\t\t\t\tif (item.id === 'leppaberry')\n"
                           "\t\t\t\t\t\t\tfoe.staleness = 'external';\n"
                           '\t\t\t\t\t}\n'
                           '\t\t\t\t\tif (item.onEat)\n'
                           '\t\t\t\t\t\tfoe.ateBerry = true;\n'
                           '\t\t\t\t};\n'
                           '\t\t\t}\n'
                           '\t\t\telse if (item.fling.effect) {\n'
                           '\t\t\t\tmove.onHit = item.fling.effect;\n'
                           '\t\t\t}\n'
                           '\t\t\telse {\n'
                           '\t\t\t\tif (!move.secondaries)\n'
                           '\t\t\t\t\tmove.secondaries = [];\n'
                           '\t\t\t\tif (item.fling.status) {\n'
                           '\t\t\t\t\tmove.secondaries.push({ status: '
                           'item.fling.status });\n'
                           '\t\t\t\t}\n'
                           '\t\t\t\telse if (item.fling.volatileStatus) {\n'
                           '\t\t\t\t\tmove.secondaries.push({ volatileStatus: '
                           'item.fling.volatileStatus });\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           "\t\t\tsource.addVolatile('fling');\n"
                           '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Dark'},
 'flipturn': {'accuracy': 100,
              'basePower': 60,
              'category': 'Physical',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Flip Turn',
              'num': 812,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'selfSwitch': True,
              'target': 'normal',
              'type': 'Water'},
 'floatyfall': {'accuracy': 95,
                'basePower': 90,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'gravity': 1, 'protect': 1},
                'isNonstandard': 'LGPE',
                'name': 'Floaty Fall',
                'num': 731,
                'pp': 15,
                'priority': 0,
                'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                'target': 'normal',
                'type': 'Flying'},
 'floralhealing': {'accuracy': True,
                   'basePower': 0,
                   'category': 'Status',
                   'contestType': 'Beautiful',
                   'flags': {'heal': 1,
                             'mystery': 1,
                             'protect': 1,
                             'reflectable': 1},
                   'name': 'Floral Healing',
                   'num': 666,
                   'onHit': 'function (target, source) {\n'
                            '\t\t\tvar success = false;\n'
                            "\t\t\tif (this.field.isTerrain('grassyterrain')) "
                            '{\n'
                            '\t\t\t\tsuccess = '
                            '!!this.heal(this.modify(target.baseMaxhp, '
                            '0.667));\n'
                            '\t\t\t}\n'
                            '\t\t\telse {\n'
                            '\t\t\t\tsuccess = '
                            '!!this.heal(Math.ceil(target.baseMaxhp * 0.5));\n'
                            '\t\t\t}\n'
                            '\t\t\tif (success && !target.isAlly(source)) {\n'
                            "\t\t\t\ttarget.staleness = 'external';\n"
                            '\t\t\t}\n'
                            '\t\t\treturn success;\n'
                            '\t\t}',
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Fairy',
                   'zMove': {'effect': 'clearnegativeboost'}},
 'flowershield': {'accuracy': True,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Beautiful',
                  'flags': {'distance': 1},
                  'name': 'Flower Shield',
                  'num': 579,
                  'onHitField': 'function (t, source, move) {\n'
                                '\t\t\tvar targets = [];\n'
                                '\t\t\tfor (var _i = 0, _a = '
                                'this.getAllActive(); _i < _a.length; _i++) {\n'
                                '\t\t\t\tvar pokemon = _a[_i];\n'
                                "\t\t\t\tif (pokemon.hasType('Grass') &&\n"
                                "\t\t\t\t\t(!pokemon.volatiles['maxguard'] ||\n"
                                "\t\t\t\t\t\tthis.runEvent('TryHit', pokemon, "
                                'source, move))) {\n'
                                '\t\t\t\t\t// This move affects every '
                                'Grass-type Pokemon in play.\n'
                                '\t\t\t\t\ttargets.push(pokemon);\n'
                                '\t\t\t\t}\n'
                                '\t\t\t}\n'
                                '\t\t\tvar success = false;\n'
                                '\t\t\tfor (var _b = 0, targets_1 = targets; '
                                '_b < targets_1.length; _b++) {\n'
                                '\t\t\t\tvar target = targets_1[_b];\n'
                                '\t\t\t\tsuccess = this.boost({ def: 1 }, '
                                'target, source, move) || success;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn success;\n'
                                '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'all',
                  'type': 'Fairy',
                  'zMove': {'boost': {'def': 1}}},
 'fly': {'accuracy': 95,
         'basePower': 90,
         'category': 'Physical',
         'condition': {'duration': 2,
                       'onInvulnerability': 'function (target, source, move) '
                                            '{\n'
                                            "\t\t\t\tif (['gust', 'twister', "
                                            "'skyuppercut', 'thunder', "
                                            "'hurricane', 'smackdown', "
                                            "'thousandarrows'].includes(move.id)) "
                                            '{\n'
                                            '\t\t\t\t\treturn;\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t\treturn false;\n'
                                            '\t\t\t}',
                       'onSourceModifyDamage': 'function (damage, source, '
                                               'target, move) {\n'
                                               "\t\t\t\tif (move.id === 'gust' "
                                               "|| move.id === 'twister') {\n"
                                               '\t\t\t\t\treturn '
                                               'this.chainModify(2);\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}'},
         'contestType': 'Clever',
         'flags': {'charge': 1,
                   'contact': 1,
                   'distance': 1,
                   'gravity': 1,
                   'mirror': 1,
                   'protect': 1},
         'name': 'Fly',
         'num': 19,
         'onTryMove': 'function (attacker, defender, move) {\n'
                      '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                      '\t\t\t\treturn;\n'
                      '\t\t\t}\n'
                      "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                      "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                      'defender, move)) {\n'
                      '\t\t\t\treturn;\n'
                      '\t\t\t}\n'
                      "\t\t\tattacker.addVolatile('twoturnmove', defender);\n"
                      '\t\t\treturn null;\n'
                      '\t\t}',
         'pp': 15,
         'priority': 0,
         'secondary': None,
         'target': 'any',
         'type': 'Flying'},
 'flyingpress': {'accuracy': 95,
                 'basePower': 100,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1,
                           'distance': 1,
                           'gravity': 1,
                           'mirror': 1,
                           'nonsky': 1,
                           'protect': 1},
                 'name': 'Flying Press',
                 'num': 560,
                 'onEffectiveness': 'function (typeMod, target, type, move) {\n'
                                    '\t\t\treturn typeMod + '
                                    "this.dex.getEffectiveness('Flying', "
                                    'type);\n'
                                    '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'any',
                 'type': 'Fighting',
                 'zMove': {'basePower': 170}},
 'focusblast': {'accuracy': 70,
                'basePower': 120,
                'category': 'Special',
                'contestType': 'Cool',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'name': 'Focus Blast',
                'num': 411,
                'pp': 5,
                'priority': 0,
                'secondary': {'boosts': {'spd': -1}, 'chance': 10},
                'target': 'normal',
                'type': 'Fighting'},
 'focusenergy': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'onModifyCritRatio': 'function (critRatio) {\n'
                                                    '\t\t\t\treturn critRatio '
                                                    '+ 2;\n'
                                                    '\t\t\t}',
                               'onStart': 'function (target, source, effect) '
                                          '{\n'
                                          '\t\t\t\tif ((effect === null || '
                                          'effect === void 0 ? void 0 : '
                                          "effect.id) === 'zpower') {\n"
                                          "\t\t\t\t\tthis.add('-start', "
                                          "target, 'move: Focus Energy', "
                                          "'[zeffect]');\n"
                                          '\t\t\t\t}\n'
                                          '\t\t\t\telse if (effect && '
                                          "(['imposter', 'psychup', "
                                          "'transform'].includes(effect.id))) "
                                          '{\n'
                                          "\t\t\t\t\tthis.add('-start', "
                                          "target, 'move: Focus Energy', "
                                          "'[silent]');\n"
                                          '\t\t\t\t}\n'
                                          '\t\t\t\telse {\n'
                                          "\t\t\t\t\tthis.add('-start', "
                                          "target, 'move: Focus Energy');\n"
                                          '\t\t\t\t}\n'
                                          '\t\t\t}'},
                 'contestType': 'Cool',
                 'flags': {'snatch': 1},
                 'name': 'Focus Energy',
                 'num': 116,
                 'pp': 30,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Normal',
                 'volatileStatus': 'focusenergy',
                 'zMove': {'boost': {'accuracy': 1}}},
 'focuspunch': {'accuracy': 100,
                'basePower': 150,
                'beforeMoveCallback': 'function (pokemon) {\n'
                                      '\t\t\tif '
                                      "(pokemon.volatiles['focuspunch'] && "
                                      "pokemon.volatiles['focuspunch'].lostFocus) "
                                      '{\n'
                                      "\t\t\t\tthis.add('cant', pokemon, "
                                      "'Focus Punch', 'Focus Punch');\n"
                                      '\t\t\t\treturn true;\n'
                                      '\t\t\t}\n'
                                      '\t\t}',
                'beforeTurnCallback': 'function (pokemon) {\n'
                                      '\t\t\t'
                                      "pokemon.addVolatile('focuspunch');\n"
                                      '\t\t}',
                'category': 'Physical',
                'condition': {'duration': 1,
                              'onHit': 'function (pokemon, source, move) {\n'
                                       '\t\t\t\tif (move.category !== '
                                       "'Status') {\n"
                                       '\t\t\t\t\t'
                                       "pokemon.volatiles['focuspunch'].lostFocus "
                                       '= true;\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t}',
                              'onStart': 'function (pokemon) {\n'
                                         "\t\t\t\tthis.add('-singleturn', "
                                         "pokemon, 'move: Focus Punch');\n"
                                         '\t\t\t}',
                              'onTryAddVolatile': 'function (status, pokemon) '
                                                  '{\n'
                                                  '\t\t\t\tif (status.id === '
                                                  "'flinch')\n"
                                                  '\t\t\t\t\treturn null;\n'
                                                  '\t\t\t}'},
                'contestType': 'Tough',
                'flags': {'contact': 1, 'protect': 1, 'punch': 1},
                'name': 'Focus Punch',
                'num': 264,
                'pp': 20,
                'priority': -3,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'followme': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 1,
                            'onFoeRedirectTarget': 'function (target, source, '
                                                   'source2, move) {\n'
                                                   '\t\t\t\tif '
                                                   '(!this.effectState.target.isSkyDropped() '
                                                   '&& '
                                                   'this.validTarget(this.effectState.target, '
                                                   'source, move.target)) {\n'
                                                   '\t\t\t\t\tif '
                                                   '(move.smartTarget)\n'
                                                   '\t\t\t\t\t\t'
                                                   'move.smartTarget = false;\n'
                                                   '\t\t\t\t\t'
                                                   'this.debug("Follow Me '
                                                   'redirected target of '
                                                   'move");\n'
                                                   '\t\t\t\t\treturn '
                                                   'this.effectState.target;\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t}',
                            'onFoeRedirectTargetPriority': 1,
                            'onStart': 'function (target, source, effect) {\n'
                                       '\t\t\t\tif ((effect === null || effect '
                                       '=== void 0 ? void 0 : effect.id) === '
                                       "'zpower') {\n"
                                       "\t\t\t\t\tthis.add('-singleturn', "
                                       "target, 'move: Follow Me', "
                                       "'[zeffect]');\n"
                                       '\t\t\t\t}\n'
                                       '\t\t\t\telse {\n'
                                       "\t\t\t\t\tthis.add('-singleturn', "
                                       "target, 'move: Follow Me');\n"
                                       '\t\t\t\t}\n'
                                       '\t\t\t}'},
              'contestType': 'Cute',
              'flags': {},
              'name': 'Follow Me',
              'num': 266,
              'onTry': 'function (source) {\n'
                       '\t\t\treturn this.activePerHalf > 1;\n'
                       '\t\t}',
              'pp': 20,
              'priority': 2,
              'secondary': None,
              'target': 'self',
              'type': 'Normal',
              'volatileStatus': 'followme',
              'zMove': {'effect': 'clearnegativeboost'}},
 'forcepalm': {'accuracy': 100,
               'basePower': 60,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Force Palm',
               'num': 395,
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 30, 'status': 'par'},
               'target': 'normal',
               'type': 'Fighting'},
 'foresight': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'noCopy': True,
                             'onModifyBoost': 'function (boosts) {\n'
                                              '\t\t\t\tif (boosts.evasion && '
                                              'boosts.evasion > 0) {\n'
                                              '\t\t\t\t\tboosts.evasion = 0;\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                             'onNegateImmunity': 'function (pokemon, type) {\n'
                                                 '\t\t\t\tif '
                                                 "(pokemon.hasType('Ghost') && "
                                                 "['Normal', "
                                                 "'Fighting'].includes(type))\n"
                                                 '\t\t\t\t\treturn false;\n'
                                                 '\t\t\t}',
                             'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-start', pokemon, "
                                        "'Foresight');\n"
                                        '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'protect': 1,
                         'reflectable': 1},
               'isNonstandard': 'Past',
               'name': 'Foresight',
               'num': 193,
               'onTryHit': 'function (target) {\n'
                           "\t\t\tif (target.volatiles['miracleeye'])\n"
                           '\t\t\t\treturn false;\n'
                           '\t\t}',
               'pp': 40,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'volatileStatus': 'foresight',
               'zMove': {'effect': 'crit2'}},
 'forestscurse': {'accuracy': 100,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'mirror': 1,
                            'mystery': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': "Forest's Curse",
                  'num': 571,
                  'onHit': 'function (target) {\n'
                           "\t\t\tif (target.hasType('Grass'))\n"
                           '\t\t\t\treturn false;\n'
                           "\t\t\tif (!target.addType('Grass'))\n"
                           '\t\t\t\treturn false;\n'
                           "\t\t\tthis.add('-start', target, 'typeadd', "
                           "'Grass', '[from] move: Forest's Curse');\n"
                           '\t\t}',
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Grass',
                  'zMove': {'boost': {'atk': 1,
                                      'def': 1,
                                      'spa': 1,
                                      'spd': 1,
                                      'spe': 1}}},
 'foulplay': {'accuracy': 100,
              'basePower': 95,
              'category': 'Physical',
              'contestType': 'Clever',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Foul Play',
              'num': 492,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Dark',
              'useTargetOffensive': True},
 'freezedry': {'accuracy': 100,
               'basePower': 70,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Freeze-Dry',
               'num': 573,
               'onEffectiveness': 'function (typeMod, target, type) {\n'
                                  "\t\t\tif (type === 'Water')\n"
                                  '\t\t\t\treturn 1;\n'
                                  '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': {'chance': 10, 'status': 'frz'},
               'target': 'normal',
               'type': 'Ice'},
 'freezeshock': {'accuracy': 90,
                 'basePower': 140,
                 'category': 'Physical',
                 'contestType': 'Beautiful',
                 'flags': {'charge': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Freeze Shock',
                 'num': 553,
                 'onTryMove': 'function (attacker, defender, move) {\n'
                              '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\t}\n'
                              "\t\t\tthis.add('-prepare', attacker, "
                              'move.name);\n'
                              "\t\t\tif (!this.runEvent('ChargeMove', "
                              'attacker, defender, move)) {\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\t}\n'
                              "\t\t\tattacker.addVolatile('twoturnmove', "
                              'defender);\n'
                              '\t\t\treturn null;\n'
                              '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': {'chance': 30, 'status': 'par'},
                 'target': 'normal',
                 'type': 'Ice'},
 'freezingglare': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Special',
                   'flags': {'mirror': 1, 'protect': 1},
                   'name': 'Freezing Glare',
                   'num': 821,
                   'pp': 10,
                   'priority': 0,
                   'secondary': {'chance': 10, 'status': 'frz'},
                   'target': 'normal',
                   'type': 'Psychic'},
 'freezyfrost': {'accuracy': 90,
                 'basePower': 100,
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {'protect': 1},
                 'isNonstandard': 'LGPE',
                 'name': 'Freezy Frost',
                 'num': 739,
                 'onHit': 'function () {\n'
                          "\t\t\tthis.add('-clearallboost');\n"
                          '\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i '
                          '< _a.length; _i++) {\n'
                          '\t\t\t\tvar pokemon = _a[_i];\n'
                          '\t\t\t\tpokemon.clearBoosts();\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ice'},
 'frenzyplant': {'accuracy': 90,
                 'basePower': 150,
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1,
                           'nonsky': 1,
                           'protect': 1,
                           'recharge': 1},
                 'name': 'Frenzy Plant',
                 'num': 338,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'volatileStatus': 'mustrecharge'},
                 'target': 'normal',
                 'type': 'Grass'},
 'frostbreath': {'accuracy': 90,
                 'basePower': 60,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Frost Breath',
                 'num': 524,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ice',
                 'willCrit': True},
 'frustration': {'accuracy': 100,
                 'basePower': 0,
                 'basePowerCallback': 'function (pokemon) {\n'
                                      '\t\t\treturn Math.floor(((255 - '
                                      'pokemon.happiness) * 10) / 25) || 1;\n'
                                      '\t\t}',
                 'category': 'Physical',
                 'contestType': 'Cute',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'maxMove': {'basePower': 130},
                 'name': 'Frustration',
                 'num': 218,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'basePower': 160}},
 'furyattack': {'accuracy': 85,
                'basePower': 15,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'multihit': [2, 5],
                'name': 'Fury Attack',
                'num': 31,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'furycutter': {'accuracy': 95,
                'basePower': 40,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     '\t\t\tif '
                                     "(!pokemon.volatiles['furycutter'] || "
                                     'move.hit === 1) {\n'
                                     '\t\t\t\t'
                                     "pokemon.addVolatile('furycutter');\n"
                                     '\t\t\t}\n'
                                     '\t\t\treturn '
                                     'this.clampIntRange(move.basePower * '
                                     "pokemon.volatiles['furycutter'].multiplier, "
                                     '1, 160);\n'
                                     '\t\t}',
                'category': 'Physical',
                'condition': {'duration': 2,
                              'onRestart': 'function () {\n'
                                           '\t\t\t\tif '
                                           '(this.effectState.multiplier < 4) '
                                           '{\n'
                                           '\t\t\t\t\t'
                                           'this.effectState.multiplier <<= '
                                           '1;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tthis.effectState.duration '
                                           '= 2;\n'
                                           '\t\t\t}',
                              'onStart': 'function () {\n'
                                         '\t\t\t\tthis.effectState.multiplier '
                                         '= 1;\n'
                                         '\t\t\t}'},
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Fury Cutter',
                'num': 210,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Bug'},
 'furyswipes': {'accuracy': 80,
                'basePower': 18,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 100},
                'multihit': [2, 5],
                'name': 'Fury Swipes',
                'num': 154,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'fusionbolt': {'accuracy': 100,
                'basePower': 100,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Fusion Bolt',
                'num': 559,
                'onBasePower': 'function (basePower, pokemon) {\n'
                               '\t\t\tif (this.lastSuccessfulMoveThisTurn === '
                               "'fusionflare') {\n"
                               "\t\t\t\tthis.debug('double power');\n"
                               '\t\t\t\treturn this.chainModify(2);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Electric'},
 'fusionflare': {'accuracy': 100,
                 'basePower': 100,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Fusion Flare',
                 'num': 558,
                 'onBasePower': 'function (basePower, pokemon) {\n'
                                '\t\t\tif (this.lastSuccessfulMoveThisTurn === '
                                "'fusionbolt') {\n"
                                "\t\t\t\tthis.debug('double power');\n"
                                '\t\t\t\treturn this.chainModify(2);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fire'},
 'futuresight': {'accuracy': 100,
                 'basePower': 120,
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {},
                 'ignoreImmunity': True,
                 'isFutureMove': True,
                 'name': 'Future Sight',
                 'num': 248,
                 'onTry': 'function (source, target) {\n'
                          '\t\t\tif (!target.side.addSlotCondition(target, '
                          "'futuremove'))\n"
                          '\t\t\t\treturn false;\n'
                          '\t\t\t'
                          "Object.assign(target.side.slotConditions[target.position]['futuremove'], "
                          '{\n'
                          '\t\t\t\tduration: 3,\n'
                          "\t\t\t\tmove: 'futuresight',\n"
                          '\t\t\t\tsource: source,\n'
                          '\t\t\t\tmoveData: {\n'
                          "\t\t\t\t\tid: 'futuresight',\n"
                          '\t\t\t\t\tname: "Future Sight",\n'
                          '\t\t\t\t\taccuracy: 100,\n'
                          '\t\t\t\t\tbasePower: 120,\n'
                          '\t\t\t\t\tcategory: "Special",\n'
                          '\t\t\t\t\tpriority: 0,\n'
                          '\t\t\t\t\tflags: {},\n'
                          '\t\t\t\t\tignoreImmunity: false,\n'
                          "\t\t\t\t\teffectType: 'Move',\n"
                          '\t\t\t\t\tisFutureMove: true,\n'
                          "\t\t\t\t\ttype: 'Psychic',\n"
                          '\t\t\t\t},\n'
                          '\t\t\t});\n'
                          "\t\t\tthis.add('-start', source, 'move: Future "
                          "Sight');\n"
                          '\t\t\treturn this.NOT_FAIL;\n'
                          '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Psychic'},
 'gastroacid': {'accuracy': 100,
                'basePower': 0,
                'category': 'Status',
                'condition': {'onCopy': 'function (pokemon) {\n'
                                        '\t\t\t\tif '
                                        '(pokemon.getAbility().isPermanent)\n'
                                        '\t\t\t\t\t'
                                        "pokemon.removeVolatile('gastroacid');\n"
                                        '\t\t\t}',
                              'onStart': 'function (pokemon) {\n'
                                         "\t\t\t\tthis.add('-endability', "
                                         'pokemon);\n'
                                         "\t\t\t\tthis.singleEvent('End', "
                                         'pokemon.getAbility(), '
                                         'pokemon.abilityState, pokemon, '
                                         "pokemon, 'gastroacid');\n"
                                         '\t\t\t}'},
                'contestType': 'Tough',
                'flags': {'mirror': 1,
                          'mystery': 1,
                          'protect': 1,
                          'reflectable': 1},
                'name': 'Gastro Acid',
                'num': 380,
                'onTryHit': 'function (target) {\n'
                            '\t\t\tif (target.getAbility().isPermanent) {\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Poison',
                'volatileStatus': 'gastroacid',
                'zMove': {'boost': {'spe': 1}}},
 'geargrind': {'accuracy': 85,
               'basePower': 50,
               'category': 'Physical',
               'contestType': 'Clever',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'multihit': 2,
               'name': 'Gear Grind',
               'num': 544,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Steel',
               'zMove': {'basePower': 180}},
 'gearup': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Clever',
            'flags': {'authentic': 1, 'snatch': 1},
            'name': 'Gear Up',
            'num': 674,
            'onHitSide': 'function (side, source, move) {\n'
                         '\t\t\tvar _this = this;\n'
                         '\t\t\tvar targets = side.allies().filter(function '
                         "(target) { return (target.hasAbility(['plus', "
                         "'minus']) &&\n"
                         "\t\t\t\t(!target.volatiles['maxguard'] || "
                         "_this.runEvent('TryHit', target, source, move))); "
                         '});\n'
                         '\t\t\tif (!targets.length)\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\tvar didSomething = false;\n'
                         '\t\t\tfor (var _i = 0, targets_2 = targets; _i < '
                         'targets_2.length; _i++) {\n'
                         '\t\t\t\tvar target = targets_2[_i];\n'
                         '\t\t\t\tdidSomething = this.boost({ atk: 1, spa: 1 '
                         '}, target, source, move, false, true) || '
                         'didSomething;\n'
                         '\t\t\t}\n'
                         '\t\t\treturn didSomething;\n'
                         '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'allySide',
            'type': 'Steel',
            'zMove': {'boost': {'spa': 1}}},
 'genesissupernova': {'accuracy': True,
                      'basePower': 185,
                      'category': 'Special',
                      'contestType': 'Cool',
                      'flags': {},
                      'isNonstandard': 'Past',
                      'isZ': 'mewniumz',
                      'name': 'Genesis Supernova',
                      'num': 703,
                      'pp': 1,
                      'priority': 0,
                      'secondary': {'chance': 100,
                                    'self': {'onHit': 'function () {\n'
                                                      '\t\t\t\t\t'
                                                      "this.field.setTerrain('psychicterrain');\n"
                                                      '\t\t\t\t}'}},
                      'target': 'normal',
                      'type': 'Psychic'},
 'geomancy': {'accuracy': True,
              'basePower': 0,
              'boosts': {'spa': 2, 'spd': 2, 'spe': 2},
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {'charge': 1, 'nonsky': 1},
              'name': 'Geomancy',
              'num': 601,
              'onTryMove': 'function (attacker, defender, move) {\n'
                           '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                           '\t\t\t\treturn;\n'
                           '\t\t\t}\n'
                           "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                           "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                           'defender, move)) {\n'
                           '\t\t\t\treturn;\n'
                           '\t\t\t}\n'
                           "\t\t\tattacker.addVolatile('twoturnmove', "
                           'defender);\n'
                           '\t\t\treturn null;\n'
                           '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Fairy',
              'zMove': {'boost': {'atk': 1,
                                  'def': 1,
                                  'spa': 1,
                                  'spd': 1,
                                  'spe': 1}}},
 'gigadrain': {'accuracy': 100,
               'basePower': 75,
               'category': 'Special',
               'contestType': 'Clever',
               'drain': [1, 2],
               'flags': {'heal': 1, 'mirror': 1, 'protect': 1},
               'name': 'Giga Drain',
               'num': 202,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'gigaimpact': {'accuracy': 90,
                'basePower': 150,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1,
                          'mirror': 1,
                          'protect': 1,
                          'recharge': 1},
                'name': 'Giga Impact',
                'num': 416,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'volatileStatus': 'mustrecharge'},
                'target': 'normal',
                'type': 'Normal'},
 'gigavolthavoc': {'accuracy': True,
                   'basePower': 1,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isNonstandard': 'Past',
                   'isZ': 'electriumz',
                   'name': 'Gigavolt Havoc',
                   'num': 646,
                   'pp': 1,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Electric'},
 'glaciallance': {'accuracy': 100,
                  'basePower': 130,
                  'category': 'Physical',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Glacial Lance',
                  'num': 824,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allAdjacentFoes',
                  'type': 'Ice'},
 'glaciate': {'accuracy': 95,
              'basePower': 65,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Glaciate',
              'num': 549,
              'pp': 10,
              'priority': 0,
              'secondary': {'boosts': {'spe': -1}, 'chance': 100},
              'target': 'allAdjacentFoes',
              'type': 'Ice'},
 'glare': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Tough',
           'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
           'name': 'Glare',
           'num': 137,
           'pp': 30,
           'priority': 0,
           'secondary': None,
           'status': 'par',
           'target': 'normal',
           'type': 'Normal',
           'zMove': {'boost': {'spd': 1}}},
 'glitzyglow': {'accuracy': 95,
                'basePower': 80,
                'category': 'Special',
                'contestType': 'Clever',
                'flags': {'protect': 1},
                'isNonstandard': 'LGPE',
                'name': 'Glitzy Glow',
                'num': 736,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'self': {'sideCondition': 'lightscreen'},
                'target': 'normal',
                'type': 'Psychic'},
 'gmaxbefuddle': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Butterfree',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Befuddle',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.foes(); _i < _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\tvar result = this.random(3);\n'
                                    '\t\t\t\t\tif (result === 0) {\n'
                                    "\t\t\t\t\t\tpokemon.trySetStatus('slp', "
                                    'source);\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t\telse if (result === 1) {\n'
                                    "\t\t\t\t\t\tpokemon.trySetStatus('par', "
                                    'source);\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t\telse {\n'
                                    "\t\t\t\t\t\tpokemon.trySetStatus('psn', "
                                    'source);\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Bug'},
 'gmaxcannonade': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'condition': {'duration': 4,
                                 'onResidual': 'function (target) {\n'
                                               '\t\t\t\tif '
                                               "(!target.hasType('Water'))\n"
                                               '\t\t\t\t\t'
                                               'this.damage(target.baseMaxhp / '
                                               '6, target);\n'
                                               '\t\t\t}',
                                 'onResidualOrder': 5,
                                 'onResidualSubOrder': 1,
                                 'onSideEnd': 'function (targetSide) {\n'
                                              "\t\t\t\tthis.add('-sideend', "
                                              "targetSide, 'G-Max "
                                              "Cannonade');\n"
                                              '\t\t\t}',
                                 'onSideResidualOrder': 26,
                                 'onSideResidualSubOrder': 11,
                                 'onSideStart': 'function (targetSide) {\n'
                                                '\t\t\t\t'
                                                "this.add('-sidestart', "
                                                "targetSide, 'G-Max "
                                                "Cannonade');\n"
                                                '\t\t\t}'},
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Blastoise',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Cannonade',
                   'num': 1000,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.side.foeSidesWithConditions(); _i '
                                     '< _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar side = _a[_i];\n'
                                     '\t\t\t\t\t'
                                     "side.addSideCondition('gmaxcannonade');\n"
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Water'},
 'gmaxcentiferno': {'accuracy': True,
                    'basePower': 10,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'isMax': 'Centiskorch',
                    'isNonstandard': 'Gigantamax',
                    'name': 'G-Max Centiferno',
                    'num': 1000,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'self': {'onHit': 'function (source) {\n'
                                      '\t\t\t\tfor (var _i = 0, _a = '
                                      'source.foes(); _i < _a.length; _i++) {\n'
                                      '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                      '\t\t\t\t\t'
                                      "pokemon.addVolatile('partiallytrapped', "
                                      "source, this.dex.getActiveMove('G-Max "
                                      "Centiferno'));\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t}'},
                    'target': 'adjacentFoe',
                    'type': 'Fire'},
 'gmaxchistrike': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'condition': {'noCopy': True,
                                 'onModifyCritRatio': 'function (critRatio) {\n'
                                                      '\t\t\t\treturn '
                                                      'critRatio + '
                                                      'this.effectState.layers;\n'
                                                      '\t\t\t}',
                                 'onRestart': 'function (target, source, '
                                              'effect) {\n'
                                              '\t\t\t\tif '
                                              '(this.effectState.layers >= 3)\n'
                                              '\t\t\t\t\treturn false;\n'
                                              '\t\t\t\t'
                                              'this.effectState.layers++;\n'
                                              "\t\t\t\tif (!['imposter', "
                                              "'psychup', "
                                              "'transform'].includes(effect "
                                              '=== null || effect === void 0 ? '
                                              'void 0 : effect.id)) {\n'
                                              "\t\t\t\t\tthis.add('-start', "
                                              "target, 'move: G-Max Chi "
                                              "Strike');\n"
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                                 'onStart': 'function (target, source, effect) '
                                            '{\n'
                                            '\t\t\t\tthis.effectState.layers = '
                                            '1;\n'
                                            "\t\t\t\tif (!['imposter', "
                                            "'psychup', "
                                            "'transform'].includes(effect === "
                                            'null || effect === void 0 ? void '
                                            '0 : effect.id)) {\n'
                                            "\t\t\t\t\tthis.add('-start', "
                                            "target, 'move: G-Max Chi "
                                            "Strike');\n"
                                            '\t\t\t\t}\n'
                                            '\t\t\t}'},
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Machamp',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Chi Strike',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.alliesAndSelf(); _i < _a.length; '
                                     '_i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\t'
                                     "pokemon.addVolatile('gmaxchistrike');\n"
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Fighting'},
 'gmaxcuddle': {'accuracy': True,
                'basePower': 10,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {},
                'isMax': 'Eevee',
                'isNonstandard': 'Gigantamax',
                'name': 'G-Max Cuddle',
                'num': 1000,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'onHit': 'function (source) {\n'
                                  '\t\t\t\tfor (var _i = 0, _a = '
                                  'source.foes(); _i < _a.length; _i++) {\n'
                                  '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                  "\t\t\t\t\tpokemon.addVolatile('attract');\n"
                                  '\t\t\t\t}\n'
                                  '\t\t\t}'},
                'target': 'adjacentFoe',
                'type': 'Normal'},
 'gmaxdepletion': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Duraludon',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Depletion',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.foes(); _i < _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\tvar move = pokemon.lastMove;\n'
                                     '\t\t\t\t\tif (!move || move.isZ)\n'
                                     '\t\t\t\t\t\tcontinue;\n'
                                     '\t\t\t\t\tif (move.isMax && '
                                     'move.baseMove)\n'
                                     '\t\t\t\t\t\tmove = '
                                     'this.dex.moves.get(move.baseMove);\n'
                                     '\t\t\t\t\tvar ppDeducted = '
                                     'pokemon.deductPP(move.id, 2);\n'
                                     '\t\t\t\t\tif (ppDeducted) {\n'
                                     '\t\t\t\t\t\tthis.add("-activate", '
                                     "pokemon, 'move: G-Max Depletion', "
                                     'move.name, ppDeducted);\n'
                                     "\t\t\t\t\t\t// Don't return here because "
                                     "returning early doesn't trigger\n"
                                     '\t\t\t\t\t\t// activation text for the '
                                     'second Pokemon in doubles\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Dragon'},
 'gmaxdrumsolo': {'accuracy': True,
                  'basePower': 160,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'ignoreAbility': True,
                  'isMax': 'Rillaboom',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Drum Solo',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'adjacentFoe',
                  'type': 'Grass'},
 'gmaxfinale': {'accuracy': True,
                'basePower': 10,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {},
                'isMax': 'Alcremie',
                'isNonstandard': 'Gigantamax',
                'name': 'G-Max Finale',
                'num': 1000,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'onHit': 'function (target, source, move) {\n'
                                  '\t\t\t\tfor (var _i = 0, _a = '
                                  'source.alliesAndSelf(); _i < _a.length; '
                                  '_i++) {\n'
                                  '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                  '\t\t\t\t\tthis.heal(pokemon.maxhp / 6, '
                                  'pokemon, source, move);\n'
                                  '\t\t\t\t}\n'
                                  '\t\t\t}'},
                'target': 'adjacentFoe',
                'type': 'Fairy'},
 'gmaxfireball': {'accuracy': True,
                  'basePower': 160,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'ignoreAbility': True,
                  'isMax': 'Cinderace',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Fireball',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'adjacentFoe',
                  'type': 'Fire'},
 'gmaxfoamburst': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Kingler',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Foam Burst',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.foes(); _i < _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\tthis.boost({ spe: -2 }, '
                                     'pokemon);\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Water'},
 'gmaxgoldrush': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Meowth',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Gold Rush',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.foes(); _i < _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\t'
                                    "pokemon.addVolatile('confusion');\n"
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Normal'},
 'gmaxgravitas': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Orbeetle',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Gravitas',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'self': {'pseudoWeather': 'gravity'},
                  'target': 'adjacentFoe',
                  'type': 'Psychic'},
 'gmaxhydrosnipe': {'accuracy': True,
                    'basePower': 160,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'ignoreAbility': True,
                    'isMax': 'Inteleon',
                    'isNonstandard': 'Gigantamax',
                    'name': 'G-Max Hydrosnipe',
                    'num': 1000,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'target': 'adjacentFoe',
                    'type': 'Water'},
 'gmaxmalodor': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': 'Garbodor',
                 'isNonstandard': 'Gigantamax',
                 'name': 'G-Max Malodor',
                 'num': 1000,
                 'pp': 5,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   '\t\t\t\tfor (var _i = 0, _a = '
                                   'source.foes(); _i < _a.length; _i++) {\n'
                                   '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                   "\t\t\t\t\tpokemon.trySetStatus('psn', "
                                   'source);\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Poison'},
 'gmaxmeltdown': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Melmetal',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Meltdown',
                  'num': 1000,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.foes(); _i < _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\tif '
                                    "(!pokemon.volatiles['dynamax'])\n"
                                    '\t\t\t\t\t\t'
                                    "pokemon.addVolatile('torment');\n"
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Steel'},
 'gmaxoneblow': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': 'Urshifu',
                 'isNonstandard': 'Gigantamax',
                 'name': 'G-Max One Blow',
                 'num': 1000,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'adjacentFoe',
                 'type': 'Dark'},
 'gmaxrapidflow': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Urshifu-Rapid-Strike',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Rapid Flow',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'target': 'adjacentFoe',
                   'type': 'Water'},
 'gmaxreplenish': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Snorlax',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Replenish',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tif (this.random(2) === 0)\n'
                                     '\t\t\t\t\treturn;\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.alliesAndSelf(); _i < _a.length; '
                                     '_i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\tif (pokemon.item)\n'
                                     '\t\t\t\t\t\tcontinue;\n'
                                     '\t\t\t\t\tif (pokemon.lastItem && '
                                     'this.dex.items.get(pokemon.lastItem).isBerry) '
                                     '{\n'
                                     '\t\t\t\t\t\tvar item = '
                                     'pokemon.lastItem;\n'
                                     "\t\t\t\t\t\tpokemon.lastItem = '';\n"
                                     "\t\t\t\t\t\tthis.add('-item', pokemon, "
                                     "this.dex.items.get(item), '[from] move: "
                                     "G-Max Replenish');\n"
                                     '\t\t\t\t\t\tpokemon.setItem(item);\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Normal'},
 'gmaxresonance': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Lapras',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Resonance',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'sideCondition': 'auroraveil'},
                   'target': 'adjacentFoe',
                   'type': 'Ice'},
 'gmaxsandblast': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Sandaconda',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Sandblast',
                   'num': 1000,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.foes(); _i < _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\t'
                                     "pokemon.addVolatile('partiallytrapped', "
                                     "source, this.dex.getActiveMove('G-Max "
                                     "Sandblast'));\n"
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Ground'},
 'gmaxsmite': {'accuracy': True,
               'basePower': 10,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {},
               'isMax': 'Hatterene',
               'isNonstandard': 'Gigantamax',
               'name': 'G-Max Smite',
               'num': 1000,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'self': {'onHit': 'function (source) {\n'
                                 '\t\t\t\tfor (var _i = 0, _a = source.foes(); '
                                 '_i < _a.length; _i++) {\n'
                                 '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                 "\t\t\t\t\tpokemon.addVolatile('confusion', "
                                 'source);\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}'},
               'target': 'adjacentFoe',
               'type': 'Fairy'},
 'gmaxsnooze': {'accuracy': True,
                'basePower': 10,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {},
                'isMax': 'Grimmsnarl',
                'isNonstandard': 'Gigantamax',
                'name': 'G-Max Snooze',
                'num': 1000,
                'onAfterSubDamage': 'function (damage, target) {\n'
                                    '\t\t\tif (target.status || '
                                    "!target.runStatusImmunity('slp'))\n"
                                    '\t\t\t\treturn;\n'
                                    '\t\t\tif (this.random(2) === 0)\n'
                                    '\t\t\t\treturn;\n'
                                    "\t\t\ttarget.addVolatile('yawn');\n"
                                    '\t\t}',
                'onHit': 'function (target) {\n'
                         '\t\t\tif (target.status || '
                         "!target.runStatusImmunity('slp'))\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\tif (this.random(2) === 0)\n'
                         '\t\t\t\treturn;\n'
                         "\t\t\ttarget.addVolatile('yawn');\n"
                         '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'adjacentFoe',
                'type': 'Dark'},
 'gmaxsteelsurge': {'accuracy': True,
                    'basePower': 10,
                    'category': 'Physical',
                    'condition': {'onSideStart': 'function (side) {\n'
                                                 '\t\t\t\t'
                                                 "this.add('-sidestart', side, "
                                                 "'move: G-Max Steelsurge');\n"
                                                 '\t\t\t}',
                                  'onSwitchIn': 'function (pokemon) {\n'
                                                '\t\t\t\tif '
                                                "(pokemon.hasItem('heavydutyboots'))\n"
                                                '\t\t\t\t\treturn;\n'
                                                '\t\t\t\t// Ice Face and '
                                                'Disguise correctly get typed '
                                                'damage from Stealth Rock\n'
                                                '\t\t\t\t// because Stealth '
                                                'Rock bypasses Substitute.\n'
                                                "\t\t\t\t// They don't get "
                                                'typed damage from Steelsurge '
                                                "because Steelsurge doesn't,\n"
                                                "\t\t\t\t// so we're going to "
                                                'test the damage of a '
                                                'Steel-type Stealth Rock '
                                                'instead.\n'
                                                '\t\t\t\tvar steelHazard = '
                                                "this.dex.getActiveMove('Stealth "
                                                "Rock');\n"
                                                '\t\t\t\tsteelHazard.type = '
                                                "'Steel';\n"
                                                '\t\t\t\tvar typeMod = '
                                                'this.clampIntRange(pokemon.runEffectiveness(steelHazard), '
                                                '-6, 6);\n'
                                                '\t\t\t\t'
                                                'this.damage(pokemon.maxhp * '
                                                'Math.pow(2, typeMod) / 8);\n'
                                                '\t\t\t}'},
                    'contestType': 'Cool',
                    'flags': {},
                    'isMax': 'Copperajah',
                    'isNonstandard': 'Gigantamax',
                    'name': 'G-Max Steelsurge',
                    'num': 1000,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'self': {'onHit': 'function (source) {\n'
                                      '\t\t\t\tfor (var _i = 0, _a = '
                                      'source.side.foeSidesWithConditions(); '
                                      '_i < _a.length; _i++) {\n'
                                      '\t\t\t\t\tvar side = _a[_i];\n'
                                      '\t\t\t\t\t'
                                      "side.addSideCondition('gmaxsteelsurge');\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t}'},
                    'target': 'adjacentFoe',
                    'type': 'Steel'},
 'gmaxstonesurge': {'accuracy': True,
                    'basePower': 10,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'isMax': 'Drednaw',
                    'isNonstandard': 'Gigantamax',
                    'name': 'G-Max Stonesurge',
                    'num': 1000,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'self': {'onHit': 'function (source) {\n'
                                      '\t\t\t\tfor (var _i = 0, _a = '
                                      'source.side.foeSidesWithConditions(); '
                                      '_i < _a.length; _i++) {\n'
                                      '\t\t\t\t\tvar side = _a[_i];\n'
                                      '\t\t\t\t\t'
                                      "side.addSideCondition('stealthrock');\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t}'},
                    'target': 'adjacentFoe',
                    'type': 'Water'},
 'gmaxstunshock': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Toxtricity',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Stun Shock',
                   'num': 1000,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.foes(); _i < _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\tvar result = this.random(2);\n'
                                     '\t\t\t\t\tif (result === 0) {\n'
                                     "\t\t\t\t\t\tpokemon.trySetStatus('par', "
                                     'source);\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t\telse {\n'
                                     "\t\t\t\t\t\tpokemon.trySetStatus('psn', "
                                     'source);\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Electric'},
 'gmaxsweetness': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Appletun',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Sweetness',
                   'num': 1000,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.side.pokemon; _i < _a.length; '
                                     '_i++) {\n'
                                     '\t\t\t\t\tvar ally = _a[_i];\n'
                                     '\t\t\t\t\tally.cureStatus();\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Grass'},
 'gmaxtartness': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Flapple',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Tartness',
                  'num': 1000,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.foes(); _i < _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\tthis.boost({ evasion: -1 }, '
                                    'pokemon);\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Grass'},
 'gmaxterror': {'accuracy': True,
                'basePower': 10,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {},
                'isMax': 'Gengar',
                'isNonstandard': 'Gigantamax',
                'name': 'G-Max Terror',
                'num': 1000,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'self': {'onHit': 'function (source) {\n'
                                  '\t\t\t\tfor (var _i = 0, _a = '
                                  'source.foes(); _i < _a.length; _i++) {\n'
                                  '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                  "\t\t\t\t\tpokemon.addVolatile('trapped', "
                                  "source, null, 'trapper');\n"
                                  '\t\t\t\t}\n'
                                  '\t\t\t}'},
                'target': 'adjacentFoe',
                'type': 'Ghost'},
 'gmaxvinelash': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'condition': {'duration': 4,
                                'onResidual': 'function (target) {\n'
                                              '\t\t\t\tif '
                                              "(!target.hasType('Grass'))\n"
                                              '\t\t\t\t\t'
                                              'this.damage(target.baseMaxhp / '
                                              '6, target);\n'
                                              '\t\t\t}',
                                'onResidualOrder': 5,
                                'onResidualSubOrder': 1,
                                'onSideEnd': 'function (targetSide) {\n'
                                             "\t\t\t\tthis.add('-sideend', "
                                             "targetSide, 'G-Max Vine Lash');\n"
                                             '\t\t\t}',
                                'onSideResidualOrder': 26,
                                'onSideResidualSubOrder': 11,
                                'onSideStart': 'function (targetSide) {\n'
                                               "\t\t\t\tthis.add('-sidestart', "
                                               "targetSide, 'G-Max Vine "
                                               "Lash');\n"
                                               '\t\t\t}'},
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Venusaur',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Vine Lash',
                  'num': 1000,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.side.foeSidesWithConditions(); _i '
                                    '< _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar side = _a[_i];\n'
                                    '\t\t\t\t\t'
                                    "side.addSideCondition('gmaxvinelash');\n"
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Grass'},
 'gmaxvolcalith': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'condition': {'duration': 4,
                                 'onResidual': 'function (target) {\n'
                                               '\t\t\t\tif '
                                               "(!target.hasType('Rock'))\n"
                                               '\t\t\t\t\t'
                                               'this.damage(target.baseMaxhp / '
                                               '6, target);\n'
                                               '\t\t\t}',
                                 'onResidualOrder': 5,
                                 'onResidualSubOrder': 1,
                                 'onSideEnd': 'function (targetSide) {\n'
                                              "\t\t\t\tthis.add('-sideend', "
                                              "targetSide, 'G-Max "
                                              "Volcalith');\n"
                                              '\t\t\t}',
                                 'onSideResidualOrder': 26,
                                 'onSideResidualSubOrder': 11,
                                 'onSideStart': 'function (targetSide) {\n'
                                                '\t\t\t\t'
                                                "this.add('-sidestart', "
                                                "targetSide, 'G-Max "
                                                "Volcalith');\n"
                                                '\t\t\t}'},
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Coalossal',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Volcalith',
                   'num': 1000,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.side.foeSidesWithConditions(); _i '
                                     '< _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar side = _a[_i];\n'
                                     '\t\t\t\t\t'
                                     "side.addSideCondition('gmaxvolcalith');\n"
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Rock'},
 'gmaxvoltcrash': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': 'Pikachu',
                   'isNonstandard': 'Gigantamax',
                   'name': 'G-Max Volt Crash',
                   'num': 1000,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.foes(); _i < _a.length; _i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     "\t\t\t\t\tpokemon.trySetStatus('par', "
                                     'source);\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Electric'},
 'gmaxwildfire': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'condition': {'duration': 4,
                                'onResidual': 'function (target) {\n'
                                              '\t\t\t\tif '
                                              "(!target.hasType('Fire'))\n"
                                              '\t\t\t\t\t'
                                              'this.damage(target.baseMaxhp / '
                                              '6, target);\n'
                                              '\t\t\t}',
                                'onResidualOrder': 5,
                                'onResidualSubOrder': 1,
                                'onSideEnd': 'function (targetSide) {\n'
                                             "\t\t\t\tthis.add('-sideend', "
                                             "targetSide, 'G-Max Wildfire');\n"
                                             '\t\t\t}',
                                'onSideResidualOrder': 26,
                                'onSideResidualSubOrder': 11,
                                'onSideStart': 'function (targetSide) {\n'
                                               "\t\t\t\tthis.add('-sidestart', "
                                               "targetSide, 'G-Max "
                                               "Wildfire');\n"
                                               '\t\t\t}'},
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Charizard',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Wildfire',
                  'num': 1000,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.side.foeSidesWithConditions(); _i '
                                    '< _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar side = _a[_i];\n'
                                    '\t\t\t\t\t'
                                    "side.addSideCondition('gmaxwildfire');\n"
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Fire'},
 'gmaxwindrage': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': 'Corviknight',
                  'isNonstandard': 'Gigantamax',
                  'name': 'G-Max Wind Rage',
                  'num': 1000,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tvar success = false;\n'
                                    '\t\t\t\tvar removeTarget = [\n'
                                    "\t\t\t\t\t'reflect', 'lightscreen', "
                                    "'auroraveil', 'safeguard', 'mist', "
                                    "'spikes', 'toxicspikes', 'stealthrock', "
                                    "'stickyweb',\n"
                                    '\t\t\t\t];\n'
                                    "\t\t\t\tvar removeAll = ['spikes', "
                                    "'toxicspikes', 'stealthrock', "
                                    "'stickyweb', 'gmaxsteelsurge'];\n"
                                    '\t\t\t\tfor (var _i = 0, removeTarget_2 = '
                                    'removeTarget; _i < removeTarget_2.length; '
                                    '_i++) {\n'
                                    '\t\t\t\t\tvar targetCondition = '
                                    'removeTarget_2[_i];\n'
                                    '\t\t\t\t\tif '
                                    '(source.side.foe.removeSideCondition(targetCondition)) '
                                    '{\n'
                                    '\t\t\t\t\t\tif '
                                    '(!removeAll.includes(targetCondition))\n'
                                    '\t\t\t\t\t\t\tcontinue;\n'
                                    "\t\t\t\t\t\tthis.add('-sideend', "
                                    'source.side.foe, '
                                    'this.dex.conditions.get(targetCondition).name, '
                                    "'[from] move: G-Max Wind Rage', '[of] ' + "
                                    'source);\n'
                                    '\t\t\t\t\t\tsuccess = true;\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t\tfor (var _a = 0, removeAll_2 = '
                                    'removeAll; _a < removeAll_2.length; _a++) '
                                    '{\n'
                                    '\t\t\t\t\tvar sideCondition = '
                                    'removeAll_2[_a];\n'
                                    '\t\t\t\t\tif '
                                    '(source.side.removeSideCondition(sideCondition)) '
                                    '{\n'
                                    "\t\t\t\t\t\tthis.add('-sideend', "
                                    'source.side, '
                                    'this.dex.conditions.get(sideCondition).name, '
                                    "'[from] move: G-Max Wind Rage', '[of] ' + "
                                    'source);\n'
                                    '\t\t\t\t\t\tsuccess = true;\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t\tthis.field.clearTerrain();\n'
                                    '\t\t\t\treturn success;\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Flying'},
 'grassknot': {'accuracy': 100,
               'basePower': 0,
               'basePowerCallback': 'function (pokemon, target) {\n'
                                    '\t\t\tvar targetWeight = '
                                    'target.getWeight();\n'
                                    '\t\t\tif (targetWeight >= 2000) {\n'
                                    "\t\t\t\tthis.debug('120 bp');\n"
                                    '\t\t\t\treturn 120;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (targetWeight >= 1000) {\n'
                                    "\t\t\t\tthis.debug('100 bp');\n"
                                    '\t\t\t\treturn 100;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (targetWeight >= 500) {\n'
                                    "\t\t\t\tthis.debug('80 bp');\n"
                                    '\t\t\t\treturn 80;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (targetWeight >= 250) {\n'
                                    "\t\t\t\tthis.debug('60 bp');\n"
                                    '\t\t\t\treturn 60;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (targetWeight >= 100) {\n'
                                    "\t\t\t\tthis.debug('40 bp');\n"
                                    '\t\t\t\treturn 40;\n'
                                    '\t\t\t}\n'
                                    "\t\t\tthis.debug('20 bp');\n"
                                    '\t\t\treturn 20;\n'
                                    '\t\t}',
               'category': 'Special',
               'contestType': 'Cute',
               'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Grass Knot',
               'num': 447,
               'onTryHit': 'function (target, source, move) {\n'
                           "\t\t\tif (target.volatiles['dynamax']) {\n"
                           "\t\t\t\tthis.add('-fail', source, 'move: Grass "
                           "Knot', '[from] Dynamax');\n"
                           "\t\t\t\tthis.attrLastMove('[still]');\n"
                           '\t\t\t\treturn null;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass',
               'zMove': {'basePower': 160}},
 'grasspledge': {'accuracy': 100,
                 'basePower': 80,
                 'basePowerCallback': 'function (target, source, move) {\n'
                                      "\t\t\tif (['waterpledge', "
                                      "'firepledge'].includes(move.sourceEffect)) "
                                      '{\n'
                                      "\t\t\t\tthis.add('-combine');\n"
                                      '\t\t\t\treturn 150;\n'
                                      '\t\t\t}\n'
                                      '\t\t\treturn 80;\n'
                                      '\t\t}',
                 'category': 'Special',
                 'condition': {'duration': 4,
                               'onModifySpe': 'function (spe, pokemon) {\n'
                                              '\t\t\t\treturn '
                                              'this.chainModify(0.25);\n'
                                              '\t\t\t}',
                               'onSideEnd': 'function (targetSide) {\n'
                                            "\t\t\t\tthis.add('-sideend', "
                                            "targetSide, 'Grass Pledge');\n"
                                            '\t\t\t}',
                               'onSideResidualOrder': 26,
                               'onSideResidualSubOrder': 9,
                               'onSideStart': 'function (targetSide) {\n'
                                              "\t\t\t\tthis.add('-sidestart', "
                                              "targetSide, 'Grass Pledge');\n"
                                              '\t\t\t}'},
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                 'name': 'Grass Pledge',
                 'num': 520,
                 'onModifyMove': 'function (move) {\n'
                                 '\t\t\tif (move.sourceEffect === '
                                 "'waterpledge') {\n"
                                 "\t\t\t\tmove.type = 'Grass';\n"
                                 '\t\t\t\tmove.forceSTAB = true;\n'
                                 "\t\t\t\tmove.sideCondition = 'grasspledge';\n"
                                 '\t\t\t}\n'
                                 '\t\t\tif (move.sourceEffect === '
                                 "'firepledge') {\n"
                                 "\t\t\t\tmove.type = 'Fire';\n"
                                 '\t\t\t\tmove.forceSTAB = true;\n'
                                 "\t\t\t\tmove.sideCondition = 'firepledge';\n"
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'onPrepareHit': 'function (target, source, move) {\n'
                                 '\t\t\tvar _a;\n'
                                 '\t\t\tfor (var _i = 0, _b = this.queue.list; '
                                 '_i < _b.length; _i++) {\n'
                                 '\t\t\t\tvar action = _b[_i];\n'
                                 '\t\t\t\tif (!action.move || !((_a = '
                                 'action.pokemon) === null || _a === void 0 ? '
                                 'void 0 : _a.isActive) ||\n'
                                 '\t\t\t\t\taction.pokemon.fainted || '
                                 'action.maxMove || action.zmove) {\n'
                                 '\t\t\t\t\tcontinue;\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t\tif (action.pokemon.isAlly(source) && '
                                 "['waterpledge', "
                                 "'firepledge'].includes(action.move.id)) {\n"
                                 '\t\t\t\t\t'
                                 'this.queue.prioritizeAction(action, move);\n'
                                 "\t\t\t\t\tthis.add('-waiting', source, "
                                 'action.pokemon);\n'
                                 '\t\t\t\t\treturn null;\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Grass'},
 'grasswhistle': {'accuracy': 55,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'authentic': 1,
                            'mirror': 1,
                            'protect': 1,
                            'reflectable': 1,
                            'sound': 1},
                  'isNonstandard': 'Past',
                  'name': 'Grass Whistle',
                  'num': 320,
                  'pp': 15,
                  'priority': 0,
                  'secondary': None,
                  'status': 'slp',
                  'target': 'normal',
                  'type': 'Grass',
                  'zMove': {'boost': {'spe': 1}}},
 'grassyglide': {'accuracy': 100,
                 'basePower': 70,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mystery': 1, 'protect': 1},
                 'name': 'Grassy Glide',
                 'num': 803,
                 'onModifyPriority': 'function (priority, source, target, '
                                     'move) {\n'
                                     '\t\t\tif '
                                     "(this.field.isTerrain('grassyterrain') "
                                     '&& source.isGrounded()) {\n'
                                     '\t\t\t\treturn priority + 1;\n'
                                     '\t\t\t}\n'
                                     '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Grass'},
 'grassyterrain': {'accuracy': True,
                   'basePower': 0,
                   'category': 'Status',
                   'condition': {'duration': 5,
                                 'durationCallback': 'function (source, '
                                                     'effect) {\n'
                                                     '\t\t\t\tif (source === '
                                                     'null || source === void '
                                                     '0 ? void 0 : '
                                                     "source.hasItem('terrainextender')) "
                                                     '{\n'
                                                     '\t\t\t\t\treturn 8;\n'
                                                     '\t\t\t\t}\n'
                                                     '\t\t\t\treturn 5;\n'
                                                     '\t\t\t}',
                                 'onBasePower': 'function (basePower, '
                                                'attacker, defender, move) {\n'
                                                '\t\t\t\tvar weakenedMoves = '
                                                "['earthquake', 'bulldoze', "
                                                "'magnitude'];\n"
                                                '\t\t\t\tif '
                                                '(weakenedMoves.includes(move.id) '
                                                '&& defender.isGrounded() && '
                                                '!defender.isSemiInvulnerable()) '
                                                '{\n'
                                                "\t\t\t\t\tthis.debug('move "
                                                'weakened by grassy '
                                                "terrain');\n"
                                                '\t\t\t\t\treturn '
                                                'this.chainModify(0.5);\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t\tif (move.type === '
                                                "'Grass' && "
                                                'attacker.isGrounded()) {\n'
                                                "\t\t\t\t\tthis.debug('grassy "
                                                "terrain boost');\n"
                                                '\t\t\t\t\treturn '
                                                'this.chainModify([5325, '
                                                '4096]);\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t}',
                                 'onBasePowerPriority': 6,
                                 'onFieldEnd': 'function () {\n'
                                               "\t\t\t\tthis.add('-fieldend', "
                                               "'move: Grassy Terrain');\n"
                                               '\t\t\t}',
                                 'onFieldResidualOrder': 27,
                                 'onFieldResidualSubOrder': 7,
                                 'onFieldStart': 'function (field, source, '
                                                 'effect) {\n'
                                                 '\t\t\t\tif ((effect === null '
                                                 '|| effect === void 0 ? void '
                                                 '0 : effect.effectType) === '
                                                 "'Ability') {\n"
                                                 '\t\t\t\t\t'
                                                 "this.add('-fieldstart', "
                                                 "'move: Grassy Terrain', "
                                                 "'[from] ability: ' + effect, "
                                                 "'[of] ' + source);\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\telse {\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-fieldstart', "
                                                 "'move: Grassy Terrain');\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t}',
                                 'onResidual': 'function (pokemon) {\n'
                                               '\t\t\t\tif '
                                               '(pokemon.isGrounded() && '
                                               '!pokemon.isSemiInvulnerable()) '
                                               '{\n'
                                               '\t\t\t\t\t'
                                               'this.heal(pokemon.baseMaxhp / '
                                               '16, pokemon, pokemon);\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t\telse {\n'
                                               '\t\t\t\t\tthis.debug("Pokemon '
                                               'semi-invuln or not grounded; '
                                               'Grassy Terrain skipped");\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                                 'onResidualOrder': 5,
                                 'onResidualSubOrder': 2},
                   'contestType': 'Beautiful',
                   'flags': {'nonsky': 1},
                   'name': 'Grassy Terrain',
                   'num': 580,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'all',
                   'terrain': 'grassyterrain',
                   'type': 'Grass',
                   'zMove': {'boost': {'def': 1}}},
 'gravapple': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Grav Apple',
               'num': 788,
               'onBasePower': 'function (basePower) {\n'
                              '\t\t\tif '
                              "(this.field.getPseudoWeather('gravity')) {\n"
                              '\t\t\t\treturn this.chainModify(1.5);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'def': -1}, 'chance': 100},
               'target': 'normal',
               'type': 'Grass'},
 'gravity': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 5,
                           'durationCallback': 'function (source, effect) {\n'
                                               '\t\t\t\tif (source === null || '
                                               'source === void 0 ? void 0 : '
                                               "source.hasAbility('persistent')) "
                                               '{\n'
                                               '\t\t\t\t\t'
                                               "this.add('-activate', source, "
                                               "'ability: Persistent', "
                                               'effect);\n'
                                               '\t\t\t\t\treturn 7;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t\treturn 5;\n'
                                               '\t\t\t}',
                           'onBeforeMove': 'function (pokemon, target, move) '
                                           '{\n'
                                           "\t\t\t\tif (move.flags['gravity'] "
                                           '&& !move.isZ) {\n'
                                           "\t\t\t\t\tthis.add('cant', "
                                           "pokemon, 'move: Gravity', move);\n"
                                           '\t\t\t\t\treturn false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                           'onBeforeMovePriority': 6,
                           'onDisableMove': 'function (pokemon) {\n'
                                            '\t\t\t\tfor (var _i = 0, _a = '
                                            'pokemon.moveSlots; _i < '
                                            '_a.length; _i++) {\n'
                                            '\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                            '\t\t\t\t\tif '
                                            "(this.dex.moves.get(moveSlot.id).flags['gravity']) "
                                            '{\n'
                                            '\t\t\t\t\t\t'
                                            'pokemon.disableMove(moveSlot.id);\n'
                                            '\t\t\t\t\t}\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}',
                           'onFieldEnd': 'function () {\n'
                                         "\t\t\t\tthis.add('-fieldend', 'move: "
                                         "Gravity');\n"
                                         '\t\t\t}',
                           'onFieldResidualOrder': 27,
                           'onFieldResidualSubOrder': 2,
                           'onFieldStart': 'function () {\n'
                                           "\t\t\t\tthis.add('-fieldstart', "
                                           "'move: Gravity');\n"
                                           '\t\t\t\tfor (var _i = 0, _a = '
                                           'this.getAllActive(); _i < '
                                           '_a.length; _i++) {\n'
                                           '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                           '\t\t\t\t\tvar applies = false;\n'
                                           '\t\t\t\t\tif '
                                           "(pokemon.removeVolatile('bounce') "
                                           "|| pokemon.removeVolatile('fly')) "
                                           '{\n'
                                           '\t\t\t\t\t\tapplies = true;\n'
                                           '\t\t\t\t\t\t'
                                           'this.queue.cancelMove(pokemon);\n'
                                           '\t\t\t\t\t\t'
                                           "pokemon.removeVolatile('twoturnmove');\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t\tif '
                                           "(pokemon.volatiles['skydrop']) {\n"
                                           '\t\t\t\t\t\tapplies = true;\n'
                                           '\t\t\t\t\t\t'
                                           'this.queue.cancelMove(pokemon);\n'
                                           '\t\t\t\t\t\tif '
                                           "(pokemon.volatiles['skydrop'].source) "
                                           '{\n'
                                           "\t\t\t\t\t\t\tthis.add('-end', "
                                           "pokemon.volatiles['twoturnmove'].source, "
                                           "'Sky Drop', '[interrupt]');\n"
                                           '\t\t\t\t\t\t}\n'
                                           '\t\t\t\t\t\t'
                                           "pokemon.removeVolatile('skydrop');\n"
                                           '\t\t\t\t\t\t'
                                           "pokemon.removeVolatile('twoturnmove');\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t\tif '
                                           "(pokemon.volatiles['magnetrise']) "
                                           '{\n'
                                           '\t\t\t\t\t\tapplies = true;\n'
                                           '\t\t\t\t\t\tdelete '
                                           "pokemon.volatiles['magnetrise'];\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t\tif '
                                           "(pokemon.volatiles['telekinesis']) "
                                           '{\n'
                                           '\t\t\t\t\t\tapplies = true;\n'
                                           '\t\t\t\t\t\tdelete '
                                           "pokemon.volatiles['telekinesis'];\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t\tif (applies)\n'
                                           "\t\t\t\t\t\tthis.add('-activate', "
                                           "pokemon, 'move: Gravity');\n"
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                           'onModifyAccuracy': 'function (accuracy) {\n'
                                               '\t\t\t\tif (typeof accuracy '
                                               "!== 'number')\n"
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\treturn '
                                               'this.chainModify([6840, '
                                               '4096]);\n'
                                               '\t\t\t}',
                           'onModifyMove': 'function (move, pokemon, target) '
                                           '{\n'
                                           "\t\t\t\tif (move.flags['gravity'] "
                                           '&& !move.isZ) {\n'
                                           "\t\t\t\t\tthis.add('cant', "
                                           "pokemon, 'move: Gravity', move);\n"
                                           '\t\t\t\t\treturn false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'nonsky': 1},
             'name': 'Gravity',
             'num': 356,
             'pp': 5,
             'priority': 0,
             'pseudoWeather': 'gravity',
             'secondary': None,
             'target': 'all',
             'type': 'Psychic',
             'zMove': {'boost': {'spa': 1}}},
 'growl': {'accuracy': 100,
           'basePower': 0,
           'boosts': {'atk': -1},
           'category': 'Status',
           'contestType': 'Cute',
           'flags': {'authentic': 1,
                     'mirror': 1,
                     'protect': 1,
                     'reflectable': 1,
                     'sound': 1},
           'name': 'Growl',
           'num': 45,
           'pp': 40,
           'priority': 0,
           'secondary': None,
           'target': 'allAdjacentFoes',
           'type': 'Normal',
           'zMove': {'boost': {'def': 1}}},
 'growth': {'accuracy': True,
            'basePower': 0,
            'boosts': {'atk': 1, 'spa': 1},
            'category': 'Status',
            'contestType': 'Beautiful',
            'flags': {'snatch': 1},
            'name': 'Growth',
            'num': 74,
            'onModifyMove': 'function (move, pokemon) {\n'
                            "\t\t\tif (['sunnyday', "
                            "'desolateland'].includes(pokemon.effectiveWeather()))\n"
                            '\t\t\t\tmove.boosts = { atk: 2, spa: 2 };\n'
                            '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Normal',
            'zMove': {'boost': {'spa': 1}}},
 'grudge': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'condition': {'onBeforeMove': 'function (pokemon) {\n'
                                          "\t\t\t\tthis.debug('removing Grudge "
                                          "before attack');\n"
                                          '\t\t\t\t'
                                          "pokemon.removeVolatile('grudge');\n"
                                          '\t\t\t}',
                          'onBeforeMovePriority': 100,
                          'onFaint': 'function (target, source, effect) {\n'
                                     '\t\t\t\tif (!source || source.fainted || '
                                     '!effect)\n'
                                     '\t\t\t\t\treturn;\n'
                                     "\t\t\t\tif (effect.effectType === 'Move' "
                                     '&& !effect.isFutureMove && '
                                     'source.lastMove) {\n'
                                     '\t\t\t\t\tvar move = source.lastMove;\n'
                                     '\t\t\t\t\tif (move.isMax && '
                                     'move.baseMove)\n'
                                     '\t\t\t\t\t\tmove = '
                                     'this.dex.moves.get(move.baseMove);\n'
                                     '\t\t\t\t\tfor (var _i = 0, _a = '
                                     'source.moveSlots; _i < _a.length; _i++) '
                                     '{\n'
                                     '\t\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                     '\t\t\t\t\t\tif (moveSlot.id === move.id) '
                                     '{\n'
                                     '\t\t\t\t\t\t\tmoveSlot.pp = 0;\n'
                                     "\t\t\t\t\t\t\tthis.add('-activate', "
                                     "source, 'move: Grudge', move.name);\n"
                                     '\t\t\t\t\t\t}\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}',
                          'onStart': 'function (pokemon) {\n'
                                     "\t\t\t\tthis.add('-singlemove', pokemon, "
                                     "'Grudge');\n"
                                     '\t\t\t}'},
            'contestType': 'Tough',
            'flags': {'authentic': 1},
            'name': 'Grudge',
            'num': 288,
            'pp': 5,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Ghost',
            'volatileStatus': 'grudge',
            'zMove': {'effect': 'redirect'}},
 'guardianofalola': {'accuracy': True,
                     'basePower': 0,
                     'category': 'Special',
                     'contestType': 'Tough',
                     'damageCallback': 'function (pokemon, target) {\n'
                                       '\t\t\tvar hp75 = '
                                       'Math.floor(target.getUndynamaxedHP() * '
                                       '3 / 4);\n'
                                       "\t\t\tif (target.volatiles['protect'] "
                                       "|| target.volatiles['banefulbunker'] "
                                       "|| target.volatiles['kingsshield'] ||\n"
                                       '\t\t\t\t'
                                       "target.volatiles['spikyshield'] || "
                                       "target.side.getSideCondition('matblock')) "
                                       '{\n'
                                       "\t\t\t\tthis.add('-zbroken', target);\n"
                                       '\t\t\t\treturn '
                                       'this.clampIntRange(Math.ceil(hp75 / 4 '
                                       '- 0.5), 1);\n'
                                       '\t\t\t}\n'
                                       '\t\t\treturn this.clampIntRange(hp75, '
                                       '1);\n'
                                       '\t\t}',
                     'flags': {},
                     'isNonstandard': 'Past',
                     'isZ': 'tapuniumz',
                     'name': 'Guardian of Alola',
                     'num': 698,
                     'pp': 1,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Fairy'},
 'guardsplit': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mystery': 1, 'protect': 1},
                'name': 'Guard Split',
                'num': 470,
                'onHit': 'function (target, source) {\n'
                         '\t\t\tvar newdef = '
                         'Math.floor((target.storedStats.def + '
                         'source.storedStats.def) / 2);\n'
                         '\t\t\ttarget.storedStats.def = newdef;\n'
                         '\t\t\tsource.storedStats.def = newdef;\n'
                         '\t\t\tvar newspd = '
                         'Math.floor((target.storedStats.spd + '
                         'source.storedStats.spd) / 2);\n'
                         '\t\t\ttarget.storedStats.spd = newspd;\n'
                         '\t\t\tsource.storedStats.spd = newspd;\n'
                         "\t\t\tthis.add('-activate', source, 'move: Guard "
                         "Split', '[of] ' + target);\n"
                         '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Psychic',
                'zMove': {'boost': {'spe': 1}}},
 'guardswap': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'protect': 1},
               'name': 'Guard Swap',
               'num': 385,
               'onHit': 'function (target, source) {\n'
                        '\t\t\tvar targetBoosts = {};\n'
                        '\t\t\tvar sourceBoosts = {};\n'
                        "\t\t\tvar defSpd = ['def', 'spd'];\n"
                        '\t\t\tfor (var _i = 0, defSpd_1 = defSpd; _i < '
                        'defSpd_1.length; _i++) {\n'
                        '\t\t\t\tvar stat = defSpd_1[_i];\n'
                        '\t\t\t\ttargetBoosts[stat] = target.boosts[stat];\n'
                        '\t\t\t\tsourceBoosts[stat] = source.boosts[stat];\n'
                        '\t\t\t}\n'
                        '\t\t\tsource.setBoost(targetBoosts);\n'
                        '\t\t\ttarget.setBoost(sourceBoosts);\n'
                        "\t\t\tthis.add('-swapboost', source, target, 'def, "
                        "spd', '[from] move: Guard Swap');\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic',
               'zMove': {'boost': {'spe': 1}}},
 'guillotine': {'accuracy': 30,
                'basePower': 0,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 130},
                'name': 'Guillotine',
                'num': 12,
                'ohko': True,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal',
                'zMove': {'basePower': 180}},
 'gunkshot': {'accuracy': 80,
              'basePower': 120,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Gunk Shot',
              'num': 441,
              'pp': 5,
              'priority': 0,
              'secondary': {'chance': 30, 'status': 'psn'},
              'target': 'normal',
              'type': 'Poison'},
 'gust': {'accuracy': 100,
          'basePower': 40,
          'category': 'Special',
          'contestType': 'Clever',
          'flags': {'distance': 1, 'mirror': 1, 'protect': 1},
          'name': 'Gust',
          'num': 16,
          'pp': 35,
          'priority': 0,
          'secondary': None,
          'target': 'any',
          'type': 'Flying'},
 'gyroball': {'accuracy': 100,
              'basePower': 0,
              'basePowerCallback': 'function (pokemon, target) {\n'
                                   '\t\t\tvar power = Math.floor(25 * '
                                   "target.getStat('spe') / "
                                   "pokemon.getStat('spe')) + 1;\n"
                                   '\t\t\tif (!isFinite(power))\n'
                                   '\t\t\t\tpower = 1;\n'
                                   '\t\t\tif (power > 150)\n'
                                   '\t\t\t\tpower = 150;\n'
                                   '\t\t\tthis.debug(power + " bp");\n'
                                   '\t\t\treturn power;\n'
                                   '\t\t}',
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'bullet': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
              'maxMove': {'basePower': 130},
              'name': 'Gyro Ball',
              'num': 360,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Steel',
              'zMove': {'basePower': 160}},
 'hail': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Beautiful',
          'flags': {},
          'name': 'Hail',
          'num': 258,
          'pp': 10,
          'priority': 0,
          'secondary': None,
          'target': 'all',
          'type': 'Ice',
          'weather': 'hail',
          'zMove': {'boost': {'spe': 1}}},
 'hammerarm': {'accuracy': 90,
               'basePower': 100,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
               'name': 'Hammer Arm',
               'num': 359,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'self': {'boosts': {'spe': -1}},
               'target': 'normal',
               'type': 'Fighting'},
 'happyhour': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {},
               'name': 'Happy Hour',
               'num': 603,
               'onTryHit': 'function (target, source) {\n'
                           "\t\t\tthis.add('-activate', target, 'move: Happy "
                           "Hour');\n"
                           '\t\t}',
               'pp': 30,
               'priority': 0,
               'secondary': None,
               'target': 'allySide',
               'type': 'Normal',
               'zMove': {'boost': {'atk': 1,
                                   'def': 1,
                                   'spa': 1,
                                   'spd': 1,
                                   'spe': 1}}},
 'harden': {'accuracy': True,
            'basePower': 0,
            'boosts': {'def': 1},
            'category': 'Status',
            'contestType': 'Tough',
            'flags': {'snatch': 1},
            'name': 'Harden',
            'num': 106,
            'pp': 30,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Normal',
            'zMove': {'boost': {'def': 1}}},
 'haze': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Beautiful',
          'flags': {'authentic': 1},
          'name': 'Haze',
          'num': 114,
          'onHitField': 'function () {\n'
                        "\t\t\tthis.add('-clearallboost');\n"
                        '\t\t\tfor (var _i = 0, _a = this.getAllActive(); _i < '
                        '_a.length; _i++) {\n'
                        '\t\t\t\tvar pokemon = _a[_i];\n'
                        '\t\t\t\tpokemon.clearBoosts();\n'
                        '\t\t\t}\n'
                        '\t\t}',
          'pp': 30,
          'priority': 0,
          'secondary': None,
          'target': 'all',
          'type': 'Ice',
          'zMove': {'effect': 'heal'}},
 'headbutt': {'accuracy': 100,
              'basePower': 70,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Headbutt',
              'num': 29,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
              'target': 'normal',
              'type': 'Normal'},
 'headcharge': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Head Charge',
                'num': 543,
                'pp': 15,
                'priority': 0,
                'recoil': [1, 4],
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'headsmash': {'accuracy': 80,
               'basePower': 150,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Head Smash',
               'num': 457,
               'pp': 5,
               'priority': 0,
               'recoil': [1, 2],
               'secondary': None,
               'target': 'normal',
               'type': 'Rock'},
 'healbell': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {'authentic': 1, 'distance': 1, 'snatch': 1, 'sound': 1},
              'name': 'Heal Bell',
              'num': 215,
              'onHit': 'function (pokemon, source) {\n'
                       "\t\t\tthis.add('-activate', source, 'move: Heal "
                       "Bell');\n"
                       '\t\t\tvar side = pokemon.side;\n'
                       '\t\t\tvar success = false;\n'
                       '\t\t\tfor (var _i = 0, _a = side.pokemon; _i < '
                       '_a.length; _i++) {\n'
                       '\t\t\t\tvar ally = _a[_i];\n'
                       '\t\t\t\tif (ally !== source && '
                       "ally.hasAbility('soundproof'))\n"
                       '\t\t\t\t\tcontinue;\n'
                       '\t\t\t\tif (ally.cureStatus())\n'
                       '\t\t\t\t\tsuccess = true;\n'
                       '\t\t\t}\n'
                       '\t\t\treturn success;\n'
                       '\t\t}',
              'pp': 5,
              'priority': 0,
              'target': 'allyTeam',
              'type': 'Normal',
              'zMove': {'effect': 'heal'}},
 'healblock': {'accuracy': 100,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 5,
                             'durationCallback': 'function (target, source, '
                                                 'effect) {\n'
                                                 '\t\t\t\tif (source === null '
                                                 '|| source === void 0 ? void '
                                                 '0 : '
                                                 "source.hasAbility('persistent')) "
                                                 '{\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "source, 'ability: "
                                                 "Persistent', effect);\n"
                                                 '\t\t\t\t\treturn 7;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\treturn 5;\n'
                                                 '\t\t\t}',
                             'onBeforeMove': 'function (pokemon, target, move) '
                                             '{\n'
                                             "\t\t\t\tif (move.flags['heal'] "
                                             '&& !move.isZ && !move.isMax) {\n'
                                             "\t\t\t\t\tthis.add('cant', "
                                             "pokemon, 'move: Heal Block', "
                                             'move);\n'
                                             '\t\t\t\t\treturn false;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                             'onBeforeMovePriority': 6,
                             'onDisableMove': 'function (pokemon) {\n'
                                              '\t\t\t\tfor (var _i = 0, _a = '
                                              'pokemon.moveSlots; _i < '
                                              '_a.length; _i++) {\n'
                                              '\t\t\t\t\tvar moveSlot = '
                                              '_a[_i];\n'
                                              '\t\t\t\t\tif '
                                              "(this.dex.moves.get(moveSlot.id).flags['heal']) "
                                              '{\n'
                                              '\t\t\t\t\t\t'
                                              'pokemon.disableMove(moveSlot.id);\n'
                                              '\t\t\t\t\t}\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                             'onEnd': 'function (pokemon) {\n'
                                      "\t\t\t\tthis.add('-end', pokemon, "
                                      "'move: Heal Block');\n"
                                      '\t\t\t}',
                             'onModifyMove': 'function (move, pokemon, target) '
                                             '{\n'
                                             "\t\t\t\tif (move.flags['heal'] "
                                             '&& !move.isZ && !move.isMax) {\n'
                                             "\t\t\t\t\tthis.add('cant', "
                                             "pokemon, 'move: Heal Block', "
                                             'move);\n'
                                             '\t\t\t\t\treturn false;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                             'onResidualOrder': 20,
                             'onRestart': 'function (target, source) {\n'
                                          "\t\t\t\tthis.add('-fail', target, "
                                          "'move: Heal Block'); // Succeeds to "
                                          'supress downstream messages\n'
                                          '\t\t\t\tif '
                                          '(!source.moveThisTurnResult) {\n'
                                          '\t\t\t\t\tsource.moveThisTurnResult '
                                          '= false;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t}',
                             'onStart': 'function (pokemon, source) {\n'
                                        "\t\t\t\tthis.add('-start', pokemon, "
                                        "'move: Heal Block');\n"
                                        '\t\t\t\tsource.moveThisTurnResult = '
                                        'true;\n'
                                        '\t\t\t}',
                             'onTryHeal': 'function (damage, target, source, '
                                          'effect) {\n'
                                          '\t\t\t\tif (((effect === null || '
                                          'effect === void 0 ? void 0 : '
                                          "effect.id) === 'zpower') || "
                                          'this.effectState.isZ)\n'
                                          '\t\t\t\t\treturn damage;\n'
                                          '\t\t\t\treturn false;\n'
                                          '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'isNonstandard': 'Past',
               'name': 'Heal Block',
               'num': 377,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Psychic',
               'volatileStatus': 'healblock',
               'zMove': {'boost': {'spa': 2}}},
 'healingwish': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'onSwap': 'function (target) {\n'
                                         '\t\t\t\tif (!target.fainted && '
                                         '(target.hp < target.maxhp || '
                                         'target.status)) {\n'
                                         '\t\t\t\t\t'
                                         'target.heal(target.maxhp);\n'
                                         "\t\t\t\t\ttarget.setStatus('');\n"
                                         "\t\t\t\t\tthis.add('-heal', target, "
                                         "target.getHealth, '[from] move: "
                                         "Healing Wish');\n"
                                         '\t\t\t\t\t'
                                         'target.side.removeSlotCondition(target, '
                                         "'healingwish');\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t}'},
                 'contestType': 'Beautiful',
                 'flags': {'heal': 1, 'snatch': 1},
                 'name': 'Healing Wish',
                 'num': 361,
                 'onTryHit': 'function (pokemon, target, move) {\n'
                             '\t\t\tif (!this.canSwitch(pokemon.side)) {\n'
                             '\t\t\t\tdelete move.selfdestruct;\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'selfdestruct': 'ifHit',
                 'slotCondition': 'healingwish',
                 'target': 'self',
                 'type': 'Psychic'},
 'healorder': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'heal': 1, 'snatch': 1},
               'heal': [1, 2],
               'isNonstandard': 'Past',
               'name': 'Heal Order',
               'num': 456,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Bug',
               'zMove': {'effect': 'clearnegativeboost'}},
 'healpulse': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Beautiful',
               'flags': {'distance': 1,
                         'heal': 1,
                         'mystery': 1,
                         'protect': 1,
                         'pulse': 1,
                         'reflectable': 1},
               'name': 'Heal Pulse',
               'num': 505,
               'onHit': 'function (target, source) {\n'
                        '\t\t\tvar success = false;\n'
                        "\t\t\tif (source.hasAbility('megalauncher')) {\n"
                        '\t\t\t\tsuccess = '
                        '!!this.heal(this.modify(target.baseMaxhp, 0.75));\n'
                        '\t\t\t}\n'
                        '\t\t\telse {\n'
                        '\t\t\t\tsuccess = '
                        '!!this.heal(Math.ceil(target.baseMaxhp * 0.5));\n'
                        '\t\t\t}\n'
                        '\t\t\tif (success && !target.isAlly(source)) {\n'
                        "\t\t\t\ttarget.staleness = 'external';\n"
                        '\t\t\t}\n'
                        '\t\t\treturn success;\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'any',
               'type': 'Psychic',
               'zMove': {'effect': 'clearnegativeboost'}},
 'heartstamp': {'accuracy': 100,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Cute',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Heart Stamp',
                'num': 531,
                'pp': 25,
                'priority': 0,
                'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                'target': 'normal',
                'type': 'Psychic'},
 'heartswap': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Heart Swap',
               'num': 391,
               'onHit': 'function (target, source) {\n'
                        '\t\t\tvar targetBoosts = {};\n'
                        '\t\t\tvar sourceBoosts = {};\n'
                        '\t\t\tvar i;\n'
                        '\t\t\tfor (i in target.boosts) {\n'
                        '\t\t\t\ttargetBoosts[i] = target.boosts[i];\n'
                        '\t\t\t\tsourceBoosts[i] = source.boosts[i];\n'
                        '\t\t\t}\n'
                        '\t\t\ttarget.setBoost(sourceBoosts);\n'
                        '\t\t\tsource.setBoost(targetBoosts);\n'
                        "\t\t\tthis.add('-swapboost', source, target, '[from] "
                        "move: Heart Swap');\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic',
               'zMove': {'effect': 'crit2'}},
 'heatcrash': {'accuracy': 100,
               'basePower': 0,
               'basePowerCallback': 'function (pokemon, target) {\n'
                                    '\t\t\tvar targetWeight = '
                                    'target.getWeight();\n'
                                    '\t\t\tvar pokemonWeight = '
                                    'pokemon.getWeight();\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '5) {\n'
                                    '\t\t\t\treturn 120;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '4) {\n'
                                    '\t\t\t\treturn 100;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '3) {\n'
                                    '\t\t\t\treturn 80;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '2) {\n'
                                    '\t\t\t\treturn 60;\n'
                                    '\t\t\t}\n'
                                    '\t\t\treturn 40;\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Heat Crash',
               'num': 535,
               'onTryHit': 'function (target, pokemon, move) {\n'
                           "\t\t\tif (target.volatiles['dynamax']) {\n"
                           "\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n"
                           "\t\t\t\tthis.attrLastMove('[still]');\n"
                           '\t\t\t\treturn null;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fire',
               'zMove': {'basePower': 160}},
 'heatwave': {'accuracy': 90,
              'basePower': 95,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Heat Wave',
              'num': 257,
              'pp': 10,
              'priority': 0,
              'secondary': {'chance': 10, 'status': 'brn'},
              'target': 'allAdjacentFoes',
              'type': 'Fire'},
 'heavyslam': {'accuracy': 100,
               'basePower': 0,
               'basePowerCallback': 'function (pokemon, target) {\n'
                                    '\t\t\tvar targetWeight = '
                                    'target.getWeight();\n'
                                    '\t\t\tvar pokemonWeight = '
                                    'pokemon.getWeight();\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '5) {\n'
                                    '\t\t\t\treturn 120;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '4) {\n'
                                    '\t\t\t\treturn 100;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '3) {\n'
                                    '\t\t\t\treturn 80;\n'
                                    '\t\t\t}\n'
                                    '\t\t\tif (pokemonWeight >= targetWeight * '
                                    '2) {\n'
                                    '\t\t\t\treturn 60;\n'
                                    '\t\t\t}\n'
                                    '\t\t\treturn 40;\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Heavy Slam',
               'num': 484,
               'onTryHit': 'function (target, pokemon, move) {\n'
                           "\t\t\tif (target.volatiles['dynamax']) {\n"
                           "\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n"
                           "\t\t\t\tthis.attrLastMove('[still]');\n"
                           '\t\t\t\treturn null;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Steel',
               'zMove': {'basePower': 160}},
 'helpinghand': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'duration': 1,
                               'onBasePower': 'function (basePower) {\n'
                                              "\t\t\t\tthis.debug('Boosting "
                                              "from Helping Hand: ' + "
                                              'this.effectState.multiplier);\n'
                                              '\t\t\t\treturn '
                                              'this.chainModify(this.effectState.multiplier);\n'
                                              '\t\t\t}',
                               'onBasePowerPriority': 10,
                               'onRestart': 'function (target, source) {\n'
                                            '\t\t\t\t'
                                            'this.effectState.multiplier *= '
                                            '1.5;\n'
                                            "\t\t\t\tthis.add('-singleturn', "
                                            "target, 'Helping Hand', '[of] ' + "
                                            'source);\n'
                                            '\t\t\t}',
                               'onStart': 'function (target, source) {\n'
                                          '\t\t\t\tthis.effectState.multiplier '
                                          '= 1.5;\n'
                                          "\t\t\t\tthis.add('-singleturn', "
                                          "target, 'Helping Hand', '[of] ' + "
                                          'source);\n'
                                          '\t\t\t}'},
                 'contestType': 'Clever',
                 'flags': {'authentic': 1},
                 'name': 'Helping Hand',
                 'num': 270,
                 'onTryHit': 'function (target) {\n'
                             '\t\t\tif (!target.newlySwitched && '
                             '!this.queue.willMove(target))\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t}',
                 'pp': 20,
                 'priority': 5,
                 'secondary': None,
                 'target': 'adjacentAlly',
                 'type': 'Normal',
                 'volatileStatus': 'helpinghand',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'hex': {'accuracy': 100,
         'basePower': 65,
         'basePowerCallback': 'function (pokemon, target, move) {\n'
                              '\t\t\tif (target.status || '
                              "target.hasAbility('comatose'))\n"
                              '\t\t\t\treturn move.basePower * 2;\n'
                              '\t\t\treturn move.basePower;\n'
                              '\t\t}',
         'category': 'Special',
         'contestType': 'Clever',
         'flags': {'mirror': 1, 'protect': 1},
         'name': 'Hex',
         'num': 506,
         'pp': 10,
         'priority': 0,
         'secondary': None,
         'target': 'normal',
         'type': 'Ghost',
         'zMove': {'basePower': 160}},
 'hiddenpower': {'accuracy': 100,
                 'basePower': 60,
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Hidden Power',
                 'num': 237,
                 'onModifyType': 'function (move, pokemon) {\n'
                                 "\t\t\tmove.type = pokemon.hpType || 'Dark';\n"
                                 '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'hiddenpowerbug': {'accuracy': 100,
                    'basePower': 60,
                    'category': 'Special',
                    'contestType': 'Clever',
                    'flags': {'mirror': 1, 'protect': 1},
                    'isNonstandard': 'Past',
                    'name': 'Hidden Power Bug',
                    'num': 237,
                    'pp': 15,
                    'priority': 0,
                    'realMove': 'Hidden Power',
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Bug'},
 'hiddenpowerdark': {'accuracy': 100,
                     'basePower': 60,
                     'category': 'Special',
                     'contestType': 'Clever',
                     'flags': {'mirror': 1, 'protect': 1},
                     'isNonstandard': 'Past',
                     'name': 'Hidden Power Dark',
                     'num': 237,
                     'pp': 15,
                     'priority': 0,
                     'realMove': 'Hidden Power',
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Dark'},
 'hiddenpowerdragon': {'accuracy': 100,
                       'basePower': 60,
                       'category': 'Special',
                       'contestType': 'Clever',
                       'flags': {'mirror': 1, 'protect': 1},
                       'isNonstandard': 'Past',
                       'name': 'Hidden Power Dragon',
                       'num': 237,
                       'pp': 15,
                       'priority': 0,
                       'realMove': 'Hidden Power',
                       'secondary': None,
                       'target': 'normal',
                       'type': 'Dragon'},
 'hiddenpowerelectric': {'accuracy': 100,
                         'basePower': 60,
                         'category': 'Special',
                         'contestType': 'Clever',
                         'flags': {'mirror': 1, 'protect': 1},
                         'isNonstandard': 'Past',
                         'name': 'Hidden Power Electric',
                         'num': 237,
                         'pp': 15,
                         'priority': 0,
                         'realMove': 'Hidden Power',
                         'secondary': None,
                         'target': 'normal',
                         'type': 'Electric'},
 'hiddenpowerfighting': {'accuracy': 100,
                         'basePower': 60,
                         'category': 'Special',
                         'contestType': 'Clever',
                         'flags': {'mirror': 1, 'protect': 1},
                         'isNonstandard': 'Past',
                         'name': 'Hidden Power Fighting',
                         'num': 237,
                         'pp': 15,
                         'priority': 0,
                         'realMove': 'Hidden Power',
                         'secondary': None,
                         'target': 'normal',
                         'type': 'Fighting'},
 'hiddenpowerfire': {'accuracy': 100,
                     'basePower': 60,
                     'category': 'Special',
                     'contestType': 'Clever',
                     'flags': {'mirror': 1, 'protect': 1},
                     'isNonstandard': 'Past',
                     'name': 'Hidden Power Fire',
                     'num': 237,
                     'pp': 15,
                     'priority': 0,
                     'realMove': 'Hidden Power',
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Fire'},
 'hiddenpowerflying': {'accuracy': 100,
                       'basePower': 60,
                       'category': 'Special',
                       'contestType': 'Clever',
                       'flags': {'mirror': 1, 'protect': 1},
                       'isNonstandard': 'Past',
                       'name': 'Hidden Power Flying',
                       'num': 237,
                       'pp': 15,
                       'priority': 0,
                       'realMove': 'Hidden Power',
                       'secondary': None,
                       'target': 'normal',
                       'type': 'Flying'},
 'hiddenpowerghost': {'accuracy': 100,
                      'basePower': 60,
                      'category': 'Special',
                      'contestType': 'Clever',
                      'flags': {'mirror': 1, 'protect': 1},
                      'isNonstandard': 'Past',
                      'name': 'Hidden Power Ghost',
                      'num': 237,
                      'pp': 15,
                      'priority': 0,
                      'realMove': 'Hidden Power',
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Ghost'},
 'hiddenpowergrass': {'accuracy': 100,
                      'basePower': 60,
                      'category': 'Special',
                      'contestType': 'Clever',
                      'flags': {'mirror': 1, 'protect': 1},
                      'isNonstandard': 'Past',
                      'name': 'Hidden Power Grass',
                      'num': 237,
                      'pp': 15,
                      'priority': 0,
                      'realMove': 'Hidden Power',
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Grass'},
 'hiddenpowerground': {'accuracy': 100,
                       'basePower': 60,
                       'category': 'Special',
                       'contestType': 'Clever',
                       'flags': {'mirror': 1, 'protect': 1},
                       'isNonstandard': 'Past',
                       'name': 'Hidden Power Ground',
                       'num': 237,
                       'pp': 15,
                       'priority': 0,
                       'realMove': 'Hidden Power',
                       'secondary': None,
                       'target': 'normal',
                       'type': 'Ground'},
 'hiddenpowerice': {'accuracy': 100,
                    'basePower': 60,
                    'category': 'Special',
                    'contestType': 'Clever',
                    'flags': {'mirror': 1, 'protect': 1},
                    'isNonstandard': 'Past',
                    'name': 'Hidden Power Ice',
                    'num': 237,
                    'pp': 15,
                    'priority': 0,
                    'realMove': 'Hidden Power',
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Ice'},
 'hiddenpowerpoison': {'accuracy': 100,
                       'basePower': 60,
                       'category': 'Special',
                       'contestType': 'Clever',
                       'flags': {'mirror': 1, 'protect': 1},
                       'isNonstandard': 'Past',
                       'name': 'Hidden Power Poison',
                       'num': 237,
                       'pp': 15,
                       'priority': 0,
                       'realMove': 'Hidden Power',
                       'secondary': None,
                       'target': 'normal',
                       'type': 'Poison'},
 'hiddenpowerpsychic': {'accuracy': 100,
                        'basePower': 60,
                        'category': 'Special',
                        'contestType': 'Clever',
                        'flags': {'mirror': 1, 'protect': 1},
                        'isNonstandard': 'Past',
                        'name': 'Hidden Power Psychic',
                        'num': 237,
                        'pp': 15,
                        'priority': 0,
                        'realMove': 'Hidden Power',
                        'secondary': None,
                        'target': 'normal',
                        'type': 'Psychic'},
 'hiddenpowerrock': {'accuracy': 100,
                     'basePower': 60,
                     'category': 'Special',
                     'contestType': 'Clever',
                     'flags': {'mirror': 1, 'protect': 1},
                     'isNonstandard': 'Past',
                     'name': 'Hidden Power Rock',
                     'num': 237,
                     'pp': 15,
                     'priority': 0,
                     'realMove': 'Hidden Power',
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Rock'},
 'hiddenpowersteel': {'accuracy': 100,
                      'basePower': 60,
                      'category': 'Special',
                      'contestType': 'Clever',
                      'flags': {'mirror': 1, 'protect': 1},
                      'isNonstandard': 'Past',
                      'name': 'Hidden Power Steel',
                      'num': 237,
                      'pp': 15,
                      'priority': 0,
                      'realMove': 'Hidden Power',
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Steel'},
 'hiddenpowerwater': {'accuracy': 100,
                      'basePower': 60,
                      'category': 'Special',
                      'contestType': 'Clever',
                      'flags': {'mirror': 1, 'protect': 1},
                      'isNonstandard': 'Past',
                      'name': 'Hidden Power Water',
                      'num': 237,
                      'pp': 15,
                      'priority': 0,
                      'realMove': 'Hidden Power',
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Water'},
 'highhorsepower': {'accuracy': 95,
                    'basePower': 95,
                    'category': 'Physical',
                    'contestType': 'Tough',
                    'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                    'name': 'High Horsepower',
                    'num': 667,
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Ground'},
 'highjumpkick': {'accuracy': 90,
                  'basePower': 130,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {'contact': 1,
                            'gravity': 1,
                            'mirror': 1,
                            'protect': 1},
                  'hasCrashDamage': True,
                  'name': 'High Jump Kick',
                  'num': 136,
                  'onMoveFail': 'function (target, source, move) {\n'
                                '\t\t\tthis.damage(source.baseMaxhp / 2, '
                                "source, source, this.dex.conditions.get('High "
                                "Jump Kick'));\n"
                                '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Fighting'},
 'holdback': {'accuracy': 100,
              'basePower': 40,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Hold Back',
              'num': 610,
              'onDamage': 'function (damage, target, source, effect) {\n'
                          '\t\t\tif (damage >= target.hp)\n'
                          '\t\t\t\treturn target.hp - 1;\n'
                          '\t\t}',
              'onDamagePriority': -20,
              'pp': 40,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'holdhands': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'authentic': 1},
               'name': 'Hold Hands',
               'num': 607,
               'pp': 40,
               'priority': 0,
               'secondary': None,
               'target': 'adjacentAlly',
               'type': 'Normal',
               'zMove': {'boost': {'atk': 1,
                                   'def': 1,
                                   'spa': 1,
                                   'spd': 1,
                                   'spe': 1}}},
 'honeclaws': {'accuracy': True,
               'basePower': 0,
               'boosts': {'accuracy': 1, 'atk': 1},
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'snatch': 1},
               'name': 'Hone Claws',
               'num': 468,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Dark',
               'zMove': {'boost': {'atk': 1}}},
 'hornattack': {'accuracy': 100,
                'basePower': 65,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Horn Attack',
                'num': 30,
                'pp': 25,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'horndrill': {'accuracy': 30,
               'basePower': 0,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Horn Drill',
               'num': 32,
               'ohko': True,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'basePower': 180}},
 'hornleech': {'accuracy': 100,
               'basePower': 75,
               'category': 'Physical',
               'contestType': 'Tough',
               'drain': [1, 2],
               'flags': {'contact': 1, 'heal': 1, 'mirror': 1, 'protect': 1},
               'name': 'Horn Leech',
               'num': 532,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'howl': {'accuracy': True,
          'basePower': 0,
          'boosts': {'atk': 1},
          'category': 'Status',
          'contestType': 'Cool',
          'flags': {'snatch': 1, 'sound': 1},
          'name': 'Howl',
          'num': 336,
          'pp': 40,
          'priority': 0,
          'secondary': None,
          'target': 'allies',
          'type': 'Normal',
          'zMove': {'boost': {'atk': 1}}},
 'hurricane': {'accuracy': 70,
               'basePower': 110,
               'category': 'Special',
               'contestType': 'Tough',
               'flags': {'distance': 1, 'mirror': 1, 'protect': 1},
               'name': 'Hurricane',
               'num': 542,
               'onModifyMove': 'function (move, pokemon, target) {\n'
                               '\t\t\tswitch (target === null || target === '
                               'void 0 ? void 0 : target.effectiveWeather()) '
                               '{\n'
                               "\t\t\t\tcase 'raindance':\n"
                               "\t\t\t\tcase 'primordialsea':\n"
                               '\t\t\t\t\tmove.accuracy = true;\n'
                               '\t\t\t\t\tbreak;\n'
                               "\t\t\t\tcase 'sunnyday':\n"
                               "\t\t\t\tcase 'desolateland':\n"
                               '\t\t\t\t\tmove.accuracy = 50;\n'
                               '\t\t\t\t\tbreak;\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 30, 'volatileStatus': 'confusion'},
               'target': 'any',
               'type': 'Flying'},
 'hydrocannon': {'accuracy': 90,
                 'basePower': 150,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
                 'name': 'Hydro Cannon',
                 'num': 308,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'volatileStatus': 'mustrecharge'},
                 'target': 'normal',
                 'type': 'Water'},
 'hydropump': {'accuracy': 80,
               'basePower': 110,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Hydro Pump',
               'num': 56,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Water'},
 'hydrovortex': {'accuracy': True,
                 'basePower': 1,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isNonstandard': 'Past',
                 'isZ': 'wateriumz',
                 'name': 'Hydro Vortex',
                 'num': 642,
                 'pp': 1,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Water'},
 'hyperbeam': {'accuracy': 90,
               'basePower': 150,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
               'name': 'Hyper Beam',
               'num': 63,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'self': {'volatileStatus': 'mustrecharge'},
               'target': 'normal',
               'type': 'Normal'},
 'hyperfang': {'accuracy': 90,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Hyper Fang',
               'num': 158,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 10, 'volatileStatus': 'flinch'},
               'target': 'normal',
               'type': 'Normal'},
 'hyperspacefury': {'accuracy': True,
                    'basePower': 100,
                    'breaksProtect': True,
                    'category': 'Physical',
                    'contestType': 'Tough',
                    'flags': {'authentic': 1, 'mirror': 1},
                    'isNonstandard': 'Past',
                    'name': 'Hyperspace Fury',
                    'num': 621,
                    'onTry': 'function (source) {\n'
                             '\t\t\tif (source.species.name === '
                             "'Hoopa-Unbound') {\n"
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             '\t\t\tthis.hint("Only a Pokemon whose form is '
                             'Hoopa Unbound can use this move.");\n'
                             "\t\t\tif (source.species.name === 'Hoopa') {\n"
                             "\t\t\t\tthis.attrLastMove('[still]');\n"
                             "\t\t\t\tthis.add('-fail', source, 'move: "
                             "Hyperspace Fury', '[forme]');\n"
                             '\t\t\t\treturn null;\n'
                             '\t\t\t}\n'
                             "\t\t\tthis.attrLastMove('[still]');\n"
                             "\t\t\tthis.add('-fail', source, 'move: "
                             "Hyperspace Fury');\n"
                             '\t\t\treturn null;\n'
                             '\t\t}',
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'self': {'boosts': {'def': -1}},
                    'target': 'normal',
                    'type': 'Dark'},
 'hyperspacehole': {'accuracy': True,
                    'basePower': 80,
                    'breaksProtect': True,
                    'category': 'Special',
                    'contestType': 'Clever',
                    'flags': {'authentic': 1, 'mirror': 1},
                    'isNonstandard': 'Past',
                    'name': 'Hyperspace Hole',
                    'num': 593,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Psychic'},
 'hypervoice': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Cool',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'protect': 1,
                          'sound': 1},
                'name': 'Hyper Voice',
                'num': 304,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Normal'},
 'hypnosis': {'accuracy': 60,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Clever',
              'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
              'name': 'Hypnosis',
              'num': 95,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'status': 'slp',
              'target': 'normal',
              'type': 'Psychic',
              'zMove': {'boost': {'spe': 1}}},
 'iceball': {'accuracy': 90,
             'basePower': 30,
             'basePowerCallback': 'function (pokemon, target, move) {\n'
                                  '\t\t\tvar bp = move.basePower;\n'
                                  "\t\t\tif (pokemon.volatiles['iceball'] && "
                                  "pokemon.volatiles['iceball'].hitCount) {\n"
                                  '\t\t\t\tbp *= Math.pow(2, '
                                  "pokemon.volatiles['iceball'].hitCount);\n"
                                  '\t\t\t}\n'
                                  "\t\t\tif (pokemon.status !== 'slp')\n"
                                  "\t\t\t\tpokemon.addVolatile('iceball');\n"
                                  "\t\t\tif (pokemon.volatiles['defensecurl']) "
                                  '{\n'
                                  '\t\t\t\tbp *= 2;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tthis.debug("Ice Ball bp: " + bp);\n'
                                  '\t\t\treturn bp;\n'
                                  '\t\t}',
             'category': 'Physical',
             'condition': {'duration': 2,
                           'onLockMove': 'iceball',
                           'onResidual': 'function (target) {\n'
                                         '\t\t\t\tif (target.lastMove && '
                                         "target.lastMove.id === 'struggle') "
                                         '{\n'
                                         "\t\t\t\t\t// don't lock\n"
                                         '\t\t\t\t\tdelete '
                                         "target.volatiles['iceball'];\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t}',
                           'onRestart': 'function () {\n'
                                        '\t\t\t\tthis.effectState.hitCount++;\n'
                                        '\t\t\t\tif (this.effectState.hitCount '
                                        '< 5) {\n'
                                        '\t\t\t\t\tthis.effectState.duration = '
                                        '2;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                           'onStart': 'function () {\n'
                                      '\t\t\t\tthis.effectState.hitCount = 1;\n'
                                      '\t\t\t}'},
             'contestType': 'Beautiful',
             'flags': {'bullet': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Ice Ball',
             'num': 301,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Ice'},
 'icebeam': {'accuracy': 100,
             'basePower': 90,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Ice Beam',
             'num': 58,
             'pp': 10,
             'priority': 0,
             'secondary': {'chance': 10, 'status': 'frz'},
             'target': 'normal',
             'type': 'Ice'},
 'iceburn': {'accuracy': 90,
             'basePower': 140,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'charge': 1, 'mirror': 1, 'protect': 1},
             'name': 'Ice Burn',
             'num': 554,
             'onTryMove': 'function (attacker, defender, move) {\n'
                          '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                          '\t\t\t\treturn;\n'
                          '\t\t\t}\n'
                          "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                          "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                          'defender, move)) {\n'
                          '\t\t\t\treturn;\n'
                          '\t\t\t}\n'
                          "\t\t\tattacker.addVolatile('twoturnmove', "
                          'defender);\n'
                          '\t\t\treturn null;\n'
                          '\t\t}',
             'pp': 5,
             'priority': 0,
             'secondary': {'chance': 30, 'status': 'brn'},
             'target': 'normal',
             'type': 'Ice'},
 'icefang': {'accuracy': 95,
             'basePower': 65,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Ice Fang',
             'num': 423,
             'pp': 15,
             'priority': 0,
             'secondaries': [{'chance': 10, 'status': 'frz'},
                             {'chance': 10, 'volatileStatus': 'flinch'}],
             'target': 'normal',
             'type': 'Ice'},
 'icehammer': {'accuracy': 90,
               'basePower': 100,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
               'isNonstandard': 'Past',
               'name': 'Ice Hammer',
               'num': 665,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'self': {'boosts': {'spe': -1}},
               'target': 'normal',
               'type': 'Ice'},
 'icepunch': {'accuracy': 100,
              'basePower': 75,
              'category': 'Physical',
              'contestType': 'Beautiful',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
              'name': 'Ice Punch',
              'num': 8,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 10, 'status': 'frz'},
              'target': 'normal',
              'type': 'Ice'},
 'iceshard': {'accuracy': 100,
              'basePower': 40,
              'category': 'Physical',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Ice Shard',
              'num': 420,
              'pp': 30,
              'priority': 1,
              'secondary': None,
              'target': 'normal',
              'type': 'Ice'},
 'iciclecrash': {'accuracy': 90,
                 'basePower': 85,
                 'category': 'Physical',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Icicle Crash',
                 'num': 556,
                 'pp': 10,
                 'priority': 0,
                 'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                 'target': 'normal',
                 'type': 'Ice'},
 'iciclespear': {'accuracy': 100,
                 'basePower': 25,
                 'category': 'Physical',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 130},
                 'multihit': [2, 5],
                 'name': 'Icicle Spear',
                 'num': 333,
                 'pp': 30,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ice',
                 'zMove': {'basePower': 140}},
 'icywind': {'accuracy': 95,
             'basePower': 55,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Icy Wind',
             'num': 196,
             'pp': 15,
             'priority': 0,
             'secondary': {'boosts': {'spe': -1}, 'chance': 100},
             'target': 'allAdjacentFoes',
             'type': 'Ice'},
 'imprison': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'noCopy': True,
                            'onFoeBeforeMove': 'function (attacker, defender, '
                                               'move) {\n'
                                               '\t\t\t\tif (move.id !== '
                                               "'struggle' && "
                                               'this.effectState.source.hasMove(move.id) '
                                               '&& !move.isZ && !move.isMax) '
                                               '{\n'
                                               "\t\t\t\t\tthis.add('cant', "
                                               "attacker, 'move: Imprison', "
                                               'move);\n'
                                               '\t\t\t\t\treturn false;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                            'onFoeBeforeMovePriority': 4,
                            'onFoeDisableMove': 'function (pokemon) {\n'
                                                '\t\t\t\tfor (var _i = 0, _a = '
                                                'this.effectState.source.moveSlots; '
                                                '_i < _a.length; _i++) {\n'
                                                '\t\t\t\t\tvar moveSlot = '
                                                '_a[_i];\n'
                                                '\t\t\t\t\tif (moveSlot.id === '
                                                "'struggle')\n"
                                                '\t\t\t\t\t\tcontinue;\n'
                                                '\t\t\t\t\t'
                                                'pokemon.disableMove(moveSlot.id, '
                                                "'hidden');\n"
                                                '\t\t\t\t}\n'
                                                '\t\t\t\tpokemon.maybeDisabled '
                                                '= true;\n'
                                                '\t\t\t}',
                            'onStart': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-start', target, "
                                       "'move: Imprison');\n"
                                       '\t\t\t}'},
              'contestType': 'Clever',
              'flags': {'authentic': 1, 'snatch': 1},
              'name': 'Imprison',
              'num': 286,
              'pp': 10,
              'pressureTarget': 'foeSide',
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Psychic',
              'volatileStatus': 'imprison',
              'zMove': {'boost': {'spd': 2}}},
 'incinerate': {'accuracy': 100,
                'basePower': 60,
                'category': 'Special',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Incinerate',
                'num': 510,
                'onHit': 'function (pokemon, source) {\n'
                         '\t\t\tvar item = pokemon.getItem();\n'
                         '\t\t\tif ((item.isBerry || item.isGem) && '
                         'pokemon.takeItem(source)) {\n'
                         "\t\t\t\tthis.add('-enditem', pokemon, item.name, "
                         "'[from] move: Incinerate');\n"
                         '\t\t\t}\n'
                         '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Fire'},
 'inferno': {'accuracy': 50,
             'basePower': 100,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Inferno',
             'num': 517,
             'pp': 5,
             'priority': 0,
             'secondary': {'chance': 100, 'status': 'brn'},
             'target': 'normal',
             'type': 'Fire'},
 'infernooverdrive': {'accuracy': True,
                      'basePower': 1,
                      'category': 'Physical',
                      'contestType': 'Cool',
                      'flags': {},
                      'isNonstandard': 'Past',
                      'isZ': 'firiumz',
                      'name': 'Inferno Overdrive',
                      'num': 640,
                      'pp': 1,
                      'priority': 0,
                      'secondary': None,
                      'target': 'normal',
                      'type': 'Fire'},
 'infestation': {'accuracy': 100,
                 'basePower': 20,
                 'category': 'Special',
                 'contestType': 'Cute',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Infestation',
                 'num': 611,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Bug',
                 'volatileStatus': 'partiallytrapped'},
 'ingrain': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'condition': {'onDragOut': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-activate', "
                                        "pokemon, 'move: Ingrain');\n"
                                        '\t\t\t\treturn null;\n'
                                        '\t\t\t}',
                           'onResidual': 'function (pokemon) {\n'
                                         '\t\t\t\tthis.heal(pokemon.baseMaxhp '
                                         '/ 16);\n'
                                         '\t\t\t}',
                           'onResidualOrder': 7,
                           'onStart': 'function (pokemon) {\n'
                                      "\t\t\t\tthis.add('-start', pokemon, "
                                      "'move: Ingrain');\n"
                                      '\t\t\t}',
                           'onTrapPokemon': 'function (pokemon) {\n'
                                            '\t\t\t\tpokemon.tryTrap();\n'
                                            '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'nonsky': 1, 'snatch': 1},
             'name': 'Ingrain',
             'num': 275,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Grass',
             'volatileStatus': 'ingrain',
             'zMove': {'boost': {'spd': 1}}},
 'instruct': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Clever',
              'flags': {'authentic': 1, 'mystery': 1, 'protect': 1},
              'name': 'Instruct',
              'num': 689,
              'onHit': 'function (target, source) {\n'
                       '\t\t\tif (!target.lastMove || '
                       "target.volatiles['dynamax'])\n"
                       '\t\t\t\treturn false;\n'
                       '\t\t\tvar lastMove = target.lastMove;\n'
                       '\t\t\tvar moveIndex = '
                       'target.moves.indexOf(lastMove.id);\n'
                       '\t\t\tvar noInstruct = [\n'
                       "\t\t\t\t'assist', 'beakblast', 'belch', 'bide', "
                       "'celebrate', 'copycat', 'dynamaxcannon', 'focuspunch', "
                       "'iceball', 'instruct', 'kingsshield', 'mefirst', "
                       "'metronome', 'mimic', 'mirrormove', 'naturepower', "
                       "'obstruct', 'outrage', 'petaldance', 'rollout', "
                       "'shelltrap', 'sketch', 'sleeptalk', 'struggle', "
                       "'thrash', 'transform', 'uproar',\n"
                       '\t\t\t];\n'
                       '\t\t\tif (noInstruct.includes(lastMove.id) || '
                       'lastMove.isZ || lastMove.isMax ||\n'
                       "\t\t\t\tlastMove.flags['charge'] || "
                       "lastMove.flags['recharge'] ||\n"
                       "\t\t\t\ttarget.volatiles['beakblast'] || "
                       "target.volatiles['focuspunch'] || "
                       "target.volatiles['shelltrap'] ||\n"
                       '\t\t\t\t(target.moveSlots[moveIndex] && '
                       'target.moveSlots[moveIndex].pp <= 0)) {\n'
                       '\t\t\t\treturn false;\n'
                       '\t\t\t}\n'
                       "\t\t\tthis.add('-singleturn', target, 'move: "
                       "Instruct', '[of] ' + source);\n"
                       '\t\t\tthis.actions.runMove(target.lastMove.id, target, '
                       'target.lastMoveTargetLoc);\n'
                       '\t\t}',
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Psychic',
              'zMove': {'boost': {'spa': 1}}},
 'iondeluge': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 1,
                             'onModifyType': 'function (move) {\n'
                                             '\t\t\t\tif (move.type === '
                                             "'Normal') {\n"
                                             '\t\t\t\t\tmove.type = '
                                             "'Electric';\n"
                                             '\t\t\t\t\tthis.debug(move.name + '
                                             '"\'s type changed to '
                                             'Electric");\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                             'onModifyTypePriority': -2,
                             'onStart': 'function (target, source, '
                                        'sourceEffect) {\n'
                                        "\t\t\t\tthis.add('-fieldactivate', "
                                        "'move: Ion Deluge');\n"
                                        '\t\t\t\tthis.hint("Normal-type moves '
                                        'become Electric-type after using " + '
                                        'sourceEffect + ".");\n'
                                        '\t\t\t}'},
               'contestType': 'Beautiful',
               'flags': {},
               'isNonstandard': 'Past',
               'name': 'Ion Deluge',
               'num': 569,
               'pp': 25,
               'priority': 1,
               'pseudoWeather': 'iondeluge',
               'secondary': None,
               'target': 'all',
               'type': 'Electric',
               'zMove': {'boost': {'spa': 1}}},
 'irondefense': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'def': 2},
                 'category': 'Status',
                 'contestType': 'Tough',
                 'flags': {'snatch': 1},
                 'name': 'Iron Defense',
                 'num': 334,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Steel',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'ironhead': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Iron Head',
              'num': 442,
              'pp': 15,
              'priority': 0,
              'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
              'target': 'normal',
              'type': 'Steel'},
 'irontail': {'accuracy': 75,
              'basePower': 100,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Iron Tail',
              'num': 231,
              'pp': 15,
              'priority': 0,
              'secondary': {'boosts': {'def': -1}, 'chance': 30},
              'target': 'normal',
              'type': 'Steel'},
 'jawlock': {'accuracy': 100,
             'basePower': 80,
             'category': 'Physical',
             'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Jaw Lock',
             'num': 746,
             'onHit': 'function (target, source, move) {\n'
                      "\t\t\tsource.addVolatile('trapped', target, move, "
                      "'trapper');\n"
                      "\t\t\ttarget.addVolatile('trapped', source, move, "
                      "'trapper');\n"
                      '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark'},
 'judgment': {'accuracy': 100,
              'basePower': 100,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'isNonstandard': 'Past',
              'name': 'Judgment',
              'num': 449,
              'onModifyType': 'function (move, pokemon) {\n'
                              '\t\t\tif (pokemon.ignoringItem())\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\tvar item = pokemon.getItem();\n'
                              '\t\t\tif (item.id && item.onPlate && '
                              '!item.zMove) {\n'
                              '\t\t\t\tmove.type = item.onPlate;\n'
                              '\t\t\t}\n'
                              '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'jumpkick': {'accuracy': 95,
              'basePower': 100,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'gravity': 1, 'mirror': 1, 'protect': 1},
              'hasCrashDamage': True,
              'isNonstandard': 'Past',
              'name': 'Jump Kick',
              'num': 26,
              'onMoveFail': 'function (target, source, move) {\n'
                            '\t\t\tthis.damage(source.baseMaxhp / 2, source, '
                            "source, this.dex.conditions.get('Jump Kick'));\n"
                            '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Fighting'},
 'junglehealing': {'accuracy': True,
                   'basePower': 0,
                   'category': 'Status',
                   'flags': {'authentic': 1, 'heal': 1, 'mystery': 1},
                   'name': 'Jungle Healing',
                   'num': 816,
                   'onHit': 'function (pokemon) {\n'
                            '\t\t\tvar success = '
                            '!!this.heal(this.modify(pokemon.maxhp, 0.25));\n'
                            '\t\t\treturn pokemon.cureStatus() || success;\n'
                            '\t\t}',
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'allies',
                   'type': 'Grass'},
 'karatechop': {'accuracy': 100,
                'basePower': 50,
                'category': 'Physical',
                'contestType': 'Tough',
                'critRatio': 2,
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Karate Chop',
                'num': 2,
                'pp': 25,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'kinesis': {'accuracy': 80,
             'basePower': 0,
             'boosts': {'accuracy': -1},
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
             'name': 'Kinesis',
             'num': 134,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Psychic',
             'zMove': {'boost': {'evasion': 1}}},
 'kingsshield': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'duration': 1,
                               'onHit': 'function (target, source, move) {\n'
                                        '\t\t\t\tif (move.isZOrMaxPowered && '
                                        'this.checkMoveMakesContact(move, '
                                        'source, target)) {\n'
                                        '\t\t\t\t\tthis.boost({ atk: -1 }, '
                                        'source, target, '
                                        'this.dex.getActiveMove("King\'s '
                                        'Shield"));\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                               'onStart': 'function (target) {\n'
                                          "\t\t\t\tthis.add('-singleturn', "
                                          "target, 'Protect');\n"
                                          '\t\t\t}',
                               'onTryHit': 'function (target, source, move) {\n'
                                           "\t\t\t\tif (!move.flags['protect'] "
                                           "|| move.category === 'Status') {\n"
                                           "\t\t\t\t\tif (['gmaxoneblow', "
                                           "'gmaxrapidflow'].includes(move.id))\n"
                                           '\t\t\t\t\t\treturn;\n'
                                           '\t\t\t\t\tif (move.isZ || '
                                           'move.isMax)\n'
                                           '\t\t\t\t\t\t'
                                           'target.getMoveHitData(move).zBrokeProtect '
                                           '= true;\n'
                                           '\t\t\t\t\treturn;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tif (move.smartTarget) {\n'
                                           '\t\t\t\t\tmove.smartTarget = '
                                           'false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\telse {\n'
                                           "\t\t\t\t\tthis.add('-activate', "
                                           "target, 'move: Protect');\n"
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tvar lockedmove = '
                                           "source.getVolatile('lockedmove');\n"
                                           '\t\t\t\tif (lockedmove) {\n'
                                           '\t\t\t\t\t// Outrage counter is '
                                           'reset\n'
                                           '\t\t\t\t\tif '
                                           "(source.volatiles['lockedmove'].duration "
                                           '=== 2) {\n'
                                           '\t\t\t\t\t\tdelete '
                                           "source.volatiles['lockedmove'];\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tif '
                                           '(this.checkMoveMakesContact(move, '
                                           'source, target)) {\n'
                                           '\t\t\t\t\tthis.boost({ atk: -1 }, '
                                           'source, target, '
                                           'this.dex.getActiveMove("King\'s '
                                           'Shield"));\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\treturn this.NOT_FAIL;\n'
                                           '\t\t\t}',
                               'onTryHitPriority': 3},
                 'contestType': 'Cool',
                 'flags': {},
                 'name': "King's Shield",
                 'num': 588,
                 'onHit': 'function (pokemon) {\n'
                          "\t\t\tpokemon.addVolatile('stall');\n"
                          '\t\t}',
                 'onPrepareHit': 'function (pokemon) {\n'
                                 '\t\t\treturn !!this.queue.willAct() && '
                                 "this.runEvent('StallMove', pokemon);\n"
                                 '\t\t}',
                 'pp': 10,
                 'priority': 4,
                 'secondary': None,
                 'stallingMove': True,
                 'target': 'self',
                 'type': 'Steel',
                 'volatileStatus': 'kingsshield',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'knockoff': {'accuracy': 100,
              'basePower': 65,
              'category': 'Physical',
              'contestType': 'Clever',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Knock Off',
              'num': 282,
              'onAfterHit': 'function (target, source) {\n'
                            '\t\t\tif (source.hp) {\n'
                            '\t\t\t\tvar item = target.takeItem();\n'
                            '\t\t\t\tif (item) {\n'
                            "\t\t\t\t\tthis.add('-enditem', target, item.name, "
                            "'[from] move: Knock Off', '[of] ' + source);\n"
                            '\t\t\t\t}\n'
                            '\t\t\t}\n'
                            '\t\t}',
              'onBasePower': 'function (basePower, source, target, move) {\n'
                             '\t\t\tvar item = target.getItem();\n'
                             "\t\t\tif (!this.singleEvent('TakeItem', item, "
                             'target.itemState, target, target, move, item))\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\tif (item.id) {\n'
                             '\t\t\t\treturn this.chainModify(1.5);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Dark'},
 'landswrath': {'accuracy': 100,
                'basePower': 90,
                'category': 'Physical',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                'name': "Land's Wrath",
                'num': 616,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Ground',
                'zMove': {'basePower': 185}},
 'laserfocus': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 2,
                              'onEnd': 'function (pokemon) {\n'
                                       "\t\t\t\tthis.add('-end', pokemon, "
                                       "'move: Laser Focus', '[silent]');\n"
                                       '\t\t\t}',
                              'onModifyCritRatio': 'function (critRatio) {\n'
                                                   '\t\t\t\treturn 5;\n'
                                                   '\t\t\t}',
                              'onRestart': 'function (pokemon) {\n'
                                           '\t\t\t\tthis.effectState.duration '
                                           '= 2;\n'
                                           "\t\t\t\tthis.add('-start', "
                                           "pokemon, 'move: Laser Focus');\n"
                                           '\t\t\t}',
                              'onStart': 'function (pokemon, source, effect) '
                                         '{\n'
                                         "\t\t\t\tif (effect && (['imposter', "
                                         "'psychup', "
                                         "'transform'].includes(effect.id))) "
                                         '{\n'
                                         "\t\t\t\t\tthis.add('-start', "
                                         "pokemon, 'move: Laser Focus', "
                                         "'[silent]');\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t\telse {\n'
                                         "\t\t\t\t\tthis.add('-start', "
                                         "pokemon, 'move: Laser Focus');\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t}'},
                'contestType': 'Cool',
                'flags': {'snatch': 1},
                'name': 'Laser Focus',
                'num': 673,
                'pp': 30,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'volatileStatus': 'laserfocus',
                'zMove': {'boost': {'atk': 1}}},
 'lashout': {'accuracy': 100,
             'basePower': 75,
             'category': 'Physical',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Lash Out',
             'num': 808,
             'onBasePower': 'function (basePower, source) {\n'
                            '\t\t\tif (source.statsLoweredThisTurn) {\n'
                            "\t\t\t\tthis.debug('lashout buff');\n"
                            '\t\t\t\treturn this.chainModify(2);\n'
                            '\t\t\t}\n'
                            '\t\t}',
             'pp': 5,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark'},
 'lastresort': {'accuracy': 100,
                'basePower': 140,
                'category': 'Physical',
                'contestType': 'Cute',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Last Resort',
                'num': 387,
                'onTry': 'function (source) {\n'
                         '\t\t\tif (source.moveSlots.length < 2)\n'
                         '\t\t\t\treturn false; // Last Resort fails unless '
                         'the user knows at least 2 moves\n'
                         '\t\t\tvar hasLastResort = false; // User must '
                         'actually have Last Resort for it to succeed\n'
                         '\t\t\tfor (var _i = 0, _a = source.moveSlots; _i < '
                         '_a.length; _i++) {\n'
                         '\t\t\t\tvar moveSlot = _a[_i];\n'
                         "\t\t\t\tif (moveSlot.id === 'lastresort') {\n"
                         '\t\t\t\t\thasLastResort = true;\n'
                         '\t\t\t\t\tcontinue;\n'
                         '\t\t\t\t}\n'
                         '\t\t\t\tif (!moveSlot.used)\n'
                         '\t\t\t\t\treturn false;\n'
                         '\t\t\t}\n'
                         '\t\t\treturn hasLastResort;\n'
                         '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal'},
 'lavaplume': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'contestType': 'Tough',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Lava Plume',
               'num': 436,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 30, 'status': 'brn'},
               'target': 'allAdjacent',
               'type': 'Fire'},
 'leafage': {'accuracy': 100,
             'basePower': 40,
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Leafage',
             'num': 670,
             'pp': 40,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Grass'},
 'leafblade': {'accuracy': 100,
               'basePower': 90,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Leaf Blade',
               'num': 348,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'leafstorm': {'accuracy': 90,
               'basePower': 130,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Leaf Storm',
               'num': 437,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'self': {'boosts': {'spa': -2}},
               'target': 'normal',
               'type': 'Grass'},
 'leaftornado': {'accuracy': 90,
                 'basePower': 65,
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Leaf Tornado',
                 'num': 536,
                 'pp': 10,
                 'priority': 0,
                 'secondary': {'boosts': {'accuracy': -1}, 'chance': 50},
                 'target': 'normal',
                 'type': 'Grass'},
 'leechlife': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Clever',
               'drain': [1, 2],
               'flags': {'contact': 1, 'heal': 1, 'mirror': 1, 'protect': 1},
               'name': 'Leech Life',
               'num': 141,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Bug'},
 'leechseed': {'accuracy': 90,
               'basePower': 0,
               'category': 'Status',
               'condition': {'onResidual': 'function (pokemon) {\n'
                                           '\t\t\t\tvar target = '
                                           "this.getAtSlot(pokemon.volatiles['leechseed'].sourceSlot);\n"
                                           '\t\t\t\tif (!target || '
                                           'target.fainted || target.hp <= 0) '
                                           '{\n'
                                           "\t\t\t\t\tthis.debug('Nothing to "
                                           "leech into');\n"
                                           '\t\t\t\t\treturn;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tvar damage = '
                                           'this.damage(pokemon.baseMaxhp / 8, '
                                           'pokemon, target);\n'
                                           '\t\t\t\tif (damage) {\n'
                                           '\t\t\t\t\tthis.heal(damage, '
                                           'target, pokemon);\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                             'onResidualOrder': 8,
                             'onStart': 'function (target) {\n'
                                        "\t\t\t\tthis.add('-start', target, "
                                        "'move: Leech Seed');\n"
                                        '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'name': 'Leech Seed',
               'num': 73,
               'onTryImmunity': 'function (target) {\n'
                                "\t\t\treturn !target.hasType('Grass');\n"
                                '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass',
               'volatileStatus': 'leechseed',
               'zMove': {'effect': 'clearnegativeboost'}},
 'leer': {'accuracy': 100,
          'basePower': 0,
          'boosts': {'def': -1},
          'category': 'Status',
          'contestType': 'Cool',
          'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
          'name': 'Leer',
          'num': 43,
          'pp': 30,
          'priority': 0,
          'secondary': None,
          'target': 'allAdjacentFoes',
          'type': 'Normal',
          'zMove': {'boost': {'atk': 1}}},
 'letssnuggleforever': {'accuracy': True,
                        'basePower': 190,
                        'category': 'Physical',
                        'contestType': 'Cool',
                        'flags': {'contact': 1},
                        'isNonstandard': 'Past',
                        'isZ': 'mimikiumz',
                        'name': "Let's Snuggle Forever",
                        'num': 726,
                        'pp': 1,
                        'priority': 0,
                        'secondary': None,
                        'target': 'normal',
                        'type': 'Fairy'},
 'lick': {'accuracy': 100,
          'basePower': 30,
          'category': 'Physical',
          'contestType': 'Cute',
          'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
          'name': 'Lick',
          'num': 122,
          'pp': 30,
          'priority': 0,
          'secondary': {'chance': 30, 'status': 'par'},
          'target': 'normal',
          'type': 'Ghost'},
 'lifedew': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'flags': {'authentic': 1, 'heal': 1, 'snatch': 1},
             'heal': [1, 4],
             'name': 'Life Dew',
             'num': 791,
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'allies',
             'type': 'Water'},
 'lightofruin': {'accuracy': 90,
                 'basePower': 140,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Light of Ruin',
                 'num': 617,
                 'pp': 5,
                 'priority': 0,
                 'recoil': [1, 2],
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fairy'},
 'lightscreen': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'duration': 5,
                               'durationCallback': 'function (target, source, '
                                                   'effect) {\n'
                                                   '\t\t\t\tif (source === '
                                                   'null || source === void 0 '
                                                   '? void 0 : '
                                                   "source.hasItem('lightclay')) "
                                                   '{\n'
                                                   '\t\t\t\t\treturn 8;\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t\treturn 5;\n'
                                                   '\t\t\t}',
                               'onAnyModifyDamage': 'function (damage, source, '
                                                    'target, move) {\n'
                                                    '\t\t\t\tif (target !== '
                                                    'source && '
                                                    'this.effectState.target.hasAlly(target) '
                                                    '&& this.getCategory(move) '
                                                    "=== 'Special') {\n"
                                                    '\t\t\t\t\tif '
                                                    '(!target.getMoveHitData(move).crit '
                                                    '&& !move.infiltrates) {\n'
                                                    '\t\t\t\t\t\t'
                                                    "this.debug('Light Screen "
                                                    "weaken');\n"
                                                    '\t\t\t\t\t\tif '
                                                    '(this.activePerHalf > 1)\n'
                                                    '\t\t\t\t\t\t\treturn '
                                                    'this.chainModify([2732, '
                                                    '4096]);\n'
                                                    '\t\t\t\t\t\treturn '
                                                    'this.chainModify(0.5);\n'
                                                    '\t\t\t\t\t}\n'
                                                    '\t\t\t\t}\n'
                                                    '\t\t\t}',
                               'onSideEnd': 'function (side) {\n'
                                            "\t\t\t\tthis.add('-sideend', "
                                            "side, 'move: Light Screen');\n"
                                            '\t\t\t}',
                               'onSideResidualOrder': 26,
                               'onSideResidualSubOrder': 2,
                               'onSideStart': 'function (side) {\n'
                                              "\t\t\t\tthis.add('-sidestart', "
                                              "side, 'move: Light Screen');\n"
                                              '\t\t\t}'},
                 'contestType': 'Beautiful',
                 'flags': {'snatch': 1},
                 'name': 'Light Screen',
                 'num': 113,
                 'pp': 30,
                 'priority': 0,
                 'secondary': None,
                 'sideCondition': 'lightscreen',
                 'target': 'allySide',
                 'type': 'Psychic',
                 'zMove': {'boost': {'spd': 1}}},
 'lightthatburnsthesky': {'accuracy': True,
                          'basePower': 200,
                          'category': 'Special',
                          'contestType': 'Cool',
                          'flags': {},
                          'ignoreAbility': True,
                          'isNonstandard': 'Past',
                          'isZ': 'ultranecroziumz',
                          'name': 'Light That Burns the Sky',
                          'num': 723,
                          'onModifyMove': 'function (move, pokemon) {\n'
                                          "\t\t\tif (pokemon.getStat('atk', "
                                          'false, true) > '
                                          "pokemon.getStat('spa', false, "
                                          'true))\n'
                                          '\t\t\t\tmove.category = '
                                          "'Physical';\n"
                                          '\t\t}',
                          'pp': 1,
                          'priority': 0,
                          'secondary': None,
                          'target': 'normal',
                          'type': 'Psychic'},
 'liquidation': {'accuracy': 100,
                 'basePower': 85,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Liquidation',
                 'num': 710,
                 'pp': 10,
                 'priority': 0,
                 'secondary': {'boosts': {'def': -1}, 'chance': 20},
                 'target': 'normal',
                 'type': 'Water'},
 'lockon': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'condition': {'duration': 2,
                          'noCopy': True,
                          'onSourceAccuracy': 'function (accuracy, target, '
                                              'source, move) {\n'
                                              '\t\t\t\tif (move && source === '
                                              'this.effectState.target && '
                                              'target === '
                                              'this.effectState.source)\n'
                                              '\t\t\t\t\treturn true;\n'
                                              '\t\t\t}',
                          'onSourceInvulnerability': 'function (target, '
                                                     'source, move) {\n'
                                                     '\t\t\t\tif (move && '
                                                     'source === '
                                                     'this.effectState.target '
                                                     '&& target === '
                                                     'this.effectState.source)\n'
                                                     '\t\t\t\t\treturn 0;\n'
                                                     '\t\t\t}',
                          'onSourceInvulnerabilityPriority': 1},
            'contestType': 'Clever',
            'flags': {'mirror': 1, 'protect': 1},
            'name': 'Lock-On',
            'num': 199,
            'onHit': 'function (target, source) {\n'
                     "\t\t\tsource.addVolatile('lockon', target);\n"
                     "\t\t\tthis.add('-activate', source, 'move: Lock-On', "
                     "'[of] ' + target);\n"
                     '\t\t}',
            'onTryHit': 'function (target, source) {\n'
                        "\t\t\tif (source.volatiles['lockon'])\n"
                        '\t\t\t\treturn false;\n'
                        '\t\t}',
            'pp': 5,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'zMove': {'boost': {'spe': 1}}},
 'lovelykiss': {'accuracy': 75,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                'name': 'Lovely Kiss',
                'num': 142,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'status': 'slp',
                'target': 'normal',
                'type': 'Normal',
                'zMove': {'boost': {'spe': 1}}},
 'lowkick': {'accuracy': 100,
             'basePower': 0,
             'basePowerCallback': 'function (pokemon, target) {\n'
                                  '\t\t\tvar targetWeight = '
                                  'target.getWeight();\n'
                                  '\t\t\tif (targetWeight >= 2000) {\n'
                                  '\t\t\t\treturn 120;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tif (targetWeight >= 1000) {\n'
                                  '\t\t\t\treturn 100;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tif (targetWeight >= 500) {\n'
                                  '\t\t\t\treturn 80;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tif (targetWeight >= 250) {\n'
                                  '\t\t\t\treturn 60;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tif (targetWeight >= 100) {\n'
                                  '\t\t\t\treturn 40;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn 20;\n'
                                  '\t\t}',
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Low Kick',
             'num': 67,
             'onTryHit': 'function (target, pokemon, move) {\n'
                         "\t\t\tif (target.volatiles['dynamax']) {\n"
                         "\t\t\t\tthis.add('-fail', pokemon, 'Dynamax');\n"
                         "\t\t\t\tthis.attrLastMove('[still]');\n"
                         '\t\t\t\treturn null;\n'
                         '\t\t\t}\n'
                         '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Fighting',
             'zMove': {'basePower': 160}},
 'lowsweep': {'accuracy': 100,
              'basePower': 65,
              'category': 'Physical',
              'contestType': 'Clever',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Low Sweep',
              'num': 490,
              'pp': 20,
              'priority': 0,
              'secondary': {'boosts': {'spe': -1}, 'chance': 100},
              'target': 'normal',
              'type': 'Fighting'},
 'luckychant': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 5,
                              'onCriticalHit': False,
                              'onSideEnd': 'function (side) {\n'
                                           "\t\t\t\tthis.add('-sideend', side, "
                                           "'move: Lucky Chant'); // "
                                           '"[side.name]\'s team\'s Lucky '
                                           'Chant wore off!"\n'
                                           '\t\t\t}',
                              'onSideResidualOrder': 26,
                              'onSideResidualSubOrder': 6,
                              'onSideStart': 'function (side) {\n'
                                             "\t\t\t\tthis.add('-sidestart', "
                                             "side, 'move: Lucky Chant'); // "
                                             '"The Lucky Chant shielded '
                                             "[side.name]'s team from critical "
                                             'hits!"\n'
                                             '\t\t\t}'},
                'contestType': 'Cute',
                'flags': {'snatch': 1},
                'isNonstandard': 'Past',
                'name': 'Lucky Chant',
                'num': 381,
                'pp': 30,
                'priority': 0,
                'secondary': None,
                'sideCondition': 'luckychant',
                'target': 'allySide',
                'type': 'Normal',
                'zMove': {'boost': {'evasion': 1}}},
 'lunardance': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'onSwap': 'function (target) {\n'
                                        '\t\t\t\tif (!target.fainted && '
                                        '(target.hp < target.maxhp ||\n'
                                        '\t\t\t\t\ttarget.status ||\n'
                                        '\t\t\t\t\t'
                                        'target.moveSlots.some(function '
                                        '(moveSlot) { return moveSlot.pp < '
                                        'moveSlot.maxpp; }))) {\n'
                                        '\t\t\t\t\ttarget.heal(target.maxhp);\n'
                                        "\t\t\t\t\ttarget.setStatus('');\n"
                                        '\t\t\t\t\tfor (var _i = 0, _a = '
                                        'target.moveSlots; _i < _a.length; '
                                        '_i++) {\n'
                                        '\t\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                        '\t\t\t\t\t\tmoveSlot.pp = '
                                        'moveSlot.maxpp;\n'
                                        '\t\t\t\t\t}\n'
                                        "\t\t\t\t\tthis.add('-heal', target, "
                                        "target.getHealth, '[from] move: Lunar "
                                        "Dance');\n"
                                        '\t\t\t\t\t'
                                        'target.side.removeSlotCondition(target, '
                                        "'lunardance');\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t}'},
                'contestType': 'Beautiful',
                'flags': {'dance': 1, 'heal': 1, 'snatch': 1},
                'name': 'Lunar Dance',
                'num': 461,
                'onTryHit': 'function (pokemon, target, move) {\n'
                            '\t\t\tif (!this.canSwitch(pokemon.side)) {\n'
                            '\t\t\t\tdelete move.selfdestruct;\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'selfdestruct': 'ifHit',
                'slotCondition': 'lunardance',
                'target': 'self',
                'type': 'Psychic'},
 'lunge': {'accuracy': 100,
           'basePower': 80,
           'category': 'Physical',
           'contestType': 'Cute',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Lunge',
           'num': 679,
           'pp': 15,
           'priority': 0,
           'secondary': {'boosts': {'atk': -1}, 'chance': 100},
           'target': 'normal',
           'type': 'Bug'},
 'lusterpurge': {'accuracy': 100,
                 'basePower': 70,
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Luster Purge',
                 'num': 295,
                 'pp': 5,
                 'priority': 0,
                 'secondary': {'boosts': {'spd': -1}, 'chance': 50},
                 'target': 'normal',
                 'type': 'Psychic'},
 'machpunch': {'accuracy': 100,
               'basePower': 40,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
               'name': 'Mach Punch',
               'num': 183,
               'pp': 30,
               'priority': 1,
               'secondary': None,
               'target': 'normal',
               'type': 'Fighting'},
 'magicalleaf': {'accuracy': True,
                 'basePower': 60,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Magical Leaf',
                 'num': 345,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Grass'},
 'magiccoat': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 1,
                             'onAllyTryHitSide': 'function (target, source, '
                                                 'move) {\n'
                                                 '\t\t\t\tif '
                                                 '(target.isAlly(source) || '
                                                 'move.hasBounced || '
                                                 "!move.flags['reflectable']) "
                                                 '{\n'
                                                 '\t\t\t\t\treturn;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tvar newMove = '
                                                 'this.dex.getActiveMove(move.id);\n'
                                                 '\t\t\t\tnewMove.hasBounced = '
                                                 'true;\n'
                                                 '\t\t\t\t'
                                                 'newMove.pranksterBoosted = '
                                                 'false;\n'
                                                 '\t\t\t\t'
                                                 'this.actions.useMove(newMove, '
                                                 'this.effectState.target, '
                                                 'source);\n'
                                                 '\t\t\t\treturn null;\n'
                                                 '\t\t\t}',
                             'onStart': 'function (target, source, effect) {\n'
                                        "\t\t\t\tthis.add('-singleturn', "
                                        "target, 'move: Magic Coat');\n"
                                        '\t\t\t\tif ((effect === null || '
                                        'effect === void 0 ? void 0 : '
                                        "effect.effectType) === 'Move') {\n"
                                        '\t\t\t\t\t'
                                        'this.effectState.pranksterBoosted = '
                                        'effect.pranksterBoosted;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                             'onTryHit': 'function (target, source, move) {\n'
                                         '\t\t\t\tif (target === source || '
                                         'move.hasBounced || '
                                         "!move.flags['reflectable']) {\n"
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t\tvar newMove = '
                                         'this.dex.getActiveMove(move.id);\n'
                                         '\t\t\t\tnewMove.hasBounced = true;\n'
                                         '\t\t\t\tnewMove.pranksterBoosted = '
                                         'this.effectState.pranksterBoosted;\n'
                                         '\t\t\t\t'
                                         'this.actions.useMove(newMove, '
                                         'target, source);\n'
                                         '\t\t\t\treturn null;\n'
                                         '\t\t\t}',
                             'onTryHitPriority': 2},
               'contestType': 'Beautiful',
               'flags': {},
               'name': 'Magic Coat',
               'num': 277,
               'pp': 15,
               'priority': 4,
               'secondary': None,
               'target': 'self',
               'type': 'Psychic',
               'volatileStatus': 'magiccoat',
               'zMove': {'boost': {'spd': 2}}},
 'magicpowder': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'flags': {'mirror': 1,
                           'mystery': 1,
                           'powder': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'name': 'Magic Powder',
                 'num': 750,
                 'onHit': 'function (target) {\n'
                          "\t\t\tif (target.getTypes().join() === 'Psychic' || "
                          "!target.setType('Psychic'))\n"
                          '\t\t\t\treturn false;\n'
                          "\t\t\tthis.add('-start', target, 'typechange', "
                          "'Psychic');\n"
                          '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Psychic'},
 'magicroom': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 5,
                             'durationCallback': 'function (source, effect) {\n'
                                                 '\t\t\t\tif (source === null '
                                                 '|| source === void 0 ? void '
                                                 '0 : '
                                                 "source.hasAbility('persistent')) "
                                                 '{\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "source, 'ability: "
                                                 "Persistent', effect);\n"
                                                 '\t\t\t\t\treturn 7;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\treturn 5;\n'
                                                 '\t\t\t}',
                             'onFieldEnd': 'function () {\n'
                                           "\t\t\t\tthis.add('-fieldend', "
                                           "'move: Magic Room', '[of] ' + "
                                           'this.effectState.source);\n'
                                           '\t\t\t}',
                             'onFieldResidualOrder': 27,
                             'onFieldResidualSubOrder': 6,
                             'onFieldRestart': 'function (target, source) {\n'
                                               '\t\t\t\t'
                                               "this.field.removePseudoWeather('magicroom');\n"
                                               '\t\t\t}',
                             'onFieldStart': 'function (target, source) {\n'
                                             "\t\t\t\tthis.add('-fieldstart', "
                                             "'move: Magic Room', '[of] ' + "
                                             'source);\n'
                                             '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1},
               'name': 'Magic Room',
               'num': 478,
               'pp': 10,
               'priority': 0,
               'pseudoWeather': 'magicroom',
               'secondary': None,
               'target': 'all',
               'type': 'Psychic',
               'zMove': {'boost': {'spd': 1}}},
 'magmastorm': {'accuracy': 75,
                'basePower': 100,
                'category': 'Special',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Magma Storm',
                'num': 463,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fire',
                'volatileStatus': 'partiallytrapped'},
 'magnetbomb': {'accuracy': True,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Magnet Bomb',
                'num': 443,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Steel'},
 'magneticflux': {'accuracy': True,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'authentic': 1, 'distance': 1, 'snatch': 1},
                  'name': 'Magnetic Flux',
                  'num': 602,
                  'onHitSide': 'function (side, source, move) {\n'
                               '\t\t\tvar _this = this;\n'
                               '\t\t\tvar targets = '
                               'side.allies().filter(function (ally) { return '
                               "(ally.hasAbility(['plus', 'minus']) &&\n"
                               "\t\t\t\t(!ally.volatiles['maxguard'] || "
                               "_this.runEvent('TryHit', ally, source, "
                               'move))); });\n'
                               '\t\t\tif (!targets.length)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\tvar didSomething = false;\n'
                               '\t\t\tfor (var _i = 0, targets_3 = targets; _i '
                               '< targets_3.length; _i++) {\n'
                               '\t\t\t\tvar target = targets_3[_i];\n'
                               '\t\t\t\tdidSomething = this.boost({ def: 1, '
                               'spd: 1 }, target, source, move, false, true) '
                               '|| didSomething;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn didSomething;\n'
                               '\t\t}',
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allySide',
                  'type': 'Electric',
                  'zMove': {'boost': {'spd': 1}}},
 'magnetrise': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 5,
                              'onEnd': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-end', target, "
                                       "'Magnet Rise');\n"
                                       '\t\t\t}',
                              'onImmunity': 'function (type) {\n'
                                            "\t\t\t\tif (type === 'Ground')\n"
                                            '\t\t\t\t\treturn false;\n'
                                            '\t\t\t}',
                              'onResidualOrder': 18,
                              'onStart': 'function (target) {\n'
                                         "\t\t\t\tthis.add('-start', target, "
                                         "'Magnet Rise');\n"
                                         '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'gravity': 1, 'snatch': 1},
                'name': 'Magnet Rise',
                'num': 393,
                'onTry': 'function (source, target, move) {\n'
                         "\t\t\tif (target.volatiles['smackdown'] || "
                         "target.volatiles['ingrain'])\n"
                         '\t\t\t\treturn false;\n'
                         '\t\t\t// Additional Gravity check for Z-move '
                         'variant\n'
                         "\t\t\tif (this.field.getPseudoWeather('Gravity')) {\n"
                         "\t\t\t\tthis.add('cant', source, 'move: Gravity', "
                         'move);\n'
                         '\t\t\t\treturn null;\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Electric',
                'volatileStatus': 'magnetrise',
                'zMove': {'boost': {'evasion': 1}}},
 'magnitude': {'accuracy': 100,
               'basePower': 0,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'maxMove': {'basePower': 140},
               'name': 'Magnitude',
               'num': 222,
               'onModifyMove': 'function (move, pokemon) {\n'
                               '\t\t\tvar i = this.random(100);\n'
                               '\t\t\tif (i < 5) {\n'
                               '\t\t\t\tmove.magnitude = 4;\n'
                               '\t\t\t\tmove.basePower = 10;\n'
                               '\t\t\t}\n'
                               '\t\t\telse if (i < 15) {\n'
                               '\t\t\t\tmove.magnitude = 5;\n'
                               '\t\t\t\tmove.basePower = 30;\n'
                               '\t\t\t}\n'
                               '\t\t\telse if (i < 35) {\n'
                               '\t\t\t\tmove.magnitude = 6;\n'
                               '\t\t\t\tmove.basePower = 50;\n'
                               '\t\t\t}\n'
                               '\t\t\telse if (i < 65) {\n'
                               '\t\t\t\tmove.magnitude = 7;\n'
                               '\t\t\t\tmove.basePower = 70;\n'
                               '\t\t\t}\n'
                               '\t\t\telse if (i < 85) {\n'
                               '\t\t\t\tmove.magnitude = 8;\n'
                               '\t\t\t\tmove.basePower = 90;\n'
                               '\t\t\t}\n'
                               '\t\t\telse if (i < 95) {\n'
                               '\t\t\t\tmove.magnitude = 9;\n'
                               '\t\t\t\tmove.basePower = 110;\n'
                               '\t\t\t}\n'
                               '\t\t\telse {\n'
                               '\t\t\t\tmove.magnitude = 10;\n'
                               '\t\t\t\tmove.basePower = 150;\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'onUseMoveMessage': 'function (pokemon, target, move) {\n'
                                   "\t\t\tthis.add('-activate', pokemon, "
                                   "'move: Magnitude', move.magnitude);\n"
                                   '\t\t}',
               'pp': 30,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacent',
               'type': 'Ground',
               'zMove': {'basePower': 140}},
 'maliciousmoonsault': {'accuracy': True,
                        'basePower': 180,
                        'category': 'Physical',
                        'contestType': 'Cool',
                        'flags': {'contact': 1},
                        'isNonstandard': 'Past',
                        'isZ': 'inciniumz',
                        'name': 'Malicious Moonsault',
                        'num': 696,
                        'pp': 1,
                        'priority': 0,
                        'secondary': None,
                        'target': 'normal',
                        'type': 'Dark'},
 'matblock': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 1,
                            'onSideStart': 'function (target, source) {\n'
                                           "\t\t\t\tthis.add('-singleturn', "
                                           "source, 'Mat Block');\n"
                                           '\t\t\t}',
                            'onTryHit': 'function (target, source, move) {\n'
                                        "\t\t\t\tif (!move.flags['protect']) "
                                        '{\n'
                                        "\t\t\t\t\tif (['gmaxoneblow', "
                                        "'gmaxrapidflow'].includes(move.id))\n"
                                        '\t\t\t\t\t\treturn;\n'
                                        '\t\t\t\t\tif (move.isZ || '
                                        'move.isMax)\n'
                                        '\t\t\t\t\t\t'
                                        'target.getMoveHitData(move).zBrokeProtect '
                                        '= true;\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif (move && (move.target === '
                                        "'self' || move.category === "
                                        "'Status'))\n"
                                        '\t\t\t\t\treturn;\n'
                                        "\t\t\t\tthis.add('-activate', target, "
                                        "'move: Mat Block', move.name);\n"
                                        '\t\t\t\tvar lockedmove = '
                                        "source.getVolatile('lockedmove');\n"
                                        '\t\t\t\tif (lockedmove) {\n'
                                        '\t\t\t\t\t// Outrage counter is '
                                        'reset\n'
                                        '\t\t\t\t\tif '
                                        "(source.volatiles['lockedmove'].duration "
                                        '=== 2) {\n'
                                        '\t\t\t\t\t\tdelete '
                                        "source.volatiles['lockedmove'];\n"
                                        '\t\t\t\t\t}\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\treturn this.NOT_FAIL;\n'
                                        '\t\t\t}',
                            'onTryHitPriority': 3},
              'contestType': 'Cool',
              'flags': {'nonsky': 1, 'snatch': 1},
              'name': 'Mat Block',
              'num': 561,
              'onTry': 'function (source) {\n'
                       '\t\t\tif (source.activeMoveActions > 1) {\n'
                       '\t\t\t\tthis.hint("Mat Block only works on your first '
                       'turn out.");\n'
                       '\t\t\t\treturn false;\n'
                       '\t\t\t}\n'
                       '\t\t\treturn !!this.queue.willAct();\n'
                       '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'sideCondition': 'matblock',
              'stallingMove': True,
              'target': 'allySide',
              'type': 'Fighting',
              'zMove': {'boost': {'def': 1}}},
 'maxairstream': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': True,
                  'name': 'Max Airstream',
                  'num': 766,
                  'pp': 10,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tif '
                                    "(!source.volatiles['dynamax'])\n"
                                    '\t\t\t\t\treturn;\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.alliesAndSelf(); _i < _a.length; '
                                    '_i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\tthis.boost({ spe: 1 }, '
                                    'pokemon);\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Flying'},
 'maxdarkness': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': True,
                 'name': 'Max Darkness',
                 'num': 772,
                 'pp': 10,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\tfor (var _i = 0, _a = '
                                   'source.foes(); _i < _a.length; _i++) {\n'
                                   '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                   '\t\t\t\t\tthis.boost({ spd: -1 }, '
                                   'pokemon);\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Dark'},
 'maxflare': {'accuracy': True,
              'basePower': 100,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {},
              'isMax': True,
              'name': 'Max Flare',
              'num': 757,
              'pp': 10,
              'priority': 0,
              'self': {'onHit': 'function (source) {\n'
                                "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                '\t\t\t\t\treturn;\n'
                                "\t\t\t\tthis.field.setWeather('sunnyday');\n"
                                '\t\t\t}'},
              'target': 'adjacentFoe',
              'type': 'Fire'},
 'maxflutterby': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': True,
                  'name': 'Max Flutterby',
                  'num': 758,
                  'pp': 10,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tif '
                                    "(!source.volatiles['dynamax'])\n"
                                    '\t\t\t\t\treturn;\n'
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.foes(); _i < _a.length; _i++) {\n'
                                    '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                    '\t\t\t\t\tthis.boost({ spa: -1 }, '
                                    'pokemon);\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Bug'},
 'maxgeyser': {'accuracy': True,
               'basePower': 10,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {},
               'isMax': True,
               'name': 'Max Geyser',
               'num': 765,
               'pp': 10,
               'priority': 0,
               'self': {'onHit': 'function (source) {\n'
                                 "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                 '\t\t\t\t\treturn;\n'
                                 "\t\t\t\tthis.field.setWeather('raindance');\n"
                                 '\t\t\t}'},
               'target': 'adjacentFoe',
               'type': 'Water'},
 'maxguard': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 1,
                            'onStart': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-singleturn', "
                                       "target, 'Max Guard');\n"
                                       '\t\t\t}',
                            'onTryHit': 'function (target, source, move) {\n'
                                        "\t\t\t\tif (['gmaxoneblow', "
                                        "'gmaxrapidflow'].includes(move.id))\n"
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\t/** moves blocked by Max '
                                        'Guard but not Protect */\n'
                                        '\t\t\t\tvar overrideBypassProtect = '
                                        '[\n'
                                        "\t\t\t\t\t'block', 'flowershield', "
                                        "'gearup', 'magneticflux', "
                                        "'phantomforce', 'psychup', "
                                        "'shadowforce', 'teatime', "
                                        "'transform',\n"
                                        '\t\t\t\t];\n'
                                        '\t\t\t\tvar blockedByMaxGuard = '
                                        "(this.dex.moves.get(move.id).flags['protect'] "
                                        '||\n'
                                        '\t\t\t\t\tmove.isZ || move.isMax || '
                                        'overrideBypassProtect.includes(move.id));\n'
                                        '\t\t\t\tif (!blockedByMaxGuard) {\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif (move.smartTarget) {\n'
                                        '\t\t\t\t\tmove.smartTarget = false;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\telse {\n'
                                        "\t\t\t\t\tthis.add('-activate', "
                                        "target, 'move: Max Guard');\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tvar lockedmove = '
                                        "source.getVolatile('lockedmove');\n"
                                        '\t\t\t\tif (lockedmove) {\n'
                                        '\t\t\t\t\t// Outrage counter is '
                                        'reset\n'
                                        '\t\t\t\t\tif '
                                        "(source.volatiles['lockedmove'].duration "
                                        '=== 2) {\n'
                                        '\t\t\t\t\t\tdelete '
                                        "source.volatiles['lockedmove'];\n"
                                        '\t\t\t\t\t}\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\treturn this.NOT_FAIL;\n'
                                        '\t\t\t}',
                            'onTryHitPriority': 3},
              'contestType': 'Cool',
              'flags': {},
              'isMax': True,
              'name': 'Max Guard',
              'num': 743,
              'onHit': 'function (pokemon) {\n'
                       "\t\t\tpokemon.addVolatile('stall');\n"
                       '\t\t}',
              'onPrepareHit': 'function (pokemon) {\n'
                              '\t\t\treturn !!this.queue.willAct() && '
                              "this.runEvent('StallMove', pokemon);\n"
                              '\t\t}',
              'pp': 10,
              'priority': 4,
              'secondary': None,
              'stallingMove': True,
              'target': 'self',
              'type': 'Normal',
              'volatileStatus': 'maxguard'},
 'maxhailstorm': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': True,
                  'name': 'Max Hailstorm',
                  'num': 763,
                  'pp': 10,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tif '
                                    "(!source.volatiles['dynamax'])\n"
                                    '\t\t\t\t\treturn;\n'
                                    "\t\t\t\tthis.field.setWeather('hail');\n"
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Ice'},
 'maxknuckle': {'accuracy': True,
                'basePower': 10,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {},
                'isMax': True,
                'name': 'Max Knuckle',
                'num': 761,
                'pp': 10,
                'priority': 0,
                'self': {'onHit': 'function (source) {\n'
                                  "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                  '\t\t\t\t\treturn;\n'
                                  '\t\t\t\tfor (var _i = 0, _a = '
                                  'source.alliesAndSelf(); _i < _a.length; '
                                  '_i++) {\n'
                                  '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                  '\t\t\t\t\tthis.boost({ atk: 1 }, pokemon);\n'
                                  '\t\t\t\t}\n'
                                  '\t\t\t}'},
                'target': 'adjacentFoe',
                'type': 'Fighting'},
 'maxlightning': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': True,
                  'name': 'Max Lightning',
                  'num': 759,
                  'pp': 10,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tif '
                                    "(!source.volatiles['dynamax'])\n"
                                    '\t\t\t\t\treturn;\n'
                                    '\t\t\t\t'
                                    "this.field.setTerrain('electricterrain');\n"
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Electric'},
 'maxmindstorm': {'accuracy': True,
                  'basePower': 10,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isMax': True,
                  'name': 'Max Mindstorm',
                  'num': 769,
                  'pp': 10,
                  'priority': 0,
                  'self': {'onHit': 'function (source) {\n'
                                    '\t\t\t\tif '
                                    "(!source.volatiles['dynamax'])\n"
                                    '\t\t\t\t\treturn;\n'
                                    '\t\t\t\t'
                                    "this.field.setTerrain('psychicterrain');\n"
                                    '\t\t\t}'},
                  'target': 'adjacentFoe',
                  'type': 'Psychic'},
 'maxooze': {'accuracy': True,
             'basePower': 10,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {},
             'isMax': True,
             'name': 'Max Ooze',
             'num': 764,
             'pp': 10,
             'priority': 0,
             'self': {'onHit': 'function (source) {\n'
                               "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                               '\t\t\t\t\treturn;\n'
                               '\t\t\t\tfor (var _i = 0, _a = '
                               'source.alliesAndSelf(); _i < _a.length; _i++) '
                               '{\n'
                               '\t\t\t\t\tvar pokemon = _a[_i];\n'
                               '\t\t\t\t\tthis.boost({ spa: 1 }, pokemon);\n'
                               '\t\t\t\t}\n'
                               '\t\t\t}'},
             'target': 'adjacentFoe',
             'type': 'Poison'},
 'maxovergrowth': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': True,
                   'name': 'Max Overgrowth',
                   'num': 773,
                   'pp': 10,
                   'priority': 0,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tif '
                                     "(!source.volatiles['dynamax'])\n"
                                     '\t\t\t\t\treturn;\n'
                                     '\t\t\t\t'
                                     "this.field.setTerrain('grassyterrain');\n"
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Grass'},
 'maxphantasm': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': True,
                 'name': 'Max Phantasm',
                 'num': 762,
                 'pp': 10,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\tfor (var _i = 0, _a = '
                                   'source.foes(); _i < _a.length; _i++) {\n'
                                   '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                   '\t\t\t\t\tthis.boost({ def: -1 }, '
                                   'pokemon);\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Ghost'},
 'maxquake': {'accuracy': True,
              'basePower': 10,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {},
              'isMax': True,
              'name': 'Max Quake',
              'num': 771,
              'pp': 10,
              'priority': 0,
              'self': {'onHit': 'function (source) {\n'
                                "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                '\t\t\t\t\treturn;\n'
                                '\t\t\t\tfor (var _i = 0, _a = '
                                'source.alliesAndSelf(); _i < _a.length; _i++) '
                                '{\n'
                                '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                '\t\t\t\t\tthis.boost({ spd: 1 }, pokemon);\n'
                                '\t\t\t\t}\n'
                                '\t\t\t}'},
              'target': 'adjacentFoe',
              'type': 'Ground'},
 'maxrockfall': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': True,
                 'name': 'Max Rockfall',
                 'num': 770,
                 'pp': 10,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\t'
                                   "this.field.setWeather('sandstorm');\n"
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Rock'},
 'maxstarfall': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': True,
                 'name': 'Max Starfall',
                 'num': 767,
                 'pp': 10,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\t'
                                   "this.field.setTerrain('mistyterrain');\n"
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Fairy'},
 'maxsteelspike': {'accuracy': True,
                   'basePower': 10,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isMax': True,
                   'name': 'Max Steelspike',
                   'num': 774,
                   'pp': 10,
                   'priority': 0,
                   'self': {'onHit': 'function (source) {\n'
                                     '\t\t\t\tif '
                                     "(!source.volatiles['dynamax'])\n"
                                     '\t\t\t\t\treturn;\n'
                                     '\t\t\t\tfor (var _i = 0, _a = '
                                     'source.alliesAndSelf(); _i < _a.length; '
                                     '_i++) {\n'
                                     '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                     '\t\t\t\t\tthis.boost({ def: 1 }, '
                                     'pokemon);\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}'},
                   'target': 'adjacentFoe',
                   'type': 'Steel'},
 'maxstrike': {'accuracy': True,
               'basePower': 10,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {},
               'isMax': True,
               'name': 'Max Strike',
               'num': 760,
               'pp': 10,
               'priority': 0,
               'self': {'onHit': 'function (source) {\n'
                                 "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                 '\t\t\t\t\treturn;\n'
                                 '\t\t\t\tfor (var _i = 0, _a = source.foes(); '
                                 '_i < _a.length; _i++) {\n'
                                 '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                 '\t\t\t\t\tthis.boost({ spe: -1 }, pokemon);\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}'},
               'target': 'adjacentFoe',
               'type': 'Normal'},
 'maxwyrmwind': {'accuracy': True,
                 'basePower': 10,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {},
                 'isMax': True,
                 'name': 'Max Wyrmwind',
                 'num': 768,
                 'pp': 10,
                 'priority': 0,
                 'self': {'onHit': 'function (source) {\n'
                                   "\t\t\t\tif (!source.volatiles['dynamax'])\n"
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\tfor (var _i = 0, _a = '
                                   'source.foes(); _i < _a.length; _i++) {\n'
                                   '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                   '\t\t\t\t\tthis.boost({ atk: -1 }, '
                                   'pokemon);\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}'},
                 'target': 'adjacentFoe',
                 'type': 'Dragon'},
 'meanlook': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'reflectable': 1},
              'name': 'Mean Look',
              'num': 212,
              'onHit': 'function (target, source, move) {\n'
                       "\t\t\treturn target.addVolatile('trapped', source, "
                       "move, 'trapper');\n"
                       '\t\t}',
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'boost': {'spd': 1}}},
 'meditate': {'accuracy': True,
              'basePower': 0,
              'boosts': {'atk': 1},
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {'snatch': 1},
              'isNonstandard': 'Past',
              'name': 'Meditate',
              'num': 96,
              'pp': 40,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Psychic',
              'zMove': {'boost': {'atk': 1}}},
 'mefirst': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 1,
                           'onBasePower': 'function (basePower) {\n'
                                          '\t\t\t\treturn '
                                          'this.chainModify(1.5);\n'
                                          '\t\t\t}',
                           'onBasePowerPriority': 12},
             'contestType': 'Clever',
             'flags': {'authentic': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Me First',
             'num': 382,
             'onTryHit': 'function (target, pokemon) {\n'
                         '\t\t\tvar action = this.queue.willMove(target);\n'
                         '\t\t\tif (!action)\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\tvar noMeFirst = [\n'
                         "\t\t\t\t'beakblast', 'chatter', 'counter', 'covet', "
                         "'focuspunch', 'mefirst', 'metalburst', 'mirrorcoat', "
                         "'shelltrap', 'struggle', 'thief',\n"
                         '\t\t\t];\n'
                         '\t\t\tvar move = '
                         'this.dex.getActiveMove(action.move.id);\n'
                         '\t\t\tif (action.zmove || move.isZ || move.isMax)\n'
                         '\t\t\t\treturn false;\n'
                         "\t\t\tif (target.volatiles['mustrecharge'])\n"
                         '\t\t\t\treturn false;\n'
                         "\t\t\tif (move.category === 'Status' || "
                         'noMeFirst.includes(move.id))\n'
                         '\t\t\t\treturn false;\n'
                         "\t\t\tpokemon.addVolatile('mefirst');\n"
                         '\t\t\tthis.actions.useMove(move, pokemon, target);\n'
                         '\t\t\treturn null;\n'
                         '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'adjacentFoe',
             'type': 'Normal',
             'zMove': {'boost': {'spe': 2}}},
 'megadrain': {'accuracy': 100,
               'basePower': 40,
               'category': 'Special',
               'contestType': 'Clever',
               'drain': [1, 2],
               'flags': {'heal': 1, 'mirror': 1, 'protect': 1},
               'name': 'Mega Drain',
               'num': 72,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass',
               'zMove': {'basePower': 120}},
 'megahorn': {'accuracy': 85,
              'basePower': 120,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Megahorn',
              'num': 224,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Bug'},
 'megakick': {'accuracy': 75,
              'basePower': 120,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Mega Kick',
              'num': 25,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'megapunch': {'accuracy': 85,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
               'name': 'Mega Punch',
               'num': 5,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal'},
 'memento': {'accuracy': 100,
             'basePower': 0,
             'boosts': {'atk': -2, 'spa': -2},
             'category': 'Status',
             'contestType': 'Tough',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Memento',
             'num': 262,
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'selfdestruct': 'ifHit',
             'target': 'normal',
             'type': 'Dark',
             'zMove': {'effect': 'healreplacement'}},
 'menacingmoonrazemaelstrom': {'accuracy': True,
                               'basePower': 200,
                               'category': 'Special',
                               'contestType': 'Cool',
                               'flags': {},
                               'ignoreAbility': True,
                               'isNonstandard': 'Past',
                               'isZ': 'lunaliumz',
                               'name': 'Menacing Moonraze Maelstrom',
                               'num': 725,
                               'pp': 1,
                               'priority': 0,
                               'secondary': None,
                               'target': 'normal',
                               'type': 'Ghost'},
 'metalburst': {'accuracy': 100,
                'basePower': 0,
                'category': 'Physical',
                'contestType': 'Cool',
                'damageCallback': 'function (pokemon) {\n'
                                  '\t\t\tvar lastDamagedBy = '
                                  'pokemon.getLastDamagedBy(true);\n'
                                  '\t\t\tif (lastDamagedBy !== undefined) {\n'
                                  '\t\t\t\treturn (lastDamagedBy.damage * 1.5) '
                                  '|| 1;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn 0;\n'
                                  '\t\t}',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Metal Burst',
                'num': 368,
                'onModifyTarget': 'function (targetRelayVar, source, target, '
                                  'move) {\n'
                                  '\t\t\tvar lastDamagedBy = '
                                  'source.getLastDamagedBy(true);\n'
                                  '\t\t\tif (lastDamagedBy) {\n'
                                  '\t\t\t\ttargetRelayVar.target = '
                                  'this.getAtSlot(lastDamagedBy.slot);\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                'onTryHit': 'function (target, source, move) {\n'
                            '\t\t\tvar lastDamagedBy = '
                            'source.getLastDamagedBy(true);\n'
                            '\t\t\tif (lastDamagedBy === undefined || '
                            '!lastDamagedBy.thisTurn)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'scripted',
                'type': 'Steel'},
 'metalclaw': {'accuracy': 95,
               'basePower': 50,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Metal Claw',
               'num': 232,
               'pp': 35,
               'priority': 0,
               'secondary': {'chance': 10, 'self': {'boosts': {'atk': 1}}},
               'target': 'normal',
               'type': 'Steel'},
 'metalsound': {'accuracy': 85,
                'basePower': 0,
                'boosts': {'spd': -2},
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'mystery': 1,
                          'protect': 1,
                          'reflectable': 1,
                          'sound': 1},
                'name': 'Metal Sound',
                'num': 319,
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Steel',
                'zMove': {'boost': {'spa': 1}}},
 'meteorassault': {'accuracy': 100,
                   'basePower': 150,
                   'category': 'Physical',
                   'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
                   'name': 'Meteor Assault',
                   'num': 794,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'self': {'volatileStatus': 'mustrecharge'},
                   'target': 'normal',
                   'type': 'Fighting'},
 'meteorbeam': {'accuracy': 90,
                'basePower': 120,
                'category': 'Special',
                'flags': {'charge': 1, 'mirror': 1, 'protect': 1},
                'name': 'Meteor Beam',
                'num': 800,
                'onTryMove': 'function (attacker, defender, move) {\n'
                             '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             "\t\t\tthis.add('-prepare', attacker, "
                             'move.name);\n'
                             '\t\t\tthis.boost({ spa: 1 }, attacker, attacker, '
                             'move);\n'
                             "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                             'defender, move)) {\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             "\t\t\tattacker.addVolatile('twoturnmove', "
                             'defender);\n'
                             '\t\t\treturn null;\n'
                             '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Rock'},
 'meteormash': {'accuracy': 90,
                'basePower': 90,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                'name': 'Meteor Mash',
                'num': 309,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 20, 'self': {'boosts': {'atk': 1}}},
                'target': 'normal',
                'type': 'Steel'},
 'metronome': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {},
               'name': 'Metronome',
               'noMetronome': ['After You',
                               'Apple Acid',
                               'Assist',
                               'Astral Barrage',
                               'Aura Wheel',
                               'Baneful Bunker',
                               'Beak Blast',
                               'Behemoth Bash',
                               'Behemoth Blade',
                               'Belch',
                               'Bestow',
                               'Body Press',
                               'Branch Poke',
                               'Breaking Swipe',
                               'Celebrate',
                               'Chatter',
                               'Clangorous Soul',
                               'Copycat',
                               'Counter',
                               'Covet',
                               'Crafty Shield',
                               'Decorate',
                               'Destiny Bond',
                               'Detect',
                               'Diamond Storm',
                               'Double Iron Bash',
                               'Dragon Ascent',
                               'Dragon Energy',
                               'Drum Beating',
                               'Dynamax Cannon',
                               'Endure',
                               'Eternabeam',
                               'False Surrender',
                               'Feint',
                               'Fiery Wrath',
                               'Fleur Cannon',
                               'Focus Punch',
                               'Follow Me',
                               'Freeze Shock',
                               'Freezing Glare',
                               'Glacial Lance',
                               'Grav Apple',
                               'Helping Hand',
                               'Hold Hands',
                               'Hyperspace Fury',
                               'Hyperspace Hole',
                               'Ice Burn',
                               'Instruct',
                               'Jungle Healing',
                               "King's Shield",
                               'Life Dew',
                               'Light of Ruin',
                               'Mat Block',
                               'Me First',
                               'Meteor Assault',
                               'Metronome',
                               'Mimic',
                               'Mind Blown',
                               'Mirror Coat',
                               'Mirror Move',
                               'Moongeist Beam',
                               'Nature Power',
                               "Nature's Madness",
                               'Obstruct',
                               'Origin Pulse',
                               'Overdrive',
                               'Photon Geyser',
                               'Plasma Fists',
                               'Precipice Blades',
                               'Protect',
                               'Pyro Ball',
                               'Quash',
                               'Quick Guard',
                               'Rage Powder',
                               'Relic Song',
                               'Secret Sword',
                               'Shell Trap',
                               'Sketch',
                               'Sleep Talk',
                               'Snap Trap',
                               'Snarl',
                               'Snatch',
                               'Snore',
                               'Spectral Thief',
                               'Spiky Shield',
                               'Spirit Break',
                               'Spotlight',
                               'Steam Eruption',
                               'Steel Beam',
                               'Strange Steam',
                               'Struggle',
                               'Sunsteel Strike',
                               'Surging Strikes',
                               'Switcheroo',
                               'Techno Blast',
                               'Thief',
                               'Thousand Arrows',
                               'Thousand Waves',
                               'Thunder Cage',
                               'Thunderous Kick',
                               'Transform',
                               'Trick',
                               'V-create',
                               'Wicked Blow',
                               'Wide Guard'],
               'num': 118,
               'onHit': 'function (target, source, effect) {\n'
                        '\t\t\tvar moves = [];\n'
                        '\t\t\tfor (var id in exports.Moves) {\n'
                        '\t\t\t\tvar move = exports.Moves[id];\n'
                        '\t\t\t\tif (move.realMove)\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\tif (move.isZ || move.isMax || '
                        'move.isNonstandard)\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\tif (effect.noMetronome.includes(move.name))\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\tif (this.dex.moves.get(id).gen > this.gen)\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\tmoves.push(move);\n'
                        '\t\t\t}\n'
                        "\t\t\tvar randomMove = '';\n"
                        '\t\t\tif (moves.length) {\n'
                        '\t\t\t\tmoves.sort(function (a, b) { return a.num - '
                        'b.num; });\n'
                        '\t\t\t\trandomMove = this.sample(moves).name;\n'
                        '\t\t\t}\n'
                        '\t\t\tif (!randomMove) {\n'
                        '\t\t\t\treturn false;\n'
                        '\t\t\t}\n'
                        '\t\t\tthis.actions.useMove(randomMove, target);\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Normal'},
 'milkdrink': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'heal': 1, 'snatch': 1},
               'heal': [1, 2],
               'name': 'Milk Drink',
               'num': 208,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Normal',
               'zMove': {'effect': 'clearnegativeboost'}},
 'mimic': {'accuracy': True,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Cute',
           'flags': {'authentic': 1, 'mystery': 1, 'protect': 1},
           'name': 'Mimic',
           'num': 102,
           'onHit': 'function (target, source) {\n'
                    "\t\t\tvar disallowedMoves = ['chatter', 'mimic', "
                    "'sketch', 'struggle', 'transform'];\n"
                    '\t\t\tvar move = target.lastMove;\n'
                    '\t\t\tif (source.transformed || !move || '
                    'disallowedMoves.includes(move.id) || '
                    'source.moves.includes(move.id)) {\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\t}\n'
                    '\t\t\tif (move.isZ || move.isMax)\n'
                    '\t\t\t\treturn false;\n'
                    "\t\t\tvar mimicIndex = source.moves.indexOf('mimic');\n"
                    '\t\t\tif (mimicIndex < 0)\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\tsource.moveSlots[mimicIndex] = {\n'
                    '\t\t\t\tmove: move.name,\n'
                    '\t\t\t\tid: move.id,\n'
                    '\t\t\t\tpp: move.pp,\n'
                    '\t\t\t\tmaxpp: move.pp,\n'
                    '\t\t\t\ttarget: move.target,\n'
                    '\t\t\t\tdisabled: false,\n'
                    '\t\t\t\tused: false,\n'
                    '\t\t\t\tvirtual: true,\n'
                    '\t\t\t};\n'
                    "\t\t\tthis.add('-start', source, 'Mimic', move.name);\n"
                    '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal',
           'zMove': {'boost': {'accuracy': 1}}},
 'mindblown': {'accuracy': 100,
               'basePower': 150,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'mirror': 1, 'protect': 1},
               'mindBlownRecoil': True,
               'name': 'Mind Blown',
               'num': 720,
               'onAfterMove': 'function (pokemon, target, move) {\n'
                              '\t\t\tif (move.mindBlownRecoil && '
                              '!move.multihit) {\n'
                              '\t\t\t\tthis.damage(Math.round(pokemon.maxhp / '
                              '2), pokemon, pokemon, '
                              "this.dex.conditions.get('Mind Blown'), true);\n"
                              '\t\t\t}\n'
                              '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacent',
               'type': 'Fire'},
 'mindreader': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Mind Reader',
                'num': 170,
                'onHit': 'function (target, source) {\n'
                         "\t\t\tsource.addVolatile('lockon', target);\n"
                         "\t\t\tthis.add('-activate', source, 'move: Mind "
                         "Reader', '[of] ' + target);\n"
                         '\t\t}',
                'onTryHit': 'function (target, source) {\n'
                            "\t\t\tif (source.volatiles['lockon'])\n"
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal',
                'zMove': {'boost': {'spa': 1}}},
 'minimize': {'accuracy': True,
              'basePower': 0,
              'boosts': {'evasion': 2},
              'category': 'Status',
              'condition': {'noCopy': True,
                            'onAccuracy': 'function (accuracy, target, source, '
                                          'move) {\n'
                                          '\t\t\t\tvar boostedMoves = [\n'
                                          "\t\t\t\t\t'stomp', 'steamroller', "
                                          "'bodyslam', 'flyingpress', "
                                          "'dragonrush', 'heatcrash', "
                                          "'heavyslam', 'maliciousmoonsault',\n"
                                          '\t\t\t\t];\n'
                                          '\t\t\t\tif '
                                          '(boostedMoves.includes(move.id)) {\n'
                                          '\t\t\t\t\treturn true;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\treturn accuracy;\n'
                                          '\t\t\t}',
                            'onSourceModifyDamage': 'function (damage, source, '
                                                    'target, move) {\n'
                                                    '\t\t\t\tvar boostedMoves '
                                                    '= [\n'
                                                    "\t\t\t\t\t'stomp', "
                                                    "'steamroller', "
                                                    "'bodyslam', "
                                                    "'flyingpress', "
                                                    "'dragonrush', "
                                                    "'heatcrash', 'heavyslam', "
                                                    "'maliciousmoonsault',\n"
                                                    '\t\t\t\t];\n'
                                                    '\t\t\t\tif '
                                                    '(boostedMoves.includes(move.id)) '
                                                    '{\n'
                                                    '\t\t\t\t\treturn '
                                                    'this.chainModify(2);\n'
                                                    '\t\t\t\t}\n'
                                                    '\t\t\t}'},
              'contestType': 'Cute',
              'flags': {'snatch': 1},
              'name': 'Minimize',
              'num': 107,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Normal',
              'volatileStatus': 'minimize',
              'zMove': {'effect': 'clearnegativeboost'}},
 'miracleeye': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'noCopy': True,
                              'onModifyBoost': 'function (boosts) {\n'
                                               '\t\t\t\tif (boosts.evasion && '
                                               'boosts.evasion > 0) {\n'
                                               '\t\t\t\t\tboosts.evasion = 0;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                              'onNegateImmunity': 'function (pokemon, type) {\n'
                                                  '\t\t\t\tif '
                                                  "(pokemon.hasType('Dark') && "
                                                  "type === 'Psychic')\n"
                                                  '\t\t\t\t\treturn false;\n'
                                                  '\t\t\t}',
                              'onStart': 'function (pokemon) {\n'
                                         "\t\t\t\tthis.add('-start', pokemon, "
                                         "'Miracle Eye');\n"
                                         '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'protect': 1,
                          'reflectable': 1},
                'isNonstandard': 'Past',
                'name': 'Miracle Eye',
                'num': 357,
                'onTryHit': 'function (target) {\n'
                            "\t\t\tif (target.volatiles['foresight'])\n"
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Psychic',
                'volatileStatus': 'miracleeye',
                'zMove': {'boost': {'spa': 1}}},
 'mirrorcoat': {'accuracy': 100,
                'basePower': 0,
                'beforeTurnCallback': 'function (pokemon) {\n'
                                      '\t\t\t'
                                      "pokemon.addVolatile('mirrorcoat');\n"
                                      '\t\t}',
                'category': 'Special',
                'condition': {'duration': 1,
                              'noCopy': True,
                              'onDamagingHit': 'function (damage, target, '
                                               'source, move) {\n'
                                               '\t\t\t\tif '
                                               '(!source.isAlly(target) && '
                                               'this.getCategory(move) === '
                                               "'Special') {\n"
                                               '\t\t\t\t\t'
                                               'this.effectState.slot = '
                                               'source.getSlot();\n'
                                               '\t\t\t\t\t'
                                               'this.effectState.damage = 2 * '
                                               'damage;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                              'onRedirectTarget': 'function (target, source, '
                                                  'source2, move) {\n'
                                                  '\t\t\t\tif (move.id !== '
                                                  "'mirrorcoat')\n"
                                                  '\t\t\t\t\treturn;\n'
                                                  '\t\t\t\tif (source !== '
                                                  'this.effectState.target || '
                                                  '!this.effectState.slot)\n'
                                                  '\t\t\t\t\treturn;\n'
                                                  '\t\t\t\treturn '
                                                  'this.getAtSlot(this.effectState.slot);\n'
                                                  '\t\t\t}',
                              'onRedirectTargetPriority': -1,
                              'onStart': 'function (target, source, move) {\n'
                                         '\t\t\t\tthis.effectState.slot = '
                                         'null;\n'
                                         '\t\t\t\tthis.effectState.damage = '
                                         '0;\n'
                                         '\t\t\t}'},
                'contestType': 'Beautiful',
                'damageCallback': 'function (pokemon) {\n'
                                  '\t\t\tif '
                                  "(!pokemon.volatiles['mirrorcoat'])\n"
                                  '\t\t\t\treturn 0;\n'
                                  '\t\t\treturn '
                                  "pokemon.volatiles['mirrorcoat'].damage || "
                                  '1;\n'
                                  '\t\t}',
                'flags': {'protect': 1},
                'name': 'Mirror Coat',
                'num': 243,
                'onTryHit': 'function (target, source, move) {\n'
                            "\t\t\tif (!source.volatiles['mirrorcoat'])\n"
                            '\t\t\t\treturn false;\n'
                            "\t\t\tif (source.volatiles['mirrorcoat'].slot === "
                            'null)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 20,
                'priority': -5,
                'secondary': None,
                'target': 'scripted',
                'type': 'Psychic'},
 'mirrormove': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {},
                'isNonstandard': 'Past',
                'name': 'Mirror Move',
                'num': 119,
                'onTryHit': 'function (target, pokemon) {\n'
                            '\t\t\tvar move = target.lastMove;\n'
                            '\t\t\tif (!(move === null || move === void 0 ? '
                            "void 0 : move.flags['mirror']) || move.isZ || "
                            'move.isMax) {\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t\tthis.actions.useMove(move.id, pokemon, '
                            'target);\n'
                            '\t\t\treturn null;\n'
                            '\t\t}',
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Flying',
                'zMove': {'boost': {'atk': 2}}},
 'mirrorshot': {'accuracy': 85,
                'basePower': 65,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Mirror Shot',
                'num': 429,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'accuracy': -1}, 'chance': 30},
                'target': 'normal',
                'type': 'Steel'},
 'mist': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'condition': {'duration': 5,
                        'onBoost': 'function (boost, target, source, effect) '
                                   '{\n'
                                   "\t\t\t\tif (effect.effectType === 'Move' "
                                   '&& effect.infiltrates && '
                                   '!target.isAlly(source))\n'
                                   '\t\t\t\t\treturn;\n'
                                   '\t\t\t\tif (source && target !== source) '
                                   '{\n'
                                   '\t\t\t\t\tvar showMsg = false;\n'
                                   '\t\t\t\t\tvar i = void 0;\n'
                                   '\t\t\t\t\tfor (i in boost) {\n'
                                   '\t\t\t\t\t\tif (boost[i] < 0) {\n'
                                   '\t\t\t\t\t\t\tdelete boost[i];\n'
                                   '\t\t\t\t\t\t\tshowMsg = true;\n'
                                   '\t\t\t\t\t\t}\n'
                                   '\t\t\t\t\t}\n'
                                   '\t\t\t\t\tif (showMsg && '
                                   '!effect.secondaries) {\n'
                                   "\t\t\t\t\t\tthis.add('-activate', target, "
                                   "'move: Mist');\n"
                                   '\t\t\t\t\t}\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}',
                        'onSideEnd': 'function (side) {\n'
                                     "\t\t\t\tthis.add('-sideend', side, "
                                     "'Mist');\n"
                                     '\t\t\t}',
                        'onSideResidualOrder': 26,
                        'onSideResidualSubOrder': 4,
                        'onSideStart': 'function (side) {\n'
                                       "\t\t\t\tthis.add('-sidestart', side, "
                                       "'Mist');\n"
                                       '\t\t\t}'},
          'contestType': 'Beautiful',
          'flags': {'snatch': 1},
          'name': 'Mist',
          'num': 54,
          'pp': 30,
          'priority': 0,
          'secondary': None,
          'sideCondition': 'mist',
          'target': 'allySide',
          'type': 'Ice',
          'zMove': {'effect': 'heal'}},
 'mistball': {'accuracy': 100,
              'basePower': 70,
              'category': 'Special',
              'contestType': 'Clever',
              'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
              'name': 'Mist Ball',
              'num': 296,
              'pp': 5,
              'priority': 0,
              'secondary': {'boosts': {'spa': -1}, 'chance': 50},
              'target': 'normal',
              'type': 'Psychic'},
 'mistyexplosion': {'accuracy': 100,
                    'basePower': 100,
                    'category': 'Special',
                    'flags': {'mirror': 1, 'protect': 1},
                    'name': 'Misty Explosion',
                    'num': 802,
                    'onBasePower': 'function (basePower, source) {\n'
                                   '\t\t\tif '
                                   "(this.field.isTerrain('mistyterrain') && "
                                   'source.isGrounded()) {\n'
                                   "\t\t\t\tthis.debug('misty terrain "
                                   "boost');\n"
                                   '\t\t\t\treturn this.chainModify(1.5);\n'
                                   '\t\t\t}\n'
                                   '\t\t}',
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'selfdestruct': 'always',
                    'target': 'allAdjacent',
                    'type': 'Fairy'},
 'mistyterrain': {'accuracy': True,
                  'basePower': 0,
                  'category': 'Status',
                  'condition': {'duration': 5,
                                'durationCallback': 'function (source, effect) '
                                                    '{\n'
                                                    '\t\t\t\tif (source === '
                                                    'null || source === void 0 '
                                                    '? void 0 : '
                                                    "source.hasItem('terrainextender')) "
                                                    '{\n'
                                                    '\t\t\t\t\treturn 8;\n'
                                                    '\t\t\t\t}\n'
                                                    '\t\t\t\treturn 5;\n'
                                                    '\t\t\t}',
                                'onBasePower': 'function (basePower, attacker, '
                                               'defender, move) {\n'
                                               '\t\t\t\tif (move.type === '
                                               "'Dragon' && "
                                               'defender.isGrounded() && '
                                               '!defender.isSemiInvulnerable()) '
                                               '{\n'
                                               "\t\t\t\t\tthis.debug('misty "
                                               "terrain weaken');\n"
                                               '\t\t\t\t\treturn '
                                               'this.chainModify(0.5);\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                                'onBasePowerPriority': 6,
                                'onFieldEnd': 'function () {\n'
                                              "\t\t\t\tthis.add('-fieldend', "
                                              "'Misty Terrain');\n"
                                              '\t\t\t}',
                                'onFieldResidualOrder': 27,
                                'onFieldResidualSubOrder': 7,
                                'onFieldStart': 'function (field, source, '
                                                'effect) {\n'
                                                '\t\t\t\tif ((effect === null '
                                                '|| effect === void 0 ? void 0 '
                                                ': effect.effectType) === '
                                                "'Ability') {\n"
                                                '\t\t\t\t\t'
                                                "this.add('-fieldstart', "
                                                "'move: Misty Terrain', "
                                                "'[from] ability: ' + effect, "
                                                "'[of] ' + source);\n"
                                                '\t\t\t\t}\n'
                                                '\t\t\t\telse {\n'
                                                '\t\t\t\t\t'
                                                "this.add('-fieldstart', "
                                                "'move: Misty Terrain');\n"
                                                '\t\t\t\t}\n'
                                                '\t\t\t}',
                                'onSetStatus': 'function (status, target, '
                                               'source, effect) {\n'
                                               '\t\t\t\tif '
                                               '(!target.isGrounded() || '
                                               'target.isSemiInvulnerable())\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\tif (effect && '
                                               '(effect.status || effect.id '
                                               "=== 'yawn')) {\n"
                                               '\t\t\t\t\t'
                                               "this.add('-activate', target, "
                                               "'move: Misty Terrain');\n"
                                               '\t\t\t\t}\n'
                                               '\t\t\t\treturn false;\n'
                                               '\t\t\t}',
                                'onTryAddVolatile': 'function (status, target, '
                                                    'source, effect) {\n'
                                                    '\t\t\t\tif '
                                                    '(!target.isGrounded() || '
                                                    'target.isSemiInvulnerable())\n'
                                                    '\t\t\t\t\treturn;\n'
                                                    '\t\t\t\tif (status.id === '
                                                    "'confusion') {\n"
                                                    '\t\t\t\t\tif '
                                                    '(effect.effectType === '
                                                    "'Move' && "
                                                    '!effect.secondaries)\n'
                                                    '\t\t\t\t\t\t'
                                                    "this.add('-activate', "
                                                    "target, 'move: Misty "
                                                    "Terrain');\n"
                                                    '\t\t\t\t\treturn null;\n'
                                                    '\t\t\t\t}\n'
                                                    '\t\t\t}'},
                  'contestType': 'Beautiful',
                  'flags': {'nonsky': 1},
                  'name': 'Misty Terrain',
                  'num': 581,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'all',
                  'terrain': 'mistyterrain',
                  'type': 'Fairy',
                  'zMove': {'boost': {'spd': 1}}},
 'moonblast': {'accuracy': 100,
               'basePower': 95,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Moonblast',
               'num': 585,
               'pp': 15,
               'priority': 0,
               'secondary': {'boosts': {'spa': -1}, 'chance': 30},
               'target': 'normal',
               'type': 'Fairy'},
 'moongeistbeam': {'accuracy': 100,
                   'basePower': 100,
                   'category': 'Special',
                   'contestType': 'Cool',
                   'flags': {'mirror': 1, 'protect': 1},
                   'ignoreAbility': True,
                   'name': 'Moongeist Beam',
                   'num': 714,
                   'pp': 5,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Ghost'},
 'moonlight': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Beautiful',
               'flags': {'heal': 1, 'snatch': 1},
               'name': 'Moonlight',
               'num': 236,
               'onHit': 'function (pokemon) {\n'
                        '\t\t\tvar factor = 0.5;\n'
                        '\t\t\tswitch (pokemon.effectiveWeather()) {\n'
                        "\t\t\t\tcase 'sunnyday':\n"
                        "\t\t\t\tcase 'desolateland':\n"
                        '\t\t\t\t\tfactor = 0.667;\n'
                        '\t\t\t\t\tbreak;\n'
                        "\t\t\t\tcase 'raindance':\n"
                        "\t\t\t\tcase 'primordialsea':\n"
                        "\t\t\t\tcase 'sandstorm':\n"
                        "\t\t\t\tcase 'hail':\n"
                        '\t\t\t\t\tfactor = 0.25;\n'
                        '\t\t\t\t\tbreak;\n'
                        '\t\t\t}\n'
                        '\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, '
                        'factor));\n'
                        '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Fairy',
               'zMove': {'effect': 'clearnegativeboost'}},
 'morningsun': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Beautiful',
                'flags': {'heal': 1, 'snatch': 1},
                'name': 'Morning Sun',
                'num': 234,
                'onHit': 'function (pokemon) {\n'
                         '\t\t\tvar factor = 0.5;\n'
                         '\t\t\tswitch (pokemon.effectiveWeather()) {\n'
                         "\t\t\t\tcase 'sunnyday':\n"
                         "\t\t\t\tcase 'desolateland':\n"
                         '\t\t\t\t\tfactor = 0.667;\n'
                         '\t\t\t\t\tbreak;\n'
                         "\t\t\t\tcase 'raindance':\n"
                         "\t\t\t\tcase 'primordialsea':\n"
                         "\t\t\t\tcase 'sandstorm':\n"
                         "\t\t\t\tcase 'hail':\n"
                         '\t\t\t\t\tfactor = 0.25;\n'
                         '\t\t\t\t\tbreak;\n'
                         '\t\t\t}\n'
                         '\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, '
                         'factor));\n'
                         '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'effect': 'clearnegativeboost'}},
 'mudbomb': {'accuracy': 85,
             'basePower': 65,
             'category': 'Special',
             'contestType': 'Cute',
             'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Mud Bomb',
             'num': 426,
             'pp': 10,
             'priority': 0,
             'secondary': {'boosts': {'accuracy': -1}, 'chance': 30},
             'target': 'normal',
             'type': 'Ground'},
 'muddywater': {'accuracy': 85,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                'name': 'Muddy Water',
                'num': 330,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'accuracy': -1}, 'chance': 30},
                'target': 'allAdjacentFoes',
                'type': 'Water'},
 'mudshot': {'accuracy': 95,
             'basePower': 55,
             'category': 'Special',
             'contestType': 'Tough',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Mud Shot',
             'num': 341,
             'pp': 15,
             'priority': 0,
             'secondary': {'boosts': {'spe': -1}, 'chance': 100},
             'target': 'normal',
             'type': 'Ground'},
 'mudslap': {'accuracy': 100,
             'basePower': 20,
             'category': 'Special',
             'contestType': 'Cute',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Mud-Slap',
             'num': 189,
             'pp': 10,
             'priority': 0,
             'secondary': {'boosts': {'accuracy': -1}, 'chance': 100},
             'target': 'normal',
             'type': 'Ground'},
 'mudsport': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 5,
                            'onBasePower': 'function (basePower, attacker, '
                                           'defender, move) {\n'
                                           '\t\t\t\tif (move.type === '
                                           "'Electric') {\n"
                                           "\t\t\t\t\tthis.debug('mud sport "
                                           "weaken');\n"
                                           '\t\t\t\t\treturn '
                                           'this.chainModify([1352, 4096]);\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t}',
                            'onBasePowerPriority': 1,
                            'onFieldEnd': 'function () {\n'
                                          "\t\t\t\tthis.add('-fieldend', "
                                          "'move: Mud Sport');\n"
                                          '\t\t\t}',
                            'onFieldResidualOrder': 27,
                            'onFieldResidualSubOrder': 4,
                            'onFieldStart': 'function (field, source) {\n'
                                            "\t\t\t\tthis.add('-fieldstart', "
                                            "'move: Mud Sport', '[of] ' + "
                                            'source);\n'
                                            '\t\t\t}'},
              'contestType': 'Cute',
              'flags': {'nonsky': 1},
              'isNonstandard': 'Past',
              'name': 'Mud Sport',
              'num': 300,
              'pp': 15,
              'priority': 0,
              'pseudoWeather': 'mudsport',
              'secondary': None,
              'target': 'all',
              'type': 'Ground',
              'zMove': {'boost': {'spd': 1}}},
 'multiattack': {'accuracy': 100,
                 'basePower': 120,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 95},
                 'name': 'Multi-Attack',
                 'num': 718,
                 'onModifyType': 'function (move, pokemon) {\n'
                                 '\t\t\tif (pokemon.ignoringItem())\n'
                                 '\t\t\t\treturn;\n'
                                 "\t\t\tmove.type = this.runEvent('Memory', "
                                 "pokemon, null, move, 'Normal');\n"
                                 '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'basePower': 185}},
 'mysticalfire': {'accuracy': 100,
                  'basePower': 75,
                  'category': 'Special',
                  'contestType': 'Beautiful',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Mystical Fire',
                  'num': 595,
                  'pp': 10,
                  'priority': 0,
                  'secondary': {'boosts': {'spa': -1}, 'chance': 100},
                  'target': 'normal',
                  'type': 'Fire'},
 'nastyplot': {'accuracy': True,
               'basePower': 0,
               'boosts': {'spa': 2},
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'snatch': 1},
               'name': 'Nasty Plot',
               'num': 417,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Dark',
               'zMove': {'effect': 'clearnegativeboost'}},
 'naturalgift': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'maxMove': {'basePower': 130},
                 'name': 'Natural Gift',
                 'num': 363,
                 'onModifyType': 'function (move, pokemon) {\n'
                                 '\t\t\tif (pokemon.ignoringItem())\n'
                                 '\t\t\t\treturn;\n'
                                 '\t\t\tvar item = pokemon.getItem();\n'
                                 '\t\t\tif (!item.naturalGift)\n'
                                 '\t\t\t\treturn;\n'
                                 '\t\t\tmove.type = item.naturalGift.type;\n'
                                 '\t\t}',
                 'onPrepareHit': 'function (target, pokemon, move) {\n'
                                 '\t\t\tif (pokemon.ignoringItem())\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\tvar item = pokemon.getItem();\n'
                                 '\t\t\tif (!item.naturalGift)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\tmove.basePower = '
                                 'item.naturalGift.basePower;\n'
                                 "\t\t\tpokemon.setItem('');\n"
                                 '\t\t\tpokemon.lastItem = item.id;\n'
                                 '\t\t\tpokemon.usedItemThisTurn = true;\n'
                                 "\t\t\tthis.runEvent('AfterUseItem', pokemon, "
                                 'null, null, item);\n'
                                 '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'basePower': 160}},
 'naturepower': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {},
                 'name': 'Nature Power',
                 'num': 267,
                 'onTryHit': 'function (target, pokemon) {\n'
                             "\t\t\tvar move = 'triattack';\n"
                             '\t\t\tif '
                             "(this.field.isTerrain('electricterrain')) {\n"
                             "\t\t\t\tmove = 'thunderbolt';\n"
                             '\t\t\t}\n'
                             '\t\t\telse if '
                             "(this.field.isTerrain('grassyterrain')) {\n"
                             "\t\t\t\tmove = 'energyball';\n"
                             '\t\t\t}\n'
                             '\t\t\telse if '
                             "(this.field.isTerrain('mistyterrain')) {\n"
                             "\t\t\t\tmove = 'moonblast';\n"
                             '\t\t\t}\n'
                             '\t\t\telse if '
                             "(this.field.isTerrain('psychicterrain')) {\n"
                             "\t\t\t\tmove = 'psychic';\n"
                             '\t\t\t}\n'
                             '\t\t\tthis.actions.useMove(move, pokemon, '
                             'target);\n'
                             '\t\t\treturn null;\n'
                             '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'naturesmadness': {'accuracy': 90,
                    'basePower': 0,
                    'category': 'Special',
                    'contestType': 'Tough',
                    'damageCallback': 'function (pokemon, target) {\n'
                                      '\t\t\treturn '
                                      'this.clampIntRange(Math.floor(target.getUndynamaxedHP() '
                                      '/ 2), 1);\n'
                                      '\t\t}',
                    'flags': {'mirror': 1, 'protect': 1},
                    'name': "Nature's Madness",
                    'num': 717,
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Fairy'},
 'needlearm': {'accuracy': 100,
               'basePower': 60,
               'category': 'Physical',
               'contestType': 'Clever',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Needle Arm',
               'num': 302,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
               'target': 'normal',
               'type': 'Grass'},
 'neverendingnightmare': {'accuracy': True,
                          'basePower': 1,
                          'category': 'Physical',
                          'contestType': 'Cool',
                          'flags': {},
                          'isNonstandard': 'Past',
                          'isZ': 'ghostiumz',
                          'name': 'Never-Ending Nightmare',
                          'num': 636,
                          'pp': 1,
                          'priority': 0,
                          'secondary': None,
                          'target': 'normal',
                          'type': 'Ghost'},
 'nightdaze': {'accuracy': 95,
               'basePower': 85,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Night Daze',
               'num': 539,
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'accuracy': -1}, 'chance': 40},
               'target': 'normal',
               'type': 'Dark'},
 'nightmare': {'accuracy': 100,
               'basePower': 0,
               'category': 'Status',
               'condition': {'noCopy': True,
                             'onResidual': 'function (pokemon) {\n'
                                           '\t\t\t\t'
                                           'this.damage(pokemon.baseMaxhp / '
                                           '4);\n'
                                           '\t\t\t}',
                             'onResidualOrder': 11,
                             'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tif (pokemon.status !== 'slp' "
                                        "&& !pokemon.hasAbility('comatose')) "
                                        '{\n'
                                        '\t\t\t\t\treturn false;\n'
                                        '\t\t\t\t}\n'
                                        "\t\t\t\tthis.add('-start', pokemon, "
                                        "'Nightmare');\n"
                                        '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Nightmare',
               'num': 171,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Ghost',
               'volatileStatus': 'nightmare',
               'zMove': {'boost': {'spa': 1}}},
 'nightshade': {'accuracy': 100,
                'basePower': 0,
                'category': 'Special',
                'contestType': 'Clever',
                'damage': 'level',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Night Shade',
                'num': 101,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ghost'},
 'nightslash': {'accuracy': 100,
                'basePower': 70,
                'category': 'Physical',
                'contestType': 'Cool',
                'critRatio': 2,
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Night Slash',
                'num': 400,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dark'},
 'nobleroar': {'accuracy': 100,
               'basePower': 0,
               'boosts': {'atk': -1, 'spa': -1},
               'category': 'Status',
               'contestType': 'Tough',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'protect': 1,
                         'reflectable': 1,
                         'sound': 1},
               'name': 'Noble Roar',
               'num': 568,
               'pp': 30,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'boost': {'def': 1}}},
 'noretreat': {'accuracy': True,
               'basePower': 0,
               'boosts': {'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1},
               'category': 'Status',
               'condition': {'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-start', pokemon, "
                                        "'move: No Retreat');\n"
                                        '\t\t\t}',
                             'onTrapPokemon': 'function (pokemon) {\n'
                                              '\t\t\t\tpokemon.tryTrap();\n'
                                              '\t\t\t}'},
               'flags': {'snatch': 1},
               'name': 'No Retreat',
               'num': 748,
               'onTry': 'function (source, target, move) {\n'
                        "\t\t\tif (source.volatiles['noretreat'])\n"
                        '\t\t\t\treturn false;\n'
                        "\t\t\tif (source.volatiles['trapped']) {\n"
                        '\t\t\t\tdelete move.volatileStatus;\n'
                        '\t\t\t}\n'
                        '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Fighting',
               'volatileStatus': 'noretreat'},
 'nuzzle': {'accuracy': 100,
            'basePower': 20,
            'category': 'Physical',
            'contestType': 'Cute',
            'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
            'name': 'Nuzzle',
            'num': 609,
            'pp': 20,
            'priority': 0,
            'secondary': {'chance': 100, 'status': 'par'},
            'target': 'normal',
            'type': 'Electric'},
 'oblivionwing': {'accuracy': 100,
                  'basePower': 80,
                  'category': 'Special',
                  'contestType': 'Cool',
                  'drain': [3, 4],
                  'flags': {'distance': 1,
                            'heal': 1,
                            'mirror': 1,
                            'protect': 1},
                  'name': 'Oblivion Wing',
                  'num': 613,
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'any',
                  'type': 'Flying'},
 'obstruct': {'accuracy': 100,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 1,
                            'onHit': 'function (target, source, move) {\n'
                                     '\t\t\t\tif (move.isZOrMaxPowered && '
                                     'this.checkMoveMakesContact(move, source, '
                                     'target)) {\n'
                                     '\t\t\t\t\tthis.boost({ def: -2 }, '
                                     'source, target, '
                                     'this.dex.getActiveMove("Obstruct"));\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}',
                            'onStart': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-singleturn', "
                                       "target, 'Protect');\n"
                                       '\t\t\t}',
                            'onTryHit': 'function (target, source, move) {\n'
                                        "\t\t\t\tif (!move.flags['protect'] || "
                                        "move.category === 'Status') {\n"
                                        "\t\t\t\t\tif (['gmaxoneblow', "
                                        "'gmaxrapidflow'].includes(move.id))\n"
                                        '\t\t\t\t\t\treturn;\n'
                                        '\t\t\t\t\tif (move.isZ || '
                                        'move.isMax)\n'
                                        '\t\t\t\t\t\t'
                                        'target.getMoveHitData(move).zBrokeProtect '
                                        '= true;\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif (move.smartTarget) {\n'
                                        '\t\t\t\t\tmove.smartTarget = false;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\telse {\n'
                                        "\t\t\t\t\tthis.add('-activate', "
                                        "target, 'move: Protect');\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tvar lockedmove = '
                                        "source.getVolatile('lockedmove');\n"
                                        '\t\t\t\tif (lockedmove) {\n'
                                        '\t\t\t\t\t// Outrage counter is '
                                        'reset\n'
                                        '\t\t\t\t\tif '
                                        "(source.volatiles['lockedmove'].duration "
                                        '=== 2) {\n'
                                        '\t\t\t\t\t\tdelete '
                                        "source.volatiles['lockedmove'];\n"
                                        '\t\t\t\t\t}\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif '
                                        '(this.checkMoveMakesContact(move, '
                                        'source, target)) {\n'
                                        '\t\t\t\t\tthis.boost({ def: -2 }, '
                                        'source, target, '
                                        'this.dex.getActiveMove("Obstruct"));\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\treturn this.NOT_FAIL;\n'
                                        '\t\t\t}',
                            'onTryHitPriority': 3},
              'flags': {},
              'name': 'Obstruct',
              'num': 792,
              'onHit': 'function (pokemon) {\n'
                       "\t\t\tpokemon.addVolatile('stall');\n"
                       '\t\t}',
              'onPrepareHit': 'function (pokemon) {\n'
                              '\t\t\treturn !!this.queue.willAct() && '
                              "this.runEvent('StallMove', pokemon);\n"
                              '\t\t}',
              'pp': 10,
              'priority': 4,
              'secondary': None,
              'stallingMove': True,
              'target': 'self',
              'type': 'Dark',
              'volatileStatus': 'obstruct'},
 'oceanicoperetta': {'accuracy': True,
                     'basePower': 195,
                     'category': 'Special',
                     'contestType': 'Cool',
                     'flags': {},
                     'isNonstandard': 'Past',
                     'isZ': 'primariumz',
                     'name': 'Oceanic Operetta',
                     'num': 697,
                     'pp': 1,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Water'},
 'octazooka': {'accuracy': 85,
               'basePower': 65,
               'category': 'Special',
               'contestType': 'Tough',
               'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
               'name': 'Octazooka',
               'num': 190,
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'accuracy': -1}, 'chance': 50},
               'target': 'normal',
               'type': 'Water'},
 'octolock': {'accuracy': 100,
              'basePower': 0,
              'category': 'Status',
              'condition': {'onResidual': 'function (pokemon) {\n'
                                          '\t\t\t\tvar source = '
                                          'this.effectState.source;\n'
                                          '\t\t\t\tif (source && '
                                          '(!source.isActive || source.hp <= 0 '
                                          '|| !source.activeTurns)) {\n'
                                          '\t\t\t\t\tdelete '
                                          "pokemon.volatiles['octolock'];\n"
                                          "\t\t\t\t\tthis.add('-end', pokemon, "
                                          "'Octolock', '[partiallytrapped]', "
                                          "'[silent]');\n"
                                          '\t\t\t\t\treturn;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\tthis.boost({ def: -1, spd: '
                                          '-1 }, pokemon, source, '
                                          "this.dex.getActiveMove('octolock'));\n"
                                          '\t\t\t}',
                            'onResidualOrder': 14,
                            'onStart': 'function (pokemon, source) {\n'
                                       "\t\t\t\tthis.add('-start', pokemon, "
                                       "'move: Octolock', '[of] ' + source);\n"
                                       '\t\t\t}',
                            'onTrapPokemon': 'function (pokemon) {\n'
                                             '\t\t\t\tif '
                                             '(this.effectState.source && '
                                             'this.effectState.source.isActive)\n'
                                             '\t\t\t\t\tpokemon.tryTrap();\n'
                                             '\t\t\t}'},
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Octolock',
              'num': 753,
              'onTryImmunity': 'function (target) {\n'
                               "\t\t\treturn this.dex.getImmunity('trapped', "
                               'target);\n'
                               '\t\t}',
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Fighting',
              'volatileStatus': 'octolock'},
 'odorsleuth': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'mystery': 1,
                          'protect': 1,
                          'reflectable': 1},
                'isNonstandard': 'Past',
                'name': 'Odor Sleuth',
                'num': 316,
                'onTryHit': 'function (target) {\n'
                            "\t\t\tif (target.volatiles['miracleeye'])\n"
                            '\t\t\t\treturn false;\n'
                            '\t\t}',
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal',
                'volatileStatus': 'foresight',
                'zMove': {'boost': {'atk': 1}}},
 'ominouswind': {'accuracy': 100,
                 'basePower': 60,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Ominous Wind',
                 'num': 466,
                 'pp': 5,
                 'priority': 0,
                 'secondary': {'chance': 10,
                               'self': {'boosts': {'atk': 1,
                                                   'def': 1,
                                                   'spa': 1,
                                                   'spd': 1,
                                                   'spe': 1}}},
                 'target': 'normal',
                 'type': 'Ghost'},
 'originpulse': {'accuracy': 85,
                 'basePower': 110,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'protect': 1, 'pulse': 1},
                 'name': 'Origin Pulse',
                 'num': 618,
                 'pp': 10,
                 'priority': 0,
                 'target': 'allAdjacentFoes',
                 'type': 'Water'},
 'outrage': {'accuracy': 100,
             'basePower': 120,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Outrage',
             'num': 200,
             'onAfterMove': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.volatiles['lockedmove'] && "
                            "pokemon.volatiles['lockedmove'].duration === 1) "
                            '{\n'
                            "\t\t\t\tpokemon.removeVolatile('lockedmove');\n"
                            '\t\t\t}\n'
                            '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'self': {'volatileStatus': 'lockedmove'},
             'target': 'randomNormal',
             'type': 'Dragon'},
 'overdrive': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
               'name': 'Overdrive',
               'num': 786,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Electric'},
 'overheat': {'accuracy': 90,
              'basePower': 130,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Overheat',
              'num': 315,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'self': {'boosts': {'spa': -2}},
              'target': 'normal',
              'type': 'Fire'},
 'painsplit': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
               'name': 'Pain Split',
               'num': 220,
               'onHit': 'function (target, pokemon) {\n'
                        '\t\t\tvar targetHP = target.getUndynamaxedHP();\n'
                        '\t\t\tvar averagehp = Math.floor((targetHP + '
                        'pokemon.hp) / 2) || 1;\n'
                        '\t\t\tvar targetChange = targetHP - averagehp;\n'
                        '\t\t\ttarget.sethp(target.hp - targetChange);\n'
                        "\t\t\tthis.add('-sethp', target, target.getHealth, "
                        "'[from] move: Pain Split', '[silent]');\n"
                        '\t\t\tpokemon.sethp(averagehp);\n'
                        "\t\t\tthis.add('-sethp', pokemon, pokemon.getHealth, "
                        "'[from] move: Pain Split');\n"
                        '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'boost': {'def': 1}}},
 'paleowave': {'accuracy': 100,
               'basePower': 85,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'isNonstandard': 'CAP',
               'name': 'Paleo Wave',
               'num': 0,
               'pp': 15,
               'priority': 0,
               'secondary': {'boosts': {'atk': -1}, 'chance': 20},
               'target': 'normal',
               'type': 'Rock'},
 'paraboliccharge': {'accuracy': 100,
                     'basePower': 65,
                     'category': 'Special',
                     'contestType': 'Clever',
                     'drain': [1, 2],
                     'flags': {'heal': 1, 'mirror': 1, 'protect': 1},
                     'name': 'Parabolic Charge',
                     'num': 570,
                     'pp': 20,
                     'priority': 0,
                     'secondary': None,
                     'target': 'allAdjacent',
                     'type': 'Electric'},
 'partingshot': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Cool',
                 'flags': {'authentic': 1,
                           'mirror': 1,
                           'protect': 1,
                           'reflectable': 1,
                           'sound': 1},
                 'name': 'Parting Shot',
                 'num': 575,
                 'onHit': 'function (target, source, move) {\n'
                          '\t\t\tvar success = this.boost({ atk: -1, spa: -1 '
                          '}, target, source);\n'
                          '\t\t\tif (!success && '
                          "!target.hasAbility('mirrorarmor')) {\n"
                          '\t\t\t\tdelete move.selfSwitch;\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'selfSwitch': True,
                 'target': 'normal',
                 'type': 'Dark',
                 'zMove': {'effect': 'healreplacement'}},
 'payback': {'accuracy': 100,
             'basePower': 50,
             'basePowerCallback': 'function (pokemon, target, move) {\n'
                                  '\t\t\tif (target.newlySwitched || '
                                  'this.queue.willMove(target)) {\n'
                                  "\t\t\t\tthis.debug('Payback NOT boosted');\n"
                                  '\t\t\t\treturn move.basePower;\n'
                                  '\t\t\t}\n'
                                  "\t\t\tthis.debug('Payback damage boost');\n"
                                  '\t\t\treturn move.basePower * 2;\n'
                                  '\t\t}',
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Payback',
             'num': 371,
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark'},
 'payday': {'accuracy': 100,
            'basePower': 40,
            'category': 'Physical',
            'contestType': 'Clever',
            'flags': {'mirror': 1, 'protect': 1},
            'name': 'Pay Day',
            'num': 6,
            'onHit': 'function () {\n'
                     "\t\t\tthis.add('-fieldactivate', 'move: Pay Day');\n"
                     '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal'},
 'peck': {'accuracy': 100,
          'basePower': 35,
          'category': 'Physical',
          'contestType': 'Cool',
          'flags': {'contact': 1, 'distance': 1, 'mirror': 1, 'protect': 1},
          'name': 'Peck',
          'num': 64,
          'pp': 35,
          'priority': 0,
          'secondary': None,
          'target': 'any',
          'type': 'Flying'},
 'perishsong': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 4,
                              'onEnd': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-start', target, "
                                       "'perish0');\n"
                                       '\t\t\t\ttarget.faint();\n'
                                       '\t\t\t}',
                              'onResidual': 'function (pokemon) {\n'
                                            '\t\t\t\tvar duration = '
                                            "pokemon.volatiles['perishsong'].duration;\n"
                                            "\t\t\t\tthis.add('-start', "
                                            "pokemon, 'perish' + duration);\n"
                                            '\t\t\t}',
                              'onResidualOrder': 24},
                'contestType': 'Beautiful',
                'flags': {'authentic': 1, 'distance': 1, 'sound': 1},
                'name': 'Perish Song',
                'num': 195,
                'onHitField': 'function (target, source, move) {\n'
                              '\t\t\tvar result = false;\n'
                              '\t\t\tvar message = false;\n'
                              '\t\t\tfor (var _i = 0, _a = '
                              'this.getAllActive(); _i < _a.length; _i++) {\n'
                              '\t\t\t\tvar pokemon = _a[_i];\n'
                              "\t\t\t\tif (this.runEvent('Invulnerability', "
                              'pokemon, source, move) === false) {\n'
                              "\t\t\t\t\tthis.add('-miss', source, pokemon);\n"
                              '\t\t\t\t\tresult = true;\n'
                              '\t\t\t\t}\n'
                              "\t\t\t\telse if (this.runEvent('TryHit', "
                              'pokemon, source, move) === null) {\n'
                              '\t\t\t\t\tresult = true;\n'
                              '\t\t\t\t}\n'
                              '\t\t\t\telse if '
                              "(!pokemon.volatiles['perishsong']) {\n"
                              "\t\t\t\t\tpokemon.addVolatile('perishsong');\n"
                              "\t\t\t\t\tthis.add('-start', pokemon, "
                              "'perish3', '[silent]');\n"
                              '\t\t\t\t\tresult = true;\n'
                              '\t\t\t\t\tmessage = true;\n'
                              '\t\t\t\t}\n'
                              '\t\t\t}\n'
                              '\t\t\tif (!result)\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\tif (message)\n'
                              "\t\t\t\tthis.add('-fieldactivate', 'move: "
                              "Perish Song');\n"
                              '\t\t}',
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'all',
                'type': 'Normal',
                'zMove': {'effect': 'clearnegativeboost'}},
 'petalblizzard': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Physical',
                   'contestType': 'Beautiful',
                   'flags': {'mirror': 1, 'protect': 1},
                   'name': 'Petal Blizzard',
                   'num': 572,
                   'pp': 15,
                   'priority': 0,
                   'secondary': None,
                   'target': 'allAdjacent',
                   'type': 'Grass'},
 'petaldance': {'accuracy': 100,
                'basePower': 120,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'contact': 1, 'dance': 1, 'mirror': 1, 'protect': 1},
                'name': 'Petal Dance',
                'num': 80,
                'onAfterMove': 'function (pokemon) {\n'
                               "\t\t\tif (pokemon.volatiles['lockedmove'] && "
                               "pokemon.volatiles['lockedmove'].duration === "
                               '1) {\n'
                               "\t\t\t\tpokemon.removeVolatile('lockedmove');\n"
                               '\t\t\t}\n'
                               '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'self': {'volatileStatus': 'lockedmove'},
                'target': 'randomNormal',
                'type': 'Grass'},
 'phantomforce': {'accuracy': 100,
                  'basePower': 90,
                  'breaksProtect': True,
                  'category': 'Physical',
                  'condition': {'duration': 2, 'onInvulnerability': False},
                  'contestType': 'Cool',
                  'flags': {'charge': 1, 'contact': 1, 'mirror': 1},
                  'name': 'Phantom Force',
                  'num': 566,
                  'onTryMove': 'function (attacker, defender, move) {\n'
                               '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                               '\t\t\t\treturn;\n'
                               '\t\t\t}\n'
                               "\t\t\tthis.add('-prepare', attacker, "
                               'move.name);\n'
                               "\t\t\tif (!this.runEvent('ChargeMove', "
                               'attacker, defender, move)) {\n'
                               '\t\t\t\treturn;\n'
                               '\t\t\t}\n'
                               "\t\t\tattacker.addVolatile('twoturnmove', "
                               'defender);\n'
                               '\t\t\treturn null;\n'
                               '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Ghost'},
 'photongeyser': {'accuracy': 100,
                  'basePower': 100,
                  'category': 'Special',
                  'contestType': 'Cool',
                  'flags': {'mirror': 1, 'protect': 1},
                  'ignoreAbility': True,
                  'name': 'Photon Geyser',
                  'num': 722,
                  'onModifyMove': 'function (move, pokemon) {\n'
                                  "\t\t\tif (pokemon.getStat('atk', false, "
                                  "true) > pokemon.getStat('spa', false, "
                                  'true))\n'
                                  "\t\t\t\tmove.category = 'Physical';\n"
                                  '\t\t}',
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Psychic'},
 'pikapapow': {'accuracy': True,
               'basePower': 0,
               'basePowerCallback': 'function (pokemon) {\n'
                                    '\t\t\treturn '
                                    'Math.floor((pokemon.happiness * 10) / 25) '
                                    '|| 1;\n'
                                    '\t\t}',
               'category': 'Special',
               'contestType': 'Cute',
               'flags': {'protect': 1},
               'isNonstandard': 'LGPE',
               'name': 'Pika Papow',
               'num': 732,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Electric'},
 'pinmissile': {'accuracy': 95,
                'basePower': 25,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 130},
                'multihit': [2, 5],
                'name': 'Pin Missile',
                'num': 42,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Bug',
                'zMove': {'basePower': 140}},
 'plasmafists': {'accuracy': 100,
                 'basePower': 100,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                 'name': 'Plasma Fists',
                 'num': 721,
                 'pp': 15,
                 'priority': 0,
                 'pseudoWeather': 'iondeluge',
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Electric'},
 'playnice': {'accuracy': True,
              'basePower': 0,
              'boosts': {'atk': -1},
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'authentic': 1, 'mirror': 1, 'reflectable': 1},
              'name': 'Play Nice',
              'num': 589,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'boost': {'def': 1}}},
 'playrough': {'accuracy': 90,
               'basePower': 90,
               'category': 'Physical',
               'contestType': 'Cute',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Play Rough',
               'num': 583,
               'pp': 10,
               'priority': 0,
               'secondary': {'boosts': {'atk': -1}, 'chance': 10},
               'target': 'normal',
               'type': 'Fairy'},
 'pluck': {'accuracy': 100,
           'basePower': 60,
           'category': 'Physical',
           'contestType': 'Cute',
           'flags': {'contact': 1, 'distance': 1, 'mirror': 1, 'protect': 1},
           'name': 'Pluck',
           'num': 365,
           'onHit': 'function (target, source) {\n'
                    '\t\t\tvar item = target.getItem();\n'
                    '\t\t\tif (source.hp && item.isBerry && '
                    'target.takeItem(source)) {\n'
                    "\t\t\t\tthis.add('-enditem', target, item.name, '[from] "
                    "stealeat', '[move] Pluck', '[of] ' + source);\n"
                    "\t\t\t\tif (this.singleEvent('Eat', item, null, source, "
                    'null, null)) {\n'
                    "\t\t\t\t\tthis.runEvent('EatItem', source, null, null, "
                    'item);\n'
                    "\t\t\t\t\tif (item.id === 'leppaberry')\n"
                    "\t\t\t\t\t\ttarget.staleness = 'external';\n"
                    '\t\t\t\t}\n'
                    '\t\t\t\tif (item.onEat)\n'
                    '\t\t\t\t\tsource.ateBerry = true;\n'
                    '\t\t\t}\n'
                    '\t\t}',
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'any',
           'type': 'Flying'},
 'poisonfang': {'accuracy': 100,
                'basePower': 50,
                'category': 'Physical',
                'contestType': 'Clever',
                'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Poison Fang',
                'num': 305,
                'pp': 15,
                'priority': 0,
                'secondary': {'chance': 50, 'status': 'tox'},
                'target': 'normal',
                'type': 'Poison'},
 'poisongas': {'accuracy': 90,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'name': 'Poison Gas',
               'num': 139,
               'pp': 40,
               'priority': 0,
               'secondary': None,
               'status': 'psn',
               'target': 'allAdjacentFoes',
               'type': 'Poison',
               'zMove': {'boost': {'def': 1}}},
 'poisonjab': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Poison Jab',
               'num': 398,
               'pp': 20,
               'priority': 0,
               'secondary': {'chance': 30, 'status': 'psn'},
               'target': 'normal',
               'type': 'Poison'},
 'poisonpowder': {'accuracy': 75,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Clever',
                  'flags': {'mirror': 1,
                            'powder': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': 'Poison Powder',
                  'num': 77,
                  'pp': 35,
                  'priority': 0,
                  'secondary': None,
                  'status': 'psn',
                  'target': 'normal',
                  'type': 'Poison',
                  'zMove': {'boost': {'def': 1}}},
 'poisonsting': {'accuracy': 100,
                 'basePower': 15,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Poison Sting',
                 'num': 40,
                 'pp': 35,
                 'priority': 0,
                 'secondary': {'chance': 30, 'status': 'psn'},
                 'target': 'normal',
                 'type': 'Poison'},
 'poisontail': {'accuracy': 100,
                'basePower': 50,
                'category': 'Physical',
                'contestType': 'Clever',
                'critRatio': 2,
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Poison Tail',
                'num': 342,
                'pp': 25,
                'priority': 0,
                'secondary': {'chance': 10, 'status': 'psn'},
                'target': 'normal',
                'type': 'Poison'},
 'pollenpuff': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Cute',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'name': 'Pollen Puff',
                'num': 676,
                'onHit': 'function (target, source) {\n'
                         '\t\t\tif (source.isAlly(target)) {\n'
                         '\t\t\t\tif (!this.heal(Math.floor(target.baseMaxhp * '
                         '0.5))) {\n'
                         "\t\t\t\t\tthis.add('-immune', target);\n"
                         '\t\t\t\t}\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onTryHit': 'function (target, source, move) {\n'
                            '\t\t\tif (source.isAlly(target)) {\n'
                            '\t\t\t\tmove.basePower = 0;\n'
                            '\t\t\t\tmove.infiltrates = true;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Bug'},
 'poltergeist': {'accuracy': 90,
                 'basePower': 110,
                 'category': 'Physical',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Poltergeist',
                 'num': 809,
                 'onTry': 'function (source, target) {\n'
                          '\t\t\treturn !!target.item;\n'
                          '\t\t}',
                 'onTryHit': 'function (target, source, move) {\n'
                             "\t\t\tthis.add('-activate', target, 'move: "
                             "Poltergeist', "
                             'this.dex.items.get(target.item).name);\n'
                             '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ghost'},
 'pound': {'accuracy': 100,
           'basePower': 40,
           'category': 'Physical',
           'contestType': 'Tough',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Pound',
           'num': 1,
           'pp': 35,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal'},
 'powder': {'accuracy': 100,
            'basePower': 0,
            'category': 'Status',
            'condition': {'duration': 1,
                          'onStart': 'function (target) {\n'
                                     "\t\t\t\tthis.add('-singleturn', target, "
                                     "'Powder');\n"
                                     '\t\t\t}',
                          'onTryMove': 'function (pokemon, target, move) {\n'
                                       "\t\t\t\tif (move.type === 'Fire') {\n"
                                       "\t\t\t\t\tthis.add('-activate', "
                                       "pokemon, 'move: Powder');\n"
                                       '\t\t\t\t\t'
                                       'this.damage(this.clampIntRange(Math.round(pokemon.maxhp '
                                       '/ 4), 1));\n'
                                       '\t\t\t\t\treturn false;\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t}',
                          'onTryMovePriority': -1},
            'contestType': 'Clever',
            'flags': {'authentic': 1,
                      'mirror': 1,
                      'powder': 1,
                      'protect': 1,
                      'reflectable': 1},
            'isNonstandard': 'Past',
            'name': 'Powder',
            'num': 600,
            'pp': 20,
            'priority': 1,
            'secondary': None,
            'target': 'normal',
            'type': 'Bug',
            'volatileStatus': 'powder',
            'zMove': {'boost': {'spd': 2}}},
 'powdersnow': {'accuracy': 100,
                'basePower': 40,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Powder Snow',
                'num': 181,
                'pp': 25,
                'priority': 0,
                'secondary': {'chance': 10, 'status': 'frz'},
                'target': 'allAdjacentFoes',
                'type': 'Ice'},
 'powergem': {'accuracy': 100,
              'basePower': 80,
              'category': 'Special',
              'contestType': 'Beautiful',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Power Gem',
              'num': 408,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Rock'},
 'powersplit': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mystery': 1, 'protect': 1},
                'name': 'Power Split',
                'num': 471,
                'onHit': 'function (target, source) {\n'
                         '\t\t\tvar newatk = '
                         'Math.floor((target.storedStats.atk + '
                         'source.storedStats.atk) / 2);\n'
                         '\t\t\ttarget.storedStats.atk = newatk;\n'
                         '\t\t\tsource.storedStats.atk = newatk;\n'
                         '\t\t\tvar newspa = '
                         'Math.floor((target.storedStats.spa + '
                         'source.storedStats.spa) / 2);\n'
                         '\t\t\ttarget.storedStats.spa = newspa;\n'
                         '\t\t\tsource.storedStats.spa = newspa;\n'
                         "\t\t\tthis.add('-activate', source, 'move: Power "
                         "Split', '[of] ' + target);\n"
                         '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Psychic',
                'zMove': {'boost': {'spe': 1}}},
 'powerswap': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'protect': 1},
               'name': 'Power Swap',
               'num': 384,
               'onHit': 'function (target, source) {\n'
                        '\t\t\tvar targetBoosts = {};\n'
                        '\t\t\tvar sourceBoosts = {};\n'
                        "\t\t\tvar atkSpa = ['atk', 'spa'];\n"
                        '\t\t\tfor (var _i = 0, atkSpa_1 = atkSpa; _i < '
                        'atkSpa_1.length; _i++) {\n'
                        '\t\t\t\tvar stat = atkSpa_1[_i];\n'
                        '\t\t\t\ttargetBoosts[stat] = target.boosts[stat];\n'
                        '\t\t\t\tsourceBoosts[stat] = source.boosts[stat];\n'
                        '\t\t\t}\n'
                        '\t\t\tsource.setBoost(targetBoosts);\n'
                        '\t\t\ttarget.setBoost(sourceBoosts);\n'
                        "\t\t\tthis.add('-swapboost', source, target, 'atk, "
                        "spa', '[from] move: Power Swap');\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic',
               'zMove': {'boost': {'spe': 1}}},
 'powertrick': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'onCopy': 'function (pokemon) {\n'
                                        '\t\t\t\tvar newatk = '
                                        'pokemon.storedStats.def;\n'
                                        '\t\t\t\tvar newdef = '
                                        'pokemon.storedStats.atk;\n'
                                        '\t\t\t\tpokemon.storedStats.atk = '
                                        'newatk;\n'
                                        '\t\t\t\tpokemon.storedStats.def = '
                                        'newdef;\n'
                                        '\t\t\t}',
                              'onEnd': 'function (pokemon) {\n'
                                       "\t\t\t\tthis.add('-end', pokemon, "
                                       "'Power Trick');\n"
                                       '\t\t\t\tvar newatk = '
                                       'pokemon.storedStats.def;\n'
                                       '\t\t\t\tvar newdef = '
                                       'pokemon.storedStats.atk;\n'
                                       '\t\t\t\tpokemon.storedStats.atk = '
                                       'newatk;\n'
                                       '\t\t\t\tpokemon.storedStats.def = '
                                       'newdef;\n'
                                       '\t\t\t}',
                              'onRestart': 'function (pokemon) {\n'
                                           '\t\t\t\t'
                                           "pokemon.removeVolatile('Power "
                                           "Trick');\n"
                                           '\t\t\t}',
                              'onStart': 'function (pokemon) {\n'
                                         "\t\t\t\tthis.add('-start', pokemon, "
                                         "'Power Trick');\n"
                                         '\t\t\t\tvar newatk = '
                                         'pokemon.storedStats.def;\n'
                                         '\t\t\t\tvar newdef = '
                                         'pokemon.storedStats.atk;\n'
                                         '\t\t\t\tpokemon.storedStats.atk = '
                                         'newatk;\n'
                                         '\t\t\t\tpokemon.storedStats.def = '
                                         'newdef;\n'
                                         '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'snatch': 1},
                'name': 'Power Trick',
                'num': 379,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Psychic',
                'volatileStatus': 'powertrick',
                'zMove': {'boost': {'atk': 1}}},
 'powertrip': {'accuracy': 100,
               'basePower': 20,
               'basePowerCallback': 'function (pokemon, target, move) {\n'
                                    '\t\t\treturn move.basePower + 20 * '
                                    'pokemon.positiveBoosts();\n'
                                    '\t\t}',
               'category': 'Physical',
               'contestType': 'Clever',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Power Trip',
               'num': 681,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Dark',
               'zMove': {'basePower': 160}},
 'poweruppunch': {'accuracy': 100,
                  'basePower': 40,
                  'category': 'Physical',
                  'contestType': 'Tough',
                  'flags': {'contact': 1,
                            'mirror': 1,
                            'protect': 1,
                            'punch': 1},
                  'name': 'Power-Up Punch',
                  'num': 612,
                  'pp': 20,
                  'priority': 0,
                  'secondary': {'chance': 100, 'self': {'boosts': {'atk': 1}}},
                  'target': 'normal',
                  'type': 'Fighting'},
 'powerwhip': {'accuracy': 85,
               'basePower': 120,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Power Whip',
               'num': 438,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'precipiceblades': {'accuracy': 85,
                     'basePower': 120,
                     'category': 'Physical',
                     'contestType': 'Cool',
                     'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                     'name': 'Precipice Blades',
                     'num': 619,
                     'pp': 10,
                     'priority': 0,
                     'target': 'allAdjacentFoes',
                     'type': 'Ground'},
 'present': {'accuracy': 90,
             'basePower': 0,
             'category': 'Physical',
             'contestType': 'Cute',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Present',
             'num': 217,
             'onModifyMove': 'function (move, pokemon, target) {\n'
                             '\t\t\tvar rand = this.random(10);\n'
                             '\t\t\tif (rand < 2) {\n'
                             '\t\t\t\tmove.heal = [1, 4];\n'
                             '\t\t\t\tmove.infiltrates = true;\n'
                             '\t\t\t}\n'
                             '\t\t\telse if (rand < 6) {\n'
                             '\t\t\t\tmove.basePower = 40;\n'
                             '\t\t\t}\n'
                             '\t\t\telse if (rand < 9) {\n'
                             '\t\t\t\tmove.basePower = 80;\n'
                             '\t\t\t}\n'
                             '\t\t\telse {\n'
                             '\t\t\t\tmove.basePower = 120;\n'
                             '\t\t\t}\n'
                             '\t\t}',
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal'},
 'prismaticlaser': {'accuracy': 100,
                    'basePower': 160,
                    'category': 'Special',
                    'contestType': 'Cool',
                    'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
                    'name': 'Prismatic Laser',
                    'num': 711,
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'self': {'volatileStatus': 'mustrecharge'},
                    'target': 'normal',
                    'type': 'Psychic'},
 'protect': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 1,
                           'onStart': 'function (target) {\n'
                                      "\t\t\t\tthis.add('-singleturn', target, "
                                      "'Protect');\n"
                                      '\t\t\t}',
                           'onTryHit': 'function (target, source, move) {\n'
                                       "\t\t\t\tif (!move.flags['protect']) {\n"
                                       "\t\t\t\t\tif (['gmaxoneblow', "
                                       "'gmaxrapidflow'].includes(move.id))\n"
                                       '\t\t\t\t\t\treturn;\n'
                                       '\t\t\t\t\tif (move.isZ || move.isMax)\n'
                                       '\t\t\t\t\t\t'
                                       'target.getMoveHitData(move).zBrokeProtect '
                                       '= true;\n'
                                       '\t\t\t\t\treturn;\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t\tif (move.smartTarget) {\n'
                                       '\t\t\t\t\tmove.smartTarget = false;\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t\telse {\n'
                                       "\t\t\t\t\tthis.add('-activate', "
                                       "target, 'move: Protect');\n"
                                       '\t\t\t\t}\n'
                                       '\t\t\t\tvar lockedmove = '
                                       "source.getVolatile('lockedmove');\n"
                                       '\t\t\t\tif (lockedmove) {\n'
                                       '\t\t\t\t\t// Outrage counter is reset\n'
                                       '\t\t\t\t\tif '
                                       "(source.volatiles['lockedmove'].duration "
                                       '=== 2) {\n'
                                       '\t\t\t\t\t\tdelete '
                                       "source.volatiles['lockedmove'];\n"
                                       '\t\t\t\t\t}\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t\treturn this.NOT_FAIL;\n'
                                       '\t\t\t}',
                           'onTryHitPriority': 3},
             'contestType': 'Cute',
             'flags': {},
             'name': 'Protect',
             'num': 182,
             'onHit': 'function (pokemon) {\n'
                      "\t\t\tpokemon.addVolatile('stall');\n"
                      '\t\t}',
             'onPrepareHit': 'function (pokemon) {\n'
                             '\t\t\treturn !!this.queue.willAct() && '
                             "this.runEvent('StallMove', pokemon);\n"
                             '\t\t}',
             'pp': 10,
             'priority': 4,
             'secondary': None,
             'stallingMove': True,
             'target': 'self',
             'type': 'Normal',
             'volatileStatus': 'protect',
             'zMove': {'effect': 'clearnegativeboost'}},
 'psybeam': {'accuracy': 100,
             'basePower': 65,
             'category': 'Special',
             'contestType': 'Beautiful',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Psybeam',
             'num': 60,
             'pp': 20,
             'priority': 0,
             'secondary': {'chance': 10, 'volatileStatus': 'confusion'},
             'target': 'normal',
             'type': 'Psychic'},
 'psychic': {'accuracy': 100,
             'basePower': 90,
             'category': 'Special',
             'contestType': 'Clever',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Psychic',
             'num': 94,
             'pp': 10,
             'priority': 0,
             'secondary': {'boosts': {'spd': -1}, 'chance': 10},
             'target': 'normal',
             'type': 'Psychic'},
 'psychicfangs': {'accuracy': 100,
                  'basePower': 85,
                  'category': 'Physical',
                  'contestType': 'Clever',
                  'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Psychic Fangs',
                  'num': 706,
                  'onTryHit': 'function (pokemon) {\n'
                              '\t\t\t// will shatter screens through sub, '
                              'before you hit\n'
                              '\t\t\t'
                              "pokemon.side.removeSideCondition('reflect');\n"
                              '\t\t\t'
                              "pokemon.side.removeSideCondition('lightscreen');\n"
                              '\t\t\t'
                              "pokemon.side.removeSideCondition('auroraveil');\n"
                              '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Psychic'},
 'psychicterrain': {'accuracy': True,
                    'basePower': 0,
                    'category': 'Status',
                    'condition': {'duration': 5,
                                  'durationCallback': 'function (source, '
                                                      'effect) {\n'
                                                      '\t\t\t\tif (source === '
                                                      'null || source === void '
                                                      '0 ? void 0 : '
                                                      "source.hasItem('terrainextender')) "
                                                      '{\n'
                                                      '\t\t\t\t\treturn 8;\n'
                                                      '\t\t\t\t}\n'
                                                      '\t\t\t\treturn 5;\n'
                                                      '\t\t\t}',
                                  'onBasePower': 'function (basePower, '
                                                 'attacker, defender, move) {\n'
                                                 '\t\t\t\tif (move.type === '
                                                 "'Psychic' && "
                                                 'attacker.isGrounded() && '
                                                 '!attacker.isSemiInvulnerable()) '
                                                 '{\n'
                                                 '\t\t\t\t\t'
                                                 "this.debug('psychic terrain "
                                                 "boost');\n"
                                                 '\t\t\t\t\treturn '
                                                 'this.chainModify([5325, '
                                                 '4096]);\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t}',
                                  'onBasePowerPriority': 6,
                                  'onFieldEnd': 'function () {\n'
                                                "\t\t\t\tthis.add('-fieldend', "
                                                "'move: Psychic Terrain');\n"
                                                '\t\t\t}',
                                  'onFieldResidualOrder': 27,
                                  'onFieldResidualSubOrder': 7,
                                  'onFieldStart': 'function (field, source, '
                                                  'effect) {\n'
                                                  '\t\t\t\tif ((effect === '
                                                  'null || effect === void 0 ? '
                                                  'void 0 : effect.effectType) '
                                                  "=== 'Ability') {\n"
                                                  '\t\t\t\t\t'
                                                  "this.add('-fieldstart', "
                                                  "'move: Psychic Terrain', "
                                                  "'[from] ability: ' + "
                                                  "effect, '[of] ' + source);\n"
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t\telse {\n'
                                                  '\t\t\t\t\t'
                                                  "this.add('-fieldstart', "
                                                  "'move: Psychic Terrain');\n"
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t}',
                                  'onTryHit': 'function (target, source, '
                                              'effect) {\n'
                                              '\t\t\t\tif (effect && '
                                              '(effect.priority <= 0.1 || '
                                              "effect.target === 'self')) {\n"
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t\tif '
                                              '(target.isSemiInvulnerable() || '
                                              'target.isAlly(source))\n'
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\tif '
                                              '(!target.isGrounded()) {\n'
                                              '\t\t\t\t\tvar baseMove = '
                                              'this.dex.moves.get(effect.id);\n'
                                              '\t\t\t\t\tif (baseMove.priority '
                                              '> 0) {\n'
                                              '\t\t\t\t\t\tthis.hint("Psychic '
                                              "Terrain doesn't affect Pokemon "
                                              'immune to Ground.");\n'
                                              '\t\t\t\t\t}\n'
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\t}\n'
                                              "\t\t\t\tthis.add('-activate', "
                                              "target, 'move: Psychic "
                                              "Terrain');\n"
                                              '\t\t\t\treturn null;\n'
                                              '\t\t\t}',
                                  'onTryHitPriority': 4},
                    'contestType': 'Clever',
                    'flags': {'nonsky': 1},
                    'name': 'Psychic Terrain',
                    'num': 678,
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'all',
                    'terrain': 'psychicterrain',
                    'type': 'Psychic',
                    'zMove': {'boost': {'spa': 1}}},
 'psychoboost': {'accuracy': 90,
                 'basePower': 140,
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Psycho Boost',
                 'num': 354,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'boosts': {'spa': -2}},
                 'target': 'normal',
                 'type': 'Psychic'},
 'psychocut': {'accuracy': 100,
               'basePower': 70,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Psycho Cut',
               'num': 427,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic'},
 'psychoshift': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Psycho Shift',
                 'num': 375,
                 'onTryHit': 'function (target, source, move) {\n'
                             '\t\t\tif (!source.status)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\tmove.status = source.status;\n'
                             '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'self': {'onHit': 'function (pokemon) {\n'
                                   '\t\t\t\tpokemon.cureStatus();\n'
                                   '\t\t\t}'},
                 'target': 'normal',
                 'type': 'Psychic',
                 'zMove': {'boost': {'spa': 2}}},
 'psychup': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'authentic': 1, 'mystery': 1},
             'name': 'Psych Up',
             'num': 244,
             'onHit': 'function (target, source) {\n'
                      '\t\t\tvar i;\n'
                      '\t\t\tfor (i in target.boosts) {\n'
                      '\t\t\t\tsource.boosts[i] = target.boosts[i];\n'
                      '\t\t\t}\n'
                      "\t\t\tvar volatilesToCopy = ['focusenergy', "
                      "'gmaxchistrike', 'laserfocus'];\n"
                      '\t\t\tfor (var _i = 0, volatilesToCopy_1 = '
                      'volatilesToCopy; _i < volatilesToCopy_1.length; _i++) '
                      '{\n'
                      '\t\t\t\tvar volatile = volatilesToCopy_1[_i];\n'
                      '\t\t\t\tif (target.volatiles[volatile]) {\n'
                      '\t\t\t\t\tsource.addVolatile(volatile);\n'
                      "\t\t\t\t\tif (volatile === 'gmaxchistrike')\n"
                      '\t\t\t\t\t\tsource.volatiles[volatile].layers = '
                      'target.volatiles[volatile].layers;\n'
                      '\t\t\t\t}\n'
                      '\t\t\t\telse {\n'
                      '\t\t\t\t\tsource.removeVolatile(volatile);\n'
                      '\t\t\t\t}\n'
                      '\t\t\t}\n'
                      "\t\t\tthis.add('-copyboost', source, target, '[from] "
                      "move: Psych Up');\n"
                      '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'zMove': {'effect': 'heal'}},
 'psyshock': {'accuracy': 100,
              'basePower': 80,
              'category': 'Special',
              'contestType': 'Beautiful',
              'defensiveCategory': 'Physical',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Psyshock',
              'num': 473,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Psychic'},
 'psystrike': {'accuracy': 100,
               'basePower': 100,
               'category': 'Special',
               'contestType': 'Cool',
               'defensiveCategory': 'Physical',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Psystrike',
               'num': 540,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic'},
 'psywave': {'accuracy': 100,
             'basePower': 0,
             'category': 'Special',
             'contestType': 'Clever',
             'damageCallback': 'function (pokemon) {\n'
                               '\t\t\treturn (this.random(50, 151) * '
                               'pokemon.level) / 100;\n'
                               '\t\t}',
             'flags': {'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Psywave',
             'num': 149,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Psychic'},
 'pulverizingpancake': {'accuracy': True,
                        'basePower': 210,
                        'category': 'Physical',
                        'contestType': 'Cool',
                        'flags': {'contact': 1},
                        'isNonstandard': 'Past',
                        'isZ': 'snorliumz',
                        'name': 'Pulverizing Pancake',
                        'num': 701,
                        'pp': 1,
                        'priority': 0,
                        'secondary': None,
                        'target': 'normal',
                        'type': 'Normal'},
 'punishment': {'accuracy': 100,
                'basePower': 0,
                'basePowerCallback': 'function (pokemon, target) {\n'
                                     '\t\t\tvar power = 60 + 20 * '
                                     'target.positiveBoosts();\n'
                                     '\t\t\tif (power > 200)\n'
                                     '\t\t\t\tpower = 200;\n'
                                     '\t\t\treturn power;\n'
                                     '\t\t}',
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'maxMove': {'basePower': 130},
                'name': 'Punishment',
                'num': 386,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dark',
                'zMove': {'basePower': 160}},
 'purify': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Beautiful',
            'flags': {'heal': 1, 'protect': 1, 'reflectable': 1},
            'name': 'Purify',
            'num': 685,
            'onHit': 'function (target, source) {\n'
                     '\t\t\tif (!target.cureStatus())\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\tthis.heal(Math.ceil(source.maxhp * 0.5), source);\n'
                     '\t\t}',
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Poison',
            'zMove': {'boost': {'atk': 1,
                                'def': 1,
                                'spa': 1,
                                'spd': 1,
                                'spe': 1}}},
 'pursuit': {'accuracy': 100,
             'basePower': 40,
             'basePowerCallback': 'function (pokemon, target, move) {\n'
                                  "\t\t\t// You can't get here unless the "
                                  'pursuit succeeds\n'
                                  '\t\t\tif (target.beingCalledBack || '
                                  'target.switchFlag) {\n'
                                  "\t\t\t\tthis.debug('Pursuit damage "
                                  "boost');\n"
                                  '\t\t\t\treturn move.basePower * 2;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn move.basePower;\n'
                                  '\t\t}',
             'beforeTurnCallback': 'function (pokemon) {\n'
                                   '\t\t\tfor (var _i = 0, _a = this.sides; _i '
                                   '< _a.length; _i++) {\n'
                                   '\t\t\t\tvar side = _a[_i];\n'
                                   '\t\t\t\tif (side.hasAlly(pokemon))\n'
                                   '\t\t\t\t\tcontinue;\n'
                                   "\t\t\t\tside.addSideCondition('pursuit', "
                                   'pokemon);\n'
                                   '\t\t\t\tvar data = '
                                   "side.getSideConditionData('pursuit');\n"
                                   '\t\t\t\tif (!data.sources) {\n'
                                   '\t\t\t\t\tdata.sources = [];\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t\tdata.sources.push(pokemon);\n'
                                   '\t\t\t}\n'
                                   '\t\t}',
             'category': 'Physical',
             'condition': {'duration': 1,
                           'onBeforeSwitchOut': 'function (pokemon) {\n'
                                                "\t\t\t\tthis.debug('Pursuit "
                                                "start');\n"
                                                '\t\t\t\tvar alreadyAdded = '
                                                'false;\n'
                                                '\t\t\t\t'
                                                "pokemon.removeVolatile('destinybond');\n"
                                                '\t\t\t\tfor (var _i = 0, _a = '
                                                'this.effectState.sources; _i '
                                                '< _a.length; _i++) {\n'
                                                '\t\t\t\t\tvar source = '
                                                '_a[_i];\n'
                                                '\t\t\t\t\tif '
                                                '(!this.queue.cancelMove(source) '
                                                '|| !source.hp)\n'
                                                '\t\t\t\t\t\tcontinue;\n'
                                                '\t\t\t\t\tif (!alreadyAdded) '
                                                '{\n'
                                                '\t\t\t\t\t\t'
                                                "this.add('-activate', "
                                                "pokemon, 'move: Pursuit');\n"
                                                '\t\t\t\t\t\talreadyAdded = '
                                                'true;\n'
                                                '\t\t\t\t\t}\n'
                                                '\t\t\t\t\t// Run through each '
                                                'action in queue to check if '
                                                'the Pursuit user is supposed '
                                                'to Mega Evolve this turn.\n'
                                                '\t\t\t\t\t// If it is, then '
                                                'Mega Evolve before moving.\n'
                                                '\t\t\t\t\tif '
                                                '(source.canMegaEvo || '
                                                'source.canUltraBurst) {\n'
                                                '\t\t\t\t\t\tfor (var _b = 0, '
                                                '_c = this.queue.entries(); _b '
                                                '< _c.length; _b++) {\n'
                                                '\t\t\t\t\t\t\tvar _d = '
                                                '_c[_b], actionIndex = _d[0], '
                                                'action = _d[1];\n'
                                                '\t\t\t\t\t\t\tif '
                                                '(action.pokemon === source && '
                                                "action.choice === 'megaEvo') "
                                                '{\n'
                                                '\t\t\t\t\t\t\t\t'
                                                'this.actions.runMegaEvo(source);\n'
                                                '\t\t\t\t\t\t\t\t'
                                                'this.queue.list.splice(actionIndex, '
                                                '1);\n'
                                                '\t\t\t\t\t\t\t\tbreak;\n'
                                                '\t\t\t\t\t\t\t}\n'
                                                '\t\t\t\t\t\t}\n'
                                                '\t\t\t\t\t}\n'
                                                '\t\t\t\t\t'
                                                "this.actions.runMove('pursuit', "
                                                'source, '
                                                'source.getLocOf(pokemon));\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Pursuit',
             'num': 228,
             'onModifyMove': 'function (move, source, target) {\n'
                             '\t\t\tif ((target === null || target === void 0 '
                             '? void 0 : target.beingCalledBack) || (target '
                             '=== null || target === void 0 ? void 0 : '
                             'target.switchFlag))\n'
                             '\t\t\t\tmove.accuracy = true;\n'
                             '\t\t}',
             'onTryHit': 'function (target, pokemon) {\n'
                         "\t\t\ttarget.side.removeSideCondition('pursuit');\n"
                         '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark'},
 'pyroball': {'accuracy': 90,
              'basePower': 120,
              'category': 'Physical',
              'flags': {'bullet': 1, 'defrost': 1, 'mirror': 1, 'protect': 1},
              'name': 'Pyro Ball',
              'num': 780,
              'pp': 5,
              'priority': 0,
              'secondary': {'chance': 10, 'status': 'brn'},
              'target': 'normal',
              'type': 'Fire'},
 'quash': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Clever',
           'flags': {'mirror': 1, 'protect': 1},
           'name': 'Quash',
           'num': 511,
           'onHit': 'function (target) {\n'
                    '\t\t\tif (this.activePerHalf === 1)\n'
                    '\t\t\t\treturn false; // fails in singles\n'
                    '\t\t\tvar action = this.queue.willMove(target);\n'
                    '\t\t\tif (!action)\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\taction.order = 201;\n'
                    "\t\t\tthis.add('-activate', target, 'move: Quash');\n"
                    '\t\t}',
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Dark',
           'zMove': {'boost': {'spe': 1}}},
 'quickattack': {'accuracy': 100,
                 'basePower': 40,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Quick Attack',
                 'num': 98,
                 'pp': 30,
                 'priority': 1,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'quickguard': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 1,
                              'onSideStart': 'function (target, source) {\n'
                                             "\t\t\t\tthis.add('-singleturn', "
                                             "source, 'Quick Guard');\n"
                                             '\t\t\t}',
                              'onTryHit': 'function (target, source, move) {\n'
                                          '\t\t\t\t// Quick Guard blocks moves '
                                          'with positive priority, even those '
                                          'given increased priority by '
                                          'Prankster or Gale Wings.\n'
                                          '\t\t\t\t// (e.g. it blocks 0 '
                                          'priority moves boosted by Prankster '
                                          'or Gale Wings; Quick Claw/Custap '
                                          'Berry do not count)\n'
                                          '\t\t\t\tif (move.priority <= 0.1)\n'
                                          '\t\t\t\t\treturn;\n'
                                          "\t\t\t\tif (!move.flags['protect']) "
                                          '{\n'
                                          "\t\t\t\t\tif (['gmaxoneblow', "
                                          "'gmaxrapidflow'].includes(move.id))\n"
                                          '\t\t\t\t\t\treturn;\n'
                                          '\t\t\t\t\tif (move.isZ || '
                                          'move.isMax)\n'
                                          '\t\t\t\t\t\t'
                                          'target.getMoveHitData(move).zBrokeProtect '
                                          '= true;\n'
                                          '\t\t\t\t\treturn;\n'
                                          '\t\t\t\t}\n'
                                          "\t\t\t\tthis.add('-activate', "
                                          "target, 'move: Quick Guard');\n"
                                          '\t\t\t\tvar lockedmove = '
                                          "source.getVolatile('lockedmove');\n"
                                          '\t\t\t\tif (lockedmove) {\n'
                                          '\t\t\t\t\t// Outrage counter is '
                                          'reset\n'
                                          '\t\t\t\t\tif '
                                          "(source.volatiles['lockedmove'].duration "
                                          '=== 2) {\n'
                                          '\t\t\t\t\t\tdelete '
                                          "source.volatiles['lockedmove'];\n"
                                          '\t\t\t\t\t}\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\treturn this.NOT_FAIL;\n'
                                          '\t\t\t}',
                              'onTryHitPriority': 4},
                'contestType': 'Cool',
                'flags': {'snatch': 1},
                'name': 'Quick Guard',
                'num': 501,
                'onHitSide': 'function (side, source) {\n'
                             "\t\t\tsource.addVolatile('stall');\n"
                             '\t\t}',
                'onTry': 'function () {\n'
                         '\t\t\treturn !!this.queue.willAct();\n'
                         '\t\t}',
                'pp': 15,
                'priority': 3,
                'secondary': None,
                'sideCondition': 'quickguard',
                'target': 'allySide',
                'type': 'Fighting',
                'zMove': {'boost': {'def': 1}}},
 'quiverdance': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'spa': 1, 'spd': 1, 'spe': 1},
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {'dance': 1, 'snatch': 1},
                 'name': 'Quiver Dance',
                 'num': 483,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Bug',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'rage': {'accuracy': 100,
          'basePower': 20,
          'category': 'Physical',
          'condition': {'onBeforeMove': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.debug('removing Rage "
                                        "before attack');\n"
                                        '\t\t\t\t'
                                        "pokemon.removeVolatile('rage');\n"
                                        '\t\t\t}',
                        'onBeforeMovePriority': 100,
                        'onHit': 'function (target, source, move) {\n'
                                 '\t\t\t\tif (target !== source && '
                                 "move.category !== 'Status') {\n"
                                 '\t\t\t\t\tthis.boost({ atk: 1 });\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}',
                        'onStart': 'function (pokemon) {\n'
                                   "\t\t\t\tthis.add('-singlemove', pokemon, "
                                   "'Rage');\n"
                                   '\t\t\t}'},
          'contestType': 'Tough',
          'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
          'isNonstandard': 'Past',
          'name': 'Rage',
          'num': 99,
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'self': {'volatileStatus': 'rage'},
          'target': 'normal',
          'type': 'Normal'},
 'ragepowder': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 1,
                              'onFoeRedirectTarget': 'function (target, '
                                                     'source, source2, move) '
                                                     '{\n'
                                                     '\t\t\t\tvar '
                                                     'ragePowderUser = '
                                                     'this.effectState.target;\n'
                                                     '\t\t\t\tif '
                                                     '(ragePowderUser.isSkyDropped())\n'
                                                     '\t\t\t\t\treturn;\n'
                                                     '\t\t\t\tif '
                                                     "(source.runStatusImmunity('powder') "
                                                     '&& '
                                                     'this.validTarget(ragePowderUser, '
                                                     'source, move.target)) {\n'
                                                     '\t\t\t\t\tif '
                                                     '(move.smartTarget)\n'
                                                     '\t\t\t\t\t\t'
                                                     'move.smartTarget = '
                                                     'false;\n'
                                                     '\t\t\t\t\t'
                                                     'this.debug("Rage Powder '
                                                     'redirected target of '
                                                     'move");\n'
                                                     '\t\t\t\t\treturn '
                                                     'ragePowderUser;\n'
                                                     '\t\t\t\t}\n'
                                                     '\t\t\t}',
                              'onFoeRedirectTargetPriority': 1,
                              'onStart': 'function (pokemon) {\n'
                                         "\t\t\t\tthis.add('-singleturn', "
                                         "pokemon, 'move: Rage Powder');\n"
                                         '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'powder': 1},
                'name': 'Rage Powder',
                'num': 476,
                'onTry': 'function (source) {\n'
                         '\t\t\treturn this.activePerHalf > 1;\n'
                         '\t\t}',
                'pp': 20,
                'priority': 2,
                'secondary': None,
                'target': 'self',
                'type': 'Bug',
                'volatileStatus': 'ragepowder',
                'zMove': {'effect': 'clearnegativeboost'}},
 'raindance': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Beautiful',
               'flags': {},
               'name': 'Rain Dance',
               'num': 240,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'all',
               'type': 'Water',
               'weather': 'RainDance',
               'zMove': {'boost': {'spe': 1}}},
 'rapidspin': {'accuracy': 100,
               'basePower': 50,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Rapid Spin',
               'num': 229,
               'onAfterHit': 'function (target, pokemon) {\n'
                             '\t\t\tif (pokemon.hp && '
                             "pokemon.removeVolatile('leechseed')) {\n"
                             "\t\t\t\tthis.add('-end', pokemon, 'Leech Seed', "
                             "'[from] move: Rapid Spin', '[of] ' + pokemon);\n"
                             '\t\t\t}\n'
                             "\t\t\tvar sideConditions = ['spikes', "
                             "'toxicspikes', 'stealthrock', 'stickyweb', "
                             "'gmaxsteelsurge'];\n"
                             '\t\t\tfor (var _i = 0, sideConditions_3 = '
                             'sideConditions; _i < sideConditions_3.length; '
                             '_i++) {\n'
                             '\t\t\t\tvar condition = sideConditions_3[_i];\n'
                             '\t\t\t\tif (pokemon.hp && '
                             'pokemon.side.removeSideCondition(condition)) {\n'
                             "\t\t\t\t\tthis.add('-sideend', pokemon.side, "
                             "this.dex.conditions.get(condition).name, '[from] "
                             "move: Rapid Spin', '[of] ' + pokemon);\n"
                             '\t\t\t\t}\n'
                             '\t\t\t}\n'
                             '\t\t\tif (pokemon.hp && '
                             "pokemon.volatiles['partiallytrapped']) {\n"
                             '\t\t\t\t'
                             "pokemon.removeVolatile('partiallytrapped');\n"
                             '\t\t\t}\n'
                             '\t\t}',
               'onAfterSubDamage': 'function (damage, target, pokemon) {\n'
                                   '\t\t\tif (pokemon.hp && '
                                   "pokemon.removeVolatile('leechseed')) {\n"
                                   "\t\t\t\tthis.add('-end', pokemon, 'Leech "
                                   "Seed', '[from] move: Rapid Spin', '[of] ' "
                                   '+ pokemon);\n'
                                   '\t\t\t}\n'
                                   "\t\t\tvar sideConditions = ['spikes', "
                                   "'toxicspikes', 'stealthrock', 'stickyweb', "
                                   "'gmaxsteelsurge'];\n"
                                   '\t\t\tfor (var _i = 0, sideConditions_4 = '
                                   'sideConditions; _i < '
                                   'sideConditions_4.length; _i++) {\n'
                                   '\t\t\t\tvar condition = '
                                   'sideConditions_4[_i];\n'
                                   '\t\t\t\tif (pokemon.hp && '
                                   'pokemon.side.removeSideCondition(condition)) '
                                   '{\n'
                                   "\t\t\t\t\tthis.add('-sideend', "
                                   'pokemon.side, '
                                   'this.dex.conditions.get(condition).name, '
                                   "'[from] move: Rapid Spin', '[of] ' + "
                                   'pokemon);\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t}\n'
                                   '\t\t\tif (pokemon.hp && '
                                   "pokemon.volatiles['partiallytrapped']) {\n"
                                   '\t\t\t\t'
                                   "pokemon.removeVolatile('partiallytrapped');\n"
                                   '\t\t\t}\n'
                                   '\t\t}',
               'pp': 40,
               'priority': 0,
               'secondary': {'chance': 100, 'self': {'boosts': {'spe': 1}}},
               'target': 'normal',
               'type': 'Normal'},
 'razorleaf': {'accuracy': 95,
               'basePower': 55,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Razor Leaf',
               'num': 75,
               'pp': 25,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Grass'},
 'razorshell': {'accuracy': 95,
                'basePower': 75,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Razor Shell',
                'num': 534,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'def': -1}, 'chance': 50},
                'target': 'normal',
                'type': 'Water'},
 'razorwind': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'charge': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Razor Wind',
               'num': 13,
               'onTryMove': 'function (attacker, defender, move) {\n'
                            '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                            "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                            'defender, move)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tattacker.addVolatile('twoturnmove', "
                            'defender);\n'
                            '\t\t\treturn null;\n'
                            '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Normal'},
 'recover': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'heal': 1, 'snatch': 1},
             'heal': [1, 2],
             'name': 'Recover',
             'num': 105,
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'effect': 'clearnegativeboost'}},
 'recycle': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'snatch': 1},
             'name': 'Recycle',
             'num': 278,
             'onHit': 'function (pokemon) {\n'
                      '\t\t\tif (pokemon.item || !pokemon.lastItem)\n'
                      '\t\t\t\treturn false;\n'
                      '\t\t\tvar item = pokemon.lastItem;\n'
                      "\t\t\tpokemon.lastItem = '';\n"
                      "\t\t\tthis.add('-item', pokemon, "
                      "this.dex.items.get(item), '[from] move: Recycle');\n"
                      '\t\t\tpokemon.setItem(item);\n'
                      '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'boost': {'spe': 2}}},
 'reflect': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'condition': {'duration': 5,
                           'durationCallback': 'function (target, source, '
                                               'effect) {\n'
                                               '\t\t\t\tif (source === null || '
                                               'source === void 0 ? void 0 : '
                                               "source.hasItem('lightclay')) "
                                               '{\n'
                                               '\t\t\t\t\treturn 8;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t\treturn 5;\n'
                                               '\t\t\t}',
                           'onAnyModifyDamage': 'function (damage, source, '
                                                'target, move) {\n'
                                                '\t\t\t\tif (target !== source '
                                                '&& '
                                                'this.effectState.target.hasAlly(target) '
                                                '&& this.getCategory(move) === '
                                                "'Physical') {\n"
                                                '\t\t\t\t\tif '
                                                '(!target.getMoveHitData(move).crit '
                                                '&& !move.infiltrates) {\n'
                                                '\t\t\t\t\t\t'
                                                "this.debug('Reflect "
                                                "weaken');\n"
                                                '\t\t\t\t\t\tif '
                                                '(this.activePerHalf > 1)\n'
                                                '\t\t\t\t\t\t\treturn '
                                                'this.chainModify([2732, '
                                                '4096]);\n'
                                                '\t\t\t\t\t\treturn '
                                                'this.chainModify(0.5);\n'
                                                '\t\t\t\t\t}\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t}',
                           'onSideEnd': 'function (side) {\n'
                                        "\t\t\t\tthis.add('-sideend', side, "
                                        "'Reflect');\n"
                                        '\t\t\t}',
                           'onSideResidualOrder': 26,
                           'onSideResidualSubOrder': 1,
                           'onSideStart': 'function (side) {\n'
                                          "\t\t\t\tthis.add('-sidestart', "
                                          "side, 'Reflect');\n"
                                          '\t\t\t}'},
             'contestType': 'Clever',
             'flags': {'snatch': 1},
             'name': 'Reflect',
             'num': 115,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'sideCondition': 'reflect',
             'target': 'allySide',
             'type': 'Psychic',
             'zMove': {'boost': {'def': 1}}},
 'reflecttype': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'authentic': 1, 'mystery': 1, 'protect': 1},
                 'name': 'Reflect Type',
                 'num': 513,
                 'onHit': 'function (target, source) {\n'
                          '\t\t\tif (source.species && (source.species.num === '
                          '493 || source.species.num === 773))\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\tvar newBaseTypes = '
                          'target.getTypes(true).filter(function (type) { '
                          "return type !== '???'; });\n"
                          '\t\t\tif (!newBaseTypes.length) {\n'
                          '\t\t\t\tif (target.addedType) {\n'
                          "\t\t\t\t\tnewBaseTypes = ['Normal'];\n"
                          '\t\t\t\t}\n'
                          '\t\t\t\telse {\n'
                          '\t\t\t\t\treturn false;\n'
                          '\t\t\t\t}\n'
                          '\t\t\t}\n'
                          "\t\t\tthis.add('-start', source, 'typechange', "
                          "'[from] move: Reflect Type', '[of] ' + target);\n"
                          '\t\t\tsource.setType(newBaseTypes);\n'
                          '\t\t\tsource.addedType = target.addedType;\n'
                          '\t\t\tsource.knownType = target.isAlly(source) && '
                          'target.knownType;\n'
                          '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'boost': {'spa': 1}}},
 'refresh': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {'snatch': 1},
             'isNonstandard': 'Past',
             'name': 'Refresh',
             'num': 287,
             'onHit': 'function (pokemon) {\n'
                      "\t\t\tif (['', 'slp', 'frz'].includes(pokemon.status))\n"
                      '\t\t\t\treturn false;\n'
                      '\t\t\tpokemon.cureStatus();\n'
                      '\t\t}',
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'effect': 'heal'}},
 'relicsong': {'accuracy': 100,
               'basePower': 75,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
               'isNonstandard': 'Past',
               'name': 'Relic Song',
               'num': 547,
               'onAfterMoveSecondarySelf': 'function (pokemon, target, move) '
                                           '{\n'
                                           '\t\t\tif (move.willChangeForme) {\n'
                                           '\t\t\t\tvar meloettaForme = '
                                           'pokemon.species.id === '
                                           "'meloettapirouette' ? '' : "
                                           "'-Pirouette';\n"
                                           '\t\t\t\t'
                                           "pokemon.formeChange('Meloetta' + "
                                           'meloettaForme, this.effect, false, '
                                           "'[msg]');\n"
                                           '\t\t\t}\n'
                                           '\t\t}',
               'onHit': 'function (target, pokemon, move) {\n'
                        '\t\t\tif (pokemon.baseSpecies.baseSpecies === '
                        "'Meloetta' && !pokemon.transformed) {\n"
                        '\t\t\t\tmove.willChangeForme = true;\n'
                        '\t\t\t}\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 10, 'status': 'slp'},
               'target': 'allAdjacentFoes',
               'type': 'Normal'},
 'rest': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Cute',
          'flags': {'heal': 1, 'snatch': 1},
          'name': 'Rest',
          'num': 156,
          'onHit': 'function (target, source, move) {\n'
                   "\t\t\tif (!target.setStatus('slp', source, move))\n"
                   '\t\t\t\treturn false;\n'
                   '\t\t\ttarget.statusState.time = 3;\n'
                   '\t\t\ttarget.statusState.startTime = 3;\n'
                   '\t\t\tthis.heal(target.maxhp); // Aesthetic only as the '
                   'healing happens after you fall asleep in-game\n'
                   '\t\t}',
          'onTry': 'function (source) {\n'
                   "\t\t\tif (source.status === 'slp' || "
                   "source.hasAbility('comatose'))\n"
                   '\t\t\t\treturn false;\n'
                   '\t\t\tif (source.hp === source.maxhp) {\n'
                   "\t\t\t\tthis.add('-fail', source, 'heal');\n"
                   '\t\t\t\treturn null;\n'
                   '\t\t\t}\n'
                   "\t\t\tif (source.hasAbility(['insomnia', 'vitalspirit'])) "
                   '{\n'
                   "\t\t\t\tthis.add('-fail', source, '[from] ability: ' + "
                   "source.getAbility().name, '[of] ' + source);\n"
                   '\t\t\t\treturn null;\n'
                   '\t\t\t}\n'
                   '\t\t}',
          'pp': 10,
          'priority': 0,
          'secondary': None,
          'target': 'self',
          'type': 'Psychic',
          'zMove': {'effect': 'clearnegativeboost'}},
 'retaliate': {'accuracy': 100,
               'basePower': 70,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Retaliate',
               'num': 514,
               'onBasePower': 'function (basePower, pokemon) {\n'
                              '\t\t\tif (pokemon.side.faintedLastTurn) {\n'
                              "\t\t\t\tthis.debug('Boosted for a faint last "
                              "turn');\n"
                              '\t\t\t\treturn this.chainModify(2);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal'},
 'return': {'accuracy': 100,
            'basePower': 0,
            'basePowerCallback': 'function (pokemon) {\n'
                                 '\t\t\treturn Math.floor((pokemon.happiness * '
                                 '10) / 25) || 1;\n'
                                 '\t\t}',
            'category': 'Physical',
            'contestType': 'Cute',
            'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
            'isNonstandard': 'Past',
            'maxMove': {'basePower': 130},
            'name': 'Return',
            'num': 216,
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'zMove': {'basePower': 160}},
 'revelationdance': {'accuracy': 100,
                     'basePower': 90,
                     'category': 'Special',
                     'contestType': 'Beautiful',
                     'flags': {'dance': 1, 'mirror': 1, 'protect': 1},
                     'isNonstandard': 'Past',
                     'name': 'Revelation Dance',
                     'num': 686,
                     'onModifyType': 'function (move, pokemon) {\n'
                                     '\t\t\tvar type = pokemon.getTypes()[0];\n'
                                     '\t\t\tif (type === "Bird")\n'
                                     '\t\t\t\ttype = "???";\n'
                                     '\t\t\tmove.type = type;\n'
                                     '\t\t}',
                     'pp': 15,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Normal'},
 'revenge': {'accuracy': 100,
             'basePower': 60,
             'basePowerCallback': 'function (pokemon, target, move) {\n'
                                  '\t\t\tvar damagedByTarget = '
                                  'pokemon.attackedBy.some(function (p) { '
                                  'return p.source === target && p.damage > 0 '
                                  '&& p.thisTurn; });\n'
                                  '\t\t\tif (damagedByTarget) {\n'
                                  "\t\t\t\tthis.debug('Boosted for getting hit "
                                  "by ' + target);\n"
                                  '\t\t\t\treturn move.basePower * 2;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn move.basePower;\n'
                                  '\t\t}',
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Revenge',
             'num': 279,
             'pp': 10,
             'priority': -4,
             'secondary': None,
             'target': 'normal',
             'type': 'Fighting'},
 'reversal': {'accuracy': 100,
              'basePower': 0,
              'basePowerCallback': 'function (pokemon, target) {\n'
                                   '\t\t\tvar ratio = pokemon.hp * 48 / '
                                   'pokemon.maxhp;\n'
                                   '\t\t\tif (ratio < 2) {\n'
                                   '\t\t\t\treturn 200;\n'
                                   '\t\t\t}\n'
                                   '\t\t\tif (ratio < 5) {\n'
                                   '\t\t\t\treturn 150;\n'
                                   '\t\t\t}\n'
                                   '\t\t\tif (ratio < 10) {\n'
                                   '\t\t\t\treturn 100;\n'
                                   '\t\t\t}\n'
                                   '\t\t\tif (ratio < 17) {\n'
                                   '\t\t\t\treturn 80;\n'
                                   '\t\t\t}\n'
                                   '\t\t\tif (ratio < 33) {\n'
                                   '\t\t\t\treturn 40;\n'
                                   '\t\t\t}\n'
                                   '\t\t\treturn 20;\n'
                                   '\t\t}',
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Reversal',
              'num': 179,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Fighting',
              'zMove': {'basePower': 160}},
 'risingvoltage': {'accuracy': 100,
                   'basePower': 70,
                   'category': 'Special',
                   'flags': {'mirror': 1, 'protect': 1},
                   'maxMove': {'basePower': 140},
                   'name': 'Rising Voltage',
                   'num': 804,
                   'onBasePower': 'function (basePower, pokemon, target) {\n'
                                  '\t\t\tif '
                                  "(this.field.isTerrain('electricterrain') && "
                                  'target.isGrounded()) {\n'
                                  "\t\t\t\tthis.debug('terrain buff');\n"
                                  '\t\t\t\treturn this.chainModify(2);\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                   'pp': 20,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Electric'},
 'roar': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Cool',
          'flags': {'authentic': 1,
                    'mirror': 1,
                    'mystery': 1,
                    'reflectable': 1,
                    'sound': 1},
          'forceSwitch': True,
          'name': 'Roar',
          'num': 46,
          'pp': 20,
          'priority': -6,
          'secondary': None,
          'target': 'normal',
          'type': 'Normal',
          'zMove': {'boost': {'def': 1}}},
 'roaroftime': {'accuracy': 90,
                'basePower': 150,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1, 'recharge': 1},
                'name': 'Roar of Time',
                'num': 459,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'volatileStatus': 'mustrecharge'},
                'target': 'normal',
                'type': 'Dragon'},
 'rockblast': {'accuracy': 90,
               'basePower': 25,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'multihit': [2, 5],
               'name': 'Rock Blast',
               'num': 350,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Rock',
               'zMove': {'basePower': 140}},
 'rockclimb': {'accuracy': 85,
               'basePower': 90,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Rock Climb',
               'num': 431,
               'pp': 20,
               'priority': 0,
               'secondary': {'chance': 20, 'volatileStatus': 'confusion'},
               'target': 'normal',
               'type': 'Normal'},
 'rockpolish': {'accuracy': True,
                'basePower': 0,
                'boosts': {'spe': 2},
                'category': 'Status',
                'contestType': 'Tough',
                'flags': {'snatch': 1},
                'name': 'Rock Polish',
                'num': 397,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Rock',
                'zMove': {'effect': 'clearnegativeboost'}},
 'rockslide': {'accuracy': 90,
               'basePower': 75,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Rock Slide',
               'num': 157,
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
               'target': 'allAdjacentFoes',
               'type': 'Rock'},
 'rocksmash': {'accuracy': 100,
               'basePower': 40,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Rock Smash',
               'num': 249,
               'pp': 15,
               'priority': 0,
               'secondary': {'boosts': {'def': -1}, 'chance': 50},
               'target': 'normal',
               'type': 'Fighting'},
 'rockthrow': {'accuracy': 90,
               'basePower': 50,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Rock Throw',
               'num': 88,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Rock'},
 'rocktomb': {'accuracy': 95,
              'basePower': 60,
              'category': 'Physical',
              'contestType': 'Clever',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Rock Tomb',
              'num': 317,
              'pp': 15,
              'priority': 0,
              'secondary': {'boosts': {'spe': -1}, 'chance': 100},
              'target': 'normal',
              'type': 'Rock'},
 'rockwrecker': {'accuracy': 90,
                 'basePower': 150,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'bullet': 1,
                           'mirror': 1,
                           'protect': 1,
                           'recharge': 1},
                 'name': 'Rock Wrecker',
                 'num': 439,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'self': {'volatileStatus': 'mustrecharge'},
                 'target': 'normal',
                 'type': 'Rock'},
 'roleplay': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'authentic': 1, 'mystery': 1},
              'name': 'Role Play',
              'num': 272,
              'onHit': 'function (target, source) {\n'
                       '\t\t\tvar oldAbility = '
                       'source.setAbility(target.ability);\n'
                       '\t\t\tif (oldAbility) {\n'
                       "\t\t\t\tthis.add('-ability', source, "
                       "source.getAbility().name, '[from] move: Role Play', "
                       "'[of] ' + target);\n"
                       '\t\t\t\treturn;\n'
                       '\t\t\t}\n'
                       '\t\t\treturn false;\n'
                       '\t\t}',
              'onTryHit': 'function (target, source) {\n'
                          '\t\t\tif (target.ability === source.ability)\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\tvar additionalBannedTargetAbilities = [\n'
                          '\t\t\t\t// Zen Mode included here for compatability '
                          'with Gen 5-6\n'
                          "\t\t\t\t'flowergift', 'forecast', 'hungerswitch', "
                          "'illusion', 'imposter', 'neutralizinggas', "
                          "'powerofalchemy', 'receiver', 'trace', "
                          "'wonderguard', 'zenmode',\n"
                          '\t\t\t];\n'
                          '\t\t\tif (target.getAbility().isPermanent || '
                          'additionalBannedTargetAbilities.includes(target.ability) '
                          '||\n'
                          '\t\t\t\tsource.getAbility().isPermanent) {\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t}',
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Psychic',
              'zMove': {'boost': {'spe': 1}}},
 'rollingkick': {'accuracy': 85,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Rolling Kick',
                 'num': 27,
                 'pp': 15,
                 'priority': 0,
                 'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                 'target': 'normal',
                 'type': 'Fighting'},
 'rollout': {'accuracy': 90,
             'basePower': 30,
             'basePowerCallback': 'function (pokemon, target, move) {\n'
                                  '\t\t\tvar bp = move.basePower;\n'
                                  "\t\t\tif (pokemon.volatiles['rollout'] && "
                                  "pokemon.volatiles['rollout'].hitCount) {\n"
                                  '\t\t\t\tbp *= Math.pow(2, '
                                  "pokemon.volatiles['rollout'].hitCount);\n"
                                  '\t\t\t}\n'
                                  "\t\t\tif (pokemon.status !== 'slp')\n"
                                  "\t\t\t\tpokemon.addVolatile('rollout');\n"
                                  "\t\t\tif (pokemon.volatiles['defensecurl']) "
                                  '{\n'
                                  '\t\t\t\tbp *= 2;\n'
                                  '\t\t\t}\n'
                                  '\t\t\tthis.debug("Rollout bp: " + bp);\n'
                                  '\t\t\treturn bp;\n'
                                  '\t\t}',
             'category': 'Physical',
             'condition': {'duration': 2,
                           'onLockMove': 'rollout',
                           'onResidual': 'function (target) {\n'
                                         '\t\t\t\tif (target.lastMove && '
                                         "target.lastMove.id === 'struggle') "
                                         '{\n'
                                         "\t\t\t\t\t// don't lock\n"
                                         '\t\t\t\t\tdelete '
                                         "target.volatiles['rollout'];\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t}',
                           'onRestart': 'function () {\n'
                                        '\t\t\t\tthis.effectState.hitCount++;\n'
                                        '\t\t\t\tif (this.effectState.hitCount '
                                        '< 5) {\n'
                                        '\t\t\t\t\tthis.effectState.duration = '
                                        '2;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                           'onStart': 'function () {\n'
                                      '\t\t\t\tthis.effectState.hitCount = 1;\n'
                                      '\t\t\t}'},
             'contestType': 'Cute',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Rollout',
             'num': 205,
             'pp': 20,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Rock'},
 'roost': {'accuracy': True,
           'basePower': 0,
           'category': 'Status',
           'condition': {'duration': 1,
                         'onResidualOrder': 25,
                         'onStart': 'function (target) {\n'
                                    "\t\t\t\tthis.add('-singleturn', target, "
                                    "'move: Roost');\n"
                                    '\t\t\t}',
                         'onType': 'function (types, pokemon) {\n'
                                   '\t\t\t\tthis.effectState.typeWas = types;\n'
                                   '\t\t\t\treturn types.filter(function '
                                   "(type) { return type !== 'Flying'; });\n"
                                   '\t\t\t}',
                         'onTypePriority': -1},
           'contestType': 'Clever',
           'flags': {'heal': 1, 'snatch': 1},
           'heal': [1, 2],
           'name': 'Roost',
           'num': 355,
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'self': {'volatileStatus': 'roost'},
           'target': 'self',
           'type': 'Flying',
           'zMove': {'effect': 'clearnegativeboost'}},
 'rototiller': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Tough',
                'flags': {'distance': 1, 'nonsky': 1},
                'isNonstandard': 'Past',
                'name': 'Rototiller',
                'num': 563,
                'onHitField': 'function (target, source) {\n'
                              '\t\t\tvar targets = [];\n'
                              '\t\t\tvar anyAirborne = false;\n'
                              '\t\t\tfor (var _i = 0, _a = '
                              'this.getAllActive(); _i < _a.length; _i++) {\n'
                              '\t\t\t\tvar pokemon = _a[_i];\n'
                              "\t\t\t\tif (!pokemon.runImmunity('Ground')) {\n"
                              "\t\t\t\t\tthis.add('-immune', pokemon);\n"
                              '\t\t\t\t\tanyAirborne = true;\n'
                              '\t\t\t\t\tcontinue;\n'
                              '\t\t\t\t}\n'
                              "\t\t\t\tif (pokemon.hasType('Grass')) {\n"
                              '\t\t\t\t\t// This move affects every grounded '
                              'Grass-type Pokemon in play.\n'
                              '\t\t\t\t\ttargets.push(pokemon);\n'
                              '\t\t\t\t}\n'
                              '\t\t\t}\n'
                              '\t\t\tif (!targets.length && !anyAirborne)\n'
                              '\t\t\t\treturn false; // Fails when there are '
                              'no grounded Grass types or airborne Pokemon\n'
                              '\t\t\tfor (var _b = 0, targets_4 = targets; _b '
                              '< targets_4.length; _b++) {\n'
                              '\t\t\t\tvar pokemon = targets_4[_b];\n'
                              '\t\t\t\tthis.boost({ atk: 1, spa: 1 }, pokemon, '
                              'source);\n'
                              '\t\t\t}\n'
                              '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'all',
                'type': 'Ground',
                'zMove': {'boost': {'atk': 1}}},
 'round': {'accuracy': 100,
           'basePower': 60,
           'basePowerCallback': 'function (target, source, move) {\n'
                                "\t\t\tif (move.sourceEffect === 'round') {\n"
                                '\t\t\t\treturn move.basePower * 2;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn move.basePower;\n'
                                '\t\t}',
           'category': 'Special',
           'contestType': 'Beautiful',
           'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
           'name': 'Round',
           'num': 496,
           'onTry': 'function (source, target, move) {\n'
                    '\t\t\tfor (var _i = 0, _a = this.queue.list; _i < '
                    '_a.length; _i++) {\n'
                    '\t\t\t\tvar action = _a[_i];\n'
                    '\t\t\t\tif (!action.pokemon || !action.move || '
                    'action.maxMove || action.zmove)\n'
                    '\t\t\t\t\tcontinue;\n'
                    "\t\t\t\tif (action.move.id === 'round') {\n"
                    '\t\t\t\t\tthis.queue.prioritizeAction(action, move);\n'
                    '\t\t\t\t\treturn;\n'
                    '\t\t\t\t}\n'
                    '\t\t\t}\n'
                    '\t\t}',
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal'},
 'sacredfire': {'accuracy': 95,
                'basePower': 100,
                'category': 'Physical',
                'contestType': 'Beautiful',
                'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
                'name': 'Sacred Fire',
                'num': 221,
                'pp': 5,
                'priority': 0,
                'secondary': {'chance': 50, 'status': 'brn'},
                'target': 'normal',
                'type': 'Fire'},
 'sacredsword': {'accuracy': 100,
                 'basePower': 90,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'ignoreDefensive': True,
                 'ignoreEvasion': True,
                 'name': 'Sacred Sword',
                 'num': 533,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fighting'},
 'safeguard': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 5,
                             'durationCallback': 'function (target, source, '
                                                 'effect) {\n'
                                                 '\t\t\t\tif (source === null '
                                                 '|| source === void 0 ? void '
                                                 '0 : '
                                                 "source.hasAbility('persistent')) "
                                                 '{\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "source, 'ability: "
                                                 "Persistent', effect);\n"
                                                 '\t\t\t\t\treturn 7;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\treturn 5;\n'
                                                 '\t\t\t}',
                             'onSetStatus': 'function (status, target, source, '
                                            'effect) {\n'
                                            '\t\t\t\tif (!effect || !source)\n'
                                            '\t\t\t\t\treturn;\n'
                                            '\t\t\t\tif (effect.id === '
                                            "'yawn')\n"
                                            '\t\t\t\t\treturn;\n'
                                            '\t\t\t\tif (effect.effectType === '
                                            "'Move' && effect.infiltrates && "
                                            '!target.isAlly(source))\n'
                                            '\t\t\t\t\treturn;\n'
                                            '\t\t\t\tif (target !== source) {\n'
                                            '\t\t\t\t\t'
                                            "this.debug('interrupting "
                                            "setStatus');\n"
                                            '\t\t\t\t\tif (effect.id === '
                                            "'synchronize' || "
                                            "(effect.effectType === 'Move' && "
                                            '!effect.secondaries)) {\n'
                                            "\t\t\t\t\t\tthis.add('-activate', "
                                            "target, 'move: Safeguard');\n"
                                            '\t\t\t\t\t}\n'
                                            '\t\t\t\t\treturn null;\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}',
                             'onSideEnd': 'function (side) {\n'
                                          "\t\t\t\tthis.add('-sideend', side, "
                                          "'Safeguard');\n"
                                          '\t\t\t}',
                             'onSideResidualOrder': 26,
                             'onSideResidualSubOrder': 3,
                             'onSideStart': 'function (side) {\n'
                                            "\t\t\t\tthis.add('-sidestart', "
                                            "side, 'Safeguard');\n"
                                            '\t\t\t}',
                             'onTryAddVolatile': 'function (status, target, '
                                                 'source, effect) {\n'
                                                 '\t\t\t\tif (!effect || '
                                                 '!source)\n'
                                                 '\t\t\t\t\treturn;\n'
                                                 '\t\t\t\tif '
                                                 '(effect.effectType === '
                                                 "'Move' && effect.infiltrates "
                                                 '&& !target.isAlly(source))\n'
                                                 '\t\t\t\t\treturn;\n'
                                                 '\t\t\t\tif ((status.id === '
                                                 "'confusion' || status.id === "
                                                 "'yawn') && target !== "
                                                 'source) {\n'
                                                 '\t\t\t\t\tif '
                                                 '(effect.effectType === '
                                                 "'Move' && "
                                                 '!effect.secondaries)\n'
                                                 '\t\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "target, 'move: Safeguard');\n"
                                                 '\t\t\t\t\treturn null;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t}'},
               'contestType': 'Beautiful',
               'flags': {'snatch': 1},
               'name': 'Safeguard',
               'num': 219,
               'pp': 25,
               'priority': 0,
               'secondary': None,
               'sideCondition': 'safeguard',
               'target': 'allySide',
               'type': 'Normal',
               'zMove': {'boost': {'spe': 1}}},
 'sandattack': {'accuracy': 100,
                'basePower': 0,
                'boosts': {'accuracy': -1},
                'category': 'Status',
                'contestType': 'Cute',
                'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                'name': 'Sand Attack',
                'num': 28,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ground',
                'zMove': {'boost': {'evasion': 1}}},
 'sandstorm': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Tough',
               'flags': {},
               'name': 'Sandstorm',
               'num': 201,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'all',
               'type': 'Rock',
               'weather': 'Sandstorm',
               'zMove': {'boost': {'spe': 1}}},
 'sandtomb': {'accuracy': 85,
              'basePower': 35,
              'category': 'Physical',
              'contestType': 'Clever',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Sand Tomb',
              'num': 328,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Ground',
              'volatileStatus': 'partiallytrapped'},
 'sappyseed': {'accuracy': 90,
               'basePower': 100,
               'category': 'Physical',
               'contestType': 'Clever',
               'flags': {'protect': 1, 'reflectable': 1},
               'isNonstandard': 'LGPE',
               'name': 'Sappy Seed',
               'num': 738,
               'onHit': 'function (target, source) {\n'
                        "\t\t\tif (target.hasType('Grass'))\n"
                        '\t\t\t\treturn null;\n'
                        "\t\t\ttarget.addVolatile('leechseed', source);\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'savagespinout': {'accuracy': True,
                   'basePower': 1,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isNonstandard': 'Past',
                   'isZ': 'buginiumz',
                   'name': 'Savage Spin-Out',
                   'num': 634,
                   'pp': 1,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Bug'},
 'scald': {'accuracy': 100,
           'basePower': 80,
           'category': 'Special',
           'contestType': 'Tough',
           'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
           'name': 'Scald',
           'num': 503,
           'pp': 15,
           'priority': 0,
           'secondary': {'chance': 30, 'status': 'brn'},
           'target': 'normal',
           'thawsTarget': True,
           'type': 'Water'},
 'scaleshot': {'accuracy': 90,
               'basePower': 25,
               'category': 'Physical',
               'flags': {'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'multihit': [2, 5],
               'name': 'Scale Shot',
               'num': 799,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'selfBoost': {'boosts': {'def': -1, 'spe': 1}},
               'target': 'normal',
               'type': 'Dragon',
               'zMove': {'basePower': 140}},
 'scaryface': {'accuracy': 100,
               'basePower': 0,
               'boosts': {'spe': -2},
               'category': 'Status',
               'contestType': 'Tough',
               'flags': {'mirror': 1,
                         'mystery': 1,
                         'protect': 1,
                         'reflectable': 1},
               'name': 'Scary Face',
               'num': 184,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'boost': {'spe': 1}}},
 'scorchingsands': {'accuracy': 100,
                    'basePower': 70,
                    'category': 'Special',
                    'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
                    'name': 'Scorching Sands',
                    'num': 815,
                    'pp': 10,
                    'priority': 0,
                    'secondary': {'chance': 30, 'status': 'brn'},
                    'target': 'normal',
                    'thawsTarget': True,
                    'type': 'Ground'},
 'scratch': {'accuracy': 100,
             'basePower': 40,
             'category': 'Physical',
             'contestType': 'Tough',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Scratch',
             'num': 10,
             'pp': 35,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal'},
 'screech': {'accuracy': 85,
             'basePower': 0,
             'boosts': {'def': -2},
             'category': 'Status',
             'contestType': 'Clever',
             'flags': {'authentic': 1,
                       'mirror': 1,
                       'mystery': 1,
                       'protect': 1,
                       'reflectable': 1,
                       'sound': 1},
             'name': 'Screech',
             'num': 103,
             'pp': 40,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'zMove': {'boost': {'atk': 1}}},
 'searingshot': {'accuracy': 100,
                 'basePower': 100,
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Searing Shot',
                 'num': 545,
                 'pp': 5,
                 'priority': 0,
                 'secondary': {'chance': 30, 'status': 'brn'},
                 'target': 'allAdjacent',
                 'type': 'Fire'},
 'searingsunrazesmash': {'accuracy': True,
                         'basePower': 200,
                         'category': 'Physical',
                         'contestType': 'Cool',
                         'flags': {'contact': 1},
                         'ignoreAbility': True,
                         'isNonstandard': 'Past',
                         'isZ': 'solganiumz',
                         'name': 'Searing Sunraze Smash',
                         'num': 724,
                         'pp': 1,
                         'priority': 0,
                         'secondary': None,
                         'target': 'normal',
                         'type': 'Steel'},
 'secretpower': {'accuracy': 100,
                 'basePower': 70,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Secret Power',
                 'num': 290,
                 'onModifyMove': 'function (move, pokemon) {\n'
                                 "\t\t\tif (this.field.isTerrain(''))\n"
                                 '\t\t\t\treturn;\n'
                                 '\t\t\tmove.secondaries = [];\n'
                                 '\t\t\tif '
                                 "(this.field.isTerrain('electricterrain')) {\n"
                                 '\t\t\t\tmove.secondaries.push({\n'
                                 '\t\t\t\t\tchance: 30,\n'
                                 "\t\t\t\t\tstatus: 'par',\n"
                                 '\t\t\t\t});\n'
                                 '\t\t\t}\n'
                                 '\t\t\telse if '
                                 "(this.field.isTerrain('grassyterrain')) {\n"
                                 '\t\t\t\tmove.secondaries.push({\n'
                                 '\t\t\t\t\tchance: 30,\n'
                                 "\t\t\t\t\tstatus: 'slp',\n"
                                 '\t\t\t\t});\n'
                                 '\t\t\t}\n'
                                 '\t\t\telse if '
                                 "(this.field.isTerrain('mistyterrain')) {\n"
                                 '\t\t\t\tmove.secondaries.push({\n'
                                 '\t\t\t\t\tchance: 30,\n'
                                 '\t\t\t\t\tboosts: {\n'
                                 '\t\t\t\t\t\tspa: -1,\n'
                                 '\t\t\t\t\t},\n'
                                 '\t\t\t\t});\n'
                                 '\t\t\t}\n'
                                 '\t\t\telse if '
                                 "(this.field.isTerrain('psychicterrain')) {\n"
                                 '\t\t\t\tmove.secondaries.push({\n'
                                 '\t\t\t\t\tchance: 30,\n'
                                 '\t\t\t\t\tboosts: {\n'
                                 '\t\t\t\t\t\tspe: -1,\n'
                                 '\t\t\t\t\t},\n'
                                 '\t\t\t\t});\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'chance': 30, 'status': 'par'},
                 'target': 'normal',
                 'type': 'Normal'},
 'secretsword': {'accuracy': 100,
                 'basePower': 85,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'defensiveCategory': 'Physical',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Secret Sword',
                 'num': 548,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fighting'},
 'seedbomb': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
              'name': 'Seed Bomb',
              'num': 402,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Grass'},
 'seedflare': {'accuracy': 85,
               'basePower': 120,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Seed Flare',
               'num': 465,
               'pp': 5,
               'priority': 0,
               'secondary': {'boosts': {'spd': -2}, 'chance': 40},
               'target': 'normal',
               'type': 'Grass'},
 'seismictoss': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'damage': 'level',
                 'flags': {'contact': 1,
                           'mirror': 1,
                           'nonsky': 1,
                           'protect': 1},
                 'maxMove': {'basePower': 75},
                 'name': 'Seismic Toss',
                 'num': 69,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fighting'},
 'selfdestruct': {'accuracy': 100,
                  'basePower': 200,
                  'category': 'Physical',
                  'contestType': 'Beautiful',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Self-Destruct',
                  'num': 120,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'selfdestruct': 'always',
                  'target': 'allAdjacent',
                  'type': 'Normal'},
 'shadowball': {'accuracy': 100,
                'basePower': 80,
                'category': 'Special',
                'contestType': 'Clever',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'name': 'Shadow Ball',
                'num': 247,
                'pp': 15,
                'priority': 0,
                'secondary': {'boosts': {'spd': -1}, 'chance': 20},
                'target': 'normal',
                'type': 'Ghost'},
 'shadowbone': {'accuracy': 100,
                'basePower': 85,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Shadow Bone',
                'num': 708,
                'pp': 10,
                'priority': 0,
                'secondary': {'boosts': {'def': -1}, 'chance': 20},
                'target': 'normal',
                'type': 'Ghost'},
 'shadowclaw': {'accuracy': 100,
                'basePower': 70,
                'category': 'Physical',
                'contestType': 'Cool',
                'critRatio': 2,
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Shadow Claw',
                'num': 421,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ghost'},
 'shadowforce': {'accuracy': 100,
                 'basePower': 120,
                 'breaksProtect': True,
                 'category': 'Physical',
                 'condition': {'duration': 2, 'onInvulnerability': False},
                 'contestType': 'Cool',
                 'flags': {'charge': 1, 'contact': 1, 'mirror': 1},
                 'name': 'Shadow Force',
                 'num': 467,
                 'onTryMove': 'function (attacker, defender, move) {\n'
                              '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\t}\n'
                              "\t\t\tthis.add('-prepare', attacker, "
                              'move.name);\n'
                              "\t\t\tif (!this.runEvent('ChargeMove', "
                              'attacker, defender, move)) {\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\t}\n'
                              "\t\t\tattacker.addVolatile('twoturnmove', "
                              'defender);\n'
                              '\t\t\treturn null;\n'
                              '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ghost'},
 'shadowpunch': {'accuracy': True,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                 'name': 'Shadow Punch',
                 'num': 325,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ghost'},
 'shadowsneak': {'accuracy': 100,
                 'basePower': 40,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Shadow Sneak',
                 'num': 425,
                 'pp': 30,
                 'priority': 1,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Ghost'},
 'shadowstrike': {'accuracy': 95,
                  'basePower': 80,
                  'category': 'Physical',
                  'contestType': 'Clever',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'isNonstandard': 'CAP',
                  'name': 'Shadow Strike',
                  'num': 0,
                  'pp': 10,
                  'priority': 0,
                  'secondary': {'boosts': {'def': -1}, 'chance': 50},
                  'target': 'normal',
                  'type': 'Ghost'},
 'sharpen': {'accuracy': True,
             'basePower': 0,
             'boosts': {'atk': 1},
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {'snatch': 1},
             'isNonstandard': 'Past',
             'name': 'Sharpen',
             'num': 159,
             'pp': 30,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'boost': {'atk': 1}}},
 'shatteredpsyche': {'accuracy': True,
                     'basePower': 1,
                     'category': 'Physical',
                     'contestType': 'Cool',
                     'flags': {},
                     'isNonstandard': 'Past',
                     'isZ': 'psychiumz',
                     'name': 'Shattered Psyche',
                     'num': 648,
                     'pp': 1,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Psychic'},
 'sheercold': {'accuracy': 30,
               'basePower': 0,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'maxMove': {'basePower': 130},
               'name': 'Sheer Cold',
               'num': 329,
               'ohko': 'Ice',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Ice',
               'zMove': {'basePower': 180}},
 'shellsidearm': {'accuracy': 100,
                  'basePower': 90,
                  'category': 'Special',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Shell Side Arm',
                  'num': 801,
                  'onAfterSubDamage': 'function (damage, target, source, move) '
                                      '{\n'
                                      '\t\t\tif (!source.isAlly(target))\n'
                                      '\t\t\t\tthis.hint(move.category + " '
                                      'Shell Side Arm");\n'
                                      '\t\t}',
                  'onHit': 'function (target, source, move) {\n'
                           '\t\t\t// Shell Side Arm normally reveals its '
                           "category via animation on cart, but doesn't play "
                           'either custom animation against allies\n'
                           '\t\t\tif (!source.isAlly(target))\n'
                           '\t\t\t\tthis.hint(move.category + " Shell Side '
                           'Arm");\n'
                           '\t\t}',
                  'onModifyMove': 'function (move, pokemon, target) {\n'
                                  '\t\t\tif (!target)\n'
                                  '\t\t\t\treturn;\n'
                                  "\t\t\tvar atk = pokemon.getStat('atk', "
                                  'false, true);\n'
                                  "\t\t\tvar spa = pokemon.getStat('spa', "
                                  'false, true);\n'
                                  "\t\t\tvar def = target.getStat('def', "
                                  'false, true);\n'
                                  "\t\t\tvar spd = target.getStat('spd', "
                                  'false, true);\n'
                                  '\t\t\tvar physical = '
                                  'Math.floor(Math.floor(Math.floor(Math.floor(2 '
                                  '* pokemon.level / 5 + 2) * 90 * atk) / def) '
                                  '/ 50);\n'
                                  '\t\t\tvar special = '
                                  'Math.floor(Math.floor(Math.floor(Math.floor(2 '
                                  '* pokemon.level / 5 + 2) * 90 * spa) / spd) '
                                  '/ 50);\n'
                                  '\t\t\tif (physical > special || (physical '
                                  '=== special && this.random(2) === 0)) {\n'
                                  "\t\t\t\tmove.category = 'Physical';\n"
                                  '\t\t\t\tmove.flags.contact = 1;\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                  'onPrepareHit': 'function (target, source, move) {\n'
                                  '\t\t\tif (!source.isAlly(target)) {\n'
                                  "\t\t\t\tthis.attrLastMove('[anim] Shell "
                                  "Side Arm ' + move.category);\n"
                                  '\t\t\t}\n'
                                  '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': {'chance': 20, 'status': 'psn'},
                  'target': 'normal',
                  'type': 'Poison'},
 'shellsmash': {'accuracy': True,
                'basePower': 0,
                'boosts': {'atk': 2, 'def': -1, 'spa': 2, 'spd': -1, 'spe': 2},
                'category': 'Status',
                'contestType': 'Tough',
                'flags': {'snatch': 1},
                'name': 'Shell Smash',
                'num': 504,
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'effect': 'clearnegativeboost'}},
 'shelltrap': {'accuracy': 100,
               'basePower': 150,
               'beforeTurnCallback': 'function (pokemon) {\n'
                                     "\t\t\tpokemon.addVolatile('shelltrap');\n"
                                     '\t\t}',
               'category': 'Special',
               'condition': {'duration': 1,
                             'onHit': 'function (pokemon, source, move) {\n'
                                      '\t\t\t\tif (!pokemon.isAlly(source) && '
                                      "move.category === 'Physical') {\n"
                                      '\t\t\t\t\t'
                                      "pokemon.volatiles['shelltrap'].gotHit = "
                                      'true;\n'
                                      '\t\t\t\t\tvar action = '
                                      'this.queue.willMove(pokemon);\n'
                                      '\t\t\t\t\tif (action) {\n'
                                      '\t\t\t\t\t\t'
                                      'this.queue.prioritizeAction(action);\n'
                                      '\t\t\t\t\t}\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                             'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-singleturn', "
                                        "pokemon, 'move: Shell Trap');\n"
                                        '\t\t\t}'},
               'contestType': 'Tough',
               'flags': {'protect': 1},
               'name': 'Shell Trap',
               'num': 704,
               'onTryMove': 'function (pokemon) {\n'
                            '\t\t\tvar _a;\n'
                            "\t\t\tif (!((_a = pokemon.volatiles['shelltrap']) "
                            '=== null || _a === void 0 ? void 0 : _a.gotHit)) '
                            '{\n'
                            "\t\t\t\tthis.attrLastMove('[still]');\n"
                            "\t\t\t\tthis.add('cant', pokemon, 'Shell Trap', "
                            "'Shell Trap');\n"
                            '\t\t\t\treturn null;\n'
                            '\t\t\t}\n'
                            '\t\t}',
               'pp': 5,
               'priority': -3,
               'secondary': None,
               'target': 'allAdjacentFoes',
               'type': 'Fire'},
 'shiftgear': {'accuracy': True,
               'basePower': 0,
               'boosts': {'atk': 1, 'spe': 2},
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'snatch': 1},
               'name': 'Shift Gear',
               'num': 508,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Steel',
               'zMove': {'effect': 'clearnegativeboost'}},
 'shockwave': {'accuracy': True,
               'basePower': 60,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Shock Wave',
               'num': 351,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Electric'},
 'shoreup': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Beautiful',
             'flags': {'heal': 1, 'snatch': 1},
             'name': 'Shore Up',
             'num': 659,
             'onHit': 'function (pokemon) {\n'
                      '\t\t\tvar factor = 0.5;\n'
                      "\t\t\tif (this.field.isWeather('sandstorm')) {\n"
                      '\t\t\t\tfactor = 0.667;\n'
                      '\t\t\t}\n'
                      '\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, '
                      'factor));\n'
                      '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Ground',
             'zMove': {'effect': 'clearnegativeboost'}},
 'signalbeam': {'accuracy': 100,
                'basePower': 75,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Signal Beam',
                'num': 324,
                'pp': 15,
                'priority': 0,
                'secondary': {'chance': 10, 'volatileStatus': 'confusion'},
                'target': 'normal',
                'type': 'Bug'},
 'silverwind': {'accuracy': 100,
                'basePower': 60,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Silver Wind',
                'num': 318,
                'pp': 5,
                'priority': 0,
                'secondary': {'chance': 10,
                              'self': {'boosts': {'atk': 1,
                                                  'def': 1,
                                                  'spa': 1,
                                                  'spd': 1,
                                                  'spe': 1}}},
                'target': 'normal',
                'type': 'Bug'},
 'simplebeam': {'accuracy': 100,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Cute',
                'flags': {'mirror': 1,
                          'mystery': 1,
                          'protect': 1,
                          'reflectable': 1},
                'name': 'Simple Beam',
                'num': 493,
                'onHit': 'function (pokemon) {\n'
                         '\t\t\tvar oldAbility = '
                         "pokemon.setAbility('simple');\n"
                         '\t\t\tif (oldAbility) {\n'
                         "\t\t\t\tthis.add('-ability', pokemon, 'Simple', "
                         "'[from] move: Simple Beam');\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         '\t\t\treturn false;\n'
                         '\t\t}',
                'onTryHit': 'function (target) {\n'
                            '\t\t\tif (target.getAbility().isPermanent || '
                            "target.ability === 'simple' || target.ability === "
                            "'truant') {\n"
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 15,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal',
                'zMove': {'boost': {'spa': 1}}},
 'sing': {'accuracy': 55,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Cute',
          'flags': {'authentic': 1,
                    'mirror': 1,
                    'protect': 1,
                    'reflectable': 1,
                    'sound': 1},
          'name': 'Sing',
          'num': 47,
          'pp': 15,
          'priority': 0,
          'secondary': None,
          'status': 'slp',
          'target': 'normal',
          'type': 'Normal',
          'zMove': {'boost': {'spe': 1}}},
 'sinisterarrowraid': {'accuracy': True,
                       'basePower': 180,
                       'category': 'Physical',
                       'contestType': 'Cool',
                       'flags': {},
                       'isNonstandard': 'Past',
                       'isZ': 'decidiumz',
                       'name': 'Sinister Arrow Raid',
                       'num': 695,
                       'pp': 1,
                       'priority': 0,
                       'secondary': None,
                       'target': 'normal',
                       'type': 'Ghost'},
 'sizzlyslide': {'accuracy': 100,
                 'basePower': 60,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'defrost': 1, 'protect': 1},
                 'isNonstandard': 'LGPE',
                 'name': 'Sizzly Slide',
                 'num': 735,
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'chance': 100, 'status': 'brn'},
                 'target': 'normal',
                 'type': 'Fire'},
 'sketch': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Clever',
            'flags': {'authentic': 1, 'mystery': 1},
            'isNonstandard': 'Past',
            'name': 'Sketch',
            'noPPBoosts': True,
            'noSketch': True,
            'num': 166,
            'onHit': 'function (target, source) {\n'
                     "\t\t\tvar disallowedMoves = ['chatter', 'sketch', "
                     "'struggle'];\n"
                     '\t\t\tvar move = target.lastMove;\n'
                     '\t\t\tif (source.transformed || !move || '
                     'source.moves.includes(move.id))\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\tif (disallowedMoves.includes(move.id) || move.isZ '
                     '|| move.isMax)\n'
                     '\t\t\t\treturn false;\n'
                     "\t\t\tvar sketchIndex = source.moves.indexOf('sketch');\n"
                     '\t\t\tif (sketchIndex < 0)\n'
                     '\t\t\t\treturn false;\n'
                     '\t\t\tvar sketchedMove = {\n'
                     '\t\t\t\tmove: move.name,\n'
                     '\t\t\t\tid: move.id,\n'
                     '\t\t\t\tpp: move.pp,\n'
                     '\t\t\t\tmaxpp: move.pp,\n'
                     '\t\t\t\ttarget: move.target,\n'
                     '\t\t\t\tdisabled: false,\n'
                     '\t\t\t\tused: false,\n'
                     '\t\t\t};\n'
                     '\t\t\tsource.moveSlots[sketchIndex] = sketchedMove;\n'
                     '\t\t\tsource.baseMoveSlots[sketchIndex] = sketchedMove;\n'
                     "\t\t\tthis.add('-activate', source, 'move: Sketch', "
                     'move.name);\n'
                     '\t\t}',
            'pp': 1,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'zMove': {'boost': {'atk': 1,
                                'def': 1,
                                'spa': 1,
                                'spd': 1,
                                'spe': 1}}},
 'skillswap': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'protect': 1},
               'name': 'Skill Swap',
               'num': 285,
               'onHit': 'function (target, source, move) {\n'
                        '\t\t\tvar targetAbility = target.getAbility();\n'
                        '\t\t\tvar sourceAbility = source.getAbility();\n'
                        '\t\t\tif (target.isAlly(source)) {\n'
                        "\t\t\t\tthis.add('-activate', source, 'move: Skill "
                        "Swap', '', '', '[of] ' + target);\n"
                        '\t\t\t}\n'
                        '\t\t\telse {\n'
                        "\t\t\t\tthis.add('-activate', source, 'move: Skill "
                        "Swap', targetAbility, sourceAbility, '[of] ' + "
                        'target);\n'
                        '\t\t\t}\n'
                        "\t\t\tthis.singleEvent('End', sourceAbility, "
                        'source.abilityState, source);\n'
                        "\t\t\tthis.singleEvent('End', targetAbility, "
                        'target.abilityState, target);\n'
                        '\t\t\tsource.ability = targetAbility.id;\n'
                        '\t\t\ttarget.ability = sourceAbility.id;\n'
                        '\t\t\tsource.abilityState = { id: '
                        'this.toID(source.ability), target: source };\n'
                        '\t\t\ttarget.abilityState = { id: '
                        'this.toID(target.ability), target: target };\n'
                        '\t\t\tif (!target.isAlly(source))\n'
                        "\t\t\t\ttarget.volatileStaleness = 'external';\n"
                        "\t\t\tthis.singleEvent('Start', targetAbility, "
                        'source.abilityState, source);\n'
                        "\t\t\tthis.singleEvent('Start', sourceAbility, "
                        'target.abilityState, target);\n'
                        '\t\t}',
               'onTryHit': 'function (target, source) {\n'
                           '\t\t\tvar additionalBannedAbilities = '
                           "['hungerswitch', 'illusion', 'neutralizinggas', "
                           "'wonderguard'];\n"
                           "\t\t\tif (target.volatiles['dynamax'] ||\n"
                           '\t\t\t\ttarget.getAbility().isPermanent || '
                           'source.getAbility().isPermanent ||\n'
                           '\t\t\t\t'
                           'additionalBannedAbilities.includes(target.ability) '
                           '|| '
                           'additionalBannedAbilities.includes(source.ability)) '
                           '{\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic',
               'zMove': {'boost': {'spe': 1}}},
 'skittersmack': {'accuracy': 90,
                  'basePower': 70,
                  'category': 'Physical',
                  'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                  'name': 'Skitter Smack',
                  'num': 806,
                  'pp': 10,
                  'priority': 0,
                  'secondary': {'boosts': {'spa': -1}, 'chance': 100},
                  'target': 'normal',
                  'type': 'Bug'},
 'skullbash': {'accuracy': 100,
               'basePower': 130,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'charge': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Skull Bash',
               'num': 130,
               'onTryMove': 'function (attacker, defender, move) {\n'
                            '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                            '\t\t\tthis.boost({ def: 1 }, attacker, attacker, '
                            'move);\n'
                            "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                            'defender, move)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tattacker.addVolatile('twoturnmove', "
                            'defender);\n'
                            '\t\t\treturn null;\n'
                            '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal'},
 'skyattack': {'accuracy': 90,
               'basePower': 140,
               'category': 'Physical',
               'contestType': 'Cool',
               'critRatio': 2,
               'flags': {'charge': 1, 'distance': 1, 'mirror': 1, 'protect': 1},
               'name': 'Sky Attack',
               'num': 143,
               'onTryMove': 'function (attacker, defender, move) {\n'
                            '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                            "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                            'defender, move)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tattacker.addVolatile('twoturnmove', "
                            'defender);\n'
                            '\t\t\treturn null;\n'
                            '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
               'target': 'any',
               'type': 'Flying'},
 'skydrop': {'accuracy': 100,
             'basePower': 60,
             'category': 'Physical',
             'condition': {'duration': 2,
                           'onAnyBasePower': 'function (basePower, target, '
                                             'source, move) {\n'
                                             '\t\t\t\tif (target !== '
                                             'this.effectState.target && '
                                             'target !== '
                                             'this.effectState.source) {\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\tif (source === '
                                             'this.effectState.target && '
                                             'target === '
                                             'this.effectState.source) {\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             "\t\t\t\tif (move.id === 'gust' "
                                             "|| move.id === 'twister') {\n"
                                             '\t\t\t\t\treturn '
                                             'this.chainModify(2);\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                           'onAnyDragOut': 'function (pokemon) {\n'
                                           '\t\t\t\tif (pokemon === '
                                           'this.effectState.target || pokemon '
                                           '=== this.effectState.source)\n'
                                           '\t\t\t\t\treturn false;\n'
                                           '\t\t\t}',
                           'onAnyInvulnerability': 'function (target, source, '
                                                   'move) {\n'
                                                   '\t\t\t\tif (target !== '
                                                   'this.effectState.target && '
                                                   'target !== '
                                                   'this.effectState.source) '
                                                   '{\n'
                                                   '\t\t\t\t\treturn;\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t\tif (source === '
                                                   'this.effectState.target && '
                                                   'target === '
                                                   'this.effectState.source) '
                                                   '{\n'
                                                   '\t\t\t\t\treturn;\n'
                                                   '\t\t\t\t}\n'
                                                   "\t\t\t\tif (['gust', "
                                                   "'twister', 'skyuppercut', "
                                                   "'thunder', 'hurricane', "
                                                   "'smackdown', "
                                                   "'thousandarrows'].includes(move.id)) "
                                                   '{\n'
                                                   '\t\t\t\t\treturn;\n'
                                                   '\t\t\t\t}\n'
                                                   '\t\t\t\treturn false;\n'
                                                   '\t\t\t}',
                           'onFaint': 'function (target) {\n'
                                      "\t\t\t\tif (target.volatiles['skydrop'] "
                                      '&& '
                                      "target.volatiles['twoturnmove'].source) "
                                      '{\n'
                                      "\t\t\t\t\tthis.add('-end', "
                                      "target.volatiles['twoturnmove'].source, "
                                      "'Sky Drop', '[interrupt]');\n"
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                           'onFoeBeforeMove': 'function (attacker, defender, '
                                              'move) {\n'
                                              '\t\t\t\tif (attacker === '
                                              'this.effectState.source) {\n'
                                              '\t\t\t\t\t'
                                              'attacker.activeMoveActions--;\n'
                                              "\t\t\t\t\tthis.debug('Sky drop "
                                              "nullifying.');\n"
                                              '\t\t\t\t\treturn null;\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                           'onFoeBeforeMovePriority': 12,
                           'onFoeTrapPokemon': 'function (defender) {\n'
                                               '\t\t\t\tif (defender !== '
                                               'this.effectState.source)\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\tdefender.trapped = '
                                               'true;\n'
                                               '\t\t\t}',
                           'onFoeTrapPokemonPriority': -15,
                           'onRedirectTarget': 'function (target, source, '
                                               'source2) {\n'
                                               '\t\t\t\tif (source !== '
                                               'this.effectState.target)\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\tif '
                                               '(this.effectState.source.fainted)\n'
                                               '\t\t\t\t\treturn;\n'
                                               '\t\t\t\treturn '
                                               'this.effectState.source;\n'
                                               '\t\t\t}',
                           'onRedirectTargetPriority': 99},
             'contestType': 'Tough',
             'flags': {'charge': 1,
                       'contact': 1,
                       'distance': 1,
                       'gravity': 1,
                       'mirror': 1,
                       'protect': 1},
             'isNonstandard': 'Past',
             'name': 'Sky Drop',
             'num': 507,
             'onHit': 'function (target, source) {\n'
                      '\t\t\tif (target.hp)\n'
                      "\t\t\t\tthis.add('-end', target, 'Sky Drop');\n"
                      '\t\t}',
             'onModifyMove': 'function (move, source) {\n'
                             "\t\t\tif (!source.volatiles['skydrop']) {\n"
                             '\t\t\t\tmove.accuracy = true;\n'
                             '\t\t\t\tmove.flags.contact = 0;\n'
                             '\t\t\t}\n'
                             '\t\t}',
             'onMoveFail': 'function (target, source) {\n'
                           "\t\t\tif (source.volatiles['twoturnmove'] && "
                           "source.volatiles['twoturnmove'].duration === 1) {\n"
                           "\t\t\t\tsource.removeVolatile('skydrop');\n"
                           "\t\t\t\tsource.removeVolatile('twoturnmove');\n"
                           '\t\t\t\tif (target === this.effectState.target) {\n'
                           "\t\t\t\t\tthis.add('-end', target, 'Sky Drop', "
                           "'[interrupt]');\n"
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t}',
             'onTry': 'function (source, target) {\n'
                      '\t\t\treturn !target.fainted;\n'
                      '\t\t}',
             'onTryHit': 'function (target, source, move) {\n'
                         '\t\t\tif (source.removeVolatile(move.id)) {\n'
                         '\t\t\t\tif (target !== '
                         "source.volatiles['twoturnmove'].source)\n"
                         '\t\t\t\t\treturn false;\n'
                         "\t\t\t\tif (target.hasType('Flying')) {\n"
                         "\t\t\t\t\tthis.add('-immune', target);\n"
                         '\t\t\t\t\treturn null;\n'
                         '\t\t\t\t}\n'
                         '\t\t\t}\n'
                         '\t\t\telse {\n'
                         "\t\t\t\tif (target.volatiles['substitute'] || "
                         'target.isAlly(source)) {\n'
                         '\t\t\t\t\treturn false;\n'
                         '\t\t\t\t}\n'
                         '\t\t\t\tif (target.getWeight() >= 2000) {\n'
                         "\t\t\t\t\tthis.add('-fail', target, 'move: Sky "
                         "Drop', '[heavy]');\n"
                         '\t\t\t\t\treturn null;\n'
                         '\t\t\t\t}\n'
                         "\t\t\t\tthis.add('-prepare', source, move.name, "
                         'target);\n'
                         "\t\t\t\tsource.addVolatile('twoturnmove', target);\n"
                         '\t\t\t\treturn null;\n'
                         '\t\t\t}\n'
                         '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'any',
             'type': 'Flying'},
 'skyuppercut': {'accuracy': 90,
                 'basePower': 85,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                 'isNonstandard': 'Past',
                 'name': 'Sky Uppercut',
                 'num': 327,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Fighting'},
 'slackoff': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'heal': 1, 'snatch': 1},
              'heal': [1, 2],
              'name': 'Slack Off',
              'num': 303,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Normal',
              'zMove': {'effect': 'clearnegativeboost'}},
 'slam': {'accuracy': 75,
          'basePower': 80,
          'category': 'Physical',
          'contestType': 'Tough',
          'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
          'name': 'Slam',
          'num': 21,
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Normal'},
 'slash': {'accuracy': 100,
           'basePower': 70,
           'category': 'Physical',
           'contestType': 'Cool',
           'critRatio': 2,
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Slash',
           'num': 163,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Normal'},
 'sleeppowder': {'accuracy': 75,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1,
                           'powder': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'name': 'Sleep Powder',
                 'num': 79,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'status': 'slp',
                 'target': 'normal',
                 'type': 'Grass',
                 'zMove': {'boost': {'spe': 1}}},
 'sleeptalk': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {},
               'name': 'Sleep Talk',
               'num': 214,
               'onHit': 'function (pokemon) {\n'
                        '\t\t\tvar noSleepTalk = [\n'
                        "\t\t\t\t'assist', 'beakblast', 'belch', 'bide', "
                        "'celebrate', 'chatter', 'copycat', 'dynamaxcannon', "
                        "'focuspunch', 'mefirst', 'metronome', 'mimic', "
                        "'mirrormove', 'naturepower', 'shelltrap', 'sketch', "
                        "'sleeptalk', 'uproar',\n"
                        '\t\t\t];\n'
                        '\t\t\tvar moves = [];\n'
                        '\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; _i < '
                        '_a.length; _i++) {\n'
                        '\t\t\t\tvar moveSlot = _a[_i];\n'
                        '\t\t\t\tvar moveid = moveSlot.id;\n'
                        '\t\t\t\tif (!moveid)\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\tvar move = this.dex.moves.get(moveid);\n'
                        '\t\t\t\tif (noSleepTalk.includes(moveid) || '
                        "move.flags['charge'] || (move.isZ && move.basePower "
                        '!== 1)) {\n'
                        '\t\t\t\t\tcontinue;\n'
                        '\t\t\t\t}\n'
                        '\t\t\t\tmoves.push(moveid);\n'
                        '\t\t\t}\n'
                        "\t\t\tvar randomMove = '';\n"
                        '\t\t\tif (moves.length)\n'
                        '\t\t\t\trandomMove = this.sample(moves);\n'
                        '\t\t\tif (!randomMove) {\n'
                        '\t\t\t\treturn false;\n'
                        '\t\t\t}\n'
                        '\t\t\tthis.actions.useMove(randomMove, pokemon);\n'
                        '\t\t}',
               'onTry': 'function (source) {\n'
                        "\t\t\treturn source.status === 'slp' || "
                        "source.hasAbility('comatose');\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'sleepUsable': True,
               'target': 'self',
               'type': 'Normal',
               'zMove': {'effect': 'crit2'}},
 'sludge': {'accuracy': 100,
            'basePower': 65,
            'category': 'Special',
            'contestType': 'Tough',
            'flags': {'mirror': 1, 'protect': 1},
            'name': 'Sludge',
            'num': 124,
            'pp': 20,
            'priority': 0,
            'secondary': {'chance': 30, 'status': 'psn'},
            'target': 'normal',
            'type': 'Poison'},
 'sludgebomb': {'accuracy': 100,
                'basePower': 90,
                'category': 'Special',
                'contestType': 'Tough',
                'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                'name': 'Sludge Bomb',
                'num': 188,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 30, 'status': 'psn'},
                'target': 'normal',
                'type': 'Poison'},
 'sludgewave': {'accuracy': 100,
                'basePower': 95,
                'category': 'Special',
                'contestType': 'Tough',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Sludge Wave',
                'num': 482,
                'pp': 10,
                'priority': 0,
                'secondary': {'chance': 10, 'status': 'psn'},
                'target': 'allAdjacent',
                'type': 'Poison'},
 'smackdown': {'accuracy': 100,
               'basePower': 50,
               'category': 'Physical',
               'condition': {'noCopy': True,
                             'onRestart': 'function (pokemon) {\n'
                                          '\t\t\t\tif '
                                          "(pokemon.removeVolatile('fly') || "
                                          "pokemon.removeVolatile('bounce')) "
                                          '{\n'
                                          '\t\t\t\t\t'
                                          'this.queue.cancelMove(pokemon);\n'
                                          "\t\t\t\t\tthis.add('-start', "
                                          "pokemon, 'Smack Down');\n"
                                          '\t\t\t\t}\n'
                                          '\t\t\t}',
                             'onStart': 'function (pokemon) {\n'
                                        '\t\t\t\tvar applies = false;\n'
                                        "\t\t\t\tif (pokemon.hasType('Flying') "
                                        "|| pokemon.hasAbility('levitate'))\n"
                                        '\t\t\t\t\tapplies = true;\n'
                                        '\t\t\t\tif '
                                        "(pokemon.hasItem('ironball') || "
                                        "pokemon.volatiles['ingrain'] ||\n"
                                        '\t\t\t\t\t'
                                        "this.field.getPseudoWeather('gravity'))\n"
                                        '\t\t\t\t\tapplies = false;\n'
                                        '\t\t\t\tif '
                                        "(pokemon.removeVolatile('fly') || "
                                        "pokemon.removeVolatile('bounce')) {\n"
                                        '\t\t\t\t\tapplies = true;\n'
                                        '\t\t\t\t\t'
                                        'this.queue.cancelMove(pokemon);\n'
                                        '\t\t\t\t\t'
                                        "pokemon.removeVolatile('twoturnmove');\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif '
                                        "(pokemon.volatiles['magnetrise']) {\n"
                                        '\t\t\t\t\tapplies = true;\n'
                                        '\t\t\t\t\tdelete '
                                        "pokemon.volatiles['magnetrise'];\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif '
                                        "(pokemon.volatiles['telekinesis']) {\n"
                                        '\t\t\t\t\tapplies = true;\n'
                                        '\t\t\t\t\tdelete '
                                        "pokemon.volatiles['telekinesis'];\n"
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif (!applies)\n'
                                        '\t\t\t\t\treturn false;\n'
                                        "\t\t\t\tthis.add('-start', pokemon, "
                                        "'Smack Down');\n"
                                        '\t\t\t}'},
               'contestType': 'Tough',
               'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
               'name': 'Smack Down',
               'num': 479,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Rock',
               'volatileStatus': 'smackdown'},
 'smartstrike': {'accuracy': True,
                 'basePower': 70,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Smart Strike',
                 'num': 684,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Steel'},
 'smellingsalts': {'accuracy': 100,
                   'basePower': 70,
                   'basePowerCallback': 'function (pokemon, target, move) {\n'
                                        "\t\t\tif (target.status === 'par')\n"
                                        '\t\t\t\treturn move.basePower * 2;\n'
                                        '\t\t\treturn move.basePower;\n'
                                        '\t\t}',
                   'category': 'Physical',
                   'contestType': 'Tough',
                   'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                   'isNonstandard': 'Past',
                   'name': 'Smelling Salts',
                   'num': 265,
                   'onHit': 'function (target) {\n'
                            "\t\t\tif (target.status === 'par')\n"
                            '\t\t\t\ttarget.cureStatus();\n'
                            '\t\t}',
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Normal'},
 'smog': {'accuracy': 70,
          'basePower': 30,
          'category': 'Special',
          'contestType': 'Tough',
          'flags': {'mirror': 1, 'protect': 1},
          'name': 'Smog',
          'num': 123,
          'pp': 20,
          'priority': 0,
          'secondary': {'chance': 40, 'status': 'psn'},
          'target': 'normal',
          'type': 'Poison'},
 'smokescreen': {'accuracy': 100,
                 'basePower': 0,
                 'boosts': {'accuracy': -1},
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                 'name': 'Smokescreen',
                 'num': 108,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'boost': {'evasion': 1}}},
 'snaptrap': {'accuracy': 100,
              'basePower': 35,
              'category': 'Physical',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Snap Trap',
              'num': 779,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Grass',
              'volatileStatus': 'partiallytrapped'},
 'snarl': {'accuracy': 95,
           'basePower': 55,
           'category': 'Special',
           'contestType': 'Tough',
           'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
           'name': 'Snarl',
           'num': 555,
           'pp': 15,
           'priority': 0,
           'secondary': {'boosts': {'spa': -1}, 'chance': 100},
           'target': 'allAdjacentFoes',
           'type': 'Dark'},
 'snatch': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'condition': {'duration': 1,
                          'onAnyPrepareHit': 'function (source, target, move) '
                                             '{\n'
                                             '\t\t\t\tvar snatchUser = '
                                             'this.effectState.source;\n'
                                             '\t\t\t\tif '
                                             '(snatchUser.isSkyDropped())\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\tif (!move || move.isZ || '
                                             'move.isMax || '
                                             "!move.flags['snatch'] || "
                                             "move.sourceEffect === 'snatch') "
                                             '{\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\t'
                                             "snatchUser.removeVolatile('snatch');\n"
                                             "\t\t\t\tthis.add('-activate', "
                                             "snatchUser, 'move: Snatch', "
                                             "'[of] ' + source);\n"
                                             '\t\t\t\t'
                                             'this.actions.useMove(move.id, '
                                             'snatchUser);\n'
                                             '\t\t\t\treturn null;\n'
                                             '\t\t\t}',
                          'onAnyPrepareHitPriority': -1,
                          'onStart': 'function (pokemon) {\n'
                                     "\t\t\t\tthis.add('-singleturn', pokemon, "
                                     "'Snatch');\n"
                                     '\t\t\t}'},
            'contestType': 'Clever',
            'flags': {'authentic': 1},
            'isNonstandard': 'Past',
            'name': 'Snatch',
            'num': 289,
            'pp': 10,
            'pressureTarget': 'foeSide',
            'priority': 4,
            'secondary': None,
            'target': 'self',
            'type': 'Dark',
            'volatileStatus': 'snatch',
            'zMove': {'boost': {'spe': 2}}},
 'snipeshot': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'critRatio': 2,
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Snipe Shot',
               'num': 745,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'tracksTarget': True,
               'type': 'Water'},
 'snore': {'accuracy': 100,
           'basePower': 50,
           'category': 'Special',
           'contestType': 'Cute',
           'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
           'name': 'Snore',
           'num': 173,
           'onTry': 'function (source) {\n'
                    "\t\t\treturn source.status === 'slp' || "
                    "source.hasAbility('comatose');\n"
                    '\t\t}',
           'pp': 15,
           'priority': 0,
           'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
           'sleepUsable': True,
           'target': 'normal',
           'type': 'Normal'},
 'soak': {'accuracy': 100,
          'basePower': 0,
          'category': 'Status',
          'contestType': 'Cute',
          'flags': {'mirror': 1, 'mystery': 1, 'protect': 1, 'reflectable': 1},
          'name': 'Soak',
          'num': 487,
          'onHit': 'function (target) {\n'
                   "\t\t\tif (target.getTypes().join() === 'Water' || "
                   "!target.setType('Water')) {\n"
                   '\t\t\t\t// Soak should animate even when it fails.\n'
                   '\t\t\t\t// Returning false would suppress the animation.\n'
                   "\t\t\t\tthis.add('-fail', target);\n"
                   '\t\t\t\treturn null;\n'
                   '\t\t\t}\n'
                   "\t\t\tthis.add('-start', target, 'typechange', 'Water');\n"
                   '\t\t}',
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Water',
          'zMove': {'boost': {'spa': 1}}},
 'softboiled': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Cute',
                'flags': {'heal': 1, 'snatch': 1},
                'heal': [1, 2],
                'name': 'Soft-Boiled',
                'num': 135,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'zMove': {'effect': 'clearnegativeboost'}},
 'solarbeam': {'accuracy': 100,
               'basePower': 120,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'charge': 1, 'mirror': 1, 'protect': 1},
               'name': 'Solar Beam',
               'num': 76,
               'onBasePower': 'function (basePower, pokemon, target) {\n'
                              "\t\t\tif (['raindance', 'primordialsea', "
                              "'sandstorm', "
                              "'hail'].includes(pokemon.effectiveWeather())) "
                              '{\n'
                              "\t\t\t\tthis.debug('weakened by weather');\n"
                              '\t\t\t\treturn this.chainModify(0.5);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onTryMove': 'function (attacker, defender, move) {\n'
                            '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tthis.add('-prepare', attacker, move.name);\n"
                            "\t\t\tif (['sunnyday', "
                            "'desolateland'].includes(attacker.effectiveWeather())) "
                            '{\n'
                            "\t\t\t\tthis.attrLastMove('[still]');\n"
                            "\t\t\t\tthis.addMove('-anim', attacker, "
                            'move.name, defender);\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                            'defender, move)) {\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\t}\n'
                            "\t\t\tattacker.addVolatile('twoturnmove', "
                            'defender);\n'
                            '\t\t\treturn null;\n'
                            '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass'},
 'solarblade': {'accuracy': 100,
                'basePower': 125,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'charge': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Solar Blade',
                'num': 669,
                'onBasePower': 'function (basePower, pokemon, target) {\n'
                               "\t\t\tif (['raindance', 'primordialsea', "
                               "'sandstorm', "
                               "'hail'].includes(pokemon.effectiveWeather())) "
                               '{\n'
                               "\t\t\t\tthis.debug('weakened by weather');\n"
                               '\t\t\t\treturn this.chainModify(0.5);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onTryMove': 'function (attacker, defender, move) {\n'
                             '\t\t\tif (attacker.removeVolatile(move.id)) {\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             "\t\t\tthis.add('-prepare', attacker, "
                             'move.name);\n'
                             "\t\t\tif (['sunnyday', "
                             "'desolateland'].includes(attacker.effectiveWeather())) "
                             '{\n'
                             "\t\t\t\tthis.attrLastMove('[still]');\n"
                             "\t\t\t\tthis.addMove('-anim', attacker, "
                             'move.name, defender);\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             "\t\t\tif (!this.runEvent('ChargeMove', attacker, "
                             'defender, move)) {\n'
                             '\t\t\t\treturn;\n'
                             '\t\t\t}\n'
                             "\t\t\tattacker.addVolatile('twoturnmove', "
                             'defender);\n'
                             '\t\t\treturn null;\n'
                             '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Grass'},
 'sonicboom': {'accuracy': 90,
               'basePower': 0,
               'category': 'Special',
               'contestType': 'Cool',
               'damage': 20,
               'flags': {'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'name': 'Sonic Boom',
               'num': 49,
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal'},
 'soulstealing7starstrike': {'accuracy': True,
                             'basePower': 195,
                             'category': 'Physical',
                             'contestType': 'Cool',
                             'flags': {'contact': 1},
                             'isNonstandard': 'Past',
                             'isZ': 'marshadiumz',
                             'name': 'Soul-Stealing 7-Star Strike',
                             'num': 699,
                             'pp': 1,
                             'priority': 0,
                             'secondary': None,
                             'target': 'normal',
                             'type': 'Ghost'},
 'spacialrend': {'accuracy': 95,
                 'basePower': 100,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'critRatio': 2,
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Spacial Rend',
                 'num': 460,
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Dragon'},
 'spark': {'accuracy': 100,
           'basePower': 65,
           'category': 'Physical',
           'contestType': 'Cool',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Spark',
           'num': 209,
           'pp': 20,
           'priority': 0,
           'secondary': {'chance': 30, 'status': 'par'},
           'target': 'normal',
           'type': 'Electric'},
 'sparklingaria': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Special',
                   'contestType': 'Tough',
                   'flags': {'authentic': 1,
                             'mirror': 1,
                             'protect': 1,
                             'sound': 1},
                   'name': 'Sparkling Aria',
                   'num': 664,
                   'pp': 10,
                   'priority': 0,
                   'secondary': {'chance': 100,
                                 'dustproof': True,
                                 'onHit': 'function (target) {\n'
                                          '\t\t\t\tif (target.status === '
                                          "'brn')\n"
                                          '\t\t\t\t\ttarget.cureStatus();\n'
                                          '\t\t\t}'},
                   'target': 'allAdjacent',
                   'type': 'Water'},
 'sparklyswirl': {'accuracy': 85,
                  'basePower': 120,
                  'category': 'Special',
                  'contestType': 'Clever',
                  'flags': {'protect': 1},
                  'isNonstandard': 'LGPE',
                  'name': 'Sparkly Swirl',
                  'num': 740,
                  'pp': 5,
                  'priority': 0,
                  'secondary': None,
                  'self': {'onHit': 'function (pokemon, source, move) {\n'
                                    "\t\t\t\tthis.add('-activate', source, "
                                    "'move: Aromatherapy');\n"
                                    '\t\t\t\tfor (var _i = 0, _a = '
                                    'source.side.pokemon; _i < _a.length; '
                                    '_i++) {\n'
                                    '\t\t\t\t\tvar ally = _a[_i];\n'
                                    '\t\t\t\t\tif (ally !== source && '
                                    "(ally.volatiles['substitute'] && "
                                    '!move.infiltrates)) {\n'
                                    '\t\t\t\t\t\tcontinue;\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t\tally.cureStatus();\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                  'target': 'normal',
                  'type': 'Fairy'},
 'spectralthief': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {'authentic': 1,
                             'contact': 1,
                             'mirror': 1,
                             'protect': 1},
                   'name': 'Spectral Thief',
                   'num': 712,
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'stealsBoosts': True,
                   'target': 'normal',
                   'type': 'Ghost'},
 'speedswap': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'protect': 1},
               'name': 'Speed Swap',
               'num': 683,
               'onHit': 'function (target, source) {\n'
                        '\t\t\tvar targetSpe = target.storedStats.spe;\n'
                        '\t\t\ttarget.storedStats.spe = '
                        'source.storedStats.spe;\n'
                        '\t\t\tsource.storedStats.spe = targetSpe;\n'
                        "\t\t\tthis.add('-activate', source, 'move: Speed "
                        "Swap', '[of] ' + target);\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Psychic',
               'zMove': {'boost': {'spe': 1}}},
 'spiderweb': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'isNonstandard': 'Past',
               'name': 'Spider Web',
               'num': 169,
               'onHit': 'function (target, source, move) {\n'
                        "\t\t\treturn target.addVolatile('trapped', source, "
                        "move, 'trapper');\n"
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Bug',
               'zMove': {'boost': {'def': 1}}},
 'spikecannon': {'accuracy': 100,
                 'basePower': 20,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'maxMove': {'basePower': 120},
                 'multihit': [2, 5],
                 'name': 'Spike Cannon',
                 'num': 131,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'spikes': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'condition': {'onSideRestart': 'function (side) {\n'
                                           '\t\t\t\tif '
                                           '(this.effectState.layers >= 3)\n'
                                           '\t\t\t\t\treturn false;\n'
                                           "\t\t\t\tthis.add('-sidestart', "
                                           "side, 'Spikes');\n"
                                           '\t\t\t\t'
                                           'this.effectState.layers++;\n'
                                           '\t\t\t}',
                          'onSideStart': 'function (side) {\n'
                                         "\t\t\t\tthis.add('-sidestart', side, "
                                         "'Spikes');\n"
                                         '\t\t\t\tthis.effectState.layers = '
                                         '1;\n'
                                         '\t\t\t}',
                          'onSwitchIn': 'function (pokemon) {\n'
                                        '\t\t\t\tif (!pokemon.isGrounded())\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif '
                                        "(pokemon.hasItem('heavydutyboots'))\n"
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tvar damageAmounts = [0, 3, 4, '
                                        '6]; // 1/8, 1/6, 1/4\n'
                                        '\t\t\t\t'
                                        'this.damage(damageAmounts[this.effectState.layers] '
                                        '* pokemon.maxhp / 24);\n'
                                        '\t\t\t}'},
            'contestType': 'Clever',
            'flags': {'nonsky': 1, 'reflectable': 1},
            'name': 'Spikes',
            'num': 191,
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'sideCondition': 'spikes',
            'target': 'foeSide',
            'type': 'Ground',
            'zMove': {'boost': {'def': 1}}},
 'spikyshield': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'duration': 1,
                               'onHit': 'function (target, source, move) {\n'
                                        '\t\t\t\tif (move.isZOrMaxPowered && '
                                        'this.checkMoveMakesContact(move, '
                                        'source, target)) {\n'
                                        '\t\t\t\t\t'
                                        'this.damage(source.baseMaxhp / 8, '
                                        'source, target);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}',
                               'onStart': 'function (target) {\n'
                                          "\t\t\t\tthis.add('-singleturn', "
                                          "target, 'move: Protect');\n"
                                          '\t\t\t}',
                               'onTryHit': 'function (target, source, move) {\n'
                                           '\t\t\t\tif '
                                           "(!move.flags['protect']) {\n"
                                           "\t\t\t\t\tif (['gmaxoneblow', "
                                           "'gmaxrapidflow'].includes(move.id))\n"
                                           '\t\t\t\t\t\treturn;\n'
                                           '\t\t\t\t\tif (move.isZ || '
                                           'move.isMax)\n'
                                           '\t\t\t\t\t\t'
                                           'target.getMoveHitData(move).zBrokeProtect '
                                           '= true;\n'
                                           '\t\t\t\t\treturn;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tif (move.smartTarget) {\n'
                                           '\t\t\t\t\tmove.smartTarget = '
                                           'false;\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\telse {\n'
                                           "\t\t\t\t\tthis.add('-activate', "
                                           "target, 'move: Protect');\n"
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tvar lockedmove = '
                                           "source.getVolatile('lockedmove');\n"
                                           '\t\t\t\tif (lockedmove) {\n'
                                           '\t\t\t\t\t// Outrage counter is '
                                           'reset\n'
                                           '\t\t\t\t\tif '
                                           "(source.volatiles['lockedmove'].duration "
                                           '=== 2) {\n'
                                           '\t\t\t\t\t\tdelete '
                                           "source.volatiles['lockedmove'];\n"
                                           '\t\t\t\t\t}\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\tif '
                                           '(this.checkMoveMakesContact(move, '
                                           'source, target)) {\n'
                                           '\t\t\t\t\t'
                                           'this.damage(source.baseMaxhp / 8, '
                                           'source, target);\n'
                                           '\t\t\t\t}\n'
                                           '\t\t\t\treturn this.NOT_FAIL;\n'
                                           '\t\t\t}',
                               'onTryHitPriority': 3},
                 'contestType': 'Tough',
                 'flags': {},
                 'name': 'Spiky Shield',
                 'num': 596,
                 'onHit': 'function (pokemon) {\n'
                          "\t\t\tpokemon.addVolatile('stall');\n"
                          '\t\t}',
                 'onPrepareHit': 'function (pokemon) {\n'
                                 '\t\t\treturn !!this.queue.willAct() && '
                                 "this.runEvent('StallMove', pokemon);\n"
                                 '\t\t}',
                 'pp': 10,
                 'priority': 4,
                 'secondary': None,
                 'stallingMove': True,
                 'target': 'self',
                 'type': 'Grass',
                 'volatileStatus': 'spikyshield',
                 'zMove': {'boost': {'def': 1}}},
 'spiritbreak': {'accuracy': 100,
                 'basePower': 75,
                 'category': 'Physical',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Spirit Break',
                 'num': 789,
                 'pp': 15,
                 'priority': 0,
                 'secondary': {'boosts': {'spa': -1}, 'chance': 100},
                 'target': 'normal',
                 'type': 'Fairy'},
 'spiritshackle': {'accuracy': 100,
                   'basePower': 80,
                   'category': 'Physical',
                   'contestType': 'Tough',
                   'flags': {'mirror': 1, 'protect': 1},
                   'name': 'Spirit Shackle',
                   'num': 662,
                   'pp': 10,
                   'priority': 0,
                   'secondary': {'chance': 100,
                                 'onHit': 'function (target, source, move) {\n'
                                          '\t\t\t\tif (source.isActive)\n'
                                          '\t\t\t\t\t'
                                          "target.addVolatile('trapped', "
                                          "source, move, 'trapper');\n"
                                          '\t\t\t}'},
                   'target': 'normal',
                   'type': 'Ghost'},
 'spite': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Tough',
           'flags': {'authentic': 1,
                     'mirror': 1,
                     'protect': 1,
                     'reflectable': 1},
           'name': 'Spite',
           'num': 180,
           'onHit': 'function (target) {\n'
                    '\t\t\tvar move = target.lastMove;\n'
                    '\t\t\tif (!move || move.isZ)\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\tif (move.isMax && move.baseMove)\n'
                    '\t\t\t\tmove = this.dex.moves.get(move.baseMove);\n'
                    '\t\t\tvar ppDeducted = target.deductPP(move.id, 4);\n'
                    '\t\t\tif (!ppDeducted)\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\tthis.add("-activate", target, \'move: Spite\', '
                    'move.name, ppDeducted);\n'
                    '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Ghost',
           'zMove': {'effect': 'heal'}},
 'spitup': {'accuracy': 100,
            'basePower': 0,
            'basePowerCallback': 'function (pokemon) {\n'
                                 '\t\t\tvar _a;\n'
                                 '\t\t\tif (!((_a = '
                                 "pokemon.volatiles['stockpile']) === null || "
                                 '_a === void 0 ? void 0 : _a.layers))\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn '
                                 "pokemon.volatiles['stockpile'].layers * "
                                 '100;\n'
                                 '\t\t}',
            'category': 'Special',
            'contestType': 'Tough',
            'flags': {'protect': 1},
            'name': 'Spit Up',
            'num': 255,
            'onAfterMove': 'function (pokemon) {\n'
                           "\t\t\tpokemon.removeVolatile('stockpile');\n"
                           '\t\t}',
            'onTry': 'function (source) {\n'
                     "\t\t\treturn !!source.volatiles['stockpile'];\n"
                     '\t\t}',
            'pp': 10,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal'},
 'splash': {'accuracy': True,
            'basePower': 0,
            'category': 'Status',
            'contestType': 'Cute',
            'flags': {'gravity': 1},
            'name': 'Splash',
            'num': 150,
            'onTry': 'function (source, target, move) {\n'
                     '\t\t\t// Additional Gravity check for Z-move variant\n'
                     "\t\t\tif (this.field.getPseudoWeather('Gravity')) {\n"
                     "\t\t\t\tthis.add('cant', source, 'move: Gravity', "
                     'move);\n'
                     '\t\t\t\treturn null;\n'
                     '\t\t\t}\n'
                     '\t\t}',
            'onTryHit': 'function (target, source) {\n'
                        "\t\t\tthis.add('-nothing');\n"
                        '\t\t}',
            'pp': 40,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Normal',
            'zMove': {'boost': {'atk': 3}}},
 'splinteredstormshards': {'accuracy': True,
                           'basePower': 190,
                           'category': 'Physical',
                           'contestType': 'Cool',
                           'flags': {},
                           'isNonstandard': 'Past',
                           'isZ': 'lycaniumz',
                           'name': 'Splintered Stormshards',
                           'num': 727,
                           'onAfterSubDamage': 'function () {\n'
                                               '\t\t\t'
                                               'this.field.clearTerrain();\n'
                                               '\t\t}',
                           'onHit': 'function () {\n'
                                    '\t\t\tthis.field.clearTerrain();\n'
                                    '\t\t}',
                           'pp': 1,
                           'priority': 0,
                           'secondary': None,
                           'target': 'normal',
                           'type': 'Rock'},
 'splishysplash': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Special',
                   'contestType': 'Cool',
                   'flags': {'protect': 1},
                   'isNonstandard': 'LGPE',
                   'name': 'Splishy Splash',
                   'num': 730,
                   'pp': 15,
                   'priority': 0,
                   'secondary': {'chance': 30, 'status': 'par'},
                   'target': 'allAdjacentFoes',
                   'type': 'Water'},
 'spore': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Beautiful',
           'flags': {'mirror': 1, 'powder': 1, 'protect': 1, 'reflectable': 1},
           'name': 'Spore',
           'num': 147,
           'pp': 15,
           'priority': 0,
           'secondary': None,
           'status': 'slp',
           'target': 'normal',
           'type': 'Grass',
           'zMove': {'effect': 'clearnegativeboost'}},
 'spotlight': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 1,
                             'onFoeRedirectTarget': 'function (target, source, '
                                                    'source2, move) {\n'
                                                    '\t\t\t\tif '
                                                    '(this.validTarget(this.effectState.target, '
                                                    'source, move.target)) {\n'
                                                    '\t\t\t\t\t'
                                                    'this.debug("Spotlight '
                                                    'redirected target of '
                                                    'move");\n'
                                                    '\t\t\t\t\treturn '
                                                    'this.effectState.target;\n'
                                                    '\t\t\t\t}\n'
                                                    '\t\t\t}',
                             'onFoeRedirectTargetPriority': 2,
                             'onStart': 'function (pokemon) {\n'
                                        "\t\t\t\tthis.add('-singleturn', "
                                        "pokemon, 'move: Spotlight');\n"
                                        '\t\t\t}'},
               'contestType': 'Cute',
               'flags': {'mystery': 1, 'protect': 1, 'reflectable': 1},
               'isNonstandard': 'Past',
               'name': 'Spotlight',
               'num': 671,
               'onTryHit': 'function (target) {\n'
                           '\t\t\tif (this.activePerHalf === 1)\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t}',
               'pp': 15,
               'priority': 3,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'volatileStatus': 'spotlight',
               'zMove': {'boost': {'spd': 1}}},
 'stealthrock': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'onSideStart': 'function (side) {\n'
                                              "\t\t\t\tthis.add('-sidestart', "
                                              "side, 'move: Stealth Rock');\n"
                                              '\t\t\t}',
                               'onSwitchIn': 'function (pokemon) {\n'
                                             '\t\t\t\tif '
                                             "(pokemon.hasItem('heavydutyboots'))\n"
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\tvar typeMod = '
                                             "this.clampIntRange(pokemon.runEffectiveness(this.dex.getActiveMove('stealthrock')), "
                                             '-6, 6);\n'
                                             '\t\t\t\t'
                                             'this.damage(pokemon.maxhp * '
                                             'Math.pow(2, typeMod) / 8);\n'
                                             '\t\t\t}'},
                 'contestType': 'Cool',
                 'flags': {'reflectable': 1},
                 'name': 'Stealth Rock',
                 'num': 446,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'sideCondition': 'stealthrock',
                 'target': 'foeSide',
                 'type': 'Rock',
                 'zMove': {'boost': {'def': 1}}},
 'steameruption': {'accuracy': 95,
                   'basePower': 110,
                   'category': 'Special',
                   'contestType': 'Beautiful',
                   'flags': {'defrost': 1, 'mirror': 1, 'protect': 1},
                   'name': 'Steam Eruption',
                   'num': 592,
                   'pp': 5,
                   'priority': 0,
                   'secondary': {'chance': 30, 'status': 'brn'},
                   'target': 'normal',
                   'thawsTarget': True,
                   'type': 'Water'},
 'steamroller': {'accuracy': 100,
                 'basePower': 65,
                 'category': 'Physical',
                 'contestType': 'Tough',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'isNonstandard': 'Past',
                 'name': 'Steamroller',
                 'num': 537,
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
                 'target': 'normal',
                 'type': 'Bug'},
 'steelbeam': {'accuracy': 95,
               'basePower': 140,
               'category': 'Special',
               'flags': {'mirror': 1, 'protect': 1},
               'mindBlownRecoil': True,
               'name': 'Steel Beam',
               'num': 796,
               'onAfterMove': 'function (pokemon, target, move) {\n'
                              '\t\t\tif (move.mindBlownRecoil && '
                              '!move.multihit) {\n'
                              '\t\t\t\tthis.damage(Math.round(pokemon.maxhp / '
                              '2), pokemon, pokemon, '
                              "this.dex.conditions.get('Steel Beam'), true);\n"
                              '\t\t\t}\n'
                              '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Steel'},
 'steelroller': {'accuracy': 100,
                 'basePower': 130,
                 'category': 'Physical',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Steel Roller',
                 'num': 798,
                 'onAfterSubDamage': 'function () {\n'
                                     '\t\t\tthis.field.clearTerrain();\n'
                                     '\t\t}',
                 'onHit': 'function () {\n'
                          '\t\t\tthis.field.clearTerrain();\n'
                          '\t\t}',
                 'onTry': 'function () {\n'
                          "\t\t\treturn !this.field.isTerrain('');\n"
                          '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Steel'},
 'steelwing': {'accuracy': 90,
               'basePower': 70,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Steel Wing',
               'num': 211,
               'pp': 25,
               'priority': 0,
               'secondary': {'chance': 10, 'self': {'boosts': {'def': 1}}},
               'target': 'normal',
               'type': 'Steel'},
 'stickyweb': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'onSideStart': 'function (side) {\n'
                                            "\t\t\t\tthis.add('-sidestart', "
                                            "side, 'move: Sticky Web');\n"
                                            '\t\t\t}',
                             'onSwitchIn': 'function (pokemon) {\n'
                                           '\t\t\t\tif '
                                           '(!pokemon.isGrounded())\n'
                                           '\t\t\t\t\treturn;\n'
                                           '\t\t\t\tif '
                                           "(pokemon.hasItem('heavydutyboots'))\n"
                                           '\t\t\t\t\treturn;\n'
                                           "\t\t\t\tthis.add('-activate', "
                                           "pokemon, 'move: Sticky Web');\n"
                                           '\t\t\t\tthis.boost({ spe: -1 }, '
                                           'pokemon, this.effectState.source, '
                                           "this.dex.getActiveMove('stickyweb'));\n"
                                           '\t\t\t}'},
               'contestType': 'Tough',
               'flags': {'reflectable': 1},
               'name': 'Sticky Web',
               'num': 564,
               'pp': 20,
               'pressureTarget': 'self',
               'priority': 0,
               'secondary': None,
               'sideCondition': 'stickyweb',
               'target': 'foeSide',
               'type': 'Bug',
               'zMove': {'boost': {'spe': 1}}},
 'stockpile': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'noCopy': True,
                             'onEnd': 'function (target) {\n'
                                      '\t\t\t\tif (this.effectState.def || '
                                      'this.effectState.spd) {\n'
                                      '\t\t\t\t\tvar boosts = {};\n'
                                      '\t\t\t\t\tif (this.effectState.def)\n'
                                      '\t\t\t\t\t\tboosts.def = '
                                      'this.effectState.def;\n'
                                      '\t\t\t\t\tif (this.effectState.spd)\n'
                                      '\t\t\t\t\t\tboosts.spd = '
                                      'this.effectState.spd;\n'
                                      '\t\t\t\t\tthis.boost(boosts, target, '
                                      'target);\n'
                                      '\t\t\t\t}\n'
                                      "\t\t\t\tthis.add('-end', target, "
                                      "'Stockpile');\n"
                                      '\t\t\t\tif (this.effectState.def !== '
                                      'this.effectState.layers * -1 || '
                                      'this.effectState.spd !== '
                                      'this.effectState.layers * -1) {\n'
                                      '\t\t\t\t\tthis.hint("In Gen 7, '
                                      'Stockpile keeps track of how many times '
                                      'it successfully altered each stat '
                                      'individually.");\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}',
                             'onRestart': 'function (target) {\n'
                                          '\t\t\t\tif (this.effectState.layers '
                                          '>= 3)\n'
                                          '\t\t\t\t\treturn false;\n'
                                          '\t\t\t\tthis.effectState.layers++;\n'
                                          "\t\t\t\tthis.add('-start', target, "
                                          "'stockpile' + "
                                          'this.effectState.layers);\n'
                                          '\t\t\t\tvar curDef = '
                                          'target.boosts.def;\n'
                                          '\t\t\t\tvar curSpD = '
                                          'target.boosts.spd;\n'
                                          '\t\t\t\tthis.boost({ def: 1, spd: 1 '
                                          '}, target, target);\n'
                                          '\t\t\t\tif (curDef !== '
                                          'target.boosts.def)\n'
                                          '\t\t\t\t\tthis.effectState.def--;\n'
                                          '\t\t\t\tif (curSpD !== '
                                          'target.boosts.spd)\n'
                                          '\t\t\t\t\tthis.effectState.spd--;\n'
                                          '\t\t\t}',
                             'onStart': 'function (target) {\n'
                                        '\t\t\t\tthis.effectState.layers = 1;\n'
                                        '\t\t\t\tthis.effectState.def = 0;\n'
                                        '\t\t\t\tthis.effectState.spd = 0;\n'
                                        "\t\t\t\tthis.add('-start', target, "
                                        "'stockpile' + "
                                        'this.effectState.layers);\n'
                                        '\t\t\t\tvar _a = [target.boosts.def, '
                                        'target.boosts.spd], curDef = _a[0], '
                                        'curSpD = _a[1];\n'
                                        '\t\t\t\tthis.boost({ def: 1, spd: 1 '
                                        '}, target, target);\n'
                                        '\t\t\t\tif (curDef !== '
                                        'target.boosts.def)\n'
                                        '\t\t\t\t\tthis.effectState.def--;\n'
                                        '\t\t\t\tif (curSpD !== '
                                        'target.boosts.spd)\n'
                                        '\t\t\t\t\tthis.effectState.spd--;\n'
                                        '\t\t\t}'},
               'contestType': 'Tough',
               'flags': {'snatch': 1},
               'name': 'Stockpile',
               'num': 254,
               'onTry': 'function (source) {\n'
                        "\t\t\tif (source.volatiles['stockpile'] && "
                        "source.volatiles['stockpile'].layers >= 3)\n"
                        '\t\t\t\treturn false;\n'
                        '\t\t}',
               'pp': 20,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Normal',
               'volatileStatus': 'stockpile',
               'zMove': {'effect': 'heal'}},
 'stokedsparksurfer': {'accuracy': True,
                       'basePower': 175,
                       'category': 'Special',
                       'contestType': 'Cool',
                       'flags': {},
                       'isNonstandard': 'Past',
                       'isZ': 'aloraichiumz',
                       'name': 'Stoked Sparksurfer',
                       'num': 700,
                       'pp': 1,
                       'priority': 0,
                       'secondary': {'chance': 100, 'status': 'par'},
                       'target': 'normal',
                       'type': 'Electric'},
 'stomp': {'accuracy': 100,
           'basePower': 65,
           'category': 'Physical',
           'contestType': 'Tough',
           'flags': {'contact': 1, 'mirror': 1, 'nonsky': 1, 'protect': 1},
           'name': 'Stomp',
           'num': 23,
           'pp': 20,
           'priority': 0,
           'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
           'target': 'normal',
           'type': 'Normal'},
 'stompingtantrum': {'accuracy': 100,
                     'basePower': 75,
                     'basePowerCallback': 'function (pokemon, target, move) {\n'
                                          '\t\t\tif '
                                          '(pokemon.moveLastTurnResult === '
                                          'false) {\n'
                                          "\t\t\t\tthis.debug('doubling "
                                          'Stomping Tantrum BP due to previous '
                                          "move failure');\n"
                                          '\t\t\t\treturn move.basePower * 2;\n'
                                          '\t\t\t}\n'
                                          '\t\t\treturn move.basePower;\n'
                                          '\t\t}',
                     'category': 'Physical',
                     'contestType': 'Tough',
                     'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                     'name': 'Stomping Tantrum',
                     'num': 707,
                     'pp': 10,
                     'priority': 0,
                     'secondary': None,
                     'target': 'normal',
                     'type': 'Ground'},
 'stoneedge': {'accuracy': 80,
               'basePower': 100,
               'category': 'Physical',
               'contestType': 'Tough',
               'critRatio': 2,
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Stone Edge',
               'num': 444,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Rock'},
 'storedpower': {'accuracy': 100,
                 'basePower': 20,
                 'basePowerCallback': 'function (pokemon, target, move) {\n'
                                      '\t\t\treturn move.basePower + 20 * '
                                      'pokemon.positiveBoosts();\n'
                                      '\t\t}',
                 'category': 'Special',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 130},
                 'name': 'Stored Power',
                 'num': 500,
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Psychic',
                 'zMove': {'basePower': 160}},
 'stormthrow': {'accuracy': 100,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Storm Throw',
                'num': 480,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting',
                'willCrit': True},
 'strangesteam': {'accuracy': 95,
                  'basePower': 90,
                  'category': 'Special',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Strange Steam',
                  'num': 790,
                  'pp': 10,
                  'priority': 0,
                  'secondary': {'chance': 20, 'volatileStatus': 'confusion'},
                  'target': 'normal',
                  'type': 'Fairy'},
 'strength': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Strength',
              'num': 70,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'strengthsap': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Cute',
                 'flags': {'heal': 1,
                           'mirror': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'name': 'Strength Sap',
                 'num': 668,
                 'onHit': 'function (target, source) {\n'
                          '\t\t\tif (target.boosts.atk === -6)\n'
                          '\t\t\t\treturn false;\n'
                          "\t\t\tvar atk = target.getStat('atk', false, "
                          'true);\n'
                          '\t\t\tvar success = this.boost({ atk: -1 }, target, '
                          'source, null, false, true);\n'
                          '\t\t\treturn !!(this.heal(atk, source, target) || '
                          'success);\n'
                          '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Grass',
                 'zMove': {'boost': {'def': 1}}},
 'stringshot': {'accuracy': 95,
                'basePower': 0,
                'boosts': {'spe': -2},
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                'name': 'String Shot',
                'num': 81,
                'pp': 40,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Bug',
                'zMove': {'boost': {'spe': 1}}},
 'struggle': {'accuracy': True,
              'basePower': 50,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'protect': 1},
              'name': 'Struggle',
              'noPPBoosts': True,
              'noSketch': True,
              'num': 165,
              'onModifyMove': 'function (move, pokemon, target) {\n'
                              "\t\t\tmove.type = '???';\n"
                              "\t\t\tthis.add('-activate', pokemon, 'move: "
                              "Struggle');\n"
                              '\t\t}',
              'pp': 1,
              'priority': 0,
              'secondary': None,
              'struggleRecoil': True,
              'target': 'randomNormal',
              'type': 'Normal'},
 'strugglebug': {'accuracy': 100,
                 'basePower': 50,
                 'category': 'Special',
                 'contestType': 'Cute',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Struggle Bug',
                 'num': 522,
                 'pp': 20,
                 'priority': 0,
                 'secondary': {'boosts': {'spa': -1}, 'chance': 100},
                 'target': 'allAdjacentFoes',
                 'type': 'Bug'},
 'stuffcheeks': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'flags': {'snatch': 1},
                 'name': 'Stuff Cheeks',
                 'num': 747,
                 'onTry': 'function (source) {\n'
                          '\t\t\tvar item = source.getItem();\n'
                          '\t\t\tif (item.isBerry && source.eatItem(true)) {\n'
                          '\t\t\t\tthis.boost({ def: 2 }, source, null, null, '
                          'false, true);\n'
                          '\t\t\t}\n'
                          '\t\t\telse {\n'
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Normal'},
 'stunspore': {'accuracy': 75,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mirror': 1,
                         'powder': 1,
                         'protect': 1,
                         'reflectable': 1},
               'name': 'Stun Spore',
               'num': 78,
               'pp': 30,
               'priority': 0,
               'secondary': None,
               'status': 'par',
               'target': 'normal',
               'type': 'Grass',
               'zMove': {'boost': {'spd': 1}}},
 'submission': {'accuracy': 80,
                'basePower': 80,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Submission',
                'num': 66,
                'pp': 20,
                'priority': 0,
                'recoil': [1, 4],
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'substitute': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'onEnd': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-end', target, "
                                       "'Substitute');\n"
                                       '\t\t\t}',
                              'onStart': 'function (target) {\n'
                                         "\t\t\t\tthis.add('-start', target, "
                                         "'Substitute');\n"
                                         '\t\t\t\tthis.effectState.hp = '
                                         'Math.floor(target.maxhp / 4);\n'
                                         '\t\t\t\tif '
                                         "(target.volatiles['partiallytrapped']) "
                                         '{\n'
                                         "\t\t\t\t\tthis.add('-end', target, "
                                         "target.volatiles['partiallytrapped'].sourceEffect, "
                                         "'[partiallytrapped]', '[silent]');\n"
                                         '\t\t\t\t\tdelete '
                                         "target.volatiles['partiallytrapped'];\n"
                                         '\t\t\t\t}\n'
                                         '\t\t\t}',
                              'onTryPrimaryHit': 'function (target, source, '
                                                 'move) {\n'
                                                 '\t\t\t\tif (target === '
                                                 'source || '
                                                 "move.flags['authentic'] || "
                                                 'move.infiltrates) {\n'
                                                 '\t\t\t\t\treturn;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tvar damage = '
                                                 'this.actions.getDamage(source, '
                                                 'target, move);\n'
                                                 '\t\t\t\tif (!damage && '
                                                 'damage !== 0) {\n'
                                                 "\t\t\t\t\tthis.add('-fail', "
                                                 'source);\n'
                                                 '\t\t\t\t\t'
                                                 "this.attrLastMove('[still]');\n"
                                                 '\t\t\t\t\treturn null;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tdamage = '
                                                 "this.runEvent('SubDamage', "
                                                 'target, source, move, '
                                                 'damage);\n'
                                                 '\t\t\t\tif (!damage) {\n'
                                                 '\t\t\t\t\treturn damage;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tif (damage > '
                                                 "target.volatiles['substitute'].hp) "
                                                 '{\n'
                                                 '\t\t\t\t\tdamage = '
                                                 "target.volatiles['substitute'].hp;\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\t'
                                                 "target.volatiles['substitute'].hp "
                                                 '-= damage;\n'
                                                 '\t\t\t\tsource.lastDamage = '
                                                 'damage;\n'
                                                 '\t\t\t\tif '
                                                 "(target.volatiles['substitute'].hp "
                                                 '<= 0) {\n'
                                                 '\t\t\t\t\tif (move.ohko)\n'
                                                 '\t\t\t\t\t\t'
                                                 "this.add('-ohko');\n"
                                                 '\t\t\t\t\t'
                                                 "target.removeVolatile('substitute');\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\telse {\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "target, 'move: Substitute', "
                                                 "'[damage]');\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tif (move.recoil) {\n'
                                                 '\t\t\t\t\t'
                                                 'this.damage(this.actions.calcRecoilDamage(damage, '
                                                 'move), source, target, '
                                                 "'recoil');\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\tif (move.drain) {\n'
                                                 '\t\t\t\t\t'
                                                 'this.heal(Math.ceil(damage * '
                                                 'move.drain[0] / '
                                                 'move.drain[1]), source, '
                                                 "target, 'drain');\n"
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\t'
                                                 "this.singleEvent('AfterSubDamage', "
                                                 'move, null, target, source, '
                                                 'move, damage);\n'
                                                 '\t\t\t\t'
                                                 "this.runEvent('AfterSubDamage', "
                                                 'target, source, move, '
                                                 'damage);\n'
                                                 '\t\t\t\treturn '
                                                 'this.HIT_SUBSTITUTE;\n'
                                                 '\t\t\t}',
                              'onTryPrimaryHitPriority': -1},
                'contestType': 'Cute',
                'flags': {'nonsky': 1, 'snatch': 1},
                'name': 'Substitute',
                'num': 164,
                'onHit': 'function (target) {\n'
                         '\t\t\tthis.directDamage(target.maxhp / 4);\n'
                         '\t\t}',
                'onTryHit': 'function (target) {\n'
                            "\t\t\tif (target.volatiles['substitute']) {\n"
                            "\t\t\t\tthis.add('-fail', target, 'move: "
                            "Substitute');\n"
                            '\t\t\t\treturn null;\n'
                            '\t\t\t}\n'
                            '\t\t\tif (target.hp <= target.maxhp / 4 || '
                            'target.maxhp === 1) { // Shedinja clause\n'
                            "\t\t\t\tthis.add('-fail', target, 'move: "
                            "Substitute', '[weak]');\n"
                            '\t\t\t\treturn null;\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'self',
                'type': 'Normal',
                'volatileStatus': 'substitute',
                'zMove': {'effect': 'clearnegativeboost'}},
 'subzeroslammer': {'accuracy': True,
                    'basePower': 1,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {},
                    'isNonstandard': 'Past',
                    'isZ': 'iciumz',
                    'name': 'Subzero Slammer',
                    'num': 650,
                    'pp': 1,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Ice'},
 'suckerpunch': {'accuracy': 100,
                 'basePower': 70,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Sucker Punch',
                 'num': 389,
                 'onTry': 'function (source, target) {\n'
                          '\t\t\tvar action = this.queue.willMove(target);\n'
                          '\t\t\tvar move = (action === null || action === '
                          "void 0 ? void 0 : action.choice) === 'move' ? "
                          'action.move : null;\n'
                          "\t\t\tif (!move || (move.category === 'Status' && "
                          "move.id !== 'mefirst') || "
                          "target.volatiles['mustrecharge']) {\n"
                          '\t\t\t\treturn false;\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 5,
                 'priority': 1,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Dark'},
 'sunnyday': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {},
              'name': 'Sunny Day',
              'num': 241,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'all',
              'type': 'Fire',
              'weather': 'sunnyday',
              'zMove': {'boost': {'spe': 1}}},
 'sunsteelstrike': {'accuracy': 100,
                    'basePower': 100,
                    'category': 'Physical',
                    'contestType': 'Cool',
                    'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                    'ignoreAbility': True,
                    'name': 'Sunsteel Strike',
                    'num': 713,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Steel'},
 'superfang': {'accuracy': 90,
               'basePower': 0,
               'category': 'Physical',
               'contestType': 'Tough',
               'damageCallback': 'function (pokemon, target) {\n'
                                 '\t\t\treturn '
                                 'this.clampIntRange(target.getUndynamaxedHP() '
                                 '/ 2, 1);\n'
                                 '\t\t}',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Super Fang',
               'num': 162,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal'},
 'superpower': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Superpower',
                'num': 276,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'self': {'boosts': {'atk': -1, 'def': -1}},
                'target': 'normal',
                'type': 'Fighting'},
 'supersonic': {'accuracy': 55,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'authentic': 1,
                          'mirror': 1,
                          'protect': 1,
                          'reflectable': 1,
                          'sound': 1},
                'name': 'Supersonic',
                'num': 48,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Normal',
                'volatileStatus': 'confusion',
                'zMove': {'boost': {'spe': 1}}},
 'supersonicskystrike': {'accuracy': True,
                         'basePower': 1,
                         'category': 'Physical',
                         'contestType': 'Cool',
                         'flags': {},
                         'isNonstandard': 'Past',
                         'isZ': 'flyiniumz',
                         'name': 'Supersonic Skystrike',
                         'num': 626,
                         'pp': 1,
                         'priority': 0,
                         'secondary': None,
                         'target': 'normal',
                         'type': 'Flying'},
 'surf': {'accuracy': 100,
          'basePower': 90,
          'category': 'Special',
          'contestType': 'Beautiful',
          'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
          'name': 'Surf',
          'num': 57,
          'pp': 15,
          'priority': 0,
          'secondary': None,
          'target': 'allAdjacent',
          'type': 'Water'},
 'surgingstrikes': {'accuracy': 100,
                    'basePower': 25,
                    'category': 'Physical',
                    'flags': {'contact': 1,
                              'mirror': 1,
                              'protect': 1,
                              'punch': 1},
                    'maxMove': {'basePower': 130},
                    'multihit': 3,
                    'name': 'Surging Strikes',
                    'num': 818,
                    'pp': 5,
                    'priority': 0,
                    'secondary': None,
                    'target': 'normal',
                    'type': 'Water',
                    'willCrit': True,
                    'zMove': {'basePower': 140}},
 'swagger': {'accuracy': 85,
             'basePower': 0,
             'boosts': {'atk': 2},
             'category': 'Status',
             'contestType': 'Cute',
             'flags': {'mirror': 1,
                       'mystery': 1,
                       'protect': 1,
                       'reflectable': 1},
             'name': 'Swagger',
             'num': 207,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Normal',
             'volatileStatus': 'confusion',
             'zMove': {'effect': 'clearnegativeboost'}},
 'swallow': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'contestType': 'Tough',
             'flags': {'heal': 1, 'snatch': 1},
             'name': 'Swallow',
             'num': 256,
             'onHit': 'function (pokemon) {\n'
                      '\t\t\tvar healAmount = [0.25, 0.5, 1];\n'
                      '\t\t\tvar healedBy = '
                      'this.heal(this.modify(pokemon.maxhp, '
                      "healAmount[(pokemon.volatiles['stockpile'].layers - "
                      '1)]));\n'
                      "\t\t\tpokemon.removeVolatile('stockpile');\n"
                      '\t\t\treturn !!healedBy;\n'
                      '\t\t}',
             'onTry': 'function (source) {\n'
                      "\t\t\treturn !!source.volatiles['stockpile'];\n"
                      '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'self',
             'type': 'Normal',
             'zMove': {'effect': 'clearnegativeboost'}},
 'sweetkiss': {'accuracy': 75,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Cute',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'name': 'Sweet Kiss',
               'num': 186,
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Fairy',
               'volatileStatus': 'confusion',
               'zMove': {'boost': {'spa': 1}}},
 'sweetscent': {'accuracy': 100,
                'basePower': 0,
                'boosts': {'evasion': -2},
                'category': 'Status',
                'contestType': 'Cute',
                'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                'name': 'Sweet Scent',
                'num': 230,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Normal',
                'zMove': {'boost': {'accuracy': 1}}},
 'swift': {'accuracy': True,
           'basePower': 60,
           'category': 'Special',
           'contestType': 'Cool',
           'flags': {'mirror': 1, 'protect': 1},
           'name': 'Swift',
           'num': 129,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'allAdjacentFoes',
           'type': 'Normal'},
 'switcheroo': {'accuracy': 100,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
                'name': 'Switcheroo',
                'num': 415,
                'onHit': 'function (target, source, move) {\n'
                         '\t\t\tvar yourItem = target.takeItem(source);\n'
                         '\t\t\tvar myItem = source.takeItem();\n'
                         '\t\t\tif (target.item || source.item || (!yourItem '
                         '&& !myItem)) {\n'
                         '\t\t\t\tif (yourItem)\n'
                         '\t\t\t\t\ttarget.item = yourItem.id;\n'
                         '\t\t\t\tif (myItem)\n'
                         '\t\t\t\t\tsource.item = myItem.id;\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\t}\n'
                         "\t\t\tif ((myItem && !this.singleEvent('TakeItem', "
                         'myItem, source.itemState, target, source, move, '
                         'myItem)) ||\n'
                         "\t\t\t\t(yourItem && !this.singleEvent('TakeItem', "
                         'yourItem, target.itemState, source, target, move, '
                         'yourItem))) {\n'
                         '\t\t\t\tif (yourItem)\n'
                         '\t\t\t\t\ttarget.item = yourItem.id;\n'
                         '\t\t\t\tif (myItem)\n'
                         '\t\t\t\t\tsource.item = myItem.id;\n'
                         '\t\t\t\treturn false;\n'
                         '\t\t\t}\n'
                         "\t\t\tthis.add('-activate', source, 'move: Trick', "
                         "'[of] ' + target);\n"
                         '\t\t\tif (myItem) {\n'
                         '\t\t\t\ttarget.setItem(myItem);\n'
                         "\t\t\t\tthis.add('-item', target, myItem, '[from] "
                         "move: Switcheroo');\n"
                         '\t\t\t}\n'
                         '\t\t\telse {\n'
                         "\t\t\t\tthis.add('-enditem', target, yourItem, "
                         "'[silent]', '[from] move: Switcheroo');\n"
                         '\t\t\t}\n'
                         '\t\t\tif (yourItem) {\n'
                         '\t\t\t\tsource.setItem(yourItem);\n'
                         "\t\t\t\tthis.add('-item', source, yourItem, '[from] "
                         "move: Switcheroo');\n"
                         '\t\t\t}\n'
                         '\t\t\telse {\n'
                         "\t\t\t\tthis.add('-enditem', source, myItem, "
                         "'[silent]', '[from] move: Switcheroo');\n"
                         '\t\t\t}\n'
                         '\t\t}',
                'onTryImmunity': 'function (target) {\n'
                                 '\t\t\treturn '
                                 "!target.hasAbility('stickyhold');\n"
                                 '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dark',
                'zMove': {'boost': {'spe': 2}}},
 'swordsdance': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'atk': 2},
                 'category': 'Status',
                 'contestType': 'Beautiful',
                 'flags': {'dance': 1, 'snatch': 1},
                 'name': 'Swords Dance',
                 'num': 14,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'self',
                 'type': 'Normal',
                 'zMove': {'effect': 'clearnegativeboost'}},
 'synchronoise': {'accuracy': 100,
                  'basePower': 120,
                  'category': 'Special',
                  'contestType': 'Clever',
                  'flags': {'mirror': 1, 'protect': 1},
                  'isNonstandard': 'Past',
                  'name': 'Synchronoise',
                  'num': 485,
                  'onTryImmunity': 'function (target, source) {\n'
                                   '\t\t\treturn '
                                   'target.hasType(source.getTypes());\n'
                                   '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'allAdjacent',
                  'type': 'Psychic'},
 'synthesis': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'heal': 1, 'snatch': 1},
               'name': 'Synthesis',
               'num': 235,
               'onHit': 'function (pokemon) {\n'
                        '\t\t\tvar factor = 0.5;\n'
                        '\t\t\tswitch (pokemon.effectiveWeather()) {\n'
                        "\t\t\t\tcase 'sunnyday':\n"
                        "\t\t\t\tcase 'desolateland':\n"
                        '\t\t\t\t\tfactor = 0.667;\n'
                        '\t\t\t\t\tbreak;\n'
                        "\t\t\t\tcase 'raindance':\n"
                        "\t\t\t\tcase 'primordialsea':\n"
                        "\t\t\t\tcase 'sandstorm':\n"
                        "\t\t\t\tcase 'hail':\n"
                        '\t\t\t\t\tfactor = 0.25;\n'
                        '\t\t\t\t\tbreak;\n'
                        '\t\t\t}\n'
                        '\t\t\treturn !!this.heal(this.modify(pokemon.maxhp, '
                        'factor));\n'
                        '\t\t}',
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'self',
               'type': 'Grass',
               'zMove': {'effect': 'clearnegativeboost'}},
 'tackle': {'accuracy': 100,
            'basePower': 40,
            'category': 'Physical',
            'contestType': 'Tough',
            'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
            'name': 'Tackle',
            'num': 33,
            'pp': 35,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal'},
 'tailglow': {'accuracy': True,
              'basePower': 0,
              'boosts': {'spa': 3},
              'category': 'Status',
              'contestType': 'Beautiful',
              'flags': {'snatch': 1},
              'isNonstandard': 'Past',
              'name': 'Tail Glow',
              'num': 294,
              'pp': 20,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Bug',
              'zMove': {'effect': 'clearnegativeboost'}},
 'tailslap': {'accuracy': 85,
              'basePower': 25,
              'category': 'Physical',
              'contestType': 'Cute',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'maxMove': {'basePower': 130},
              'multihit': [2, 5],
              'name': 'Tail Slap',
              'num': 541,
              'pp': 10,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'basePower': 140}},
 'tailwhip': {'accuracy': 100,
              'basePower': 0,
              'boosts': {'def': -1},
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
              'name': 'Tail Whip',
              'num': 39,
              'pp': 30,
              'priority': 0,
              'secondary': None,
              'target': 'allAdjacentFoes',
              'type': 'Normal',
              'zMove': {'boost': {'atk': 1}}},
 'tailwind': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'condition': {'duration': 4,
                            'durationCallback': 'function (target, source, '
                                                'effect) {\n'
                                                '\t\t\t\tif (source === null '
                                                '|| source === void 0 ? void 0 '
                                                ': '
                                                "source.hasAbility('persistent')) "
                                                '{\n'
                                                '\t\t\t\t\t'
                                                "this.add('-activate', source, "
                                                "'ability: Persistent', "
                                                'effect);\n'
                                                '\t\t\t\t\treturn 6;\n'
                                                '\t\t\t\t}\n'
                                                '\t\t\t\treturn 4;\n'
                                                '\t\t\t}',
                            'onModifySpe': 'function (spe, pokemon) {\n'
                                           '\t\t\t\treturn '
                                           'this.chainModify(2);\n'
                                           '\t\t\t}',
                            'onSideEnd': 'function (side) {\n'
                                         "\t\t\t\tthis.add('-sideend', side, "
                                         "'move: Tailwind');\n"
                                         '\t\t\t}',
                            'onSideResidualOrder': 26,
                            'onSideResidualSubOrder': 5,
                            'onSideStart': 'function (side) {\n'
                                           "\t\t\t\tthis.add('-sidestart', "
                                           "side, 'move: Tailwind');\n"
                                           '\t\t\t}'},
              'contestType': 'Cool',
              'flags': {'snatch': 1},
              'name': 'Tailwind',
              'num': 366,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'sideCondition': 'tailwind',
              'target': 'allySide',
              'type': 'Flying',
              'zMove': {'effect': 'crit2'}},
 'takedown': {'accuracy': 85,
              'basePower': 90,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Take Down',
              'num': 36,
              'pp': 20,
              'priority': 0,
              'recoil': [1, 4],
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'tarshot': {'accuracy': 100,
             'basePower': 0,
             'boosts': {'spe': -1},
             'category': 'Status',
             'condition': {'onEffectiveness': 'function (typeMod, target, '
                                              'type, move) {\n'
                                              '\t\t\t\tif (move.type !== '
                                              "'Fire')\n"
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\tif (!target)\n'
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\tif (type !== '
                                              'target.getTypes()[0])\n'
                                              '\t\t\t\t\treturn;\n'
                                              '\t\t\t\treturn typeMod + 1;\n'
                                              '\t\t\t}',
                           'onEffectivenessPriority': -2,
                           'onStart': 'function (pokemon) {\n'
                                      "\t\t\t\tthis.add('-start', pokemon, "
                                      "'Tar Shot');\n"
                                      '\t\t\t}'},
             'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
             'name': 'Tar Shot',
             'num': 749,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Rock',
             'volatileStatus': 'tarshot'},
 'taunt': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'condition': {'duration': 3,
                         'onBeforeMove': 'function (attacker, defender, move) '
                                         '{\n'
                                         '\t\t\t\tif (!move.isZ && !move.isMax '
                                         "&& move.category === 'Status' && "
                                         "move.id !== 'mefirst') {\n"
                                         "\t\t\t\t\tthis.add('cant', attacker, "
                                         "'move: Taunt', move);\n"
                                         '\t\t\t\t\treturn false;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}',
                         'onBeforeMovePriority': 5,
                         'onDisableMove': 'function (pokemon) {\n'
                                          '\t\t\t\tfor (var _i = 0, _a = '
                                          'pokemon.moveSlots; _i < _a.length; '
                                          '_i++) {\n'
                                          '\t\t\t\t\tvar moveSlot = _a[_i];\n'
                                          '\t\t\t\t\tvar move = '
                                          'this.dex.moves.get(moveSlot.id);\n'
                                          '\t\t\t\t\tif (move.category === '
                                          "'Status' && move.id !== 'mefirst') "
                                          '{\n'
                                          '\t\t\t\t\t\t'
                                          'pokemon.disableMove(moveSlot.id);\n'
                                          '\t\t\t\t\t}\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t}',
                         'onEnd': 'function (target) {\n'
                                  "\t\t\t\tthis.add('-end', target, 'move: "
                                  "Taunt');\n"
                                  '\t\t\t}',
                         'onResidualOrder': 15,
                         'onStart': 'function (target) {\n'
                                    '\t\t\t\tif (target.activeTurns && '
                                    '!this.queue.willMove(target)) {\n'
                                    '\t\t\t\t\tthis.effectState.duration++;\n'
                                    '\t\t\t\t}\n'
                                    "\t\t\t\tthis.add('-start', target, 'move: "
                                    "Taunt');\n"
                                    '\t\t\t}'},
           'contestType': 'Clever',
           'flags': {'authentic': 1,
                     'mirror': 1,
                     'protect': 1,
                     'reflectable': 1},
           'name': 'Taunt',
           'num': 269,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Dark',
           'volatileStatus': 'taunt',
           'zMove': {'boost': {'atk': 1}}},
 'tearfullook': {'accuracy': True,
                 'basePower': 0,
                 'boosts': {'atk': -1, 'spa': -1},
                 'category': 'Status',
                 'contestType': 'Cute',
                 'flags': {'mirror': 1, 'reflectable': 1},
                 'name': 'Tearful Look',
                 'num': 715,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'boost': {'def': 1}}},
 'teatime': {'accuracy': True,
             'basePower': 0,
             'category': 'Status',
             'flags': {'authentic': 1},
             'name': 'Teatime',
             'num': 752,
             'onHitField': 'function (target, source, move) {\n'
                           '\t\t\tvar result = false;\n'
                           '\t\t\tfor (var _i = 0, _a = this.getAllActive(); '
                           '_i < _a.length; _i++) {\n'
                           '\t\t\t\tvar active = _a[_i];\n'
                           "\t\t\t\tif (this.runEvent('Invulnerability', "
                           'active, source, move) === false) {\n'
                           "\t\t\t\t\tthis.add('-miss', source, active);\n"
                           '\t\t\t\t\tresult = true;\n'
                           '\t\t\t\t}\n'
                           "\t\t\t\telse if (this.runEvent('TryHit', active, "
                           'source, move)) {\n'
                           '\t\t\t\t\tvar item = active.getItem();\n'
                           '\t\t\t\t\tif (active.hp && item.isBerry) {\n'
                           '\t\t\t\t\t\t// bypasses Unnerve\n'
                           '\t\t\t\t\t\tactive.eatItem(true);\n'
                           '\t\t\t\t\t\tresult = true;\n'
                           '\t\t\t\t\t}\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t\treturn result;\n'
                           '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': None,
             'target': 'all',
             'type': 'Normal'},
 'technoblast': {'accuracy': 100,
                 'basePower': 120,
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Techno Blast',
                 'num': 546,
                 'onModifyType': 'function (move, pokemon) {\n'
                                 '\t\t\tif (pokemon.ignoringItem())\n'
                                 '\t\t\t\treturn;\n'
                                 "\t\t\tmove.type = this.runEvent('Drive', "
                                 "pokemon, null, move, 'Normal');\n"
                                 '\t\t}',
                 'pp': 5,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal'},
 'tectonicrage': {'accuracy': True,
                  'basePower': 1,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {},
                  'isNonstandard': 'Past',
                  'isZ': 'groundiumz',
                  'name': 'Tectonic Rage',
                  'num': 630,
                  'pp': 1,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Ground'},
 'teeterdance': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Cute',
                 'flags': {'dance': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Teeter Dance',
                 'num': 298,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'allAdjacent',
                 'type': 'Normal',
                 'volatileStatus': 'confusion',
                 'zMove': {'boost': {'spa': 1}}},
 'telekinesis': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'duration': 3,
                               'onAccuracy': 'function (accuracy, target, '
                                             'source, move) {\n'
                                             '\t\t\t\tif (move && !move.ohko)\n'
                                             '\t\t\t\t\treturn true;\n'
                                             '\t\t\t}',
                               'onAccuracyPriority': -1,
                               'onEnd': 'function (target) {\n'
                                        "\t\t\t\tthis.add('-end', target, "
                                        "'Telekinesis');\n"
                                        '\t\t\t}',
                               'onImmunity': 'function (type) {\n'
                                             "\t\t\t\tif (type === 'Ground')\n"
                                             '\t\t\t\t\treturn false;\n'
                                             '\t\t\t}',
                               'onResidualOrder': 19,
                               'onStart': 'function (target) {\n'
                                          "\t\t\t\tif (['Diglett', 'Dugtrio', "
                                          "'Palossand', "
                                          "'Sandygast'].includes(target.baseSpecies.baseSpecies) "
                                          '||\n'
                                          '\t\t\t\t\ttarget.baseSpecies.name '
                                          "=== 'Gengar-Mega') {\n"
                                          "\t\t\t\t\tthis.add('-immune', "
                                          'target);\n'
                                          '\t\t\t\t\treturn null;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\tif '
                                          "(target.volatiles['smackdown'] || "
                                          "target.volatiles['ingrain'])\n"
                                          '\t\t\t\t\treturn false;\n'
                                          "\t\t\t\tthis.add('-start', target, "
                                          "'Telekinesis');\n"
                                          '\t\t\t}',
                               'onUpdate': 'function (pokemon) {\n'
                                           '\t\t\t\tif '
                                           '(pokemon.baseSpecies.name === '
                                           "'Gengar-Mega') {\n"
                                           '\t\t\t\t\tdelete '
                                           "pokemon.volatiles['telekinesis'];\n"
                                           "\t\t\t\t\tthis.add('-end', "
                                           "pokemon, 'Telekinesis', "
                                           "'[silent]');\n"
                                           '\t\t\t\t}\n'
                                           '\t\t\t}'},
                 'contestType': 'Clever',
                 'flags': {'gravity': 1,
                           'mirror': 1,
                           'mystery': 1,
                           'protect': 1,
                           'reflectable': 1},
                 'isNonstandard': 'Past',
                 'name': 'Telekinesis',
                 'num': 477,
                 'onTry': 'function (source, target, move) {\n'
                          '\t\t\t// Additional Gravity check for Z-move '
                          'variant\n'
                          "\t\t\tif (this.field.getPseudoWeather('Gravity')) "
                          '{\n'
                          "\t\t\t\tthis.attrLastMove('[still]');\n"
                          "\t\t\t\tthis.add('cant', source, 'move: Gravity', "
                          'move);\n'
                          '\t\t\t\treturn null;\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Psychic',
                 'volatileStatus': 'telekinesis',
                 'zMove': {'boost': {'spa': 1}}},
 'teleport': {'accuracy': True,
              'basePower': 0,
              'category': 'Status',
              'contestType': 'Cool',
              'flags': {},
              'name': 'Teleport',
              'num': 100,
              'onTryHit': True,
              'pp': 20,
              'priority': -6,
              'secondary': None,
              'selfSwitch': True,
              'target': 'self',
              'type': 'Psychic',
              'zMove': {'effect': 'heal'}},
 'terrainpulse': {'accuracy': 100,
                  'basePower': 50,
                  'category': 'Special',
                  'flags': {'mirror': 1, 'protect': 1, 'pulse': 1},
                  'maxMove': {'basePower': 130},
                  'name': 'Terrain Pulse',
                  'num': 805,
                  'onModifyMove': 'function (move, pokemon) {\n'
                                  '\t\t\tif (this.field.terrain && '
                                  'pokemon.isGrounded()) {\n'
                                  '\t\t\t\tmove.basePower *= 2;\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                  'onModifyType': 'function (move, pokemon) {\n'
                                  '\t\t\tif (!pokemon.isGrounded())\n'
                                  '\t\t\t\treturn;\n'
                                  '\t\t\tswitch (this.field.terrain) {\n'
                                  "\t\t\t\tcase 'electricterrain':\n"
                                  "\t\t\t\t\tmove.type = 'Electric';\n"
                                  '\t\t\t\t\tbreak;\n'
                                  "\t\t\t\tcase 'grassyterrain':\n"
                                  "\t\t\t\t\tmove.type = 'Grass';\n"
                                  '\t\t\t\t\tbreak;\n'
                                  "\t\t\t\tcase 'mistyterrain':\n"
                                  "\t\t\t\t\tmove.type = 'Fairy';\n"
                                  '\t\t\t\t\tbreak;\n'
                                  "\t\t\t\tcase 'psychicterrain':\n"
                                  "\t\t\t\t\tmove.type = 'Psychic';\n"
                                  '\t\t\t\t\tbreak;\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                  'pp': 10,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Normal',
                  'zMove': {'basePower': 160}},
 'thief': {'accuracy': 100,
           'basePower': 60,
           'category': 'Physical',
           'contestType': 'Tough',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'Thief',
           'num': 168,
           'onAfterHit': 'function (target, source, move) {\n'
                         "\t\t\tif (source.item || source.volatiles['gem']) {\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         '\t\t\tvar yourItem = target.takeItem(source);\n'
                         '\t\t\tif (!yourItem) {\n'
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tif (!this.singleEvent('TakeItem', yourItem, "
                         'target.itemState, source, target, move, yourItem) '
                         '||\n'
                         '\t\t\t\t!source.setItem(yourItem)) {\n'
                         '\t\t\t\ttarget.item = yourItem.id; // bypass setItem '
                         "so we don't break choicelock or anything\n"
                         '\t\t\t\treturn;\n'
                         '\t\t\t}\n'
                         "\t\t\tthis.add('-enditem', target, yourItem, "
                         "'[silent]', '[from] move: Thief', '[of] ' + "
                         'source);\n'
                         "\t\t\tthis.add('-item', source, yourItem, '[from] "
                         "move: Thief', '[of] ' + target);\n"
                         '\t\t}',
           'pp': 25,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Dark'},
 'thousandarrows': {'accuracy': 100,
                    'basePower': 90,
                    'category': 'Physical',
                    'contestType': 'Beautiful',
                    'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                    'ignoreImmunity': {'Ground': True},
                    'name': 'Thousand Arrows',
                    'num': 614,
                    'onEffectiveness': 'function (typeMod, target, type, move) '
                                       '{\n'
                                       "\t\t\tif (move.type !== 'Ground')\n"
                                       '\t\t\t\treturn;\n'
                                       '\t\t\tif (!target)\n'
                                       '\t\t\t\treturn; // avoid crashing when '
                                       'called from a chat plugin\n'
                                       '\t\t\t// ignore effectiveness if the '
                                       'target is Flying type and immune to '
                                       'Ground\n'
                                       '\t\t\tif '
                                       "(!target.runImmunity('Ground')) {\n"
                                       "\t\t\t\tif (target.hasType('Flying'))\n"
                                       '\t\t\t\t\treturn 0;\n'
                                       '\t\t\t}\n'
                                       '\t\t}',
                    'pp': 10,
                    'priority': 0,
                    'secondary': None,
                    'target': 'allAdjacentFoes',
                    'type': 'Ground',
                    'volatileStatus': 'smackdown',
                    'zMove': {'basePower': 180}},
 'thousandwaves': {'accuracy': 100,
                   'basePower': 90,
                   'category': 'Physical',
                   'contestType': 'Tough',
                   'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                   'name': 'Thousand Waves',
                   'num': 615,
                   'onHit': 'function (target, source, move) {\n'
                            '\t\t\tif (source.isActive)\n'
                            "\t\t\t\ttarget.addVolatile('trapped', source, "
                            "move, 'trapper');\n"
                            '\t\t}',
                   'pp': 10,
                   'priority': 0,
                   'secondary': None,
                   'target': 'allAdjacentFoes',
                   'type': 'Ground'},
 'thrash': {'accuracy': 100,
            'basePower': 120,
            'category': 'Physical',
            'contestType': 'Tough',
            'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
            'name': 'Thrash',
            'num': 37,
            'onAfterMove': 'function (pokemon) {\n'
                           "\t\t\tif (pokemon.volatiles['lockedmove'] && "
                           "pokemon.volatiles['lockedmove'].duration === 1) {\n"
                           "\t\t\t\tpokemon.removeVolatile('lockedmove');\n"
                           '\t\t\t}\n'
                           '\t\t}',
            'pp': 10,
            'priority': 0,
            'secondary': None,
            'self': {'volatileStatus': 'lockedmove'},
            'target': 'randomNormal',
            'type': 'Normal'},
 'throatchop': {'accuracy': 100,
                'basePower': 80,
                'category': 'Physical',
                'condition': {'duration': 2,
                              'onBeforeMove': 'function (pokemon, target, '
                                              'move) {\n'
                                              '\t\t\t\tif (!move.isZ && '
                                              '!move.isMax && '
                                              "move.flags['sound']) {\n"
                                              "\t\t\t\t\tthis.add('cant', "
                                              "pokemon, 'move: Throat Chop');\n"
                                              '\t\t\t\t\treturn false;\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                              'onBeforeMovePriority': 6,
                              'onDisableMove': 'function (pokemon) {\n'
                                               '\t\t\t\tfor (var _i = 0, _a = '
                                               'pokemon.moveSlots; _i < '
                                               '_a.length; _i++) {\n'
                                               '\t\t\t\t\tvar moveSlot = '
                                               '_a[_i];\n'
                                               '\t\t\t\t\tif '
                                               "(this.dex.moves.get(moveSlot.id).flags['sound']) "
                                               '{\n'
                                               '\t\t\t\t\t\t'
                                               'pokemon.disableMove(moveSlot.id);\n'
                                               '\t\t\t\t\t}\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                              'onEnd': 'function (target) {\n'
                                       "\t\t\t\tthis.add('-end', target, "
                                       "'Throat Chop', '[silent]');\n"
                                       '\t\t\t}',
                              'onModifyMove': 'function (move, pokemon, '
                                              'target) {\n'
                                              '\t\t\t\tif (!move.isZ && '
                                              '!move.isMax && '
                                              "move.flags['sound']) {\n"
                                              "\t\t\t\t\tthis.add('cant', "
                                              "pokemon, 'move: Throat Chop');\n"
                                              '\t\t\t\t\treturn false;\n'
                                              '\t\t\t\t}\n'
                                              '\t\t\t}',
                              'onResidualOrder': 22,
                              'onStart': 'function (target) {\n'
                                         "\t\t\t\tthis.add('-start', target, "
                                         "'Throat Chop', '[silent]');\n"
                                         '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Throat Chop',
                'num': 675,
                'pp': 15,
                'priority': 0,
                'secondary': {'chance': 100,
                              'onHit': 'function (target) {\n'
                                       '\t\t\t\t'
                                       "target.addVolatile('throatchop');\n"
                                       '\t\t\t}'},
                'target': 'normal',
                'type': 'Dark'},
 'thunder': {'accuracy': 70,
             'basePower': 110,
             'category': 'Special',
             'contestType': 'Cool',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Thunder',
             'num': 87,
             'onModifyMove': 'function (move, pokemon, target) {\n'
                             '\t\t\tswitch (target === null || target === void '
                             '0 ? void 0 : target.effectiveWeather()) {\n'
                             "\t\t\t\tcase 'raindance':\n"
                             "\t\t\t\tcase 'primordialsea':\n"
                             '\t\t\t\t\tmove.accuracy = true;\n'
                             '\t\t\t\t\tbreak;\n'
                             "\t\t\t\tcase 'sunnyday':\n"
                             "\t\t\t\tcase 'desolateland':\n"
                             '\t\t\t\t\tmove.accuracy = 50;\n'
                             '\t\t\t\t\tbreak;\n'
                             '\t\t\t}\n'
                             '\t\t}',
             'pp': 10,
             'priority': 0,
             'secondary': {'chance': 30, 'status': 'par'},
             'target': 'normal',
             'type': 'Electric'},
 'thunderbolt': {'accuracy': 100,
                 'basePower': 90,
                 'category': 'Special',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Thunderbolt',
                 'num': 85,
                 'pp': 15,
                 'priority': 0,
                 'secondary': {'chance': 10, 'status': 'par'},
                 'target': 'normal',
                 'type': 'Electric'},
 'thundercage': {'accuracy': 90,
                 'basePower': 80,
                 'category': 'Special',
                 'flags': {'mirror': 1, 'protect': 1},
                 'name': 'Thunder Cage',
                 'num': 819,
                 'pp': 15,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Electric',
                 'volatileStatus': 'partiallytrapped'},
 'thunderfang': {'accuracy': 95,
                 'basePower': 65,
                 'category': 'Physical',
                 'contestType': 'Cool',
                 'flags': {'bite': 1, 'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Thunder Fang',
                 'num': 422,
                 'pp': 15,
                 'priority': 0,
                 'secondaries': [{'chance': 10, 'status': 'par'},
                                 {'chance': 10, 'volatileStatus': 'flinch'}],
                 'target': 'normal',
                 'type': 'Electric'},
 'thunderouskick': {'accuracy': 100,
                    'basePower': 90,
                    'category': 'Physical',
                    'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                    'name': 'Thunderous Kick',
                    'num': 823,
                    'pp': 10,
                    'priority': 0,
                    'secondary': {'boosts': {'def': -1}, 'chance': 100},
                    'target': 'normal',
                    'type': 'Fighting'},
 'thunderpunch': {'accuracy': 100,
                  'basePower': 75,
                  'category': 'Physical',
                  'contestType': 'Cool',
                  'flags': {'contact': 1,
                            'mirror': 1,
                            'protect': 1,
                            'punch': 1},
                  'name': 'Thunder Punch',
                  'num': 9,
                  'pp': 15,
                  'priority': 0,
                  'secondary': {'chance': 10, 'status': 'par'},
                  'target': 'normal',
                  'type': 'Electric'},
 'thundershock': {'accuracy': 100,
                  'basePower': 40,
                  'category': 'Special',
                  'contestType': 'Cool',
                  'flags': {'mirror': 1, 'protect': 1},
                  'name': 'Thunder Shock',
                  'num': 84,
                  'pp': 30,
                  'priority': 0,
                  'secondary': {'chance': 10, 'status': 'par'},
                  'target': 'normal',
                  'type': 'Electric'},
 'thunderwave': {'accuracy': 90,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Cool',
                 'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                 'ignoreImmunity': False,
                 'name': 'Thunder Wave',
                 'num': 86,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'status': 'par',
                 'target': 'normal',
                 'type': 'Electric',
                 'zMove': {'boost': {'spd': 1}}},
 'tickle': {'accuracy': 100,
            'basePower': 0,
            'boosts': {'atk': -1, 'def': -1},
            'category': 'Status',
            'contestType': 'Cute',
            'flags': {'mirror': 1,
                      'mystery': 1,
                      'protect': 1,
                      'reflectable': 1},
            'name': 'Tickle',
            'num': 321,
            'pp': 20,
            'priority': 0,
            'secondary': None,
            'target': 'normal',
            'type': 'Normal',
            'zMove': {'boost': {'def': 1}}},
 'topsyturvy': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'contestType': 'Clever',
                'flags': {'mirror': 1,
                          'mystery': 1,
                          'protect': 1,
                          'reflectable': 1},
                'name': 'Topsy-Turvy',
                'num': 576,
                'onHit': 'function (target) {\n'
                         '\t\t\tvar success = false;\n'
                         '\t\t\tvar i;\n'
                         '\t\t\tfor (i in target.boosts) {\n'
                         '\t\t\t\tif (target.boosts[i] === 0)\n'
                         '\t\t\t\t\tcontinue;\n'
                         '\t\t\t\ttarget.boosts[i] = -target.boosts[i];\n'
                         '\t\t\t\tsuccess = true;\n'
                         '\t\t\t}\n'
                         '\t\t\tif (!success)\n'
                         '\t\t\t\treturn false;\n'
                         "\t\t\tthis.add('-invertboost', target, '[from] move: "
                         "Topsy-Turvy');\n"
                         '\t\t}',
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dark',
                'zMove': {'boost': {'atk': 1}}},
 'torment': {'accuracy': 100,
             'basePower': 0,
             'category': 'Status',
             'condition': {'noCopy': True,
                           'onDisableMove': 'function (pokemon) {\n'
                                            '\t\t\t\tif (pokemon.lastMove && '
                                            'pokemon.lastMove.id !== '
                                            "'struggle')\n"
                                            '\t\t\t\t\t'
                                            'pokemon.disableMove(pokemon.lastMove.id);\n'
                                            '\t\t\t}',
                           'onEnd': 'function (pokemon) {\n'
                                    "\t\t\t\tthis.add('-end', pokemon, "
                                    "'Torment');\n"
                                    '\t\t\t}',
                           'onStart': 'function (pokemon) {\n'
                                      '\t\t\t\tif '
                                      "(pokemon.volatiles['dynamax']) {\n"
                                      '\t\t\t\t\tdelete '
                                      "pokemon.volatiles['torment'];\n"
                                      '\t\t\t\t\treturn false;\n'
                                      '\t\t\t\t}\n'
                                      "\t\t\t\tthis.add('-start', pokemon, "
                                      "'Torment');\n"
                                      '\t\t\t}'},
             'contestType': 'Tough',
             'flags': {'authentic': 1,
                       'mirror': 1,
                       'protect': 1,
                       'reflectable': 1},
             'name': 'Torment',
             'num': 259,
             'pp': 15,
             'priority': 0,
             'secondary': None,
             'target': 'normal',
             'type': 'Dark',
             'volatileStatus': 'torment',
             'zMove': {'boost': {'def': 1}}},
 'toxic': {'accuracy': 90,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Clever',
           'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
           'name': 'Toxic',
           'num': 92,
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'status': 'tox',
           'target': 'normal',
           'type': 'Poison',
           'zMove': {'boost': {'def': 1}}},
 'toxicspikes': {'accuracy': True,
                 'basePower': 0,
                 'category': 'Status',
                 'condition': {'onSideRestart': 'function (side) {\n'
                                                '\t\t\t\tif '
                                                '(this.effectState.layers >= '
                                                '2)\n'
                                                '\t\t\t\t\treturn false;\n'
                                                '\t\t\t\t'
                                                "this.add('-sidestart', side, "
                                                "'move: Toxic Spikes');\n"
                                                '\t\t\t\t'
                                                'this.effectState.layers++;\n'
                                                '\t\t\t}',
                               'onSideStart': 'function (side) {\n'
                                              "\t\t\t\tthis.add('-sidestart', "
                                              "side, 'move: Toxic Spikes');\n"
                                              '\t\t\t\tthis.effectState.layers '
                                              '= 1;\n'
                                              '\t\t\t}',
                               'onSwitchIn': 'function (pokemon) {\n'
                                             '\t\t\t\tif '
                                             '(!pokemon.isGrounded())\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\tif '
                                             "(pokemon.hasType('Poison')) {\n"
                                             "\t\t\t\t\tthis.add('-sideend', "
                                             "pokemon.side, 'move: Toxic "
                                             "Spikes', '[of] ' + pokemon);\n"
                                             '\t\t\t\t\t'
                                             "pokemon.side.removeSideCondition('toxicspikes');\n"
                                             '\t\t\t\t}\n'
                                             '\t\t\t\telse if '
                                             "(pokemon.hasType('Steel') || "
                                             "pokemon.hasItem('heavydutyboots')) "
                                             '{\n'
                                             '\t\t\t\t\treturn;\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\telse if '
                                             '(this.effectState.layers >= 2) '
                                             '{\n'
                                             '\t\t\t\t\t'
                                             "pokemon.trySetStatus('tox', "
                                             'pokemon.side.foe.active[0]);\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t\telse {\n'
                                             '\t\t\t\t\t'
                                             "pokemon.trySetStatus('psn', "
                                             'pokemon.side.foe.active[0]);\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}'},
                 'contestType': 'Clever',
                 'flags': {'nonsky': 1, 'reflectable': 1},
                 'name': 'Toxic Spikes',
                 'num': 390,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'sideCondition': 'toxicspikes',
                 'target': 'foeSide',
                 'type': 'Poison',
                 'zMove': {'boost': {'def': 1}}},
 'toxicthread': {'accuracy': 100,
                 'basePower': 0,
                 'boosts': {'spe': -1},
                 'category': 'Status',
                 'contestType': 'Tough',
                 'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                 'isNonstandard': 'Past',
                 'name': 'Toxic Thread',
                 'num': 672,
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'status': 'psn',
                 'target': 'normal',
                 'type': 'Poison',
                 'zMove': {'boost': {'spe': 1}}},
 'transform': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mystery': 1},
               'name': 'Transform',
               'num': 144,
               'onHit': 'function (target, pokemon) {\n'
                        '\t\t\tif (!pokemon.transformInto(target)) {\n'
                        '\t\t\t\treturn false;\n'
                        '\t\t\t}\n'
                        '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'effect': 'heal'}},
 'triattack': {'accuracy': 100,
               'basePower': 80,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Tri Attack',
               'num': 161,
               'pp': 10,
               'priority': 0,
               'secondary': {'chance': 20,
                             'onHit': 'function (target, source) {\n'
                                      '\t\t\t\tvar result = this.random(3);\n'
                                      '\t\t\t\tif (result === 0) {\n'
                                      "\t\t\t\t\ttarget.trySetStatus('brn', "
                                      'source);\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\telse if (result === 1) {\n'
                                      "\t\t\t\t\ttarget.trySetStatus('par', "
                                      'source);\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t\telse {\n'
                                      "\t\t\t\t\ttarget.trySetStatus('frz', "
                                      'source);\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}'},
               'target': 'normal',
               'type': 'Normal'},
 'trick': {'accuracy': 100,
           'basePower': 0,
           'category': 'Status',
           'contestType': 'Clever',
           'flags': {'mirror': 1, 'mystery': 1, 'protect': 1},
           'name': 'Trick',
           'num': 271,
           'onHit': 'function (target, source, move) {\n'
                    '\t\t\tvar yourItem = target.takeItem(source);\n'
                    '\t\t\tvar myItem = source.takeItem();\n'
                    '\t\t\tif (target.item || source.item || (!yourItem && '
                    '!myItem)) {\n'
                    '\t\t\t\tif (yourItem)\n'
                    '\t\t\t\t\ttarget.item = yourItem.id;\n'
                    '\t\t\t\tif (myItem)\n'
                    '\t\t\t\t\tsource.item = myItem.id;\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\t}\n'
                    "\t\t\tif ((myItem && !this.singleEvent('TakeItem', "
                    'myItem, source.itemState, target, source, move, myItem)) '
                    '||\n'
                    "\t\t\t\t(yourItem && !this.singleEvent('TakeItem', "
                    'yourItem, target.itemState, source, target, move, '
                    'yourItem))) {\n'
                    '\t\t\t\tif (yourItem)\n'
                    '\t\t\t\t\ttarget.item = yourItem.id;\n'
                    '\t\t\t\tif (myItem)\n'
                    '\t\t\t\t\tsource.item = myItem.id;\n'
                    '\t\t\t\treturn false;\n'
                    '\t\t\t}\n'
                    "\t\t\tthis.add('-activate', source, 'move: Trick', '[of] "
                    "' + target);\n"
                    '\t\t\tif (myItem) {\n'
                    '\t\t\t\ttarget.setItem(myItem);\n'
                    "\t\t\t\tthis.add('-item', target, myItem, '[from] move: "
                    "Trick');\n"
                    '\t\t\t}\n'
                    '\t\t\telse {\n'
                    "\t\t\t\tthis.add('-enditem', target, yourItem, "
                    "'[silent]', '[from] move: Trick');\n"
                    '\t\t\t}\n'
                    '\t\t\tif (yourItem) {\n'
                    '\t\t\t\tsource.setItem(yourItem);\n'
                    "\t\t\t\tthis.add('-item', source, yourItem, '[from] move: "
                    "Trick');\n"
                    '\t\t\t}\n'
                    '\t\t\telse {\n'
                    "\t\t\t\tthis.add('-enditem', source, myItem, '[silent]', "
                    "'[from] move: Trick');\n"
                    '\t\t\t}\n'
                    '\t\t}',
           'onTryImmunity': 'function (target) {\n'
                            "\t\t\treturn !target.hasAbility('stickyhold');\n"
                            '\t\t}',
           'pp': 10,
           'priority': 0,
           'secondary': None,
           'target': 'normal',
           'type': 'Psychic',
           'zMove': {'boost': {'spe': 2}}},
 'trickortreat': {'accuracy': 100,
                  'basePower': 0,
                  'category': 'Status',
                  'contestType': 'Cute',
                  'flags': {'mirror': 1,
                            'mystery': 1,
                            'protect': 1,
                            'reflectable': 1},
                  'name': 'Trick-or-Treat',
                  'num': 567,
                  'onHit': 'function (target) {\n'
                           "\t\t\tif (target.hasType('Ghost'))\n"
                           '\t\t\t\treturn false;\n'
                           "\t\t\tif (!target.addType('Ghost'))\n"
                           '\t\t\t\treturn false;\n'
                           "\t\t\tthis.add('-start', target, 'typeadd', "
                           "'Ghost', '[from] move: Trick-or-Treat');\n"
                           '\t\t\tif (target.side.active.length === 2 && '
                           'target.position === 1) {\n'
                           '\t\t\t\t// Curse Glitch\n'
                           '\t\t\t\tvar action = this.queue.willMove(target);\n'
                           "\t\t\t\tif (action && action.move.id === 'curse') "
                           '{\n'
                           '\t\t\t\t\taction.targetLoc = -1;\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t}',
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Ghost',
                  'zMove': {'boost': {'atk': 1,
                                      'def': 1,
                                      'spa': 1,
                                      'spd': 1,
                                      'spe': 1}}},
 'trickroom': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 5,
                             'durationCallback': 'function (source, effect) {\n'
                                                 '\t\t\t\tif (source === null '
                                                 '|| source === void 0 ? void '
                                                 '0 : '
                                                 "source.hasAbility('persistent')) "
                                                 '{\n'
                                                 '\t\t\t\t\t'
                                                 "this.add('-activate', "
                                                 "source, 'ability: "
                                                 "Persistent', effect);\n"
                                                 '\t\t\t\t\treturn 7;\n'
                                                 '\t\t\t\t}\n'
                                                 '\t\t\t\treturn 5;\n'
                                                 '\t\t\t}',
                             'onFieldEnd': 'function () {\n'
                                           "\t\t\t\tthis.add('-fieldend', "
                                           "'move: Trick Room');\n"
                                           '\t\t\t}',
                             'onFieldResidualOrder': 27,
                             'onFieldResidualSubOrder': 1,
                             'onFieldRestart': 'function (target, source) {\n'
                                               '\t\t\t\t'
                                               "this.field.removePseudoWeather('trickroom');\n"
                                               '\t\t\t}',
                             'onFieldStart': 'function (target, source) {\n'
                                             "\t\t\t\tthis.add('-fieldstart', "
                                             "'move: Trick Room', '[of] ' + "
                                             'source);\n'
                                             '\t\t\t}'},
               'contestType': 'Clever',
               'flags': {'mirror': 1},
               'name': 'Trick Room',
               'num': 433,
               'pp': 5,
               'priority': -7,
               'pseudoWeather': 'trickroom',
               'secondary': None,
               'target': 'all',
               'type': 'Psychic',
               'zMove': {'boost': {'accuracy': 1}}},
 'tripleaxel': {'accuracy': 90,
                'basePower': 20,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     '\t\t\treturn 20 * move.hit;\n'
                                     '\t\t}',
                'category': 'Physical',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 140},
                'multiaccuracy': True,
                'multihit': 3,
                'name': 'Triple Axel',
                'num': 813,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Ice',
                'zMove': {'basePower': 120}},
 'triplekick': {'accuracy': 90,
                'basePower': 10,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     '\t\t\treturn 10 * move.hit;\n'
                                     '\t\t}',
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'maxMove': {'basePower': 80},
                'multiaccuracy': True,
                'multihit': 3,
                'name': 'Triple Kick',
                'num': 167,
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting',
                'zMove': {'basePower': 120}},
 'tropkick': {'accuracy': 100,
              'basePower': 70,
              'category': 'Physical',
              'contestType': 'Cute',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Trop Kick',
              'num': 688,
              'pp': 15,
              'priority': 0,
              'secondary': {'boosts': {'atk': -1}, 'chance': 100},
              'target': 'normal',
              'type': 'Grass'},
 'trumpcard': {'accuracy': True,
               'basePower': 0,
               'basePowerCallback': 'function (source, target, move) {\n'
                                    '\t\t\tvar callerMoveId = '
                                    'move.sourceEffect || move.id;\n'
                                    '\t\t\tvar moveSlot = callerMoveId === '
                                    "'instruct' ? source.getMoveData(move.id) "
                                    ': source.getMoveData(callerMoveId);\n'
                                    '\t\t\tif (!moveSlot)\n'
                                    '\t\t\t\treturn 40;\n'
                                    '\t\t\tswitch (moveSlot.pp) {\n'
                                    '\t\t\t\tcase 0:\n'
                                    '\t\t\t\t\treturn 200;\n'
                                    '\t\t\t\tcase 1:\n'
                                    '\t\t\t\t\treturn 80;\n'
                                    '\t\t\t\tcase 2:\n'
                                    '\t\t\t\t\treturn 60;\n'
                                    '\t\t\t\tcase 3:\n'
                                    '\t\t\t\t\treturn 50;\n'
                                    '\t\t\t\tdefault:\n'
                                    '\t\t\t\t\treturn 40;\n'
                                    '\t\t\t}\n'
                                    '\t\t}',
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'maxMove': {'basePower': 130},
               'name': 'Trump Card',
               'noPPBoosts': True,
               'num': 376,
               'pp': 5,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'basePower': 160}},
 'twineedle': {'accuracy': 100,
               'basePower': 25,
               'category': 'Physical',
               'contestType': 'Cool',
               'flags': {'mirror': 1, 'protect': 1},
               'isNonstandard': 'Past',
               'maxMove': {'basePower': 100},
               'multihit': 2,
               'name': 'Twineedle',
               'num': 41,
               'pp': 20,
               'priority': 0,
               'secondary': {'chance': 20, 'status': 'psn'},
               'target': 'normal',
               'type': 'Bug'},
 'twinkletackle': {'accuracy': True,
                   'basePower': 1,
                   'category': 'Physical',
                   'contestType': 'Cool',
                   'flags': {},
                   'isNonstandard': 'Past',
                   'isZ': 'fairiumz',
                   'name': 'Twinkle Tackle',
                   'num': 656,
                   'pp': 1,
                   'priority': 0,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Fairy'},
 'twister': {'accuracy': 100,
             'basePower': 40,
             'category': 'Special',
             'contestType': 'Cool',
             'flags': {'mirror': 1, 'protect': 1},
             'name': 'Twister',
             'num': 239,
             'pp': 20,
             'priority': 0,
             'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
             'target': 'allAdjacentFoes',
             'type': 'Dragon'},
 'uproar': {'accuracy': 100,
            'basePower': 90,
            'category': 'Special',
            'condition': {'duration': 3,
                          'onAnySetStatus': 'function (status, pokemon) {\n'
                                            "\t\t\t\tif (status.id === 'slp') "
                                            '{\n'
                                            '\t\t\t\t\tif (pokemon === '
                                            'this.effectState.target) {\n'
                                            "\t\t\t\t\t\tthis.add('-fail', "
                                            "pokemon, 'slp', '[from] Uproar', "
                                            "'[msg]');\n"
                                            '\t\t\t\t\t}\n'
                                            '\t\t\t\t\telse {\n'
                                            "\t\t\t\t\t\tthis.add('-fail', "
                                            "pokemon, 'slp', '[from] "
                                            "Uproar');\n"
                                            '\t\t\t\t\t}\n'
                                            '\t\t\t\t\treturn null;\n'
                                            '\t\t\t\t}\n'
                                            '\t\t\t}',
                          'onEnd': 'function (target) {\n'
                                   "\t\t\t\tthis.add('-end', target, "
                                   "'Uproar');\n"
                                   '\t\t\t}',
                          'onLockMove': 'uproar',
                          'onResidual': 'function (target) {\n'
                                        '\t\t\t\tif '
                                        "(target.volatiles['throatchop']) {\n"
                                        '\t\t\t\t\t'
                                        "target.removeVolatile('uproar');\n"
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t\tif (target.lastMove && '
                                        "target.lastMove.id === 'struggle') {\n"
                                        "\t\t\t\t\t// don't lock\n"
                                        '\t\t\t\t\tdelete '
                                        "target.volatiles['uproar'];\n"
                                        '\t\t\t\t}\n'
                                        "\t\t\t\tthis.add('-start', target, "
                                        "'Uproar', '[upkeep]');\n"
                                        '\t\t\t}',
                          'onResidualOrder': 28,
                          'onResidualSubOrder': 1,
                          'onStart': 'function (target) {\n'
                                     "\t\t\t\tthis.add('-start', target, "
                                     "'Uproar');\n"
                                     '\t\t\t}'},
            'contestType': 'Cute',
            'flags': {'authentic': 1, 'mirror': 1, 'protect': 1, 'sound': 1},
            'name': 'Uproar',
            'num': 253,
            'onTryHit': 'function (target) {\n'
                        '\t\t\tvar activeTeam = target.side.activeTeam();\n'
                        '\t\t\tvar foeActiveTeam = '
                        'target.side.foe.activeTeam();\n'
                        '\t\t\tfor (var _i = 0, _a = activeTeam.entries(); _i '
                        '< _a.length; _i++) {\n'
                        '\t\t\t\tvar _b = _a[_i], i = _b[0], allyActive = '
                        '_b[1];\n'
                        '\t\t\t\tif (allyActive && allyActive.status === '
                        "'slp')\n"
                        '\t\t\t\t\tallyActive.cureStatus();\n'
                        '\t\t\t\tvar foeActive = foeActiveTeam[i];\n'
                        "\t\t\t\tif (foeActive && foeActive.status === 'slp')\n"
                        '\t\t\t\t\tfoeActive.cureStatus();\n'
                        '\t\t\t}\n'
                        '\t\t}',
            'pp': 10,
            'priority': 0,
            'secondary': None,
            'self': {'volatileStatus': 'uproar'},
            'target': 'randomNormal',
            'type': 'Normal'},
 'uturn': {'accuracy': 100,
           'basePower': 70,
           'category': 'Physical',
           'contestType': 'Cute',
           'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
           'name': 'U-turn',
           'num': 369,
           'pp': 20,
           'priority': 0,
           'secondary': None,
           'selfSwitch': True,
           'target': 'normal',
           'type': 'Bug'},
 'vacuumwave': {'accuracy': 100,
                'basePower': 40,
                'category': 'Special',
                'contestType': 'Cool',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Vacuum Wave',
                'num': 410,
                'pp': 30,
                'priority': 1,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'vcreate': {'accuracy': 95,
             'basePower': 180,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'V-create',
             'num': 557,
             'pp': 5,
             'priority': 0,
             'secondary': None,
             'self': {'boosts': {'def': -1, 'spd': -1, 'spe': -1}},
             'target': 'normal',
             'type': 'Fire',
             'zMove': {'basePower': 220}},
 'veeveevolley': {'accuracy': True,
                  'basePower': 0,
                  'basePowerCallback': 'function (pokemon) {\n'
                                       '\t\t\treturn '
                                       'Math.floor((pokemon.happiness * 10) / '
                                       '25) || 1;\n'
                                       '\t\t}',
                  'category': 'Physical',
                  'contestType': 'Cute',
                  'flags': {'contact': 1, 'protect': 1},
                  'isNonstandard': 'LGPE',
                  'name': 'Veevee Volley',
                  'num': 741,
                  'pp': 20,
                  'priority': 0,
                  'secondary': None,
                  'target': 'normal',
                  'type': 'Normal'},
 'venomdrench': {'accuracy': 100,
                 'basePower': 0,
                 'category': 'Status',
                 'contestType': 'Clever',
                 'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
                 'name': 'Venom Drench',
                 'num': 599,
                 'onHit': 'function (target, source, move) {\n'
                          "\t\t\tif (target.status === 'psn' || target.status "
                          "=== 'tox') {\n"
                          '\t\t\t\treturn !!this.boost({ atk: -1, spa: -1, '
                          'spe: -1 }, target, source, move);\n'
                          '\t\t\t}\n'
                          '\t\t\treturn false;\n'
                          '\t\t}',
                 'pp': 20,
                 'priority': 0,
                 'secondary': None,
                 'target': 'allAdjacentFoes',
                 'type': 'Poison',
                 'zMove': {'boost': {'def': 1}}},
 'venoshock': {'accuracy': 100,
               'basePower': 65,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Venoshock',
               'num': 474,
               'onBasePower': 'function (basePower, pokemon, target) {\n'
                              "\t\t\tif (target.status === 'psn' || "
                              "target.status === 'tox') {\n"
                              '\t\t\t\treturn this.chainModify(2);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Poison'},
 'vinewhip': {'accuracy': 100,
              'basePower': 45,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Vine Whip',
              'num': 22,
              'pp': 25,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Grass'},
 'visegrip': {'accuracy': 100,
              'basePower': 55,
              'category': 'Physical',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'Vise Grip',
              'num': 11,
              'pp': 30,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal'},
 'vitalthrow': {'accuracy': True,
                'basePower': 70,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Vital Throw',
                'num': 233,
                'pp': 10,
                'priority': -1,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'voltswitch': {'accuracy': 100,
                'basePower': 70,
                'category': 'Special',
                'contestType': 'Cool',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Volt Switch',
                'num': 521,
                'pp': 20,
                'priority': 0,
                'secondary': None,
                'selfSwitch': True,
                'target': 'normal',
                'type': 'Electric'},
 'volttackle': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Volt Tackle',
                'num': 344,
                'pp': 15,
                'priority': 0,
                'recoil': [33, 100],
                'secondary': {'chance': 10, 'status': 'par'},
                'target': 'normal',
                'type': 'Electric'},
 'wakeupslap': {'accuracy': 100,
                'basePower': 70,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     "\t\t\tif (target.status === 'slp' || "
                                     "target.hasAbility('comatose'))\n"
                                     '\t\t\t\treturn move.basePower * 2;\n'
                                     '\t\t\treturn move.basePower;\n'
                                     '\t\t}',
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'isNonstandard': 'Past',
                'name': 'Wake-Up Slap',
                'num': 358,
                'onHit': 'function (target) {\n'
                         "\t\t\tif (target.status === 'slp')\n"
                         '\t\t\t\ttarget.cureStatus();\n'
                         '\t\t}',
                'pp': 10,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Fighting'},
 'waterfall': {'accuracy': 100,
               'basePower': 80,
               'category': 'Physical',
               'contestType': 'Tough',
               'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
               'name': 'Waterfall',
               'num': 127,
               'pp': 15,
               'priority': 0,
               'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
               'target': 'normal',
               'type': 'Water'},
 'watergun': {'accuracy': 100,
              'basePower': 40,
              'category': 'Special',
              'contestType': 'Cute',
              'flags': {'mirror': 1, 'protect': 1},
              'name': 'Water Gun',
              'num': 55,
              'pp': 25,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Water'},
 'waterpledge': {'accuracy': 100,
                 'basePower': 80,
                 'basePowerCallback': 'function (target, source, move) {\n'
                                      "\t\t\tif (['firepledge', "
                                      "'grasspledge'].includes(move.sourceEffect)) "
                                      '{\n'
                                      "\t\t\t\tthis.add('-combine');\n"
                                      '\t\t\t\treturn 150;\n'
                                      '\t\t\t}\n'
                                      '\t\t\treturn 80;\n'
                                      '\t\t}',
                 'category': 'Special',
                 'condition': {'duration': 4,
                               'onModifyMove': 'function (move, pokemon) {\n'
                                               '\t\t\t\tvar _a;\n'
                                               '\t\t\t\tif (move.secondaries '
                                               "&& move.id !== 'secretpower') "
                                               '{\n'
                                               "\t\t\t\t\tthis.debug('doubling "
                                               "secondary chance');\n"
                                               '\t\t\t\t\tfor (var _i = 0, _b '
                                               '= move.secondaries; _i < '
                                               '_b.length; _i++) {\n'
                                               '\t\t\t\t\t\tvar secondary = '
                                               '_b[_i];\n'
                                               '\t\t\t\t\t\tif '
                                               "(pokemon.hasAbility('serenegrace') "
                                               '&& secondary.volatileStatus '
                                               "=== 'flinch')\n"
                                               '\t\t\t\t\t\t\tcontinue;\n'
                                               '\t\t\t\t\t\tif '
                                               '(secondary.chance)\n'
                                               '\t\t\t\t\t\t\tsecondary.chance '
                                               '*= 2;\n'
                                               '\t\t\t\t\t}\n'
                                               '\t\t\t\t\tif ((_a = move.self) '
                                               '=== null || _a === void 0 ? '
                                               'void 0 : _a.chance)\n'
                                               '\t\t\t\t\t\tmove.self.chance '
                                               '*= 2;\n'
                                               '\t\t\t\t}\n'
                                               '\t\t\t}',
                               'onSideEnd': 'function (targetSide) {\n'
                                            "\t\t\t\tthis.add('-sideend', "
                                            "targetSide, 'Water Pledge');\n"
                                            '\t\t\t}',
                               'onSideResidualOrder': 26,
                               'onSideResidualSubOrder': 7,
                               'onSideStart': 'function (targetSide) {\n'
                                              "\t\t\t\tthis.add('-sidestart', "
                                              "targetSide, 'Water Pledge');\n"
                                              '\t\t\t}'},
                 'contestType': 'Beautiful',
                 'flags': {'mirror': 1, 'nonsky': 1, 'protect': 1},
                 'name': 'Water Pledge',
                 'num': 518,
                 'onModifyMove': 'function (move) {\n'
                                 '\t\t\tif (move.sourceEffect === '
                                 "'grasspledge') {\n"
                                 "\t\t\t\tmove.type = 'Grass';\n"
                                 '\t\t\t\tmove.forceSTAB = true;\n'
                                 "\t\t\t\tmove.sideCondition = 'grasspledge';\n"
                                 '\t\t\t}\n'
                                 '\t\t\tif (move.sourceEffect === '
                                 "'firepledge') {\n"
                                 "\t\t\t\tmove.type = 'Water';\n"
                                 '\t\t\t\tmove.forceSTAB = true;\n'
                                 '\t\t\t\tmove.self = { sideCondition: '
                                 "'waterpledge' };\n"
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'onPrepareHit': 'function (target, source, move) {\n'
                                 '\t\t\tfor (var _i = 0, _a = this.queue; _i < '
                                 '_a.length; _i++) {\n'
                                 '\t\t\t\tvar action = _a[_i];\n'
                                 "\t\t\t\tif (action.choice !== 'move')\n"
                                 '\t\t\t\t\tcontinue;\n'
                                 '\t\t\t\tvar otherMove = action.move;\n'
                                 '\t\t\t\tvar otherMoveUser = action.pokemon;\n'
                                 '\t\t\t\tif (!otherMove || !action.pokemon || '
                                 '!otherMoveUser.isActive ||\n'
                                 '\t\t\t\t\totherMoveUser.fainted || '
                                 'action.maxMove || action.zmove) {\n'
                                 '\t\t\t\t\tcontinue;\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t\tif (otherMoveUser.isAlly(source) && '
                                 "['firepledge', "
                                 "'grasspledge'].includes(otherMove.id)) {\n"
                                 '\t\t\t\t\t'
                                 'this.queue.prioritizeAction(action, move);\n'
                                 "\t\t\t\t\tthis.add('-waiting', source, "
                                 'otherMoveUser);\n'
                                 '\t\t\t\t\treturn null;\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Water'},
 'waterpulse': {'accuracy': 100,
                'basePower': 60,
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'distance': 1, 'mirror': 1, 'protect': 1, 'pulse': 1},
                'name': 'Water Pulse',
                'num': 352,
                'pp': 20,
                'priority': 0,
                'secondary': {'chance': 20, 'volatileStatus': 'confusion'},
                'target': 'any',
                'type': 'Water'},
 'watershuriken': {'accuracy': 100,
                   'basePower': 15,
                   'basePowerCallback': 'function (pokemon, target, move) {\n'
                                        '\t\t\tif (pokemon.species.name === '
                                        "'Greninja-Ash' && "
                                        "pokemon.hasAbility('battlebond')) {\n"
                                        '\t\t\t\treturn move.basePower + 5;\n'
                                        '\t\t\t}\n'
                                        '\t\t\treturn move.basePower;\n'
                                        '\t\t}',
                   'category': 'Special',
                   'contestType': 'Cool',
                   'flags': {'mirror': 1, 'protect': 1},
                   'multihit': [2, 5],
                   'name': 'Water Shuriken',
                   'num': 594,
                   'pp': 20,
                   'priority': 1,
                   'secondary': None,
                   'target': 'normal',
                   'type': 'Water'},
 'watersport': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 5,
                              'onBasePower': 'function (basePower, attacker, '
                                             'defender, move) {\n'
                                             '\t\t\t\tif (move.type === '
                                             "'Fire') {\n"
                                             "\t\t\t\t\tthis.debug('water "
                                             "sport weaken');\n"
                                             '\t\t\t\t\treturn '
                                             'this.chainModify([1352, 4096]);\n'
                                             '\t\t\t\t}\n'
                                             '\t\t\t}',
                              'onBasePowerPriority': 1,
                              'onFieldEnd': 'function () {\n'
                                            "\t\t\t\tthis.add('-fieldend', "
                                            "'move: Water Sport');\n"
                                            '\t\t\t}',
                              'onFieldResidualOrder': 27,
                              'onFieldResidualSubOrder': 3,
                              'onFieldStart': 'function (field, source) {\n'
                                              "\t\t\t\tthis.add('-fieldstart', "
                                              "'move: Water Sport', '[of] ' + "
                                              'source);\n'
                                              '\t\t\t}'},
                'contestType': 'Cute',
                'flags': {'nonsky': 1},
                'isNonstandard': 'Past',
                'name': 'Water Sport',
                'num': 346,
                'pp': 15,
                'priority': 0,
                'pseudoWeather': 'watersport',
                'secondary': None,
                'target': 'all',
                'type': 'Water',
                'zMove': {'boost': {'spd': 1}}},
 'waterspout': {'accuracy': 100,
                'basePower': 150,
                'basePowerCallback': 'function (pokemon, target, move) {\n'
                                     '\t\t\treturn move.basePower * pokemon.hp '
                                     '/ pokemon.maxhp;\n'
                                     '\t\t}',
                'category': 'Special',
                'contestType': 'Beautiful',
                'flags': {'mirror': 1, 'protect': 1},
                'name': 'Water Spout',
                'num': 323,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'allAdjacentFoes',
                'type': 'Water'},
 'weatherball': {'accuracy': 100,
                 'basePower': 50,
                 'category': 'Special',
                 'contestType': 'Beautiful',
                 'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
                 'maxMove': {'basePower': 130},
                 'name': 'Weather Ball',
                 'num': 311,
                 'onModifyMove': 'function (move, pokemon) {\n'
                                 '\t\t\tswitch (pokemon.effectiveWeather()) {\n'
                                 "\t\t\t\tcase 'sunnyday':\n"
                                 "\t\t\t\tcase 'desolateland':\n"
                                 '\t\t\t\t\tmove.basePower *= 2;\n'
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'raindance':\n"
                                 "\t\t\t\tcase 'primordialsea':\n"
                                 '\t\t\t\t\tmove.basePower *= 2;\n'
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'sandstorm':\n"
                                 '\t\t\t\t\tmove.basePower *= 2;\n'
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'hail':\n"
                                 '\t\t\t\t\tmove.basePower *= 2;\n'
                                 '\t\t\t\t\tbreak;\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'onModifyType': 'function (move, pokemon) {\n'
                                 '\t\t\tswitch (pokemon.effectiveWeather()) {\n'
                                 "\t\t\t\tcase 'sunnyday':\n"
                                 "\t\t\t\tcase 'desolateland':\n"
                                 "\t\t\t\t\tmove.type = 'Fire';\n"
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'raindance':\n"
                                 "\t\t\t\tcase 'primordialsea':\n"
                                 "\t\t\t\t\tmove.type = 'Water';\n"
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'sandstorm':\n"
                                 "\t\t\t\t\tmove.type = 'Rock';\n"
                                 '\t\t\t\t\tbreak;\n'
                                 "\t\t\t\tcase 'hail':\n"
                                 "\t\t\t\t\tmove.type = 'Ice';\n"
                                 '\t\t\t\t\tbreak;\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                 'pp': 10,
                 'priority': 0,
                 'secondary': None,
                 'target': 'normal',
                 'type': 'Normal',
                 'zMove': {'basePower': 160}},
 'whirlpool': {'accuracy': 85,
               'basePower': 35,
               'category': 'Special',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1},
               'name': 'Whirlpool',
               'num': 250,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Water',
               'volatileStatus': 'partiallytrapped'},
 'whirlwind': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'authentic': 1,
                         'mirror': 1,
                         'mystery': 1,
                         'reflectable': 1},
               'forceSwitch': True,
               'name': 'Whirlwind',
               'num': 18,
               'pp': 20,
               'priority': -6,
               'secondary': None,
               'target': 'normal',
               'type': 'Normal',
               'zMove': {'boost': {'spd': 1}}},
 'wickedblow': {'accuracy': 100,
                'basePower': 80,
                'category': 'Physical',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1, 'punch': 1},
                'name': 'Wicked Blow',
                'num': 817,
                'pp': 5,
                'priority': 0,
                'secondary': None,
                'target': 'normal',
                'type': 'Dark',
                'willCrit': True},
 'wideguard': {'accuracy': True,
               'basePower': 0,
               'category': 'Status',
               'condition': {'duration': 1,
                             'onSideStart': 'function (target, source) {\n'
                                            "\t\t\t\tthis.add('-singleturn', "
                                            "source, 'Wide Guard');\n"
                                            '\t\t\t}',
                             'onTryHit': 'function (target, source, move) {\n'
                                         '\t\t\t\t// Wide Guard blocks all '
                                         'spread moves\n'
                                         '\t\t\t\tif ((move === null || move '
                                         '=== void 0 ? void 0 : move.target) '
                                         "!== 'allAdjacent' && move.target !== "
                                         "'allAdjacentFoes') {\n"
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t\tif (move.isZ || move.isMax) '
                                         '{\n'
                                         "\t\t\t\t\tif (['gmaxoneblow', "
                                         "'gmaxrapidflow'].includes(move.id))\n"
                                         '\t\t\t\t\t\treturn;\n'
                                         '\t\t\t\t\t'
                                         'target.getMoveHitData(move).zBrokeProtect '
                                         '= true;\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\t}\n'
                                         "\t\t\t\tthis.add('-activate', "
                                         "target, 'move: Wide Guard');\n"
                                         '\t\t\t\tvar lockedmove = '
                                         "source.getVolatile('lockedmove');\n"
                                         '\t\t\t\tif (lockedmove) {\n'
                                         '\t\t\t\t\t// Outrage counter is '
                                         'reset\n'
                                         '\t\t\t\t\tif '
                                         "(source.volatiles['lockedmove'].duration "
                                         '=== 2) {\n'
                                         '\t\t\t\t\t\tdelete '
                                         "source.volatiles['lockedmove'];\n"
                                         '\t\t\t\t\t}\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t\treturn this.NOT_FAIL;\n'
                                         '\t\t\t}',
                             'onTryHitPriority': 4},
               'contestType': 'Tough',
               'flags': {'snatch': 1},
               'name': 'Wide Guard',
               'num': 469,
               'onHitSide': 'function (side, source) {\n'
                            "\t\t\tsource.addVolatile('stall');\n"
                            '\t\t}',
               'onTry': 'function () {\n'
                        '\t\t\treturn !!this.queue.willAct();\n'
                        '\t\t}',
               'pp': 10,
               'priority': 3,
               'secondary': None,
               'sideCondition': 'wideguard',
               'target': 'allySide',
               'type': 'Rock',
               'zMove': {'boost': {'def': 1}}},
 'wildcharge': {'accuracy': 100,
                'basePower': 90,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Wild Charge',
                'num': 528,
                'pp': 15,
                'priority': 0,
                'recoil': [1, 4],
                'secondary': None,
                'target': 'normal',
                'type': 'Electric'},
 'willowisp': {'accuracy': 85,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Beautiful',
               'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
               'name': 'Will-O-Wisp',
               'num': 261,
               'pp': 15,
               'priority': 0,
               'secondary': None,
               'status': 'brn',
               'target': 'normal',
               'type': 'Fire',
               'zMove': {'boost': {'atk': 1}}},
 'wingattack': {'accuracy': 100,
                'basePower': 60,
                'category': 'Physical',
                'contestType': 'Cool',
                'flags': {'contact': 1,
                          'distance': 1,
                          'mirror': 1,
                          'protect': 1},
                'name': 'Wing Attack',
                'num': 17,
                'pp': 35,
                'priority': 0,
                'secondary': None,
                'target': 'any',
                'type': 'Flying'},
 'wish': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'condition': {'duration': 2,
                        'onEnd': 'function (target) {\n'
                                 '\t\t\t\tif (target && !target.fainted) {\n'
                                 '\t\t\t\t\tvar damage = '
                                 'this.heal(this.effectState.hp, target, '
                                 'target);\n'
                                 '\t\t\t\t\tif (damage) {\n'
                                 "\t\t\t\t\t\tthis.add('-heal', target, "
                                 "target.getHealth, '[from] move: Wish', "
                                 "'[wisher] ' + "
                                 'this.effectState.source.name);\n'
                                 '\t\t\t\t\t}\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}',
                        'onResidualOrder': 4,
                        'onStart': 'function (pokemon, source) {\n'
                                   '\t\t\t\tthis.effectState.hp = source.maxhp '
                                   '/ 2;\n'
                                   '\t\t\t}'},
          'contestType': 'Cute',
          'flags': {'heal': 1, 'snatch': 1},
          'name': 'Wish',
          'num': 273,
          'pp': 10,
          'priority': 0,
          'secondary': None,
          'slotCondition': 'Wish',
          'target': 'self',
          'type': 'Normal',
          'zMove': {'boost': {'spd': 1}}},
 'withdraw': {'accuracy': True,
              'basePower': 0,
              'boosts': {'def': 1},
              'category': 'Status',
              'contestType': 'Cute',
              'flags': {'snatch': 1},
              'name': 'Withdraw',
              'num': 110,
              'pp': 40,
              'priority': 0,
              'secondary': None,
              'target': 'self',
              'type': 'Water',
              'zMove': {'boost': {'def': 1}}},
 'wonderroom': {'accuracy': True,
                'basePower': 0,
                'category': 'Status',
                'condition': {'duration': 5,
                              'durationCallback': 'function (source, effect) '
                                                  '{\n'
                                                  '\t\t\t\tif (source === null '
                                                  '|| source === void 0 ? void '
                                                  '0 : '
                                                  "source.hasAbility('persistent')) "
                                                  '{\n'
                                                  '\t\t\t\t\t'
                                                  "this.add('-activate', "
                                                  "source, 'ability: "
                                                  "Persistent', effect);\n"
                                                  '\t\t\t\t\treturn 7;\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t\treturn 5;\n'
                                                  '\t\t\t}',
                              'onFieldEnd': 'function () {\n'
                                            "\t\t\t\tthis.add('-fieldend', "
                                            "'move: Wonder Room');\n"
                                            '\t\t\t}',
                              'onFieldResidualOrder': 27,
                              'onFieldResidualSubOrder': 5,
                              'onFieldRestart': 'function (target, source) {\n'
                                                '\t\t\t\t'
                                                "this.field.removePseudoWeather('wonderroom');\n"
                                                '\t\t\t}',
                              'onFieldStart': 'function (field, source) {\n'
                                              "\t\t\t\tthis.add('-fieldstart', "
                                              "'move: Wonder Room', '[of] ' + "
                                              'source);\n'
                                              '\t\t\t}'},
                'contestType': 'Clever',
                'flags': {'mirror': 1},
                'name': 'Wonder Room',
                'num': 472,
                'pp': 10,
                'priority': 0,
                'pseudoWeather': 'wonderroom',
                'secondary': None,
                'target': 'all',
                'type': 'Psychic',
                'zMove': {'boost': {'spd': 1}}},
 'woodhammer': {'accuracy': 100,
                'basePower': 120,
                'category': 'Physical',
                'contestType': 'Tough',
                'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                'name': 'Wood Hammer',
                'num': 452,
                'pp': 15,
                'priority': 0,
                'recoil': [33, 100],
                'secondary': None,
                'target': 'normal',
                'type': 'Grass'},
 'workup': {'accuracy': True,
            'basePower': 0,
            'boosts': {'atk': 1, 'spa': 1},
            'category': 'Status',
            'contestType': 'Tough',
            'flags': {'snatch': 1},
            'name': 'Work Up',
            'num': 526,
            'pp': 30,
            'priority': 0,
            'secondary': None,
            'target': 'self',
            'type': 'Normal',
            'zMove': {'boost': {'atk': 1}}},
 'worryseed': {'accuracy': 100,
               'basePower': 0,
               'category': 'Status',
               'contestType': 'Clever',
               'flags': {'mirror': 1,
                         'mystery': 1,
                         'protect': 1,
                         'reflectable': 1},
               'name': 'Worry Seed',
               'num': 388,
               'onHit': 'function (pokemon) {\n'
                        '\t\t\tvar oldAbility = '
                        "pokemon.setAbility('insomnia');\n"
                        '\t\t\tif (oldAbility) {\n'
                        "\t\t\t\tthis.add('-ability', pokemon, 'Insomnia', "
                        "'[from] move: Worry Seed');\n"
                        "\t\t\t\tif (pokemon.status === 'slp') {\n"
                        '\t\t\t\t\tpokemon.cureStatus();\n'
                        '\t\t\t\t}\n'
                        '\t\t\t\treturn;\n'
                        '\t\t\t}\n'
                        '\t\t\treturn false;\n'
                        '\t\t}',
               'onTryHit': 'function (target) {\n'
                           '\t\t\tif (target.getAbility().isPermanent) {\n'
                           '\t\t\t\treturn false;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'onTryImmunity': 'function (target) {\n'
                                '\t\t\t// Truant and Insomnia have special '
                                'treatment; they fail before\n'
                                '\t\t\t// checking accuracy and will double '
                                "Stomping Tantrum's BP\n"
                                "\t\t\tif (target.ability === 'truant' || "
                                "target.ability === 'insomnia') {\n"
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t}',
               'pp': 10,
               'priority': 0,
               'secondary': None,
               'target': 'normal',
               'type': 'Grass',
               'zMove': {'boost': {'spe': 1}}},
 'wrap': {'accuracy': 90,
          'basePower': 15,
          'category': 'Physical',
          'contestType': 'Tough',
          'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
          'name': 'Wrap',
          'num': 35,
          'pp': 20,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Normal',
          'volatileStatus': 'partiallytrapped'},
 'wringout': {'accuracy': 100,
              'basePower': 0,
              'basePowerCallback': 'function (pokemon, target) {\n'
                                   '\t\t\treturn Math.floor(Math.floor((120 * '
                                   '(100 * Math.floor(target.hp * 4096 / '
                                   'target.maxhp)) + 2048 - 1) / 4096) / 100) '
                                   '|| 1;\n'
                                   '\t\t}',
              'category': 'Special',
              'contestType': 'Tough',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'isNonstandard': 'Past',
              'maxMove': {'basePower': 140},
              'name': 'Wring Out',
              'num': 378,
              'pp': 5,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Normal',
              'zMove': {'basePower': 190}},
 'xscissor': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
              'name': 'X-Scissor',
              'num': 404,
              'pp': 15,
              'priority': 0,
              'secondary': None,
              'target': 'normal',
              'type': 'Bug'},
 'yawn': {'accuracy': True,
          'basePower': 0,
          'category': 'Status',
          'condition': {'duration': 2,
                        'noCopy': True,
                        'onEnd': 'function (target) {\n'
                                 "\t\t\t\tthis.add('-end', target, 'move: "
                                 "Yawn', '[silent]');\n"
                                 "\t\t\t\ttarget.trySetStatus('slp', "
                                 'this.effectState.source);\n'
                                 '\t\t\t}',
                        'onResidualOrder': 23,
                        'onStart': 'function (target, source) {\n'
                                   "\t\t\t\tthis.add('-start', target, 'move: "
                                   "Yawn', '[of] ' + source);\n"
                                   '\t\t\t}'},
          'contestType': 'Cute',
          'flags': {'mirror': 1, 'protect': 1, 'reflectable': 1},
          'name': 'Yawn',
          'num': 281,
          'onTryHit': 'function (target) {\n'
                      '\t\t\tif (target.status || '
                      "!target.runStatusImmunity('slp')) {\n"
                      '\t\t\t\treturn false;\n'
                      '\t\t\t}\n'
                      '\t\t}',
          'pp': 10,
          'priority': 0,
          'secondary': None,
          'target': 'normal',
          'type': 'Normal',
          'volatileStatus': 'yawn',
          'zMove': {'boost': {'spe': 1}}},
 'zapcannon': {'accuracy': 50,
               'basePower': 120,
               'category': 'Special',
               'contestType': 'Cool',
               'flags': {'bullet': 1, 'mirror': 1, 'protect': 1},
               'name': 'Zap Cannon',
               'num': 192,
               'pp': 5,
               'priority': 0,
               'secondary': {'chance': 100, 'status': 'par'},
               'target': 'normal',
               'type': 'Electric'},
 'zenheadbutt': {'accuracy': 90,
                 'basePower': 80,
                 'category': 'Physical',
                 'contestType': 'Clever',
                 'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
                 'name': 'Zen Headbutt',
                 'num': 428,
                 'pp': 15,
                 'priority': 0,
                 'secondary': {'chance': 20, 'volatileStatus': 'flinch'},
                 'target': 'normal',
                 'type': 'Psychic'},
 'zingzap': {'accuracy': 100,
             'basePower': 80,
             'category': 'Physical',
             'contestType': 'Cool',
             'flags': {'contact': 1, 'mirror': 1, 'protect': 1},
             'name': 'Zing Zap',
             'num': 716,
             'pp': 10,
             'priority': 0,
             'secondary': {'chance': 30, 'volatileStatus': 'flinch'},
             'target': 'normal',
             'type': 'Electric'},
 'zippyzap': {'accuracy': 100,
              'basePower': 80,
              'category': 'Physical',
              'contestType': 'Cool',
              'flags': {'contact': 1, 'protect': 1},
              'isNonstandard': 'LGPE',
              'name': 'Zippy Zap',
              'num': 729,
              'pp': 10,
              'priority': 2,
              'secondary': {'chance': 100, 'self': {'boosts': {'evasion': 1}}},
              'target': 'normal',
              'type': 'Electric'}}
