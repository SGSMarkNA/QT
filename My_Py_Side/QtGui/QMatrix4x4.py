from PySide import QtGui, QtCore

class QMatrix4x4(QtGui.QMatrix4x4):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMatrix4x4,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __mgetitem__(self):
		"""

		"""
		res = super(QMatrix4x4,self).__mgetitem__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QMatrix4x4,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QMatrix4x4,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def copyDataTo(self):
		"""
		Retrieves the 16 items in this matrix and copies them to values in row-major order.
		"""
		res = super(QMatrix4x4,self).copyDataTo()
		return res
	#----------------------------------------------------------------------
	def determinant(self):
		"""
		Returns the determinant of this matrix.
		"""
		res = super(QMatrix4x4,self).determinant()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def flipCoordinates(self):
		"""
		Flips between right-handed and left-handed coordinate systems by multiplying the y and z co-ordinates by -1
		This is normally used to create a left-handed orthographic view without scaling the viewport as PySide.QtGui.QMatrix4x4.ortho() does.
		"""
		res = super(QMatrix4x4,self).flipCoordinates()
		return res
	#----------------------------------------------------------------------
	def isIdentity(self):
		"""
		Returns true if this matrix is the identity; false otherwise.
		"""
		res = super(QMatrix4x4,self).isIdentity()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def normalMatrix(self):
		"""
		Returns the normal matrix corresponding to this 4x4 transformation
		The normal matrix is the transpose of the inverse of the top-left 3x3 part of this 4x4 matrix
		If the 3x3 sub-matrix is not invertible, this function returns the identity.
		"""
		res = super(QMatrix4x4,self).normalMatrix()
		isinstance(res,QtGui.QMatrix3x3)
		return res
	#----------------------------------------------------------------------
	def __sub__(self):
		"""

		"""
		res = super(QMatrix4x4,self).__sub__()
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def optimize(self):
		"""
		Optimize the usage of this matrix from its current elements.
		Some operations such as PySide.QtGui.QMatrix4x4.translate() , PySide.QtGui.QMatrix4x4.scale() , and PySide.QtGui.QMatrix4x4.rotate() can be performed more efficiently if the matrix being modified is already known to be the identity, a previous PySide.QtGui.QMatrix4x4.translate() , a previous PySide.QtGui.QMatrix4x4.scale() , etc.
		Normally the PySide.QtGui.QMatrix4x4 class keeps track of this special type internally as operations are performed
		However, if the matrix is modified directly with operator()() or PySide.QtGui.QMatrix4x4.data() , then PySide.QtGui.QMatrix4x4 will lose track of the special type and will revert to the safest but least efficient operations thereafter.
		By calling PySide.QtGui.QMatrix4x4.optimize() after directly modifying the matrix, the programmer can force PySide.QtGui.QMatrix4x4 to recover the special type if the elements appear to conform to one of the known optimized types.
		"""
		res = super(QMatrix4x4,self).optimize()
		return res
	#----------------------------------------------------------------------
	def orthonormalInverse(self):
		"""

		"""
		res = super(QMatrix4x4,self).orthonormalInverse()
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def setToIdentity(self):
		"""
		Sets this matrix to the identity.
		"""
		res = super(QMatrix4x4,self).setToIdentity()
		return res
	#----------------------------------------------------------------------
	def toAffine(self):
		"""
		Returns the conventional Qt 2D affine transformation matrix that corresponds to this matrix
		It is assumed that this matrix only contains 2D affine transformation elements.
		"""
		res = super(QMatrix4x4,self).toAffine()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def toTransform(self):
		"""
		Returns the conventional Qt 2D transformation matrix that corresponds to this matrix.
		The returned PySide.QtGui.QTransform is formed by simply dropping the third row and third column of the PySide.QtGui.QMatrix4x4
		This is suitable for implementing orthographic projections where the z co-ordinate should be dropped rather than projected.
		"""
		res = super(QMatrix4x4,self).toTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def transposed(self):
		"""
		Returns this matrix, transposed about its diagonal.
		"""
		res = super(QMatrix4x4,self).transposed()
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def column(self,index):
		"""
		column(index)
			index=QtCore.int

		Returns the elements of column index as a 4D vector.
		"""
		res = super(QMatrix4x4,self).column(index)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def fill(self,value):
		"""
		fill(value)
			value=QtCore.qreal

		Fills all elements of this matrx with value .
		"""
		res = super(QMatrix4x4,self).fill(value)
		return res
	#----------------------------------------------------------------------
	def frustum(self,left,right,bottom,top,nearPlane,farPlane):
		"""
		frustum(left,right,bottom,top,nearPlane,farPlane)
			left=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal
			top=QtCore.qreal
			nearPlane=QtCore.qreal
			farPlane=QtCore.qreal

		Multiplies this matrix by another that applies a perspective frustum projection for a window with lower-left corner (left , bottom ), upper-right corner (right , top ), and the specified nearPlane and farPlane clipping planes.
		"""
		res = super(QMatrix4x4,self).frustum(left,right,bottom,top,nearPlane,farPlane)
		return res
	#----------------------------------------------------------------------
	def inverted(self,invertible=None):
		"""
		inverted(invertible=None)
			invertible=QtCore.bool

		Returns the inverse of this matrix
		Returns the identity if this matrix cannot be inverted; i.e
		PySide.QtGui.QMatrix4x4.determinant() is zero
		If invertible is not null, then true will be written to that location if the matrix can be inverted; false otherwise.
		If the matrix is recognized as the identity or an orthonormal matrix, then this function will quickly invert the matrix using optimized routines.
		"""
		res = super(QMatrix4x4,self).inverted(invertible)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def lookAt(self,eye,center,up):
		"""
		lookAt(eye,center,up)
			eye=QtGui.QVector3D
			center=QtGui.QVector3D
			up=QtGui.QVector3D

		Multiplies this matrix by another that applies an eye position transformation
		The center value indicates the center of the view that the eye is looking at
		The up value indicates which direction should be considered up with respect to the eye .
		"""
		res = super(QMatrix4x4,self).lookAt(eye,center,up)
		return res
	#----------------------------------------------------------------------
	def map(self,*args,**kwargs):
		"""
		map(point)
			point=QtGui.QVector4D

		map(point)
			point=QtGui.QVector3D

		map(point)
			point=QtCore.QPoint

		map(point)
			point=QtCore.QPointF

		Maps point by multiplying this matrix by point .
		"""
		res = super(QMatrix4x4,self).map(*args,**kwargs)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def mapRect(self,*args,**kwargs):
		"""
		mapRect(rect)
			rect=QtCore.QRectF

		mapRect(rect)
			rect=QtCore.QRect

		Maps rect by multiplying this matrix by the corners of rect and then forming a new rectangle from the results
		The returned rectangle will be an ordinary 2D rectangle with sides parallel to the horizontal and vertical axes.
		"""
		res = super(QMatrix4x4,self).mapRect(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapVector(self,vector):
		"""
		mapVector(vector)
			vector=QtGui.QVector3D

		Maps vector by multiplying the top 3x3 portion of this matrix by vector
		The translation and projection components of this matrix are ignored.
		"""
		res = super(QMatrix4x4,self).mapVector(vector)
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QMatrix4x4

		Returns true if this matrix is not identical to other ; false otherwise
		This operator uses an exact floating-point comparison.
		"""
		res = super(QMatrix4x4,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(factor)
			factor=QtCore.qreal

		__mul__(factor)
			factor=QtCore.qreal

		__mul__(m2)
			m2=QtGui.QMatrix4x4


		"""
		res = super(QMatrix4x4,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(factor)
			factor=QtCore.qreal

		__imul__(other)
			other=QtGui.QMatrix4x4

		This is an overloaded function.
		Multiplies all elements of this matrix by factor .
		"""
		res = super(QMatrix4x4,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __add__(self,m2):
		"""
		__add__(m2)
			m2=QtGui.QMatrix4x4


		"""
		res = super(QMatrix4x4,self).__add__(m2)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,other):
		"""
		__iadd__(other)
			other=QtGui.QMatrix4x4

		Adds the contents of other to this matrix.
		"""
		res = super(QMatrix4x4,self).__iadd__(other)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,m2):
		"""
		__sub__(m2)
			m2=QtGui.QMatrix4x4


		"""
		res = super(QMatrix4x4,self).__sub__(m2)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,other):
		"""
		__isub__(other)
			other=QtGui.QMatrix4x4

		Subtracts the contents of other from this matrix.
		"""
		res = super(QMatrix4x4,self).__isub__(other)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __div__(self,divisor):
		"""
		__div__(divisor)
			divisor=QtCore.qreal


		"""
		res = super(QMatrix4x4,self).__div__(divisor)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,divisor):
		"""
		__idiv__(divisor)
			divisor=QtCore.qreal

		This is an overloaded function.
		Divides all elements of this matrix by divisor .
		"""
		res = super(QMatrix4x4,self).__idiv__(divisor)
		isinstance(res,QtGui.QMatrix4x4)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QMatrix4x4

		Returns true if this matrix is identical to other ; false otherwise
		This operator uses an exact floating-point comparison.
		"""
		res = super(QMatrix4x4,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def ortho(self,*args,**kwargs):
		"""
		ortho(rect)
			rect=QtCore.QRectF

		ortho(left,right,bottom,top,nearPlane,farPlane)
			left=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal
			top=QtCore.qreal
			nearPlane=QtCore.qreal
			farPlane=QtCore.qreal

		ortho(rect)
			rect=QtCore.QRect

		This is an overloaded function.
		Multiplies this matrix by another that applies an orthographic projection for a window with boundaries specified by rect
		The near and far clipping planes will be -1 and 1 respectively.
		"""
		res = super(QMatrix4x4,self).ortho(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def perspective(self,angle,aspect,nearPlane,farPlane):
		"""
		perspective(angle,aspect,nearPlane,farPlane)
			angle=QtCore.qreal
			aspect=QtCore.qreal
			nearPlane=QtCore.qreal
			farPlane=QtCore.qreal

		Multiplies this matrix by another that applies a perspective projection
		The field of view will be angle degrees within a window with a given aspect ratio
		The projection will have the specified nearPlane and farPlane clipping planes.
		"""
		res = super(QMatrix4x4,self).perspective(angle,aspect,nearPlane,farPlane)
		return res
	#----------------------------------------------------------------------
	def projectedRotate(self,angle,x,y,z):
		"""
		projectedRotate(angle,x,y,z)
			angle=QtCore.qreal
			x=QtCore.qreal
			y=QtCore.qreal
			z=QtCore.qreal


		"""
		res = super(QMatrix4x4,self).projectedRotate(angle,x,y,z)
		return res
	#----------------------------------------------------------------------
	def rotate(self,*args,**kwargs):
		"""
		rotate(angle,x,y,z=None)
			angle=QtCore.qreal
			x=QtCore.qreal
			y=QtCore.qreal
			z=QtCore.qreal

		rotate(quaternion)
			quaternion=QtGui.QQuaternion

		rotate(angle,vector)
			angle=QtCore.qreal
			vector=QtGui.QVector3D

		This is an overloaded function.
		Multiplies this matrix by another that rotates coordinates through angle degrees about the vector (x , y , z ).
		"""
		res = super(QMatrix4x4,self).rotate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def row(self,index):
		"""
		row(index)
			index=QtCore.int

		Returns the elements of row index as a 4D vector.
		"""
		res = super(QMatrix4x4,self).row(index)
		isinstance(res,QtGui.QVector4D)
		return res
	#----------------------------------------------------------------------
	def scale(self,*args,**kwargs):
		"""
		scale(x,y,z)
			x=QtCore.qreal
			y=QtCore.qreal
			z=QtCore.qreal

		scale(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		scale(factor)
			factor=QtCore.qreal

		scale(vector)
			vector=QtGui.QVector3D

		This is an overloaded function.
		Multiplies this matrix by another that scales coordinates by the components x , y , and z .
		"""
		res = super(QMatrix4x4,self).scale(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setColumn(self,index,value):
		"""
		setColumn(index,value)
			index=QtCore.int
			value=QtGui.QVector4D

		Sets the elements of column index to the components of value .
		"""
		res = super(QMatrix4x4,self).setColumn(index,value)
		return res
	#----------------------------------------------------------------------
	def setRow(self,index,value):
		"""
		setRow(index,value)
			index=QtCore.int
			value=QtGui.QVector4D

		Sets the elements of row index to the components of value .
		"""
		res = super(QMatrix4x4,self).setRow(index,value)
		return res
	#----------------------------------------------------------------------
	def toTransform(self,distanceToPlane):
		"""
		toTransform(distanceToPlane)
			distanceToPlane=QtCore.qreal

		Returns the conventional Qt 2D transformation matrix that corresponds to this matrix.
		If distanceToPlane is non-zero, it indicates a projection factor to use to adjust for the z co-ordinate
		The value of 1024 corresponds to the projection factor used by QTransform.rotate() for the x and y axes.
		If distanceToPlane is zero, then the returned PySide.QtGui.QTransform is formed by simply dropping the third row and third column of the PySide.QtGui.QMatrix4x4
		This is suitable for implementing orthographic projections where the z co-ordinate should be dropped rather than projected.
		"""
		res = super(QMatrix4x4,self).toTransform(distanceToPlane)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(x,y,z)
			x=QtCore.qreal
			y=QtCore.qreal
			z=QtCore.qreal

		translate(vector)
			vector=QtGui.QVector3D

		translate(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		This is an overloaded function.
		Multiplies this matrix by another that translates coordinates by the components x , y , and z .
		"""
		res = super(QMatrix4x4,self).translate(*args,**kwargs)
		return res
