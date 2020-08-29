from PySide import QtGui, QtCore

class QKeyEventTransition(QtGui.QKeyEventTransition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QKeyEventTransition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def key(self):
		"""
		This property holds the key that this key event transition is associated with.
		"""
		res = super(QKeyEventTransition,self).key()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def modifierMask(self):
		"""
		This property holds the keyboard modifier mask that this key event transition checks for.
		"""
		res = super(QKeyEventTransition,self).modifierMask()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def setKey(self,key):
		"""
		setKey(key)
			key=QtCore.int

		This property holds the key that this key event transition is associated with.
		"""
		res = super(QKeyEventTransition,self).setKey(key)
		return res
	#----------------------------------------------------------------------
	def setModifierMask(self,modifiers):
		"""
		setModifierMask(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers

		This property holds the keyboard modifier mask that this key event transition checks for.
		"""
		res = super(QKeyEventTransition,self).setModifierMask(modifiers)
		return res
