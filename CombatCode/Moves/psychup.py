def onHit(**bvalues):
	"""function (target, source) {
			var i;
			for (i in target.boosts) {
				source.boosts[i] = target.boosts[i];
			}
			var volatilesToCopy = ['focusenergy', 'gmaxchistrike', 'laserfocus'];
			for (var _i = 0, volatilesToCopy_1 = volatilesToCopy; _i < volatilesToCopy_1.length; _i++) {
				var volatile = volatilesToCopy_1[_i];
				if (target.volatiles[volatile]) {
					source.addVolatile(volatile);
					if (volatile === 'gmaxchistrike')
						source.volatiles[volatile].layers = target.volatiles[volatile].layers;
				}
				else {
					source.removeVolatile(volatile);
				}
			}
			this.add('-copyboost', source, target, '[from] move: Psych Up');
		}
	""" 
	pass
