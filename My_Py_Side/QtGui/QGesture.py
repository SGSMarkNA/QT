from PySide import QtGui, QtCore

class QGesture(QtGui.QGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def gestureCancelPolicy(self):
		"""
		This property holds the policy for deciding what happens on accepting a gesture.
		On accepting one gesture Qt can automatically cancel other gestures that belong to other targets
		The policy is normally set to not cancel any other gestures and can be set to cancel all active gestures in the context
		For example for all child widgets.
		"""
		res = super(QGesture,self).gestureCancelPolicy()
		isinstance(res,QtGui.QGesture.GestureCancelPolicy)
		return res
	#----------------------------------------------------------------------
	def gestureType(self):
		"""
		This property holds the type of the gesture.
		"""
		res = super(QGesture,self).gestureType()
		isinstance(res,QtCore.Qt.GestureType)
		return res
	#----------------------------------------------------------------------
	def hasHotSpot(self):
		"""
		This property holds whether the gesture has a hot-spot.
		"""
		res = super(QGesture,self).hasHotSpot()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hotSpot(self):
		"""
		This property holds The point that is used to find the receiver for the gesture event..
		The hot-spot is a point in the global coordinate system, use QWidget.mapFromGlobal() or QGestureEvent.mapToGraphicsScene() to get a local hot-spot.
		The hot-spot should be set by the gesture recognizer to allow gesture event delivery to a PySide.QtGui.QGraphicsObject .
		"""
		res = super(QGesture,self).hotSpot()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		This property holds the current state of the gesture.
		"""
		res = super(QGesture,self).state()
		isinstance(res,QtCore.Qt.GestureState)
		return res
	#----------------------------------------------------------------------
	def unsetHotSpot(self):
		"""
		This property holds The point that is used to find the receiver for the gesture event..
		The hot-spot is a point in the global coordinate system, use QWidget.mapFromGlobal() or QGestureEvent.mapToGraphicsScene() to get a local hot-spot.
		The hot-spot should be set by the gesture recognizer to allow gesture event delivery to a PySide.QtGui.QGraphicsObject .
		"""
		res = super(QGesture,self).unsetHotSpot()
		return res
	#----------------------------------------------------------------------
	def setGestureCancelPolicy(self,policy):
		"""
		setGestureCancelPolicy(policy)
			policy=QtGui.QGesture.GestureCancelPolicy

		This property holds the policy for deciding what happens on accepting a gesture.
		On accepting one gesture Qt can automatically cancel other gestures that belong to other targets
		The policy is normally set to not cancel any other gestures and can be set to cancel all active gestures in the context
		For example for all child widgets.
		"""
		res = super(QGesture,self).setGestureCancelPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setHotSpot(self,value):
		"""
		setHotSpot(value)
			value=QtCore.QPointF

		This property holds The point that is used to find the receiver for the gesture event..
		The hot-spot is a point in the global coordinate system, use QWidget.mapFromGlobal() or QGestureEvent.mapToGraphicsScene() to get a local hot-spot.
		The hot-spot should be set by the gesture recognizer to allow gesture event delivery to a PySide.QtGui.QGraphicsObject .
		"""
		res = super(QGesture,self).setHotSpot(value)
		return res
