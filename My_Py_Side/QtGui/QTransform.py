from PySide import QtGui, QtCore

class QTransform(QtGui.QTransform):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTransform,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QTransform,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QTransform,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def adjoint(self):
		"""
		Returns the adjoint of this matrix.
		"""
		res = super(QTransform,self).adjoint()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def det(self):
		"""
		Returns the matrixs determinant
		Use PySide.QtGui.QTransform.determinant() instead.
		"""
		res = super(QTransform,self).det()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def determinant(self):
		"""
		Returns the matrixs determinant.
		"""
		res = super(QTransform,self).determinant()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dx(self):
		"""
		Returns the horizontal translation factor.
		"""
		res = super(QTransform,self).dx()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dy(self):
		"""
		Returns the vertical translation factor.
		"""
		res = super(QTransform,self).dy()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def inline_type(self):
		"""

		"""
		res = super(QTransform,self).inline_type()
		isinstance(res,QtGui.QTransform.TransformationType)
		return res
	#----------------------------------------------------------------------
	def inverted(self):
		"""
		Returns an inverted copy of this matrix.
		If the matrix is singular (not invertible), the returned matrix is the identity matrix
		If invertible is valid (i.e
		not 0), its value is set to true if the matrix is invertible, otherwise it is set to false.
		"""
		res = super(QTransform,self).inverted()
		return res
	#----------------------------------------------------------------------
	def isAffine(self):
		"""
		Returns true if the matrix represent an affine transformation, otherwise returns false.
		"""
		res = super(QTransform,self).isAffine()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isIdentity(self):
		"""
		Returns true if the matrix is the identity matrix, otherwise returns false.
		"""
		res = super(QTransform,self).isIdentity()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isInvertible(self):
		"""
		Returns true if the matrix is invertible, otherwise returns false.
		"""
		res = super(QTransform,self).isInvertible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isRotating(self):
		"""
		Returns true if the matrix represents some kind of a rotating transformation, otherwise returns false.
		"""
		res = super(QTransform,self).isRotating()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isScaling(self):
		"""
		Returns true if the matrix represents a scaling transformation, otherwise returns false.
		"""
		res = super(QTransform,self).isScaling()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTranslating(self):
		"""
		Returns true if the matrix represents a translating transformation, otherwise returns false.
		"""
		res = super(QTransform,self).isTranslating()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def m11(self):
		"""
		Returns the horizontal scaling factor.
		"""
		res = super(QTransform,self).m11()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m12(self):
		"""
		Returns the vertical shearing factor.
		"""
		res = super(QTransform,self).m12()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m13(self):
		"""
		Returns the horizontal projection factor.
		"""
		res = super(QTransform,self).m13()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m21(self):
		"""
		Returns the horizontal shearing factor.
		"""
		res = super(QTransform,self).m21()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m22(self):
		"""
		Returns the vertical scaling factor.
		"""
		res = super(QTransform,self).m22()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m23(self):
		"""
		Returns the vertical projection factor.
		"""
		res = super(QTransform,self).m23()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m31(self):
		"""
		Returns the horizontal translation factor.
		"""
		res = super(QTransform,self).m31()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m32(self):
		"""
		Returns the vertical translation factor.
		"""
		res = super(QTransform,self).m32()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def m33(self):
		"""
		Returns the division factor.
		"""
		res = super(QTransform,self).m33()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the matrix to an identity matrix, i.e
		all elements are set to zero, except m11 and m22 (specifying the scale) and m33 which are set to 1.
		"""
		res = super(QTransform,self).reset()
		return res
	#----------------------------------------------------------------------
	def toAffine(self):
		"""
		Returns the PySide.QtGui.QTransform as an affine matrix.
		"""
		res = super(QTransform,self).toAffine()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def transposed(self):
		"""
		Returns the transpose of this matrix.
		"""
		res = super(QTransform,self).transposed()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the transformation type of this matrix.
		The transformation type is the highest enumeration value capturing all of the matrixs transformations
		For example, if the matrix both scales and shears, the type would be TxShear , because TxShear has a higher enumeration value than TxScale .
		Knowing the transformation type of a matrix is useful for optimization: you can often handle specific types more optimally than handling the generic case.
		"""
		res = super(QTransform,self).type()
		isinstance(res,QtGui.QTransform.TransformationType)
		return res
	#----------------------------------------------------------------------
	def map(self,*args,**kwargs):
		"""
		map(r)
			r=QtGui.QRegion

		map(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		map(a)
			a=QtGui.QPolygon

		map(a)
			a=QtGui.QPolygonF

		map(l)
			l=QtCore.QLine

		map(l)
			l=QtCore.QLineF

		map(p)
			p=QtCore.QPointF

		map(p)
			p=QtGui.QPainterPath

		map(p)
			p=QtCore.QPoint

		This is an overloaded function.
		Creates and returns a PySide.QtGui.QRegion object that is a copy of the given region , mapped into the coordinate system defined by this matrix.
		Calling this method can be rather expensive if rotations or shearing are used.
		"""
		res = super(QTransform,self).map(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
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
		To retrieve the exact region the given rectangle maps to, use the PySide.QtGui.QTransform.mapToPolygon() function instead.
		"""
		res = super(QTransform,self).mapRect(*args,**kwargs)
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
		res = super(QTransform,self).mapToPolygon(r)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QTransform

		Returns true if this matrix is not equal to the given matrix , otherwise returns false.
		"""
		res = super(QTransform,self).__ne__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(n)
			n=QtCore.qreal

		__mul__(o)
			o=QtGui.QTransform


		"""
		res = super(QTransform,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,*args,**kwargs):
		"""
		__imul__(div)
			div=QtCore.qreal

		__imul__(arg__1)
			arg__1=QtGui.QTransform

		This is an overloaded function.
		Returns the result of performing an element-wise multiplication of this matrix with the given scalar .
		"""
		res = super(QTransform,self).__imul__(*args,**kwargs)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __add__(self,n):
		"""
		__add__(n)
			n=QtCore.qreal


		"""
		res = super(QTransform,self).__add__(n)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,div):
		"""
		__iadd__(div)
			div=QtCore.qreal

		This is an overloaded function.
		Returns the matrix obtained by adding the given scalar to each element of this matrix.
		"""
		res = super(QTransform,self).__iadd__(div)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,n):
		"""
		__sub__(n)
			n=QtCore.qreal


		"""
		res = super(QTransform,self).__sub__(n)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,div):
		"""
		__isub__(div)
			div=QtCore.qreal

		This is an overloaded function.
		Returns the matrix obtained by subtracting the given scalar from each element of this matrix.
		"""
		res = super(QTransform,self).__isub__(div)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __div__(self,n):
		"""
		__div__(n)
			n=QtCore.qreal


		"""
		res = super(QTransform,self).__div__(n)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,div):
		"""
		__idiv__(div)
			div=QtCore.qreal

		This is an overloaded function.
		Returns the result of performing an element-wise division of this matrix by the given scalar .
		"""
		res = super(QTransform,self).__idiv__(div)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QTransform

		Returns true if this matrix is equal to the given matrix , otherwise returns false.
		"""
		res = super(QTransform,self).__eq__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def quadToQuad(self,arg__1,arg__2):
		"""
		quadToQuad(arg__1,arg__2)
			arg__1=QtGui.QPolygonF
			arg__2=QtGui.QPolygonF


		"""
		res = super(QTransform,self).quadToQuad(arg__1,arg__2)
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def quadToSquare(self,arg__1):
		"""
		quadToSquare(arg__1)
			arg__1=QtGui.QPolygonF


		"""
		res = super(QTransform,self).quadToSquare(arg__1)
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def rotate(self,a,axis=None):
		"""
		rotate(a,axis=None)
			a=QtCore.qreal
			axis=QtCore.Qt.Axis


		"""
		res = super(QTransform,self).rotate(a,axis)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def rotateRadians(self,a,axis=None):
		"""
		rotateRadians(a,axis=None)
			a=QtCore.qreal
			axis=QtCore.Qt.Axis


		"""
		res = super(QTransform,self).rotateRadians(a,axis)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def scale(self,sx,sy):
		"""
		scale(sx,sy)
			sx=QtCore.qreal
			sy=QtCore.qreal

		Scales the coordinate system by sx horizontally and sy vertically, and returns a reference to the matrix.
		"""
		res = super(QTransform,self).scale(sx,sy)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def setMatrix(self,m11,m12,m13,m21,m22,m23,m31,m32,m33):
		"""
		setMatrix(m11,m12,m13,m21,m22,m23,m31,m32,m33)
			m11=QtCore.qreal
			m12=QtCore.qreal
			m13=QtCore.qreal
			m21=QtCore.qreal
			m22=QtCore.qreal
			m23=QtCore.qreal
			m31=QtCore.qreal
			m32=QtCore.qreal
			m33=QtCore.qreal

		Sets the matrix elements to the specified values, m11 , m12 , m13m21 , m22 , m23m31 , m32 and m33
		Note that this function replaces the previous values
		PySide.QtGui.QTransform provides the PySide.QtGui.QTransform.translate() , PySide.QtGui.QTransform.rotate() , PySide.QtGui.QTransform.scale() and PySide.QtGui.QTransform.shear() convenience functions to manipulate the various matrix elements based on the currently defined coordinate system.
		"""
		res = super(QTransform,self).setMatrix(m11,m12,m13,m21,m22,m23,m31,m32,m33)
		return res
	#----------------------------------------------------------------------
	def shear(self,sh,sv):
		"""
		shear(sh,sv)
			sh=QtCore.qreal
			sv=QtCore.qreal

		Shears the coordinate system by sh horizontally and sv vertically, and returns a reference to the matrix.
		"""
		res = super(QTransform,self).shear(sh,sv)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def squareToQuad(self,arg__1):
		"""
		squareToQuad(arg__1)
			arg__1=QtGui.QPolygonF


		"""
		res = super(QTransform,self).squareToQuad(arg__1)
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def translate(self,dx,dy):
		"""
		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Moves the coordinate system dx along the x axis and dy along the y axis, and returns a reference to the matrix.
		"""
		res = super(QTransform,self).translate(dx,dy)
		isinstance(res,QtGui.QTransform)
		return res
