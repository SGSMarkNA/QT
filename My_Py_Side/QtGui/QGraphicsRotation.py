from PySide import QtGui, QtCore

class QGraphicsRotation(QtGui.QGraphicsRotation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsRotation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def angle(self):
		"""
		This property holds the angle for clockwise rotation, in degrees..
		The angle can be any real number; the default value is 0.0
		A value of 180 will rotate 180 degrees, clockwise
		If you provide a negative number, the item will be rotated counter-clockwise
		Normally the rotation angle will be in the range (-360, 360), but you can also provide numbers outside of this range (e.g., a angle of 370 degrees gives the same result as 10 degrees).
		"""
		res = super(QGraphicsRotation,self).angle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def angleChanged(self):
		"""

		"""
		res = super(QGraphicsRotation,self).angleChanged()
		return res
	#----------------------------------------------------------------------
	def axis(self):
		"""
		This property holds a rotation axis, specified by a vector in 3D space..
		This can be any axis in 3D space
		By default the axis is (0, 0, 1), which is aligned with the Z axis
		If you provide another axis, PySide.QtGui.QGraphicsRotation will provide a transformation that rotates around this axis
		For example, if you would like to rotate an item around its X axis, you could pass (1, 0, 0) as the axis.
		"""
		res = super(QGraphicsRotation,self).axis()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def axisChanged(self):
		"""

		"""
		res = super(QGraphicsRotation,self).axisChanged()
		return res
	#----------------------------------------------------------------------
	def origin(self):
		"""
		This property holds the origin of the rotation in 3D space..
		All rotations will be done relative to this point (i.e., this point will stay fixed, relative to the parent, when the item is rotated).
		"""
		res = super(QGraphicsRotation,self).origin()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def originChanged(self):
		"""

		"""
		res = super(QGraphicsRotation,self).originChanged()
		return res
	#----------------------------------------------------------------------
	def setAngle(self,arg__1):
		"""
		setAngle(arg__1)
			arg__1=QtCore.qreal

		This property holds the angle for clockwise rotation, in degrees..
		The angle can be any real number; the default value is 0.0
		A value of 180 will rotate 180 degrees, clockwise
		If you provide a negative number, the item will be rotated counter-clockwise
		Normally the rotation angle will be in the range (-360, 360), but you can also provide numbers outside of this range (e.g., a angle of 370 degrees gives the same result as 10 degrees).
		"""
		res = super(QGraphicsRotation,self).setAngle(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAxis(self,*args,**kwargs):
		"""
		setAxis(axis)
			axis=QtCore.Qt.Axis

		setAxis(axis)
			axis=QtGui.QVector3D


		"""
		res = super(QGraphicsRotation,self).setAxis(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setOrigin(self,point):
		"""
		setOrigin(point)
			point=QtGui.QVector3D

		This property holds the origin of the rotation in 3D space..
		All rotations will be done relative to this point (i.e., this point will stay fixed, relative to the parent, when the item is rotated).
		"""
		res = super(QGraphicsRotation,self).setOrigin(point)
		return res
