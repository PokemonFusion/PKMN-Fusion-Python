from Abilities import * 

BattleAbilities = {'adaptability': {'desc': "This Pokemon's moves that match one of its types "
                          'have a same-type attack bonus (STAB) of 2 instead '
                          'of 1.5.',
                  'id': 'adaptability',
                  'name': 'Adaptability',
                  'num': 91,
                  'onModifyMove': adaptability.onModifyMove,
                  'rating': 4,
                  'shortDesc': "This Pokemon's same-type attack bonus (STAB) "
                               'is 2 instead of 1.5.'},
 'aerilate': {'desc': "This Pokemon's Normal-type moves become Flying-type "
                      'moves and have their power multiplied by 1.2. This '
                      "effect comes after other effects that change a move's "
                      "type, but before Ion Deluge and Electrify's effects.",
              'id': 'aerilate',
              'name': 'Aerilate',
              'num': 185,
              'onBasePower': aerilate.onBasePower,
              'onBasePowerPriority': 8,
              'onModifyMove': aerilate.onModifyMove,
              'onModifyMovePriority': -1,
              'rating': 4,
              'shortDesc': "This Pokemon's Normal-type moves become Flying "
                           'type and have 1.2x power.'},
 'aftermath': {'desc': 'If this Pokemon is knocked out with a contact move, '
                       "that move's user loses 1/4 of its maximum HP, rounded "
                       'down. If any active Pokemon has the Damp Ability, this '
                       'effect is prevented.',
               'id': 'aftermath',
               'name': 'Aftermath',
               'num': 106,
               'onAfterDamage': aftermath.onAfterDamage,
               'onAfterDamageOrder': 1,
               'rating': 2.5,
               'shortDesc': 'If this Pokemon is KOed with a contact move, that '
                            "move's user loses 1/4 its max HP."},
 'airlock': {'id': 'airlock',
             'name': 'Air Lock',
             'num': 76,
             'onStart': airlock.onStart,
             'rating': 2.5,
             'shortDesc': 'While this Pokemon is active, the effects of '
                          'weather conditions are disabled.',
             'suppressWeather': True},
 'analytic': {'desc': "The power of this Pokemon's move is multiplied by 1.3 "
                      'if it is the last to move in a turn. Does not affect '
                      'Doom Desire and Future Sight.',
              'id': 'analytic',
              'name': 'Analytic',
              'num': 148,
              'onBasePower': analytic.onBasePower,
              'onBasePowerPriority': 8,
              'rating': 2.5,
              'shortDesc': "This Pokemon's attacks have 1.3x power if it is "
                           'the last to move in a turn.'},
 'angerpoint': {'desc': 'If this Pokemon, but not its substitute, is struck by '
                        'a critical hit, its Attack is raised by 12 stages.',
                'id': 'angerpoint',
                'name': 'Anger Point',
                'num': 83,
                'onHit': angerpoint.onHit,
                'rating': 2,
                'shortDesc': 'If this Pokemon (not its substitute) takes a '
                             'critical hit, its Attack is raised 12 stages.'},
 'anticipation': {'desc': 'On switch-in, this Pokemon is alerted if any '
                          'opposing Pokemon has an attack that is super '
                          'effective on this Pokemon, or an OHKO move. '
                          'Counter, Metal Burst, and Mirror Coat count as '
                          'attacking moves of their respective types, while '
                          'Hidden Power, Judgment, Natural Gift, Techno Blast, '
                          'and Weather Ball are considered Normal-type moves.',
                  'id': 'anticipation',
                  'name': 'Anticipation',
                  'num': 107,
                  'onStart': anticipation.onStart,
                  'rating': 1,
                  'shortDesc': 'On switch-in, this Pokemon shudders if any foe '
                               'has a supereffective or OHKO move.'},
 'arenatrap': {'desc': 'Prevents adjacent opposing Pokemon from choosing to '
                       'switch out unless they are immune to trapping or are '
                       'airborne.',
               'id': 'arenatrap',
               'name': 'Arena Trap',
               'num': 71,
               'onFoeMaybeTrapPokemon': arenatrap.onFoeMaybeTrapPokemon,
               'onFoeTrapPokemon': arenatrap.onFoeTrapPokemon,
               'rating': 4.5,
               'shortDesc': 'Prevents adjacent foes from choosing to switch '
                            'unless they are airborne.'},
 'aromaveil': {'desc': 'This Pokemon and its allies cannot be affected by '
                       'Attract, Disable, Encore, Heal Block, Taunt, or '
                       'Torment.',
               'id': 'aromaveil',
               'name': 'Aroma Veil',
               'num': 165,
               'onAllyTryAddVolatile': aromaveil.onAllyTryAddVolatile,
               'rating': 1.5,
               'shortDesc': 'Protects user/allies from Attract, Disable, '
                            'Encore, Heal Block, Taunt, and Torment.'},
 'aurabreak': {'desc': 'While this Pokemon is active, the effects of the Dark '
                       'Aura and Fairy Aura Abilities are reversed, '
                       'multiplying the power of Dark- and Fairy-type moves, '
                       'respectively, by 3/4 instead of 1.33.',
               'id': 'aurabreak',
               'name': 'Aura Break',
               'num': 188,
               'onAnyTryPrimaryHit': aurabreak.onAnyTryPrimaryHit,
               'onStart': aurabreak.onStart,
               'rating': 1.5,
               'shortDesc': 'While this Pokemon is active, the Dark Aura and '
                            'Fairy Aura power modifier is 0.75x.'},
 'baddreams': {'desc': 'Causes adjacent opposing Pokemon to lose 1/8 of their '
                       'maximum HP, rounded down, at the end of each turn if '
                       'they are asleep.',
               'id': 'baddreams',
               'name': 'Bad Dreams',
               'num': 123,
               'onResidual': baddreams.onResidual,
               'onResidualOrder': 26,
               'onResidualSubOrder': 1,
               'rating': 2,
               'shortDesc': 'Causes sleeping adjacent foes to lose 1/8 of '
                            'their max HP at the end of each turn.'},
 'battery': {'id': 'battery',
             'name': 'Battery',
             'num': 217,
             'onAllyBasePower': battery.onAllyBasePower,
             'onBasePowerPriority': 8,
             'rating': 0,
             'shortDesc': "This Pokemon's allies have the power of their "
                          'special attacks multiplied by 1.3.'},
 'battlearmor': {'id': 'battlearmor',
                 'name': 'Battle Armor',
                 'num': 4,
                 'onCriticalHit': False,
                 'rating': 1,
                 'shortDesc': 'This Pokemon cannot be struck by a critical '
                              'hit.'},
 'battlebond': {'desc': 'If this Pokemon is a Greninja, it transforms into '
                        'Ash-Greninja after knocking out a Pokemon. As '
                        'Ash-Greninja, its Water Shuriken has 20 base power '
                        'and always hits 3 times.',
                'id': 'battlebond',
                'name': 'Battle Bond',
                'num': 210,
                'onModifyMove': battlebond.onModifyMove,
                'onModifyMovePriority': -1,
                'onSourceFaint': battlebond.onSourceFaint,
                'rating': 3,
                'shortDesc': 'After KOing a Pokemon: becomes Ash-Greninja, '
                             'Water Shuriken: 20 power, hits 3x.'},
 'beastboost': {'desc': "This Pokemon's highest stat is raised by 1 stage if "
                        'it attacks and knocks out another Pokemon.',
                'id': 'beastboost',
                'name': 'Beast Boost',
                'num': 224,
                'onSourceFaint': beastboost.onSourceFaint,
                'rating': 3.5,
                'shortDesc': "This Pokemon's highest stat is raised by 1 if it "
                             'attacks and KOes another Pokemon.'},
 'berserk': {'desc': 'When this Pokemon has more than 1/2 its maximum HP and '
                     'takes damage from an attack bringing it to 1/2 or less '
                     'of its maximum HP, its Special Attack is raised by 1 '
                     'stage. This effect applies after all hits from a '
                     'multi-hit move; Sheer Force prevents it from activating '
                     'if the move has a secondary effect.',
             'id': 'berserk',
             'name': 'Berserk',
             'num': 201,
             'onAfterMoveSecondary': berserk.onAfterMoveSecondary,
             'rating': 2.5,
             'shortDesc': "This Pokemon's Sp. Atk is raised by 1 when it "
                          'reaches 1/2 or less of its max HP.'},
 'bigpecks': {'id': 'bigpecks',
              'name': 'Big Pecks',
              'num': 145,
              'onBoost': bigpecks.onBoost,
              'rating': 0.5,
              'shortDesc': 'Prevents other Pokemon from lowering this '
                           "Pokemon's Defense stat stage."},
 'blaze': {'desc': 'When this Pokemon has 1/3 or less of its maximum HP, '
                   'rounded down, its attacking stat is multiplied by 1.5 '
                   'while using a Fire-type attack.',
           'id': 'blaze',
           'name': 'Blaze',
           'num': 66,
           'onModifyAtk': blaze.onModifyAtk,
           'onModifyAtkPriority': 5,
           'onModifySpA': blaze.onModifySpA,
           'onModifySpAPriority': 5,
           'rating': 2,
           'shortDesc': "At 1/3 or less of its max HP, this Pokemon's "
                        'attacking stat is 1.5x with Fire attacks.'},
 'bulletproof': {'desc': 'This Pokemon is immune to ballistic moves. Ballistic '
                         'moves include Bullet Seed, Octazooka, Barrage, Rock '
                         'Wrecker, Zap Cannon, Acid Spray, Aura Sphere, Focus '
                         'Blast, and all moves with Ball or Bomb in their '
                         'name.',
                 'id': 'bulletproof',
                 'name': 'Bulletproof',
                 'num': 171,
                 'onTryHit': bulletproof.onTryHit,
                 'rating': 3.5,
                 'shortDesc': 'Makes user immune to ballistic moves (Shadow '
                              'Ball, Sludge Bomb, Focus Blast, etc).'},
 'cheekpouch': {'desc': 'If this Pokemon eats a Berry, it restores 1/3 of its '
                        "maximum HP, rounded down, in addition to the Berry's "
                        'effect.',
                'id': 'cheekpouch',
                'name': 'Cheek Pouch',
                'num': 167,
                'onEatItem': cheekpouch.onEatItem,
                'rating': 2,
                'shortDesc': 'If this Pokemon eats a Berry, it restores 1/3 of '
                             "its max HP after the Berry's effect."},
 'chlorophyll': {'id': 'chlorophyll',
                 'name': 'Chlorophyll',
                 'num': 34,
                 'onModifySpe': chlorophyll.onModifySpe,
                 'rating': 3,
                 'shortDesc': "If Sunny Day is active, this Pokemon's Speed is "
                              'doubled.'},
 'clearbody': {'id': 'clearbody',
               'name': 'Clear Body',
               'num': 29,
               'onBoost': clearbody.onBoost,
               'rating': 2,
               'shortDesc': 'Prevents other Pokemon from lowering this '
                            "Pokemon's stat stages."},
 'cloudnine': {'id': 'cloudnine',
               'name': 'Cloud Nine',
               'num': 13,
               'onStart': cloudnine.onStart,
               'rating': 2.5,
               'shortDesc': 'While this Pokemon is active, the effects of '
                            'weather conditions are disabled.',
               'suppressWeather': True},
 'colorchange': {'desc': "This Pokemon's type changes to match the type of the "
                         'last move that hit it, unless that type is already '
                         'one of its types. This effect applies after all hits '
                         'from a multi-hit move; Sheer Force prevents it from '
                         'activating if the move has a secondary effect.',
                 'id': 'colorchange',
                 'name': 'Color Change',
                 'num': 16,
                 'onAfterMoveSecondary': colorchange.onAfterMoveSecondary,
                 'rating': 1,
                 'shortDesc': "This Pokemon's type changes to the type of a "
                              "move it's hit by, unless it has the type."},
 'comatose': {'desc': 'This Pokemon cannot be statused, and is considered to '
                      'be asleep. Moongeist Beam, Sunsteel Strike, and the '
                      'Mold Breaker, Teravolt, and Turboblaze Abilities cannot '
                      'ignore this Ability.',
              'id': 'comatose',
              'isUnbreakable': True,
              'name': 'Comatose',
              'num': 213,
              'onSetStatus': comatose.onSetStatus,
              'onStart': comatose.onStart,
              'rating': 3,
              'shortDesc': 'This Pokemon cannot be statused, and is considered '
                           'to be asleep.'},
 'competitive': {'desc': "This Pokemon's Special Attack is raised by 2 stages "
                         'for each of its stat stages that is lowered by an '
                         'opposing Pokemon.',
                 'id': 'competitive',
                 'name': 'Competitive',
                 'num': 172,
                 'onAfterEachBoost': competitive.onAfterEachBoost,
                 'rating': 2.5,
                 'shortDesc': "This Pokemon's Sp. Atk is raised by 2 for each "
                              'of its stats that is lowered by a foe.'},
 'compoundeyes': {'id': 'compoundeyes',
                  'name': 'Compound Eyes',
                  'num': 14,
                  'onSourceModifyAccuracy': compoundeyes.onSourceModifyAccuracy,
                  'rating': 3.5,
                  'shortDesc': "This Pokemon's moves have their accuracy "
                               'multiplied by 1.3.'},
 'contrary': {'id': 'contrary',
              'name': 'Contrary',
              'num': 126,
              'onBoost': contrary.onBoost,
              'rating': 4,
              'shortDesc': 'If this Pokemon has a stat stage raised it is '
                           'lowered instead, and vice versa.'},
 'corrosion': {'id': 'corrosion',
               'name': 'Corrosion',
               'num': 212,
               'rating': 2.5,
               'shortDesc': 'This Pokemon can poison or badly poison other '
                            'Pokemon regardless of their typing.'},
 'cursedbody': {'desc': 'If this Pokemon is hit by an attack, there is a 30% '
                        'chance that move gets disabled unless one of the '
                        "attacker's moves is already disabled.",
                'id': 'cursedbody',
                'name': 'Cursed Body',
                'num': 130,
                'onAfterDamage': cursedbody.onAfterDamage,
                'rating': 2,
                'shortDesc': 'If this Pokemon is hit by an attack, there is a '
                             '30% chance that move gets disabled.'},
 'cutecharm': {'desc': 'There is a 30% chance a Pokemon making contact with '
                       'this Pokemon will become infatuated if it is of the '
                       'opposite gender.',
               'id': 'cutecharm',
               'name': 'Cute Charm',
               'num': 56,
               'onAfterDamage': cutecharm.onAfterDamage,
               'rating': 1,
               'shortDesc': '30% chance of infatuating Pokemon of the opposite '
                            'gender if they make contact.'},
 'damp': {'desc': 'While this Pokemon is active, Explosion, Mind Blown, '
                  'Self-Destruct, and the Aftermath Ability are prevented from '
                  'having an effect.',
          'id': 'damp',
          'name': 'Damp',
          'num': 6,
          'onAnyDamage': damp.onAnyDamage,
          'onAnyTryMove': damp.onAnyTryMove,
          'rating': 1,
          'shortDesc': 'Prevents Explosion/Mind Blown/Self-Destruct/Aftermath '
                       'while this Pokemon is active.'},
 'dancer': {'desc': 'After another Pokemon uses a dance move, this Pokemon '
                    'uses the same move. Moves used by this Ability cannot be '
                    'copied again.',
            'id': 'dancer',
            'name': 'Dancer',
            'num': 216,
            'rating': 2.5,
            'shortDesc': 'After another Pokemon uses a dance move, this '
                         'Pokemon uses the same move.'},
 'darkaura': {'desc': 'While this Pokemon is active, the power of Dark-type '
                      'moves used by active Pokemon is multiplied by 1.33.',
              'id': 'darkaura',
              'isUnbreakable': True,
              'name': 'Dark Aura',
              'num': 186,
              'onAnyBasePower': darkaura.onAnyBasePower,
              'onStart': darkaura.onStart,
              'rating': 3,
              'shortDesc': 'While this Pokemon is active, a Dark move used by '
                           'any Pokemon has 1.33x power.'},
 'dazzling': {'desc': 'While this Pokemon is active, priority moves from '
                      'opposing Pokemon targeted at allies are prevented from '
                      'having an effect.',
              'id': 'dazzling',
              'name': 'Dazzling',
              'num': 219,
              'onFoeTryMove': dazzling.onFoeTryMove,
              'rating': 3,
              'shortDesc': 'While this Pokemon is active, allies are protected '
                           'from opposing priority moves.'},
 'defeatist': {'desc': 'While this Pokemon has 1/2 or less of its maximum HP, '
                       'its Attack and Special Attack are halved.',
               'id': 'defeatist',
               'name': 'Defeatist',
               'num': 129,
               'onModifyAtk': defeatist.onModifyAtk,
               'onModifyAtkPriority': 5,
               'onModifySpA': defeatist.onModifySpA,
               'onModifySpAPriority': 5,
               'rating': -1,
               'shortDesc': 'While this Pokemon has 1/2 or less of its max HP, '
                            'its Attack and Sp. Atk are halved.'},
 'defiant': {'desc': "This Pokemon's Attack is raised by 2 stages for each of "
                     'its stat stages that is lowered by an opposing Pokemon.',
             'id': 'defiant',
             'name': 'Defiant',
             'num': 128,
             'onAfterEachBoost': defiant.onAfterEachBoost,
             'rating': 2.5,
             'shortDesc': "This Pokemon's Attack is raised by 2 for each of "
                          'its stats that is lowered by a foe.'},
 'deltastream': {'desc': 'On switch-in, the weather becomes strong winds that '
                         'remove the weaknesses of the Flying type from '
                         'Flying-type Pokemon. This weather remains in effect '
                         'until this Ability is no longer active for any '
                         'Pokemon, or the weather is changed by Desolate Land '
                         'or Primordial Sea.',
                 'id': 'deltastream',
                 'name': 'Delta Stream',
                 'num': 191,
                 'onAnySetWeather': deltastream.onAnySetWeather,
                 'onEnd': deltastream.onEnd,
                 'onStart': deltastream.onStart,
                 'rating': 5,
                 'shortDesc': 'On switch-in, strong winds begin until this '
                              'Ability is not active in battle.'},
 'desolateland': {'desc': 'On switch-in, the weather becomes extremely harsh '
                          'sunlight that prevents damaging Water-type moves '
                          'from executing, in addition to all the effects of '
                          'Sunny Day. This weather remains in effect until '
                          'this Ability is no longer active for any Pokemon, '
                          'or the weather is changed by Delta Stream or '
                          'Primordial Sea.',
                  'id': 'desolateland',
                  'name': 'Desolate Land',
                  'num': 190,
                  'onAnySetWeather': desolateland.onAnySetWeather,
                  'onEnd': desolateland.onEnd,
                  'onStart': desolateland.onStart,
                  'rating': 5,
                  'shortDesc': 'On switch-in, extremely harsh sunlight begins '
                               'until this Ability is not active in battle.'},
 'disguise': {'desc': 'If this Pokemon is a Mimikyu, the first hit it takes in '
                      'battle deals 0 neutral damage. Its disguise is then '
                      'broken and it changes to Busted Form. Confusion damage '
                      'also breaks the disguise.',
              'id': 'disguise',
              'name': 'Disguise',
              'num': 209,
              'onDamage': disguise.onDamage,
              'onDamagePriority': 1,
              'onEffectiveness': disguise.onEffectiveness,
              'onUpdate': disguise.onUpdate,
              'rating': 4,
              'shortDesc': 'If this Pokemon is a Mimikyu, the first hit it '
                           'takes in battle deals 0 neutral damage.'},
 'download': {'desc': "On switch-in, this Pokemon's Attack or Special Attack "
                      'is raised by 1 stage based on the weaker combined '
                      'defensive stat of all opposing Pokemon. Attack is '
                      'raised if their Defense is lower, and Special Attack is '
                      'raised if their Special Defense is the same or lower.',
              'id': 'download',
              'name': 'Download',
              'num': 88,
              'onStart': download.onStart,
              'rating': 4,
              'shortDesc': 'On switch-in, Attack or Sp. Atk is raised 1 stage '
                           "based on the foes' weaker Defense."},
 'drizzle': {'id': 'drizzle',
             'name': 'Drizzle',
             'num': 2,
             'onStart': drizzle.onStart,
             'rating': 4.5,
             'shortDesc': 'On switch-in, this Pokemon summons Rain Dance.'},
 'drought': {'id': 'drought',
             'name': 'Drought',
             'num': 70,
             'onStart': drought.onStart,
             'rating': 4.5,
             'shortDesc': 'On switch-in, this Pokemon summons Sunny Day.'},
 'dryskin': {'desc': 'This Pokemon is immune to Water-type moves and restores '
                     '1/4 of its maximum HP, rounded down, when hit by a '
                     'Water-type move. The power of Fire-type moves is '
                     'multiplied by 1.25 when used on this Pokemon. At the end '
                     'of each turn, this Pokemon restores 1/8 of its maximum '
                     'HP, rounded down, if the weather is Rain Dance, and '
                     'loses 1/8 of its maximum HP, rounded down, if the '
                     'weather is Sunny Day.',
             'id': 'dryskin',
             'name': 'Dry Skin',
             'num': 87,
             'onBasePowerPriority': 7,
             'onFoeBasePower': dryskin.onFoeBasePower,
             'onTryHit': dryskin.onTryHit,
             'onWeather': dryskin.onWeather,
             'rating': 3,
             'shortDesc': 'This Pokemon is healed 1/4 by Water, 1/8 by Rain; '
                          'is hurt 1.25x by Fire, 1/8 by Sun.'},
 'earlybird': {'id': 'earlybird',
               'name': 'Early Bird',
               'num': 48,
               'rating': 2,
               'shortDesc': "This Pokemon's sleep counter drops by 2 instead "
                            'of 1.'},
 'effectspore': {'desc': '30% chance a Pokemon making contact with this '
                         'Pokemon will be poisoned, paralyzed, or fall asleep.',
                 'id': 'effectspore',
                 'name': 'Effect Spore',
                 'num': 27,
                 'onAfterDamage': effectspore.onAfterDamage,
                 'rating': 2,
                 'shortDesc': '30% chance of poison/paralysis/sleep on others '
                              'making contact with this Pokemon.'},
 'electricsurge': {'id': 'electricsurge',
                   'name': 'Electric Surge',
                   'num': 226,
                   'onStart': electricsurge.onStart,
                   'rating': 4,
                   'shortDesc': 'On switch-in, this Pokemon summons Electric '
                                'Terrain.'},
 'emergencyexit': {'desc': 'When this Pokemon has more than 1/2 its maximum HP '
                           'and takes damage bringing it to 1/2 or less of its '
                           'maximum HP, it immediately switches out to a '
                           'chosen ally. This effect applies after all hits '
                           'from a multi-hit move; Sheer Force prevents it '
                           'from activating if the move has a secondary '
                           'effect. This effect applies to both direct and '
                           'indirect damage, except Curse and Substitute on '
                           'use, Belly Drum, Pain Split, Struggle recoil, and '
                           'confusion damage.',
                   'id': 'emergencyexit',
                   'name': 'Emergency Exit',
                   'num': 194,
                   'onAfterDamage': emergencyexit.onAfterDamage,
                   'onAfterMoveSecondary': emergencyexit.onAfterMoveSecondary,
                   'rating': 1.5,
                   'shortDesc': 'This Pokemon switches out when it reaches 1/2 '
                                'or less of its maximum HP.'},
 'fairyaura': {'desc': 'While this Pokemon is active, the power of Fairy-type '
                       'moves used by active Pokemon is multiplied by 1.33.',
               'id': 'fairyaura',
               'isUnbreakable': True,
               'name': 'Fairy Aura',
               'num': 187,
               'onAnyBasePower': fairyaura.onAnyBasePower,
               'onStart': fairyaura.onStart,
               'rating': 3,
               'shortDesc': 'While this Pokemon is active, a Fairy move used '
                            'by any Pokemon has 1.33x power.'},
 'filter': {'id': 'filter',
            'name': 'Filter',
            'num': 111,
            'onSourceModifyDamage': filter.onSourceModifyDamage,
            'rating': 3,
            'shortDesc': 'This Pokemon receives 3/4 damage from supereffective '
                         'attacks.'},
 'flamebody': {'id': 'flamebody',
               'name': 'Flame Body',
               'num': 49,
               'onAfterDamage': flamebody.onAfterDamage,
               'rating': 2,
               'shortDesc': '30% chance a Pokemon making contact with this '
                            'Pokemon will be burned.'},
 'flareboost': {'desc': 'While this Pokemon is burned, the power of its '
                        'special attacks is multiplied by 1.5.',
                'id': 'flareboost',
                'name': 'Flare Boost',
                'num': 138,
                'onBasePower': flareboost.onBasePower,
                'onBasePowerPriority': 8,
                'rating': 2.5,
                'shortDesc': 'While this Pokemon is burned, its special '
                             'attacks have 1.5x power.'},
 'flashfire': {'desc': 'This Pokemon is immune to Fire-type moves. The first '
                       'time it is hit by a Fire-type move, its attacking stat '
                       'is multiplied by 1.5 while using a Fire-type attack as '
                       'long as it remains active and has this Ability. If '
                       'this Pokemon is frozen, it cannot be defrosted by '
                       'Fire-type attacks.',
               'effect': {'noCopy': True,
                          'onEnd': flashfire.onEnd,
                          'onModifyAtk': flashfire.onModifyAtk,
                          'onModifyAtkPriority': 5,
                          'onModifySpA': flashfire.onModifySpA,
                          'onModifySpAPriority': 5,
                          'onStart': flashfire.onStart},
               'id': 'flashfire',
               'name': 'Flash Fire',
               'num': 18,
               'onEnd': flashfire.onEnd,
               'onTryHit': flashfire.onTryHit,
               'rating': 3,
               'shortDesc': "This Pokemon's Fire attacks do 1.5x damage if hit "
                            'by one Fire move; Fire immunity.'},
 'flowergift': {'desc': 'If this Pokemon is a Cherrim and Sunny Day is active, '
                        'it changes to Sunshine Form and the Attack and '
                        'Special Defense of it and its allies are multiplied '
                        'by 1.5.',
                'id': 'flowergift',
                'name': 'Flower Gift',
                'num': 122,
                'onAllyModifyAtk': flowergift.onAllyModifyAtk,
                'onAllyModifySpD': flowergift.onAllyModifySpD,
                'onModifyAtkPriority': 3,
                'onModifySpDPriority': 4,
                'onStart': flowergift.onStart,
                'onUpdate': flowergift.onUpdate,
                'rating': 2.5,
                'shortDesc': 'If user is Cherrim and Sunny Day is active, it '
                             "and allies' Attack and Sp. Def are 1.5x."},
 'flowerveil': {'desc': "Grass-type Pokemon on this Pokemon's side cannot have "
                        'their stat stages lowered by other Pokemon or have a '
                        'major status condition inflicted on them by other '
                        'Pokemon.',
                'id': 'flowerveil',
                'name': 'Flower Veil',
                'num': 166,
                'onAllyBoost': flowerveil.onAllyBoost,
                'onAllySetStatus': flowerveil.onAllySetStatus,
                'onAllyTryAddVolatile': flowerveil.onAllyTryAddVolatile,
                'rating': 0,
                'shortDesc': "This side's Grass types can't have stats lowered "
                             'or status inflicted by other Pokemon.'},
 'fluffy': {'desc': 'This Pokemon receives 1/2 damage from contact moves, but '
                    'double damage from Fire moves.',
            'id': 'fluffy',
            'name': 'Fluffy',
            'num': 218,
            'onSourceModifyDamage': fluffy.onSourceModifyDamage,
            'rating': 2.5,
            'shortDesc': 'This Pokemon takes 1/2 damage from contact moves, 2x '
                         'damage from Fire moves.'},
 'forecast': {'desc': 'If this Pokemon is a Castform, its type changes to the '
                      "current weather condition's type, except Sandstorm.",
              'id': 'forecast',
              'name': 'Forecast',
              'num': 59,
              'onUpdate': forecast.onUpdate,
              'rating': 3,
              'shortDesc': "Castform's type changes to the current weather "
                           "condition's type, except Sandstorm."},
 'forewarn': {'desc': 'On switch-in, this Pokemon is alerted to the move with '
                      'the highest power, at random, known by an opposing '
                      'Pokemon.',
              'id': 'forewarn',
              'name': 'Forewarn',
              'num': 108,
              'onStart': forewarn.onStart,
              'rating': 1,
              'shortDesc': "On switch-in, this Pokemon is alerted to the foes' "
                           'move with the highest power.'},
 'friendguard': {'id': 'friendguard',
                 'name': 'Friend Guard',
                 'num': 132,
                 'onAnyModifyDamage': friendguard.onAnyModifyDamage,
                 'rating': 0,
                 'shortDesc': "This Pokemon's allies receive 3/4 damage from "
                              "other Pokemon's attacks."},
 'frisk': {'id': 'frisk',
           'name': 'Frisk',
           'num': 119,
           'onStart': frisk.onStart,
           'rating': 1.5,
           'shortDesc': 'On switch-in, this Pokemon identifies the held items '
                        'of all opposing Pokemon.'},
 'fullmetalbody': {'desc': 'Prevents other Pokemon from lowering this '
                           "Pokemon's stat stages. Moongeist Beam, Sunsteel "
                           'Strike, and the Mold Breaker, Teravolt, and '
                           'Turboblaze Abilities cannot ignore this Ability.',
                   'id': 'fullmetalbody',
                   'isUnbreakable': True,
                   'name': 'Full Metal Body',
                   'num': 230,
                   'onBoost': fullmetalbody.onBoost,
                   'rating': 2,
                   'shortDesc': 'Prevents other Pokemon from lowering this '
                                "Pokemon's stat stages."},
 'furcoat': {'id': 'furcoat',
             'name': 'Fur Coat',
             'num': 169,
             'onModifyDef': furcoat.onModifyDef,
             'onModifyDefPriority': 6,
             'rating': 3.5,
             'shortDesc': "This Pokemon's Defense is doubled."},
 'galewings': {'id': 'galewings',
               'name': 'Gale Wings',
               'num': 177,
               'onModifyPriority': galewings.onModifyPriority,
               'rating': 3,
               'shortDesc': 'If this Pokemon is at full HP, its Flying-type '
                            'moves have their priority increased by 1.'},
 'galvanize': {'desc': "This Pokemon's Normal-type moves become Electric-type "
                       'moves and have their power multiplied by 1.2. This '
                       "effect comes after other effects that change a move's "
                       "type, but before Ion Deluge and Electrify's effects.",
               'id': 'galvanize',
               'name': 'Galvanize',
               'num': 206,
               'onBasePower': galvanize.onBasePower,
               'onBasePowerPriority': 8,
               'onModifyMove': galvanize.onModifyMove,
               'onModifyMovePriority': -1,
               'rating': 4,
               'shortDesc': "This Pokemon's Normal-type moves become Electric "
                            'type and have 1.2x power.'},
 'gluttony': {'id': 'gluttony',
              'name': 'Gluttony',
              'num': 82,
              'rating': 1.5,
              'shortDesc': 'When this Pokemon has 1/2 or less of its maximum '
                           'HP, it uses certain Berries early.'},
 'gooey': {'id': 'gooey',
           'name': 'Gooey',
           'num': 183,
           'onAfterDamage': gooey.onAfterDamage,
           'rating': 2.5,
           'shortDesc': 'Pokemon making contact with this Pokemon have their '
                        'Speed lowered by 1 stage.'},
 'grasspelt': {'id': 'grasspelt',
               'name': 'Grass Pelt',
               'num': 179,
               'onModifyDef': grasspelt.onModifyDef,
               'onModifyDefPriority': 6,
               'rating': 1,
               'shortDesc': "If Grassy Terrain is active, this Pokemon's "
                            'Defense is multiplied by 1.5.'},
 'grassysurge': {'id': 'grassysurge',
                 'name': 'Grassy Surge',
                 'num': 229,
                 'onStart': grassysurge.onStart,
                 'rating': 4,
                 'shortDesc': 'On switch-in, this Pokemon summons Grassy '
                              'Terrain.'},
 'guts': {'desc': 'If this Pokemon has a major status condition, its Attack is '
                  "multiplied by 1.5; burn's physical damage halving is "
                  'ignored.',
          'id': 'guts',
          'name': 'Guts',
          'num': 62,
          'onModifyAtk': guts.onModifyAtk,
          'onModifyAtkPriority': 5,
          'rating': 3,
          'shortDesc': 'If this Pokemon is statused, its Attack is 1.5x; '
                       'ignores burn halving physical damage.'},
 'harvest': {'desc': 'If the last item this Pokemon used is a Berry, there is '
                     'a 50% chance it gets restored at the end of each turn. '
                     'If Sunny Day is active, this chance is 100%.',
             'id': 'harvest',
             'name': 'Harvest',
             'num': 139,
             'onResidual': harvest.onResidual,
             'onResidualOrder': 26,
             'onResidualSubOrder': 1,
             'rating': 2.5,
             'shortDesc': 'If last item used is a Berry, 50% chance to restore '
                          'it each end of turn. 100% in Sun.'},
 'healer': {'desc': "There is a 30% chance of curing an adjacent ally's major "
                    'status condition at the end of each turn.',
            'id': 'healer',
            'name': 'Healer',
            'num': 131,
            'onResidual': healer.onResidual,
            'onResidualOrder': 5,
            'onResidualSubOrder': 1,
            'rating': 0,
            'shortDesc': "30% chance of curing an adjacent ally's status at "
                         'the end of each turn.'},
 'heatproof': {'desc': 'The power of Fire-type attacks against this Pokemon is '
                       'halved, and burn damage taken is halved.',
               'id': 'heatproof',
               'name': 'Heatproof',
               'num': 85,
               'onBasePowerPriority': 7,
               'onDamage': heatproof.onDamage,
               'onSourceBasePower': heatproof.onSourceBasePower,
               'rating': 2.5,
               'shortDesc': 'The power of Fire-type attacks against this '
                            'Pokemon is halved; burn damage halved.'},
 'heavymetal': {'id': 'heavymetal',
                'name': 'Heavy Metal',
                'num': 134,
                'onModifyWeight': heavymetal.onModifyWeight,
                'rating': -1,
                'shortDesc': "This Pokemon's weight is doubled."},
 'honeygather': {'id': 'honeygather',
                 'name': 'Honey Gather',
                 'num': 118,
                 'rating': 0,
                 'shortDesc': 'No competitive use.'},
 'hugepower': {'id': 'hugepower',
               'name': 'Huge Power',
               'num': 37,
               'onModifyAtk': hugepower.onModifyAtk,
               'onModifyAtkPriority': 5,
               'rating': 5,
               'shortDesc': "This Pokemon's Attack is doubled."},
 'hustle': {'desc': "This Pokemon's Attack is multiplied by 1.5 and the "
                    'accuracy of its physical attacks is multiplied by 0.8.',
            'id': 'hustle',
            'name': 'Hustle',
            'num': 55,
            'onModifyAtk': hustle.onModifyAtk,
            'onModifyAtkPriority': 5,
            'onModifyMove': hustle.onModifyMove,
            'onModifyMovePriority': -1,
            'rating': 3,
            'shortDesc': "This Pokemon's Attack is 1.5x and accuracy of its "
                         'physical attacks is 0.8x.'},
 'hydration': {'desc': 'This Pokemon has its major status condition cured at '
                       'the end of each turn if Rain Dance is active.',
               'id': 'hydration',
               'name': 'Hydration',
               'num': 93,
               'onResidual': hydration.onResidual,
               'onResidualOrder': 5,
               'onResidualSubOrder': 1,
               'rating': 2,
               'shortDesc': 'This Pokemon has its status cured at the end of '
                            'each turn if Rain Dance is active.'},
 'hypercutter': {'id': 'hypercutter',
                 'name': 'Hyper Cutter',
                 'num': 52,
                 'onBoost': hypercutter.onBoost,
                 'rating': 1.5,
                 'shortDesc': 'Prevents other Pokemon from lowering this '
                              "Pokemon's Attack stat stage."},
 'icebody': {'desc': 'If Hail is active, this Pokemon restores 1/16 of its '
                     'maximum HP, rounded down, at the end of each turn. This '
                     'Pokemon takes no damage from Hail.',
             'id': 'icebody',
             'name': 'Ice Body',
             'num': 115,
             'onImmunity': icebody.onImmunity,
             'onWeather': icebody.onWeather,
             'rating': 1.5,
             'shortDesc': 'If Hail is active, this Pokemon heals 1/16 of its '
                          'max HP each turn; immunity to Hail.'},
 'illuminate': {'id': 'illuminate',
                'name': 'Illuminate',
                'num': 35,
                'rating': 0,
                'shortDesc': 'No competitive use.'},
 'illusion': {'desc': 'When this Pokemon switches in, it appears as the last '
                      'unfainted Pokemon in its party until it takes direct '
                      "damage from another Pokemon's attack. This Pokemon's "
                      'actual level and HP are displayed instead of those of '
                      'the mimicked Pokemon.',
              'id': 'illusion',
              'isUnbreakable': True,
              'name': 'Illusion',
              'num': 149,
              'onAfterDamage': illusion.onAfterDamage,
              'onBeforeSwitchIn': illusion.onBeforeSwitchIn,
              'onEnd': illusion.onEnd,
              'onFaint': illusion.onFaint,
              'rating': 4,
              'shortDesc': 'This Pokemon appears as the last Pokemon in the '
                           'party until it takes direct damage.'},
 'immunity': {'id': 'immunity',
              'name': 'Immunity',
              'num': 17,
              'onSetStatus': immunity.onSetStatus,
              'onUpdate': immunity.onUpdate,
              'rating': 2,
              'shortDesc': 'This Pokemon cannot be poisoned. Gaining this '
                           'Ability while poisoned cures it.'},
 'imposter': {'desc': 'On switch-in, this Pokemon Transforms into the opposing '
                      'Pokemon that is facing it. If there is no Pokemon at '
                      'that position, this Pokemon does not Transform.',
              'id': 'imposter',
              'name': 'Imposter',
              'num': 150,
              'onStart': imposter.onStart,
              'rating': 4.5,
              'shortDesc': 'On switch-in, this Pokemon Transforms into the '
                           'opposing Pokemon that is facing it.'},
 'infiltrator': {'desc': "This Pokemon's moves ignore substitutes and the "
                         "opposing side's Reflect, Light Screen, Safeguard, "
                         'Mist and Aurora Veil.',
                 'id': 'infiltrator',
                 'name': 'Infiltrator',
                 'num': 151,
                 'onModifyMove': infiltrator.onModifyMove,
                 'rating': 3,
                 'shortDesc': "Moves ignore substitutes and foe's "
                              'Reflect/Light Screen/Safeguard/Mist/Aurora '
                              'Veil.'},
 'innardsout': {'desc': 'If this Pokemon is knocked out with a move, that '
                        "move's user loses HP equal to the amount of damage "
                        'inflicted on this Pokemon.',
                'id': 'innardsout',
                'name': 'Innards Out',
                'num': 215,
                'onAfterDamage': innardsout.onAfterDamage,
                'onAfterDamageOrder': 1,
                'rating': 2.5,
                'shortDesc': "If this Pokemon is KOed with a move, that move's "
                             'user loses an equal amount of HP.'},
 'innerfocus': {'id': 'innerfocus',
                'name': 'Inner Focus',
                'num': 39,
                'onFlinch': False,
                'rating': 1.5,
                'shortDesc': 'This Pokemon cannot be made to flinch.'},
 'insomnia': {'id': 'insomnia',
              'name': 'Insomnia',
              'num': 15,
              'onSetStatus': insomnia.onSetStatus,
              'onUpdate': insomnia.onUpdate,
              'rating': 2,
              'shortDesc': 'This Pokemon cannot fall asleep. Gaining this '
                           'Ability while asleep cures it.'},
 'intimidate': {'desc': 'On switch-in, this Pokemon lowers the Attack of '
                        'adjacent opposing Pokemon by 1 stage. Pokemon behind '
                        'a substitute are immune.',
                'id': 'intimidate',
                'name': 'Intimidate',
                'num': 22,
                'onStart': intimidate.onStart,
                'rating': 3.5,
                'shortDesc': 'On switch-in, this Pokemon lowers the Attack of '
                             'adjacent opponents by 1 stage.'},
 'ironbarbs': {'desc': 'Pokemon making contact with this Pokemon lose 1/8 of '
                       'their maximum HP, rounded down.',
               'id': 'ironbarbs',
               'name': 'Iron Barbs',
               'num': 160,
               'onAfterDamage': ironbarbs.onAfterDamage,
               'onAfterDamageOrder': 1,
               'rating': 3,
               'shortDesc': 'Pokemon making contact with this Pokemon lose 1/8 '
                            'of their max HP.'},
 'ironfist': {'desc': "This Pokemon's punch-based attacks have their power "
                      'multiplied by 1.2.',
              'id': 'ironfist',
              'name': 'Iron Fist',
              'num': 89,
              'onBasePower': ironfist.onBasePower,
              'onBasePowerPriority': 8,
              'rating': 3,
              'shortDesc': "This Pokemon's punch-based attacks have 1.2x "
                           'power. Sucker Punch is not boosted.'},
 'justified': {'id': 'justified',
               'name': 'Justified',
               'num': 154,
               'onAfterDamage': justified.onAfterDamage,
               'rating': 2,
               'shortDesc': "This Pokemon's Attack is raised by 1 stage after "
                            'it is damaged by a Dark-type move.'},
 'keeneye': {'desc': "Prevents other Pokemon from lowering this Pokemon's "
                     "accuracy stat stage. This Pokemon ignores a target's "
                     'evasiveness stat stage.',
             'id': 'keeneye',
             'name': 'Keen Eye',
             'num': 51,
             'onBoost': keeneye.onBoost,
             'onModifyMove': keeneye.onModifyMove,
             'rating': 1,
             'shortDesc': "This Pokemon's accuracy can't be lowered by others; "
                          'ignores their evasiveness stat.'},
 'klutz': {'desc': "This Pokemon's held item has no effect. This Pokemon "
                   'cannot use Fling successfully. Macho Brace, Power Anklet, '
                   'Power Band, Power Belt, Power Bracer, Power Lens, and '
                   'Power Weight still have their effects.',
           'id': 'klutz',
           'name': 'Klutz',
           'num': 103,
           'rating': -1,
           'shortDesc': "This Pokemon's held item has no effect, except Macho "
                        'Brace. Fling cannot be used.'},
 'leafguard': {'desc': 'If Sunny Day is active, this Pokemon cannot gain a '
                       'major status condition and Rest will fail for it.',
               'id': 'leafguard',
               'name': 'Leaf Guard',
               'num': 102,
               'onSetStatus': leafguard.onSetStatus,
               'onTryAddVolatile': leafguard.onTryAddVolatile,
               'rating': 1,
               'shortDesc': 'If Sunny Day is active, this Pokemon cannot be '
                            'statused and Rest will fail for it.'},
 'levitate': {'desc': 'This Pokemon is immune to Ground. Gravity, Ingrain, '
                      'Smack Down, Thousand Arrows, and Iron Ball nullify the '
                      'immunity.',
              'id': 'levitate',
              'name': 'Levitate',
              'num': 26,
              'rating': 3.5,
              'shortDesc': 'This Pokemon is immune to Ground; '
                           'Gravity/Ingrain/Smack Down/Iron Ball nullify it.'},
 'lightmetal': {'id': 'lightmetal',
                'name': 'Light Metal',
                'num': 135,
                'onModifyWeight': lightmetal.onModifyWeight,
                'rating': 1,
                'shortDesc': "This Pokemon's weight is halved."},
 'lightningrod': {'desc': 'This Pokemon is immune to Electric-type moves and '
                          'raises its Special Attack by 1 stage when hit by an '
                          'Electric-type move. If this Pokemon is not the '
                          'target of a single-target Electric-type move used '
                          'by another Pokemon, this Pokemon redirects that '
                          'move to itself if it is within the range of that '
                          'move.',
                  'id': 'lightningrod',
                  'name': 'Lightning Rod',
                  'num': 32,
                  'onAnyRedirectTarget': lightningrod.onAnyRedirectTarget,
                  'onTryHit': lightningrod.onTryHit,
                  'rating': 3.5,
                  'shortDesc': 'This Pokemon draws Electric moves to itself to '
                               'raise Sp. Atk by 1; Electric immunity.'},
 'limber': {'id': 'limber',
            'name': 'Limber',
            'num': 7,
            'onSetStatus': limber.onSetStatus,
            'onUpdate': limber.onUpdate,
            'rating': 1.5,
            'shortDesc': 'This Pokemon cannot be paralyzed. Gaining this '
                         'Ability while paralyzed cures it.'},
 'liquidooze': {'id': 'liquidooze',
                'name': 'Liquid Ooze',
                'num': 64,
                'onSourceTryHeal': liquidooze.onSourceTryHeal,
                'rating': 1.5,
                'shortDesc': 'This Pokemon damages those draining HP from it '
                             'for as much as they would heal.'},
 'liquidvoice': {'desc': "This Pokemon's sound-based moves become Water-type "
                         'moves. This effect comes after other effects that '
                         "change a move's type, but before Ion Deluge and "
                         "Electrify's effects.",
                 'id': 'liquidvoice',
                 'name': 'Liquid Voice',
                 'num': 204,
                 'onModifyMove': liquidvoice.onModifyMove,
                 'onModifyMovePriority': -1,
                 'rating': 2.5,
                 'shortDesc': "This Pokemon's sound-based moves become Water "
                              'type.'},
 'longreach': {'id': 'longreach',
               'name': 'Long Reach',
               'num': 203,
               'onModifyMove': longreach.onModifyMove,
               'rating': 1.5,
               'shortDesc': "This Pokemon's attacks do not make contact with "
                            'the target.'},
 'magicbounce': {'desc': 'This Pokemon blocks certain status moves and instead '
                         'uses the move against the original user.',
                 'effect': {'duration': 1},
                 'id': 'magicbounce',
                 'name': 'Magic Bounce',
                 'num': 156,
                 'onAllyTryHitSide': magicbounce.onAllyTryHitSide,
                 'onTryHit': magicbounce.onTryHit,
                 'onTryHitPriority': 1,
                 'rating': 4.5,
                 'shortDesc': 'This Pokemon blocks certain status moves and '
                              'bounces them back to the user.'},
 'magicguard': {'desc': 'This Pokemon can only be damaged by direct attacks. '
                        'Curse and Substitute on use, Belly Drum, Pain Split, '
                        'Struggle recoil, and confusion damage are considered '
                        'direct damage.',
                'id': 'magicguard',
                'name': 'Magic Guard',
                'num': 98,
                'onDamage': magicguard.onDamage,
                'rating': 4.5,
                'shortDesc': 'This Pokemon can only be damaged by direct '
                             'attacks.'},
 'magician': {'desc': 'If this Pokemon has no item, it steals the item off a '
                      'Pokemon it hits with an attack. Does not affect Doom '
                      'Desire and Future Sight.',
              'id': 'magician',
              'name': 'Magician',
              'num': 170,
              'onSourceHit': magician.onSourceHit,
              'rating': 1.5,
              'shortDesc': 'If this Pokemon has no item, it steals the item '
                           'off a Pokemon it hits with an attack.'},
 'magmaarmor': {'id': 'magmaarmor',
                'name': 'Magma Armor',
                'num': 40,
                'onImmunity': magmaarmor.onImmunity,
                'onUpdate': magmaarmor.onUpdate,
                'rating': 0.5,
                'shortDesc': 'This Pokemon cannot be frozen. Gaining this '
                             'Ability while frozen cures it.'},
 'magnetpull': {'desc': 'Prevents adjacent opposing Steel-type Pokemon from '
                        'choosing to switch out unless they are immune to '
                        'trapping.',
                'id': 'magnetpull',
                'name': 'Magnet Pull',
                'num': 42,
                'onFoeMaybeTrapPokemon': magnetpull.onFoeMaybeTrapPokemon,
                'onFoeTrapPokemon': magnetpull.onFoeTrapPokemon,
                'rating': 4.5,
                'shortDesc': 'Prevents adjacent Steel-type foes from choosing '
                             'to switch.'},
 'marvelscale': {'desc': 'If this Pokemon has a major status condition, its '
                         'Defense is multiplied by 1.5.',
                 'id': 'marvelscale',
                 'name': 'Marvel Scale',
                 'num': 63,
                 'onModifyDef': marvelscale.onModifyDef,
                 'onModifyDefPriority': 6,
                 'rating': 2.5,
                 'shortDesc': 'If this Pokemon is statused, its Defense is '
                              '1.5x.'},
 'megalauncher': {'desc': "This Pokemon's pulse moves have their power "
                          'multiplied by 1.5. Heal Pulse restores 3/4 of a '
                          "target's maximum HP, rounded half down.",
                  'id': 'megalauncher',
                  'name': 'Mega Launcher',
                  'num': 178,
                  'onBasePower': megalauncher.onBasePower,
                  'onBasePowerPriority': 8,
                  'rating': 3.5,
                  'shortDesc': "This Pokemon's pulse moves have 1.5x power. "
                               "Heal Pulse heals 3/4 target's max HP."},
 'merciless': {'id': 'merciless',
               'name': 'Merciless',
               'num': 196,
               'onModifyCritRatio': merciless.onModifyCritRatio,
               'rating': 2,
               'shortDesc': "This Pokemon's attacks are critical hits if the "
                            'target is poisoned.'},
 'minus': {'desc': 'If an active ally has this Ability or the Plus Ability, '
                   "this Pokemon's Special Attack is multiplied by 1.5.",
           'id': 'minus',
           'name': 'Minus',
           'num': 58,
           'onModifySpA': minus.onModifySpA,
           'onModifySpAPriority': 5,
           'rating': 0,
           'shortDesc': 'If an active ally has this Ability or the Plus '
                        "Ability, this Pokemon's Sp. Atk is 1.5x."},
 'mistysurge': {'id': 'mistysurge',
                'name': 'Misty Surge',
                'num': 228,
                'onStart': mistysurge.onStart,
                'rating': 4,
                'shortDesc': 'On switch-in, this Pokemon summons Misty '
                             'Terrain.'},
 'moldbreaker': {'id': 'moldbreaker',
                 'name': 'Mold Breaker',
                 'num': 104,
                 'onModifyMove': moldbreaker.onModifyMove,
                 'onStart': moldbreaker.onStart,
                 'rating': 3.5,
                 'shortDesc': "This Pokemon's moves and their effects ignore "
                              'the Abilities of other Pokemon.'},
 'moody': {'desc': 'This Pokemon has a random stat raised by 2 stages and '
                   'another stat lowered by 1 stage at the end of each turn.',
           'id': 'moody',
           'name': 'Moody',
           'num': 141,
           'onResidual': moody.onResidual,
           'onResidualOrder': 26,
           'onResidualSubOrder': 1,
           'rating': 5,
           'shortDesc': 'Raises a random stat by 2 and lowers another stat by '
                        '1 at the end of each turn.'},
 'motordrive': {'desc': 'This Pokemon is immune to Electric-type moves and '
                        'raises its Speed by 1 stage when hit by an '
                        'Electric-type move.',
                'id': 'motordrive',
                'name': 'Motor Drive',
                'num': 78,
                'onTryHit': motordrive.onTryHit,
                'rating': 3,
                'shortDesc': "This Pokemon's Speed is raised 1 stage if hit by "
                             'an Electric move; Electric immunity.'},
 'mountaineer': {'id': 'mountaineer',
                 'isNonstandard': True,
                 'name': 'Mountaineer',
                 'num': -2,
                 'onDamage': mountaineer.onDamage,
                 'onTryHit': mountaineer.onTryHit,
                 'rating': 3.5,
                 'shortDesc': 'On switch-in, this Pokemon avoids all Rock-type '
                              'attacks and Stealth Rock.'},
 'moxie': {'desc': "This Pokemon's Attack is raised by 1 stage if it attacks "
                   'and knocks out another Pokemon.',
           'id': 'moxie',
           'name': 'Moxie',
           'num': 153,
           'onSourceFaint': moxie.onSourceFaint,
           'rating': 3.5,
           'shortDesc': "This Pokemon's Attack is raised by 1 stage if it "
                        'attacks and KOes another Pokemon.'},
 'multiscale': {'id': 'multiscale',
                'name': 'Multiscale',
                'num': 136,
                'onSourceModifyDamage': multiscale.onSourceModifyDamage,
                'rating': 4,
                'shortDesc': 'If this Pokemon is at full HP, damage taken from '
                             'attacks is halved.'},
 'multitype': {'id': 'multitype',
               'name': 'Multitype',
               'num': 121,
               'rating': 4,
               'shortDesc': 'If this Pokemon is an Arceus, its type changes to '
                            'match its held Plate or Z-Crystal.'},
 'mummy': {'desc': 'Pokemon making contact with this Pokemon have their '
                   'Ability changed to Mummy. Does not affect the Battle Bond, '
                   'Comatose, Disguise, Multitype, Power Construct, RKS '
                   'System, Schooling, Shields Down, and Stance Change '
                   'Abilities.',
           'id': 'mummy',
           'name': 'Mummy',
           'num': 152,
           'onAfterDamage': mummy.onAfterDamage,
           'onBasePower': mummy.onBasePower,
           'rating': 2,
           'shortDesc': 'Pokemon making contact with this Pokemon have their '
                        'Ability changed to Mummy.'},
 'naturalcure': {'id': 'naturalcure',
                 'name': 'Natural Cure',
                 'num': 30,
                 'onCheckShow': naturalcure.onCheckShow,
                 'onSwitchOut': naturalcure.onSwitchOut,
                 'rating': 3.5,
                 'shortDesc': 'This Pokemon has its major status condition '
                              'cured when it switches out.'},
 'neuroforce': {'id': 'neuroforce',
                'name': 'Neuroforce',
                'num': 233,
                'onModifyDamage': neuroforce.onModifyDamage,
                'rating': 3,
                'shortDesc': "This Pokemon's attacks that are super effective "
                             'against the target do 1.25x damage.'},
 'noability': {'id': 'noability',
               'isNonstandard': 'gen2',
               'name': 'No Ability',
               'num': 0,
               'rating': 0.1,
               'shortDesc': 'Does nothing.'},
 'noguard': {'id': 'noguard',
             'name': 'No Guard',
             'num': 99,
             'onAnyAccuracy': noguard.onAnyAccuracy,
             'rating': 4,
             'shortDesc': 'Every move used by or against this Pokemon will '
                          'always hit.'},
 'normalize': {'desc': "This Pokemon's moves are changed to be Normal type and "
                       'have their power multiplied by 1.2. This effect comes '
                       "before other effects that change a move's type.",
               'id': 'normalize',
               'name': 'Normalize',
               'num': 96,
               'onBasePower': normalize.onBasePower,
               'onBasePowerPriority': 8,
               'onModifyMove': normalize.onModifyMove,
               'onModifyMovePriority': 1,
               'rating': -1,
               'shortDesc': "This Pokemon's moves are changed to be Normal "
                            'type and have 1.2x power.'},
 'oblivious': {'desc': 'This Pokemon cannot be infatuated or taunted. Gaining '
                       'this Ability while affected cures it.',
               'id': 'oblivious',
               'name': 'Oblivious',
               'num': 12,
               'onImmunity': oblivious.onImmunity,
               'onTryHit': oblivious.onTryHit,
               'onUpdate': oblivious.onUpdate,
               'rating': 1,
               'shortDesc': 'This Pokemon cannot be infatuated or taunted. '
                            'Gaining this Ability cures it.'},
 'overcoat': {'id': 'overcoat',
              'name': 'Overcoat',
              'num': 142,
              'onImmunity': overcoat.onImmunity,
              'onTryHit': overcoat.onTryHit,
              'onTryHitPriority': 1,
              'rating': 2.5,
              'shortDesc': 'This Pokemon is immune to powder moves and damage '
                           'from Sandstorm or Hail.'},
 'overgrow': {'desc': 'When this Pokemon has 1/3 or less of its maximum HP, '
                      'rounded down, its attacking stat is multiplied by 1.5 '
                      'while using a Grass-type attack.',
              'id': 'overgrow',
              'name': 'Overgrow',
              'num': 65,
              'onModifyAtk': overgrow.onModifyAtk,
              'onModifyAtkPriority': 5,
              'onModifySpA': overgrow.onModifySpA,
              'onModifySpAPriority': 5,
              'rating': 2,
              'shortDesc': "At 1/3 or less of its max HP, this Pokemon's "
                           'attacking stat is 1.5x with Grass attacks.'},
 'owntempo': {'id': 'owntempo',
              'name': 'Own Tempo',
              'num': 20,
              'onHit': owntempo.onHit,
              'onTryAddVolatile': owntempo.onTryAddVolatile,
              'onUpdate': owntempo.onUpdate,
              'rating': 1.5,
              'shortDesc': 'This Pokemon cannot be confused. Gaining this '
                           'Ability while confused cures it.'},
 'parentalbond': {'desc': "This Pokemon's damaging moves become multi-hit "
                          'moves that hit twice. The second hit has its damage '
                          'quartered. Does not affect multi-hit moves or moves '
                          'that have multiple targets.',
                  'id': 'parentalbond',
                  'name': 'Parental Bond',
                  'num': 184,
                  'onBasePower': parentalbond.onBasePower,
                  'onBasePowerPriority': 8,
                  'onPrepareHit': parentalbond.onPrepareHit,
                  'onSourceModifySecondaries': parentalbond.onSourceModifySecondaries,
                  'rating': 5,
                  'shortDesc': "This Pokemon's damaging moves hit twice. The "
                               'second hit has its damage quartered.'},
 'persistent': {'desc': 'The duration of Gravity, Heal Block, Magic Room, '
                        'Safeguard, Tailwind, Trick Room, and Wonder Room is '
                        'increased by 2 turns if the effect is started by this '
                        'Pokemon.',
                'id': 'persistent',
                'isNonstandard': True,
                'name': 'Persistent',
                'num': -4,
                'rating': 3.5,
                'shortDesc': 'When used, Gravity/Heal '
                             'Block/Safeguard/Tailwind/Room effects last 2 '
                             'more turns.'},
 'pickpocket': {'desc': 'If this Pokemon has no item, it steals the item off a '
                        'Pokemon that makes contact with it. This effect '
                        'applies after all hits from a multi-hit move; Sheer '
                        'Force prevents it from activating if the move has a '
                        'secondary effect.',
                'id': 'pickpocket',
                'name': 'Pickpocket',
                'num': 124,
                'onAfterMoveSecondary': pickpocket.onAfterMoveSecondary,
                'rating': 1,
                'shortDesc': 'If this Pokemon has no item, it steals the item '
                             'off a Pokemon making contact with it.'},
 'pickup': {'id': 'pickup',
            'name': 'Pickup',
            'num': 53,
            'onResidual': pickup.onResidual,
            'onResidualOrder': 26,
            'onResidualSubOrder': 1,
            'rating': 0.5,
            'shortDesc': 'If this Pokemon has no item, it finds one used by an '
                         'adjacent Pokemon this turn.'},
 'pixilate': {'desc': "This Pokemon's Normal-type moves become Fairy-type "
                      'moves and have their power multiplied by 1.2. This '
                      "effect comes after other effects that change a move's "
                      "type, but before Ion Deluge and Electrify's effects.",
              'id': 'pixilate',
              'name': 'Pixilate',
              'num': 182,
              'onBasePower': pixilate.onBasePower,
              'onBasePowerPriority': 8,
              'onModifyMove': pixilate.onModifyMove,
              'onModifyMovePriority': -1,
              'rating': 4,
              'shortDesc': "This Pokemon's Normal-type moves become Fairy type "
                           'and have 1.2x power.'},
 'plus': {'desc': 'If an active ally has this Ability or the Minus Ability, '
                  "this Pokemon's Special Attack is multiplied by 1.5.",
          'id': 'plus',
          'name': 'Plus',
          'num': 57,
          'onModifySpA': plus.onModifySpA,
          'onModifySpAPriority': 5,
          'rating': 0,
          'shortDesc': 'If an active ally has this Ability or the Minus '
                       "Ability, this Pokemon's Sp. Atk is 1.5x."},
 'poisonheal': {'desc': 'If this Pokemon is poisoned, it restores 1/8 of its '
                        'maximum HP, rounded down, at the end of each turn '
                        'instead of losing HP.',
                'id': 'poisonheal',
                'name': 'Poison Heal',
                'num': 90,
                'onDamage': poisonheal.onDamage,
                'onDamagePriority': 1,
                'rating': 4,
                'shortDesc': 'This Pokemon is healed by 1/8 of its max HP each '
                             'turn when poisoned; no HP loss.'},
 'poisonpoint': {'id': 'poisonpoint',
                 'name': 'Poison Point',
                 'num': 38,
                 'onAfterDamage': poisonpoint.onAfterDamage,
                 'rating': 2,
                 'shortDesc': '30% chance a Pokemon making contact with this '
                              'Pokemon will be poisoned.'},
 'poisontouch': {'id': 'poisontouch',
                 'name': 'Poison Touch',
                 'num': 143,
                 'onModifyMove': poisontouch.onModifyMove,
                 'rating': 2,
                 'shortDesc': "This Pokemon's contact moves have a 30% chance "
                              'of poisoning.'},
 'powerconstruct': {'desc': 'If this Pokemon is a Zygarde in its 10% or 50% '
                            'Forme, it changes to Complete Forme when it has '
                            '1/2 or less of its maximum HP at the end of the '
                            'turn.',
                    'id': 'powerconstruct',
                    'name': 'Power Construct',
                    'num': 211,
                    'onResidual': powerconstruct.onResidual,
                    'onResidualOrder': 27,
                    'rating': 4,
                    'shortDesc': 'If Zygarde 10%/50%, changes to Complete if '
                                 'at 1/2 max HP or less at end of turn.'},
 'powerofalchemy': {'desc': 'This Pokemon copies the Ability of an ally that '
                            'faints. Abilities that cannot be copied are '
                            'Flower Gift, Forecast, Illusion, Imposter, '
                            'Multitype, Stance Change, Trace, Wonder Guard, '
                            'and Zen Mode.',
                    'id': 'powerofalchemy',
                    'name': 'Power of Alchemy',
                    'num': 223,
                    'onAllyFaint': powerofalchemy.onAllyFaint,
                    'rating': 0,
                    'shortDesc': 'This Pokemon copies the Ability of an ally '
                                 'that faints.'},
 'prankster': {'id': 'prankster',
               'name': 'Prankster',
               'num': 158,
               'onModifyPriority': prankster.onModifyPriority,
               'rating': 4,
               'shortDesc': "This Pokemon's Status moves have priority raised "
                            'by 1, but Dark types are immune.'},
 'pressure': {'desc': "If this Pokemon is the target of an opposing Pokemon's "
                      'move, that move loses one additional PP.',
              'id': 'pressure',
              'name': 'Pressure',
              'num': 46,
              'onDeductPP': pressure.onDeductPP,
              'onStart': pressure.onStart,
              'rating': 2,
              'shortDesc': "If this Pokemon is the target of a foe's move, "
                           'that move loses one additional PP.'},
 'primordialsea': {'desc': 'On switch-in, the weather becomes heavy rain that '
                           'prevents damaging Fire-type moves from executing, '
                           'in addition to all the effects of Rain Dance. This '
                           'weather remains in effect until this Ability is no '
                           'longer active for any Pokemon, or the weather is '
                           'changed by Delta Stream or Desolate Land.',
                   'id': 'primordialsea',
                   'name': 'Primordial Sea',
                   'num': 189,
                   'onAnySetWeather': primordialsea.onAnySetWeather,
                   'onEnd': primordialsea.onEnd,
                   'onStart': primordialsea.onStart,
                   'rating': 5,
                   'shortDesc': 'On switch-in, heavy rain begins until this '
                                'Ability is not active in battle.'},
 'prismarmor': {'desc': 'This Pokemon receives 3/4 damage from supereffective '
                        'attacks. Moongeist Beam, Sunsteel Strike, and the '
                        'Mold Breaker, Teravolt, and Turboblaze Abilities '
                        'cannot ignore this Ability.',
                'id': 'prismarmor',
                'isUnbreakable': True,
                'name': 'Prism Armor',
                'num': 232,
                'onSourceModifyDamage': prismarmor.onSourceModifyDamage,
                'rating': 3,
                'shortDesc': 'This Pokemon receives 3/4 damage from '
                             'supereffective attacks.'},
 'protean': {'desc': "This Pokemon's type changes to match the type of the "
                     'move it is about to use. This effect comes after all '
                     "effects that change a move's type.",
             'id': 'protean',
             'name': 'Protean',
             'num': 168,
             'onPrepareHit': protean.onPrepareHit,
             'rating': 4,
             'shortDesc': "This Pokemon's type changes to match the type of "
                          'the move it is about to use.'},
 'psychicsurge': {'id': 'psychicsurge',
                  'name': 'Psychic Surge',
                  'num': 227,
                  'onStart': psychicsurge.onStart,
                  'rating': 4,
                  'shortDesc': 'On switch-in, this Pokemon summons Psychic '
                               'Terrain.'},
 'purepower': {'id': 'purepower',
               'name': 'Pure Power',
               'num': 74,
               'onModifyAtk': purepower.onModifyAtk,
               'onModifyAtkPriority': 5,
               'rating': 5,
               'shortDesc': "This Pokemon's Attack is doubled."},
 'queenlymajesty': {'desc': 'While this Pokemon is active, priority moves from '
                            'opposing Pokemon targeted at allies are prevented '
                            'from having an effect.',
                    'id': 'queenlymajesty',
                    'name': 'Queenly Majesty',
                    'num': 214,
                    'onFoeTryMove': queenlymajesty.onFoeTryMove,
                    'rating': 3,
                    'shortDesc': 'While this Pokemon is active, allies are '
                                 'protected from opposing priority moves.'},
 'quickfeet': {'desc': 'If this Pokemon has a major status condition, its '
                       'Speed is multiplied by 1.5; the Speed drop from '
                       'paralysis is ignored.',
               'id': 'quickfeet',
               'name': 'Quick Feet',
               'num': 95,
               'onModifySpe': quickfeet.onModifySpe,
               'rating': 2.5,
               'shortDesc': 'If this Pokemon is statused, its Speed is 1.5x; '
                            'ignores Speed drop from paralysis.'},
 'raindish': {'desc': 'If Rain Dance is active, this Pokemon restores 1/16 of '
                      'its maximum HP, rounded down, at the end of each turn.',
              'id': 'raindish',
              'name': 'Rain Dish',
              'num': 44,
              'onWeather': raindish.onWeather,
              'rating': 1.5,
              'shortDesc': 'If Rain Dance is active, this Pokemon heals 1/16 '
                           'of its max HP each turn.'},
 'rattled': {'desc': "This Pokemon's Speed is raised by 1 stage if hit by a "
                     'Bug-, Dark-, or Ghost-type attack.',
             'id': 'rattled',
             'name': 'Rattled',
             'num': 155,
             'onAfterDamage': rattled.onAfterDamage,
             'rating': 1.5,
             'shortDesc': "This Pokemon's Speed is raised 1 stage if hit by a "
                          'Bug-, Dark-, or Ghost-type attack.'},
 'rebound': {'desc': 'On switch-in, this Pokemon blocks certain status moves '
                     'and instead uses the move against the original user.',
             'effect': {'duration': 1},
             'id': 'rebound',
             'isNonstandard': True,
             'name': 'Rebound',
             'num': -3,
             'onAllyTryHitSide': rebound.onAllyTryHitSide,
             'onTryHit': rebound.onTryHit,
             'onTryHitPriority': 1,
             'rating': 3.5,
             'shortDesc': 'On switch-in, blocks certain status moves and '
                          'bounces them back to the user.'},
 'receiver': {'desc': 'This Pokemon copies the Ability of an ally that faints. '
                      'Abilities that cannot be copied are Flower Gift, '
                      'Forecast, Illusion, Imposter, Multitype, Stance Change, '
                      'Trace, Wonder Guard, and Zen Mode.',
              'id': 'receiver',
              'name': 'Receiver',
              'num': 222,
              'onAllyFaint': receiver.onAllyFaint,
              'rating': 0,
              'shortDesc': 'This Pokemon copies the Ability of an ally that '
                           'faints.'},
 'reckless': {'desc': "This Pokemon's attacks with recoil or crash damage have "
                      'their power multiplied by 1.2. Does not affect '
                      'Struggle.',
              'id': 'reckless',
              'name': 'Reckless',
              'num': 120,
              'onBasePower': reckless.onBasePower,
              'onBasePowerPriority': 8,
              'rating': 3,
              'shortDesc': "This Pokemon's attacks with recoil or crash damage "
                           'have 1.2x power; not Struggle.'},
 'refrigerate': {'desc': "This Pokemon's Normal-type moves become Ice-type "
                         'moves and have their power multiplied by 1.2. This '
                         'effect comes after other effects that change a '
                         "move's type, but before Ion Deluge and Electrify's "
                         'effects.',
                 'id': 'refrigerate',
                 'name': 'Refrigerate',
                 'num': 174,
                 'onBasePower': refrigerate.onBasePower,
                 'onBasePowerPriority': 8,
                 'onModifyMove': refrigerate.onModifyMove,
                 'onModifyMovePriority': -1,
                 'rating': 4,
                 'shortDesc': "This Pokemon's Normal-type moves become Ice "
                              'type and have 1.2x power.'},
 'regenerator': {'id': 'regenerator',
                 'name': 'Regenerator',
                 'num': 144,
                 'onSwitchOut': regenerator.onSwitchOut,
                 'rating': 4,
                 'shortDesc': 'This Pokemon restores 1/3 of its maximum HP, '
                              'rounded down, when it switches out.'},
 'rivalry': {'desc': "This Pokemon's attacks have their power multiplied by "
                     '1.25 against targets of the same gender or multiplied by '
                     '0.75 against targets of the opposite gender. There is no '
                     'modifier if either this Pokemon or the target is '
                     'genderless.',
             'id': 'rivalry',
             'name': 'Rivalry',
             'num': 79,
             'onBasePower': rivalry.onBasePower,
             'onBasePowerPriority': 8,
             'rating': 0.5,
             'shortDesc': "This Pokemon's attacks do 1.25x on same gender "
                          'targets; 0.75x on opposite gender.'},
 'rkssystem': {'id': 'rkssystem',
               'name': 'RKS System',
               'num': 225,
               'rating': 4,
               'shortDesc': 'If this Pokemon is a Silvally, its type changes '
                            'to match its held Memory.'},
 'rockhead': {'desc': 'This Pokemon does not take recoil damage besides '
                      'Struggle, Life Orb, and crash damage.',
              'id': 'rockhead',
              'name': 'Rock Head',
              'num': 69,
              'onDamage': rockhead.onDamage,
              'rating': 2.5,
              'shortDesc': 'This Pokemon does not take recoil damage besides '
                           'Struggle/Life Orb/crash damage.'},
 'roughskin': {'desc': 'Pokemon making contact with this Pokemon lose 1/8 of '
                       'their maximum HP, rounded down.',
               'id': 'roughskin',
               'name': 'Rough Skin',
               'num': 24,
               'onAfterDamage': roughskin.onAfterDamage,
               'onAfterDamageOrder': 1,
               'rating': 3,
               'shortDesc': 'Pokemon making contact with this Pokemon lose 1/8 '
                            'of their max HP.'},
 'runaway': {'id': 'runaway',
             'name': 'Run Away',
             'num': 50,
             'rating': 0,
             'shortDesc': 'No competitive use.'},
 'sandforce': {'desc': "If Sandstorm is active, this Pokemon's Ground-, Rock-, "
                       'and Steel-type attacks have their power multiplied by '
                       '1.3. This Pokemon takes no damage from Sandstorm.',
               'id': 'sandforce',
               'name': 'Sand Force',
               'num': 159,
               'onBasePower': sandforce.onBasePower,
               'onBasePowerPriority': 8,
               'onImmunity': sandforce.onImmunity,
               'rating': 2,
               'shortDesc': "This Pokemon's Ground/Rock/Steel attacks do 1.3x "
                            'in Sandstorm; immunity to it.'},
 'sandrush': {'desc': "If Sandstorm is active, this Pokemon's Speed is "
                      'doubled. This Pokemon takes no damage from Sandstorm.',
              'id': 'sandrush',
              'name': 'Sand Rush',
              'num': 146,
              'onImmunity': sandrush.onImmunity,
              'onModifySpe': sandrush.onModifySpe,
              'rating': 3,
              'shortDesc': "If Sandstorm is active, this Pokemon's Speed is "
                           'doubled; immunity to Sandstorm.'},
 'sandstream': {'id': 'sandstream',
                'name': 'Sand Stream',
                'num': 45,
                'onStart': sandstream.onStart,
                'rating': 4.5,
                'shortDesc': 'On switch-in, this Pokemon summons Sandstorm.'},
 'sandveil': {'desc': "If Sandstorm is active, this Pokemon's evasiveness is "
                      'multiplied by 1.25. This Pokemon takes no damage from '
                      'Sandstorm.',
              'id': 'sandveil',
              'name': 'Sand Veil',
              'num': 8,
              'onImmunity': sandveil.onImmunity,
              'onModifyAccuracy': sandveil.onModifyAccuracy,
              'rating': 1.5,
              'shortDesc': "If Sandstorm is active, this Pokemon's evasiveness "
                           'is 1.25x; immunity to Sandstorm.'},
 'sapsipper': {'desc': 'This Pokemon is immune to Grass-type moves and raises '
                       'its Attack by 1 stage when hit by a Grass-type move.',
               'id': 'sapsipper',
               'name': 'Sap Sipper',
               'num': 157,
               'onAllyTryHitSide': sapsipper.onAllyTryHitSide,
               'onTryHit': sapsipper.onTryHit,
               'onTryHitPriority': 1,
               'rating': 3.5,
               'shortDesc': "This Pokemon's Attack is raised 1 stage if hit by "
                            'a Grass move; Grass immunity.'},
 'schooling': {'desc': 'On switch-in, if this Pokemon is a Wishiwashi that is '
                       'level 20 or above and has more than 1/4 of its maximum '
                       'HP left, it changes to School Form. If it is in School '
                       'Form and its HP drops to 1/4 of its maximum HP or '
                       'less, it changes to Solo Form at the end of the turn. '
                       'If it is in Solo Form and its HP is greater than 1/4 '
                       'its maximum HP at the end of the turn, it changes to '
                       'School Form.',
               'id': 'schooling',
               'name': 'Schooling',
               'num': 208,
               'onResidual': schooling.onResidual,
               'onResidualOrder': 27,
               'onStart': schooling.onStart,
               'rating': 3,
               'shortDesc': 'If user is Wishiwashi, changes to School Form if '
                            'it has > 1/4 max HP, else Solo Form.'},
 'scrappy': {'id': 'scrappy',
             'name': 'Scrappy',
             'num': 113,
             'onModifyMove': scrappy.onModifyMove,
             'onModifyMovePriority': -5,
             'rating': 3,
             'shortDesc': 'This Pokemon can hit Ghost types with Normal- and '
                          'Fighting-type moves.'},
 'serenegrace': {'id': 'serenegrace',
                 'name': 'Serene Grace',
                 'num': 32,
                 'onModifyMove': serenegrace.onModifyMove,
                 'onModifyMovePriority': -2,
                 'rating': 4,
                 'shortDesc': "This Pokemon's moves have their secondary "
                              'effect chance doubled.'},
 'shadowshield': {'desc': 'If this Pokemon is at full HP, damage taken from '
                          'attacks is halved. Moongeist Beam, Sunsteel Strike, '
                          'and the Mold Breaker, Teravolt, and Turboblaze '
                          'Abilities cannot ignore this Ability.',
                  'id': 'shadowshield',
                  'isUnbreakable': True,
                  'name': 'Shadow Shield',
                  'num': 231,
                  'onSourceModifyDamage': shadowshield.onSourceModifyDamage,
                  'rating': 4,
                  'shortDesc': 'If this Pokemon is at full HP, damage taken '
                               'from attacks is halved.'},
 'shadowtag': {'desc': 'Prevents adjacent opposing Pokemon from choosing to '
                       'switch out unless they are immune to trapping or also '
                       'have this Ability.',
               'id': 'shadowtag',
               'name': 'Shadow Tag',
               'num': 23,
               'onFoeMaybeTrapPokemon': shadowtag.onFoeMaybeTrapPokemon,
               'onFoeTrapPokemon': shadowtag.onFoeTrapPokemon,
               'rating': 5,
               'shortDesc': 'Prevents adjacent foes from choosing to switch '
                            'unless they also have this Ability.'},
 'shedskin': {'desc': 'This Pokemon has a 33% chance to have its major status '
                      'condition cured at the end of each turn.',
              'id': 'shedskin',
              'name': 'Shed Skin',
              'num': 61,
              'onResidual': shedskin.onResidual,
              'onResidualOrder': 5,
              'onResidualSubOrder': 1,
              'rating': 3.5,
              'shortDesc': 'This Pokemon has a 33% chance to have its status '
                           'cured at the end of each turn.'},
 'sheerforce': {'desc': "This Pokemon's attacks with secondary effects have "
                        'their power multiplied by 1.3, but the secondary '
                        'effects are removed.',
                'id': 'sheerforce',
                'name': 'Sheer Force',
                'num': 125,
                'onBasePower': sheerforce.onBasePower,
                'onBasePowerPriority': 8,
                'onModifyMove': sheerforce.onModifyMove,
                'rating': 4,
                'shortDesc': "This Pokemon's attacks with secondary effects "
                             'have 1.3x power; nullifies the effects.'},
 'shellarmor': {'id': 'shellarmor',
                'name': 'Shell Armor',
                'num': 75,
                'onCriticalHit': False,
                'rating': 1,
                'shortDesc': 'This Pokemon cannot be struck by a critical '
                             'hit.'},
 'shielddust': {'id': 'shielddust',
                'name': 'Shield Dust',
                'num': 19,
                'onModifySecondaries': shielddust.onModifySecondaries,
                'rating': 2.5,
                'shortDesc': 'This Pokemon is not affected by the secondary '
                             "effect of another Pokemon's attack."},
 'shieldsdown': {'desc': 'If this Pokemon is a Minior, it changes to its Core '
                         'forme if it has 1/2 or less of its maximum HP, and '
                         'changes to Meteor Form if it has more than 1/2 its '
                         'maximum HP. This check is done on switch-in and at '
                         'the end of each turn. While in its Meteor Form, it '
                         'cannot become affected by major status conditions. '
                         'Moongeist Beam, Sunsteel Strike, and the Mold '
                         'Breaker, Teravolt, and Turboblaze Abilities cannot '
                         'ignore this Ability.',
                 'id': 'shieldsdown',
                 'isUnbreakable': True,
                 'name': 'Shields Down',
                 'num': 197,
                 'onResidual': shieldsdown.onResidual,
                 'onResidualOrder': 27,
                 'onSetStatus': shieldsdown.onSetStatus,
                 'onStart': shieldsdown.onStart,
                 'onTryAddVolatile': shieldsdown.onTryAddVolatile,
                 'rating': 3,
                 'shortDesc': 'If Minior, switch-in/end of turn it changes to '
                              'Core at 1/2 max HP or less, else Meteor.'},
 'simple': {'id': 'simple',
            'name': 'Simple',
            'num': 86,
            'onBoost': simple.onBoost,
            'rating': 4,
            'shortDesc': "When this Pokemon's stat stages are raised or "
                         'lowered, the effect is doubled instead.'},
 'skilllink': {'id': 'skilllink',
               'name': 'Skill Link',
               'num': 92,
               'onModifyMove': skilllink.onModifyMove,
               'rating': 4,
               'shortDesc': "This Pokemon's multi-hit attacks always hit the "
                            'maximum number of times.'},
 'slowstart': {'effect': {'duration': 5,
                          'onEnd': slowstart.onEnd,
                          'onModifyAtk': slowstart.onModifyAtk,
                          'onModifyAtkPriority': 5,
                          'onModifySpe': slowstart.onModifySpe,
                          'onStart': slowstart.onStart},
               'id': 'slowstart',
               'name': 'Slow Start',
               'num': 112,
               'onEnd': slowstart.onEnd,
               'onStart': slowstart.onStart,
               'rating': -2,
               'shortDesc': "On switch-in, this Pokemon's Attack and Speed are "
                            'halved for 5 turns.'},
 'slushrush': {'id': 'slushrush',
               'name': 'Slush Rush',
               'num': 202,
               'onModifySpe': slushrush.onModifySpe,
               'rating': 2.5,
               'shortDesc': "If Hail is active, this Pokemon's Speed is "
                            'doubled.'},
 'sniper': {'id': 'sniper',
            'name': 'Sniper',
            'num': 97,
            'onModifyDamage': sniper.onModifyDamage,
            'rating': 1,
            'shortDesc': 'If this Pokemon strikes with a critical hit, the '
                         'damage is multiplied by 1.5.'},
 'snowcloak': {'desc': "If Hail is active, this Pokemon's evasiveness is "
                       'multiplied by 1.25. This Pokemon takes no damage from '
                       'Hail.',
               'id': 'snowcloak',
               'name': 'Snow Cloak',
               'num': 81,
               'onImmunity': snowcloak.onImmunity,
               'onModifyAccuracy': snowcloak.onModifyAccuracy,
               'rating': 1.5,
               'shortDesc': "If Hail is active, this Pokemon's evasiveness is "
                            '1.25x; immunity to Hail.'},
 'snowwarning': {'id': 'snowwarning',
                 'name': 'Snow Warning',
                 'num': 117,
                 'onStart': snowwarning.onStart,
                 'rating': 4,
                 'shortDesc': 'On switch-in, this Pokemon summons Hail.'},
 'solarpower': {'desc': "If Sunny Day is active, this Pokemon's Special Attack "
                        'is multiplied by 1.5 and it loses 1/8 of its maximum '
                        'HP, rounded down, at the end of each turn.',
                'id': 'solarpower',
                'name': 'Solar Power',
                'num': 94,
                'onModifySpA': solarpower.onModifySpA,
                'onModifySpAPriority': 5,
                'onWeather': solarpower.onWeather,
                'rating': 1.5,
                'shortDesc': "If Sunny Day is active, this Pokemon's Sp. Atk "
                             'is 1.5x; loses 1/8 max HP per turn.'},
 'solidrock': {'id': 'solidrock',
               'name': 'Solid Rock',
               'num': 116,
               'onSourceModifyDamage': solidrock.onSourceModifyDamage,
               'rating': 3,
               'shortDesc': 'This Pokemon receives 3/4 damage from '
                            'supereffective attacks.'},
 'soulheart': {'desc': "This Pokemon's Special Attack is raised by 1 stage "
                       'when another Pokemon faints.',
               'id': 'soulheart',
               'name': 'Soul-Heart',
               'num': 220,
               'onAnyFaint': soulheart.onAnyFaint,
               'onAnyFaintPriority': 1,
               'rating': 3.5,
               'shortDesc': "This Pokemon's Sp. Atk is raised by 1 stage when "
                            'another Pokemon faints.'},
 'soundproof': {'id': 'soundproof',
                'name': 'Soundproof',
                'num': 43,
                'onAllyTryHitSide': soundproof.onAllyTryHitSide,
                'onTryHit': soundproof.onTryHit,
                'rating': 2,
                'shortDesc': 'This Pokemon is immune to sound-based moves, '
                             'including Heal Bell.'},
 'speedboost': {'desc': "This Pokemon's Speed is raised by 1 stage at the end "
                        'of each full turn it has been on the field.',
                'id': 'speedboost',
                'name': 'Speed Boost',
                'num': 3,
                'onResidual': speedboost.onResidual,
                'onResidualOrder': 26,
                'onResidualSubOrder': 1,
                'rating': 4.5,
                'shortDesc': "This Pokemon's Speed is raised 1 stage at the "
                             'end of each full turn on the field.'},
 'stakeout': {'id': 'stakeout',
              'name': 'Stakeout',
              'num': 198,
              'onModifyAtk': stakeout.onModifyAtk,
              'onModifyAtkPriority': 5,
              'onModifySpA': stakeout.onModifySpA,
              'onModifySpAPriority': 5,
              'rating': 2.5,
              'shortDesc': "This Pokemon's attacking stat is doubled against a "
                           'target that switched in this turn.'},
 'stall': {'id': 'stall',
           'name': 'Stall',
           'num': 100,
           'onModifyPriority': stall.onModifyPriority,
           'rating': -1,
           'shortDesc': 'This Pokemon moves last among Pokemon using the same '
                        'or greater priority moves.'},
 'stamina': {'id': 'stamina',
             'name': 'Stamina',
             'num': 192,
             'onAfterDamage': stamina.onAfterDamage,
             'rating': 3,
             'shortDesc': "This Pokemon's Defense is raised by 1 stage after "
                          'it is damaged by a move.'},
 'stancechange': {'desc': 'If this Pokemon is an Aegislash, it changes to '
                          'Blade Forme before attempting to use an attacking '
                          'move, and changes to Shield Forme before attempting '
                          "to use King's Shield.",
                  'id': 'stancechange',
                  'name': 'Stance Change',
                  'num': 176,
                  'onBeforeMove': stancechange.onBeforeMove,
                  'onBeforeMovePriority': 0.5,
                  'rating': 5,
                  'shortDesc': 'If Aegislash, changes Forme to Blade before '
                               "attacks and Shield before King's Shield."},
 'static': {'id': 'static',
            'name': 'Static',
            'num': 9,
            'onAfterDamage': static.onAfterDamage,
            'rating': 2,
            'shortDesc': '30% chance a Pokemon making contact with this '
                         'Pokemon will be paralyzed.'},
 'steadfast': {'id': 'steadfast',
               'name': 'Steadfast',
               'num': 80,
               'onFlinch': steadfast.onFlinch,
               'rating': 1,
               'shortDesc': 'If this Pokemon flinches, its Speed is raised by '
                            '1 stage.'},
 'steelworker': {'id': 'steelworker',
                 'name': 'Steelworker',
                 'num': 200,
                 'onModifyAtk': steelworker.onModifyAtk,
                 'onModifyAtkPriority': 5,
                 'onModifySpA': steelworker.onModifySpA,
                 'onModifySpAPriority': 5,
                 'rating': 3,
                 'shortDesc': "This Pokemon's attacking stat is multiplied by "
                              '1.5 while using a Steel-type attack.'},
 'stench': {'id': 'stench',
            'name': 'Stench',
            'num': 1,
            'onModifyMove': stench.onModifyMove,
            'onModifyMovePriority': -1,
            'rating': 0.5,
            'shortDesc': "This Pokemon's attacks without a chance to flinch "
                         'have a 10% chance to flinch.'},
 'stickyhold': {'id': 'stickyhold',
                'name': 'Sticky Hold',
                'num': 60,
                'onTakeItem': stickyhold.onTakeItem,
                'rating': 1.5,
                'shortDesc': 'This Pokemon cannot lose its held item due to '
                             "another Pokemon's attack."},
 'stormdrain': {'desc': 'This Pokemon is immune to Water-type moves and raises '
                        'its Special Attack by 1 stage when hit by a '
                        'Water-type move. If this Pokemon is not the target of '
                        'a single-target Water-type move used by another '
                        'Pokemon, this Pokemon redirects that move to itself '
                        'if it is within the range of that move.',
                'id': 'stormdrain',
                'name': 'Storm Drain',
                'num': 114,
                'onAnyRedirectTarget': stormdrain.onAnyRedirectTarget,
                'onTryHit': stormdrain.onTryHit,
                'rating': 3.5,
                'shortDesc': 'This Pokemon draws Water moves to itself to '
                             'raise Sp. Atk by 1; Water immunity.'},
 'strongjaw': {'desc': "This Pokemon's bite-based attacks have their power "
                       'multiplied by 1.5.',
               'id': 'strongjaw',
               'name': 'Strong Jaw',
               'num': 173,
               'onBasePower': strongjaw.onBasePower,
               'onBasePowerPriority': 8,
               'rating': 3,
               'shortDesc': "This Pokemon's bite-based attacks have 1.5x "
                            'power. Bug Bite is not boosted.'},
 'sturdy': {'desc': 'If this Pokemon is at full HP, it survives one hit with '
                    'at least 1 HP. OHKO moves fail when used against this '
                    'Pokemon.',
            'id': 'sturdy',
            'name': 'Sturdy',
            'num': 5,
            'onDamage': sturdy.onDamage,
            'onDamagePriority': -100,
            'onTryHit': sturdy.onTryHit,
            'rating': 3,
            'shortDesc': 'If this Pokemon is at full HP, it survives one hit '
                         'with at least 1 HP. Immune to OHKO.'},
 'suctioncups': {'id': 'suctioncups',
                 'name': 'Suction Cups',
                 'num': 21,
                 'onDragOut': suctioncups.onDragOut,
                 'onDragOutPriority': 1,
                 'rating': 1.5,
                 'shortDesc': 'This Pokemon cannot be forced to switch out by '
                              "another Pokemon's attack or item."},
 'superluck': {'id': 'superluck',
               'name': 'Super Luck',
               'num': 105,
               'onModifyCritRatio': superluck.onModifyCritRatio,
               'rating': 1.5,
               'shortDesc': "This Pokemon's critical hit ratio is raised by 1 "
                            'stage.'},
 'surgesurfer': {'id': 'surgesurfer',
                 'name': 'Surge Surfer',
                 'num': 207,
                 'onModifySpe': surgesurfer.onModifySpe,
                 'rating': 2,
                 'shortDesc': "If Electric Terrain is active, this Pokemon's "
                              'Speed is doubled.'},
 'swarm': {'desc': 'When this Pokemon has 1/3 or less of its maximum HP, '
                   'rounded down, its attacking stat is multiplied by 1.5 '
                   'while using a Bug-type attack.',
           'id': 'swarm',
           'name': 'Swarm',
           'num': 68,
           'onModifyAtk': swarm.onModifyAtk,
           'onModifyAtkPriority': 5,
           'onModifySpA': swarm.onModifySpA,
           'onModifySpAPriority': 5,
           'rating': 2,
           'shortDesc': "At 1/3 or less of its max HP, this Pokemon's "
                        'attacking stat is 1.5x with Bug attacks.'},
 'sweetveil': {'id': 'sweetveil',
               'name': 'Sweet Veil',
               'num': 175,
               'onAllySetStatus': sweetveil.onAllySetStatus,
               'onAllyTryAddVolatile': sweetveil.onAllyTryAddVolatile,
               'rating': 2,
               'shortDesc': 'This Pokemon and its allies cannot fall asleep.'},
 'swiftswim': {'id': 'swiftswim',
               'name': 'Swift Swim',
               'num': 33,
               'onModifySpe': swiftswim.onModifySpe,
               'rating': 3,
               'shortDesc': "If Rain Dance is active, this Pokemon's Speed is "
                            'doubled.'},
 'symbiosis': {'desc': 'If an ally uses its item, this Pokemon gives its item '
                       'to that ally immediately. Does not activate if the '
                       "ally's item was stolen or knocked off.",
               'id': 'symbiosis',
               'name': 'Symbiosis',
               'num': 180,
               'onAllyAfterUseItem': symbiosis.onAllyAfterUseItem,
               'rating': 0,
               'shortDesc': 'If an ally uses its item, this Pokemon gives its '
                            'item to that ally immediately.'},
 'synchronize': {'desc': 'If another Pokemon burns, paralyzes, poisons, or '
                         'badly poisons this Pokemon, that Pokemon receives '
                         'the same major status condition.',
                 'id': 'synchronize',
                 'name': 'Synchronize',
                 'num': 28,
                 'onAfterSetStatus': synchronize.onAfterSetStatus,
                 'rating': 2,
                 'shortDesc': 'If another Pokemon burns/poisons/paralyzes this '
                              'Pokemon, it also gets that status.'},
 'tangledfeet': {'id': 'tangledfeet',
                 'name': 'Tangled Feet',
                 'num': 77,
                 'onModifyAccuracy': tangledfeet.onModifyAccuracy,
                 'rating': 1,
                 'shortDesc': "This Pokemon's evasiveness is doubled as long "
                              'as it is confused.'},
 'tanglinghair': {'id': 'tanglinghair',
                  'name': 'Tangling Hair',
                  'num': 221,
                  'onAfterDamage': tanglinghair.onAfterDamage,
                  'rating': 2.5,
                  'shortDesc': 'Pokemon making contact with this Pokemon have '
                               'their Speed lowered by 1 stage.'},
 'technician': {'desc': "This Pokemon's moves of 60 power or less have their "
                        'power multiplied by 1.5. Does affect Struggle.',
                'id': 'technician',
                'name': 'Technician',
                'num': 101,
                'onBasePower': technician.onBasePower,
                'onBasePowerPriority': 8,
                'rating': 4,
                'shortDesc': "This Pokemon's moves of 60 power or less have "
                             '1.5x power. Includes Struggle.'},
 'telepathy': {'id': 'telepathy',
               'name': 'Telepathy',
               'num': 140,
               'onTryHit': telepathy.onTryHit,
               'rating': 0,
               'shortDesc': 'This Pokemon does not take damage from attacks '
                            'made by its allies.'},
 'teravolt': {'id': 'teravolt',
              'name': 'Teravolt',
              'num': 164,
              'onModifyMove': teravolt.onModifyMove,
              'onStart': teravolt.onStart,
              'rating': 3.5,
              'shortDesc': "This Pokemon's moves and their effects ignore the "
                           'Abilities of other Pokemon.'},
 'thickfat': {'desc': 'If a Pokemon uses a Fire- or Ice-type attack against '
                      "this Pokemon, that Pokemon's attacking stat is halved "
                      'when calculating the damage to this Pokemon.',
              'id': 'thickfat',
              'name': 'Thick Fat',
              'num': 47,
              'onModifyAtkPriority': 6,
              'onModifySpAPriority': 5,
              'onSourceModifyAtk': thickfat.onSourceModifyAtk,
              'onSourceModifySpA': thickfat.onSourceModifySpA,
              'rating': 3.5,
              'shortDesc': 'Fire/Ice-type moves against this Pokemon deal '
                           'damage with a halved attacking stat.'},
 'tintedlens': {'id': 'tintedlens',
                'name': 'Tinted Lens',
                'num': 110,
                'onModifyDamage': tintedlens.onModifyDamage,
                'rating': 3.5,
                'shortDesc': "This Pokemon's attacks that are not very "
                             'effective on a target deal double damage.'},
 'torrent': {'desc': 'When this Pokemon has 1/3 or less of its maximum HP, '
                     'rounded down, its attacking stat is multiplied by 1.5 '
                     'while using a Water-type attack.',
             'id': 'torrent',
             'name': 'Torrent',
             'num': 67,
             'onModifyAtk': torrent.onModifyAtk,
             'onModifyAtkPriority': 5,
             'onModifySpA': torrent.onModifySpA,
             'onModifySpAPriority': 5,
             'rating': 2,
             'shortDesc': "At 1/3 or less of its max HP, this Pokemon's "
                          'attacking stat is 1.5x with Water attacks.'},
 'toughclaws': {'id': 'toughclaws',
                'name': 'Tough Claws',
                'num': 181,
                'onBasePower': toughclaws.onBasePower,
                'onBasePowerPriority': 8,
                'rating': 3.5,
                'shortDesc': "This Pokemon's contact moves have their power "
                             'multiplied by 1.3.'},
 'toxicboost': {'desc': 'While this Pokemon is poisoned, the power of its '
                        'physical attacks is multiplied by 1.5.',
                'id': 'toxicboost',
                'name': 'Toxic Boost',
                'num': 137,
                'onBasePower': toxicboost.onBasePower,
                'onBasePowerPriority': 8,
                'rating': 3,
                'shortDesc': 'While this Pokemon is poisoned, its physical '
                             'attacks have 1.5x power.'},
 'trace': {'desc': 'On switch-in, or when this Pokemon acquires this ability, '
                   "this Pokemon copies a random adjacent opposing Pokemon's "
                   'Ability. However, if one or more adjacent Pokemon has the '
                   'Ability "No Ability", Trace won\'t copy anything even if '
                   'there is another valid Ability it could normally copy. '
                   'Otherwise, if there is no Ability that can be copied at '
                   'that time, this Ability will activate as soon as an '
                   'Ability can be copied. Abilities that cannot be copied are '
                   'the previously mentioned "No Ability", as well as '
                   'Comatose, Disguise, Flower Gift, Forecast, Illusion, '
                   'Imposter, Multitype, Schooling, Stance Change, Trace, and '
                   'Zen Mode.',
           'id': 'trace',
           'name': 'Trace',
           'num': 36,
           'onStart': trace.onStart,
           'onUpdate': trace.onUpdate,
           'rating': 3,
           'shortDesc': 'On switch-in, or when it can, this Pokemon copies a '
                        "random adjacent foe's Ability."},
 'triage': {'id': 'triage',
            'name': 'Triage',
            'num': 205,
            'onModifyPriority': triage.onModifyPriority,
            'rating': 3.5,
            'shortDesc': "This Pokemon's healing moves have their priority "
                         'increased by 3.'},
 'truant': {'effect': {},
            'id': 'truant',
            'name': 'Truant',
            'num': 54,
            'onBeforeMove': truant.onBeforeMove,
            'onBeforeMovePriority': 9,
            'onStart': truant.onStart,
            'rating': -2,
            'shortDesc': 'This Pokemon skips every other turn instead of using '
                         'a move.'},
 'turboblaze': {'id': 'turboblaze',
                'name': 'Turboblaze',
                'num': 163,
                'onModifyMove': turboblaze.onModifyMove,
                'onStart': turboblaze.onStart,
                'rating': 3.5,
                'shortDesc': "This Pokemon's moves and their effects ignore "
                             'the Abilities of other Pokemon.'},
 'unaware': {'desc': "This Pokemon ignores other Pokemon's Attack, Special "
                     'Attack, and accuracy stat stages when taking damage, and '
                     "ignores other Pokemon's Defense, Special Defense, and "
                     'evasiveness stat stages when dealing damage.',
             'id': 'unaware',
             'name': 'Unaware',
             'num': 109,
             'onAnyModifyBoost': unaware.onAnyModifyBoost,
             'rating': 3,
             'shortDesc': "This Pokemon ignores other Pokemon's stat stages "
                          'when taking or doing damage.'},
 'unburden': {'desc': 'If this Pokemon loses its held item for any reason, its '
                      'Speed is doubled. This boost is lost if it switches out '
                      'or gains a new item or Ability.',
              'effect': {'onModifySpe': unburden.onModifySpe},
              'id': 'unburden',
              'name': 'Unburden',
              'num': 84,
              'onAfterUseItem': unburden.onAfterUseItem,
              'onEnd': unburden.onEnd,
              'onTakeItem': unburden.onTakeItem,
              'rating': 3.5,
              'shortDesc': 'Speed is doubled on held item loss; boost is lost '
                           'if it switches, gets new item/Ability.'},
 'unnerve': {'id': 'unnerve',
             'name': 'Unnerve',
             'num': 127,
             'onFoeTryEatItem': False,
             'onPreStart': unnerve.onPreStart,
             'rating': 1.5,
             'shortDesc': 'While this Pokemon is active, it prevents opposing '
                          'Pokemon from using their Berries.'},
 'victorystar': {'id': 'victorystar',
                 'name': 'Victory Star',
                 'num': 162,
                 'onAllyModifyMove': victorystar.onAllyModifyMove,
                 'rating': 3,
                 'shortDesc': "This Pokemon and its allies' moves have their "
                              'accuracy multiplied by 1.1.'},
 'vitalspirit': {'id': 'vitalspirit',
                 'name': 'Vital Spirit',
                 'num': 72,
                 'onSetStatus': vitalspirit.onSetStatus,
                 'onUpdate': vitalspirit.onUpdate,
                 'rating': 2,
                 'shortDesc': 'This Pokemon cannot fall asleep. Gaining this '
                              'Ability while asleep cures it.'},
 'voltabsorb': {'desc': 'This Pokemon is immune to Electric-type moves and '
                        'restores 1/4 of its maximum HP, rounded down, when '
                        'hit by an Electric-type move.',
                'id': 'voltabsorb',
                'name': 'Volt Absorb',
                'num': 10,
                'onTryHit': voltabsorb.onTryHit,
                'rating': 3.5,
                'shortDesc': 'This Pokemon heals 1/4 of its max HP when hit by '
                             'Electric moves; Electric immunity.'},
 'waterabsorb': {'desc': 'This Pokemon is immune to Water-type moves and '
                         'restores 1/4 of its maximum HP, rounded down, when '
                         'hit by a Water-type move.',
                 'id': 'waterabsorb',
                 'name': 'Water Absorb',
                 'num': 11,
                 'onTryHit': waterabsorb.onTryHit,
                 'rating': 3.5,
                 'shortDesc': 'This Pokemon heals 1/4 of its max HP when hit '
                              'by Water moves; Water immunity.'},
 'waterbubble': {'desc': "This Pokemon's attacking stat is doubled while using "
                         'a Water-type attack. If a Pokemon uses a Fire-type '
                         "attack against this Pokemon, that Pokemon's "
                         'attacking stat is halved when calculating the damage '
                         'to this Pokemon. This Pokemon cannot be burned. '
                         'Gaining this Ability while burned cures it.',
                 'id': 'waterbubble',
                 'name': 'Water Bubble',
                 'num': 199,
                 'onModifyAtk': waterbubble.onModifyAtk,
                 'onModifyAtkPriority': 5,
                 'onModifySpA': waterbubble.onModifySpA,
                 'onModifySpAPriority': 5,
                 'onSetStatus': waterbubble.onSetStatus,
                 'onSourceModifyAtk': waterbubble.onSourceModifyAtk,
                 'onSourceModifySpA': waterbubble.onSourceModifySpA,
                 'onUpdate': waterbubble.onUpdate,
                 'rating': 4,
                 'shortDesc': "This Pokemon's Water power is 2x; it can't be "
                              'burned; Fire power against it is halved.'},
 'watercompaction': {'id': 'watercompaction',
                     'name': 'Water Compaction',
                     'num': 195,
                     'onAfterDamage': watercompaction.onAfterDamage,
                     'rating': 2,
                     'shortDesc': "This Pokemon's Defense is raised 2 stages "
                                  'after it is damaged by a Water-type move.'},
 'waterveil': {'id': 'waterveil',
               'name': 'Water Veil',
               'num': 41,
               'onSetStatus': waterveil.onSetStatus,
               'onUpdate': waterveil.onUpdate,
               'rating': 2,
               'shortDesc': 'This Pokemon cannot be burned. Gaining this '
                            'Ability while burned cures it.'},
 'weakarmor': {'desc': 'If a physical attack hits this Pokemon, its Defense is '
                       'lowered by 1 stage and its Speed is raised by 2 '
                       'stages.',
               'id': 'weakarmor',
               'name': 'Weak Armor',
               'num': 133,
               'onAfterDamage': weakarmor.onAfterDamage,
               'rating': 1,
               'shortDesc': 'If a physical attack hits this Pokemon, Defense '
                            'is lowered by 1, Speed is raised by 2.'},
 'whitesmoke': {'id': 'whitesmoke',
                'name': 'White Smoke',
                'num': 73,
                'onBoost': whitesmoke.onBoost,
                'rating': 2,
                'shortDesc': 'Prevents other Pokemon from lowering this '
                             "Pokemon's stat stages."},
 'wimpout': {'desc': 'When this Pokemon has more than 1/2 its maximum HP and '
                     'takes damage bringing it to 1/2 or less of its maximum '
                     'HP, it immediately switches out to a chosen ally. This '
                     'effect applies after all hits from a multi-hit move; '
                     'Sheer Force prevents it from activating if the move has '
                     'a secondary effect. This effect applies to both direct '
                     'and indirect damage, except Curse and Substitute on use, '
                     'Belly Drum, Pain Split, Struggle recoil, and confusion '
                     'damage.',
             'id': 'wimpout',
             'name': 'Wimp Out',
             'num': 193,
             'onAfterDamage': wimpout.onAfterDamage,
             'onAfterMoveSecondary': wimpout.onAfterMoveSecondary,
             'rating': 2,
             'shortDesc': 'This Pokemon switches out when it reaches 1/2 or '
                          'less of its maximum HP.'},
 'wonderguard': {'id': 'wonderguard',
                 'name': 'Wonder Guard',
                 'num': 25,
                 'onTryHit': wonderguard.onTryHit,
                 'rating': 5,
                 'shortDesc': 'This Pokemon can only be damaged by '
                              'supereffective moves and indirect damage.'},
 'wonderskin': {'desc': 'All non-damaging moves that check accuracy have their '
                        'accuracy changed to 50% when used on this Pokemon. '
                        'This change is done before any other accuracy '
                        'modifying effects.',
                'id': 'wonderskin',
                'name': 'Wonder Skin',
                'num': 147,
                'onModifyAccuracy': wonderskin.onModifyAccuracy,
                'onModifyAccuracyPriority': 10,
                'rating': 2,
                'shortDesc': 'Status moves with accuracy checks are 50% '
                             'accurate when used on this Pokemon.'},
 'zenmode': {'desc': 'If this Pokemon is a Darmanitan, it changes to Zen Mode '
                     'if it has 1/2 or less of its maximum HP at the end of a '
                     "turn. If Darmanitan's HP is above 1/2 of its maximum HP "
                     'at the end of a turn, it changes back to Standard Mode. '
                     'If Darmanitan loses this Ability while in Zen Mode it '
                     'reverts to Standard Mode immediately.',
             'effect': {'onEnd': zenmode.onEnd,
                        'onStart': zenmode.onStart},
             'id': 'zenmode',
             'name': 'Zen Mode',
             'num': 161,
             'onEnd': zenmode.onEnd,
             'onResidual': zenmode.onResidual,
             'onResidualOrder': 27,
             'rating': -1,
             'shortDesc': 'If Darmanitan, at end of turn changes Mode to '
                          'Standard if > 1/2 max HP, else Zen.'}}
