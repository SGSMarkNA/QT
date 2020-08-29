from PySide import QtGui, QtCore

class QSize(QtCore.QSize):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSize,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QSize,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QSize,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height.
		"""
		res = super(QSize,self).height()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if either of the width and height is less than or equal to 0; otherwise returns false.
		"""
		res = super(QSize,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if both the width and height is 0; otherwise returns false.
		"""
		res = super(QSize,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if both the width and height is equal to or greater than 0; otherwise returns false.
		"""
		res = super(QSize,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QSize,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def transpose(self):
		"""
		Swaps the width and height values.
		"""
		res = super(QSize,self).transpose()
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width.
		"""
		res = super(QSize,self).width()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def boundedTo(self,arg__1):
		"""
		boundedTo(arg__1)
			arg__1=QtCore.QSize

		Returns a size holding the minimum width and height of this size and the given otherSize .
		"""
		res = super(QSize,self).boundedTo(arg__1)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def expandedTo(self,arg__1):
		"""
		expandedTo(arg__1)
			arg__1=QtCore.QSize

		Returns a size holding the maximum width and height of this size and the given otherSize .
		"""
		res = super(QSize,self).expandedTo(arg__1)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,s2):
		"""
		__ne__(s2)
			s2=QtCore.QSize


		"""
		res = super(QSize,self).__ne__(s2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(c)
			c=QtCore.qreal

		__mul__(c)
			c=QtCore.qreal


		"""
		res = super(QSize,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,c):
		"""
		__imul__(c)
			c=QtCore.qreal

		This is an overloaded function.
		Multiplies both the width and height by the given factor , and returns a reference to the size.
		Note that the result is rounded to the nearest integer.
		"""
		res = super(QSize,self).__imul__(c)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __add__(self,s2):
		"""
		__add__(s2)
			s2=QtCore.QSize


		"""
		res = super(QSize,self).__add__(s2)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,arg__1):
		"""
		__iadd__(arg__1)
			arg__1=QtCore.QSize

		Adds the given size to this size, and returns a reference to this size
		For example:
		"""
		res = super(QSize,self).__iadd__(arg__1)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,s2):
		"""
		__sub__(s2)
			s2=QtCore.QSize


		"""
		res = super(QSize,self).__sub__(s2)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,arg__1):
		"""
		__isub__(arg__1)
			arg__1=QtCore.QSize

		Subtracts the given size from this size, and returns a reference to this size
		For example:
		"""
		res = super(QSize,self).__isub__(arg__1)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __div__(self,c):
		"""
		__div__(c)
			c=QtCore.qreal


		"""
		res = super(QSize,self).__div__(c)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,c):
		"""
		__idiv__(c)
			c=QtCore.qreal

		This is an overloaded function.
		Divides both the width and height by the given divisor , and returns a reference to the size.
		Note that the result is rounded to the nearest integer.
		"""
		res = super(QSize,self).__idiv__(c)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,s2):
		"""
		__eq__(s2)
			s2=QtCore.QSize


		"""
		res = super(QSize,self).__eq__(s2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def scale(self,*args,**kwargs):
		"""
		scale(s,mode)
			s=QtCore.QSize
			mode=QtCore.Qt.AspectRatioMode

		scale(w,h,mode)
			w=QtCore.int
			h=QtCore.int
			mode=QtCore.Qt.AspectRatioMode


		"""
		res = super(QSize,self).scale(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,h):
		"""
		setHeight(h)
			h=QtCore.int

		Sets the height to the given height .
		"""
		res = super(QSize,self).setHeight(h)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,w):
		"""
		setWidth(w)
			w=QtCore.int

		Sets the width to the given width .
		"""
		res = super(QSize,self).setWidth(w)
		return res
