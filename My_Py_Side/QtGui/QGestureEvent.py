from PySide import QtGui, QtCore

class QGestureEvent(QtGui.QGestureEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGestureEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeGestures(self):
		"""
		Returns a list of active (not canceled) gestures.
		"""
		res = super(QGestureEvent,self).activeGestures()
		return res
	#----------------------------------------------------------------------
	def canceledGestures(self):
		"""
		Returns a list of canceled gestures.
		"""
		res = super(QGestureEvent,self).canceledGestures()
		return res
	#----------------------------------------------------------------------
	def gestures(self):
		"""
		Returns all gestures that are delivered in the event.
		"""
		res = super(QGestureEvent,self).gestures()
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the widget on which the event occurred.
		"""
		res = super(QGestureEvent,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def accept(self,*args,**kwargs):
		"""
		accept(arg__1)
			arg__1=QtGui.QGesture

		accept(arg__1)
			arg__1=QtCore.Qt.GestureType

		Sets the accept flag of the given gesture object, the equivalent of calling setAccepted(gesture, true) .
		Setting the accept flag indicates that the event receiver wants the gesture
		Unwanted gestures may be propagated to the parent widget.
		"""
		res = super(QGestureEvent,self).accept(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def gesture(self,type):
		"""
		gesture(type)
			type=QtCore.Qt.GestureType


		"""
		res = super(QGestureEvent,self).gesture(type)
		isinstance(res,QtGui.QGesture)
		return res
	#----------------------------------------------------------------------
	def ignore(self,*args,**kwargs):
		"""
		ignore(arg__1)
			arg__1=QtCore.Qt.GestureType

		ignore(arg__1)
			arg__1=QtGui.QGesture


		"""
		res = super(QGestureEvent,self).ignore(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def isAccepted(self,*args,**kwargs):
		"""
		isAccepted(arg__1)
			arg__1=QtCore.Qt.GestureType

		isAccepted(arg__1)
			arg__1=QtGui.QGesture


		"""
		res = super(QGestureEvent,self).isAccepted(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def mapToGraphicsScene(self,gesturePoint):
		"""
		mapToGraphicsScene(gesturePoint)
			gesturePoint=QtCore.QPointF

		Returns the scene-local coordinates if the gesturePoint is inside a graphics view.
		This functional might be useful when the gesture event is delivered to a PySide.QtGui.QGraphicsObject to translate a point in screen coordinates to scene-local coordinates.
		"""
		res = super(QGestureEvent,self).mapToGraphicsScene(gesturePoint)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setAccepted(self,*args,**kwargs):
		"""
		setAccepted(arg__1,arg__2)
			arg__1=QtCore.Qt.GestureType
			arg__2=QtCore.bool

		setAccepted(arg__1,arg__2)
			arg__1=QtGui.QGesture
			arg__2=QtCore.bool


		"""
		res = super(QGestureEvent,self).setAccepted(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Sets the widget for this event to the widget specified.
		"""
		res = super(QGestureEvent,self).setWidget(widget)
		return res
