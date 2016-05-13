from PySide import QtGui, QtCore

class QTabletEvent(QtGui.QTabletEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTabletEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the type of device that generated the event.
		"""
		res = super(QTabletEvent,self).device()
		isinstance(res,QtGui.QTabletEvent.TabletDevice)
		return res
	#----------------------------------------------------------------------
	def globalPos(self):
		"""
		Returns the global position of the device at the time of the event
		This is important on asynchronous windows systems like X11; whenever you move your widgets around in response to mouse events, PySide.QtGui.QTabletEvent.globalPos() can differ significantly from the current position QCursor.pos() .
		"""
		res = super(QTabletEvent,self).globalPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def globalX(self):
		"""
		Returns the global x position of the mouse pointer at the time of the event.
		"""
		res = super(QTabletEvent,self).globalX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def globalY(self):
		"""
		Returns the global y position of the tablet device at the time of the event.
		"""
		res = super(QTabletEvent,self).globalY()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def hiResGlobalPos(self):
		"""
		The high precision coordinates delivered from the tablet expressed
		Sub pixeling information is in the fractional part of the PySide.QtCore.QPointF .
		"""
		res = super(QTabletEvent,self).hiResGlobalPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def hiResGlobalX(self):
		"""
		The high precision x position of the tablet device.
		"""
		res = super(QTabletEvent,self).hiResGlobalX()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hiResGlobalY(self):
		"""
		The high precision y position of the tablet device.
		"""
		res = super(QTabletEvent,self).hiResGlobalY()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def pointerType(self):
		"""
		Returns the type of point that generated the event.
		"""
		res = super(QTabletEvent,self).pointerType()
		isinstance(res,QtGui.QTabletEvent.PointerType)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the device, relative to the widget that received the event.
		If you move widgets around in response to mouse events, use PySide.QtGui.QTabletEvent.globalPos() instead of this function.
		"""
		res = super(QTabletEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def pressure(self):
		"""
		Returns the pressure for the device
		0.0 indicates that the stylus is not on the tablet, 1.0 indicates the maximum amount of pressure for the stylus.
		"""
		res = super(QTabletEvent,self).pressure()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rotation(self):
		"""
		Returns the rotation of the current device in degress
		This is usually given by a 4D Mouse
		If the device doesnt support rotation this value is always 0.0.
		"""
		res = super(QTabletEvent,self).rotation()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def tangentialPressure(self):
		"""
		Returns the tangential pressure for the device
		This is typically given by a finger wheel on an airbrush tool
		The range is from -1.0 to 1.0
		0.0 indicates a neutral position
		Current airbrushes can only move in the positive direction from the neutrual position
		If the device does not support tangential pressure, this value is always 0.0.
		"""
		res = super(QTabletEvent,self).tangentialPressure()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def uniqueId(self):
		"""
		Returns a unique ID for the current device, making it possible to differentiate between multiple devices being used at the same time on the tablet.
		Support of this feature is dependent on the tablet.
		Values for the same device may vary from OS to OS.
		Later versions of the Wacom driver for Linux will now report the ID information
		If you have a tablet that supports unique ID and are not getting the information on Linux, consider upgrading your driver.
		As of Qt 4.2, the unique ID is the same regardless of the orientation of the pen
		Earlier versions would report a different value when using the eraser-end versus the pen-end of the stylus on some OSs.
		"""
		res = super(QTabletEvent,self).uniqueId()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x position of the device, relative to the widget that received the event.
		"""
		res = super(QTabletEvent,self).x()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def xTilt(self):
		"""
		Returns the angle between the device (a pen, for example) and the perpendicular in the direction of the x axis
		Positive values are towards the tablets physical right
		The angle is in the range -60 to +60 degrees.
		"""
		res = super(QTabletEvent,self).xTilt()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y position of the device, relative to the widget that received the event.
		"""
		res = super(QTabletEvent,self).y()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def yTilt(self):
		"""
		Returns the angle between the device (a pen, for example) and the perpendicular in the direction of the y axis
		Positive values are towards the bottom of the tablet
		The angle is within the range -60 to +60 degrees.
		"""
		res = super(QTabletEvent,self).yTilt()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def z(self):
		"""
		Returns the z position of the device
		Typically this is represented by a wheel on a 4D Mouse
		If the device does not support a Z-axis, this value is always zero
		This is not the same as pressure.
		"""
		res = super(QTabletEvent,self).z()
		isinstance(res,QtCore.int)
		return res
