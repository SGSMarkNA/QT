from PySide import QtGui, QtCore

class QGraphicsPathItem(QtGui.QGraphicsPathItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsPathItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the items path as a PySide.QtGui.QPainterPath
		If no item has been set, an empty PySide.QtGui.QPainterPath is returned.
		"""
		res = super(QGraphicsPathItem,self).path()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def setPath(self,path):
		"""
		setPath(path)
			path=QtGui.QPainterPath

		Sets the items path to be the given path .
		"""
		res = super(QGraphicsPathItem,self).setPath(path)
		return res
