from PySide import QtGui, QtCore

class QHelpEvent(QtGui.QHelpEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHelpEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def globalPos(self):
		"""
		Returns the mouse cursor position when the event was generated in global coordinates.
		"""
		res = super(QHelpEvent,self).globalPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def globalX(self):
		"""
		Same as PySide.QtGui.QHelpEvent.globalPos()
		PySide.QtGui.QHelpEvent.x() .
		"""
		res = super(QHelpEvent,self).globalX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def globalY(self):
		"""
		Same as PySide.QtGui.QHelpEvent.globalPos()
		PySide.QtGui.QHelpEvent.y() .
		"""
		res = super(QHelpEvent,self).globalY()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the mouse cursor position when the event was generated, relative to the widget to which the event is dispatched.
		"""
		res = super(QHelpEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Same as PySide.QtGui.QHelpEvent.pos()
		PySide.QtGui.QHelpEvent.x() .
		"""
		res = super(QHelpEvent,self).x()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Same as PySide.QtGui.QHelpEvent.pos()
		PySide.QtGui.QHelpEvent.y() .
		"""
		res = super(QHelpEvent,self).y()
		isinstance(res,QtCore.int)
		return res
