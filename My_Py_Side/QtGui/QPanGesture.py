from PySide import QtGui, QtCore

class QPanGesture(QtGui.QPanGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPanGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceleration(self):
		"""
		This property holds the acceleration in the motion of the touch point for this gesture.
		"""
		res = super(QPanGesture,self).acceleration()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def delta(self):
		"""
		This property holds the offset from the previous input position to the current input.
		This is essentially the same as the difference between PySide.QtGui.QPanGesture.offset() and PySide.QtGui.QPanGesture.lastOffset() .
		"""
		res = super(QPanGesture,self).delta()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastOffset(self):
		"""
		This property holds the last offset recorded for this gesture.
		The last offset contains the change in position of the users input as reported in the PySide.QtGui.QPanGesture.offset() property when a previous gesture event was delivered for this gesture.
		If no previous event was delivered with information about this gesture (i.e., this gesture object contains information about the first movement in the gesture) then this property contains a zero size.
		"""
		res = super(QPanGesture,self).lastOffset()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def offset(self):
		"""
		This property holds the total offset from the first input position to the current input position.
		The offset measures the total change in position of the users input covered by the gesture on the input device.
		"""
		res = super(QPanGesture,self).offset()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setAcceleration(self,value):
		"""
		setAcceleration(value)
			value=QtCore.qreal

		This property holds the acceleration in the motion of the touch point for this gesture.
		"""
		res = super(QPanGesture,self).setAcceleration(value)
		return res
	#----------------------------------------------------------------------
	def setLastOffset(self,value):
		"""
		setLastOffset(value)
			value=QtCore.QPointF

		This property holds the last offset recorded for this gesture.
		The last offset contains the change in position of the users input as reported in the PySide.QtGui.QPanGesture.offset() property when a previous gesture event was delivered for this gesture.
		If no previous event was delivered with information about this gesture (i.e., this gesture object contains information about the first movement in the gesture) then this property contains a zero size.
		"""
		res = super(QPanGesture,self).setLastOffset(value)
		return res
	#----------------------------------------------------------------------
	def setOffset(self,value):
		"""
		setOffset(value)
			value=QtCore.QPointF

		This property holds the total offset from the first input position to the current input position.
		The offset measures the total change in position of the users input covered by the gesture on the input device.
		"""
		res = super(QPanGesture,self).setOffset(value)
		return res
