from PySide import QtGui, QtCore

class QMoveEvent(QtGui.QMoveEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMoveEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def oldPos(self):
		"""
		Returns the old position of the widget.
		"""
		res = super(QMoveEvent,self).oldPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the new position of the widget
		This excludes the window frame for top level widgets.
		"""
		res = super(QMoveEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
