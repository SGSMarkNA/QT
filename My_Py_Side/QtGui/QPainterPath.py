from PySide import QtGui, QtCore

class QPainterPath(QtGui.QPainterPath):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPainterPath,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isCurveTo(self):
		"""
		Returns true if the element is a curve, otherwise returns false.
		"""
		res = super(QPainterPath,self).isCurveTo()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isLineTo(self):
		"""
		Returns true if the element is a line, otherwise returns false.
		"""
		res = super(QPainterPath,self).isLineTo()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isMoveTo(self):
		"""
		Returns true if the element is moving the current position, otherwise returns false.
		"""
		res = super(QPainterPath,self).isMoveTo()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,e):
		"""
		__ne__(e)
			e=QtGui.QPainterPath::Element

		Returns true if this element is not equal to other ; otherwise returns false.
		"""
		res = super(QPainterPath,self).__ne__(e)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,e):
		"""
		__eq__(e)
			e=QtGui.QPainterPath::Element

		Returns true if this element is equal to other ; otherwise returns false.
		"""
		res = super(QPainterPath,self).__eq__(e)
		isinstance(res,QtCore.bool)
		return res
