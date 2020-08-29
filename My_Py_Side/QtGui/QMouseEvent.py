from PySide import QtGui, QtCore

class QMouseEvent(QtGui.QMouseEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMouseEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def button(self):
		"""
		Returns the button that caused the event.
		Note that the returned value is always Qt.NoButton for mouse move events.
		"""
		res = super(QMouseEvent,self).button()
		isinstance(res,QtCore.Qt.MouseButton)
		return res
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns the button state when the event was generated
		The button state is a combination of Qt.LeftButton , Qt.RightButton , Qt.MidButton using the OR operator
		For mouse move events, this is all buttons that are pressed down
		For mouse press and double click events this includes the button that caused the event
		For mouse release events this excludes the button that caused the event.
		"""
		res = super(QMouseEvent,self).buttons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def globalPos(self):
		"""
		Returns the global position of the mouse cursor at the time of the event
		This is important on asynchronous window systems like X11
		Whenever you move your widgets around in response to mouse events, PySide.QtGui.QMouseEvent.globalPos() may differ a lot from the current pointer position QCursor.pos() , and from QWidget::mapToGlobal( PySide.QtGui.QMouseEvent.pos() ).
		"""
		res = super(QMouseEvent,self).globalPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def globalX(self):
		"""
		Returns the global x position of the mouse cursor at the time of the event.
		"""
		res = super(QMouseEvent,self).globalX()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def globalY(self):
		"""
		Returns the global y position of the mouse cursor at the time of the event.
		"""
		res = super(QMouseEvent,self).globalY()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hasExtendedInfo(self):
		"""

		"""
		res = super(QMouseEvent,self).hasExtendedInfo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse cursor, relative to the widget that received the event.
		If you move the widget as a result of the mouse event, use the global position returned by PySide.QtGui.QMouseEvent.globalPos() to avoid a shaking motion.
		"""
		res = super(QMouseEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def posF(self):
		"""
		Returns the position of the mouse cursor as a PySide.QtCore.QPointF , relative to the widget that received the event.
		If you move the widget as a result of the mouse event, use the global position returned by PySide.QtGui.QMouseEvent.globalPos() to avoid a shaking motion.
		"""
		res = super(QMouseEvent,self).posF()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x position of the mouse cursor, relative to the widget that received the event.
		"""
		res = super(QMouseEvent,self).x()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y position of the mouse cursor, relative to the widget that received the event.
		"""
		res = super(QMouseEvent,self).y()
		isinstance(res,int)
		return res
