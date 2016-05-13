from PySide import QtGui, QtCore

class QSwipeGesture(QtGui.QSwipeGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSwipeGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def horizontalDirection(self):
		"""
		This property holds the horizontal direction of the gesture.
		If the gesture has a horizontal component, the horizontal direction is either Left or Right; otherwise, it is NoDirection .
		"""
		res = super(QSwipeGesture,self).horizontalDirection()
		isinstance(res,QtGui.QSwipeGesture.SwipeDirection)
		return res
	#----------------------------------------------------------------------
	def swipeAngle(self):
		"""
		This property holds the angle of the motion associated with the gesture.
		If the gesture has either a horizontal or vertical component, the swipe angle describes the angle between the direction of motion and the x-axis as defined using the standard widget coordinate system .
		"""
		res = super(QSwipeGesture,self).swipeAngle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def verticalDirection(self):
		"""
		This property holds the vertical direction of the gesture.
		If the gesture has a vertical component, the vertical direction is either Up or Down; otherwise, it is NoDirection .
		"""
		res = super(QSwipeGesture,self).verticalDirection()
		isinstance(res,QtGui.QSwipeGesture.SwipeDirection)
		return res
	#----------------------------------------------------------------------
	def setSwipeAngle(self,value):
		"""
		setSwipeAngle(value)
			value=QtCore.qreal

		This property holds the angle of the motion associated with the gesture.
		If the gesture has either a horizontal or vertical component, the swipe angle describes the angle between the direction of motion and the x-axis as defined using the standard widget coordinate system .
		"""
		res = super(QSwipeGesture,self).setSwipeAngle(value)
		return res
