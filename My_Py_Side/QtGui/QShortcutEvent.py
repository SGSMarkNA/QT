from PySide import QtGui, QtCore

class QShortcutEvent(QtGui.QShortcutEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QShortcutEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isAmbiguous(self):
		"""
		Returns true if the key sequence that triggered the event is ambiguous.
		"""
		res = super(QShortcutEvent,self).isAmbiguous()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		Returns the key sequence that triggered the event.
		"""
		res = super(QShortcutEvent,self).key()
		isinstance(res,QtGui.QKeySequence)
		return res
	#----------------------------------------------------------------------
	def shortcutId(self):
		"""
		Returns the ID of the PySide.QtGui.QShortcut object for which this event was generated.
		"""
		res = super(QShortcutEvent,self).shortcutId()
		isinstance(res,QtCore.int)
		return res
