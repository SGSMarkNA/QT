from PySide import QtGui, QtCore

class QTouchEvent(QtGui.QTouchEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTouchEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def id(self):
		"""
		Returns the id number of this touch point.
		Id numbers are globally sequential, starting at zero, meaning the first touch point in the application has id 0, the second has id 1, and so on.
		"""
		res = super(QTouchEvent,self).id()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isPrimary(self):
		"""
		Returns true if this touch point is the primary touch point
		The primary touch point is the point for which the windowing system generates mouse events.
		"""
		res = super(QTouchEvent,self).isPrimary()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastNormalizedPos(self):
		"""
		Returns the normalized position of this touch point from the previous touch event.
		The coordinates are normalized to the size of the touch device, i.e
		(0,0) is the top-left corner and (1,1) is the bottom-right corner.
		"""
		res = super(QTouchEvent,self).lastNormalizedPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastPos(self):
		"""
		Returns the position of this touch point from the previous touch event, relative to the widget or PySide.QtGui.QGraphicsItem that received the event.
		"""
		res = super(QTouchEvent,self).lastPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScenePos(self):
		"""
		Returns the scene position of this touch point from the previous touch event.
		The scene position is the position in PySide.QtGui.QGraphicsScene coordinates if the PySide.QtGui.QTouchEvent is handled by a QGraphicsItem::touchEvent() reimplementation, and identical to the screen position for widgets.
		"""
		res = super(QTouchEvent,self).lastScenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScreenPos(self):
		"""
		Returns the screen position of this touch point from the previous touch event.
		"""
		res = super(QTouchEvent,self).lastScreenPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def normalizedPos(self):
		"""
		Returns the normalized position of this touch point.
		The coordinates are normalized to the size of the touch device, i.e
		(0,0) is the top-left corner and (1,1) is the bottom-right corner.
		"""
		res = super(QTouchEvent,self).normalizedPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of this touch point, relative to the widget or PySide.QtGui.QGraphicsItem that received the event.
		"""
		res = super(QTouchEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def pressure(self):
		"""
		Returns the pressure of this touch point
		The return value is in the range 0.0 to 1.0.
		"""
		res = super(QTouchEvent,self).pressure()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the rect for this touch point, relative to the widget or PySide.QtGui.QGraphicsItem that received the event
		The rect is centered around the point returned by PySide.QtGui.QTouchEvent::TouchPoint.pos() .
		"""
		res = super(QTouchEvent,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the scene position of this touch point.
		The scene position is the position in PySide.QtGui.QGraphicsScene coordinates if the PySide.QtGui.QTouchEvent is handled by a QGraphicsItem::touchEvent() reimplementation, and identical to the screen position for widgets.
		"""
		res = super(QTouchEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def sceneRect(self):
		"""
		Returns the rect for this touch point in scene coordinates.
		"""
		res = super(QTouchEvent,self).sceneRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the screen position of this touch point.
		"""
		res = super(QTouchEvent,self).screenPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenRect(self):
		"""
		Returns the rect for this touch point in screen coordinates.
		"""
		res = super(QTouchEvent,self).screenRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def startNormalizedPos(self):
		"""
		Returns the normalized starting position of this touch point.
		The coordinates are normalized to the size of the touch device, i.e
		(0,0) is the top-left corner and (1,1) is the bottom-right corner.
		"""
		res = super(QTouchEvent,self).startNormalizedPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def startPos(self):
		"""
		Returns the starting position of this touch point, relative to the widget or PySide.QtGui.QGraphicsItem that received the event.
		"""
		res = super(QTouchEvent,self).startPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def startScenePos(self):
		"""
		Returns the starting scene position of this touch point.
		The scene position is the position in PySide.QtGui.QGraphicsScene coordinates if the PySide.QtGui.QTouchEvent is handled by a QGraphicsItem::touchEvent() reimplementation, and identical to the screen position for widgets.
		"""
		res = super(QTouchEvent,self).startScenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def startScreenPos(self):
		"""
		Returns the starting screen position of this touch point.
		"""
		res = super(QTouchEvent,self).startScreenPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of this touch point.
		"""
		res = super(QTouchEvent,self).state()
		isinstance(res,QtCore.Qt.TouchPointState)
		return res
	#----------------------------------------------------------------------
	def setId(self,id):
		"""
		setId(id)
			id=QtCore.int


		"""
		res = super(QTouchEvent,self).setId(id)
		return res
	#----------------------------------------------------------------------
	def setLastNormalizedPos(self,lastNormalizedPos):
		"""
		setLastNormalizedPos(lastNormalizedPos)
			lastNormalizedPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setLastNormalizedPos(lastNormalizedPos)
		return res
	#----------------------------------------------------------------------
	def setLastPos(self,lastPos):
		"""
		setLastPos(lastPos)
			lastPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setLastPos(lastPos)
		return res
	#----------------------------------------------------------------------
	def setLastScenePos(self,lastScenePos):
		"""
		setLastScenePos(lastScenePos)
			lastScenePos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setLastScenePos(lastScenePos)
		return res
	#----------------------------------------------------------------------
	def setLastScreenPos(self,lastScreenPos):
		"""
		setLastScreenPos(lastScreenPos)
			lastScreenPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setLastScreenPos(lastScreenPos)
		return res
	#----------------------------------------------------------------------
	def setNormalizedPos(self,normalizedPos):
		"""
		setNormalizedPos(normalizedPos)
			normalizedPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setNormalizedPos(normalizedPos)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setPressure(self,pressure):
		"""
		setPressure(pressure)
			pressure=QtCore.qreal


		"""
		res = super(QTouchEvent,self).setPressure(pressure)
		return res
	#----------------------------------------------------------------------
	def setRect(self,rect):
		"""
		setRect(rect)
			rect=QtCore.QRectF


		"""
		res = super(QTouchEvent,self).setRect(rect)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,scenePos):
		"""
		setScenePos(scenePos)
			scenePos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setScenePos(scenePos)
		return res
	#----------------------------------------------------------------------
	def setSceneRect(self,sceneRect):
		"""
		setSceneRect(sceneRect)
			sceneRect=QtCore.QRectF


		"""
		res = super(QTouchEvent,self).setSceneRect(sceneRect)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,screenPos):
		"""
		setScreenPos(screenPos)
			screenPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setScreenPos(screenPos)
		return res
	#----------------------------------------------------------------------
	def setScreenRect(self,screenRect):
		"""
		setScreenRect(screenRect)
			screenRect=QtCore.QRectF


		"""
		res = super(QTouchEvent,self).setScreenRect(screenRect)
		return res
	#----------------------------------------------------------------------
	def setStartNormalizedPos(self,startNormalizedPos):
		"""
		setStartNormalizedPos(startNormalizedPos)
			startNormalizedPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setStartNormalizedPos(startNormalizedPos)
		return res
	#----------------------------------------------------------------------
	def setStartPos(self,startPos):
		"""
		setStartPos(startPos)
			startPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setStartPos(startPos)
		return res
	#----------------------------------------------------------------------
	def setStartScenePos(self,startScenePos):
		"""
		setStartScenePos(startScenePos)
			startScenePos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setStartScenePos(startScenePos)
		return res
	#----------------------------------------------------------------------
	def setStartScreenPos(self,startScreenPos):
		"""
		setStartScreenPos(startScreenPos)
			startScreenPos=QtCore.QPointF


		"""
		res = super(QTouchEvent,self).setStartScreenPos(startScreenPos)
		return res
