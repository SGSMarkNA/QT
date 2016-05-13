from PySide import QtGui, QtCore

class QGraphicsSceneContextMenuEvent(QtGui.QGraphicsSceneContextMenuEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneContextMenuEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifiers in use when the context menu was requested.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the mouse cursor in item coordinates at the moment the context menu was requested.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def reason(self):
		"""
		Returns the reason for the context menu event.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).reason()
		isinstance(res,QtGui.QGraphicsSceneContextMenuEvent.Reason)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the position of the mouse cursor in scene coordinates at the moment the the context menu was requested.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the position of the mouse cursor in screen coordinates at the moment the the context menu was requested.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,modifiers):
		"""
		setModifiers(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QGraphicsSceneContextMenuEvent,self).setModifiers(modifiers)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF

		Sets the position associated with the context menu to the given point in item coordinates.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setReason(self,reason):
		"""
		setReason(reason)
			reason=QtGui.QGraphicsSceneContextMenuEvent.Reason

		Sets the reason for the context menu event to reason .
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).setReason(reason)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF

		Sets the position associated with the context menu to the given point in scene coordinates.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint

		Sets the position associated with the context menu to the given point in screen coordinates.
		"""
		res = super(QGraphicsSceneContextMenuEvent,self).setScreenPos(pos)
		return res
