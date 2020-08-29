from PySide import QtGui, QtCore

class QVector3D(QtGui.QVector3D):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QVector3D,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QVector3D,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QVector3D,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the x, y, and z coordinates are set to 0.0, otherwise returns false.
		"""
		res = super(QVector3D,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the vector from the origin.
		"""
		res = super(QVector3D,self).length()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lengthSquared(self):
		"""
		Returns the squared length of the vector from the origin
		This is equivalent to the dot product of the vector with itself.
		"""
		res = super(QVector3D,self).lengthSquared()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalize(self):
		"""
		Normalizes the currect vector in place
		Nothing happens if this vector is a null vector or the length of the vector is very close to 1.
		"""
		res = super(QVector3D,self).normalize()
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns the normalized unit vector form of this vector.
		If this vector is null, then a null vector is returned
		If the length of the vector is very close to 1, then the vector will be returned as-is
		Otherwise the normalized form of the vector of length 1 will be returned.
		"""
		res = super(QVector3D,self).normalized()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QVector3D,self).__sub__()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def toPoint(self):
		"""
		Returns the PySide.QtCore.QPoint form of this 3D vector
		The z coordinate is dropped.
		"""
		res = super(QVector3D,self).toPoint()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toPointF(self):
		"""
		Returns the PySide.QtCore.QPointF form of this 3D vector
		The z coordinate is dropped.
		"""
		res = super(QVector3D,self).toPointF()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QVector3D,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def toVector2D(self):
		"""
		Returns the 2D vector form of this 3D vector, dropping the z coordinate.
		"""
		res = super(QVector3D,self).toVector2D()
		isinstance(res,QtGui.QVector2D)
		return res
	#----------------------------------------------------------------------
	def toVector4D(self):
		"""
		Returns the 4D form of this 3D vector, with the w coordinate set to zero.
		"""
		res = super(QVector3D,self).toVector4D()
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x coordinate of this point.
		"""
		res = super(QVector3D,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y coordinate of this point.
		"""
		res = super(QVector3D,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def z(self):
		"""
		Returns the z coordinate of this point.
		"""
		res = super(QVector3D,self).z()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def distanceToLine(self,point,direction):
		"""
		distanceToLine(point,direction)
			point=QtGui.QVector3D
			direction=QtGui.QVector3D

		Returns the distance that this vertex is from a line defined by point and the unit vector direction .
		If direction is a null vector, then it does not define a line
		In that case, the distance from point to this vertex is returned.
		"""
		res = super(QVector3D,self).distanceToLine(point,direction)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def distanceToPlane(self,*args,**kwargs):
		"""
		distanceToPlane(plane1,plane2,plane3)
			plane1=QtGui.QVector3D
			plane2=QtGui.QVector3D
			plane3=QtGui.QVector3D

		distanceToPlane(plane,normal)
			plane=QtGui.QVector3D
			normal=QtGui.QVector3D

		This is an overloaded function.
		Returns the distance from this vertex a plane defined by the vertices plane1 , plane2 and plane3 .
		The return value will be negative if the vertex is below the plane, or zero if it is on the plane.
		The two vectors that define the plane are plane2 - plane1 and plane3 - plane1 .
		"""
		res = super(QVector3D,self).distanceToPlane(*args,**kwargs)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v2):
		"""
		__ne__(v2)
			v2=QtGui.QVector3D


		"""
		res = super(QVector3D,self).__ne__(v2)
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

		__mul__(v2)
			v2=QtGui.QVector3D

		__mul__(matrix)
			matrix=QtGui.QMatrix4x4


		"""
		res = super(QVector3D,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(factor)
			factor=QtCore.qreal

		__imul__(vector)
			vector=QtGui.QVector3D

		Multiplies this vectors coordinates by the given factor , and returns a reference to this vector.
		"""
		res = super(QVector3D,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __add__(self,v2):
		"""
		__add__(v2)
			v2=QtGui.QVector3D


		"""
		res = super(QVector3D,self).__add__(v2)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,vector):
		"""
		__iadd__(vector)
			vector=QtGui.QVector3D

		Adds the given vector to this vector and returns a reference to this vector.
		"""
		res = super(QVector3D,self).__iadd__(vector)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,v2):
		"""
		__sub__(v2)
			v2=QtGui.QVector3D


		"""
		res = super(QVector3D,self).__sub__(v2)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,vector):
		"""
		__isub__(vector)
			vector=QtGui.QVector3D

		Subtracts the given vector from this vector and returns a reference to this vector.
		"""
		res = super(QVector3D,self).__isub__(vector)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __div__(self,divisor):
		"""
		__div__(divisor)
			divisor=QtCore.qreal


		"""
		res = super(QVector3D,self).__div__(divisor)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,divisor):
		"""
		__idiv__(divisor)
			divisor=QtCore.qreal

		Divides this vectors coordinates by the given divisor , and returns a reference to this vector.
		"""
		res = super(QVector3D,self).__idiv__(divisor)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v2):
		"""
		__eq__(v2)
			v2=QtGui.QVector3D


		"""
		res = super(QVector3D,self).__eq__(v2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of this point to the given x coordinate.
		"""
		res = super(QVector3D,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of this point to the given y coordinate.
		"""
		res = super(QVector3D,self).setY(y)
		return res
	#----------------------------------------------------------------------
	def setZ(self,z):
		"""
		setZ(z)
			z=QtCore.qreal

		Sets the z coordinate of this point to the given z coordinate.
		"""
		res = super(QVector3D,self).setZ(z)
		return res
