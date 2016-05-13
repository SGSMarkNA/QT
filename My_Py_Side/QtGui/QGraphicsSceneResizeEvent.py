from PySide import QtGui, QtCore

class QGraphicsSceneResizeEvent(QtGui.QGraphicsSceneResizeEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneResizeEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def newSize(self):
		"""
		Returns the new size (i.e., the current size).
		"""
		res = super(QGraphicsSceneResizeEvent,self).newSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def oldSize(self):
		"""
		Returns the old size (i.e., the size immediately before the widget was resized).
		"""
		res = super(QGraphicsSceneResizeEvent,self).oldSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def setNewSize(self,size):
		"""
		setNewSize(size)
			size=QtCore.QSizeF


		"""
		res = super(QGraphicsSceneResizeEvent,self).setNewSize(size)
		return res
	#----------------------------------------------------------------------
	def setOldSize(self,size):
		"""
		setOldSize(size)
			size=QtCore.QSizeF


		"""
		res = super(QGraphicsSceneResizeEvent,self).setOldSize(size)
		return res
