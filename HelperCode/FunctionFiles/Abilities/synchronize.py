def onAfterSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			if (!source || source === target)
				return;
			if (effect && effect.id === 'toxicspikes')
				return;
			if (status.id === 'slp' || status.id === 'frz')
				return;
			this.add('-activate', target, 'ability: Synchronize');
			// Hack to make status-prevention abilities think Synchronize is a status move
			// and show messages when activating against it.
			source.trySetStatus(status, target, { status: status.id, id: 'synchronize' });
		}
	""" 
	pass