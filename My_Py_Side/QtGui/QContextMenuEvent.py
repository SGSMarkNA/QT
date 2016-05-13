from PySide import QtGui, QtCore

class QContextMenuEvent(QtGui.QContextMenuEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QContextMenuEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def globalPos(self):
		"""
		Returns the global position of the mouse pointer at the time of the event.
		"""
		res = super(QContextMenuEvent,self).globalPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def globalX(self):
		"""
		Returns the global x position of the mouse pointer at the time of the event.
		"""
		res = super(QContextMenuEvent,self).globalX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def globalY(self):
		"""
		Returns the global y position of the mouse pointer at the time of the event.
		"""
		res = super(QContextMenuEvent,self).globalY()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse pointer relative to the widget that received the event.
		"""
		res = super(QContextMenuEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def reason(self):
		"""
		Returns the reason for this context event.
		"""
		res = super(QContextMenuEvent,self).reason()
		isinstance(res,QtGui.QContextMenuEvent.Reason)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x position of the mouse pointer, relative to the widget that received the event.
		"""
		res = super(QContextMenuEvent,self).x()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y position of the mouse pointer, relative to the widget that received the event.
		"""
		res = super(QContextMenuEvent,self).y()
		isinstance(res,QtCore.int)
		return res
