def onStart(**bvalues):
	"""function (target) {
				if (target.volatiles['smackdown'] || target.volatiles['ingrain']) return false;
				this.add('-start', target, 'Magnet Rise');
			}
	""" 
	pass

def onImmunity(**bvalues):
	"""function (type) {
				if (type === 'Ground') return false;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Magnet Rise');
			}
	""" 
	pass
