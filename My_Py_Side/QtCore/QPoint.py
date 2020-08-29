from PySide import QtGui, QtCore

class QPoint(QtCore.QPoint):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPoint,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QPoint,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QPoint,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if both the x and y coordinates are set to 0, otherwise returns false.
		"""
		res = super(QPoint,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def manhattanLength(self):
		"""
		Returns the sum of the absolute values of PySide.QtCore.QPoint.x() and PySide.QtCore.QPoint.y() , traditionally known as the Manhattan length of the vector from the origin to the point
		For example:
		This is a useful, and quick to calculate, approximation to the true length:
		The tradition of Manhattan length arises because such distances apply to travelers who can only travel on a rectangular grid, like the streets of Manhattan.
		"""
		res = super(QPoint,self).manhattanLength()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QPoint,self).__sub__()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QPoint,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x coordinate of this point.
		"""
		res = super(QPoint,self).x()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y coordinate of this point.
		"""
		res = super(QPoint,self).y()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,p2):
		"""
		__ne__(p2)
			p2=QtCore.QPoint


		"""
		res = super(QPoint,self).__ne__(p2)
		isinstance(res,bool)
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
		res = super(QPoint,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,c):
		"""
		__imul__(c)
			c=QtCore.qreal

		Multiplies this points coordinates by the given factor , and returns a reference to this point
		For example:
		Note that the result is rounded to the nearest integer as points are held as integers
		Use PySide.QtCore.QPointF for floating point accuracy.
		"""
		res = super(QPoint,self).__imul__(c)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __add__(self,p2):
		"""
		__add__(p2)
			p2=QtCore.QPoint


		"""
		res = super(QPoint,self).__add__(p2)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,p):
		"""
		__iadd__(p)
			p=QtCore.QPoint

		Adds the given point to this point and returns a reference to this point
		For example:
		"""
		res = super(QPoint,self).__iadd__(p)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,p2):
		"""
		__sub__(p2)
			p2=QtCore.QPoint


		"""
		res = super(QPoint,self).__sub__(p2)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,p):
		"""
		__isub__(p)
			p=QtCore.QPoint

		Subtracts the given point from this point and returns a reference to this point
		For example:
		"""
		res = super(QPoint,self).__isub__(p)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __div__(self,c):
		"""
		__div__(c)
			c=QtCore.qreal


		"""
		res = super(QPoint,self).__div__(c)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,c):
		"""
		__idiv__(c)
			c=QtCore.qreal

		This is an overloaded function.
		Divides both x and y by the given divisor , and returns a reference to this point
		For example:
		Note that the result is rounded to the nearest integer as points are held as integers
		Use PySide.QtCore.QPointF for floating point accuracy.
		"""
		res = super(QPoint,self).__idiv__(c)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,p2):
		"""
		__eq__(p2)
			p2=QtCore.QPoint


		"""
		res = super(QPoint,self).__eq__(p2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.int

		Sets the x coordinate of this point to the given x coordinate.
		"""
		res = super(QPoint,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.int

		Sets the y coordinate of this point to the given y coordinate.
		"""
		res = super(QPoint,self).setY(y)
		return res
