from PySide import QtGui, QtCore

class QVector2D(QtGui.QVector2D):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QVector2D,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QVector2D,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QVector2D,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the x and y coordinates are set to 0.0, otherwise returns false.
		"""
		res = super(QVector2D,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the vector from the origin.
		"""
		res = super(QVector2D,self).length()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lengthSquared(self):
		"""
		Returns the squared length of the vector from the origin
		This is equivalent to the dot product of the vector with itself.
		"""
		res = super(QVector2D,self).lengthSquared()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalize(self):
		"""
		Normalizes the currect vector in place
		Nothing happens if this vector is a null vector or the length of the vector is very close to 1.
		"""
		res = super(QVector2D,self).normalize()
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns the normalized unit vector form of this vector.
		If this vector is null, then a null vector is returned
		If the length of the vector is very close to 1, then the vector will be returned as-is
		Otherwise the normalized form of the vector of length 1 will be returned.
		"""
		res = super(QVector2D,self).normalized()
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QVector2D,self).__sub__()
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def toPoint(self):
		"""
		Returns the PySide.QtCore.QPoint form of this 2D vector.
		"""
		res = super(QVector2D,self).toPoint()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toPointF(self):
		"""
		Returns the PySide.QtCore.QPointF form of this 2D vector.
		"""
		res = super(QVector2D,self).toPointF()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QVector2D,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def toVector3D(self):
		"""
		Returns the 3D form of this 2D vector, with the z coordinate set to zero.
		"""
		res = super(QVector2D,self).toVector3D()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def toVector4D(self):
		"""
		Returns the 4D form of this 2D vector, with the z and w coordinates set to zero.
		"""
		res = super(QVector2D,self).toVector4D()
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x coordinate of this point.
		"""
		res = super(QVector2D,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y coordinate of this point.
		"""
		res = super(QVector2D,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v2):
		"""
		__ne__(v2)
			v2=QtGui.QVector2D


		"""
		res = super(QVector2D,self).__ne__(v2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(factor)
			factor=QtCore.qreal

		__mul__(factor)
			factor=QtCore.qreal

		__mul__(v2)
			v2=QtGui.QVector2D


		"""
		res = super(QVector2D,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(vector)
			vector=QtGui.QVector2D

		__imul__(factor)
			factor=QtCore.qreal

		Multiplies the components of this vector by the corresponding components in vector .
		"""
		res = super(QVector2D,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __add__(self,v2):
		"""
		__add__(v2)
			v2=QtGui.QVector2D


		"""
		res = super(QVector2D,self).__add__(v2)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,vector):
		"""
		__iadd__(vector)
			vector=QtGui.QVector2D

		Adds the given vector to this vector and returns a reference to this vector.
		"""
		res = super(QVector2D,self).__iadd__(vector)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,v2):
		"""
		__sub__(v2)
			v2=QtGui.QVector2D


		"""
		res = super(QVector2D,self).__sub__(v2)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,vector):
		"""
		__isub__(vector)
			vector=QtGui.QVector2D

		Subtracts the given vector from this vector and returns a reference to this vector.
		"""
		res = super(QVector2D,self).__isub__(vector)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __div__(self,divisor):
		"""
		__div__(divisor)
			divisor=QtCore.qreal


		"""
		res = super(QVector2D,self).__div__(divisor)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,divisor):
		"""
		__idiv__(divisor)
			divisor=QtCore.qreal

		Divides this vectors coordinates by the given divisor , and returns a reference to this vector.
		"""
		res = super(QVector2D,self).__idiv__(divisor)
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v2):
		"""
		__eq__(v2)
			v2=QtGui.QVector2D


		"""
		res = super(QVector2D,self).__eq__(v2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of this point to the given x coordinate.
		"""
		res = super(QVector2D,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of this point to the given y coordinate.
		"""
		res = super(QVector2D,self).setY(y)
		return res
