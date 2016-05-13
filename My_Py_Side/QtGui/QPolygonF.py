from PySide import QtGui, QtCore

class QPolygonF(QtGui.QPolygonF):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPolygonF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignOfTypedData(self):
		"""

		"""
		res = super(QPolygonF,self).alignOfTypedData()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the bounding rectangle of the polygon, or PySide.QtCore.QRectF (0,0,0,0) if the polygon is empty.
		"""
		res = super(QPolygonF,self).boundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def capacity(self):
		"""

		"""
		res = super(QPolygonF,self).capacity()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""

		"""
		res = super(QPolygonF,self).clear()
		return res
	#----------------------------------------------------------------------
	def constData(self):
		"""

		"""
		res = super(QPolygonF,self).constData()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""

		"""
		res = super(QPolygonF,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""

		"""
		res = super(QPolygonF,self).data()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QPolygonF,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def empty(self):
		"""

		"""
		res = super(QPolygonF,self).empty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""

		"""
		res = super(QPolygonF,self).first()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def front(self):
		"""

		"""
		res = super(QPolygonF,self).front()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def isClosed(self):
		"""
		Returns true if the polygon is closed; otherwise returns false.
		A polygon is said to be closed if its start point and end point are equal.
		"""
		res = super(QPolygonF,self).isClosed()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""

		"""
		res = super(QPolygonF,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""

		"""
		res = super(QPolygonF,self).last()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QPolygonF.operator[](i)(self):
		"""

		"""
		res = super(QPolygonF,self).PySide.QtGui.QPolygonF.operator[](i)()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def pop_back(self):
		"""

		"""
		res = super(QPolygonF,self).pop_back()
		return res
	#----------------------------------------------------------------------
	def pop_front(self):
		"""

		"""
		res = super(QPolygonF,self).pop_front()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""

		"""
		res = super(QPolygonF,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sizeOfTypedData(self):
		"""

		"""
		res = super(QPolygonF,self).sizeOfTypedData()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def squeeze(self):
		"""

		"""
		res = super(QPolygonF,self).squeeze()
		return res
	#----------------------------------------------------------------------
	def toList(self):
		"""

		"""
		res = super(QPolygonF,self).toList()
		return res
	#----------------------------------------------------------------------
	def toPolygon(self):
		"""
		Creates and returns a PySide.QtGui.QPolygon by converting each PySide.QtCore.QPointF to a PySide.QtCore.QPoint .
		"""
		res = super(QPolygonF,self).toPolygon()
		isinstance(res,QtGui.QPolygon)
		return res
	#----------------------------------------------------------------------
	def append(self,t):
		"""
		append(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).append(t)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int


		"""
		res = super(QPolygonF,self).at(i)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def contains(self,t):
		"""
		contains(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).contains(t)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def containsPoint(self,pt,fillRule):
		"""
		containsPoint(pt,fillRule)
			pt=QtCore.QPointF
			fillRule=QtCore.Qt.FillRule


		"""
		res = super(QPolygonF,self).containsPoint(pt,fillRule)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def count(self,t):
		"""
		count(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).count(t)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def endsWith(self,t):
		"""
		endsWith(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).endsWith(t)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def erase(self,abegin,aend):
		"""
		erase(abegin,aend)
			abegin=QtCore.QPointF
			aend=QtCore.QPointF


		"""
		res = super(QPolygonF,self).erase(abegin,aend)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def fill(self,t,size=None):
		"""
		fill(t,size=None)
			t=QtCore.QPointF
			size=QtCore.int


		"""
		res = super(QPolygonF,self).fill(t,size)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,t,from=None):
		"""
		indexOf(t,from=None)
			t=QtCore.QPointF
			from=QtCore.int


		"""
		res = super(QPolygonF,self).indexOf(t,from)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def insert(self,*args,**kwargs):
		"""
		insert(i,n,t)
			i=QtCore.int
			n=QtCore.int
			t=QtCore.QPointF

		insert(before,n,t)
			before=QtCore.QPointF
			n=QtCore.int
			t=QtCore.QPointF

		insert(i,t)
			i=QtCore.int
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).insert(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def intersected(self,r):
		"""
		intersected(r)
			r=QtGui.QPolygonF

		Returns a polygon which is the intersection of this polygon and r .
		Set operations on polygons will treat the polygons as areas
		Non-closed polygons will be treated as implicitly closed.
		"""
		res = super(QPolygonF,self).intersected(r)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def isSharedWith(self,other):
		"""
		isSharedWith(other)
			other=unKnown


		"""
		res = super(QPolygonF,self).isSharedWith(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lastIndexOf(self,t,from=None):
		"""
		lastIndexOf(t,from=None)
			t=QtCore.QPointF
			from=QtCore.int


		"""
		res = super(QPolygonF,self).lastIndexOf(t,from)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def mid(self,pos,length=None):
		"""
		mid(pos,length=None)
			pos=QtCore.int
			length=QtCore.int


		"""
		res = super(QPolygonF,self).mid(pos,length)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v):
		"""
		__ne__(v)
			v=unKnown


		"""
		res = super(QPolygonF,self).__ne__(v)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __mul__(self,*args,**kwargs):
		"""
		__mul__(m)
			m=QtGui.QTransform

		__mul__(m)
			m=QtGui.QMatrix


		"""
		res = super(QPolygonF,self).__mul__(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def __add__(self,l):
		"""
		__add__(l)
			l=unKnown


		"""
		res = super(QPolygonF,self).__add__(l)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(l)
			l=unKnown

		__iadd__(l)
			l=unKnown

		__iadd__(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).__iadd__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v):
		"""
		__eq__(v)
			v=unKnown


		"""
		res = super(QPolygonF,self).__eq__(v)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def prepend(self,t):
		"""
		prepend(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).prepend(t)
		return res
	#----------------------------------------------------------------------
	def push_back(self,t):
		"""
		push_back(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).push_back(t)
		return res
	#----------------------------------------------------------------------
	def push_front(self,t):
		"""
		push_front(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).push_front(t)
		return res
	#----------------------------------------------------------------------
	def realloc(self,size,alloc):
		"""
		realloc(size,alloc)
			size=QtCore.int
			alloc=QtCore.int


		"""
		res = super(QPolygonF,self).realloc(size,alloc)
		return res
	#----------------------------------------------------------------------
	def remove(self,*args,**kwargs):
		"""
		remove(i,n)
			i=QtCore.int
			n=QtCore.int

		remove(i)
			i=QtCore.int


		"""
		res = super(QPolygonF,self).remove(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def replace(self,i,t):
		"""
		replace(i,t)
			i=QtCore.int
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).replace(i,t)
		return res
	#----------------------------------------------------------------------
	def reserve(self,size):
		"""
		reserve(size)
			size=QtCore.int


		"""
		res = super(QPolygonF,self).reserve(size)
		return res
	#----------------------------------------------------------------------
	def resize(self,size):
		"""
		resize(size)
			size=QtCore.int


		"""
		res = super(QPolygonF,self).resize(size)
		return res
	#----------------------------------------------------------------------
	def setSharable(self,sharable):
		"""
		setSharable(sharable)
			sharable=QtCore.bool


		"""
		res = super(QPolygonF,self).setSharable(sharable)
		return res
	#----------------------------------------------------------------------
	def startsWith(self,t):
		"""
		startsWith(t)
			t=QtCore.QPointF


		"""
		res = super(QPolygonF,self).startsWith(t)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def subtracted(self,r):
		"""
		subtracted(r)
			r=QtGui.QPolygonF

		Returns a polygon which is r subtracted from this polygon.
		Set operations on polygons will treat the polygons as areas
		Non-closed polygons will be treated as implicitly closed.
		"""
		res = super(QPolygonF,self).subtracted(r)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(offset)
			offset=QtCore.QPointF

		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Translate all points in the polygon by the given offset .
		"""
		res = super(QPolygonF,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		translated(offset)
			offset=QtCore.QPointF

		This is an overloaded function.
		Returns a copy of the polygon that is translated by (dx , dy ).
		"""
		res = super(QPolygonF,self).translated(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def united(self,r):
		"""
		united(r)
			r=QtGui.QPolygonF

		Returns a polygon which is the union of this polygon and r .
		Set operations on polygons will treat the polygons as areas
		Non-closed polygons will be treated as implicitly closed.
		"""
		res = super(QPolygonF,self).united(r)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(i)
			i=QtCore.int

		value(i,defaultValue)
			i=QtCore.int
			defaultValue=QtCore.QPointF


		"""
		res = super(QPolygonF,self).value(*args,**kwargs)
		isinstance(res,QtCore.QPointF)
		return res
