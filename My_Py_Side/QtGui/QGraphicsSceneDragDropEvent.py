from PySide import QtGui, QtCore

class QGraphicsSceneDragDropEvent(QtGui.QGraphicsSceneDragDropEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneDragDropEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceptProposedAction(self):
		"""
		Sets the proposed action as accepted, i.e, the drop action is set to the proposed action
		This is equal to:
		When using this function, one should not call accept() .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).acceptProposedAction()
		return res
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns a Qt.MouseButtons value indicating which buttons were pressed on the mouse when this mouse event was generated.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).buttons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def dropAction(self):
		"""
		Returns the action that was performed in this drag and drop
		This should be set by the receiver of the drop and is returned by QDrag.exec() .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).dropAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def mimeData(self):
		"""
		This function returns the MIME data of the event.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).mimeData()
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifiers that were pressed when the drag and drop event was created.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the mouse position of the event relative to the view that sent the event.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def possibleActions(self):
		"""
		Returns the possible drop actions that the drag and drop can result in.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).possibleActions()
		isinstance(res,QtCore.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def proposedAction(self):
		"""
		Returns the drop action that is proposed, i.e., preferred
		The action must be one of the possible actions as defined by possibleActions() .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).proposedAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the position of the mouse in scene coordinates.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the position of the mouse relative to the screen.
		"""
		res = super(QGraphicsSceneDragDropEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def source(self):
		"""
		This function returns the PySide.QtGui.QGraphicsView that created the PySide.QtGui.QGraphicsSceneDragDropEvent .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).source()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setButtons(self,buttons):
		"""
		setButtons(buttons)
			buttons=QtCore.Qt.MouseButtons


		"""
		res = super(QGraphicsSceneDragDropEvent,self).setButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def setDropAction(self,action):
		"""
		setDropAction(action)
			action=QtCore.Qt.DropAction


		"""
		res = super(QGraphicsSceneDragDropEvent,self).setDropAction(action)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,modifiers):
		"""
		setModifiers(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QGraphicsSceneDragDropEvent,self).setModifiers(modifiers)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF

		Sets the position of the mouse to pos ; this should be relative to the widget that generated the event, which normally is a PySide.QtGui.QGraphicsView .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setPossibleActions(self,actions):
		"""
		setPossibleActions(actions)
			actions=QtCore.Qt.DropActions


		"""
		res = super(QGraphicsSceneDragDropEvent,self).setPossibleActions(actions)
		return res
	#----------------------------------------------------------------------
	def setProposedAction(self,action):
		"""
		setProposedAction(action)
			action=QtCore.Qt.DropAction


		"""
		res = super(QGraphicsSceneDragDropEvent,self).setProposedAction(action)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF

		Sets the scene position of the mouse to pos .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint

		Sets the mouse position relative to the screen to pos .
		"""
		res = super(QGraphicsSceneDragDropEvent,self).setScreenPos(pos)
		return res
