from PySide import QtGui, QtCore

class QWindowStateChangeEvent(QtGui.QWindowStateChangeEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWindowStateChangeEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isOverride(self):
		"""

		"""
		res = super(QWindowStateChangeEvent,self).isOverride()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def oldState(self):
		"""
		Returns the state of the window before the change.
		"""
		res = super(QWindowStateChangeEvent,self).oldState()
		isinstance(res,QtCore.Qt.WindowStates)
		return res
