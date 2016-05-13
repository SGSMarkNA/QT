from PySide import QtGui, QtCore

class QHoverEvent(QtGui.QHoverEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHoverEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def oldPos(self):
		"""
		Returns the previous position of the mouse cursor, relative to the widget that received the event
		If there is no previous position, PySide.QtGui.QHoverEvent.oldPos() will return the same position as PySide.QtGui.QHoverEvent.pos() .
		On QEvent.HoverEnter events, this position will always be PySide.QtCore.QPoint (-1, -1).
		"""
		res = super(QHoverEvent,self).oldPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse cursor, relative to the widget that received the event.
		On QEvent.HoverLeave events, this position will always be PySide.QtCore.QPoint (-1, -1).
		"""
		res = super(QHoverEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
