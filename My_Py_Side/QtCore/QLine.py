from PySide import QtGui, QtCore

class QLine(QtCore.QLine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QLine,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QLine,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def dx(self):
		"""
		Returns the horizontal component of the lines vector.
		"""
		res = super(QLine,self).dx()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def dy(self):
		"""
		Returns the vertical component of the lines vector.
		"""
		res = super(QLine,self).dy()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the line is not set up with valid start and end point; otherwise returns false.
		"""
		res = super(QLine,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def p1(self):
		"""
		Returns the lines start point.
		"""
		res = super(QLine,self).p1()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def p2(self):
		"""
		Returns the lines end point.
		"""
		res = super(QLine,self).p2()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QLine,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def x1(self):
		"""
		Returns the x-coordinate of the lines start point.
		"""
		res = super(QLine,self).x1()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def x2(self):
		"""
		Returns the x-coordinate of the lines end point.
		"""
		res = super(QLine,self).x2()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y1(self):
		"""
		Returns the y-coordinate of the lines start point.
		"""
		res = super(QLine,self).y1()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def y2(self):
		"""
		Returns the y-coordinate of the lines end point.
		"""
		res = super(QLine,self).y2()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,d):
		"""
		__ne__(d)
			d=QtCore.QLine

		Returns true if the given line is not the same as this line.
		A line is different from another line if any of their start or end points differ, or the internal order of the points is different.
		"""
		res = super(QLine,self).__ne__(d)
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
		res = super(QLine,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QLine)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,d):
		"""
		__eq__(d)
			d=QtCore.QLine

		Returns true if the given line is the same as this line.
		A line is identical to another line if the start and end points are identical, and the internal order of the points is the same.
		"""
		res = super(QLine,self).__eq__(d)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setLine(self,x1,y1,x2,y2):
		"""
		setLine(x1,y1,x2,y2)
			x1=QtCore.int
			y1=QtCore.int
			x2=QtCore.int
			y2=QtCore.int

		Sets this line to the start in x1 , y1 and end in x2 , y2 .
		"""
		res = super(QLine,self).setLine(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def setP1(self,p1):
		"""
		setP1(p1)
			p1=QtCore.QPoint

		Sets the starting point of this line to p1 .
		"""
		res = super(QLine,self).setP1(p1)
		return res
	#----------------------------------------------------------------------
	def setP2(self,p2):
		"""
		setP2(p2)
			p2=QtCore.QPoint

		Sets the end point of this line to p2 .
		"""
		res = super(QLine,self).setP2(p2)
		return res
	#----------------------------------------------------------------------
	def setPoints(self,p1,p2):
		"""
		setPoints(p1,p2)
			p1=QtCore.QPoint
			p2=QtCore.QPoint

		Sets the start point of this line to p1 and the end point of this line to p2 .
		"""
		res = super(QLine,self).setPoints(p1,p2)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		translate(p)
			p=QtCore.QPoint

		This is an overloaded function.
		Translates this line the distance specified by dx and dy .
		"""
		res = super(QLine,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(p)
			p=QtCore.QPoint

		translated(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		Returns this line translated by the given offset .
		"""
		res = super(QLine,self).translated(*args,**kwargs)
		isinstance(res,QtCore.QLine)
		return res
