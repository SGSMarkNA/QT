from PySide import QtGui, QtCore

class QQuaternion(QtGui.QQuaternion):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QQuaternion,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QQuaternion,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QQuaternion,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def conjugate(self):
		"""
		Returns the conjugate of this quaternion, which is (-x, -y, -z, scalar).
		"""
		res = super(QQuaternion,self).conjugate()
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def isIdentity(self):
		"""
		Returns true if the x, y, and z components of this quaternion are set to 0.0, and the scalar component is set to 1.0; otherwise returns false.
		"""
		res = super(QQuaternion,self).isIdentity()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the x, y, z, and scalar components of this quaternion are set to 0.0; otherwise returns false.
		"""
		res = super(QQuaternion,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the quaternion
		This is also called the norm.
		"""
		res = super(QQuaternion,self).length()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lengthSquared(self):
		"""
		Returns the squared length of the quaternion.
		"""
		res = super(QQuaternion,self).lengthSquared()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalize(self):
		"""
		Normalizes the currect quaternion in place
		Nothing happens if this is a null quaternion or the length of the quaternion is very close to 1.
		"""
		res = super(QQuaternion,self).normalize()
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns the normalized unit form of this quaternion.
		If this quaternion is null, then a null quaternion is returned
		If the length of the quaternion is very close to 1, then the quaternion will be returned as-is
		Otherwise the normalized form of the quaternion of length 1 will be returned.
		"""
		res = super(QQuaternion,self).normalized()
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QQuaternion,self).__sub__()
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def scalar(self):
		"""
		Returns the scalar component of this quaternion.
		"""
		res = super(QQuaternion,self).scalar()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def toVector4D(self):
		"""
		Returns this quaternion as a 4D vector.
		"""
		res = super(QQuaternion,self).toVector4D()
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def vector(self):
		"""
		Returns the vector component of this quaternion.
		"""
		res = super(QQuaternion,self).vector()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x coordinate of this quaternions vector.
		"""
		res = super(QQuaternion,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y coordinate of this quaternions vector.
		"""
		res = super(QQuaternion,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def z(self):
		"""
		Returns the z coordinate of this quaternions vector.
		"""
		res = super(QQuaternion,self).z()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,q2):
		"""
		__ne__(q2)
			q2=QtGui.QQuaternion


		"""
		res = super(QQuaternion,self).__ne__(q2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(factor)
			factor=QtCore.qreal

		__mul__(factor)
			factor=QtCore.qreal

		__mul__(q2)
			q2=QtGui.QQuaternion


		"""
		res = super(QQuaternion,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(factor)
			factor=QtCore.qreal

		__imul__(quaternion)
			quaternion=QtGui.QQuaternion

		Multiplies this quaternions components by the given factor , and returns a reference to this quaternion.
		"""
		res = super(QQuaternion,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __add__(self,q2):
		"""
		__add__(q2)
			q2=QtGui.QQuaternion


		"""
		res = super(QQuaternion,self).__add__(q2)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,quaternion):
		"""
		__iadd__(quaternion)
			quaternion=QtGui.QQuaternion

		Adds the given quaternion to this quaternion and returns a reference to this quaternion.
		"""
		res = super(QQuaternion,self).__iadd__(quaternion)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,q2):
		"""
		__sub__(q2)
			q2=QtGui.QQuaternion


		"""
		res = super(QQuaternion,self).__sub__(q2)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,quaternion):
		"""
		__isub__(quaternion)
			quaternion=QtGui.QQuaternion

		Subtracts the given quaternion from this quaternion and returns a reference to this quaternion.
		"""
		res = super(QQuaternion,self).__isub__(quaternion)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __div__(self,divisor):
		"""
		__div__(divisor)
			divisor=QtCore.qreal


		"""
		res = super(QQuaternion,self).__div__(divisor)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,divisor):
		"""
		__idiv__(divisor)
			divisor=QtCore.qreal

		Divides this quaternions components by the given divisor , and returns a reference to this quaternion.
		"""
		res = super(QQuaternion,self).__idiv__(divisor)
		isinstance(res,QtGui.QQuaternion)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,q2):
		"""
		__eq__(q2)
			q2=QtGui.QQuaternion


		"""
		res = super(QQuaternion,self).__eq__(q2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rotatedVector(self,vector):
		"""
		rotatedVector(vector)
			vector=QtGui.QVector3D

		Rotates vector with this quaternion to produce a new vector in 3D space
		The following code:
		is equivalent to the following:
		"""
		res = super(QQuaternion,self).rotatedVector(vector)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def setScalar(self,scalar):
		"""
		setScalar(scalar)
			scalar=QtCore.qreal

		Sets the scalar component of this quaternion to scalar .
		"""
		res = super(QQuaternion,self).setScalar(scalar)
		return res
	#----------------------------------------------------------------------
	def setVector(self,*args,**kwargs):
		"""
		setVector(vector)
			vector=QtGui.QVector3D

		setVector(x,y,z)
			x=QtCore.qreal
			y=QtCore.qreal
			z=QtCore.qreal

		Sets the vector component of this quaternion to vector .
		"""
		res = super(QQuaternion,self).setVector(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of this quaternions vector to the given x coordinate.
		"""
		res = super(QQuaternion,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of this quaternions vector to the given y coordinate.
		"""
		res = super(QQuaternion,self).setY(y)
		return res
	#----------------------------------------------------------------------
	def setZ(self,z):
		"""
		setZ(z)
			z=QtCore.qreal

		Sets the z coordinate of this quaternions vector to the given z coordinate.
		"""
		res = super(QQuaternion,self).setZ(z)
		return res
