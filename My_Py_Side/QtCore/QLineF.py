from PySide import QtGui, QtCore

class QLineF(QtCore.QLineF):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLineF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QLineF,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QLineF,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def angle(self):
		"""
		Returns the angle of the line in degrees.
		Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction
		Zero degrees is at the 3 oclock position.
		"""
		res = super(QLineF,self).angle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dx(self):
		"""
		Returns the horizontal component of the lines vector.
		"""
		res = super(QLineF,self).dx()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dy(self):
		"""
		Returns the vertical component of the lines vector.
		"""
		res = super(QLineF,self).dy()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the line is not set up with valid start and end point; otherwise returns false.
		"""
		res = super(QLineF,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the line.
		"""
		res = super(QLineF,self).length()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalVector(self):
		"""
		Returns a line that is perpendicular to this line with the same starting point and length.
		"""
		res = super(QLineF,self).normalVector()
		isinstance(res,QtCore.QLineF)
		return res
	#----------------------------------------------------------------------
	def p1(self):
		"""
		Returns the lines start point.
		"""
		res = super(QLineF,self).p1()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def p2(self):
		"""
		Returns the lines end point.
		"""
		res = super(QLineF,self).p2()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def toLine(self):
		"""
		Returns an integer based copy of this line.
		Note that the returned lines start and end points are rounded to the nearest integer.
		"""
		res = super(QLineF,self).toLine()
		isinstance(res,QtCore.QLine)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QLineF,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def unitVector(self):
		"""
		Returns the unit vector for this line, i.e a line starting at the same point as this line with a length of 1.0.
		"""
		res = super(QLineF,self).unitVector()
		isinstance(res,QtCore.QLineF)
		return res
	#----------------------------------------------------------------------
	def x1(self):
		"""
		Returns the x-coordinate of the lines start point.
		"""
		res = super(QLineF,self).x1()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def x2(self):
		"""
		Returns the x-coordinate of the lines end point.
		"""
		res = super(QLineF,self).x2()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y1(self):
		"""
		Returns the y-coordinate of the lines start point.
		"""
		res = super(QLineF,self).y1()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y2(self):
		"""
		Returns the y-coordinate of the lines end point.
		"""
		res = super(QLineF,self).y2()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def angle(self,l):
		"""
		angle(l)
			l=QtCore.QLineF

		Returns the angle (in degrees) between this line and the given line , taking the direction of the lines into account
		If the lines do not intersect within their range, it is the intersection point of the extended lines that serves as origin (see QLineF.UnboundedIntersection ).
		When the lines are parallel, this function returns 0 if they have the same direction; otherwise it returns 180.
		"""
		res = super(QLineF,self).angle(l)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def angleTo(self,l):
		"""
		angleTo(l)
			l=QtCore.QLineF

		Returns the angle (in degrees) from this line to the given line , taking the direction of the lines into account
		If the lines do not intersect within their range, it is the intersection point of the extended lines that serves as origin (see QLineF.UnboundedIntersection ).
		The returned value represents the number of degrees you need to add to this line to make it have the same angle as the given line , going counter-clockwise.
		"""
		res = super(QLineF,self).angleTo(l)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def intersect(self,l):
		"""
		intersect(l)
			l=QtCore.QLineF

		Returns a value indicating whether or not this line intersects with the given line .
		The actual intersection point is extracted to intersectionPoint (if the pointer is valid)
		If the lines are parallel, the intersection point is undefined.
		"""
		res = super(QLineF,self).intersect(l)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,d):
		"""
		__ne__(d)
			d=QtCore.QLineF

		Returns true if the given line is not the same as this line.
		A line is different from another line if their start or end points differ, or the internal order of the points is different.
		"""
		res = super(QLineF,self).__ne__(d)
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
		res = super(QLineF,self).__mul__(*args,**kwargs)
		isinstance(res,QtCore.QLineF)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,d):
		"""
		__eq__(d)
			d=QtCore.QLineF

		Returns true if the given line is the same as this line.
		A line is identical to another line if the start and end points are identical, and the internal order of the points is the same.
		"""
		res = super(QLineF,self).__eq__(d)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pointAt(self,t):
		"""
		pointAt(t)
			t=QtCore.qreal

		Returns the point at the parameterized position specified by t
		The function returns the lines start point if t = 0, and its end point if t = 1.
		"""
		res = super(QLineF,self).pointAt(t)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setAngle(self,angle):
		"""
		setAngle(angle)
			angle=QtCore.qreal

		Sets the angle of the line to the given angle (in degrees)
		This will change the position of the second point of the line such that the line has the given angle.
		Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction
		Zero degrees is at the 3 oclock position.
		"""
		res = super(QLineF,self).setAngle(angle)
		return res
	#----------------------------------------------------------------------
	def setLength(self,len):
		"""
		setLength(len)
			len=QtCore.qreal

		Sets the length of the line to the given length
		PySide.QtCore.QLineF will move the end point - PySide.QtCore.QLineF.p2() - of the line to give the line its new length.
		If the line is a null line, the length will remain zero regardless of the length specified.
		"""
		res = super(QLineF,self).setLength(len)
		return res
	#----------------------------------------------------------------------
	def setLine(self,x1,y1,x2,y2):
		"""
		setLine(x1,y1,x2,y2)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal

		Sets this line to the start in x1 , y1 and end in x2 , y2 .
		"""
		res = super(QLineF,self).setLine(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def setP1(self,p1):
		"""
		setP1(p1)
			p1=QtCore.QPointF

		Sets the starting point of this line to p1 .
		"""
		res = super(QLineF,self).setP1(p1)
		return res
	#----------------------------------------------------------------------
	def setP2(self,p2):
		"""
		setP2(p2)
			p2=QtCore.QPointF

		Sets the end point of this line to p2 .
		"""
		res = super(QLineF,self).setP2(p2)
		return res
	#----------------------------------------------------------------------
	def setPoints(self,p1,p2):
		"""
		setPoints(p1,p2)
			p1=QtCore.QPointF
			p2=QtCore.QPointF

		Sets the start point of this line to p1 and the end point of this line to p2 .
		"""
		res = super(QLineF,self).setPoints(p1,p2)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(p)
			p=QtCore.QPointF

		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Translates this line by the given offset .
		"""
		res = super(QLineF,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(p)
			p=QtCore.QPointF

		translated(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Returns this line translated by the given offset .
		"""
		res = super(QLineF,self).translated(*args,**kwargs)
		isinstance(res,QtCore.QLineF)
		return res
