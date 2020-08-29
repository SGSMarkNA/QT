from PySide import QtGui, QtCore

class QRect(QtCore.QRect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QRect,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QRect,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		Returns the y-coordinate of the rectangles bottom edge.
		Note that for historical reasons this function returns PySide.QtCore.QRect.top() + PySide.QtCore.QRect.height() - 1; use PySide.QtCore.QRect.y() + PySide.QtCore.QRect.height() to retrieve the true y-coordinate.
		"""
		res = super(QRect,self).bottom()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def bottomLeft(self):
		"""
		Returns the position of the rectangles bottom-left corner
		Note that for historical reasons this function returns PySide.QtCore.QPoint ( PySide.QtCore.QRect.left() , PySide.QtCore.QRect.top() + PySide.QtCore.QRect.height() - 1).
		"""
		res = super(QRect,self).bottomLeft()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def bottomRight(self):
		"""
		Returns the position of the rectangles bottom-right corner.
		Note that for historical reasons this function returns PySide.QtCore.QPoint ( PySide.QtCore.QRect.left() + PySide.QtCore.QRect.width() -1, PySide.QtCore.QRect.top() + PySide.QtCore.QRect.height() - 1).
		"""
		res = super(QRect,self).bottomRight()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def center(self):
		"""
		Returns the center point of the rectangle.
		"""
		res = super(QRect,self).center()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def getCoords(self):
		"""
		Extracts the position of the rectangles top-left corner to *``x1`` and *``y1`` , and the position of the bottom-right corner to *``x2`` and *``y2`` .
		"""
		res = super(QRect,self).getCoords()
		return res
	#----------------------------------------------------------------------
	def getRect(self):
		"""
		Extracts the position of the rectangles top-left corner to *``x`` and *``y`` , and its dimensions to *``width`` and *``height`` .
		"""
		res = super(QRect,self).getRect()
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the rectangle.
		"""
		res = super(QRect,self).height()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the rectangle is empty, otherwise returns false.
		An empty rectangle has a PySide.QtCore.QRect.left() > PySide.QtCore.QRect.right() or PySide.QtCore.QRect.top() > PySide.QtCore.QRect.bottom()
		An empty rectangle is not valid (i.e., PySide.QtCore.QRect.isEmpty() == ! PySide.QtCore.QRect.isValid() ).
		Use the PySide.QtCore.QRect.normalized() function to retrieve a rectangle where the corners are swapped.
		"""
		res = super(QRect,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the rectangle is a null rectangle, otherwise returns false.
		A null rectangle has both the width and the height set to 0 (i.e., PySide.QtCore.QRect.right() == PySide.QtCore.QRect.left() - 1 and PySide.QtCore.QRect.bottom() == PySide.QtCore.QRect.top() - 1)
		A null rectangle is also empty, and hence is not valid.
		"""
		res = super(QRect,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the rectangle is valid, otherwise returns false.
		A valid rectangle has a PySide.QtCore.QRect.left() < PySide.QtCore.QRect.right() and PySide.QtCore.QRect.top() < PySide.QtCore.QRect.bottom()
		Note that non-trivial operations like intersections are not defined for invalid rectangles
		A valid rectangle is not empty (i.e., PySide.QtCore.QRect.isValid() == ! PySide.QtCore.QRect.isEmpty() ).
		"""
		res = super(QRect,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def left(self):
		"""
		Returns the x-coordinate of the rectangles left edge
		Equivalent to PySide.QtCore.QRect.x() .
		"""
		res = super(QRect,self).left()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def normalized(self):
		"""
		Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.
		If PySide.QtCore.QRect.width() < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if PySide.QtCore.QRect.height() < 0.
		"""
		res = super(QRect,self).normalized()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def right(self):
		"""
		Returns the x-coordinate of the rectangles right edge.
		Note that for historical reasons this function returns PySide.QtCore.QRect.left() + PySide.QtCore.QRect.width() - 1; use PySide.QtCore.QRect.x() + PySide.QtCore.QRect.width() to retrieve the true x-coordinate.
		"""
		res = super(QRect,self).right()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the rectangle.
		"""
		res = super(QRect,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		Returns the y-coordinate of the rectangles top edge
		Equivalent to PySide.QtCore.QRect.y() .
		"""
		res = super(QRect,self).top()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def topLeft(self):
		"""
		Returns the position of the rectangles top-left corner.
		"""
		res = super(QRect,self).topLeft()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def topRight(self):
		"""
		Returns the position of the rectangles top-right corner.
		Note that for historical reasons this function returns PySide.QtCore.QPoint ( PySide.QtCore.QRect.left() + PySide.QtCore.QRect.width() -1, PySide.QtCore.QRect.top() ).
		"""
		res = super(QRect,self).topRight()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width of the rectangle.
		"""
		res = super(QRect,self).width()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the x-coordinate of the rectangles left edge
		Equivalent to PySide.QtCore.QRect.left() .
		"""
		res = super(QRect,self).x()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the y-coordinate of the rectangles top edge
		Equivalent to PySide.QtCore.QRect.top() .
		"""
		res = super(QRect,self).y()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def adjust(self,x1,y1,x2,y2):
		"""
		adjust(x1,y1,x2,y2)
			x1=QtCore.int
			y1=QtCore.int
			x2=QtCore.int
			y2=QtCore.int

		Adds dx1 , dy1 , dx2 and dy2 respectively to the existing coordinates of the rectangle.
		"""
		res = super(QRect,self).adjust(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def adjusted(self,x1,y1,x2,y2):
		"""
		adjusted(x1,y1,x2,y2)
			x1=QtCore.int
			y1=QtCore.int
			x2=QtCore.int
			y2=QtCore.int

		Returns a new rectangle with dx1 , dy1 , dx2 and dy2 added respectively to the existing coordinates of this rectangle.
		"""
		res = super(QRect,self).adjusted(x1,y1,x2,y2)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def contains(self,*args,**kwargs):
		"""
		contains(x,y,proper)
			x=QtCore.int
			y=QtCore.int
			proper=QtCore.bool

		contains(x,y)
			x=QtCore.int
			y=QtCore.int

		contains(r,proper=None)
			r=QtCore.QRect
			proper=QtCore.bool

		contains(p,proper=None)
			p=QtCore.QPoint
			proper=QtCore.bool

		This is an overloaded function.
		Returns true if the point (x , y ) is inside or on the edge of the rectangle, otherwise returns false
		If proper is true, this function only returns true if the point is entirely inside the rectangle(not on the edge).
		"""
		res = super(QRect,self).contains(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def intersect(self,r):
		"""
		intersect(r)
			r=QtCore.QRect

		Use intersected(rectangle ) instead.
		"""
		res = super(QRect,self).intersect(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def intersected(self,other):
		"""
		intersected(other)
			other=QtCore.QRect

		Returns the intersection of this rectangle and the given rectangle
		Note that r.intersected(s) is equivalent to r & s .
		"""
		res = super(QRect,self).intersected(other)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def intersects(self,r):
		"""
		intersects(r)
			r=QtCore.QRect

		Returns true if this rectangle intersects with the given rectangle (i.e., there is at least one pixel that is within both rectangles), otherwise returns false.
		The intersection rectangle can be retrieved using the PySide.QtCore.QRect.intersected() function.
		"""
		res = super(QRect,self).intersects(r)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def moveBottom(self,pos):
		"""
		moveBottom(pos)
			pos=QtCore.int

		Moves the rectangle vertically, leaving the rectangles bottom edge at the given y coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveBottom(pos)
		return res
	#----------------------------------------------------------------------
	def moveBottomLeft(self,p):
		"""
		moveBottomLeft(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the bottom-left corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveBottomLeft(p)
		return res
	#----------------------------------------------------------------------
	def moveBottomRight(self,p):
		"""
		moveBottomRight(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the bottom-right corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveBottomRight(p)
		return res
	#----------------------------------------------------------------------
	def moveCenter(self,p):
		"""
		moveCenter(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the center point at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveCenter(p)
		return res
	#----------------------------------------------------------------------
	def moveLeft(self,pos):
		"""
		moveLeft(pos)
			pos=QtCore.int

		Moves the rectangle horizontally, leaving the rectangles left edge at the given x coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveLeft(pos)
		return res
	#----------------------------------------------------------------------
	def moveRight(self,pos):
		"""
		moveRight(pos)
			pos=QtCore.int

		Moves the rectangle horizontally, leaving the rectangles right edge at the given x coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveRight(pos)
		return res
	#----------------------------------------------------------------------
	def moveTo(self,*args,**kwargs):
		"""
		moveTo(x,t)
			x=QtCore.int
			t=QtCore.int

		moveTo(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the top-left corner at the given position (x , y )
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveTo(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def moveTop(self,pos):
		"""
		moveTop(pos)
			pos=QtCore.int

		Moves the rectangle vertically, leaving the rectangles top edge at the given y coordinate
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveTop(pos)
		return res
	#----------------------------------------------------------------------
	def moveTopLeft(self,p):
		"""
		moveTopLeft(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the top-left corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveTopLeft(p)
		return res
	#----------------------------------------------------------------------
	def moveTopRight(self,p):
		"""
		moveTopRight(p)
			p=QtCore.QPoint

		Moves the rectangle, leaving the top-right corner at the given position
		The rectangles size is unchanged.
		"""
		res = super(QRect,self).moveTopRight(p)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__2):
		"""
		__ne__(arg__2)
			arg__2=QtCore.QRect


		"""
		res = super(QRect,self).__ne__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __and__(self,r):
		"""
		__and__(r)
			r=QtCore.QRect

		Returns the intersection of this rectangle and the given rectangle
		Returns an empty rectangle if there is no intersection.
		"""
		res = super(QRect,self).__and__(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def __iand__(self,r):
		"""
		__iand__(r)
			r=QtCore.QRect

		Intersects this rectangle with the given rectangle .
		"""
		res = super(QRect,self).__iand__(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__2):
		"""
		__eq__(arg__2)
			arg__2=QtCore.QRect


		"""
		res = super(QRect,self).__eq__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __or__(self,r):
		"""
		__or__(r)
			r=QtCore.QRect

		Returns the bounding rectangle of this rectangle and the given rectangle .
		"""
		res = super(QRect,self).__or__(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def __ior__(self,r):
		"""
		__ior__(r)
			r=QtCore.QRect

		Unites this rectangle with the given rectangle .
		"""
		res = super(QRect,self).__ior__(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def setBottom(self,pos):
		"""
		setBottom(pos)
			pos=QtCore.int

		Sets the bottom edge of the rectangle to the given y coordinate
		May change the height, but will never change the top edge of the rectangle.
		"""
		res = super(QRect,self).setBottom(pos)
		return res
	#----------------------------------------------------------------------
	def setBottomLeft(self,p):
		"""
		setBottomLeft(p)
			p=QtCore.QPoint

		Set the bottom-left corner of the rectangle to the given position
		May change the size, but will never change the top-right corner of the rectangle.
		"""
		res = super(QRect,self).setBottomLeft(p)
		return res
	#----------------------------------------------------------------------
	def setBottomRight(self,p):
		"""
		setBottomRight(p)
			p=QtCore.QPoint

		Set the bottom-right corner of the rectangle to the given position
		May change the size, but will never change the top-left corner of the rectangle.
		"""
		res = super(QRect,self).setBottomRight(p)
		return res
	#----------------------------------------------------------------------
	def setCoords(self,x1,y1,x2,y2):
		"""
		setCoords(x1,y1,x2,y2)
			x1=QtCore.int
			y1=QtCore.int
			x2=QtCore.int
			y2=QtCore.int

		Sets the coordinates of the rectangles top-left corner to (x1 , y1 ), and the coordinates of its bottom-right corner to (x2 , y2 ).
		"""
		res = super(QRect,self).setCoords(x1,y1,x2,y2)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,h):
		"""
		setHeight(h)
			h=QtCore.int

		Sets the height of the rectangle to the given height
		The bottom edge is changed, but not the top one.
		"""
		res = super(QRect,self).setHeight(h)
		return res
	#----------------------------------------------------------------------
	def setLeft(self,pos):
		"""
		setLeft(pos)
			pos=QtCore.int

		Sets the left edge of the rectangle to the given x coordinate
		May change the width, but will never change the right edge of the rectangle.
		Equivalent to PySide.QtCore.QRect.setX() .
		"""
		res = super(QRect,self).setLeft(pos)
		return res
	#----------------------------------------------------------------------
	def setRect(self,x,y,w,h):
		"""
		setRect(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		Sets the coordinates of the rectangles top-left corner to (x , y ), and its size to the given width and height .
		"""
		res = super(QRect,self).setRect(x,y,w,h)
		return res
	#----------------------------------------------------------------------
	def setRight(self,pos):
		"""
		setRight(pos)
			pos=QtCore.int

		Sets the right edge of the rectangle to the given x coordinate
		May change the width, but will never change the left edge of the rectangle.
		"""
		res = super(QRect,self).setRight(pos)
		return res
	#----------------------------------------------------------------------
	def setSize(self,s):
		"""
		setSize(s)
			s=QtCore.QSize

		Sets the size of the rectangle to the given size
		The top-left corner is not moved.
		"""
		res = super(QRect,self).setSize(s)
		return res
	#----------------------------------------------------------------------
	def setTop(self,pos):
		"""
		setTop(pos)
			pos=QtCore.int

		Sets the top edge of the rectangle to the given y coordinate
		May change the height, but will never change the bottom edge of the rectangle.
		Equivalent to PySide.QtCore.QRect.setY() .
		"""
		res = super(QRect,self).setTop(pos)
		return res
	#----------------------------------------------------------------------
	def setTopLeft(self,p):
		"""
		setTopLeft(p)
			p=QtCore.QPoint

		Set the top-left corner of the rectangle to the given position
		May change the size, but will never change the bottom-right corner of the rectangle.
		"""
		res = super(QRect,self).setTopLeft(p)
		return res
	#----------------------------------------------------------------------
	def setTopRight(self,p):
		"""
		setTopRight(p)
			p=QtCore.QPoint

		Set the top-right corner of the rectangle to the given position
		May change the size, but will never change the bottom-left corner of the rectangle.
		"""
		res = super(QRect,self).setTopRight(p)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,w):
		"""
		setWidth(w)
			w=QtCore.int

		Sets the width of the rectangle to the given width
		The right edge is changed, but not the left one.
		"""
		res = super(QRect,self).setWidth(w)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.int

		Sets the left edge of the rectangle to the given x coordinate
		May change the width, but will never change the right edge of the rectangle.
		Equivalent to PySide.QtCore.QRect.setLeft() .
		"""
		res = super(QRect,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.int

		Sets the top edge of the rectangle to the given y coordinate
		May change the height, but will never change the bottom edge of the rectangle.
		Equivalent to PySide.QtCore.QRect.setTop() .
		"""
		res = super(QRect,self).setY(y)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		translate(p)
			p=QtCore.QPoint

		Moves the rectangle dx along the x axis and dy along the y axis, relative to the current position
		Positive values move the rectangle to the right and down.
		"""
		res = super(QRect,self).translate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def translated(self,*args,**kwargs):
		"""
		translated(p)
			p=QtCore.QPoint

		translated(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		This is an overloaded function.
		Returns a copy of the rectangle that is translated offset
		PySide.QtCore.QPoint.x() along the x axis and offset
		PySide.QtCore.QPoint.y() along the y axis, relative to the current position.
		"""
		res = super(QRect,self).translated(*args,**kwargs)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def unite(self,r):
		"""
		unite(r)
			r=QtCore.QRect

		Use united(rectangle ) instead.
		"""
		res = super(QRect,self).unite(r)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def united(self,other):
		"""
		united(other)
			other=QtCore.QRect

		Returns the bounding rectangle of this rectangle and the given rectangle .
		"""
		res = super(QRect,self).united(other)
		isinstance(res,QtCore.QRect)
		return res
