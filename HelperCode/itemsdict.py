BattleItems = {'abomasite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Abomasnow'],
               'megaEvolves': 'Abomasnow',
               'megaStone': 'Abomasnow-Mega',
               'name': 'Abomasite',
               'num': 674,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 575},
 'absolite': {'gen': 6,
              'isNonstandard': 'Past',
              'itemUser': ['Absol'],
              'megaEvolves': 'Absol',
              'megaStone': 'Absol-Mega',
              'name': 'Absolite',
              'num': 677,
              'onTakeItem': 'function (item, source) {\n'
                            '\t\t\tif (item.megaEvolves === '
                            'source.baseSpecies.baseSpecies)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 576},
 'absorbbulb': {'boosts': {'spa': 1},
                'fling': {'basePower': 30},
                'gen': 5,
                'name': 'Absorb Bulb',
                'num': 545,
                'onDamagingHit': 'function (damage, target, source, move) {\n'
                                 "\t\t\tif (move.type === 'Water') {\n"
                                 '\t\t\t\ttarget.useItem();\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                'spritenum': 2},
 'adamantorb': {'fling': {'basePower': 60},
                'gen': 4,
                'itemUser': ['Dialga'],
                'name': 'Adamant Orb',
                'num': 135,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               '\t\t\tif (move && user.baseSpecies.name === '
                               "'Dialga' && (move.type === 'Steel' || "
                               "move.type === 'Dragon')) {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'spritenum': 4},
 'adrenalineorb': {'boosts': {'spe': 1},
                   'fling': {'basePower': 30},
                   'gen': 7,
                   'name': 'Adrenaline Orb',
                   'num': 846,
                   'onAfterBoost': 'function (boost, target, source, effect) '
                                   '{\n'
                                   '\t\t\tvar noAtkChange = boost.atk < 0 && '
                                   "target.boosts['atk'] === -6 && "
                                   'target.itemState.lastAtk === -6;\n'
                                   '\t\t\tvar noContraryAtkChange = boost.atk '
                                   "> 0 && target.boosts['atk'] === 6 && "
                                   'target.itemState.lastAtk === 6;\n'
                                   "\t\t\tif (target.boosts['spe'] === 6 || "
                                   'noAtkChange || noContraryAtkChange) {\n'
                                   '\t\t\t\treturn;\n'
                                   '\t\t\t}\n'
                                   "\t\t\tif (effect.id === 'intimidate') {\n"
                                   '\t\t\t\ttarget.useItem();\n'
                                   '\t\t\t}\n'
                                   '\t\t}',
                   'onBoost': 'function (boost, target) {\n'
                              '\t\t\ttarget.itemState.lastAtk = '
                              "target.boosts['atk'];\n"
                              '\t\t}',
                   'onBoostPriority': 1,
                   'spritenum': 660},
 'aerodactylite': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Aerodactyl'],
                   'megaEvolves': 'Aerodactyl',
                   'megaStone': 'Aerodactyl-Mega',
                   'name': 'Aerodactylite',
                   'num': 672,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 577},
 'aggronite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Aggron'],
               'megaEvolves': 'Aggron',
               'megaStone': 'Aggron-Mega',
               'name': 'Aggronite',
               'num': 667,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 578},
 'aguavberry': {'gen': 3,
                'isBerry': True,
                'name': 'Aguav Berry',
                'naturalGift': {'basePower': 80, 'type': 'Dragon'},
                'num': 162,
                'onEat': 'function (pokemon) {\n'
                         '\t\t\tthis.heal(pokemon.baseMaxhp * 0.33);\n'
                         "\t\t\tif (pokemon.getNature().minus === 'spd') {\n"
                         "\t\t\t\tpokemon.addVolatile('confusion');\n"
                         '\t\t\t}\n'
                         '\t\t}',
                'onTryEatItem': 'function (item, pokemon) {\n'
                                "\t\t\tif (!this.runEvent('TryHeal', "
                                'pokemon))\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                            '(pokemon.hp <= pokemon.maxhp / 2 && '
                            "pokemon.hasAbility('gluttony'))) {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 5},
 'airballoon': {'fling': {'basePower': 10},
                'gen': 5,
                'name': 'Air Balloon',
                'num': 541,
                'onAfterSubDamage': 'function (damage, target, source, effect) '
                                    '{\n'
                                    "\t\t\tthis.debug('effect: ' + "
                                    'effect.id);\n'
                                    "\t\t\tif (effect.effectType === 'Move') "
                                    '{\n'
                                    "\t\t\t\tthis.add('-enditem', target, 'Air "
                                    "Balloon');\n"
                                    "\t\t\t\ttarget.item = '';\n"
                                    "\t\t\t\ttarget.itemState = { id: '', "
                                    'target: target };\n'
                                    "\t\t\t\tthis.runEvent('AfterUseItem', "
                                    'target, null, null, '
                                    "this.dex.items.get('airballoon'));\n"
                                    '\t\t\t}\n'
                                    '\t\t}',
                'onDamagingHit': 'function (damage, target, source, move) {\n'
                                 "\t\t\tthis.add('-enditem', target, 'Air "
                                 "Balloon');\n"
                                 "\t\t\ttarget.item = '';\n"
                                 "\t\t\ttarget.itemState = { id: '', target: "
                                 'target };\n'
                                 "\t\t\tthis.runEvent('AfterUseItem', target, "
                                 'null, null, '
                                 "this.dex.items.get('airballoon'));\n"
                                 '\t\t}',
                'onStart': 'function (target) {\n'
                           '\t\t\tif (!target.ignoringItem() && '
                           "!this.field.getPseudoWeather('gravity')) {\n"
                           "\t\t\t\tthis.add('-item', target, 'Air Balloon');\n"
                           '\t\t\t}\n'
                           '\t\t}',
                'spritenum': 6},
 'alakazite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Alakazam'],
               'megaEvolves': 'Alakazam',
               'megaStone': 'Alakazam-Mega',
               'name': 'Alakazite',
               'num': 679,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 579},
 'aloraichiumz': {'gen': 7,
                  'isNonstandard': 'Past',
                  'itemUser': ['Raichu-Alola'],
                  'name': 'Aloraichium Z',
                  'num': 803,
                  'onTakeItem': False,
                  'spritenum': 655,
                  'zMove': 'Stoked Sparksurfer',
                  'zMoveFrom': 'Thunderbolt'},
 'altarianite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Altaria'],
                 'megaEvolves': 'Altaria',
                 'megaStone': 'Altaria-Mega',
                 'name': 'Altarianite',
                 'num': 755,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 615},
 'ampharosite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Ampharos'],
                 'megaEvolves': 'Ampharos',
                 'megaStone': 'Ampharos-Mega',
                 'name': 'Ampharosite',
                 'num': 658,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 580},
 'apicotberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Apicot Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Ground'},
                 'num': 205,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.boost({ spd: 1 });\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 10},
 'armorfossil': {'fling': {'basePower': 100},
                 'gen': 4,
                 'isNonstandard': 'Past',
                 'name': 'Armor Fossil',
                 'num': 104,
                 'spritenum': 12},
 'aspearberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Aspear Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Ice'},
                 'num': 153,
                 'onEat': 'function (pokemon) {\n'
                          "\t\t\tif (pokemon.status === 'frz') {\n"
                          '\t\t\t\tpokemon.cureStatus();\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             "\t\t\tif (pokemon.status === 'frz') {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 13},
 'assaultvest': {'fling': {'basePower': 80},
                 'gen': 6,
                 'name': 'Assault Vest',
                 'num': 640,
                 'onDisableMove': 'function (pokemon) {\n'
                                  '\t\t\tfor (var _i = 0, _a = '
                                  'pokemon.moveSlots; _i < _a.length; _i++) {\n'
                                  '\t\t\t\tvar moveSlot = _a[_i];\n'
                                  '\t\t\t\tif '
                                  '(this.dex.moves.get(moveSlot.move).category '
                                  "=== 'Status') {\n"
                                  '\t\t\t\t\t'
                                  'pokemon.disableMove(moveSlot.id);\n'
                                  '\t\t\t\t}\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                 'onModifySpD': 'function (spd) {\n'
                                '\t\t\treturn this.chainModify(1.5);\n'
                                '\t\t}',
                 'onModifySpDPriority': 1,
                 'spritenum': 581},
 'audinite': {'gen': 6,
              'isNonstandard': 'Past',
              'itemUser': ['Audino'],
              'megaEvolves': 'Audino',
              'megaStone': 'Audino-Mega',
              'name': 'Audinite',
              'num': 757,
              'onTakeItem': 'function (item, source) {\n'
                            '\t\t\tif (item.megaEvolves === '
                            'source.baseSpecies.baseSpecies)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 617},
 'babiriberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Babiri Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Steel'},
                 'num': 199,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Steel' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 17},
 'banettite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Banette'],
               'megaEvolves': 'Banette',
               'megaStone': 'Banette-Mega',
               'name': 'Banettite',
               'num': 668,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 582},
 'beastball': {'gen': 7,
               'isPokeball': True,
               'name': 'Beast Ball',
               'num': 851,
               'spritenum': 661},
 'beedrillite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Beedrill'],
                 'megaEvolves': 'Beedrill',
                 'megaStone': 'Beedrill-Mega',
                 'name': 'Beedrillite',
                 'num': 770,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 628},
 'belueberry': {'gen': 3,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Belue Berry',
                'naturalGift': {'basePower': 100, 'type': 'Electric'},
                'num': 183,
                'onEat': False,
                'spritenum': 21},
 'berry': {'gen': 2,
           'isBerry': True,
           'isNonstandard': 'Past',
           'name': 'Berry',
           'naturalGift': {'basePower': 80, 'type': 'Poison'},
           'num': 155,
           'onEat': 'function (pokemon) {\n\t\t\tthis.heal(10);\n\t\t}',
           'onResidual': 'function (pokemon) {\n'
                         '\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n'
                         '\t\t\t\tpokemon.eatItem();\n'
                         '\t\t\t}\n'
                         '\t\t}',
           'onResidualOrder': 5,
           'onTryEatItem': 'function (item, pokemon) {\n'
                           "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                           '\t\t\t\treturn false;\n'
                           '\t\t}',
           'spritenum': 319},
 'berryjuice': {'fling': {'basePower': 30},
                'gen': 2,
                'name': 'Berry Juice',
                'num': 43,
                'onUpdate': 'function (pokemon) {\n'
                            '\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n'
                            "\t\t\t\tif (this.runEvent('TryHeal', pokemon) && "
                            'pokemon.useItem()) {\n'
                            '\t\t\t\t\tthis.heal(20);\n'
                            '\t\t\t\t}\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 22},
 'berrysweet': {'fling': {'basePower': 10},
                'gen': 8,
                'name': 'Berry Sweet',
                'num': 1111,
                'spritenum': 706},
 'berserkgene': {'gen': 2,
                 'isNonstandard': 'Past',
                 'name': 'Berserk Gene',
                 'num': 0,
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tthis.boost({ atk: 2 });\n'
                             "\t\t\tpokemon.addVolatile('confusion');\n"
                             "\t\t\tpokemon.setItem('');\n"
                             '\t\t}',
                 'spritenum': 388},
 'bigroot': {'fling': {'basePower': 10},
             'gen': 4,
             'name': 'Big Root',
             'num': 296,
             'onTryHeal': 'function (damage, target, source, effect) {\n'
                          "\t\t\tvar heals = ['drain', 'leechseed', 'ingrain', "
                          "'aquaring', 'strengthsap'];\n"
                          '\t\t\tif (heals.includes(effect.id)) {\n'
                          '\t\t\t\treturn this.chainModify([5324, 4096]);\n'
                          '\t\t\t}\n'
                          '\t\t}',
             'onTryHealPriority': 1,
             'spritenum': 29},
 'bindingband': {'fling': {'basePower': 30},
                 'gen': 5,
                 'name': 'Binding Band',
                 'num': 544,
                 'spritenum': 31},
 'bitterberry': {'gen': 2,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Bitter Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Ground'},
                 'num': 156,
                 'onEat': 'function (pokemon) {\n'
                          "\t\t\tpokemon.removeVolatile('confusion');\n"
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             "\t\t\tif (pokemon.volatiles['confusion']) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 334},
 'blackbelt': {'fling': {'basePower': 30},
               'gen': 2,
               'name': 'Black Belt',
               'num': 241,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move && move.type === 'Fighting') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'spritenum': 32},
 'blackglasses': {'fling': {'basePower': 30},
                  'gen': 2,
                  'name': 'Black Glasses',
                  'num': 240,
                  'onBasePower': 'function (basePower, user, target, move) {\n'
                                 "\t\t\tif (move && move.type === 'Dark') {\n"
                                 '\t\t\t\treturn this.chainModify([4915, '
                                 '4096]);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onBasePowerPriority': 15,
                  'spritenum': 35},
 'blacksludge': {'fling': {'basePower': 30},
                 'gen': 4,
                 'name': 'Black Sludge',
                 'num': 281,
                 'onResidual': 'function (pokemon) {\n'
                               "\t\t\tif (pokemon.hasType('Poison')) {\n"
                               '\t\t\t\tthis.heal(pokemon.baseMaxhp / 16);\n'
                               '\t\t\t}\n'
                               '\t\t\telse {\n'
                               '\t\t\t\tthis.damage(pokemon.baseMaxhp / 8);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                 'onResidualOrder': 5,
                 'onResidualSubOrder': 4,
                 'spritenum': 34},
 'blastoisinite': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Blastoise'],
                   'megaEvolves': 'Blastoise',
                   'megaStone': 'Blastoise-Mega',
                   'name': 'Blastoisinite',
                   'num': 661,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 583},
 'blazikenite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Blaziken'],
                 'megaEvolves': 'Blaziken',
                 'megaStone': 'Blaziken-Mega',
                 'name': 'Blazikenite',
                 'num': 664,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 584},
 'blueorb': {'gen': 6,
             'isNonstandard': 'Past',
             'itemUser': ['Kyogre'],
             'name': 'Blue Orb',
             'num': 535,
             'onPrimal': 'function (pokemon) {\n'
                         "\t\t\tpokemon.formeChange('Kyogre-Primal', "
                         'this.effect, true);\n'
                         '\t\t}',
             'onSwitchIn': 'function (pokemon) {\n'
                           '\t\t\tif (pokemon.isActive && '
                           "pokemon.baseSpecies.name === 'Kyogre') {\n"
                           '\t\t\t\tthis.queue.insertChoice({ choice: '
                           "'runPrimal', pokemon: pokemon });\n"
                           '\t\t\t}\n'
                           '\t\t}',
             'onTakeItem': 'function (item, source) {\n'
                           '\t\t\tif (source.baseSpecies.baseSpecies === '
                           "'Kyogre')\n"
                           '\t\t\t\treturn false;\n'
                           '\t\t\treturn true;\n'
                           '\t\t}',
             'spritenum': 41},
 'blukberry': {'gen': 3,
               'isBerry': True,
               'name': 'Bluk Berry',
               'naturalGift': {'basePower': 90, 'type': 'Fire'},
               'num': 165,
               'onEat': False,
               'spritenum': 44},
 'blunderpolicy': {'fling': {'basePower': 80},
                   'gen': 8,
                   'name': 'Blunder Policy',
                   'num': 1121,
                   'spritenum': 716},
 'bottlecap': {'fling': {'basePower': 30},
               'gen': 7,
               'name': 'Bottle Cap',
               'num': 795,
               'spritenum': 696},
 'brightpowder': {'fling': {'basePower': 10},
                  'gen': 2,
                  'name': 'Bright Powder',
                  'num': 213,
                  'onModifyAccuracy': 'function (accuracy) {\n'
                                      '\t\t\tif (typeof accuracy !== '
                                      "'number')\n"
                                      '\t\t\t\treturn;\n'
                                      "\t\t\tthis.debug('brightpowder - "
                                      "decreasing accuracy');\n"
                                      '\t\t\treturn this.chainModify([3686, '
                                      '4096]);\n'
                                      '\t\t}',
                  'onModifyAccuracyPriority': -2,
                  'spritenum': 51},
 'buggem': {'gen': 5,
            'isGem': True,
            'isNonstandard': 'Past',
            'name': 'Bug Gem',
            'num': 558,
            'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                     '\t\t\tif (target === source || '
                                     "move.category === 'Status')\n"
                                     '\t\t\t\treturn;\n'
                                     "\t\t\tif (move.type === 'Bug' && "
                                     'source.useItem()) {\n'
                                     "\t\t\t\tsource.addVolatile('gem');\n"
                                     '\t\t\t}\n'
                                     '\t\t}',
            'spritenum': 53},
 'buginiumz': {'forcedForme': 'Arceus-Bug',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Buginium Z',
               'num': 787,
               'onPlate': 'Bug',
               'onTakeItem': False,
               'spritenum': 642,
               'zMove': True,
               'zMoveType': 'Bug'},
 'bugmemory': {'forcedForme': 'Silvally-Bug',
               'gen': 7,
               'itemUser': ['Silvally-Bug'],
               'name': 'Bug Memory',
               'num': 909,
               'onMemory': 'Bug',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '773) || pokemon.baseSpecies.num === 773) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 673},
 'burndrive': {'forcedForme': 'Genesect-Burn',
               'gen': 5,
               'itemUser': ['Genesect-Burn'],
               'name': 'Burn Drive',
               'num': 118,
               'onDrive': 'Fire',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '649) || pokemon.baseSpecies.num === 649) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 54},
 'burntberry': {'gen': 2,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Burnt Berry',
                'naturalGift': {'basePower': 80, 'type': 'Ice'},
                'num': 153,
                'onEat': 'function (pokemon) {\n'
                         "\t\t\tif (pokemon.status === 'frz') {\n"
                         '\t\t\t\tpokemon.cureStatus();\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.status === 'frz') {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 13},
 'cameruptite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Camerupt'],
                 'megaEvolves': 'Camerupt',
                 'megaStone': 'Camerupt-Mega',
                 'name': 'Cameruptite',
                 'num': 767,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 625},
 'cellbattery': {'boosts': {'atk': 1},
                 'fling': {'basePower': 30},
                 'gen': 5,
                 'name': 'Cell Battery',
                 'num': 546,
                 'onDamagingHit': 'function (damage, target, source, move) {\n'
                                  "\t\t\tif (move.type === 'Electric') {\n"
                                  '\t\t\t\ttarget.useItem();\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                 'spritenum': 60},
 'charcoal': {'fling': {'basePower': 30},
              'gen': 2,
              'name': 'Charcoal',
              'num': 249,
              'onBasePower': 'function (basePower, user, target, move) {\n'
                             "\t\t\tif (move && move.type === 'Fire') {\n"
                             '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onBasePowerPriority': 15,
              'spritenum': 61},
 'charizarditex': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Charizard'],
                   'megaEvolves': 'Charizard',
                   'megaStone': 'Charizard-Mega-X',
                   'name': 'Charizardite X',
                   'num': 660,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 585},
 'charizarditey': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Charizard'],
                   'megaEvolves': 'Charizard',
                   'megaStone': 'Charizard-Mega-Y',
                   'name': 'Charizardite Y',
                   'num': 678,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 586},
 'chartiberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Charti Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Rock'},
                 'num': 195,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Rock' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 62},
 'cheriberry': {'gen': 3,
                'isBerry': True,
                'name': 'Cheri Berry',
                'naturalGift': {'basePower': 80, 'type': 'Fire'},
                'num': 149,
                'onEat': 'function (pokemon) {\n'
                         "\t\t\tif (pokemon.status === 'par') {\n"
                         '\t\t\t\tpokemon.cureStatus();\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.status === 'par') {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 63},
 'cherishball': {'gen': 4,
                 'isPokeball': True,
                 'name': 'Cherish Ball',
                 'num': 16,
                 'spritenum': 64},
 'chestoberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Chesto Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Water'},
                 'num': 150,
                 'onEat': 'function (pokemon) {\n'
                          "\t\t\tif (pokemon.status === 'slp') {\n"
                          '\t\t\t\tpokemon.cureStatus();\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             "\t\t\tif (pokemon.status === 'slp') {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 65},
 'chilanberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Chilan Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Normal'},
                 'num': 200,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Normal' &&\n"
                                         '\t\t\t\t'
                                         "(!target.volatiles['substitute'] || "
                                         "move.flags['authentic'] || "
                                         '(move.infiltrates && this.gen >= '
                                         '6))) {\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 66},
 'chilldrive': {'forcedForme': 'Genesect-Chill',
                'gen': 5,
                'itemUser': ['Genesect-Chill'],
                'name': 'Chill Drive',
                'num': 119,
                'onDrive': 'Ice',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '649) || pokemon.baseSpecies.num === 649) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 67},
 'chippedpot': {'fling': {'basePower': 80},
                'gen': 8,
                'name': 'Chipped Pot',
                'num': 1254,
                'spritenum': 720},
 'choiceband': {'fling': {'basePower': 10},
                'gen': 3,
                'isChoice': True,
                'name': 'Choice Band',
                'num': 220,
                'onModifyAtk': 'function (atk, pokemon) {\n'
                               "\t\t\tif (pokemon.volatiles['dynamax'])\n"
                               '\t\t\t\treturn;\n'
                               '\t\t\treturn this.chainModify(1.5);\n'
                               '\t\t}',
                'onModifyAtkPriority': 1,
                'onModifyMove': 'function (move, pokemon) {\n'
                                "\t\t\tpokemon.addVolatile('choicelock');\n"
                                '\t\t}',
                'onStart': 'function (pokemon) {\n'
                           "\t\t\tif (pokemon.volatiles['choicelock']) {\n"
                           "\t\t\t\tthis.debug('removing choicelock: ' + "
                           "pokemon.volatiles['choicelock']);\n"
                           '\t\t\t}\n'
                           "\t\t\tpokemon.removeVolatile('choicelock');\n"
                           '\t\t}',
                'spritenum': 68},
 'choicescarf': {'fling': {'basePower': 10},
                 'gen': 4,
                 'isChoice': True,
                 'name': 'Choice Scarf',
                 'num': 287,
                 'onModifyMove': 'function (move, pokemon) {\n'
                                 "\t\t\tpokemon.addVolatile('choicelock');\n"
                                 '\t\t}',
                 'onModifySpe': 'function (spe, pokemon) {\n'
                                "\t\t\tif (pokemon.volatiles['dynamax'])\n"
                                '\t\t\t\treturn;\n'
                                '\t\t\treturn this.chainModify(1.5);\n'
                                '\t\t}',
                 'onStart': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.volatiles['choicelock']) {\n"
                            "\t\t\t\tthis.debug('removing choicelock: ' + "
                            "pokemon.volatiles['choicelock']);\n"
                            '\t\t\t}\n'
                            "\t\t\tpokemon.removeVolatile('choicelock');\n"
                            '\t\t}',
                 'spritenum': 69},
 'choicespecs': {'fling': {'basePower': 10},
                 'gen': 4,
                 'isChoice': True,
                 'name': 'Choice Specs',
                 'num': 297,
                 'onModifyMove': 'function (move, pokemon) {\n'
                                 "\t\t\tpokemon.addVolatile('choicelock');\n"
                                 '\t\t}',
                 'onModifySpA': 'function (spa, pokemon) {\n'
                                "\t\t\tif (pokemon.volatiles['dynamax'])\n"
                                '\t\t\t\treturn;\n'
                                '\t\t\treturn this.chainModify(1.5);\n'
                                '\t\t}',
                 'onModifySpAPriority': 1,
                 'onStart': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.volatiles['choicelock']) {\n"
                            "\t\t\t\tthis.debug('removing choicelock: ' + "
                            "pokemon.volatiles['choicelock']);\n"
                            '\t\t\t}\n'
                            "\t\t\tpokemon.removeVolatile('choicelock');\n"
                            '\t\t}',
                 'spritenum': 70},
 'chopleberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Chople Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Fighting'},
                 'num': 189,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Fighting' "
                                         '&& '
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 71},
 'clawfossil': {'fling': {'basePower': 100},
                'gen': 3,
                'isNonstandard': 'Past',
                'name': 'Claw Fossil',
                'num': 100,
                'spritenum': 72},
 'cloversweet': {'fling': {'basePower': 10},
                 'gen': 8,
                 'name': 'Clover Sweet',
                 'num': 1112,
                 'spritenum': 707},
 'cobaberry': {'gen': 4,
               'isBerry': True,
               'name': 'Coba Berry',
               'naturalGift': {'basePower': 80, 'type': 'Flying'},
               'num': 192,
               'onEat': 'function () { }',
               'onSourceModifyDamage': 'function (damage, source, target, '
                                       'move) {\n'
                                       "\t\t\tif (move.type === 'Flying' && "
                                       'target.getMoveHitData(move).typeMod > '
                                       '0) {\n'
                                       '\t\t\t\tvar hitSub = '
                                       "target.volatiles['substitute'] && "
                                       "!move.flags['authentic'] && "
                                       '!(move.infiltrates && this.gen >= 6);\n'
                                       '\t\t\t\tif (hitSub)\n'
                                       '\t\t\t\t\treturn;\n'
                                       '\t\t\t\tif (target.eatItem()) {\n'
                                       "\t\t\t\t\tthis.debug('-50% "
                                       "reduction');\n"
                                       "\t\t\t\t\tthis.add('-enditem', target, "
                                       "this.effect, '[weaken]');\n"
                                       '\t\t\t\t\treturn '
                                       'this.chainModify(0.5);\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t}\n'
                                       '\t\t}',
               'spritenum': 76},
 'colburberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Colbur Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Dark'},
                 'num': 198,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Dark' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 78},
 'cornnberry': {'gen': 3,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Cornn Berry',
                'naturalGift': {'basePower': 90, 'type': 'Bug'},
                'num': 175,
                'onEat': False,
                'spritenum': 81},
 'coverfossil': {'fling': {'basePower': 100},
                 'gen': 5,
                 'isNonstandard': 'Past',
                 'name': 'Cover Fossil',
                 'num': 572,
                 'spritenum': 85},
 'crackedpot': {'fling': {'basePower': 80},
                'gen': 8,
                'name': 'Cracked Pot',
                'num': 1253,
                'spritenum': 719},
 'crucibellite': {'gen': 6,
                  'isNonstandard': 'CAP',
                  'itemUser': ['Crucibelle'],
                  'megaEvolves': 'Crucibelle',
                  'megaStone': 'Crucibelle-Mega',
                  'name': 'Crucibellite',
                  'num': -1,
                  'onTakeItem': 'function (item, source) {\n'
                                '\t\t\tif (item.megaEvolves === '
                                'source.baseSpecies.baseSpecies)\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 577},
 'custapberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Custap Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Ghost'},
                 'num': 210,
                 'onEat': 'function () { }',
                 'onFractionalPriority': 'function (priority, pokemon) {\n'
                                         '\t\t\tif (priority <= 0 &&\n'
                                         '\t\t\t\t(pokemon.hp <= pokemon.maxhp '
                                         '/ 4 || (pokemon.hp <= pokemon.maxhp '
                                         '/ 2 && '
                                         "pokemon.hasAbility('gluttony')))) {\n"
                                         '\t\t\t\tif (pokemon.eatItem()) {\n'
                                         "\t\t\t\t\tthis.add('-activate', "
                                         "pokemon, 'item: Custap Berry', "
                                         "'[consumed]');\n"
                                         '\t\t\t\t\treturn 0.1;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'onFractionalPriorityPriority': -2,
                 'spritenum': 86},
 'damprock': {'fling': {'basePower': 60},
              'gen': 4,
              'name': 'Damp Rock',
              'num': 285,
              'spritenum': 88},
 'darkgem': {'gen': 5,
             'isGem': True,
             'isNonstandard': 'Past',
             'name': 'Dark Gem',
             'num': 562,
             'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                      '\t\t\tif (target === source || '
                                      "move.category === 'Status')\n"
                                      '\t\t\t\treturn;\n'
                                      "\t\t\tif (move.type === 'Dark' && "
                                      'source.useItem()) {\n'
                                      "\t\t\t\tsource.addVolatile('gem');\n"
                                      '\t\t\t}\n'
                                      '\t\t}',
             'spritenum': 89},
 'darkiniumz': {'forcedForme': 'Arceus-Dark',
                'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Darkinium Z',
                'num': 791,
                'onPlate': 'Dark',
                'onTakeItem': False,
                'spritenum': 646,
                'zMove': True,
                'zMoveType': 'Dark'},
 'darkmemory': {'forcedForme': 'Silvally-Dark',
                'gen': 7,
                'itemUser': ['Silvally-Dark'],
                'name': 'Dark Memory',
                'num': 919,
                'onMemory': 'Dark',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '773) || pokemon.baseSpecies.num === 773) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 683},
 'dawnstone': {'fling': {'basePower': 80},
               'gen': 4,
               'name': 'Dawn Stone',
               'num': 109,
               'spritenum': 92},
 'decidiumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Decidueye'],
               'name': 'Decidium Z',
               'num': 798,
               'onTakeItem': False,
               'spritenum': 650,
               'zMove': 'Sinister Arrow Raid',
               'zMoveFrom': 'Spirit Shackle'},
 'deepseascale': {'fling': {'basePower': 30},
                  'gen': 3,
                  'itemUser': ['Clamperl'],
                  'name': 'Deep Sea Scale',
                  'num': 227,
                  'onModifySpD': 'function (spd, pokemon) {\n'
                                 '\t\t\tif (pokemon.baseSpecies.name === '
                                 "'Clamperl') {\n"
                                 '\t\t\t\treturn this.chainModify(2);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onModifySpDPriority': 2,
                  'spritenum': 93},
 'deepseatooth': {'fling': {'basePower': 90},
                  'gen': 3,
                  'itemUser': ['Clamperl'],
                  'name': 'Deep Sea Tooth',
                  'num': 226,
                  'onModifySpA': 'function (spa, pokemon) {\n'
                                 '\t\t\tif (pokemon.baseSpecies.name === '
                                 "'Clamperl') {\n"
                                 '\t\t\t\treturn this.chainModify(2);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onModifySpAPriority': 1,
                  'spritenum': 94},
 'destinyknot': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Destiny Knot',
                 'num': 280,
                 'onAttract': 'function (target, source) {\n'
                              "\t\t\tthis.debug('attract intercepted: ' + "
                              "target + ' from ' + source);\n"
                              '\t\t\tif (!source || source === target)\n'
                              '\t\t\t\treturn;\n'
                              "\t\t\tif (!source.volatiles['attract'])\n"
                              "\t\t\t\tsource.addVolatile('attract', target);\n"
                              '\t\t}',
                 'onAttractPriority': -100,
                 'spritenum': 95},
 'diancite': {'gen': 6,
              'isNonstandard': 'Past',
              'itemUser': ['Diancie'],
              'megaEvolves': 'Diancie',
              'megaStone': 'Diancie-Mega',
              'name': 'Diancite',
              'num': 764,
              'onTakeItem': 'function (item, source) {\n'
                            '\t\t\tif (item.megaEvolves === '
                            'source.baseSpecies.baseSpecies)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 624},
 'diveball': {'gen': 3,
              'isPokeball': True,
              'name': 'Dive Ball',
              'num': 7,
              'spritenum': 101},
 'domefossil': {'fling': {'basePower': 100},
                'gen': 3,
                'isNonstandard': 'Past',
                'name': 'Dome Fossil',
                'num': 102,
                'spritenum': 102},
 'dousedrive': {'forcedForme': 'Genesect-Douse',
                'gen': 5,
                'itemUser': ['Genesect-Douse'],
                'name': 'Douse Drive',
                'num': 116,
                'onDrive': 'Water',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '649) || pokemon.baseSpecies.num === 649) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 103},
 'dracoplate': {'forcedForme': 'Arceus-Dragon',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Draco Plate',
                'num': 311,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Dragon') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Dragon',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 105},
 'dragonfang': {'fling': {'basePower': 70},
                'gen': 2,
                'name': 'Dragon Fang',
                'num': 250,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Dragon') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'spritenum': 106},
 'dragongem': {'gen': 5,
               'isGem': True,
               'isNonstandard': 'Past',
               'name': 'Dragon Gem',
               'num': 561,
               'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                        '\t\t\tif (target === source || '
                                        "move.category === 'Status')\n"
                                        '\t\t\t\treturn;\n'
                                        "\t\t\tif (move.type === 'Dragon' && "
                                        'source.useItem()) {\n'
                                        "\t\t\t\tsource.addVolatile('gem');\n"
                                        '\t\t\t}\n'
                                        '\t\t}',
               'spritenum': 107},
 'dragoniumz': {'forcedForme': 'Arceus-Dragon',
                'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Dragonium Z',
                'num': 790,
                'onPlate': 'Dragon',
                'onTakeItem': False,
                'spritenum': 645,
                'zMove': True,
                'zMoveType': 'Dragon'},
 'dragonmemory': {'forcedForme': 'Silvally-Dragon',
                  'gen': 7,
                  'itemUser': ['Silvally-Dragon'],
                  'name': 'Dragon Memory',
                  'num': 918,
                  'onMemory': 'Dragon',
                  'onTakeItem': 'function (item, pokemon, source) {\n'
                                '\t\t\tif ((source && source.baseSpecies.num '
                                '=== 773) || pokemon.baseSpecies.num === 773) '
                                '{\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 682},
 'dragonscale': {'fling': {'basePower': 30},
                 'gen': 2,
                 'name': 'Dragon Scale',
                 'num': 250,
                 'spritenum': 108},
 'dreadplate': {'forcedForme': 'Arceus-Dark',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Dread Plate',
                'num': 312,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Dark') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Dark',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 110},
 'dreamball': {'gen': 5,
               'isPokeball': True,
               'name': 'Dream Ball',
               'num': 576,
               'spritenum': 111},
 'dubiousdisc': {'fling': {'basePower': 50},
                 'gen': 4,
                 'name': 'Dubious Disc',
                 'num': 324,
                 'spritenum': 113},
 'durinberry': {'gen': 3,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Durin Berry',
                'naturalGift': {'basePower': 100, 'type': 'Water'},
                'num': 182,
                'onEat': False,
                'spritenum': 114},
 'duskball': {'gen': 4,
              'isPokeball': True,
              'name': 'Dusk Ball',
              'num': 13,
              'spritenum': 115},
 'duskstone': {'fling': {'basePower': 80},
               'gen': 4,
               'name': 'Dusk Stone',
               'num': 108,
               'spritenum': 116},
 'earthplate': {'forcedForme': 'Arceus-Ground',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Earth Plate',
                'num': 305,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Ground') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Ground',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 117},
 'eeviumz': {'gen': 7,
             'isNonstandard': 'Past',
             'itemUser': ['Eevee'],
             'name': 'Eevium Z',
             'num': 805,
             'onTakeItem': False,
             'spritenum': 657,
             'zMove': 'Extreme Evoboost',
             'zMoveFrom': 'Last Resort'},
 'ejectbutton': {'fling': {'basePower': 30},
                 'gen': 5,
                 'name': 'Eject Button',
                 'num': 547,
                 'onAfterMoveSecondary': 'function (target, source, move) {\n'
                                         '\t\t\tif (source && source !== '
                                         'target && target.hp && move && '
                                         "move.category !== 'Status' && "
                                         '!move.isFutureMove) {\n'
                                         '\t\t\t\tif '
                                         '(!this.canSwitch(target.side) || '
                                         'target.forceSwitchFlag || '
                                         'target.beingCalledBack)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tfor (var _i = 0, _a = '
                                         'this.getAllActive(); _i < _a.length; '
                                         '_i++) {\n'
                                         '\t\t\t\t\tvar pokemon = _a[_i];\n'
                                         '\t\t\t\t\tif (pokemon.switchFlag === '
                                         'true)\n'
                                         '\t\t\t\t\t\treturn;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t\ttarget.switchFlag = true;\n'
                                         '\t\t\t\tif (target.useItem()) {\n'
                                         '\t\t\t\t\tsource.switchFlag = '
                                         'false;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t\telse {\n'
                                         '\t\t\t\t\ttarget.switchFlag = '
                                         'false;\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'onAfterMoveSecondaryPriority': 2,
                 'spritenum': 118},
 'ejectpack': {'fling': {'basePower': 50},
               'gen': 8,
               'name': 'Eject Pack',
               'num': 1119,
               'onAfterBoost': 'function (boost, target, source, effect) {\n'
                               '\t\t\tvar _a;\n'
                               '\t\t\tif (((_a = this.activeMove) === null || '
                               '_a === void 0 ? void 0 : _a.id) === '
                               "'partingshot')\n"
                               '\t\t\t\treturn;\n'
                               '\t\t\tvar eject = false;\n'
                               '\t\t\tvar i;\n'
                               '\t\t\tfor (i in boost) {\n'
                               '\t\t\t\tif (boost[i] < 0) {\n'
                               '\t\t\t\t\teject = true;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t}\n'
                               '\t\t\tif (eject) {\n'
                               '\t\t\t\tif (target.hp) {\n'
                               '\t\t\t\t\tif (!this.canSwitch(target.side))\n'
                               '\t\t\t\t\t\treturn;\n'
                               '\t\t\t\t\tfor (var _i = 0, _b = '
                               'this.getAllActive(); _i < _b.length; _i++) {\n'
                               '\t\t\t\t\t\tvar pokemon = _b[_i];\n'
                               '\t\t\t\t\t\tif (pokemon.switchFlag === true)\n'
                               '\t\t\t\t\t\t\treturn;\n'
                               '\t\t\t\t\t}\n'
                               '\t\t\t\t\tif (target.useItem())\n'
                               '\t\t\t\t\t\ttarget.switchFlag = true;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'spritenum': 714},
 'electirizer': {'fling': {'basePower': 80},
                 'gen': 4,
                 'name': 'Electirizer',
                 'num': 322,
                 'spritenum': 119},
 'electricgem': {'gen': 5,
                 'isGem': True,
                 'isNonstandard': 'Past',
                 'name': 'Electric Gem',
                 'num': 550,
                 'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                          "\t\t\tvar pledges = ['firepledge', "
                                          "'grasspledge', 'waterpledge'];\n"
                                          '\t\t\tif (target === source || '
                                          "move.category === 'Status' || "
                                          'pledges.includes(move.id))\n'
                                          '\t\t\t\treturn;\n'
                                          "\t\t\tif (move.type === 'Electric' "
                                          '&& source.useItem()) {\n'
                                          "\t\t\t\tsource.addVolatile('gem');\n"
                                          '\t\t\t}\n'
                                          '\t\t}',
                 'spritenum': 120},
 'electricmemory': {'forcedForme': 'Silvally-Electric',
                    'gen': 7,
                    'itemUser': ['Silvally-Electric'],
                    'name': 'Electric Memory',
                    'num': 915,
                    'onMemory': 'Electric',
                    'onTakeItem': 'function (item, pokemon, source) {\n'
                                  '\t\t\tif ((source && source.baseSpecies.num '
                                  '=== 773) || pokemon.baseSpecies.num === '
                                  '773) {\n'
                                  '\t\t\t\treturn false;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn true;\n'
                                  '\t\t}',
                    'spritenum': 679},
 'electricseed': {'boosts': {'def': 1},
                  'fling': {'basePower': 10},
                  'gen': 7,
                  'name': 'Electric Seed',
                  'num': 881,
                  'onAnyTerrainStart': 'function () {\n'
                                       '\t\t\tvar pokemon = '
                                       'this.effectState.target;\n'
                                       '\t\t\tif '
                                       "(this.field.isTerrain('electricterrain')) "
                                       '{\n'
                                       '\t\t\t\tpokemon.useItem();\n'
                                       '\t\t\t}\n'
                                       '\t\t}',
                  'onStart': 'function (pokemon) {\n'
                             '\t\t\tif (!pokemon.ignoringItem() && '
                             "this.field.isTerrain('electricterrain')) {\n"
                             '\t\t\t\tpokemon.useItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                  'spritenum': 664},
 'electriumz': {'forcedForme': 'Arceus-Electric',
                'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Electrium Z',
                'num': 779,
                'onPlate': 'Electric',
                'onTakeItem': False,
                'spritenum': 634,
                'zMove': True,
                'zMoveType': 'Electric'},
 'energypowder': {'fling': {'basePower': 30},
                  'gen': 2,
                  'name': 'Energy Powder',
                  'num': 34,
                  'spritenum': 123},
 'enigmaberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Enigma Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Bug'},
                 'num': 208,
                 'onEat': 'function () { }',
                 'onHit': 'function (target, source, move) {\n'
                          '\t\t\tif (move && '
                          'target.getMoveHitData(move).typeMod > 0) {\n'
                          '\t\t\t\tif (target.eatItem()) {\n'
                          '\t\t\t\t\tthis.heal(target.baseMaxhp / 4);\n'
                          '\t\t\t\t}\n'
                          '\t\t\t}\n'
                          '\t\t}',
                 'onTryEatItem': 'function (item, pokemon) {\n'
                                 "\t\t\tif (!this.runEvent('TryHeal', "
                                 'pokemon))\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t}',
                 'spritenum': 124},
 'eviolite': {'fling': {'basePower': 40},
              'gen': 5,
              'name': 'Eviolite',
              'num': 538,
              'onModifyDef': 'function (def, pokemon) {\n'
                             '\t\t\tif (pokemon.baseSpecies.nfe) {\n'
                             '\t\t\t\treturn this.chainModify(1.5);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onModifyDefPriority': 2,
              'onModifySpD': 'function (spd, pokemon) {\n'
                             '\t\t\tif (pokemon.baseSpecies.nfe) {\n'
                             '\t\t\t\treturn this.chainModify(1.5);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onModifySpDPriority': 2,
              'spritenum': 130},
 'expertbelt': {'fling': {'basePower': 10},
                'gen': 4,
                'name': 'Expert Belt',
                'num': 268,
                'onModifyDamage': 'function (damage, source, target, move) {\n'
                                  '\t\t\tif (move && '
                                  'target.getMoveHitData(move).typeMod > 0) {\n'
                                  '\t\t\t\treturn this.chainModify([4915, '
                                  '4096]);\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                'spritenum': 132},
 'fairiumz': {'forcedForme': 'Arceus-Fairy',
              'gen': 7,
              'isNonstandard': 'Past',
              'name': 'Fairium Z',
              'num': 793,
              'onPlate': 'Fairy',
              'onTakeItem': False,
              'spritenum': 648,
              'zMove': True,
              'zMoveType': 'Fairy'},
 'fairygem': {'gen': 6,
              'isGem': True,
              'isNonstandard': 'Past',
              'name': 'Fairy Gem',
              'num': 715,
              'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                       '\t\t\tif (target === source || '
                                       "move.category === 'Status')\n"
                                       '\t\t\t\treturn;\n'
                                       "\t\t\tif (move.type === 'Fairy' && "
                                       'source.useItem()) {\n'
                                       "\t\t\t\tsource.addVolatile('gem');\n"
                                       '\t\t\t}\n'
                                       '\t\t}',
              'spritenum': 611},
 'fairymemory': {'forcedForme': 'Silvally-Fairy',
                 'gen': 7,
                 'itemUser': ['Silvally-Fairy'],
                 'name': 'Fairy Memory',
                 'num': 920,
                 'onMemory': 'Fairy',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 773) || pokemon.baseSpecies.num === 773) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 684},
 'fastball': {'gen': 2,
              'isPokeball': True,
              'name': 'Fast Ball',
              'num': 492,
              'spritenum': 137},
 'fightinggem': {'gen': 5,
                 'isGem': True,
                 'isNonstandard': 'Past',
                 'name': 'Fighting Gem',
                 'num': 553,
                 'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                          '\t\t\tif (target === source || '
                                          "move.category === 'Status')\n"
                                          '\t\t\t\treturn;\n'
                                          "\t\t\tif (move.type === 'Fighting' "
                                          '&& source.useItem()) {\n'
                                          "\t\t\t\tsource.addVolatile('gem');\n"
                                          '\t\t\t}\n'
                                          '\t\t}',
                 'spritenum': 139},
 'fightingmemory': {'forcedForme': 'Silvally-Fighting',
                    'gen': 7,
                    'itemUser': ['Silvally-Fighting'],
                    'name': 'Fighting Memory',
                    'num': 904,
                    'onMemory': 'Fighting',
                    'onTakeItem': 'function (item, pokemon, source) {\n'
                                  '\t\t\tif ((source && source.baseSpecies.num '
                                  '=== 773) || pokemon.baseSpecies.num === '
                                  '773) {\n'
                                  '\t\t\t\treturn false;\n'
                                  '\t\t\t}\n'
                                  '\t\t\treturn true;\n'
                                  '\t\t}',
                    'spritenum': 668},
 'fightiniumz': {'forcedForme': 'Arceus-Fighting',
                 'gen': 7,
                 'isNonstandard': 'Past',
                 'name': 'Fightinium Z',
                 'num': 782,
                 'onPlate': 'Fighting',
                 'onTakeItem': False,
                 'spritenum': 637,
                 'zMove': True,
                 'zMoveType': 'Fighting'},
 'figyberry': {'gen': 3,
               'isBerry': True,
               'name': 'Figy Berry',
               'naturalGift': {'basePower': 80, 'type': 'Bug'},
               'num': 159,
               'onEat': 'function (pokemon) {\n'
                        '\t\t\tthis.heal(pokemon.baseMaxhp * 0.33);\n'
                        "\t\t\tif (pokemon.getNature().minus === 'atk') {\n"
                        "\t\t\t\tpokemon.addVolatile('confusion');\n"
                        '\t\t\t}\n'
                        '\t\t}',
               'onTryEatItem': 'function (item, pokemon) {\n'
                               "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                               '\t\t\t\treturn false;\n'
                               '\t\t}',
               'onUpdate': 'function (pokemon) {\n'
                           '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                           '(pokemon.hp <= pokemon.maxhp / 2 && '
                           "pokemon.hasAbility('gluttony'))) {\n"
                           '\t\t\t\tpokemon.eatItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 140},
 'firegem': {'gen': 5,
             'isGem': True,
             'isNonstandard': 'Past',
             'name': 'Fire Gem',
             'num': 548,
             'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                      "\t\t\tvar pledges = ['firepledge', "
                                      "'grasspledge', 'waterpledge'];\n"
                                      '\t\t\tif (target === source || '
                                      "move.category === 'Status' || "
                                      'pledges.includes(move.id))\n'
                                      '\t\t\t\treturn;\n'
                                      "\t\t\tif (move.type === 'Fire' && "
                                      'source.useItem()) {\n'
                                      "\t\t\t\tsource.addVolatile('gem');\n"
                                      '\t\t\t}\n'
                                      '\t\t}',
             'spritenum': 141},
 'firememory': {'forcedForme': 'Silvally-Fire',
                'gen': 7,
                'itemUser': ['Silvally-Fire'],
                'name': 'Fire Memory',
                'num': 912,
                'onMemory': 'Fire',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '773) || pokemon.baseSpecies.num === 773) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 676},
 'firestone': {'fling': {'basePower': 30},
               'gen': 1,
               'name': 'Fire Stone',
               'num': 82,
               'spritenum': 142},
 'firiumz': {'forcedForme': 'Arceus-Fire',
             'gen': 7,
             'isNonstandard': 'Past',
             'name': 'Firium Z',
             'num': 777,
             'onPlate': 'Fire',
             'onTakeItem': False,
             'spritenum': 632,
             'zMove': True,
             'zMoveType': 'Fire'},
 'fistplate': {'forcedForme': 'Arceus-Fighting',
               'gen': 4,
               'isNonstandard': 'Unobtainable',
               'name': 'Fist Plate',
               'num': 303,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move && move.type === 'Fighting') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'onPlate': 'Fighting',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '493) || pokemon.baseSpecies.num === 493) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 143},
 'flameorb': {'fling': {'basePower': 30, 'status': 'brn'},
              'gen': 4,
              'name': 'Flame Orb',
              'num': 273,
              'onResidual': 'function (pokemon) {\n'
                            "\t\t\tpokemon.trySetStatus('brn', pokemon);\n"
                            '\t\t}',
              'onResidualOrder': 28,
              'onResidualSubOrder': 3,
              'spritenum': 145},
 'flameplate': {'forcedForme': 'Arceus-Fire',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Flame Plate',
                'num': 298,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Fire') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Fire',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 146},
 'floatstone': {'fling': {'basePower': 30},
                'gen': 5,
                'name': 'Float Stone',
                'num': 539,
                'onModifyWeight': 'function (weighthg) {\n'
                                  '\t\t\treturn this.trunc(weighthg / 2);\n'
                                  '\t\t}',
                'spritenum': 147},
 'flowersweet': {'fling': {'basePower': 0},
                 'gen': 8,
                 'name': 'Flower Sweet',
                 'num': 1113,
                 'spritenum': 708},
 'flyinggem': {'gen': 5,
               'isGem': True,
               'isNonstandard': 'Past',
               'name': 'Flying Gem',
               'num': 556,
               'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                        '\t\t\tif (target === source || '
                                        "move.category === 'Status')\n"
                                        '\t\t\t\treturn;\n'
                                        "\t\t\tif (move.type === 'Flying' && "
                                        'source.useItem()) {\n'
                                        "\t\t\t\tsource.addVolatile('gem');\n"
                                        '\t\t\t}\n'
                                        '\t\t}',
               'spritenum': 149},
 'flyingmemory': {'forcedForme': 'Silvally-Flying',
                  'gen': 7,
                  'itemUser': ['Silvally-Flying'],
                  'name': 'Flying Memory',
                  'num': 905,
                  'onMemory': 'Flying',
                  'onTakeItem': 'function (item, pokemon, source) {\n'
                                '\t\t\tif ((source && source.baseSpecies.num '
                                '=== 773) || pokemon.baseSpecies.num === 773) '
                                '{\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 669},
 'flyiniumz': {'forcedForme': 'Arceus-Flying',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Flyinium Z',
               'num': 785,
               'onPlate': 'Flying',
               'onTakeItem': False,
               'spritenum': 640,
               'zMove': True,
               'zMoveType': 'Flying'},
 'focusband': {'fling': {'basePower': 10},
               'gen': 2,
               'name': 'Focus Band',
               'num': 230,
               'onDamage': 'function (damage, target, source, effect) {\n'
                           '\t\t\tif (this.randomChance(1, 10) && damage >= '
                           'target.hp && effect && effect.effectType === '
                           "'Move') {\n"
                           '\t\t\t\tthis.add("-activate", target, "item: Focus '
                           'Band");\n'
                           '\t\t\t\treturn target.hp - 1;\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'onDamagePriority': -40,
               'spritenum': 150},
 'focussash': {'fling': {'basePower': 10},
               'gen': 4,
               'name': 'Focus Sash',
               'num': 275,
               'onDamage': 'function (damage, target, source, effect) {\n'
                           '\t\t\tif (target.hp === target.maxhp && damage >= '
                           'target.hp && effect && effect.effectType === '
                           "'Move') {\n"
                           '\t\t\t\tif (target.useItem()) {\n'
                           '\t\t\t\t\treturn target.hp - 1;\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'onDamagePriority': -40,
               'spritenum': 151},
 'fossilizedbird': {'fling': {'basePower': 100},
                    'gen': 8,
                    'name': 'Fossilized Bird',
                    'num': 1105,
                    'spritenum': 700},
 'fossilizeddino': {'fling': {'basePower': 100},
                    'gen': 8,
                    'name': 'Fossilized Dino',
                    'num': 1108,
                    'spritenum': 703},
 'fossilizeddrake': {'fling': {'basePower': 100},
                     'gen': 8,
                     'name': 'Fossilized Drake',
                     'num': 1107,
                     'spritenum': 702},
 'fossilizedfish': {'fling': {'basePower': 100},
                    'gen': 8,
                    'name': 'Fossilized Fish',
                    'num': 1106,
                    'spritenum': 701},
 'friendball': {'gen': 2,
                'isPokeball': True,
                'name': 'Friend Ball',
                'num': 497,
                'spritenum': 153},
 'fullincense': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Full Incense',
                 'num': 316,
                 'onFractionalPriority': -0.1,
                 'spritenum': 155},
 'galaricacuff': {'fling': {'basePower': 30},
                  'gen': 8,
                  'name': 'Galarica Cuff',
                  'num': 1582,
                  'spritenum': 739},
 'galaricawreath': {'fling': {'basePower': 30},
                    'gen': 8,
                    'name': 'Galarica Wreath',
                    'num': 1592,
                    'spritenum': 740},
 'galladite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Gallade'],
               'megaEvolves': 'Gallade',
               'megaStone': 'Gallade-Mega',
               'name': 'Galladite',
               'num': 756,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 616},
 'ganlonberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Ganlon Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Ice'},
                 'num': 202,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.boost({ def: 1 });\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 158},
 'garchompite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Garchomp'],
                 'megaEvolves': 'Garchomp',
                 'megaStone': 'Garchomp-Mega',
                 'name': 'Garchompite',
                 'num': 683,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 589},
 'gardevoirite': {'gen': 6,
                  'isNonstandard': 'Past',
                  'itemUser': ['Gardevoir'],
                  'megaEvolves': 'Gardevoir',
                  'megaStone': 'Gardevoir-Mega',
                  'name': 'Gardevoirite',
                  'num': 657,
                  'onTakeItem': 'function (item, source) {\n'
                                '\t\t\tif (item.megaEvolves === '
                                'source.baseSpecies.baseSpecies)\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 587},
 'gengarite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Gengar'],
               'megaEvolves': 'Gengar',
               'megaStone': 'Gengar-Mega',
               'name': 'Gengarite',
               'num': 656,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 588},
 'ghostgem': {'gen': 5,
              'isGem': True,
              'isNonstandard': 'Past',
              'name': 'Ghost Gem',
              'num': 560,
              'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                       '\t\t\tif (target === source || '
                                       "move.category === 'Status')\n"
                                       '\t\t\t\treturn;\n'
                                       "\t\t\tif (move.type === 'Ghost' && "
                                       'source.useItem()) {\n'
                                       "\t\t\t\tsource.addVolatile('gem');\n"
                                       '\t\t\t}\n'
                                       '\t\t}',
              'spritenum': 161},
 'ghostiumz': {'forcedForme': 'Arceus-Ghost',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Ghostium Z',
               'num': 789,
               'onPlate': 'Ghost',
               'onTakeItem': False,
               'spritenum': 644,
               'zMove': True,
               'zMoveType': 'Ghost'},
 'ghostmemory': {'forcedForme': 'Silvally-Ghost',
                 'gen': 7,
                 'itemUser': ['Silvally-Ghost'],
                 'name': 'Ghost Memory',
                 'num': 910,
                 'onMemory': 'Ghost',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 773) || pokemon.baseSpecies.num === 773) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 674},
 'glalitite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Glalie'],
               'megaEvolves': 'Glalie',
               'megaStone': 'Glalie-Mega',
               'name': 'Glalitite',
               'num': 763,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 623},
 'goldberry': {'gen': 2,
               'isBerry': True,
               'isNonstandard': 'Past',
               'name': 'Gold Berry',
               'naturalGift': {'basePower': 80, 'type': 'Psychic'},
               'num': 158,
               'onEat': 'function (pokemon) {\n\t\t\tthis.heal(30);\n\t\t}',
               'onResidual': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n'
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
               'onResidualOrder': 5,
               'onTryEatItem': 'function (item, pokemon) {\n'
                               "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                               '\t\t\t\treturn false;\n'
                               '\t\t}',
               'spritenum': 448},
 'goldbottlecap': {'fling': {'basePower': 30},
                   'gen': 7,
                   'name': 'Gold Bottle Cap',
                   'num': 796,
                   'spritenum': 697},
 'grassgem': {'gen': 5,
              'isGem': True,
              'isNonstandard': 'Past',
              'name': 'Grass Gem',
              'num': 551,
              'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                       "\t\t\tvar pledges = ['firepledge', "
                                       "'grasspledge', 'waterpledge'];\n"
                                       '\t\t\tif (target === source || '
                                       "move.category === 'Status' || "
                                       'pledges.includes(move.id))\n'
                                       '\t\t\t\treturn;\n'
                                       "\t\t\tif (move.type === 'Grass' && "
                                       'source.useItem()) {\n'
                                       "\t\t\t\tsource.addVolatile('gem');\n"
                                       '\t\t\t}\n'
                                       '\t\t}',
              'spritenum': 172},
 'grassiumz': {'forcedForme': 'Arceus-Grass',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Grassium Z',
               'num': 780,
               'onPlate': 'Grass',
               'onTakeItem': False,
               'spritenum': 635,
               'zMove': True,
               'zMoveType': 'Grass'},
 'grassmemory': {'forcedForme': 'Silvally-Grass',
                 'gen': 7,
                 'itemUser': ['Silvally-Grass'],
                 'name': 'Grass Memory',
                 'num': 914,
                 'onMemory': 'Grass',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 773) || pokemon.baseSpecies.num === 773) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 678},
 'grassyseed': {'boosts': {'def': 1},
                'fling': {'basePower': 10},
                'gen': 7,
                'name': 'Grassy Seed',
                'num': 884,
                'onAnyTerrainStart': 'function () {\n'
                                     '\t\t\tvar pokemon = '
                                     'this.effectState.target;\n'
                                     '\t\t\tif '
                                     "(this.field.isTerrain('grassyterrain')) "
                                     '{\n'
                                     '\t\t\t\tpokemon.useItem();\n'
                                     '\t\t\t}\n'
                                     '\t\t}',
                'onStart': 'function (pokemon) {\n'
                           '\t\t\tif (!pokemon.ignoringItem() && '
                           "this.field.isTerrain('grassyterrain')) {\n"
                           '\t\t\t\tpokemon.useItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
                'spritenum': 667},
 'greatball': {'gen': 1,
               'isPokeball': True,
               'name': 'Great Ball',
               'num': 3,
               'spritenum': 174},
 'grepaberry': {'gen': 3,
                'isBerry': True,
                'name': 'Grepa Berry',
                'naturalGift': {'basePower': 90, 'type': 'Flying'},
                'num': 173,
                'onEat': False,
                'spritenum': 178},
 'gripclaw': {'fling': {'basePower': 90},
              'gen': 4,
              'name': 'Grip Claw',
              'num': 286,
              'spritenum': 179},
 'griseousorb': {'fling': {'basePower': 60},
                 'forcedForme': 'Giratina-Origin',
                 'gen': 4,
                 'itemUser': ['Giratina-Origin'],
                 'name': 'Griseous Orb',
                 'num': 112,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                '\t\t\tif (user.baseSpecies.num === 487 && '
                                "(move.type === 'Ghost' || move.type === "
                                "'Dragon')) {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 487) || pokemon.baseSpecies.num === 487) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 180},
 'groundgem': {'gen': 5,
               'isGem': True,
               'isNonstandard': 'Past',
               'name': 'Ground Gem',
               'num': 555,
               'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                        '\t\t\tif (target === source || '
                                        "move.category === 'Status')\n"
                                        '\t\t\t\treturn;\n'
                                        "\t\t\tif (move.type === 'Ground' && "
                                        'source.useItem()) {\n'
                                        "\t\t\t\tsource.addVolatile('gem');\n"
                                        '\t\t\t}\n'
                                        '\t\t}',
               'spritenum': 182},
 'groundiumz': {'forcedForme': 'Arceus-Ground',
                'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Groundium Z',
                'num': 784,
                'onPlate': 'Ground',
                'onTakeItem': False,
                'spritenum': 639,
                'zMove': True,
                'zMoveType': 'Ground'},
 'groundmemory': {'forcedForme': 'Silvally-Ground',
                  'gen': 7,
                  'itemUser': ['Silvally-Ground'],
                  'name': 'Ground Memory',
                  'num': 907,
                  'onMemory': 'Ground',
                  'onTakeItem': 'function (item, pokemon, source) {\n'
                                '\t\t\tif ((source && source.baseSpecies.num '
                                '=== 773) || pokemon.baseSpecies.num === 773) '
                                '{\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 671},
 'gyaradosite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Gyarados'],
                 'megaEvolves': 'Gyarados',
                 'megaStone': 'Gyarados-Mega',
                 'name': 'Gyaradosite',
                 'num': 676,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 589},
 'habanberry': {'gen': 4,
                'isBerry': True,
                'name': 'Haban Berry',
                'naturalGift': {'basePower': 80, 'type': 'Dragon'},
                'num': 197,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Dragon' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 185},
 'hardstone': {'fling': {'basePower': 100},
               'gen': 2,
               'name': 'Hard Stone',
               'num': 238,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move && move.type === 'Rock') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'spritenum': 187},
 'healball': {'gen': 4,
              'isPokeball': True,
              'name': 'Heal Ball',
              'num': 14,
              'spritenum': 188},
 'heatrock': {'fling': {'basePower': 60},
              'gen': 4,
              'name': 'Heat Rock',
              'num': 284,
              'spritenum': 193},
 'heavyball': {'gen': 2,
               'isPokeball': True,
               'name': 'Heavy Ball',
               'num': 495,
               'spritenum': 194},
 'heavydutyboots': {'fling': {'basePower': 80},
                    'gen': 8,
                    'name': 'Heavy-Duty Boots',
                    'num': 1120,
                    'spritenum': 715},
 'helixfossil': {'fling': {'basePower': 100},
                 'gen': 3,
                 'isNonstandard': 'Past',
                 'name': 'Helix Fossil',
                 'num': 101,
                 'spritenum': 195},
 'heracronite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Heracross'],
                 'megaEvolves': 'Heracross',
                 'megaStone': 'Heracross-Mega',
                 'name': 'Heracronite',
                 'num': 680,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 590},
 'hondewberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Hondew Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Ground'},
                 'num': 172,
                 'onEat': False,
                 'spritenum': 213},
 'houndoominite': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Houndoom'],
                   'megaEvolves': 'Houndoom',
                   'megaStone': 'Houndoom-Mega',
                   'name': 'Houndoominite',
                   'num': 666,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 591},
 'iapapaberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Iapapa Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Dark'},
                 'num': 163,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.heal(pokemon.baseMaxhp * 0.33);\n'
                          "\t\t\tif (pokemon.getNature().minus === 'def') {\n"
                          "\t\t\t\tpokemon.addVolatile('confusion');\n"
                          '\t\t\t}\n'
                          '\t\t}',
                 'onTryEatItem': 'function (item, pokemon) {\n'
                                 "\t\t\tif (!this.runEvent('TryHeal', "
                                 'pokemon))\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 217},
 'iceberry': {'gen': 2,
              'isBerry': True,
              'isNonstandard': 'Past',
              'name': 'Ice Berry',
              'naturalGift': {'basePower': 80, 'type': 'Grass'},
              'num': 152,
              'onEat': 'function (pokemon) {\n'
                       "\t\t\tif (pokemon.status === 'brn') {\n"
                       '\t\t\t\tpokemon.cureStatus();\n'
                       '\t\t\t}\n'
                       '\t\t}',
              'onUpdate': 'function (pokemon) {\n'
                          "\t\t\tif (pokemon.status === 'brn') {\n"
                          '\t\t\t\tpokemon.eatItem();\n'
                          '\t\t\t}\n'
                          '\t\t}',
              'spritenum': 381},
 'icegem': {'gen': 5,
            'isGem': True,
            'isNonstandard': 'Past',
            'name': 'Ice Gem',
            'num': 552,
            'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                     '\t\t\tif (target === source || '
                                     "move.category === 'Status')\n"
                                     '\t\t\t\treturn;\n'
                                     "\t\t\tif (move.type === 'Ice' && "
                                     'source.useItem()) {\n'
                                     "\t\t\t\tsource.addVolatile('gem');\n"
                                     '\t\t\t}\n'
                                     '\t\t}',
            'spritenum': 218},
 'icememory': {'forcedForme': 'Silvally-Ice',
               'gen': 7,
               'itemUser': ['Silvally-Ice'],
               'name': 'Ice Memory',
               'num': 917,
               'onMemory': 'Ice',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '773) || pokemon.baseSpecies.num === 773) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 681},
 'icestone': {'fling': {'basePower': 30},
              'gen': 7,
              'name': 'Ice Stone',
              'num': 849,
              'spritenum': 693},
 'icicleplate': {'forcedForme': 'Arceus-Ice',
                 'gen': 4,
                 'isNonstandard': 'Unobtainable',
                 'name': 'Icicle Plate',
                 'num': 302,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Ice') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onPlate': 'Ice',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 493) || pokemon.baseSpecies.num === 493) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 220},
 'iciumz': {'forcedForme': 'Arceus-Ice',
            'gen': 7,
            'isNonstandard': 'Past',
            'name': 'Icium Z',
            'num': 781,
            'onPlate': 'Ice',
            'onTakeItem': False,
            'spritenum': 636,
            'zMove': True,
            'zMoveType': 'Ice'},
 'icyrock': {'fling': {'basePower': 40},
             'gen': 4,
             'name': 'Icy Rock',
             'num': 282,
             'spritenum': 221},
 'inciniumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Incineroar'],
               'name': 'Incinium Z',
               'num': 799,
               'onTakeItem': False,
               'spritenum': 651,
               'zMove': 'Malicious Moonsault',
               'zMoveFrom': 'Darkest Lariat'},
 'insectplate': {'forcedForme': 'Arceus-Bug',
                 'gen': 4,
                 'isNonstandard': 'Unobtainable',
                 'name': 'Insect Plate',
                 'num': 308,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Bug') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onPlate': 'Bug',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 493) || pokemon.baseSpecies.num === 493) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 223},
 'ironball': {'fling': {'basePower': 130},
              'gen': 4,
              'name': 'Iron Ball',
              'num': 278,
              'onEffectiveness': 'function (typeMod, target, type, move) {\n'
                                 '\t\t\tif (!target)\n'
                                 '\t\t\t\treturn;\n'
                                 "\t\t\tif (target.volatiles['ingrain'] || "
                                 "target.volatiles['smackdown'] || "
                                 "this.field.getPseudoWeather('gravity'))\n"
                                 '\t\t\t\treturn;\n'
                                 "\t\t\tif (move.type === 'Ground' && "
                                 "target.hasType('Flying'))\n"
                                 '\t\t\t\treturn 0;\n'
                                 '\t\t}',
              'onModifySpe': 'function (spe) {\n'
                             '\t\t\treturn this.chainModify(0.5);\n'
                             '\t\t}',
              'spritenum': 224},
 'ironplate': {'forcedForme': 'Arceus-Steel',
               'gen': 4,
               'isNonstandard': 'Unobtainable',
               'name': 'Iron Plate',
               'num': 313,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move.type === 'Steel') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'onPlate': 'Steel',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '493) || pokemon.baseSpecies.num === 493) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 225},
 'jabocaberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Jaboca Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Dragon'},
                 'num': 211,
                 'onDamagingHit': 'function (damage, target, source, move) {\n'
                                  "\t\t\tif (move.category === 'Physical' && "
                                  'source.hp && source.isActive) {\n'
                                  '\t\t\t\tif (target.eatItem()) {\n'
                                  '\t\t\t\t\tthis.damage(source.baseMaxhp / '
                                  "(target.hasAbility('ripen') ? 4 : 8), "
                                  'source, target);\n'
                                  '\t\t\t\t}\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                 'onEat': 'function () { }',
                 'spritenum': 230},
 'jawfossil': {'fling': {'basePower': 100},
               'gen': 6,
               'isNonstandard': 'Past',
               'name': 'Jaw Fossil',
               'num': 710,
               'spritenum': 694},
 'kangaskhanite': {'gen': 6,
                   'isNonstandard': 'Past',
                   'itemUser': ['Kangaskhan'],
                   'megaEvolves': 'Kangaskhan',
                   'megaStone': 'Kangaskhan-Mega',
                   'name': 'Kangaskhanite',
                   'num': 675,
                   'onTakeItem': 'function (item, source) {\n'
                                 '\t\t\tif (item.megaEvolves === '
                                 'source.baseSpecies.baseSpecies)\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 592},
 'kasibberry': {'gen': 4,
                'isBerry': True,
                'name': 'Kasib Berry',
                'naturalGift': {'basePower': 80, 'type': 'Ghost'},
                'num': 196,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Ghost' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 233},
 'kebiaberry': {'gen': 4,
                'isBerry': True,
                'name': 'Kebia Berry',
                'naturalGift': {'basePower': 80, 'type': 'Poison'},
                'num': 190,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Poison' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 234},
 'keeberry': {'gen': 6,
              'isBerry': True,
              'name': 'Kee Berry',
              'naturalGift': {'basePower': 100, 'type': 'Fairy'},
              'num': 687,
              'onAfterMoveSecondary': 'function (target, source, move) {\n'
                                      "\t\t\tif (move.category === 'Physical') "
                                      '{\n'
                                      "\t\t\t\tif (move.id === 'present' && "
                                      'move.heal)\n'
                                      '\t\t\t\t\treturn;\n'
                                      '\t\t\t\ttarget.eatItem();\n'
                                      '\t\t\t}\n'
                                      '\t\t}',
              'onEat': 'function (pokemon) {\n'
                       '\t\t\tthis.boost({ def: 1 });\n'
                       '\t\t}',
              'spritenum': 593},
 'kelpsyberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Kelpsy Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Fighting'},
                 'num': 170,
                 'onEat': False,
                 'spritenum': 235},
 'kingsrock': {'fling': {'basePower': 30, 'volatileStatus': 'flinch'},
               'gen': 2,
               'name': "King's Rock",
               'num': 221,
               'onModifyMove': 'function (move) {\n'
                               '\t\t\tif (move.category !== "Status") {\n'
                               '\t\t\t\tif (!move.secondaries)\n'
                               '\t\t\t\t\tmove.secondaries = [];\n'
                               '\t\t\t\tfor (var _i = 0, _a = '
                               'move.secondaries; _i < _a.length; _i++) {\n'
                               '\t\t\t\t\tvar secondary = _a[_i];\n'
                               '\t\t\t\t\tif (secondary.volatileStatus === '
                               "'flinch')\n"
                               '\t\t\t\t\t\treturn;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t\tmove.secondaries.push({\n'
                               '\t\t\t\t\tchance: 10,\n'
                               "\t\t\t\t\tvolatileStatus: 'flinch',\n"
                               '\t\t\t\t});\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'onModifyMovePriority': -1,
               'spritenum': 236},
 'kommoniumz': {'gen': 7,
                'isNonstandard': 'Past',
                'itemUser': ['Kommo-o', 'Kommo-o-Totem'],
                'name': 'Kommonium Z',
                'num': 926,
                'onTakeItem': False,
                'spritenum': 690,
                'zMove': 'Clangorous Soulblaze',
                'zMoveFrom': 'Clanging Scales'},
 'laggingtail': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Lagging Tail',
                 'num': 279,
                 'onFractionalPriority': -0.1,
                 'spritenum': 237},
 'lansatberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Lansat Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Flying'},
                 'num': 206,
                 'onEat': 'function (pokemon) {\n'
                          "\t\t\tpokemon.addVolatile('focusenergy');\n"
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 238},
 'latiasite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Latias'],
               'megaEvolves': 'Latias',
               'megaStone': 'Latias-Mega',
               'name': 'Latiasite',
               'num': 684,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 629},
 'latiosite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Latios'],
               'megaEvolves': 'Latios',
               'megaStone': 'Latios-Mega',
               'name': 'Latiosite',
               'num': 685,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 630},
 'laxincense': {'fling': {'basePower': 10},
                'gen': 3,
                'name': 'Lax Incense',
                'num': 255,
                'onModifyAccuracy': 'function (accuracy) {\n'
                                    "\t\t\tif (typeof accuracy !== 'number')\n"
                                    '\t\t\t\treturn;\n'
                                    "\t\t\tthis.debug('lax incense - "
                                    "decreasing accuracy');\n"
                                    '\t\t\treturn this.chainModify([3686, '
                                    '4096]);\n'
                                    '\t\t}',
                'onModifyAccuracyPriority': -2,
                'spritenum': 240},
 'leafstone': {'fling': {'basePower': 30},
               'gen': 1,
               'name': 'Leaf Stone',
               'num': 85,
               'spritenum': 241},
 'leek': {'fling': {'basePower': 60},
          'gen': 8,
          'itemUser': ['Farfetch'd', 'Sirfetch`d'],
          'name': 'Leek',
          'num': 259,
          'onModifyCritRatio': 'function (critRatio, user) {\n'
                               '\t\t\tif (["farfetchd", '
                               '"sirfetchd"].includes(this.toID(user.baseSpecies.baseSpecies))) '
                               '{\n'
                               '\t\t\t\treturn critRatio + 2;\n'
                               '\t\t\t}\n'
                               '\t\t}',
          'spritenum': 475},
 'leftovers': {'fling': {'basePower': 10},
               'gen': 2,
               'name': 'Leftovers',
               'num': 234,
               'onResidual': 'function (pokemon) {\n'
                             '\t\t\tthis.heal(pokemon.baseMaxhp / 16);\n'
                             '\t\t}',
               'onResidualOrder': 5,
               'onResidualSubOrder': 4,
               'spritenum': 242},
 'leppaberry': {'gen': 3,
                'isBerry': True,
                'name': 'Leppa Berry',
                'naturalGift': {'basePower': 80, 'type': 'Fighting'},
                'num': 154,
                'onEat': 'function (pokemon) {\n'
                         '\t\t\tvar moveSlot = pokemon.moveSlots.find(function '
                         '(move) { return move.pp === 0; }) ||\n'
                         '\t\t\t\tpokemon.moveSlots.find(function (move) { '
                         'return move.pp < move.maxpp; });\n'
                         '\t\t\tif (!moveSlot)\n'
                         '\t\t\t\treturn;\n'
                         '\t\t\tmoveSlot.pp += 10;\n'
                         '\t\t\tif (moveSlot.pp > moveSlot.maxpp)\n'
                         '\t\t\t\tmoveSlot.pp = moveSlot.maxpp;\n'
                         "\t\t\tthis.add('-activate', pokemon, 'item: Leppa "
                         "Berry', moveSlot.move, '[consumed]');\n"
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            '\t\t\tif (!pokemon.hp)\n'
                            '\t\t\t\treturn;\n'
                            '\t\t\tif (pokemon.moveSlots.some(function (move) '
                            '{ return move.pp === 0; })) {\n'
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 244},
 'levelball': {'gen': 2,
               'isPokeball': True,
               'name': 'Level Ball',
               'num': 493,
               'spritenum': 246},
 'liechiberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Liechi Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Grass'},
                 'num': 201,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.boost({ atk: 1 });\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 248},
 'lifeorb': {'fling': {'basePower': 30},
             'gen': 4,
             'name': 'Life Orb',
             'num': 270,
             'onAfterMoveSecondarySelf': 'function (source, target, move) {\n'
                                         '\t\t\tif (source && source !== '
                                         'target && move && move.category !== '
                                         "'Status') {\n"
                                         '\t\t\t\tthis.damage(source.baseMaxhp '
                                         '/ 10, source, source, '
                                         "this.dex.items.get('lifeorb'));\n"
                                         '\t\t\t}\n'
                                         '\t\t}',
             'onModifyDamage': 'function (damage, source, target, move) {\n'
                               '\t\t\treturn this.chainModify([5324, 4096]);\n'
                               '\t\t}',
             'spritenum': 249},
 'lightball': {'fling': {'basePower': 30, 'status': 'par'},
               'gen': 2,
               'itemUser': ['Pikachu'],
               'name': 'Light Ball',
               'num': 236,
               'onModifyAtk': 'function (atk, pokemon) {\n'
                              '\t\t\tif (pokemon.baseSpecies.baseSpecies === '
                              "'Pikachu') {\n"
                              '\t\t\t\treturn this.chainModify(2);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onModifyAtkPriority': 1,
               'onModifySpA': 'function (spa, pokemon) {\n'
                              '\t\t\tif (pokemon.baseSpecies.baseSpecies === '
                              "'Pikachu') {\n"
                              '\t\t\t\treturn this.chainModify(2);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onModifySpAPriority': 1,
               'spritenum': 251},
 'lightclay': {'fling': {'basePower': 30},
               'gen': 4,
               'name': 'Light Clay',
               'num': 269,
               'spritenum': 252},
 'lopunnite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Lopunny'],
               'megaEvolves': 'Lopunny',
               'megaStone': 'Lopunny-Mega',
               'name': 'Lopunnite',
               'num': 768,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 626},
 'loveball': {'gen': 2,
              'isPokeball': True,
              'name': 'Love Ball',
              'num': 496,
              'spritenum': 258},
 'lovesweet': {'fling': {'basePower': 10},
               'gen': 8,
               'name': 'Love Sweet',
               'num': 1110,
               'spritenum': 705},
 'lucarionite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Lucario'],
                 'megaEvolves': 'Lucario',
                 'megaStone': 'Lucario-Mega',
                 'name': 'Lucarionite',
                 'num': 673,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 594},
 'luckypunch': {'fling': {'basePower': 40},
                'gen': 2,
                'isNonstandard': 'Past',
                'itemUser': ['Chansey'],
                'name': 'Lucky Punch',
                'num': 256,
                'onModifyCritRatio': 'function (critRatio, user) {\n'
                                     '\t\t\tif (user.baseSpecies.name === '
                                     "'Chansey') {\n"
                                     '\t\t\t\treturn critRatio + 2;\n'
                                     '\t\t\t}\n'
                                     '\t\t}',
                'spritenum': 261},
 'lumberry': {'gen': 3,
              'isBerry': True,
              'name': 'Lum Berry',
              'naturalGift': {'basePower': 80, 'type': 'Flying'},
              'num': 157,
              'onAfterSetStatus': 'function (status, pokemon) {\n'
                                  '\t\t\tpokemon.eatItem();\n'
                                  '\t\t}',
              'onAfterSetStatusPriority': -1,
              'onEat': 'function (pokemon) {\n'
                       '\t\t\tpokemon.cureStatus();\n'
                       "\t\t\tpokemon.removeVolatile('confusion');\n"
                       '\t\t}',
              'onUpdate': 'function (pokemon) {\n'
                          '\t\t\tif (pokemon.status || '
                          "pokemon.volatiles['confusion']) {\n"
                          '\t\t\t\tpokemon.eatItem();\n'
                          '\t\t\t}\n'
                          '\t\t}',
              'spritenum': 262},
 'luminousmoss': {'boosts': {'spd': 1},
                  'fling': {'basePower': 30},
                  'gen': 6,
                  'name': 'Luminous Moss',
                  'num': 648,
                  'onDamagingHit': 'function (damage, target, source, move) {\n'
                                   "\t\t\tif (move.type === 'Water') {\n"
                                   '\t\t\t\ttarget.useItem();\n'
                                   '\t\t\t}\n'
                                   '\t\t}',
                  'spritenum': 595},
 'lunaliumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Lunala', 'Necrozma-Dawn-Wings'],
               'name': 'Lunalium Z',
               'num': 922,
               'onTakeItem': False,
               'spritenum': 686,
               'zMove': 'Menacing Moonraze Maelstrom',
               'zMoveFrom': 'Moongeist Beam'},
 'lureball': {'gen': 2,
              'isPokeball': True,
              'name': 'Lure Ball',
              'num': 494,
              'spritenum': 264},
 'lustrousorb': {'fling': {'basePower': 60},
                 'gen': 4,
                 'itemUser': ['Palkia'],
                 'name': 'Lustrous Orb',
                 'num': 136,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                '\t\t\tif (move && user.baseSpecies.name === '
                                "'Palkia' && (move.type === 'Water' || "
                                "move.type === 'Dragon')) {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 265},
 'luxuryball': {'gen': 3,
                'isPokeball': True,
                'name': 'Luxury Ball',
                'num': 11,
                'spritenum': 266},
 'lycaniumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Lycanroc', 'Lycanroc-Midnight', 'Lycanroc-Dusk'],
               'name': 'Lycanium Z',
               'num': 925,
               'onTakeItem': False,
               'spritenum': 689,
               'zMove': 'Splintered Stormshards',
               'zMoveFrom': 'Stone Edge'},
 'machobrace': {'fling': {'basePower': 60},
                'gen': 3,
                'ignoreKlutz': True,
                'name': 'Macho Brace',
                'num': 215,
                'onModifySpe': 'function (spe) {\n'
                               '\t\t\treturn this.chainModify(0.5);\n'
                               '\t\t}',
                'spritenum': 269},
 'magmarizer': {'fling': {'basePower': 80},
                'gen': 4,
                'name': 'Magmarizer',
                'num': 323,
                'spritenum': 272},
 'magnet': {'fling': {'basePower': 30},
            'gen': 2,
            'name': 'Magnet',
            'num': 242,
            'onBasePower': 'function (basePower, user, target, move) {\n'
                           "\t\t\tif (move.type === 'Electric') {\n"
                           '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                           '\t\t\t}\n'
                           '\t\t}',
            'onBasePowerPriority': 15,
            'spritenum': 273},
 'magoberry': {'gen': 3,
               'isBerry': True,
               'name': 'Mago Berry',
               'naturalGift': {'basePower': 80, 'type': 'Ghost'},
               'num': 161,
               'onEat': 'function (pokemon) {\n'
                        '\t\t\tthis.heal(pokemon.baseMaxhp * 0.33);\n'
                        "\t\t\tif (pokemon.getNature().minus === 'spe') {\n"
                        "\t\t\t\tpokemon.addVolatile('confusion');\n"
                        '\t\t\t}\n'
                        '\t\t}',
               'onTryEatItem': 'function (item, pokemon) {\n'
                               "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                               '\t\t\t\treturn false;\n'
                               '\t\t}',
               'onUpdate': 'function (pokemon) {\n'
                           '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                           '(pokemon.hp <= pokemon.maxhp / 2 && '
                           "pokemon.hasAbility('gluttony'))) {\n"
                           '\t\t\t\tpokemon.eatItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 274},
 'magostberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Magost Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Rock'},
                 'num': 176,
                 'onEat': False,
                 'spritenum': 275},
 'mail': {'gen': 2,
          'isNonstandard': 'Past',
          'name': 'Mail',
          'num': 0,
          'onTakeItem': 'function (item, source) {\n'
                        '\t\t\tif (!this.activeMove)\n'
                        '\t\t\t\treturn false;\n'
                        "\t\t\tif (this.activeMove.id !== 'knockoff' && "
                        "this.activeMove.id !== 'thief' && this.activeMove.id "
                        "!== 'covet')\n"
                        '\t\t\t\treturn false;\n'
                        '\t\t}',
          'spritenum': 403},
 'manectite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Manectric'],
               'megaEvolves': 'Manectric',
               'megaStone': 'Manectric-Mega',
               'name': 'Manectite',
               'num': 682,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 596},
 'marangaberry': {'gen': 6,
                  'isBerry': True,
                  'name': 'Maranga Berry',
                  'naturalGift': {'basePower': 100, 'type': 'Dark'},
                  'num': 688,
                  'onAfterMoveSecondary': 'function (target, source, move) {\n'
                                          '\t\t\tif (move.category === '
                                          "'Special') {\n"
                                          '\t\t\t\ttarget.eatItem();\n'
                                          '\t\t\t}\n'
                                          '\t\t}',
                  'onEat': 'function (pokemon) {\n'
                           '\t\t\tthis.boost({ spd: 1 });\n'
                           '\t\t}',
                  'spritenum': 597},
 'marshadiumz': {'gen': 7,
                 'isNonstandard': 'Past',
                 'itemUser': ['Marshadow'],
                 'name': 'Marshadium Z',
                 'num': 802,
                 'onTakeItem': False,
                 'spritenum': 654,
                 'zMove': 'Soul-Stealing 7-Star Strike',
                 'zMoveFrom': 'Spectral Thief'},
 'masterball': {'gen': 1,
                'isPokeball': True,
                'name': 'Master Ball',
                'num': 1,
                'spritenum': 276},
 'mawilite': {'gen': 6,
              'isNonstandard': 'Past',
              'itemUser': ['Mawile'],
              'megaEvolves': 'Mawile',
              'megaStone': 'Mawile-Mega',
              'name': 'Mawilite',
              'num': 681,
              'onTakeItem': 'function (item, source) {\n'
                            '\t\t\tif (item.megaEvolves === '
                            'source.baseSpecies.baseSpecies)\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 598},
 'meadowplate': {'forcedForme': 'Arceus-Grass',
                 'gen': 4,
                 'isNonstandard': 'Unobtainable',
                 'name': 'Meadow Plate',
                 'num': 301,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Grass') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onPlate': 'Grass',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 493) || pokemon.baseSpecies.num === 493) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 282},
 'medichamite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Medicham'],
                 'megaEvolves': 'Medicham',
                 'megaStone': 'Medicham-Mega',
                 'name': 'Medichamite',
                 'num': 665,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 599},
 'mentalherb': {'fling': {'basePower': 10,
                          'effect': 'function (pokemon) {\n'
                                    "\t\t\t\tvar conditions = ['attract', "
                                    "'taunt', 'encore', 'torment', 'disable', "
                                    "'healblock'];\n"
                                    '\t\t\t\tfor (var _i = 0, conditions_1 = '
                                    'conditions; _i < conditions_1.length; '
                                    '_i++) {\n'
                                    '\t\t\t\t\tvar firstCondition = '
                                    'conditions_1[_i];\n'
                                    '\t\t\t\t\tif '
                                    '(pokemon.volatiles[firstCondition]) {\n'
                                    '\t\t\t\t\t\tfor (var _a = 0, conditions_2 '
                                    '= conditions; _a < conditions_2.length; '
                                    '_a++) {\n'
                                    '\t\t\t\t\t\t\tvar secondCondition = '
                                    'conditions_2[_a];\n'
                                    '\t\t\t\t\t\t\t'
                                    'pokemon.removeVolatile(secondCondition);\n'
                                    '\t\t\t\t\t\t\tif (firstCondition === '
                                    "'attract' && secondCondition === "
                                    "'attract') {\n"
                                    "\t\t\t\t\t\t\t\tthis.add('-end', pokemon, "
                                    "'move: Attract', '[from] item: Mental "
                                    "Herb');\n"
                                    '\t\t\t\t\t\t\t}\n'
                                    '\t\t\t\t\t\t}\n'
                                    '\t\t\t\t\t\treturn;\n'
                                    '\t\t\t\t\t}\n'
                                    '\t\t\t\t}\n'
                                    '\t\t\t}'},
                'gen': 3,
                'name': 'Mental Herb',
                'num': 219,
                'onUpdate': 'function (pokemon) {\n'
                            "\t\t\tvar conditions = ['attract', 'taunt', "
                            "'encore', 'torment', 'disable', 'healblock'];\n"
                            '\t\t\tfor (var _i = 0, conditions_3 = conditions; '
                            '_i < conditions_3.length; _i++) {\n'
                            '\t\t\t\tvar firstCondition = conditions_3[_i];\n'
                            '\t\t\t\tif (pokemon.volatiles[firstCondition]) {\n'
                            '\t\t\t\t\tif (!pokemon.useItem())\n'
                            '\t\t\t\t\t\treturn;\n'
                            '\t\t\t\t\tfor (var _a = 0, conditions_4 = '
                            'conditions; _a < conditions_4.length; _a++) {\n'
                            '\t\t\t\t\t\tvar secondCondition = '
                            'conditions_4[_a];\n'
                            '\t\t\t\t\t\t'
                            'pokemon.removeVolatile(secondCondition);\n'
                            "\t\t\t\t\t\tif (firstCondition === 'attract' && "
                            "secondCondition === 'attract') {\n"
                            "\t\t\t\t\t\t\tthis.add('-end', pokemon, 'move: "
                            "Attract', '[from] item: Mental Herb');\n"
                            '\t\t\t\t\t\t}\n'
                            '\t\t\t\t\t}\n'
                            '\t\t\t\t\treturn;\n'
                            '\t\t\t\t}\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 285},
 'metagrossite': {'gen': 6,
                  'isNonstandard': 'Past',
                  'itemUser': ['Metagross'],
                  'megaEvolves': 'Metagross',
                  'megaStone': 'Metagross-Mega',
                  'name': 'Metagrossite',
                  'num': 758,
                  'onTakeItem': 'function (item, source) {\n'
                                '\t\t\tif (item.megaEvolves === '
                                'source.baseSpecies.baseSpecies)\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 618},
 'metalcoat': {'fling': {'basePower': 30},
               'gen': 2,
               'name': 'Metal Coat',
               'num': 233,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move.type === 'Steel') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'spritenum': 286},
 'metalpowder': {'fling': {'basePower': 10},
                 'gen': 2,
                 'itemUser': ['Ditto'],
                 'name': 'Metal Powder',
                 'num': 257,
                 'onModifyDef': 'function (def, pokemon) {\n'
                                "\t\t\tif (pokemon.species.name === 'Ditto' && "
                                '!pokemon.transformed) {\n'
                                '\t\t\t\treturn this.chainModify(2);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onModifyDefPriority': 2,
                 'spritenum': 287},
 'metronome': {'condition': {'onModifyDamage': 'function (damage, source, '
                                               'target, move) {\n'
                                               '\t\t\t\tvar dmgMod = [4096, '
                                               '4915, 5734, 6553, 7372, '
                                               '8192];\n'
                                               '\t\t\t\tvar numConsecutive = '
                                               'this.effectState.numConsecutive '
                                               '> 5 ? 5 : '
                                               'this.effectState.numConsecutive;\n'
                                               '\t\t\t\tthis.debug("Current '
                                               'Metronome boost: " + '
                                               'dmgMod[numConsecutive] + '
                                               '"/4096");\n'
                                               '\t\t\t\treturn '
                                               'this.chainModify([dmgMod[numConsecutive], '
                                               '4096]);\n'
                                               '\t\t\t}',
                             'onStart': 'function (pokemon) {\n'
                                        '\t\t\t\tthis.effectState.lastMove = '
                                        "'';\n"
                                        '\t\t\t\t'
                                        'this.effectState.numConsecutive = 0;\n'
                                        '\t\t\t}',
                             'onTryMove': 'function (pokemon, target, move) {\n'
                                          '\t\t\t\tif '
                                          "(!pokemon.hasItem('metronome')) {\n"
                                          '\t\t\t\t\t'
                                          "pokemon.removeVolatile('metronome');\n"
                                          '\t\t\t\t\treturn;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\tif '
                                          '(this.effectState.lastMove === '
                                          'move.id && '
                                          'pokemon.moveLastTurnResult) {\n'
                                          '\t\t\t\t\t'
                                          'this.effectState.numConsecutive++;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\telse if '
                                          "(pokemon.volatiles['twoturnmove'] "
                                          '&& this.effectState.lastMove !== '
                                          'move.id) {\n'
                                          '\t\t\t\t\t'
                                          'this.effectState.numConsecutive = '
                                          '1;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\telse {\n'
                                          '\t\t\t\t\t'
                                          'this.effectState.numConsecutive = '
                                          '0;\n'
                                          '\t\t\t\t}\n'
                                          '\t\t\t\tthis.effectState.lastMove = '
                                          'move.id;\n'
                                          '\t\t\t}',
                             'onTryMovePriority': -2},
               'fling': {'basePower': 30},
               'gen': 4,
               'name': 'Metronome',
               'num': 277,
               'onStart': 'function (pokemon) {\n'
                          "\t\t\tpokemon.addVolatile('metronome');\n"
                          '\t\t}',
               'spritenum': 289},
 'mewniumz': {'gen': 7,
              'isNonstandard': 'Past',
              'itemUser': ['Mew'],
              'name': 'Mewnium Z',
              'num': 806,
              'onTakeItem': False,
              'spritenum': 658,
              'zMove': 'Genesis Supernova',
              'zMoveFrom': 'Psychic'},
 'mewtwonitex': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Mewtwo'],
                 'megaEvolves': 'Mewtwo',
                 'megaStone': 'Mewtwo-Mega-X',
                 'name': 'Mewtwonite X',
                 'num': 662,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 600},
 'mewtwonitey': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Mewtwo'],
                 'megaEvolves': 'Mewtwo',
                 'megaStone': 'Mewtwo-Mega-Y',
                 'name': 'Mewtwonite Y',
                 'num': 663,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 601},
 'micleberry': {'condition': {'duration': 2,
                              'onSourceAccuracy': 'function (accuracy, target, '
                                                  'source, move) {\n'
                                                  '\t\t\t\tif (!move.ohko) {\n'
                                                  '\t\t\t\t\t'
                                                  "this.add('-enditem', "
                                                  "source, 'Micle Berry');\n"
                                                  '\t\t\t\t\t'
                                                  "source.removeVolatile('micleberry');\n"
                                                  '\t\t\t\t\tif (typeof '
                                                  "accuracy === 'number') {\n"
                                                  '\t\t\t\t\t\treturn '
                                                  'this.chainModify([4915, '
                                                  '4096]);\n'
                                                  '\t\t\t\t\t}\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t}'},
                'gen': 4,
                'isBerry': True,
                'name': 'Micle Berry',
                'naturalGift': {'basePower': 100, 'type': 'Rock'},
                'num': 209,
                'onEat': 'function (pokemon) {\n'
                         "\t\t\tpokemon.addVolatile('micleberry');\n"
                         '\t\t}',
                'onResidual': 'function (pokemon) {\n'
                              '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                              '(pokemon.hp <= pokemon.maxhp / 2 && '
                              "pokemon.hasAbility('gluttony'))) {\n"
                              '\t\t\t\tpokemon.eatItem();\n'
                              '\t\t\t}\n'
                              '\t\t}',
                'spritenum': 290},
 'mimikiumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Mimikyu',
                            'Mimikyu-Busted',
                            'Mimikyu-Totem',
                            'Mimikyu-Busted-Totem'],
               'name': 'Mimikium Z',
               'num': 924,
               'onTakeItem': False,
               'spritenum': 688,
               'zMove': "Let's Snuggle Forever",
               'zMoveFrom': 'Play Rough'},
 'mindplate': {'forcedForme': 'Arceus-Psychic',
               'gen': 4,
               'isNonstandard': 'Unobtainable',
               'name': 'Mind Plate',
               'num': 307,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move.type === 'Psychic') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'onPlate': 'Psychic',
               'onTakeItem': 'function (item, pokemon, source) {\n'
                             '\t\t\tif ((source && source.baseSpecies.num === '
                             '493) || pokemon.baseSpecies.num === 493) {\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\t}\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 291},
 'mintberry': {'gen': 2,
               'isBerry': True,
               'isNonstandard': 'Past',
               'name': 'Mint Berry',
               'naturalGift': {'basePower': 80, 'type': 'Water'},
               'num': 150,
               'onEat': 'function (pokemon) {\n'
                        "\t\t\tif (pokemon.status === 'slp') {\n"
                        '\t\t\t\tpokemon.cureStatus();\n'
                        '\t\t\t}\n'
                        '\t\t}',
               'onUpdate': 'function (pokemon) {\n'
                           "\t\t\tif (pokemon.status === 'slp') {\n"
                           '\t\t\t\tpokemon.eatItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 65},
 'miracleberry': {'gen': 2,
                  'isBerry': True,
                  'isNonstandard': 'Past',
                  'name': 'Miracle Berry',
                  'naturalGift': {'basePower': 80, 'type': 'Flying'},
                  'num': 157,
                  'onEat': 'function (pokemon) {\n'
                           '\t\t\tpokemon.cureStatus();\n'
                           "\t\t\tpokemon.removeVolatile('confusion');\n"
                           '\t\t}',
                  'onUpdate': 'function (pokemon) {\n'
                              '\t\t\tif (pokemon.status || '
                              "pokemon.volatiles['confusion']) {\n"
                              '\t\t\t\tpokemon.eatItem();\n'
                              '\t\t\t}\n'
                              '\t\t}',
                  'spritenum': 262},
 'miracleseed': {'fling': {'basePower': 30},
                 'gen': 2,
                 'name': 'Miracle Seed',
                 'num': 239,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Grass') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 292},
 'mistyseed': {'boosts': {'spd': 1},
               'fling': {'basePower': 10},
               'gen': 7,
               'name': 'Misty Seed',
               'num': 883,
               'onAnyTerrainStart': 'function () {\n'
                                    '\t\t\tvar pokemon = '
                                    'this.effectState.target;\n'
                                    '\t\t\tif '
                                    "(this.field.isTerrain('mistyterrain')) {\n"
                                    '\t\t\t\tpokemon.useItem();\n'
                                    '\t\t\t}\n'
                                    '\t\t}',
               'onStart': 'function (pokemon) {\n'
                          '\t\t\tif (!pokemon.ignoringItem() && '
                          "this.field.isTerrain('mistyterrain')) {\n"
                          '\t\t\t\tpokemon.useItem();\n'
                          '\t\t\t}\n'
                          '\t\t}',
               'spritenum': 666},
 'moonball': {'gen': 2,
              'isPokeball': True,
              'name': 'Moon Ball',
              'num': 498,
              'spritenum': 294},
 'moonstone': {'fling': {'basePower': 30},
               'gen': 1,
               'name': 'Moon Stone',
               'num': 81,
               'spritenum': 295},
 'muscleband': {'fling': {'basePower': 10},
                'gen': 4,
                'name': 'Muscle Band',
                'num': 266,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move.category === 'Physical') {\n"
                               '\t\t\t\treturn this.chainModify([4505, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 16,
                'spritenum': 297},
 'mysteryberry': {'gen': 2,
                  'isBerry': True,
                  'isNonstandard': 'Past',
                  'name': 'Mystery Berry',
                  'naturalGift': {'basePower': 80, 'type': 'Fighting'},
                  'num': 154,
                  'onEat': 'function (pokemon) {\n'
                           '\t\t\tvar moveSlot;\n'
                           "\t\t\tif (pokemon.volatiles['leppaberry']) {\n"
                           '\t\t\t\tmoveSlot = '
                           "pokemon.volatiles['leppaberry'].moveSlot;\n"
                           "\t\t\t\tpokemon.removeVolatile('leppaberry');\n"
                           '\t\t\t}\n'
                           '\t\t\telse {\n'
                           '\t\t\t\tvar pp = 99;\n'
                           '\t\t\t\tfor (var _i = 0, _a = pokemon.moveSlots; '
                           '_i < _a.length; _i++) {\n'
                           '\t\t\t\t\tvar possibleMoveSlot = _a[_i];\n'
                           '\t\t\t\t\tif (possibleMoveSlot.pp < pp) {\n'
                           '\t\t\t\t\t\tmoveSlot = possibleMoveSlot;\n'
                           '\t\t\t\t\t\tpp = moveSlot.pp;\n'
                           '\t\t\t\t\t}\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t\tmoveSlot.pp += 5;\n'
                           '\t\t\tif (moveSlot.pp > moveSlot.maxpp)\n'
                           '\t\t\t\tmoveSlot.pp = moveSlot.maxpp;\n'
                           "\t\t\tthis.add('-activate', pokemon, 'item: "
                           "Mystery Berry', moveSlot.move);\n"
                           '\t\t}',
                  'onUpdate': 'function (pokemon) {\n'
                              '\t\t\tif (!pokemon.hp)\n'
                              '\t\t\t\treturn;\n'
                              '\t\t\tvar moveSlot = pokemon.lastMove && '
                              'pokemon.getMoveData(pokemon.lastMove.id);\n'
                              '\t\t\tif (moveSlot && moveSlot.pp === 0) {\n'
                              "\t\t\t\tpokemon.addVolatile('leppaberry');\n"
                              '\t\t\t\t'
                              "pokemon.volatiles['leppaberry'].moveSlot = "
                              'moveSlot;\n'
                              '\t\t\t\tpokemon.eatItem();\n'
                              '\t\t\t}\n'
                              '\t\t}',
                  'spritenum': 244},
 'mysticwater': {'fling': {'basePower': 30},
                 'gen': 2,
                 'name': 'Mystic Water',
                 'num': 243,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Water') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 300},
 'nanabberry': {'gen': 3,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Nanab Berry',
                'naturalGift': {'basePower': 90, 'type': 'Water'},
                'num': 166,
                'onEat': False,
                'spritenum': 302},
 'nestball': {'gen': 3,
              'isPokeball': True,
              'name': 'Nest Ball',
              'num': 8,
              'spritenum': 303},
 'netball': {'gen': 3,
             'isPokeball': True,
             'name': 'Net Ball',
             'num': 6,
             'spritenum': 304},
 'nevermeltice': {'fling': {'basePower': 30},
                  'gen': 2,
                  'name': 'Never-Melt Ice',
                  'num': 246,
                  'onBasePower': 'function (basePower, user, target, move) {\n'
                                 "\t\t\tif (move.type === 'Ice') {\n"
                                 '\t\t\t\treturn this.chainModify([4915, '
                                 '4096]);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onBasePowerPriority': 15,
                  'spritenum': 305},
 'nomelberry': {'gen': 3,
                'isBerry': True,
                'isNonstandard': 'Past',
                'name': 'Nomel Berry',
                'naturalGift': {'basePower': 90, 'type': 'Dragon'},
                'num': 178,
                'onEat': False,
                'spritenum': 306},
 'normalgem': {'gen': 5,
               'isGem': True,
               'name': 'Normal Gem',
               'num': 564,
               'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                        "\t\t\tvar pledges = ['firepledge', "
                                        "'grasspledge', 'waterpledge'];\n"
                                        '\t\t\tif (target === source || '
                                        "move.category === 'Status' || "
                                        'pledges.includes(move.id))\n'
                                        '\t\t\t\treturn;\n'
                                        "\t\t\tif (move.type === 'Normal' && "
                                        'source.useItem()) {\n'
                                        "\t\t\t\tsource.addVolatile('gem');\n"
                                        '\t\t\t}\n'
                                        '\t\t}',
               'spritenum': 307},
 'normaliumz': {'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Normalium Z',
                'num': 776,
                'onTakeItem': False,
                'spritenum': 631,
                'zMove': True,
                'zMoveType': 'Normal'},
 'occaberry': {'gen': 4,
               'isBerry': True,
               'name': 'Occa Berry',
               'naturalGift': {'basePower': 80, 'type': 'Fire'},
               'num': 184,
               'onEat': 'function () { }',
               'onSourceModifyDamage': 'function (damage, source, target, '
                                       'move) {\n'
                                       "\t\t\tif (move.type === 'Fire' && "
                                       'target.getMoveHitData(move).typeMod > '
                                       '0) {\n'
                                       '\t\t\t\tvar hitSub = '
                                       "target.volatiles['substitute'] && "
                                       "!move.flags['authentic'] && "
                                       '!(move.infiltrates && this.gen >= 6);\n'
                                       '\t\t\t\tif (hitSub)\n'
                                       '\t\t\t\t\treturn;\n'
                                       '\t\t\t\tif (target.eatItem()) {\n'
                                       "\t\t\t\t\tthis.debug('-50% "
                                       "reduction');\n"
                                       "\t\t\t\t\tthis.add('-enditem', target, "
                                       "this.effect, '[weaken]');\n"
                                       '\t\t\t\t\treturn '
                                       'this.chainModify(0.5);\n'
                                       '\t\t\t\t}\n'
                                       '\t\t\t}\n'
                                       '\t\t}',
               'spritenum': 311},
 'oddincense': {'fling': {'basePower': 10},
                'gen': 4,
                'name': 'Odd Incense',
                'num': 314,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move.type === 'Psychic') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'spritenum': 312},
 'oldamber': {'fling': {'basePower': 100},
              'gen': 3,
              'isNonstandard': 'Past',
              'name': 'Old Amber',
              'num': 103,
              'spritenum': 314},
 'oranberry': {'gen': 3,
               'isBerry': True,
               'name': 'Oran Berry',
               'naturalGift': {'basePower': 80, 'type': 'Poison'},
               'num': 155,
               'onEat': 'function (pokemon) {\n\t\t\tthis.heal(10);\n\t\t}',
               'onTryEatItem': 'function (item, pokemon) {\n'
                               "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                               '\t\t\t\treturn false;\n'
                               '\t\t}',
               'onUpdate': 'function (pokemon) {\n'
                           '\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n'
                           '\t\t\t\tpokemon.eatItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 319},
 'ovalstone': {'fling': {'basePower': 80},
               'gen': 4,
               'name': 'Oval Stone',
               'num': 110,
               'spritenum': 321},
 'pamtreberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Pamtre Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Steel'},
                 'num': 180,
                 'onEat': False,
                 'spritenum': 323},
 'parkball': {'gen': 4,
              'isPokeball': True,
              'name': 'Park Ball',
              'num': 500,
              'spritenum': 325},
 'passhoberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Passho Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Water'},
                 'num': 185,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Water' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 329},
 'payapaberry': {'gen': 4,
                 'isBerry': True,
                 'name': 'Payapa Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Psychic'},
                 'num': 193,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Psychic' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 330},
 'pechaberry': {'gen': 3,
                'isBerry': True,
                'name': 'Pecha Berry',
                'naturalGift': {'basePower': 80, 'type': 'Electric'},
                'num': 151,
                'onEat': 'function (pokemon) {\n'
                         "\t\t\tif (pokemon.status === 'psn' || pokemon.status "
                         "=== 'tox') {\n"
                         '\t\t\t\tpokemon.cureStatus();\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.status === 'psn' || "
                            "pokemon.status === 'tox') {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 333},
 'persimberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Persim Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Ground'},
                 'num': 156,
                 'onEat': 'function (pokemon) {\n'
                          "\t\t\tpokemon.removeVolatile('confusion');\n"
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             "\t\t\tif (pokemon.volatiles['confusion']) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 334},
 'petayaberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Petaya Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Poison'},
                 'num': 204,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.boost({ spa: 1 });\n'
                          '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                             '(pokemon.hp <= pokemon.maxhp / 2 && '
                             "pokemon.hasAbility('gluttony'))) {\n"
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 335},
 'pidgeotite': {'gen': 6,
                'isNonstandard': 'Past',
                'itemUser': ['Pidgeot'],
                'megaEvolves': 'Pidgeot',
                'megaStone': 'Pidgeot-Mega',
                'name': 'Pidgeotite',
                'num': 762,
                'onTakeItem': 'function (item, source) {\n'
                              '\t\t\tif (item.megaEvolves === '
                              'source.baseSpecies.baseSpecies)\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 622},
 'pikaniumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Pikachu'],
               'name': 'Pikanium Z',
               'num': 794,
               'onTakeItem': False,
               'spritenum': 649,
               'zMove': 'Catastropika',
               'zMoveFrom': 'Volt Tackle'},
 'pikashuniumz': {'gen': 7,
                  'isNonstandard': 'Past',
                  'itemUser': ['Pikachu-Original',
                               'Pikachu-Hoenn',
                               'Pikachu-Sinnoh',
                               'Pikachu-Unova',
                               'Pikachu-Kalos',
                               'Pikachu-Alola',
                               'Pikachu-Partner'],
                  'name': 'Pikashunium Z',
                  'num': 836,
                  'onTakeItem': False,
                  'spritenum': 659,
                  'zMove': '10,000,000 Volt Thunderbolt',
                  'zMoveFrom': 'Thunderbolt'},
 'pinapberry': {'gen': 3,
                'isBerry': True,
                'name': 'Pinap Berry',
                'naturalGift': {'basePower': 90, 'type': 'Grass'},
                'num': 168,
                'onEat': False,
                'spritenum': 337},
 'pinkbow': {'gen': 2,
             'isNonstandard': 'Past',
             'name': 'Pink Bow',
             'num': 251,
             'onBasePower': 'function (basePower, user, target, move) {\n'
                            "\t\t\tif (move.type === 'Normal') {\n"
                            '\t\t\t\treturn basePower * 1.1;\n'
                            '\t\t\t}\n'
                            '\t\t}',
             'spritenum': 444},
 'pinsirite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Pinsir'],
               'megaEvolves': 'Pinsir',
               'megaStone': 'Pinsir-Mega',
               'name': 'Pinsirite',
               'num': 671,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 602},
 'pixieplate': {'forcedForme': 'Arceus-Fairy',
                'gen': 6,
                'name': 'Pixie Plate',
                'num': 644,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Fairy') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Fairy',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 610},
 'plumefossil': {'fling': {'basePower': 100},
                 'gen': 5,
                 'isNonstandard': 'Past',
                 'name': 'Plume Fossil',
                 'num': 573,
                 'spritenum': 339},
 'poisonbarb': {'fling': {'basePower': 70, 'status': 'psn'},
                'gen': 2,
                'name': 'Poison Barb',
                'num': 245,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move.type === 'Poison') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'spritenum': 343},
 'poisongem': {'gen': 5,
               'isGem': True,
               'isNonstandard': 'Past',
               'name': 'Poison Gem',
               'num': 554,
               'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                        '\t\t\tif (target === source || '
                                        "move.category === 'Status')\n"
                                        '\t\t\t\treturn;\n'
                                        "\t\t\tif (move.type === 'Poison' && "
                                        'source.useItem()) {\n'
                                        "\t\t\t\tsource.addVolatile('gem');\n"
                                        '\t\t\t}\n'
                                        '\t\t}',
               'spritenum': 344},
 'poisoniumz': {'forcedForme': 'Arceus-Poison',
                'gen': 7,
                'isNonstandard': 'Past',
                'name': 'Poisonium Z',
                'num': 783,
                'onPlate': 'Poison',
                'onTakeItem': False,
                'spritenum': 638,
                'zMove': True,
                'zMoveType': 'Poison'},
 'poisonmemory': {'forcedForme': 'Silvally-Poison',
                  'gen': 7,
                  'itemUser': ['Silvally-Poison'],
                  'name': 'Poison Memory',
                  'num': 906,
                  'onMemory': 'Poison',
                  'onTakeItem': 'function (item, pokemon, source) {\n'
                                '\t\t\tif ((source && source.baseSpecies.num '
                                '=== 773) || pokemon.baseSpecies.num === 773) '
                                '{\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 670},
 'pokeball': {'gen': 1,
              'isPokeball': True,
              'name': 'Poke Ball',
              'num': 4,
              'spritenum': 345},
 'polkadotbow': {'gen': 2,
                 'isNonstandard': 'Past',
                 'name': 'Polkadot Bow',
                 'num': 251,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Normal') {\n"
                                '\t\t\t\treturn basePower * 1.1;\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'spritenum': 444},
 'pomegberry': {'gen': 3,
                'isBerry': True,
                'name': 'Pomeg Berry',
                'naturalGift': {'basePower': 90, 'type': 'Ice'},
                'num': 169,
                'onEat': False,
                'spritenum': 351},
 'poweranklet': {'fling': {'basePower': 70},
                 'gen': 4,
                 'ignoreKlutz': True,
                 'name': 'Power Anklet',
                 'num': 293,
                 'onModifySpe': 'function (spe) {\n'
                                '\t\t\treturn this.chainModify(0.5);\n'
                                '\t\t}',
                 'spritenum': 354},
 'powerband': {'fling': {'basePower': 70},
               'gen': 4,
               'ignoreKlutz': True,
               'name': 'Power Band',
               'num': 292,
               'onModifySpe': 'function (spe) {\n'
                              '\t\t\treturn this.chainModify(0.5);\n'
                              '\t\t}',
               'spritenum': 355},
 'powerbelt': {'fling': {'basePower': 70},
               'gen': 4,
               'ignoreKlutz': True,
               'name': 'Power Belt',
               'num': 290,
               'onModifySpe': 'function (spe) {\n'
                              '\t\t\treturn this.chainModify(0.5);\n'
                              '\t\t}',
               'spritenum': 356},
 'powerbracer': {'fling': {'basePower': 70},
                 'gen': 4,
                 'ignoreKlutz': True,
                 'name': 'Power Bracer',
                 'num': 289,
                 'onModifySpe': 'function (spe) {\n'
                                '\t\t\treturn this.chainModify(0.5);\n'
                                '\t\t}',
                 'spritenum': 357},
 'powerherb': {'fling': {'basePower': 10},
               'gen': 4,
               'name': 'Power Herb',
               'num': 271,
               'onChargeMove': 'function (pokemon, target, move) {\n'
                               '\t\t\tif (pokemon.useItem()) {\n'
                               "\t\t\t\tthis.debug('power herb - remove charge "
                               "turn for ' + move.id);\n"
                               "\t\t\t\tthis.attrLastMove('[still]');\n"
                               "\t\t\t\tthis.addMove('-anim', pokemon, "
                               'move.name, target);\n'
                               '\t\t\t\treturn false; // skip charge turn\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'spritenum': 358},
 'powerlens': {'fling': {'basePower': 70},
               'gen': 4,
               'ignoreKlutz': True,
               'name': 'Power Lens',
               'num': 291,
               'onModifySpe': 'function (spe) {\n'
                              '\t\t\treturn this.chainModify(0.5);\n'
                              '\t\t}',
               'spritenum': 359},
 'powerweight': {'fling': {'basePower': 70},
                 'gen': 4,
                 'ignoreKlutz': True,
                 'name': 'Power Weight',
                 'num': 294,
                 'onModifySpe': 'function (spe) {\n'
                                '\t\t\treturn this.chainModify(0.5);\n'
                                '\t\t}',
                 'spritenum': 360},
 'premierball': {'gen': 3,
                 'isPokeball': True,
                 'name': 'Premier Ball',
                 'num': 12,
                 'spritenum': 363},
 'primariumz': {'gen': 7,
                'isNonstandard': 'Past',
                'itemUser': ['Primarina'],
                'name': 'Primarium Z',
                'num': 800,
                'onTakeItem': False,
                'spritenum': 652,
                'zMove': 'Oceanic Operetta',
                'zMoveFrom': 'Sparkling Aria'},
 'prismscale': {'fling': {'basePower': 30},
                'gen': 5,
                'name': 'Prism Scale',
                'num': 537,
                'spritenum': 365},
 'protectivepads': {'fling': {'basePower': 30},
                    'gen': 7,
                    'name': 'Protective Pads',
                    'num': 880,
                    'spritenum': 663},
 'protector': {'fling': {'basePower': 80},
               'gen': 4,
               'name': 'Protector',
               'num': 321,
               'spritenum': 367},
 'przcureberry': {'gen': 2,
                  'isBerry': True,
                  'isNonstandard': 'Past',
                  'name': 'PRZ Cure Berry',
                  'naturalGift': {'basePower': 80, 'type': 'Fire'},
                  'num': 149,
                  'onEat': 'function (pokemon) {\n'
                           "\t\t\tif (pokemon.status === 'par') {\n"
                           '\t\t\t\tpokemon.cureStatus();\n'
                           '\t\t\t}\n'
                           '\t\t}',
                  'onUpdate': 'function (pokemon) {\n'
                              "\t\t\tif (pokemon.status === 'par') {\n"
                              '\t\t\t\tpokemon.eatItem();\n'
                              '\t\t\t}\n'
                              '\t\t}',
                  'spritenum': 63},
 'psncureberry': {'gen': 2,
                  'isBerry': True,
                  'isNonstandard': 'Past',
                  'name': 'PSN Cure Berry',
                  'naturalGift': {'basePower': 80, 'type': 'Electric'},
                  'num': 151,
                  'onEat': 'function (pokemon) {\n'
                           "\t\t\tif (pokemon.status === 'psn' || "
                           "pokemon.status === 'tox') {\n"
                           '\t\t\t\tpokemon.cureStatus();\n'
                           '\t\t\t}\n'
                           '\t\t}',
                  'onUpdate': 'function (pokemon) {\n'
                              "\t\t\tif (pokemon.status === 'psn' || "
                              "pokemon.status === 'tox') {\n"
                              '\t\t\t\tpokemon.eatItem();\n'
                              '\t\t\t}\n'
                              '\t\t}',
                  'spritenum': 333},
 'psychicgem': {'gen': 5,
                'isGem': True,
                'isNonstandard': 'Past',
                'name': 'Psychic Gem',
                'num': 557,
                'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                         '\t\t\tif (target === source || '
                                         "move.category === 'Status')\n"
                                         '\t\t\t\treturn;\n'
                                         "\t\t\tif (move.type === 'Psychic' && "
                                         'source.useItem()) {\n'
                                         "\t\t\t\tsource.addVolatile('gem');\n"
                                         '\t\t\t}\n'
                                         '\t\t}',
                'spritenum': 369},
 'psychicmemory': {'forcedForme': 'Silvally-Psychic',
                   'gen': 7,
                   'itemUser': ['Silvally-Psychic'],
                   'name': 'Psychic Memory',
                   'num': 916,
                   'onMemory': 'Psychic',
                   'onTakeItem': 'function (item, pokemon, source) {\n'
                                 '\t\t\tif ((source && source.baseSpecies.num '
                                 '=== 773) || pokemon.baseSpecies.num === 773) '
                                 '{\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t\t}\n'
                                 '\t\t\treturn true;\n'
                                 '\t\t}',
                   'spritenum': 680},
 'psychicseed': {'boosts': {'spd': 1},
                 'fling': {'basePower': 10},
                 'gen': 7,
                 'name': 'Psychic Seed',
                 'num': 882,
                 'onAnyTerrainStart': 'function () {\n'
                                      '\t\t\tvar pokemon = '
                                      'this.effectState.target;\n'
                                      '\t\t\tif '
                                      "(this.field.isTerrain('psychicterrain')) "
                                      '{\n'
                                      '\t\t\t\tpokemon.useItem();\n'
                                      '\t\t\t}\n'
                                      '\t\t}',
                 'onStart': 'function (pokemon) {\n'
                            '\t\t\tif (!pokemon.ignoringItem() && '
                            "this.field.isTerrain('psychicterrain')) {\n"
                            '\t\t\t\tpokemon.useItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                 'spritenum': 665},
 'psychiumz': {'forcedForme': 'Arceus-Psychic',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Psychium Z',
               'num': 786,
               'onPlate': 'Psychic',
               'onTakeItem': False,
               'spritenum': 641,
               'zMove': True,
               'zMoveType': 'Psychic'},
 'qualotberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Qualot Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Poison'},
                 'num': 171,
                 'onEat': False,
                 'spritenum': 371},
 'quickball': {'gen': 4,
               'isPokeball': True,
               'name': 'Quick Ball',
               'num': 15,
               'spritenum': 372},
 'quickclaw': {'fling': {'basePower': 80},
               'gen': 2,
               'name': 'Quick Claw',
               'num': 217,
               'onFractionalPriority': 'function (priority, pokemon) {\n'
                                       '\t\t\tif (priority <= 0 && '
                                       'this.randomChance(1, 5)) {\n'
                                       "\t\t\t\tthis.add('-activate', pokemon, "
                                       "'item: Quick Claw');\n"
                                       '\t\t\t\treturn 0.1;\n'
                                       '\t\t\t}\n'
                                       '\t\t}',
               'onFractionalPriorityPriority': -2,
               'spritenum': 373},
 'quickpowder': {'fling': {'basePower': 10},
                 'gen': 4,
                 'itemUser': ['Ditto'],
                 'name': 'Quick Powder',
                 'num': 274,
                 'onModifySpe': 'function (spe, pokemon) {\n'
                                "\t\t\tif (pokemon.species.name === 'Ditto' && "
                                '!pokemon.transformed) {\n'
                                '\t\t\t\treturn this.chainModify(2);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'spritenum': 374},
 'rabutaberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Rabuta Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Ghost'},
                 'num': 177,
                 'onEat': False,
                 'spritenum': 375},
 'rarebone': {'fling': {'basePower': 100},
              'gen': 4,
              'name': 'Rare Bone',
              'num': 106,
              'spritenum': 379},
 'rawstberry': {'gen': 3,
                'isBerry': True,
                'name': 'Rawst Berry',
                'naturalGift': {'basePower': 80, 'type': 'Grass'},
                'num': 152,
                'onEat': 'function (pokemon) {\n'
                         "\t\t\tif (pokemon.status === 'brn') {\n"
                         '\t\t\t\tpokemon.cureStatus();\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            "\t\t\tif (pokemon.status === 'brn') {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 381},
 'razorclaw': {'fling': {'basePower': 80},
               'gen': 4,
               'name': 'Razor Claw',
               'num': 326,
               'onModifyCritRatio': 'function (critRatio) {\n'
                                    '\t\t\treturn critRatio + 1;\n'
                                    '\t\t}',
               'spritenum': 382},
 'razorfang': {'fling': {'basePower': 30, 'volatileStatus': 'flinch'},
               'gen': 4,
               'isNonstandard': 'Past',
               'name': 'Razor Fang',
               'num': 327,
               'onModifyMove': 'function (move) {\n'
                               '\t\t\tif (move.category !== "Status") {\n'
                               '\t\t\t\tif (!move.secondaries)\n'
                               '\t\t\t\t\tmove.secondaries = [];\n'
                               '\t\t\t\tfor (var _i = 0, _a = '
                               'move.secondaries; _i < _a.length; _i++) {\n'
                               '\t\t\t\t\tvar secondary = _a[_i];\n'
                               '\t\t\t\t\tif (secondary.volatileStatus === '
                               "'flinch')\n"
                               '\t\t\t\t\t\treturn;\n'
                               '\t\t\t\t}\n'
                               '\t\t\t\tmove.secondaries.push({\n'
                               '\t\t\t\t\tchance: 10,\n'
                               "\t\t\t\t\tvolatileStatus: 'flinch',\n"
                               '\t\t\t\t});\n'
                               '\t\t\t}\n'
                               '\t\t}',
               'onModifyMovePriority': -1,
               'spritenum': 383},
 'razzberry': {'gen': 3,
               'isBerry': True,
               'isNonstandard': 'Past',
               'name': 'Razz Berry',
               'naturalGift': {'basePower': 80, 'type': 'Steel'},
               'num': 164,
               'onEat': False,
               'spritenum': 384},
 'reapercloth': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Reaper Cloth',
                 'num': 325,
                 'spritenum': 385},
 'redcard': {'fling': {'basePower': 10},
             'gen': 5,
             'name': 'Red Card',
             'num': 542,
             'onAfterMoveSecondary': 'function (target, source, move) {\n'
                                     '\t\t\tif (source && source !== target && '
                                     'source.hp && target.hp && move && '
                                     "move.category !== 'Status') {\n"
                                     '\t\t\t\tif (!source.isActive || '
                                     '!this.canSwitch(source.side) || '
                                     'source.forceSwitchFlag || '
                                     'target.forceSwitchFlag) {\n'
                                     '\t\t\t\t\treturn;\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t\t// The item is used up even '
                                     'against a pokemon with Ingrain or that '
                                     "otherwise can't be forced out\n"
                                     '\t\t\t\tif (target.useItem(source)) {\n'
                                     "\t\t\t\t\tif (this.runEvent('DragOut', "
                                     'source, target, move)) {\n'
                                     '\t\t\t\t\t\tsource.forceSwitchFlag = '
                                     'true;\n'
                                     '\t\t\t\t\t}\n'
                                     '\t\t\t\t}\n'
                                     '\t\t\t}\n'
                                     '\t\t}',
             'spritenum': 387},
 'redorb': {'gen': 6,
            'isNonstandard': 'Past',
            'itemUser': ['Groudon'],
            'name': 'Red Orb',
            'num': 534,
            'onPrimal': 'function (pokemon) {\n'
                        "\t\t\tpokemon.formeChange('Groudon-Primal', "
                        'this.effect, true);\n'
                        '\t\t}',
            'onSwitchIn': 'function (pokemon) {\n'
                          '\t\t\tif (pokemon.isActive && '
                          "pokemon.baseSpecies.name === 'Groudon') {\n"
                          '\t\t\t\tthis.queue.insertChoice({ choice: '
                          "'runPrimal', pokemon: pokemon });\n"
                          '\t\t\t}\n'
                          '\t\t}',
            'onTakeItem': 'function (item, source) {\n'
                          '\t\t\tif (source.baseSpecies.baseSpecies === '
                          "'Groudon')\n"
                          '\t\t\t\treturn false;\n'
                          '\t\t\treturn true;\n'
                          '\t\t}',
            'spritenum': 390},
 'repeatball': {'gen': 3,
                'isPokeball': True,
                'name': 'Repeat Ball',
                'num': 9,
                'spritenum': 401},
 'ribbonsweet': {'fling': {'basePower': 10},
                 'gen': 8,
                 'name': 'Ribbon Sweet',
                 'num': 1115,
                 'spritenum': 710},
 'rindoberry': {'gen': 4,
                'isBerry': True,
                'name': 'Rindo Berry',
                'naturalGift': {'basePower': 80, 'type': 'Grass'},
                'num': 187,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Grass' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 409},
 'ringtarget': {'fling': {'basePower': 10},
                'gen': 5,
                'name': 'Ring Target',
                'num': 543,
                'onNegateImmunity': False,
                'spritenum': 410},
 'rockgem': {'gen': 5,
             'isGem': True,
             'isNonstandard': 'Past',
             'name': 'Rock Gem',
             'num': 559,
             'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                      '\t\t\tif (target === source || '
                                      "move.category === 'Status')\n"
                                      '\t\t\t\treturn;\n'
                                      "\t\t\tif (move.type === 'Rock' && "
                                      'source.useItem()) {\n'
                                      "\t\t\t\tsource.addVolatile('gem');\n"
                                      '\t\t\t}\n'
                                      '\t\t}',
             'spritenum': 415},
 'rockincense': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Rock Incense',
                 'num': 315,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Rock') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 416},
 'rockiumz': {'forcedForme': 'Arceus-Rock',
              'gen': 7,
              'isNonstandard': 'Past',
              'name': 'Rockium Z',
              'num': 788,
              'onPlate': 'Rock',
              'onTakeItem': False,
              'spritenum': 643,
              'zMove': True,
              'zMoveType': 'Rock'},
 'rockmemory': {'forcedForme': 'Silvally-Rock',
                'gen': 7,
                'itemUser': ['Silvally-Rock'],
                'name': 'Rock Memory',
                'num': 908,
                'onMemory': 'Rock',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '773) || pokemon.baseSpecies.num === 773) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 672},
 'rockyhelmet': {'fling': {'basePower': 60},
                 'gen': 5,
                 'name': 'Rocky Helmet',
                 'num': 540,
                 'onDamagingHit': 'function (damage, target, source, move) {\n'
                                  '\t\t\tif (this.checkMoveMakesContact(move, '
                                  'source, target)) {\n'
                                  '\t\t\t\tthis.damage(source.baseMaxhp / 6, '
                                  'source, target);\n'
                                  '\t\t\t}\n'
                                  '\t\t}',
                 'onDamagingHitOrder': 2,
                 'spritenum': 417},
 'roomservice': {'boosts': {'spe': -1},
                 'fling': {'basePower': 100},
                 'gen': 8,
                 'name': 'Room Service',
                 'num': 1122,
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif '
                             "(this.field.getPseudoWeather('trickroom')) {\n"
                             '\t\t\t\tpokemon.useItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 717},
 'rootfossil': {'fling': {'basePower': 100},
                'gen': 3,
                'isNonstandard': 'Past',
                'name': 'Root Fossil',
                'num': 99,
                'spritenum': 418},
 'roseincense': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Rose Incense',
                 'num': 318,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Grass') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 419},
 'roseliberry': {'gen': 6,
                 'isBerry': True,
                 'name': 'Roseli Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Fairy'},
                 'num': 686,
                 'onEat': 'function () { }',
                 'onSourceModifyDamage': 'function (damage, source, target, '
                                         'move) {\n'
                                         "\t\t\tif (move.type === 'Fairy' && "
                                         'target.getMoveHitData(move).typeMod '
                                         '> 0) {\n'
                                         '\t\t\t\tvar hitSub = '
                                         "target.volatiles['substitute'] && "
                                         "!move.flags['authentic'] && "
                                         '!(move.infiltrates && this.gen >= '
                                         '6);\n'
                                         '\t\t\t\tif (hitSub)\n'
                                         '\t\t\t\t\treturn;\n'
                                         '\t\t\t\tif (target.eatItem()) {\n'
                                         "\t\t\t\t\tthis.debug('-50% "
                                         "reduction');\n"
                                         "\t\t\t\t\tthis.add('-enditem', "
                                         "target, this.effect, '[weaken]');\n"
                                         '\t\t\t\t\treturn '
                                         'this.chainModify(0.5);\n'
                                         '\t\t\t\t}\n'
                                         '\t\t\t}\n'
                                         '\t\t}',
                 'spritenum': 603},
 'rowapberry': {'gen': 4,
                'isBerry': True,
                'name': 'Rowap Berry',
                'naturalGift': {'basePower': 100, 'type': 'Dark'},
                'num': 212,
                'onDamagingHit': 'function (damage, target, source, move) {\n'
                                 "\t\t\tif (move.category === 'Special' && "
                                 'source.hp && source.isActive) {\n'
                                 '\t\t\t\tif (target.eatItem()) {\n'
                                 '\t\t\t\t\tthis.damage(source.baseMaxhp / '
                                 "(target.hasAbility('ripen') ? 4 : 8), "
                                 'source, target);\n'
                                 '\t\t\t\t}\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                'onEat': 'function () { }',
                'spritenum': 420},
 'rustedshield': {'forcedForme': 'Zamazenta-Crowned',
                  'gen': 8,
                  'itemUser': ['Zamazenta-Crowned'],
                  'name': 'Rusted Shield',
                  'num': 1104,
                  'onTakeItem': 'function (item, pokemon, source) {\n'
                                '\t\t\tif ((source && source.baseSpecies.num '
                                '=== 889) || pokemon.baseSpecies.num === 889) '
                                '{\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\t}\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 699},
 'rustedsword': {'forcedForme': 'Zacian-Crowned',
                 'gen': 8,
                 'itemUser': ['Zacian-Crowned'],
                 'name': 'Rusted Sword',
                 'num': 1103,
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 888) || pokemon.baseSpecies.num === 888) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 698},
 'sablenite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Sableye'],
               'megaEvolves': 'Sableye',
               'megaStone': 'Sableye-Mega',
               'name': 'Sablenite',
               'num': 754,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 614},
 'sachet': {'fling': {'basePower': 80},
            'gen': 6,
            'name': 'Sachet',
            'num': 647,
            'spritenum': 691},
 'safariball': {'gen': 1,
                'isPokeball': True,
                'name': 'Safari Ball',
                'num': 5,
                'spritenum': 425},
 'safetygoggles': {'fling': {'basePower': 80},
                   'gen': 6,
                   'name': 'Safety Goggles',
                   'num': 650,
                   'onImmunity': 'function (type, pokemon) {\n'
                                 "\t\t\tif (type === 'sandstorm' || type === "
                                 "'hail' || type === 'powder')\n"
                                 '\t\t\t\treturn false;\n'
                                 '\t\t}',
                   'onTryHit': 'function (pokemon, source, move) {\n'
                               "\t\t\tif (move.flags['powder'] && pokemon !== "
                               "source && this.dex.getImmunity('powder', "
                               'pokemon)) {\n'
                               "\t\t\t\tthis.add('-activate', pokemon, 'item: "
                               "Safety Goggles', move.name);\n"
                               '\t\t\t\treturn null;\n'
                               '\t\t\t}\n'
                               '\t\t}',
                   'spritenum': 604},
 'sailfossil': {'fling': {'basePower': 100},
                'gen': 6,
                'isNonstandard': 'Past',
                'name': 'Sail Fossil',
                'num': 711,
                'spritenum': 695},
 'salacberry': {'gen': 3,
                'isBerry': True,
                'name': 'Salac Berry',
                'naturalGift': {'basePower': 100, 'type': 'Fighting'},
                'num': 203,
                'onEat': 'function (pokemon) {\n'
                         '\t\t\tthis.boost({ spe: 1 });\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                            '(pokemon.hp <= pokemon.maxhp / 2 && '
                            "pokemon.hasAbility('gluttony'))) {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 426},
 'salamencite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Salamence'],
                 'megaEvolves': 'Salamence',
                 'megaStone': 'Salamence-Mega',
                 'name': 'Salamencite',
                 'num': 769,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 627},
 'sceptilite': {'gen': 6,
                'isNonstandard': 'Past',
                'itemUser': ['Sceptile'],
                'megaEvolves': 'Sceptile',
                'megaStone': 'Sceptile-Mega',
                'name': 'Sceptilite',
                'num': 753,
                'onTakeItem': 'function (item, source) {\n'
                              '\t\t\tif (item.megaEvolves === '
                              'source.baseSpecies.baseSpecies)\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 613},
 'scizorite': {'gen': 6,
               'isNonstandard': 'Past',
               'itemUser': ['Scizor'],
               'megaEvolves': 'Scizor',
               'megaStone': 'Scizor-Mega',
               'name': 'Scizorite',
               'num': 670,
               'onTakeItem': 'function (item, source) {\n'
                             '\t\t\tif (item.megaEvolves === '
                             'source.baseSpecies.baseSpecies)\n'
                             '\t\t\t\treturn false;\n'
                             '\t\t\treturn true;\n'
                             '\t\t}',
               'spritenum': 605},
 'scopelens': {'fling': {'basePower': 30},
               'gen': 2,
               'name': 'Scope Lens',
               'num': 232,
               'onModifyCritRatio': 'function (critRatio) {\n'
                                    '\t\t\treturn critRatio + 1;\n'
                                    '\t\t}',
               'spritenum': 429},
 'seaincense': {'fling': {'basePower': 10},
                'gen': 3,
                'name': 'Sea Incense',
                'num': 254,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move && move.type === 'Water') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'spritenum': 430},
 'sharpbeak': {'fling': {'basePower': 50},
               'gen': 2,
               'name': 'Sharp Beak',
               'num': 244,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move && move.type === 'Flying') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'spritenum': 436},
 'sharpedonite': {'gen': 6,
                  'isNonstandard': 'Past',
                  'itemUser': ['Sharpedo'],
                  'megaEvolves': 'Sharpedo',
                  'megaStone': 'Sharpedo-Mega',
                  'name': 'Sharpedonite',
                  'num': 759,
                  'onTakeItem': 'function (item, source) {\n'
                                '\t\t\tif (item.megaEvolves === '
                                'source.baseSpecies.baseSpecies)\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 619},
 'shedshell': {'fling': {'basePower': 10},
               'gen': 4,
               'name': 'Shed Shell',
               'num': 295,
               'onTrapPokemon': 'function (pokemon) {\n'
                                '\t\t\tpokemon.trapped = pokemon.maybeTrapped '
                                '= false;\n'
                                '\t\t}',
               'onTrapPokemonPriority': -10,
               'spritenum': 437},
 'shellbell': {'fling': {'basePower': 30},
               'gen': 3,
               'name': 'Shell Bell',
               'num': 253,
               'onAfterMoveSecondarySelf': 'function (pokemon, target, move) '
                                           '{\n'
                                           '\t\t\tif (move.totalDamage) {\n'
                                           '\t\t\t\tthis.heal(move.totalDamage '
                                           '/ 8, pokemon);\n'
                                           '\t\t\t}\n'
                                           '\t\t}',
               'onAfterMoveSecondarySelfPriority': -1,
               'spritenum': 438},
 'shinystone': {'fling': {'basePower': 80},
                'gen': 4,
                'name': 'Shiny Stone',
                'num': 107,
                'spritenum': 439},
 'shockdrive': {'forcedForme': 'Genesect-Shock',
                'gen': 5,
                'itemUser': ['Genesect-Shock'],
                'name': 'Shock Drive',
                'num': 117,
                'onDrive': 'Electric',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '649) || pokemon.baseSpecies.num === 649) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 442},
 'shucaberry': {'gen': 4,
                'isBerry': True,
                'name': 'Shuca Berry',
                'naturalGift': {'basePower': 80, 'type': 'Ground'},
                'num': 191,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Ground' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 443},
 'silkscarf': {'fling': {'basePower': 10},
               'gen': 3,
               'name': 'Silk Scarf',
               'num': 251,
               'onBasePower': 'function (basePower, user, target, move) {\n'
                              "\t\t\tif (move.type === 'Normal') {\n"
                              '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onBasePowerPriority': 15,
               'spritenum': 444},
 'silverpowder': {'fling': {'basePower': 10},
                  'gen': 2,
                  'name': 'Silver Powder',
                  'num': 222,
                  'onBasePower': 'function (basePower, user, target, move) {\n'
                                 "\t\t\tif (move.type === 'Bug') {\n"
                                 '\t\t\t\treturn this.chainModify([4915, '
                                 '4096]);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onBasePowerPriority': 15,
                  'spritenum': 447},
 'sitrusberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Sitrus Berry',
                 'naturalGift': {'basePower': 80, 'type': 'Psychic'},
                 'num': 158,
                 'onEat': 'function (pokemon) {\n'
                          '\t\t\tthis.heal(pokemon.baseMaxhp / 4);\n'
                          '\t\t}',
                 'onTryEatItem': 'function (item, pokemon) {\n'
                                 "\t\t\tif (!this.runEvent('TryHeal', "
                                 'pokemon))\n'
                                 '\t\t\t\treturn false;\n'
                                 '\t\t}',
                 'onUpdate': 'function (pokemon) {\n'
                             '\t\t\tif (pokemon.hp <= pokemon.maxhp / 2) {\n'
                             '\t\t\t\tpokemon.eatItem();\n'
                             '\t\t\t}\n'
                             '\t\t}',
                 'spritenum': 448},
 'skullfossil': {'fling': {'basePower': 100},
                 'gen': 4,
                 'isNonstandard': 'Past',
                 'name': 'Skull Fossil',
                 'num': 105,
                 'spritenum': 449},
 'skyplate': {'forcedForme': 'Arceus-Flying',
              'gen': 4,
              'isNonstandard': 'Unobtainable',
              'name': 'Sky Plate',
              'num': 306,
              'onBasePower': 'function (basePower, user, target, move) {\n'
                             "\t\t\tif (move.type === 'Flying') {\n"
                             '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onBasePowerPriority': 15,
              'onPlate': 'Flying',
              'onTakeItem': 'function (item, pokemon, source) {\n'
                            '\t\t\tif ((source && source.baseSpecies.num === '
                            '493) || pokemon.baseSpecies.num === 493) {\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 450},
 'slowbronite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Slowbro'],
                 'megaEvolves': 'Slowbro',
                 'megaStone': 'Slowbro-Mega',
                 'name': 'Slowbronite',
                 'num': 760,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 620},
 'smoothrock': {'fling': {'basePower': 10},
                'gen': 4,
                'name': 'Smooth Rock',
                'num': 283,
                'spritenum': 453},
 'snorliumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Snorlax'],
               'name': 'Snorlium Z',
               'num': 804,
               'onTakeItem': False,
               'spritenum': 656,
               'zMove': 'Pulverizing Pancake',
               'zMoveFrom': 'Giga Impact'},
 'snowball': {'boosts': {'atk': 1},
              'fling': {'basePower': 30},
              'gen': 6,
              'name': 'Snowball',
              'num': 649,
              'onDamagingHit': 'function (damage, target, source, move) {\n'
                               "\t\t\tif (move.type === 'Ice') {\n"
                               '\t\t\t\ttarget.useItem();\n'
                               '\t\t\t}\n'
                               '\t\t}',
              'spritenum': 606},
 'softsand': {'fling': {'basePower': 10},
              'gen': 2,
              'name': 'Soft Sand',
              'num': 237,
              'onBasePower': 'function (basePower, user, target, move) {\n'
                             "\t\t\tif (move.type === 'Ground') {\n"
                             '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onBasePowerPriority': 15,
              'spritenum': 456},
 'solganiumz': {'gen': 7,
                'isNonstandard': 'Past',
                'itemUser': ['Solgaleo', 'Necrozma-Dusk-Mane'],
                'name': 'Solganium Z',
                'num': 921,
                'onTakeItem': False,
                'spritenum': 685,
                'zMove': 'Searing Sunraze Smash',
                'zMoveFrom': 'Sunsteel Strike'},
 'souldew': {'fling': {'basePower': 30},
             'gen': 3,
             'itemUser': ['Latios', 'Latias'],
             'name': 'Soul Dew',
             'num': 225,
             'onBasePower': 'function (basePower, user, target, move) {\n'
                            '\t\t\tif (move && (user.baseSpecies.num === 380 '
                            '|| user.baseSpecies.num === 381) &&\n'
                            "\t\t\t\t(move.type === 'Psychic' || move.type === "
                            "'Dragon')) {\n"
                            '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                            '\t\t\t}\n'
                            '\t\t}',
             'onBasePowerPriority': 15,
             'spritenum': 459},
 'spelltag': {'fling': {'basePower': 30},
              'gen': 2,
              'name': 'Spell Tag',
              'num': 247,
              'onBasePower': 'function (basePower, user, target, move) {\n'
                             "\t\t\tif (move.type === 'Ghost') {\n"
                             '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onBasePowerPriority': 15,
              'spritenum': 461},
 'spelonberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Spelon Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Dark'},
                 'num': 179,
                 'onEat': False,
                 'spritenum': 462},
 'splashplate': {'forcedForme': 'Arceus-Water',
                 'gen': 4,
                 'isNonstandard': 'Unobtainable',
                 'name': 'Splash Plate',
                 'num': 299,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Water') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onPlate': 'Water',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 493) || pokemon.baseSpecies.num === 493) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 463},
 'spookyplate': {'forcedForme': 'Arceus-Ghost',
                 'gen': 4,
                 'isNonstandard': 'Unobtainable',
                 'name': 'Spooky Plate',
                 'num': 310,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Ghost') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'onPlate': 'Ghost',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 493) || pokemon.baseSpecies.num === 493) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 464},
 'sportball': {'gen': 2,
               'isPokeball': True,
               'name': 'Sport Ball',
               'num': 499,
               'spritenum': 465},
 'starfberry': {'gen': 3,
                'isBerry': True,
                'name': 'Starf Berry',
                'naturalGift': {'basePower': 100, 'type': 'Psychic'},
                'num': 207,
                'onEat': 'function (pokemon) {\n'
                         '\t\t\tvar stats = [];\n'
                         '\t\t\tvar stat;\n'
                         '\t\t\tfor (stat in pokemon.boosts) {\n'
                         "\t\t\t\tif (stat !== 'accuracy' && stat !== "
                         "'evasion' && pokemon.boosts[stat] < 6) {\n"
                         '\t\t\t\t\tstats.push(stat);\n'
                         '\t\t\t\t}\n'
                         '\t\t\t}\n'
                         '\t\t\tif (stats.length) {\n'
                         '\t\t\t\tvar randomStat = this.sample(stats);\n'
                         '\t\t\t\tvar boost = {};\n'
                         '\t\t\t\tboost[randomStat] = 2;\n'
                         '\t\t\t\tthis.boost(boost);\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onUpdate': 'function (pokemon) {\n'
                            '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                            '(pokemon.hp <= pokemon.maxhp / 2 && '
                            "pokemon.hasAbility('gluttony'))) {\n"
                            '\t\t\t\tpokemon.eatItem();\n'
                            '\t\t\t}\n'
                            '\t\t}',
                'spritenum': 472},
 'starsweet': {'fling': {'basePower': 10},
               'gen': 8,
               'name': 'Star Sweet',
               'num': 1114,
               'spritenum': 709},
 'steelgem': {'gen': 5,
              'isGem': True,
              'isNonstandard': 'Past',
              'name': 'Steel Gem',
              'num': 563,
              'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                       '\t\t\tif (target === source || '
                                       "move.category === 'Status')\n"
                                       '\t\t\t\treturn;\n'
                                       "\t\t\tif (move.type === 'Steel' && "
                                       'source.useItem()) {\n'
                                       "\t\t\t\tsource.addVolatile('gem');\n"
                                       '\t\t\t}\n'
                                       '\t\t}',
              'spritenum': 473},
 'steeliumz': {'forcedForme': 'Arceus-Steel',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Steelium Z',
               'num': 792,
               'onPlate': 'Steel',
               'onTakeItem': False,
               'spritenum': 647,
               'zMove': True,
               'zMoveType': 'Steel'},
 'steelixite': {'gen': 6,
                'isNonstandard': 'Past',
                'itemUser': ['Steelix'],
                'megaEvolves': 'Steelix',
                'megaStone': 'Steelix-Mega',
                'name': 'Steelixite',
                'num': 761,
                'onTakeItem': 'function (item, source) {\n'
                              '\t\t\tif (item.megaEvolves === '
                              'source.baseSpecies.baseSpecies)\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 621},
 'steelmemory': {'forcedForme': 'Silvally-Steel',
                 'gen': 7,
                 'itemUser': ['Silvally-Steel'],
                 'name': 'Steel Memory',
                 'num': 911,
                 'onMemory': 'Steel',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 773) || pokemon.baseSpecies.num === 773) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 675},
 'stick': {'fling': {'basePower': 60},
           'gen': 2,
           'isNonstandard': 'Past',
           'itemUser': ['Farfetch'd'],
           'name': 'Stick',
           'num': 259,
           'onModifyCritRatio': 'function (critRatio, user) {\n'
                                '\t\t\tif '
                                '(this.toID(user.baseSpecies.baseSpecies) === '
                                "'farfetchd') {\n"
                                '\t\t\t\treturn critRatio + 2;\n'
                                '\t\t\t}\n'
                                '\t\t}',
           'spritenum': 475},
 'stickybarb': {'fling': {'basePower': 80},
                'gen': 4,
                'name': 'Sticky Barb',
                'num': 288,
                'onHit': 'function (target, source, move) {\n'
                         '\t\t\tif (source && source !== target && '
                         '!source.item && move && '
                         'this.checkMoveMakesContact(move, source, target)) {\n'
                         '\t\t\t\tvar barb = target.takeItem();\n'
                         '\t\t\t\tif (!barb)\n'
                         '\t\t\t\t\treturn; // Gen 4 Multitype\n'
                         '\t\t\t\tsource.setItem(barb);\n'
                         '\t\t\t\t// no message for Sticky Barb changing '
                         'hands\n'
                         '\t\t\t}\n'
                         '\t\t}',
                'onResidual': 'function (pokemon) {\n'
                              '\t\t\tthis.damage(pokemon.baseMaxhp / 8);\n'
                              '\t\t}',
                'onResidualOrder': 28,
                'onResidualSubOrder': 3,
                'spritenum': 476},
 'stoneplate': {'forcedForme': 'Arceus-Rock',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Stone Plate',
                'num': 309,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move.type === 'Rock') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Rock',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 477},
 'strawberrysweet': {'fling': {'basePower': 10},
                     'gen': 8,
                     'name': 'Strawberry Sweet',
                     'num': 1109,
                     'spritenum': 704},
 'sunstone': {'fling': {'basePower': 30},
              'gen': 2,
              'name': 'Sun Stone',
              'num': 80,
              'spritenum': 480},
 'swampertite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Swampert'],
                 'megaEvolves': 'Swampert',
                 'megaStone': 'Swampert-Mega',
                 'name': 'Swampertite',
                 'num': 752,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 612},
 'sweetapple': {'fling': {'basePower': 30},
                'gen': 8,
                'name': 'Sweet Apple',
                'num': 1116,
                'spritenum': 711},
 'tamatoberry': {'gen': 3,
                 'isBerry': True,
                 'name': 'Tamato Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Psychic'},
                 'num': 174,
                 'onEat': False,
                 'spritenum': 486},
 'tangaberry': {'gen': 4,
                'isBerry': True,
                'name': 'Tanga Berry',
                'naturalGift': {'basePower': 80, 'type': 'Bug'},
                'num': 194,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Bug' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 487},
 'tapuniumz': {'gen': 7,
               'isNonstandard': 'Past',
               'itemUser': ['Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini'],
               'name': 'Tapunium Z',
               'num': 801,
               'onTakeItem': False,
               'spritenum': 653,
               'zMove': 'Guardian of Alola',
               'zMoveFrom': "Nature's Madness"},
 'tartapple': {'fling': {'basePower': 30},
               'gen': 8,
               'name': 'Tart Apple',
               'num': 1117,
               'spritenum': 712},
 'terrainextender': {'fling': {'basePower': 60},
                     'gen': 7,
                     'name': 'Terrain Extender',
                     'num': 879,
                     'spritenum': 662},
 'thickclub': {'fling': {'basePower': 90},
               'gen': 2,
               'itemUser': ['Marowak', 'Cubone'],
               'name': 'Thick Club',
               'num': 258,
               'onModifyAtk': 'function (atk, pokemon) {\n'
                              '\t\t\tif (pokemon.baseSpecies.baseSpecies === '
                              "'Cubone' || pokemon.baseSpecies.baseSpecies === "
                              "'Marowak') {\n"
                              '\t\t\t\treturn this.chainModify(2);\n'
                              '\t\t\t}\n'
                              '\t\t}',
               'onModifyAtkPriority': 1,
               'spritenum': 491},
 'throatspray': {'boosts': {'spa': 1},
                 'fling': {'basePower': 30},
                 'gen': 8,
                 'name': 'Throat Spray',
                 'num': 1118,
                 'onAfterMoveSecondarySelf': 'function (target, source, move) '
                                             '{\n'
                                             "\t\t\tif (move.flags['sound']) "
                                             '{\n'
                                             '\t\t\t\ttarget.useItem();\n'
                                             '\t\t\t}\n'
                                             '\t\t}',
                 'spritenum': 713},
 'thunderstone': {'fling': {'basePower': 30},
                  'gen': 1,
                  'name': 'Thunder Stone',
                  'num': 83,
                  'spritenum': 492},
 'timerball': {'gen': 3,
               'isPokeball': True,
               'name': 'Timer Ball',
               'num': 10,
               'spritenum': 494},
 'toxicorb': {'fling': {'basePower': 30, 'status': 'tox'},
              'gen': 4,
              'name': 'Toxic Orb',
              'num': 272,
              'onResidual': 'function (pokemon) {\n'
                            "\t\t\tpokemon.trySetStatus('tox', pokemon);\n"
                            '\t\t}',
              'onResidualOrder': 28,
              'onResidualSubOrder': 3,
              'spritenum': 515},
 'toxicplate': {'forcedForme': 'Arceus-Poison',
                'gen': 4,
                'isNonstandard': 'Unobtainable',
                'name': 'Toxic Plate',
                'num': 304,
                'onBasePower': 'function (basePower, user, target, move) {\n'
                               "\t\t\tif (move.type === 'Poison') {\n"
                               '\t\t\t\treturn this.chainModify([4915, '
                               '4096]);\n'
                               '\t\t\t}\n'
                               '\t\t}',
                'onBasePowerPriority': 15,
                'onPlate': 'Poison',
                'onTakeItem': 'function (item, pokemon, source) {\n'
                              '\t\t\tif ((source && source.baseSpecies.num === '
                              '493) || pokemon.baseSpecies.num === 493) {\n'
                              '\t\t\t\treturn false;\n'
                              '\t\t\t}\n'
                              '\t\t\treturn true;\n'
                              '\t\t}',
                'spritenum': 516},
 'tr00': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR00',
          'num': 1130,
          'spritenum': 721},
 'tr01': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR01',
          'num': 1131,
          'spritenum': 721},
 'tr02': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR02',
          'num': 1132,
          'spritenum': 730},
 'tr03': {'fling': {'basePower': 110},
          'gen': 8,
          'name': 'TR03',
          'num': 1133,
          'spritenum': 731},
 'tr04': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR04',
          'num': 1134,
          'spritenum': 731},
 'tr05': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR05',
          'num': 1135,
          'spritenum': 735},
 'tr06': {'fling': {'basePower': 110},
          'gen': 8,
          'name': 'TR06',
          'num': 1136,
          'spritenum': 735},
 'tr07': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR07',
          'num': 1137,
          'spritenum': 722},
 'tr08': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR08',
          'num': 1138,
          'spritenum': 733},
 'tr09': {'fling': {'basePower': 110},
          'gen': 8,
          'name': 'TR09',
          'num': 1139,
          'spritenum': 733},
 'tr10': {'fling': {'basePower': 100},
          'gen': 8,
          'name': 'TR10',
          'num': 1140,
          'spritenum': 725},
 'tr11': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR11',
          'num': 1141,
          'spritenum': 734},
 'tr12': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR12',
          'num': 1142,
          'spritenum': 734},
 'tr13': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR13',
          'num': 1143,
          'spritenum': 721},
 'tr14': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR14',
          'num': 1144,
          'spritenum': 721},
 'tr15': {'fling': {'basePower': 110},
          'gen': 8,
          'name': 'TR15',
          'num': 1145,
          'spritenum': 730},
 'tr16': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR16',
          'num': 1146,
          'spritenum': 731},
 'tr17': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR17',
          'num': 1147,
          'spritenum': 734},
 'tr18': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR18',
          'num': 1148,
          'spritenum': 727},
 'tr19': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR19',
          'num': 1149,
          'spritenum': 721},
 'tr20': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR20',
          'num': 1150,
          'spritenum': 721},
 'tr21': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR21',
          'num': 1151,
          'spritenum': 722},
 'tr22': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR22',
          'num': 1152,
          'spritenum': 724},
 'tr23': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR23',
          'num': 1153,
          'spritenum': 725},
 'tr24': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR24',
          'num': 1154,
          'spritenum': 736},
 'tr25': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR25',
          'num': 1155,
          'spritenum': 734},
 'tr26': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR26',
          'num': 1156,
          'spritenum': 721},
 'tr27': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR27',
          'num': 1157,
          'spritenum': 721},
 'tr28': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR28',
          'num': 1158,
          'spritenum': 727},
 'tr29': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR29',
          'num': 1159,
          'spritenum': 721},
 'tr30': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR30',
          'num': 1160,
          'spritenum': 721},
 'tr31': {'fling': {'basePower': 100},
          'gen': 8,
          'name': 'TR31',
          'num': 1161,
          'spritenum': 729},
 'tr32': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR32',
          'num': 1162,
          'spritenum': 737},
 'tr33': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR33',
          'num': 1163,
          'spritenum': 728},
 'tr34': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR34',
          'num': 1164,
          'spritenum': 734},
 'tr35': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR35',
          'num': 1165,
          'spritenum': 721},
 'tr36': {'fling': {'basePower': 95},
          'gen': 8,
          'name': 'TR36',
          'num': 1166,
          'spritenum': 730},
 'tr37': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR37',
          'num': 1167,
          'spritenum': 737},
 'tr38': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR38',
          'num': 1168,
          'spritenum': 734},
 'tr39': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR39',
          'num': 1169,
          'spritenum': 722},
 'tr40': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR40',
          'num': 1170,
          'spritenum': 734},
 'tr41': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR41',
          'num': 1171,
          'spritenum': 730},
 'tr42': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR42',
          'num': 1172,
          'spritenum': 721},
 'tr43': {'fling': {'basePower': 130},
          'gen': 8,
          'name': 'TR43',
          'num': 1173,
          'spritenum': 730},
 'tr44': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR44',
          'num': 1174,
          'spritenum': 734},
 'tr45': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR45',
          'num': 1175,
          'spritenum': 731},
 'tr46': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR46',
          'num': 1176,
          'spritenum': 729},
 'tr47': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR47',
          'num': 1177,
          'spritenum': 736},
 'tr48': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR48',
          'num': 1178,
          'spritenum': 722},
 'tr49': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR49',
          'num': 1179,
          'spritenum': 734},
 'tr50': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR50',
          'num': 1180,
          'spritenum': 732},
 'tr51': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR51',
          'num': 1181,
          'spritenum': 736},
 'tr52': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR52',
          'num': 1182,
          'spritenum': 729},
 'tr53': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR53',
          'num': 1183,
          'spritenum': 722},
 'tr54': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR54',
          'num': 1184,
          'spritenum': 724},
 'tr55': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR55',
          'num': 1185,
          'spritenum': 730},
 'tr56': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR56',
          'num': 1186,
          'spritenum': 722},
 'tr57': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR57',
          'num': 1187,
          'spritenum': 724},
 'tr58': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR58',
          'num': 1188,
          'spritenum': 737},
 'tr59': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR59',
          'num': 1189,
          'spritenum': 732},
 'tr60': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR60',
          'num': 1190,
          'spritenum': 727},
 'tr61': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR61',
          'num': 1191,
          'spritenum': 727},
 'tr62': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR62',
          'num': 1192,
          'spritenum': 736},
 'tr63': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR63',
          'num': 1193,
          'spritenum': 726},
 'tr64': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR64',
          'num': 1194,
          'spritenum': 722},
 'tr65': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR65',
          'num': 1195,
          'spritenum': 732},
 'tr66': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR66',
          'num': 1196,
          'spritenum': 723},
 'tr67': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR67',
          'num': 1197,
          'spritenum': 725},
 'tr68': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR68',
          'num': 1198,
          'spritenum': 737},
 'tr69': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR69',
          'num': 1199,
          'spritenum': 734},
 'tr70': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR70',
          'num': 1200,
          'spritenum': 729},
 'tr71': {'fling': {'basePower': 130},
          'gen': 8,
          'name': 'TR71',
          'num': 1201,
          'spritenum': 732},
 'tr72': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR72',
          'num': 1202,
          'spritenum': 732},
 'tr73': {'fling': {'basePower': 120},
          'gen': 8,
          'name': 'TR73',
          'num': 1203,
          'spritenum': 724},
 'tr74': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR74',
          'num': 1204,
          'spritenum': 729},
 'tr75': {'fling': {'basePower': 100},
          'gen': 8,
          'name': 'TR75',
          'num': 1205,
          'spritenum': 726},
 'tr76': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR76',
          'num': 1206,
          'spritenum': 726},
 'tr77': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR77',
          'num': 1207,
          'spritenum': 732},
 'tr78': {'fling': {'basePower': 95},
          'gen': 8,
          'name': 'TR78',
          'num': 1208,
          'spritenum': 724},
 'tr79': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR79',
          'num': 1209,
          'spritenum': 729},
 'tr80': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR80',
          'num': 1210,
          'spritenum': 733},
 'tr81': {'fling': {'basePower': 95},
          'gen': 8,
          'name': 'TR81',
          'num': 1211,
          'spritenum': 737},
 'tr82': {'fling': {'basePower': 20},
          'gen': 8,
          'name': 'TR82',
          'num': 1212,
          'spritenum': 734},
 'tr83': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR83',
          'num': 1213,
          'spritenum': 734},
 'tr84': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR84',
          'num': 1214,
          'spritenum': 731},
 'tr85': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR85',
          'num': 1215,
          'spritenum': 721},
 'tr86': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR86',
          'num': 1216,
          'spritenum': 733},
 'tr87': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR87',
          'num': 1217,
          'spritenum': 725},
 'tr88': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR88',
          'num': 1218,
          'spritenum': 730},
 'tr89': {'fling': {'basePower': 110},
          'gen': 8,
          'name': 'TR89',
          'num': 1219,
          'spritenum': 723},
 'tr90': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR90',
          'num': 1220,
          'spritenum': 738},
 'tr91': {'fling': {'basePower': 10},
          'gen': 8,
          'name': 'TR91',
          'num': 1221,
          'spritenum': 724},
 'tr92': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR92',
          'num': 1222,
          'spritenum': 738},
 'tr93': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR93',
          'num': 1223,
          'spritenum': 737},
 'tr94': {'fling': {'basePower': 95},
          'gen': 8,
          'name': 'TR94',
          'num': 1224,
          'spritenum': 725},
 'tr95': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR95',
          'num': 1225,
          'spritenum': 737},
 'tr96': {'fling': {'basePower': 90},
          'gen': 8,
          'name': 'TR96',
          'num': 1226,
          'spritenum': 727},
 'tr97': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR97',
          'num': 1227,
          'spritenum': 734},
 'tr98': {'fling': {'basePower': 85},
          'gen': 8,
          'name': 'TR98',
          'num': 1228,
          'spritenum': 731},
 'tr99': {'fling': {'basePower': 80},
          'gen': 8,
          'name': 'TR99',
          'num': 1229,
          'spritenum': 722},
 'twistedspoon': {'fling': {'basePower': 30},
                  'gen': 2,
                  'name': 'Twisted Spoon',
                  'num': 248,
                  'onBasePower': 'function (basePower, user, target, move) {\n'
                                 "\t\t\tif (move.type === 'Psychic') {\n"
                                 '\t\t\t\treturn this.chainModify([4915, '
                                 '4096]);\n'
                                 '\t\t\t}\n'
                                 '\t\t}',
                  'onBasePowerPriority': 15,
                  'spritenum': 520},
 'tyranitarite': {'gen': 6,
                  'isNonstandard': 'Past',
                  'itemUser': ['Tyranitar'],
                  'megaEvolves': 'Tyranitar',
                  'megaStone': 'Tyranitar-Mega',
                  'name': 'Tyranitarite',
                  'num': 669,
                  'onTakeItem': 'function (item, source) {\n'
                                '\t\t\tif (item.megaEvolves === '
                                'source.baseSpecies.baseSpecies)\n'
                                '\t\t\t\treturn false;\n'
                                '\t\t\treturn true;\n'
                                '\t\t}',
                  'spritenum': 607},
 'ultraball': {'gen': 1,
               'isPokeball': True,
               'name': 'Ultra Ball',
               'num': 2,
               'spritenum': 521},
 'ultranecroziumz': {'gen': 7,
                     'isNonstandard': 'Past',
                     'itemUser': ['Necrozma-Ultra'],
                     'name': 'Ultranecrozium Z',
                     'num': 923,
                     'onTakeItem': False,
                     'spritenum': 687,
                     'zMove': 'Light That Burns the Sky',
                     'zMoveFrom': 'Photon Geyser'},
 'upgrade': {'fling': {'basePower': 30},
             'gen': 2,
             'name': 'Up-Grade',
             'num': 252,
             'spritenum': 523},
 'utilityumbrella': {'fling': {'basePower': 60},
                     'gen': 8,
                     'name': 'Utility Umbrella',
                     'num': 1123,
                     'spritenum': 718},
 'venusaurite': {'gen': 6,
                 'isNonstandard': 'Past',
                 'itemUser': ['Venusaur'],
                 'megaEvolves': 'Venusaur',
                 'megaStone': 'Venusaur-Mega',
                 'name': 'Venusaurite',
                 'num': 659,
                 'onTakeItem': 'function (item, source) {\n'
                               '\t\t\tif (item.megaEvolves === '
                               'source.baseSpecies.baseSpecies)\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 608},
 'wacanberry': {'gen': 4,
                'isBerry': True,
                'name': 'Wacan Berry',
                'naturalGift': {'basePower': 80, 'type': 'Electric'},
                'num': 186,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Electric' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 526},
 'watergem': {'gen': 5,
              'isGem': True,
              'isNonstandard': 'Past',
              'name': 'Water Gem',
              'num': 549,
              'onSourceTryPrimaryHit': 'function (target, source, move) {\n'
                                       "\t\t\tvar pledges = ['firepledge', "
                                       "'grasspledge', 'waterpledge'];\n"
                                       '\t\t\tif (target === source || '
                                       "move.category === 'Status' || "
                                       'pledges.includes(move.id))\n'
                                       '\t\t\t\treturn;\n'
                                       "\t\t\tif (move.type === 'Water' && "
                                       'source.useItem()) {\n'
                                       "\t\t\t\tsource.addVolatile('gem');\n"
                                       '\t\t\t}\n'
                                       '\t\t}',
              'spritenum': 528},
 'wateriumz': {'forcedForme': 'Arceus-Water',
               'gen': 7,
               'isNonstandard': 'Past',
               'name': 'Waterium Z',
               'num': 778,
               'onPlate': 'Water',
               'onTakeItem': False,
               'spritenum': 633,
               'zMove': True,
               'zMoveType': 'Water'},
 'watermemory': {'forcedForme': 'Silvally-Water',
                 'gen': 7,
                 'itemUser': ['Silvally-Water'],
                 'name': 'Water Memory',
                 'num': 913,
                 'onMemory': 'Water',
                 'onTakeItem': 'function (item, pokemon, source) {\n'
                               '\t\t\tif ((source && source.baseSpecies.num '
                               '=== 773) || pokemon.baseSpecies.num === 773) '
                               '{\n'
                               '\t\t\t\treturn false;\n'
                               '\t\t\t}\n'
                               '\t\t\treturn true;\n'
                               '\t\t}',
                 'spritenum': 677},
 'waterstone': {'fling': {'basePower': 30},
                'gen': 1,
                'name': 'Water Stone',
                'num': 84,
                'spritenum': 529},
 'watmelberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Watmel Berry',
                 'naturalGift': {'basePower': 100, 'type': 'Fire'},
                 'num': 181,
                 'onEat': False,
                 'spritenum': 530},
 'waveincense': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Wave Incense',
                 'num': 317,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.type === 'Water') {\n"
                                '\t\t\t\treturn this.chainModify([4915, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 15,
                 'spritenum': 531},
 'weaknesspolicy': {'boosts': {'atk': 2, 'spa': 2},
                    'fling': {'basePower': 80},
                    'gen': 6,
                    'name': 'Weakness Policy',
                    'num': 639,
                    'onDamagingHit': 'function (damage, target, source, move) '
                                     '{\n'
                                     '\t\t\tif (!move.damage && '
                                     '!move.damageCallback && '
                                     'target.getMoveHitData(move).typeMod > 0) '
                                     '{\n'
                                     '\t\t\t\ttarget.useItem();\n'
                                     '\t\t\t}\n'
                                     '\t\t}',
                    'spritenum': 609},
 'wepearberry': {'gen': 3,
                 'isBerry': True,
                 'isNonstandard': 'Past',
                 'name': 'Wepear Berry',
                 'naturalGift': {'basePower': 90, 'type': 'Electric'},
                 'num': 167,
                 'onEat': False,
                 'spritenum': 533},
 'whippeddream': {'fling': {'basePower': 80},
                  'gen': 6,
                  'name': 'Whipped Dream',
                  'num': 646,
                  'spritenum': 692},
 'whiteherb': {'fling': {'basePower': 10,
                         'effect': 'function (pokemon) {\n'
                                   '\t\t\t\tvar activate = false;\n'
                                   '\t\t\t\tvar boosts = {};\n'
                                   '\t\t\t\tvar i;\n'
                                   '\t\t\t\tfor (i in pokemon.boosts) {\n'
                                   '\t\t\t\t\tif (pokemon.boosts[i] < 0) {\n'
                                   '\t\t\t\t\t\tactivate = true;\n'
                                   '\t\t\t\t\t\tboosts[i] = 0;\n'
                                   '\t\t\t\t\t}\n'
                                   '\t\t\t\t}\n'
                                   '\t\t\t\tif (activate) {\n'
                                   '\t\t\t\t\tpokemon.setBoost(boosts);\n'
                                   "\t\t\t\t\tthis.add('-clearnegativeboost', "
                                   "pokemon, '[silent]');\n"
                                   '\t\t\t\t}\n'
                                   '\t\t\t}'},
               'gen': 3,
               'name': 'White Herb',
               'num': 214,
               'onUpdate': 'function (pokemon) {\n'
                           '\t\t\tvar activate = false;\n'
                           '\t\t\tvar boosts = {};\n'
                           '\t\t\tvar i;\n'
                           '\t\t\tfor (i in pokemon.boosts) {\n'
                           '\t\t\t\tif (pokemon.boosts[i] < 0) {\n'
                           '\t\t\t\t\tactivate = true;\n'
                           '\t\t\t\t\tboosts[i] = 0;\n'
                           '\t\t\t\t}\n'
                           '\t\t\t}\n'
                           '\t\t\tif (activate && pokemon.useItem()) {\n'
                           '\t\t\t\tpokemon.setBoost(boosts);\n'
                           "\t\t\t\tthis.add('-clearnegativeboost', pokemon, "
                           "'[silent]');\n"
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 535},
 'widelens': {'fling': {'basePower': 10},
              'gen': 4,
              'name': 'Wide Lens',
              'num': 265,
              'onSourceModifyAccuracy': 'function (accuracy) {\n'
                                        '\t\t\tif (typeof accuracy === '
                                        "'number') {\n"
                                        '\t\t\t\treturn '
                                        'this.chainModify([4505, 4096]);\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
              'onSourceModifyAccuracyPriority': -2,
              'spritenum': 537},
 'wikiberry': {'gen': 3,
               'isBerry': True,
               'name': 'Wiki Berry',
               'naturalGift': {'basePower': 80, 'type': 'Rock'},
               'num': 160,
               'onEat': 'function (pokemon) {\n'
                        '\t\t\tthis.heal(pokemon.baseMaxhp * 0.33);\n'
                        "\t\t\tif (pokemon.getNature().minus === 'spa') {\n"
                        "\t\t\t\tpokemon.addVolatile('confusion');\n"
                        '\t\t\t}\n'
                        '\t\t}',
               'onTryEatItem': 'function (item, pokemon) {\n'
                               "\t\t\tif (!this.runEvent('TryHeal', pokemon))\n"
                               '\t\t\t\treturn false;\n'
                               '\t\t}',
               'onUpdate': 'function (pokemon) {\n'
                           '\t\t\tif (pokemon.hp <= pokemon.maxhp / 4 || '
                           '(pokemon.hp <= pokemon.maxhp / 2 && '
                           "pokemon.hasAbility('gluttony'))) {\n"
                           '\t\t\t\tpokemon.eatItem();\n'
                           '\t\t\t}\n'
                           '\t\t}',
               'spritenum': 538},
 'wiseglasses': {'fling': {'basePower': 10},
                 'gen': 4,
                 'name': 'Wise Glasses',
                 'num': 267,
                 'onBasePower': 'function (basePower, user, target, move) {\n'
                                "\t\t\tif (move.category === 'Special') {\n"
                                '\t\t\t\treturn this.chainModify([4505, '
                                '4096]);\n'
                                '\t\t\t}\n'
                                '\t\t}',
                 'onBasePowerPriority': 16,
                 'spritenum': 539},
 'yacheberry': {'gen': 4,
                'isBerry': True,
                'name': 'Yache Berry',
                'naturalGift': {'basePower': 80, 'type': 'Ice'},
                'num': 188,
                'onEat': 'function () { }',
                'onSourceModifyDamage': 'function (damage, source, target, '
                                        'move) {\n'
                                        "\t\t\tif (move.type === 'Ice' && "
                                        'target.getMoveHitData(move).typeMod > '
                                        '0) {\n'
                                        '\t\t\t\tvar hitSub = '
                                        "target.volatiles['substitute'] && "
                                        "!move.flags['authentic'] && "
                                        '!(move.infiltrates && this.gen >= '
                                        '6);\n'
                                        '\t\t\t\tif (hitSub)\n'
                                        '\t\t\t\t\treturn;\n'
                                        '\t\t\t\tif (target.eatItem()) {\n'
                                        "\t\t\t\t\tthis.debug('-50% "
                                        "reduction');\n"
                                        "\t\t\t\t\tthis.add('-enditem', "
                                        "target, this.effect, '[weaken]');\n"
                                        '\t\t\t\t\treturn '
                                        'this.chainModify(0.5);\n'
                                        '\t\t\t\t}\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
                'spritenum': 567},
 'zapplate': {'forcedForme': 'Arceus-Electric',
              'gen': 4,
              'isNonstandard': 'Unobtainable',
              'name': 'Zap Plate',
              'num': 300,
              'onBasePower': 'function (basePower, user, target, move) {\n'
                             "\t\t\tif (move.type === 'Electric') {\n"
                             '\t\t\t\treturn this.chainModify([4915, 4096]);\n'
                             '\t\t\t}\n'
                             '\t\t}',
              'onBasePowerPriority': 15,
              'onPlate': 'Electric',
              'onTakeItem': 'function (item, pokemon, source) {\n'
                            '\t\t\tif ((source && source.baseSpecies.num === '
                            '493) || pokemon.baseSpecies.num === 493) {\n'
                            '\t\t\t\treturn false;\n'
                            '\t\t\t}\n'
                            '\t\t\treturn true;\n'
                            '\t\t}',
              'spritenum': 572},
 'zoomlens': {'fling': {'basePower': 10},
              'gen': 4,
              'name': 'Zoom Lens',
              'num': 276,
              'onSourceModifyAccuracy': 'function (accuracy, target) {\n'
                                        '\t\t\tif (typeof accuracy === '
                                        "'number' && "
                                        '!this.queue.willMove(target)) {\n'
                                        "\t\t\t\tthis.debug('Zoom Lens "
                                        "boosting accuracy');\n"
                                        '\t\t\t\treturn '
                                        'this.chainModify([4915, 4096]);\n'
                                        '\t\t\t}\n'
                                        '\t\t}',
              'onSourceModifyAccuracyPriority': -2,
              'spritenum': 574}}
