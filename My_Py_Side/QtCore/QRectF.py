from PySide import QtGui, QtCore

class QRectF(QtCore.QRectF):
	'''\n
class PySide.QtCore.QRectF\n
class PySide.QtCore.QRectF(topleft, bottomRight)\n
class PySide.QtCore.QRectF(topleft, size)\n
class PySide.QtCore.QRectF(rect)\n
class PySide.QtCore.QRectF(QRectF)\n
class PySide.QtCore.QRectF(left, top, width, height)
	'''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRectF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QRectF,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QRectF,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		Returns the y-coordinate of the rectangles bottom edge.
		"""
		res = super(QRectF,self).bottom()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def bottomLeft(self):
		"""
		Returns the position of the rectangles bottom-left corner.
		"""
		res = super(QRectF,self).bottomLeft()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def bottomRight(self):
		"""
		Returns the position of the rectangles bottom-right corner.
		"""
		res = super(QRectF,self).bottomRight()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def center(self):
		"""
		Returns the center point of the rectangle.
		"""
		res = super(QRectF,self).center()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def getCoords(self):
		"""
		Extracts the position of the rectangles top-left corner to *``x1`` and *``y1`` , and the position of the bottom-right corner to *``x2`` and *``y2`` .
		"""
		res = super(QRectF,self).getCoords()
		return res
	#----------------------------------------------------------------------
	def getRect(self):
		"""
		Extracts the position of the rectangles top-left corner to *``x`` and *``y`` , and its dimensions to *``width`` and *``height`` .
		"""
		res = super(QRectF,self).getRect()
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the rectangle.
		"""
		res = super(QRectF,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the rectangle is empty, otherwise returns false.
		An empty rectangle has PySide.QtCore.QRectF.width() <= 0 or PySide.QtCore.QRectF.height() <= 0
		An empty rectangle is not valid (i.e., PySide.QtCore.QRectF.isEmpty() == ! PySide.QtCore.QRectF.isValid() ).
		Use the PySide.QtCore.QRectF.normalized() function to retrieve a rectangle where the corners are swapped.
		"""
		res = super(QRectF,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the rectangle is a null rectangle, otherwise returns false.
		A null rectangle has both the width and the height set to 0
		A null rectangle is also empty, and hence not valid.
		"""
		res = super(QRectF,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the rectangle is valid, otherwise returns false.
		A valid rectangle has a PySide.QtCore.QRectF.width() > 0 and PySide.QtCore.QRectF.height() > 0
		Note that non-trivial operations like intersections are not defined for invalid rectangles
		A valid rectangle is not empty (i.e., PySide.QtCore.QRectF.isValid() == ! PySide.QtCore.QRectF.isEmpty() ).
		"""
		res = super(QRectF,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def left(self):
		"""
		Returns the x-coordinate of the rectangles left edge
		Equivalent to PySide.QtCore.QRectF.x() .
		"""
		res = super(QRectF,self).left()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.
		If PySide.QtCore.QRectF.width() < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if PySide.QtCore.QRectF.height() < 0.
		"""
		res = super(QRectF,self).normalized()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def right(self):
		"""
		Returns the x-coordinate of the rectangles right edge.
		"""
		res = super(QRectF,self).right()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the rectangle.
		"""
		res = super(QRectF,self).size()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def toAlignedRect(self):
		"""
		Returns a PySide.QtCore.QRect based on the values of this rectangle that is the smallest possible integer rectangle that completely contains this rectangle.
		"""
		res = super(QRectF,self).toAlignedRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def toRect(self):
		"""
		Returns a PySide.QtCore.QRect based on the values of this rectangle
		Note that the coordinates in the returned rectangle are rounded to the nearest integer.
		"""
		res = super(QRectF,self).toRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		Returns the y-coordinate of the rectangles top edge
		Equivalent to PySide.QtCore.QRectF.y() .
		"""
		res = super(QRectF,self).top()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def topLeft(self):
		"""
		Returns the position of the rectangles top-left corner.
		"""
		res = super(QRectF,self).topLeft()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def topRight(self):
		"""
		Returns the position of the rectangles top-right corner.
		"""
		res = super(QRectF,self).topRight()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width of the rectangle.
		"""
		res = super(QRectF,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x-coordinate of the rectangles left edge
		Equivalent to PySide.QtCore.QRectF.left() .
		"""
		res = super(QRectF,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y-coordinate of the rectangles top edge
		Equivalent to PySide.QtCore.QRectF.top() .
		"""
		res = super(QRectF,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def adjust(self,x1,y1,x2,y2):
		"""
		adjust(x1,y1,x2,y2)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal

		Adds dx1 , dy1 , dx2 and dy2 respectively to the existing coordinates of the rectangle.
		"""
		res = super(QRectF,self).adjust(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def adjusted(self,x1,y1,x2,y2):
		"""
		adjusted(x1,y1,x2,y2)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal

		Returns a new rectangle with dx1 , dy1 , dx2 and dy2 added respectively to the existing coordinates of this rectangle.
		"""
		res = super(QRectF,self).adjusted(x1,y1,x2,y2)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def contains(self,*args,**kwargs):
		"""
		contains(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		contains(p)
			p=QtCore.QPointF

		contains(r)
			r=QtCore.QRectF

		This is an overloaded function.
		Returns true if the point (x , y ) is inside or on the edge of the rectangle; otherwise returns false.
		"""
		res = super(QRectF,self).contains(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def intersect(self,r):
		"""
		intersect(r)
			r=QtCore.QRectF

		Use intersected(rectangle ) instead.
		"""
		res = super(QRectF,self).intersect(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def intersected(self,other):
		"""
		intersected(other)
			other=QtCore.QRectF

		Returns the intersection of this rectangle and the given rectangle
		Note that r.intersected(s) is equivalent to r & s .
		"""
		res = super(QRectF,self).intersected(other)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def intersects(self,r):
		"""
		intersects(r)
			r=QtCore.QRectF

		Returns true if this rectangle intersects with the given rectangle (i.e
		there is a non-empty area of overlap between them), otherwise returns false.
		The intersection rectangle can be retrieved using the PySide.QtCore.QRectF.intersected() function.
		"""
		res = super(QRectF,self).intersects(r)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def moveBottom(self,pos):
		"""
		moveBottom(pos)
			pos=QtCore.qreal

		Moves the rectangle vertically, leaving the rectangles bottom edge at the given y coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveBottom(pos)
		return res
	#----------------------------------------------------------------------
	def moveBottomLeft(self,p):
		"""
		moveBottomLeft(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the bottom-left corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveBottomLeft(p)
		return res
	#----------------------------------------------------------------------
	def moveBottomRight(self,p):
		"""
		moveBottomRight(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the bottom-right corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveBottomRight(p)
		return res
	#----------------------------------------------------------------------
	def moveCenter(self,p):
		"""
		moveCenter(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the center point at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveCenter(p)
		return res
	#----------------------------------------------------------------------
	def moveLeft(self,pos):
		"""
		moveLeft(pos)
			pos=QtCore.qreal

		Moves the rectangle horizontally, leaving the rectangles left edge at the given x coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveLeft(pos)
		return res
	#----------------------------------------------------------------------
	def moveRight(self,pos):
		"""
		moveRight(pos)
			pos=QtCore.qreal

		Moves the rectangle horizontally, leaving the rectangles right edge at the given x coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveRight(pos)
		return res
	#----------------------------------------------------------------------
	def moveTo(self,*args,**kwargs):
		"""
		moveTo(x,t)
			x=QtCore.qreal
			t=QtCore.qreal

		moveTo(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the top-left corner at the given position (x , y )
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveTo(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def moveTop(self,pos):
		"""
		moveTop(pos)
			pos=QtCore.qreal

		Moves the rectangle vertically, leaving the rectangles top line at the given y coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveTop(pos)
		return res
	#----------------------------------------------------------------------
	def moveTopLeft(self,p):
		"""
		moveTopLeft(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the top-left corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveTopLeft(p)
		return res
	#----------------------------------------------------------------------
	def moveTopRight(self,p):
		"""
		moveTopRight(p)
			p=QtCore.QPointF

		Moves the rectangle, leaving the top-right corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRectF,self).moveTopRight(p)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__2):
		"""
		__ne__(arg__2)
			arg__2=QtCore.QRectF


		"""
		res = super(QRectF,self).__ne__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __and__(self,r):
		"""
		__and__(r)
			r=QtCore.QRectF

		Returns the intersection of this rectangle and the given rectangle
		Returns an empty rectangle if there is no intersection.
		"""
		res = super(QRectF,self).__and__(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def __iand__(self,r):
		"""
		__iand__(r)
			r=QtCore.QRectF

		Intersects this rectangle with the given rectangle .
		"""
		res = super(QRectF,self).__iand__(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__2):
		"""
		__eq__(arg__2)
			arg__2=QtCore.QRectF


		"""
		res = super(QRectF,self).__eq__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __or__(self,r):
		"""
		__or__(r)
			r=QtCore.QRectF

		Returns the bounding rectangle of this rectangle and the given rectangle .
		"""
		res = super(QRectF,self).__or__(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def __ior__(self,r):
		"""
		__ior__(r)
			r=QtCore.QRectF

		Unites this rectangle with the given rectangle .
		"""
		res = super(QRectF,self).__ior__(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def setBottom(self,pos):
		"""
		setBottom(pos)
			pos=QtCore.qreal

		Sets the bottom edge of the rectangle to the given y coordinate
		May change the height, but will never change the top edge of the rectangle.
		"""
		res = super(QRectF,self).setBottom(pos)
		return res
	#----------------------------------------------------------------------
	def setBottomLeft(self,p):
		"""
		setBottomLeft(p)
			p=QtCore.QPointF

		Set the bottom-left corner of the rectangle to the given position
		May change the size, but will never change the top-right corner of the rectangle.
		"""
		res = super(QRectF,self).setBottomLeft(p)
		return res
	#----------------------------------------------------------------------
	def setBottomRight(self,p):
		"""
		setBottomRight(p)
			p=QtCore.QPointF

		Set the bottom-right corner of the rectangle to the given position
		May change the size, but will never change the top-left corner of the rectangle.
		"""
		res = super(QRectF,self).setBottomRight(p)
		return res
	#----------------------------------------------------------------------
	def setCoords(self,x1,y1,x2,y2):
		"""
		setCoords(x1,y1,x2,y2)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal

		Sets the coordinates of the rectangles top-left corner to (x1 , y1 ), and the coordinates of its bottom-right corner to (x2 , y2 ).
		"""
		res = super(QRectF,self).setCoords(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,h):
		"""
		setHeight(h)
			h=QtCore.qreal

		Sets the height of the rectangle to the given height
		The bottom edge is changed, but not the top one.
		"""
		res = super(QRectF,self).setHeight(h)
		return res
	#----------------------------------------------------------------------
	def setLeft(self,pos):
		"""
		setLeft(pos)
			pos=QtCore.qreal

		Sets the left edge of the rectangle to the given x coordinate
		May change the width, but will never change the right edge of the rectangle.
		Equivalent to PySide.QtCore.QRectF.setX() .
		"""
		res = super(QRectF,self).setLeft(pos)
		return res
	#----------------------------------------------------------------------
	def setRect(self,x,y,w,h):
		"""
		setRect(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		Sets the coordinates of the rectangles top-left corner to (x , y ), and its size to the given width and height .
		"""
		res = super(QRectF,self).setRect(x,y,w,h)
		return res
	#----------------------------------------------------------------------
	def setRight(self,pos):
		"""
		setRight(pos)
			pos=QtCore.qreal

		Sets the right edge of the rectangle to the given x coordinate
		May change the width, but will never change the left edge of the rectangle.
		"""
		res = super(QRectF,self).setRight(pos)
		return res
	#----------------------------------------------------------------------
	def setSize(self,s):
		"""
		setSize(s)
			s=QtCore.QSizeF

		Sets the size of the rectangle to the given size
		The top-left corner is not moved.
		"""
		res = super(QRectF,self).setSize(s)
		return res
	#----------------------------------------------------------------------
	def setTop(self,pos):
		"""
		setTop(pos)
			pos=QtCore.qreal

		Sets the top edge of the rectangle to the given y coordinate
		May change the height, but will never change the bottom edge of the rectangle.
		Equivalent to PySide.QtCore.QRectF.setY() .
		"""
		res = super(QRectF,self).setTop(pos)
		return res
	#----------------------------------------------------------------------
	def setTopLeft(self,p):
		"""
		setTopLeft(p)
			p=QtCore.QPointF

		Set the top-left corner of the rectangle to the given position
		May change the size, but will never change the bottom-right corner of the rectangle.
		"""
		res = super(QRectF,self).setTopLeft(p)
		return res
	#----------------------------------------------------------------------
	def setTopRight(self,p):
		"""
		setTopRight(p)
			p=QtCore.QPointF

		Set the top-right corner of the rectangle to the given position
		May change the size, but will never change the bottom-left corner of the rectangle.
		"""
		res = super(QRectF,self).setTopRight(p)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,w):
		"""
		setWidth(w)
			w=QtCore.qreal

		Sets the width of the rectangle to the given width
		The right edge is changed, but not the left one.
		"""
		res = super(QRectF,self).setWidth(w)
		return res
	#----------------------------------------------------------------------
	def setX(self,pos):
		"""
		setX(pos)
			pos=QtCore.qreal

		Sets the left edge of the rectangle to the given x coordinate
		May change the width, but will never change the right edge of the rectangle.
		Equivalent to PySide.QtCore.QRectF.setLeft() .
		"""
		res = super(QRectF,self).setX(pos)
		return res
	#----------------------------------------------------------------------
	def setY(self,pos):
		"""
		setY(pos)
			pos=QtCore.qreal

		Sets the top edge of the rectangle to the given y coordinate
		May change the height, but will never change the bottom edge of the rectangle.
		Equivalent to PySide.QtCore.QRectF.setTop() .
		"""
		res = super(QRectF,self).setY(pos)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		translate(p)
			p=QtCore.QPointF

		Moves the rectangle dx along the x-axis and dy along the y-axis, relative to the current position
		Positive values move the rectangle to the right and downwards.
		"""
		res = super(QRectF,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(p)
			p=QtCore.QPointF

		translated(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		This is an overloaded function.
		Returns a copy of the rectangle that is translated offset
		PySide.QtCore.QPointF.x() along the x axis and offset
		PySide.QtCore.QPointF.y() along the y axis, relative to the current position.
		"""
		res = super(QRectF,self).translated(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def unite(self,r):
		"""
		unite(r)
			r=QtCore.QRectF

		Use united(rectangle ) instead.
		"""
		res = super(QRectF,self).unite(r)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def united(self,other):
		"""
		united(other)
			other=QtCore.QRectF

		Returns the bounding rectangle of this rectangle and the given rectangle .
		"""
		res = super(QRectF,self).united(other)
		isinstance(res,QtCore.QRectF)
		return res
