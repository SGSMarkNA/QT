from PySide import QtGui, QtCore

class QSizeF(QtCore.QSizeF):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSizeF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QSizeF,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QSizeF,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height.
		"""
		res = super(QSizeF,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if either of the width and height is less than or equal to 0; otherwise returns false.
		"""
		res = super(QSizeF,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if both the width and height are +0.0; otherwise returns false.
		"""
		res = super(QSizeF,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if both the width and height is equal to or greater than 0; otherwise returns false.
		"""
		res = super(QSizeF,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toSize(self):
		"""
		Returns an integer based copy of this size.
		Note that the coordinates in the returned size will be rounded to the nearest integer.
		"""
		res = super(QSizeF,self).toSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QSizeF,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def transpose(self):
		"""
		Swaps the width and height values.
		"""
		res = super(QSizeF,self).transpose()
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width.
		"""
		res = super(QSizeF,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def boundedTo(self,arg__1):
		"""
		boundedTo(arg__1)
			arg__1=QtCore.QSizeF

		Returns a size holding the minimum width and height of this size and the given otherSize .
		"""
		res = super(QSizeF,self).boundedTo(arg__1)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def expandedTo(self,arg__1):
		"""
		expandedTo(arg__1)
			arg__1=QtCore.QSizeF

		Returns a size holding the maximum width and height of this size and the given otherSize .
		"""
		res = super(QSizeF,self).expandedTo(arg__1)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,s2):
		"""
		__ne__(s2)
			s2=QtCore.QSizeF


		"""
		res = super(QSizeF,self).__ne__(s2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(c)
			c=QtCore.qreal

		__mul__(c)
			c=QtCore.qreal


		"""
		res = super(QSizeF,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,c):
		"""
		__imul__(c)
			c=QtCore.qreal

		This is an overloaded function.
		Multiplies both the width and height by the given factor and returns a reference to the size.
		"""
		res = super(QSizeF,self).__imul__(c)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __add__(self,s2):
		"""
		__add__(s2)
			s2=QtCore.QSizeF


		"""
		res = super(QSizeF,self).__add__(s2)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,arg__1):
		"""
		__iadd__(arg__1)
			arg__1=QtCore.QSizeF

		Adds the given size to this size and returns a reference to this size
		For example:
		"""
		res = super(QSizeF,self).__iadd__(arg__1)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,s2):
		"""
		__sub__(s2)
			s2=QtCore.QSizeF


		"""
		res = super(QSizeF,self).__sub__(s2)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,arg__1):
		"""
		__isub__(arg__1)
			arg__1=QtCore.QSizeF

		Subtracts the given size from this size and returns a reference to this size
		For example:
		"""
		res = super(QSizeF,self).__isub__(arg__1)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __div__(self,c):
		"""
		__div__(c)
			c=QtCore.qreal


		"""
		res = super(QSizeF,self).__div__(c)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,c):
		"""
		__idiv__(c)
			c=QtCore.qreal

		This is an overloaded function.
		Divides both the width and height by the given divisor and returns a reference to the size.
		"""
		res = super(QSizeF,self).__idiv__(c)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,s2):
		"""
		__eq__(s2)
			s2=QtCore.QSizeF


		"""
		res = super(QSizeF,self).__eq__(s2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def scale(self,*args,**kwargs):
		"""
		scale(w,h,mode)
			w=QtCore.qreal
			h=QtCore.qreal
			mode=QtCore.Qt.AspectRatioMode

		scale(s,mode)
			s=QtCore.QSizeF
			mode=QtCore.Qt.AspectRatioMode


		"""
		res = super(QSizeF,self).scale(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,h):
		"""
		setHeight(h)
			h=QtCore.qreal

		Sets the height to the given height .
		"""
		res = super(QSizeF,self).setHeight(h)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,w):
		"""
		setWidth(w)
			w=QtCore.qreal

		Sets the width to the given width .
		"""
		res = super(QSizeF,self).setWidth(w)
		return res
