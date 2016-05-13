from PySide import QtGui, QtCore

class QGraphicsSceneMoveEvent(QtGui.QGraphicsSceneMoveEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneMoveEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def newPos(self):
		"""
		Returns the new position (i.e., the current position).
		"""
		res = super(QGraphicsSceneMoveEvent,self).newPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def oldPos(self):
		"""
		Returns the old position (i.e., the position immediately before the widget was moved).
		"""
		res = super(QGraphicsSceneMoveEvent,self).oldPos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setNewPos(self,pos):
		"""
		setNewPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMoveEvent,self).setNewPos(pos)
		return res
	#----------------------------------------------------------------------
	def setOldPos(self,pos):
		"""
		setOldPos(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsSceneMoveEvent,self).setOldPos(pos)
		return res
