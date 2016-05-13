from PySide import QtGui, QtCore

class QActionEvent(QtGui.QActionEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QActionEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def action(self):
		"""
		Returns the action that is changed, added, or removed.
		"""
		res = super(QActionEvent,self).action()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def before(self):
		"""
		If PySide.QtCore.QEvent.type() is ActionAdded , returns the action that should appear before PySide.QtGui.QActionEvent.action()
		If this function returns 0, the action should be appended to already existing actions on the same widget.
		"""
		res = super(QActionEvent,self).before()
		isinstance(res,QtGui.QAction)
		return res
