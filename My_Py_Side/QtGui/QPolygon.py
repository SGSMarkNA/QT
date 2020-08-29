from PySide import QtGui, QtCore

class QPolygon(QtGui.QPolygon):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPolygon,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QPolygon,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def alignOfTypedData(self):
		"""

		"""
		res = super(QPolygon,self).alignOfTypedData()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the bounding rectangle of the polygon, or PySide.QtCore.QRect (0, 0, 0, 0) if the polygon is empty.
		"""
		res = super(QPolygon,self).boundingRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def capacity(self):
		"""

		"""
		res = super(QPolygon,self).capacity()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""

		"""
		res = super(QPolygon,self).clear()
		return res
	#----------------------------------------------------------------------
	def constData(self):
		"""

		"""
		res = super(QPolygon,self).constData()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""

		"""
		res = super(QPolygon,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""

		"""
		res = super(QPolygon,self).data()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QPolygon,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def empty(self):
		"""

		"""
		res = super(QPolygon,self).empty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""

		"""
		res = super(QPolygon,self).first()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def front(self):
		"""

		"""
		res = super(QPolygon,self).front()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""

		"""
		res = super(QPolygon,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""

		"""
		res = super(QPolygon,self).last()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QPolygon.operator[](i)(self):
		"""

		"""
		res = super(QPolygon,self).PySide.QtGui.QPolygon.operator[](i)()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def pop_back(self):
		"""

		"""
		res = super(QPolygon,self).pop_back()
		return res
	#----------------------------------------------------------------------
	def pop_front(self):
		"""

		"""
		res = super(QPolygon,self).pop_front()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""

		"""
		res = super(QPolygon,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sizeOfTypedData(self):
		"""

		"""
		res = super(QPolygon,self).sizeOfTypedData()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def squeeze(self):
		"""

		"""
		res = super(QPolygon,self).squeeze()
		return res
	#----------------------------------------------------------------------
	def toList(self):
		"""

		"""
		res = super(QPolygon,self).toList()
		return res
	#----------------------------------------------------------------------
	def append(self,t):
		"""
		append(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).append(t)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int


		"""
		res = super(QPolygon,self).at(i)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def contains(self,t):
		"""
		contains(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).contains(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def containsPoint(self,pt,fillRule):
		"""
		containsPoint(pt,fillRule)
			pt=QtCore.QPoint
			fillRule=QtCore.Qt.FillRule


		"""
		res = super(QPolygon,self).containsPoint(pt,fillRule)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self,t):
		"""
		count(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).count(t)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def endsWith(self,t):
		"""
		endsWith(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).endsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def erase(self,abegin,aend):
		"""
		erase(abegin,aend)
			abegin=QtCore.QPoint
			aend=QtCore.QPoint


		"""
		res = super(QPolygon,self).erase(abegin,aend)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def fill(self,t,size=None):
		"""
		fill(t,size=None)
			t=QtCore.QPoint
			size=QtCore.int


		"""
		res = super(QPolygon,self).fill(t,size)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,t,from=None):
		"""
		indexOf(t,from=None)
			t=QtCore.QPoint
			from=QtCore.int


		"""
		res = super(QPolygon,self).indexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insert(self,*args,**kwargs):
		"""
		insert(i,t)
			i=QtCore.int
			t=QtCore.QPoint

		insert(i,n,t)
			i=QtCore.int
			n=QtCore.int
			t=QtCore.QPoint

		insert(before,n,t)
			before=QtCore.QPoint
			n=QtCore.int
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).insert(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def intersected(self,r):
		"""
		intersected(r)
			r=QtGui.QPolygon

		Returns a polygon which is the intersection of this polygon and r .
		Set operations on polygons will treat the polygons as areas
		Non-closed polygons will be treated as implicitly closed.
		"""
		res = super(QPolygon,self).intersected(r)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def isSharedWith(self,other):
		"""
		isSharedWith(other)
			other=unKnown


		"""
		res = super(QPolygon,self).isSharedWith(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastIndexOf(self,t,from=None):
		"""
		lastIndexOf(t,from=None)
			t=QtCore.QPoint
			from=QtCore.int


		"""
		res = super(QPolygon,self).lastIndexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def mid(self,pos,length=None):
		"""
		mid(pos,length=None)
			pos=QtCore.int
			length=QtCore.int


		"""
		res = super(QPolygon,self).mid(pos,length)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v):
		"""
		__ne__(v)
			v=unKnown


		"""
		res = super(QPolygon,self).__ne__(v)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(m)
			m=QtGui.QMatrix

		__mul__(m)
			m=QtGui.QTransform


		"""
		res = super(QPolygon,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def __add__(self,l):
		"""
		__add__(l)
			l=unKnown


		"""
		res = super(QPolygon,self).__add__(l)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(t)
			t=QtCore.QPoint

		__iadd__(l)
			l=unKnown

		__iadd__(l)
			l=unKnown


		"""
		res = super(QPolygon,self).__iadd__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __lshift__(self,*args,**kwargs):
		"""
		__lshift__(l)
			l=unKnown

		__lshift__(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).__lshift__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v):
		"""
		__eq__(v)
			v=unKnown


		"""
		res = super(QPolygon,self).__eq__(v)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepend(self,t):
		"""
		prepend(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).prepend(t)
		return res
	#----------------------------------------------------------------------
	def push_back(self,t):
		"""
		push_back(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).push_back(t)
		return res
	#----------------------------------------------------------------------
	def push_front(self,t):
		"""
		push_front(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).push_front(t)
		return res
	#----------------------------------------------------------------------
	def realloc(self,size,alloc):
		"""
		realloc(size,alloc)
			size=QtCore.int
			alloc=QtCore.int


		"""
		res = super(QPolygon,self).realloc(size,alloc)
		return res
	#----------------------------------------------------------------------
	def remove(self,*args,**kwargs):
		"""
		remove(i)
			i=QtCore.int

		remove(i,n)
			i=QtCore.int
			n=QtCore.int


		"""
		res = super(QPolygon,self).remove(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def replace(self,i,t):
		"""
		replace(i,t)
			i=QtCore.int
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).replace(i,t)
		return res
	#----------------------------------------------------------------------
	def reserve(self,size):
		"""
		reserve(size)
			size=QtCore.int


		"""
		res = super(QPolygon,self).reserve(size)
		return res
	#----------------------------------------------------------------------
	def resize(self,size):
		"""
		resize(size)
			size=QtCore.int


		"""
		res = super(QPolygon,self).resize(size)
		return res
	#----------------------------------------------------------------------
	def setSharable(self,sharable):
		"""
		setSharable(sharable)
			sharable=QtCore.bool


		"""
		res = super(QPolygon,self).setSharable(sharable)
		return res
	#----------------------------------------------------------------------
	def startsWith(self,t):
		"""
		startsWith(t)
			t=QtCore.QPoint


		"""
		res = super(QPolygon,self).startsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def subtracted(self,r):
		"""
		subtracted(r)
			r=QtGui.QPolygon

		Returns a polygon which is r subtracted from this polygon.
		Set operations on polygons will treat the polygons as areas
		Non-closed polygons will be treated as implicitly closed.
		"""
		res = super(QPolygon,self).subtracted(r)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		translate(offset)
			offset=QtCore.QPoint

		Translates all points in the polygon by (dx , dy ).
		"""
		res = super(QPolygon,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		translated(offset)
			offset=QtCore.QPoint

		Returns a copy of the polygon that is translated by (dx , dy ).
		"""
		res = super(QPolygon,self).translated(*args,**kwargs)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def united(self,r):
		"""
		united(r)
			r=QtGui.QPolygon

		Returns a polygon which is the union of this polygon and r .
		Set operations on polygons, will treat the polygons as areas, and implicitly close the polygon.
		"""
		res = super(QPolygon,self).united(r)
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(i)
			i=QtCore.int

		value(i,defaultValue)
			i=QtCore.int
			defaultValue=QtCore.QPoint


		"""
		res = super(QPolygon,self).value(*args,**kwargs)
		isinstance(res,QtCore.QPoint)
		return res
