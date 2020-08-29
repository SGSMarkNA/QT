from PySide import QtGui, QtCore

class QVector4D(QtGui.QVector4D):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QVector4D,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QVector4D,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QVector4D,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the x, y, z, and w coordinates are set to 0.0, otherwise returns false.
		"""
		res = super(QVector4D,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the vector from the origin.
		"""
		res = super(QVector4D,self).length()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lengthSquared(self):
		"""
		Returns the squared length of the vector from the origin
		This is equivalent to the dot product of the vector with itself.
		"""
		res = super(QVector4D,self).lengthSquared()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalize(self):
		"""
		Normalizes the currect vector in place
		Nothing happens if this vector is a null vector or the length of the vector is very close to 1.
		"""
		res = super(QVector4D,self).normalize()
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns the normalized unit vector form of this vector.
		If this vector is null, then a null vector is returned
		If the length of the vector is very close to 1, then the vector will be returned as-is
		Otherwise the normalized form of the vector of length 1 will be returned.
		"""
		res = super(QVector4D,self).normalized()
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QVector4D,self).__sub__()
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def toPoint(self):
		"""
		Returns the PySide.QtCore.QPoint form of this 4D vector
		The z and w coordinates are dropped.
		"""
		res = super(QVector4D,self).toPoint()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toPointF(self):
		"""
		Returns the PySide.QtCore.QPointF form of this 4D vector
		The z and w coordinates are dropped.
		"""
		res = super(QVector4D,self).toPointF()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QVector4D,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def toVector2D(self):
		"""
		Returns the 2D vector form of this 4D vector, dropping the z and w coordinates.
		"""
		res = super(QVector4D,self).toVector2D()
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def toVector2DAffine(self):
		"""
		Returns the 2D vector form of this 4D vector, dividing the x and y coordinates by the w coordinate and dropping the z coordinate
		Returns a null vector if w is zero.
		"""
		res = super(QVector4D,self).toVector2DAffine()
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def toVector3D(self):
		"""
		Returns the 3D vector form of this 4D vector, dropping the w coordinate.
		"""
		res = super(QVector4D,self).toVector3D()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def toVector3DAffine(self):
		"""
		Returns the 3D vector form of this 4D vector, dividing the x, y, and z coordinates by the w coordinate
		Returns a null vector if w is zero.
		"""
		res = super(QVector4D,self).toVector3DAffine()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def w(self):
		"""
		Returns the w coordinate of this point.
		"""
		res = super(QVector4D,self).w()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x coordinate of this point.
		"""
		res = super(QVector4D,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y coordinate of this point.
		"""
		res = super(QVector4D,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def z(self):
		"""
		Returns the z coordinate of this point.
		"""
		res = super(QVector4D,self).z()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v2):
		"""
		__ne__(v2)
			v2=QtGui.QVector4D


		"""
		res = super(QVector4D,self).__ne__(v2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(factor)
			factor=QtCore.qreal

		__mul__(factor)
			factor=QtCore.qreal

		__mul__(matrix)
			matrix=QtGui.QMatrix4x4

		__mul__(matrix)
			matrix=QtGui.QMatrix4x4

		__mul__(v2)
			v2=QtGui.QVector4D


		"""
		res = super(QVector4D,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(factor)
			factor=QtCore.qreal

		__imul__(vector)
			vector=QtGui.QVector4D

		Multiplies this vectors coordinates by the given factor , and returns a reference to this vector.
		"""
		res = super(QVector4D,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __add__(self,v2):
		"""
		__add__(v2)
			v2=QtGui.QVector4D


		"""
		res = super(QVector4D,self).__add__(v2)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,vector):
		"""
		__iadd__(vector)
			vector=QtGui.QVector4D

		Adds the given vector to this vector and returns a reference to this vector.
		"""
		res = super(QVector4D,self).__iadd__(vector)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,v2):
		"""
		__sub__(v2)
			v2=QtGui.QVector4D


		"""
		res = super(QVector4D,self).__sub__(v2)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,vector):
		"""
		__isub__(vector)
			vector=QtGui.QVector4D

		Subtracts the given vector from this vector and returns a reference to this vector.
		"""
		res = super(QVector4D,self).__isub__(vector)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __div__(self,divisor):
		"""
		__div__(divisor)
			divisor=QtCore.qreal


		"""
		res = super(QVector4D,self).__div__(divisor)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,divisor):
		"""
		__idiv__(divisor)
			divisor=QtCore.qreal

		Divides this vectors coordinates by the given divisor , and returns a reference to this vector.
		"""
		res = super(QVector4D,self).__idiv__(divisor)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v2):
		"""
		__eq__(v2)
			v2=QtGui.QVector4D


		"""
		res = super(QVector4D,self).__eq__(v2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setW(self,w):
		"""
		setW(w)
			w=QtCore.qreal

		Sets the w coordinate of this point to the given w coordinate.
		"""
		res = super(QVector4D,self).setW(w)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of this point to the given x coordinate.
		"""
		res = super(QVector4D,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of this point to the given y coordinate.
		"""
		res = super(QVector4D,self).setY(y)
		return res
	#----------------------------------------------------------------------
	def setZ(self,z):
		"""
		setZ(z)
			z=QtCore.qreal

		Sets the z coordinate of this point to the given z coordinate.
		"""
		res = super(QVector4D,self).setZ(z)
		return res
