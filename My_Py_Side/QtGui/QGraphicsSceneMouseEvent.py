from PySide import QtGui, QtCore

class QGraphicsSceneMouseEvent(QtGui.QGraphicsSceneMouseEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneMouseEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def button(self):
		"""
		Returns the mouse button (if any) that caused the event.
		"""
		res = super(QGraphicsSceneMouseEvent,self).button()
		isinstance(res,QtCore.Qt.MouseButton)
		return res
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns the combination of mouse buttons that were pressed at the time the event was sent.
		"""
		res = super(QGraphicsSceneMouseEvent,self).buttons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def lastPos(self):
		"""
		Returns the last recorded mouse cursor position in item coordinates.
		"""
		res = super(QGraphicsSceneMouseEvent,self).lastPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScenePos(self):
		"""
		Returns the last recorded mouse cursor position in scene coordinates
		The last recorded position is the position of the previous mouse event received by the view that created the event.
		"""
		res = super(QGraphicsSceneMouseEvent,self).lastScenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def lastScreenPos(self):
		"""
		Returns the last recorded mouse cursor position in screen coordinates
		The last recorded position is the position of the previous mouse event received by the view that created the event.
		"""
		res = super(QGraphicsSceneMouseEvent,self).lastScreenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifiers in use at the time the event was sent.
		"""
		res = super(QGraphicsSceneMouseEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the mouse cursor position in item coordinates.
		"""
		res = super(QGraphicsSceneMouseEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the mouse cursor position in scene coordinates.
		"""
		res = super(QGraphicsSceneMouseEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the mouse cursor position in screen coordinates.
		"""
		res = super(QGraphicsSceneMouseEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def buttonDownPos(self,button):
		"""
		buttonDownPos(button)
			button=QtCore.Qt.MouseButton


		"""
		res = super(QGraphicsSceneMouseEvent,self).buttonDownPos(button)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def buttonDownScenePos(self,button):
		"""
		buttonDownScenePos(button)
			button=QtCore.Qt.MouseButton


		"""
		res = super(QGraphicsSceneMouseEvent,self).buttonDownScenePos(button)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def buttonDownScreenPos(self,button):
		"""
		buttonDownScreenPos(button)
			button=QtCore.Qt.MouseButton


		"""
		res = super(QGraphicsSceneMouseEvent,self).buttonDownScreenPos(button)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def setButton(self,button):
		"""
		setButton(button)
			button=QtCore.Qt.MouseButton


		"""
		res = super(QGraphicsSceneMouseEvent,self).setButton(button)
		return res
	#----------------------------------------------------------------------
	def setButtonDownPos(self,button,pos):
		"""
		setButtonDownPos(button,pos)
			button=QtCore.Qt.MouseButton
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setButtonDownPos(button,pos)
		return res
	#----------------------------------------------------------------------
	def setButtonDownScenePos(self,button,pos):
		"""
		setButtonDownScenePos(button,pos)
			button=QtCore.Qt.MouseButton
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setButtonDownScenePos(button,pos)
		return res
	#----------------------------------------------------------------------
	def setButtonDownScreenPos(self,button,pos):
		"""
		setButtonDownScreenPos(button,pos)
			button=QtCore.Qt.MouseButton
			pos=QtCore.QPoint


		"""
		res = super(QGraphicsSceneMouseEvent,self).setButtonDownScreenPos(button,pos)
		return res
	#----------------------------------------------------------------------
	def setButtons(self,buttons):
		"""
		setButtons(buttons)
			buttons=QtCore.Qt.MouseButtons


		"""
		res = super(QGraphicsSceneMouseEvent,self).setButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def setLastPos(self,pos):
		"""
		setLastPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setLastPos(pos)
		return res
	#----------------------------------------------------------------------
	def setLastScenePos(self,pos):
		"""
		setLastScenePos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setLastScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setLastScreenPos(self,pos):
		"""
		setLastScreenPos(pos)
			pos=QtCore.QPoint


		"""
		res = super(QGraphicsSceneMouseEvent,self).setLastScreenPos(pos)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,modifiers):
		"""
		setModifiers(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QGraphicsSceneMouseEvent,self).setModifiers(modifiers)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMouseEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint


		"""
		res = super(QGraphicsSceneMouseEvent,self).setScreenPos(pos)
		return res
