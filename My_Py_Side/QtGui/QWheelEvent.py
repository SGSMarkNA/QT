from PySide import QtGui, QtCore

class QWheelEvent(QtGui.QWheelEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWheelEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns the mouse state when the event occurred.
		"""
		res = super(QWheelEvent,self).buttons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def delta(self):
		"""
		Returns the distance that the wheel is rotated, in eighths of a degree
		A positive value indicates that the wheel was rotated forwards away from the user; a negative value indicates that the wheel was rotated backwards toward the user.
		Most mouse types work in steps of 15 degrees, in which case the delta value is a multiple of 120; i.e., 120 units * 1/8 = 15 degrees.
		However, some mice have finer-resolution wheels and send delta values that are less than 120 units (less than 15 degrees)
		To support this possibility, you can either cumulatively add the delta values from events until the value of 120 is reached, then scroll the widget, or you can partially scroll the widget in response to each wheel event.
		Example:
		"""
		res = super(QWheelEvent,self).delta()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def globalPos(self):
		"""
		Returns the global position of the mouse pointer at the time of the event
		This is important on asynchronous window systems such as X11; whenever you move your widgets around in response to mouse events, PySide.QtGui.QWheelEvent.globalPos() can differ a lot from the current cursor position returned by QCursor.pos() .
		"""
		res = super(QWheelEvent,self).globalPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def globalX(self):
		"""
		Returns the global x position of the mouse cursor at the time of the event.
		"""
		res = super(QWheelEvent,self).globalX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def globalY(self):
		"""
		Returns the global y position of the mouse cursor at the time of the event.
		"""
		res = super(QWheelEvent,self).globalY()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the wheels orientation.
		"""
		res = super(QWheelEvent,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse cursor relative to the widget that received the event.
		If you move your widgets around in response to mouse events, use PySide.QtGui.QWheelEvent.globalPos() instead of this function.
		"""
		res = super(QWheelEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x position of the mouse cursor, relative to the widget that received the event.
		"""
		res = super(QWheelEvent,self).x()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y position of the mouse cursor, relative to the widget that received the event.
		"""
		res = super(QWheelEvent,self).y()
		isinstance(res,QtCore.int)
		return res
