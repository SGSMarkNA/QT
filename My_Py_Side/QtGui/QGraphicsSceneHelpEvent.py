from PySide import QtGui, QtCore

class QGraphicsSceneHelpEvent(QtGui.QGraphicsSceneHelpEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneHelpEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the position of the mouse cursor in scene coordinates at the moment the help event was sent.
		"""
		res = super(QGraphicsSceneHelpEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the position of the mouse cursor in screen coordinates at the moment the help event was sent.
		"""
		res = super(QGraphicsSceneHelpEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF

		Sets the position associated with the context menu to the given point in scene coordinates.
		"""
		res = super(QGraphicsSceneHelpEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint

		Sets the position associated with the context menu to the given point in screen coordinates.
		"""
		res = super(QGraphicsSceneHelpEvent,self).setScreenPos(pos)
		return res
