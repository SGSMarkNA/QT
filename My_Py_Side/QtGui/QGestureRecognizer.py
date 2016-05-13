from PySide import QtGui, QtCore

class QGestureRecognizer(QtGui.QGestureRecognizer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGestureRecognizer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def create(self,target):
		"""
		create(target)
			target=QtCore.QObject

		This function is called by Qt to create a new PySide.QtGui.QGesture object for the given target ( PySide.QtGui.QWidget or PySide.QtGui.QGraphicsObject ).
		Reimplement this function to create a custom PySide.QtGui.QGesture -derived gesture object if necessary.
		The application takes ownership of the created gesture object.
		"""
		res = super(QGestureRecognizer,self).create(target)
		isinstance(res,QtGui.QGesture)
		return res
	#----------------------------------------------------------------------
	def recognize(self,state,watched,event):
		"""
		recognize(state,watched,event)
			state=QtGui.QGesture
			watched=QtCore.QObject
			event=QtCore.QEvent

		Handles the given event for the watched object, updating the state of the gesture object as required, and returns a suitable result for the current recognition step.
		This function is called by the framework to allow the recognizer to filter input events dispatched to PySide.QtGui.QWidget or PySide.QtGui.QGraphicsObject instances that it is monitoring.
		The result reflects how much of the gesture has been recognized
		The state of the gesture object is set depending on the result.
		"""
		res = super(QGestureRecognizer,self).recognize(state,watched,event)
		isinstance(res,QtGui.QGestureRecognizer.Result)
		return res
	#----------------------------------------------------------------------
	def reset(self,state):
		"""
		reset(state)
			state=QtGui.QGesture

		This function is called by the framework to reset a given gesture .
		Reimplement this function to implement additional requirements for custom PySide.QtGui.QGesture objects
		This may be necessary if you implement a custom PySide.QtGui.QGesture whose properties need special handling when the gesture is reset.
		"""
		res = super(QGestureRecognizer,self).reset(state)
		return res
