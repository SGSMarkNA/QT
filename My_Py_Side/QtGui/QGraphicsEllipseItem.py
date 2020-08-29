from PySide import QtGui, QtCore

class QGraphicsEllipseItem(QtGui.QGraphicsEllipseItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsEllipseItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the items ellipse geometry as a PySide.QtCore.QRectF .
		"""
		res = super(QGraphicsEllipseItem,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def spanAngle(self):
		"""
		Returns the span angle of an ellipse segment in 16ths of a degree
		This angle is used together with PySide.QtGui.QGraphicsEllipseItem.startAngle() for representing an ellipse segment (a pie)
		By default, this function returns 5760 (360 * 16, a full ellipse).
		"""
		res = super(QGraphicsEllipseItem,self).spanAngle()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def startAngle(self):
		"""
		Returns the start angle for an ellipse segment in 16ths of a degree
		This angle is used together with PySide.QtGui.QGraphicsEllipseItem.spanAngle() for representing an ellipse segment (a pie)
		By default, the start angle is 0.
		"""
		res = super(QGraphicsEllipseItem,self).startAngle()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setRect(self,*args,**kwargs):
		"""
		setRect(rect)
			rect=QtCore.QRectF

		setRect(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		Sets the items ellipse geometry to rect
		The rectangles left edge defines the left edge of the ellipse, and the rectangles top edge describes the top of the ellipse
		The height and width of the rectangle describe the height and width of the ellipse.
		"""
		res = super(QGraphicsEllipseItem,self).setRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSpanAngle(self,angle):
		"""
		setSpanAngle(angle)
			angle=QtCore.int

		Sets the span angle for an ellipse segment to angle , which is in 16ths of a degree
		This angle is used together with PySide.QtGui.QGraphicsEllipseItem.startAngle() to represent an ellipse segment (a pie)
		By default, the span angle is 5760 (360 * 16, a full ellipse).
		"""
		res = super(QGraphicsEllipseItem,self).setSpanAngle(angle)
		return res
	#----------------------------------------------------------------------
	def setStartAngle(self,angle):
		"""
		setStartAngle(angle)
			angle=QtCore.int

		Sets the start angle for an ellipse segment to angle , which is in 16ths of a degree
		This angle is used together with PySide.QtGui.QGraphicsEllipseItem.spanAngle() for representing an ellipse segment (a pie)
		By default, the start angle is 0.
		"""
		res = super(QGraphicsEllipseItem,self).setStartAngle(angle)
		return res
