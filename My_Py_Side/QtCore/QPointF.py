from PySide import QtGui, QtCore

class QPointF(QtCore.QPointF):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPointF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QPointF,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QPointF,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if both the x and y coordinates are set to +0.0; otherwise returns false.
		"""
		res = super(QPointF,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def manhattanLength(self):
		"""
		Returns the sum of the absolute values of PySide.QtCore.QPointF.x() and PySide.QtCore.QPointF.y() , traditionally known as the Manhattan length of the vector from the origin to the point.
		"""
		res = super(QPointF,self).manhattanLength()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QPointF,self).__sub__()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def toPoint(self):
		"""
		Rounds the coordinates of this point to the nearest integer, and returns a PySide.QtCore.QPoint object with the rounded coordinates.
		"""
		res = super(QPointF,self).toPoint()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QPointF,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x-coordinate of this point.
		"""
		res = super(QPointF,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y-coordinate of this point.
		"""
		res = super(QPointF,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,p2):
		"""
		__ne__(p2)
			p2=QtCore.QPointF


		"""
		res = super(QPointF,self).__ne__(p2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(c)
			c=QtCore.qreal

		__mul__(c)
			c=QtCore.qreal

		__mul__(m)
			m=QtGui.QTransform

		__mul__(matrix)
			matrix=QtGui.QMatrix4x4

		__mul__(m)
			m=QtGui.QMatrix

		__mul__(matrix)
			matrix=QtGui.QMatrix4x4


		"""
		res = super(QPointF,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,c):
		"""
		__imul__(c)
			c=QtCore.qreal

		Multiplies this points coordinates by the given factor , and returns a reference to this point
		For example:
		"""
		res = super(QPointF,self).__imul__(c)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __add__(self,p2):
		"""
		__add__(p2)
			p2=QtCore.QPointF


		"""
		res = super(QPointF,self).__add__(p2)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,p):
		"""
		__iadd__(p)
			p=QtCore.QPointF

		Adds the given point to this point and returns a reference to this point
		For example:
		"""
		res = super(QPointF,self).__iadd__(p)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,p2):
		"""
		__sub__(p2)
			p2=QtCore.QPointF


		"""
		res = super(QPointF,self).__sub__(p2)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,p):
		"""
		__isub__(p)
			p=QtCore.QPointF

		Subtracts the given point from this point and returns a reference to this point
		For example:
		"""
		res = super(QPointF,self).__isub__(p)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __div__(self,c):
		"""
		__div__(c)
			c=QtCore.qreal


		"""
		res = super(QPointF,self).__div__(c)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,c):
		"""
		__idiv__(c)
			c=QtCore.qreal

		Divides both x and y by the given divisor , and returns a reference to this point
		For example:
		"""
		res = super(QPointF,self).__idiv__(c)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,p2):
		"""
		__eq__(p2)
			p2=QtCore.QPointF


		"""
		res = super(QPointF,self).__eq__(p2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of this point to the given x coordinate.
		"""
		res = super(QPointF,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of this point to the given y coordinate.
		"""
		res = super(QPointF,self).setY(y)
		return res
