from PySide import QtGui, QtCore

class QGraphicsSceneHoverEvent(QtGui.QGraphicsSceneHoverEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneHoverEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def lastPos(self):
		"""
		Returns the last recorded mouse cursor position in item coordinates.
		"""
		res = super(QGraphicsSceneHoverEvent,self).lastPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScenePos(self):
		"""
		Returns the last recorded, the scene coordinates of the previous mouse or hover event received by the view, that created the event mouse cursor position in scene coordinates.
		"""
		res = super(QGraphicsSceneHoverEvent,self).lastScenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScreenPos(self):
		"""
		Returns the last recorded mouse cursor position in screen coordinates
		The last recorded position is the position of the previous mouse or hover event received by the view that created the event.
		"""
		res = super(QGraphicsSceneHoverEvent,self).lastScreenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifiers at the moment the hover event was sent.
		"""
		res = super(QGraphicsSceneHoverEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse cursor in item coordinates at the moment the hover event was sent.
		"""
		res = super(QGraphicsSceneHoverEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the position of the mouse cursor in scene coordinates at the moment the hover event was sent.
		"""
		res = super(QGraphicsSceneHoverEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the position of the mouse cursor in screen coordinates at the moment the hover event was sent.
		"""
		res = super(QGraphicsSceneHoverEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def setLastPos(self,pos):
		"""
		setLastPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneHoverEvent,self).setLastPos(pos)
		return res
	#----------------------------------------------------------------------
	def setLastScenePos(self,pos):
		"""
		setLastScenePos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneHoverEvent,self).setLastScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setLastScreenPos(self,pos):
		"""
		setLastScreenPos(pos)
			pos=QtCore.QPoint


		"""
		res = super(QGraphicsSceneHoverEvent,self).setLastScreenPos(pos)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,modifiers):
		"""
		setModifiers(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QGraphicsSceneHoverEvent,self).setModifiers(modifiers)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF

		Sets the position associated with the hover event to the given point in item coordinates.
		"""
		res = super(QGraphicsSceneHoverEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF

		Sets the position associated with the hover event to the given point in scene coordinates.
		"""
		res = super(QGraphicsSceneHoverEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint

		Sets the position associated with the hover event to the given point in screen coordinates.
		"""
		res = super(QGraphicsSceneHoverEvent,self).setScreenPos(pos)
		return res
