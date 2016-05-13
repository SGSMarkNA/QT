from PySide import QtGui, QtCore

class QInputEvent(QtGui.QInputEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QInputEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifier flags that existed immediately before the event occurred.
		"""
		res = super(QInputEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,amodifiers):
		"""
		setModifiers(amodifiers)
			amodifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QInputEvent,self).setModifiers(amodifiers)
		return res
