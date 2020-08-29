from PySide import QtGui, QtCore

class QGraphicsSceneWheelEvent(QtGui.QGraphicsSceneWheelEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneWheelEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns the mouse buttons that were pressed when the wheel event occurred.
		"""
		res = super(QGraphicsSceneWheelEvent,self).buttons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def delta(self):
		"""
		Returns the distance that the wheel is rotated, in eighths (1/8s) of a degree
		A positive value indicates that the wheel was rotated forwards away from the user; a negative value indicates that the wheel was rotated backwards toward the user.
		Most mouse types work in steps of 15 degrees, in which case the delta value is a multiple of 120 (== 15 * 8).
		"""
		res = super(QGraphicsSceneWheelEvent,self).delta()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def modifiers(self):
		"""
		Returns the keyboard modifiers that were active when the wheel event occurred.
		"""
		res = super(QGraphicsSceneWheelEvent,self).modifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the wheel orientation.
		"""
		res = super(QGraphicsSceneWheelEvent,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the cursor in item coordinates when the wheel event occurred.
		"""
		res = super(QGraphicsSceneWheelEvent,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the position of the cursor in scene coordinates when the wheel event occurred.
		"""
		res = super(QGraphicsSceneWheelEvent,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def screenPos(self):
		"""
		Returns the position of the cursor in screen coordinates when the wheel event occurred.
		"""
		res = super(QGraphicsSceneWheelEvent,self).screenPos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def setButtons(self,buttons):
		"""
		setButtons(buttons)
			buttons=QtCore.Qt.MouseButtons


		"""
		res = super(QGraphicsSceneWheelEvent,self).setButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def setDelta(self,delta):
		"""
		setDelta(delta)
			delta=QtCore.int


		"""
		res = super(QGraphicsSceneWheelEvent,self).setDelta(delta)
		return res
	#----------------------------------------------------------------------
	def setModifiers(self,modifiers):
		"""
		setModifiers(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QGraphicsSceneWheelEvent,self).setModifiers(modifiers)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,orientation):
		"""
		setOrientation(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QGraphicsSceneWheelEvent,self).setOrientation(orientation)
		return res
	#----------------------------------------------------------------------
	def setPos(self,pos):
		"""
		setPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneWheelEvent,self).setPos(pos)
		return res
	#----------------------------------------------------------------------
	def setScenePos(self,pos):
		"""
		setScenePos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneWheelEvent,self).setScenePos(pos)
		return res
	#----------------------------------------------------------------------
	def setScreenPos(self,pos):
		"""
		setScreenPos(pos)
			pos=QtCore.QPoint


		"""
		res = super(QGraphicsSceneWheelEvent,self).setScreenPos(pos)
		return res
