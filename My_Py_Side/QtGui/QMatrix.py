from PySide import QtGui, QtCore

class QMatrix(QtGui.QMatrix):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMatrix,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QMatrix,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QMatrix,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def det(self):
		"""
		Returns the matrixs determinant.
		"""
		res = super(QMatrix,self).det()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def determinant(self):
		"""
		Returns the matrixs determinant.
		"""
		res = super(QMatrix,self).determinant()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dx(self):
		"""
		Returns the horizontal translation factor.
		"""
		res = super(QMatrix,self).dx()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dy(self):
		"""
		Returns the vertical translation factor.
		"""
		res = super(QMatrix,self).dy()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def inverted(self):
		"""
		Returns an inverted copy of this matrix.
		If the matrix is singular (not invertible), the returned matrix is the identity matrix
		If invertible is valid (i.e
		not 0), its value is set to true if the matrix is invertible, otherwise it is set to false.
		"""
		res = super(QMatrix,self).inverted()
		return res
	#----------------------------------------------------------------------
	def isIdentity(self):
		"""
		Returns true if the matrix is the identity matrix, otherwise returns false.
		"""
		res = super(QMatrix,self).isIdentity()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isInvertible(self):
		"""
		Returns true if the matrix is invertible, otherwise returns false.
		"""
		res = super(QMatrix,self).isInvertible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def m11(self):
		"""
		Returns the horizontal scaling factor.
		"""
		res = super(QMatrix,self).m11()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m12(self):
		"""
		Returns the vertical shearing factor.
		"""
		res = super(QMatrix,self).m12()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m21(self):
		"""
		Returns the horizontal shearing factor.
		"""
		res = super(QMatrix,self).m21()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m22(self):
		"""
		Returns the vertical scaling factor.
		"""
		res = super(QMatrix,self).m22()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the matrix to an identity matrix, i.e
		all elements are set to zero, except m11 and m22 (specifying the scale) which are set to 1.
		"""
		res = super(QMatrix,self).reset()
		return res
	#----------------------------------------------------------------------
	def map(self,*args,**kwargs):
		"""
		map(a)
			a=QtGui.QPolygonF

		map(r)
			r=QtGui.QRegion

		map(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		map(a)
			a=QtGui.QPolygon

		map(x,y)
			x=QtCore.int
			y=QtCore.int

		map(p)
			p=QtCore.QPointF

		map(l)
			l=QtCore.QLine

		map(l)
			l=QtCore.QLineF

		map(p)
			p=QtGui.QPainterPath

		map(p)
			p=QtCore.QPoint

		This is an overloaded function.
		Creates and returns a PySide.QtGui.QPolygonF object that is a copy of the given polygon , mapped into the coordinate system defined by this matrix.
		"""
		res = super(QMatrix,self).map(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def mapRect(self,*args,**kwargs):
		"""
		mapRect(arg__1)
			arg__1=QtCore.QRectF

		mapRect(arg__1)
			arg__1=QtCore.QRect

		Creates and returns a PySide.QtCore.QRectF object that is a copy of the given rectangle , mapped into the coordinate system defined by this matrix.
		The rectangles coordinates are transformed using the following formulas:
		If rotation or shearing has been specified, this function returns the bounding rectangle
		To retrieve the exact region the given rectangle maps to, use the PySide.QtGui.QMatrix.mapToPolygon() function instead.
		"""
		res = super(QMatrix,self).mapRect(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapToPolygon(self,r):
		"""
		mapToPolygon(r)
			r=QtCore.QRect

		Creates and returns a PySide.QtGui.QPolygon representation of the given rectangle , mapped into the coordinate system defined by this matrix.
		The rectangles coordinates are transformed using the following formulas:
		Polygons and rectangles behave slightly differently when transformed (due to integer rounding), so matrix.map(QPolygon(rectangle)) is not always the same as matrix.mapToPolygon(rectangle) .
		"""
		res = super(QMatrix,self).mapToPolygon(r)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QMatrix

		Returns true if this matrix is not equal to the given matrix , otherwise returns false.
		"""
		res = super(QMatrix,self).__ne__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,o):
		"""
		__mul__(o)
			o=QtGui.QMatrix

		Returns the result of multiplying this matrix by the given matrix .
		Note that matrix multiplication is not commutative, i.e
		a*b != b*a.
		"""
		res = super(QMatrix,self).__mul__(o)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,arg__1):
		"""
		__imul__(arg__1)
			arg__1=QtGui.QMatrix

		This is an overloaded function.
		Returns the result of multiplying this matrix by the given matrix .
		"""
		res = super(QMatrix,self).__imul__(arg__1)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QMatrix

		Returns true if this matrix is equal to the given matrix , otherwise returns false.
		"""
		res = super(QMatrix,self).__eq__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rotate(self,a):
		"""
		rotate(a)
			a=QtCore.qreal

		Rotates the coordinate system the given degrees counterclockwise.
		Note that if you apply a PySide.QtGui.QMatrix to a point defined in widget coordinates, the direction of the rotation will be clockwise because the y-axis points downwards.
		Returns a reference to the matrix.
		"""
		res = super(QMatrix,self).rotate(a)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def scale(self,sx,sy):
		"""
		scale(sx,sy)
			sx=QtCore.qreal
			sy=QtCore.qreal

		Scales the coordinate system by sx horizontally and sy vertically, and returns a reference to the matrix.
		"""
		res = super(QMatrix,self).scale(sx,sy)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def setMatrix(self,m11,m12,m21,m22,dx,dy):
		"""
		setMatrix(m11,m12,m21,m22,dx,dy)
			m11=QtCore.qreal
			m12=QtCore.qreal
			m21=QtCore.qreal
			m22=QtCore.qreal
			dx=QtCore.qreal
			dy=QtCore.qreal

		Sets the matrix elements to the specified values, m11 , m12 , m21 , m22 , dx and dy .
		Note that this function replaces the previous values
		PySide.QtGui.QMatrix provide the PySide.QtGui.QMatrix.translate() , PySide.QtGui.QMatrix.rotate() , PySide.QtGui.QMatrix.scale() and PySide.QtGui.QMatrix.shear() convenience functions to manipulate the various matrix elements based on the currently defined coordinate system.
		"""
		res = super(QMatrix,self).setMatrix(m11,m12,m21,m22,dx,dy)
		return res
	#----------------------------------------------------------------------
	def shear(self,sh,sv):
		"""
		shear(sh,sv)
			sh=QtCore.qreal
			sv=QtCore.qreal

		Shears the coordinate system by sh horizontally and sv vertically, and returns a reference to the matrix.
		"""
		res = super(QMatrix,self).shear(sh,sv)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def translate(self,dx,dy):
		"""
		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Moves the coordinate system dx along the x axis and dy along the y axis, and returns a reference to the matrix.
		"""
		res = super(QMatrix,self).translate(dx,dy)
		isinstance(res,QtGui.QMatrix)
		return res
