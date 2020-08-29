from PySide import QtGui, QtCore

class QRegion(QtGui.QRegion):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRegion,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the bounding rectangle of this region
		An empty region gives a rectangle that is QRect.isNull() .
		"""
		res = super(QRegion,self).boundingRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def copy(self):
		"""

		"""
		res = super(QRegion,self).copy()
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the region is empty; otherwise returns false
		An empty region is a region that contains no points.
		Example:
		"""
		res = super(QRegion,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def numRects(self):
		"""
		Returns the number of rectangles that will be returned in PySide.QtGui.QRegion.rects() .
		"""
		res = super(QRegion,self).numRects()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rectCount(self):
		"""
		Returns the number of rectangles that will be returned in PySide.QtGui.QRegion.rects() .
		"""
		res = super(QRegion,self).rectCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rects(self):
		"""
		Returns an array of non-overlapping rectangles that make up the region.
		The union of all the rectangles is equal to the original region.
		"""
		res = super(QRegion,self).rects()
		return res
	#----------------------------------------------------------------------
	def updateX11Region(self):
		"""

		"""
		res = super(QRegion,self).updateX11Region()
		return res
	#----------------------------------------------------------------------
	def clipRectangles(self,num):
		"""
		clipRectangles(num)
			num=QtCore.int


		"""
		res = super(QRegion,self).clipRectangles(num)
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def contains(self,*args,**kwargs):
		"""
		contains(p)
			p=QtCore.QPoint

		contains(r)
			r=QtCore.QRect

		Returns true if the region contains the point p ; otherwise returns false.
		"""
		res = super(QRegion,self).contains(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def exec(self,ba,ver=None,byteOrder=None):
		"""
		exec(ba,ver=None,byteOrder=None)
			ba=QtCore.QByteArray
			ver=QtCore.int
			byteOrder=QtCore.QDataStream.ByteOrder


		"""
		res = super(QRegion,self).exec(ba,ver,byteOrder)
		return res
	#----------------------------------------------------------------------
	def intersected(self,*args,**kwargs):
		"""
		intersected(r)
			r=QtCore.QRect

		intersected(r)
			r=QtGui.QRegion

		Returns a region which is the intersection of this region and the given rect .
		"""
		res = super(QRegion,self).intersected(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def intersects(self,*args,**kwargs):
		"""
		intersects(r)
			r=QtGui.QRegion

		intersects(r)
			r=QtCore.QRect

		Returns true if this region intersects with region , otherwise returns false.
		"""
		res = super(QRegion,self).intersects(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,r):
		"""
		__ne__(r)
			r=QtGui.QRegion

		Returns true if this region is different from the other region; otherwise returns false.
		"""
		res = super(QRegion,self).__ne__(r)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __and__(self,*args,**kwargs):
		"""
		__and__(r)
			r=QtGui.QRegion

		__and__(r)
			r=QtCore.QRect

		Applies the PySide.QtGui.QRegion.intersected() function to this region and r
		r1&r2 is equivalent to r1.intersected(r2) .
		"""
		res = super(QRegion,self).__and__(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(m)
			m=QtGui.QTransform

		__mul__(m)
			m=QtGui.QMatrix


		"""
		res = super(QRegion,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __add__(self,*args,**kwargs):
		"""
		__add__(r)
			r=QtGui.QRegion

		__add__(r)
			r=QtCore.QRect

		Applies the PySide.QtGui.QRegion.united() function to this region and r
		r1+r2 is equivalent to r1.united(r2) .
		"""
		res = super(QRegion,self).__add__(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(r)
			r=QtGui.QRegion

		__iadd__(r)
			r=QtCore.QRect

		Applies the PySide.QtGui.QRegion.united() function to this region and r and assigns the result to this region
		r1+=r2 is equivalent to r1 = r1.united(r2) .
		"""
		res = super(QRegion,self).__iadd__(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __sub__(self,r):
		"""
		__sub__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.subtracted() function to this region and r
		r1-r2 is equivalent to r1.subtracted(r2) .
		"""
		res = super(QRegion,self).__sub__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,r):
		"""
		__isub__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.subtracted() function to this region and r and assigns the result to this region
		r1-=r2 is equivalent to r1 = r1.subtracted(r2) .
		"""
		res = super(QRegion,self).__isub__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,r):
		"""
		__eq__(r)
			r=QtGui.QRegion

		Returns true if the region is equal to r ; otherwise returns false.
		"""
		res = super(QRegion,self).__eq__(r)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __xor__(self,r):
		"""
		__xor__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.xored() function to this region and r
		r1^r2 is equivalent to r1.xored(r2) .
		"""
		res = super(QRegion,self).__xor__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __ixor__(self,r):
		"""
		__ixor__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.xored() function to this region and r and assigns the result to this region
		r1^=r2 is equivalent to r1 = r1.xored(r2) .
		"""
		res = super(QRegion,self).__ixor__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __or__(self,r):
		"""
		__or__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.united() function to this region and r
		r1|r2 is equivalent to r1.united(r2) .
		"""
		res = super(QRegion,self).__or__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def __ior__(self,r):
		"""
		__ior__(r)
			r=QtGui.QRegion

		Applies the PySide.QtGui.QRegion.united() function to this region and r and assigns the result to this region
		r1|=r2 is equivalent to r1 = r1.united(r2) .
		"""
		res = super(QRegion,self).__ior__(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def setRects(self,rect,num):
		"""
		setRects(rect,num)
			rect=QtCore.QRect
			num=QtCore.int

		Sets the region using the array of rectangles specified by rects and number
		The rectangles must be optimally Y-X sorted and follow these restrictions:
		"""
		res = super(QRegion,self).setRects(rect,num)
		return res
	#----------------------------------------------------------------------
	def subtracted(self,r):
		"""
		subtracted(r)
			r=QtGui.QRegion

		Returns a region which is r subtracted from this region.
		The figure shows the result when the ellipse on the right is subtracted from the ellipse on the left (left - right ).
		"""
		res = super(QRegion,self).subtracted(r)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(p)
			p=QtCore.QPoint

		translate(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		This is an overloaded function.
		Translates the region point
		:meth:`~PySide.QtGui.QRegion.x` * along the x axis and point
		:meth:`~PySide.QtGui.QRegion.y` * along the y axis, relative to the current position
		Positive values move the region to the right and down.
		Translates to the given point .
		"""
		res = super(QRegion,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		translated(p)
			p=QtCore.QPoint

		Returns a copy of the region that is translated dx along the x axis and dy along the y axis, relative to the current position
		Positive values move the region to the right and down.
		"""
		res = super(QRegion,self).translated(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def united(self,*args,**kwargs):
		"""
		united(r)
			r=QtGui.QRegion

		united(r)
			r=QtCore.QRect

		Returns a region which is the union of this region and r .
		The figure shows the union of two elliptical regions.
		"""
		res = super(QRegion,self).united(*args,**kwargs)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def xored(self,r):
		"""
		xored(r)
			r=QtGui.QRegion

		Returns a region which is the exclusive or (XOR) of this region and r .
		The figure shows the exclusive or of two elliptical regions.
		"""
		res = super(QRegion,self).xored(r)
		isinstance(res,QtGui.QRegion)
		return res
