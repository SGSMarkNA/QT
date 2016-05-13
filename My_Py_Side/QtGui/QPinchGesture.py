from PySide import QtGui, QtCore

class QPinchGesture(QtGui.QPinchGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPinchGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def centerPoint(self):
		"""
		This property holds the current center point.
		The center point is the midpoint between the two input points in the gesture.
		"""
		res = super(QPinchGesture,self).centerPoint()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def changeFlags(self):
		"""

		"""
		res = super(QPinchGesture,self).changeFlags()
		isinstance(res,QtGui.QPinchGesture.ChangeFlags)
		return res
	#----------------------------------------------------------------------
	def lastCenterPoint(self):
		"""
		This property holds the last position of the center point recorded for this gesture.
		"""
		res = super(QPinchGesture,self).lastCenterPoint()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastRotationAngle(self):
		"""
		This property holds the last reported angle covered by the gesture motion.
		The last rotation angle is the angle as reported in the PySide.QtGui.QPinchGesture.rotationAngle() property when a previous gesture event was delivered for this gesture.
		"""
		res = super(QPinchGesture,self).lastRotationAngle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lastScaleFactor(self):
		"""
		This property holds the last scale factor recorded for this gesture.
		The last scale factor contains the scale factor reported in the PySide.QtGui.QPinchGesture.scaleFactor() property when a previous gesture event included information about this gesture.
		If no previous event was delivered with information about this gesture (i.e., this gesture object contains information about the first movement in the gesture) then this property contains zero.
		"""
		res = super(QPinchGesture,self).lastScaleFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rotationAngle(self):
		"""
		This property holds the angle covered by the gesture motion.
		"""
		res = super(QPinchGesture,self).rotationAngle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def scaleFactor(self):
		"""
		This property holds the current scale factor.
		The scale factor measures the scale factor associated with the distance between two of the users inputs on a touch device.
		"""
		res = super(QPinchGesture,self).scaleFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def startCenterPoint(self):
		"""
		This property holds the starting position of the center point.
		"""
		res = super(QPinchGesture,self).startCenterPoint()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def totalChangeFlags(self):
		"""

		"""
		res = super(QPinchGesture,self).totalChangeFlags()
		isinstance(res,QtGui.QPinchGesture.ChangeFlags)
		return res
	#----------------------------------------------------------------------
	def totalRotationAngle(self):
		"""
		This property holds the total angle covered by the gesture.
		This total angle measures the complete angle covered by the gesture
		Usually, this is equal to the value held by the PySide.QtGui.QPinchGesture.rotationAngle() property, except in the case where the user performs multiple rotations by removing and repositioning one of the touch points, as described above
		In this case, the total angle will be the sum of the rotation angles for the multiple stages of the gesture.
		"""
		res = super(QPinchGesture,self).totalRotationAngle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def totalScaleFactor(self):
		"""
		This property holds the total scale factor.
		The total scale factor measures the total change in scale factor from the original value to the current scale factor.
		"""
		res = super(QPinchGesture,self).totalScaleFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setCenterPoint(self,value):
		"""
		setCenterPoint(value)
			value=QtCore.QPointF

		This property holds the current center point.
		The center point is the midpoint between the two input points in the gesture.
		"""
		res = super(QPinchGesture,self).setCenterPoint(value)
		return res
	#----------------------------------------------------------------------
	def setChangeFlags(self,value):
		"""
		setChangeFlags(value)
			value=QtGui.QPinchGesture.ChangeFlags


		"""
		res = super(QPinchGesture,self).setChangeFlags(value)
		return res
	#----------------------------------------------------------------------
	def setLastCenterPoint(self,value):
		"""
		setLastCenterPoint(value)
			value=QtCore.QPointF

		This property holds the last position of the center point recorded for this gesture.
		"""
		res = super(QPinchGesture,self).setLastCenterPoint(value)
		return res
	#----------------------------------------------------------------------
	def setLastRotationAngle(self,value):
		"""
		setLastRotationAngle(value)
			value=QtCore.qreal

		This property holds the last reported angle covered by the gesture motion.
		The last rotation angle is the angle as reported in the PySide.QtGui.QPinchGesture.rotationAngle() property when a previous gesture event was delivered for this gesture.
		"""
		res = super(QPinchGesture,self).setLastRotationAngle(value)
		return res
	#----------------------------------------------------------------------
	def setLastScaleFactor(self,value):
		"""
		setLastScaleFactor(value)
			value=QtCore.qreal

		This property holds the last scale factor recorded for this gesture.
		The last scale factor contains the scale factor reported in the PySide.QtGui.QPinchGesture.scaleFactor() property when a previous gesture event included information about this gesture.
		If no previous event was delivered with information about this gesture (i.e., this gesture object contains information about the first movement in the gesture) then this property contains zero.
		"""
		res = super(QPinchGesture,self).setLastScaleFactor(value)
		return res
	#----------------------------------------------------------------------
	def setRotationAngle(self,value):
		"""
		setRotationAngle(value)
			value=QtCore.qreal

		This property holds the angle covered by the gesture motion.
		"""
		res = super(QPinchGesture,self).setRotationAngle(value)
		return res
	#----------------------------------------------------------------------
	def setScaleFactor(self,value):
		"""
		setScaleFactor(value)
			value=QtCore.qreal

		This property holds the current scale factor.
		The scale factor measures the scale factor associated with the distance between two of the users inputs on a touch device.
		"""
		res = super(QPinchGesture,self).setScaleFactor(value)
		return res
	#----------------------------------------------------------------------
	def setStartCenterPoint(self,value):
		"""
		setStartCenterPoint(value)
			value=QtCore.QPointF

		This property holds the starting position of the center point.
		"""
		res = super(QPinchGesture,self).setStartCenterPoint(value)
		return res
	#----------------------------------------------------------------------
	def setTotalChangeFlags(self,value):
		"""
		setTotalChangeFlags(value)
			value=QtGui.QPinchGesture.ChangeFlags


		"""
		res = super(QPinchGesture,self).setTotalChangeFlags(value)
		return res
	#----------------------------------------------------------------------
	def setTotalRotationAngle(self,value):
		"""
		setTotalRotationAngle(value)
			value=QtCore.qreal

		This property holds the total angle covered by the gesture.
		This total angle measures the complete angle covered by the gesture
		Usually, this is equal to the value held by the PySide.QtGui.QPinchGesture.rotationAngle() property, except in the case where the user performs multiple rotations by removing and repositioning one of the touch points, as described above
		In this case, the total angle will be the sum of the rotation angles for the multiple stages of the gesture.
		"""
		res = super(QPinchGesture,self).setTotalRotationAngle(value)
		return res
	#----------------------------------------------------------------------
	def setTotalScaleFactor(self,value):
		"""
		setTotalScaleFactor(value)
			value=QtCore.qreal

		This property holds the total scale factor.
		The total scale factor measures the total change in scale factor from the original value to the current scale factor.
		"""
		res = super(QPinchGesture,self).setTotalScaleFactor(value)
		return res
