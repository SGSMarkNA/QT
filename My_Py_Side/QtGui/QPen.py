from PySide import QtGui, QtCore

class QPen(QtGui.QPen):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPen,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def brush(self):
		"""
		Returns the brush used to fill strokes generated with this pen.
		"""
		res = super(QPen,self).brush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def capStyle(self):
		"""
		Returns the pens cap style.
		"""
		res = super(QPen,self).capStyle()
		isinstance(res,QtCore.Qt.PenCapStyle)
		return res
	#----------------------------------------------------------------------
	def color(self):
		"""
		Returns the color of this pens brush.
		"""
		res = super(QPen,self).color()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def dashOffset(self):
		"""
		Returns the dash offset for the pen.
		"""
		res = super(QPen,self).dashOffset()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dashPattern(self):
		"""
		Returns the dash pattern of this pen.
		"""
		res = super(QPen,self).dashPattern()
		return res
	#----------------------------------------------------------------------
	def isCosmetic(self):
		"""
		Returns true if the pen is cosmetic; otherwise returns false.
		Cosmetic pens are used to draw strokes that have a constant width regardless of any transformations applied to the PySide.QtGui.QPainter they are used with
		Drawing a shape with a cosmetic pen ensures that its outline will have the same thickness at different scale factors.
		A zero width pen is cosmetic by default; pens with a non-zero width are non-cosmetic.
		"""
		res = super(QPen,self).isCosmetic()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSolid(self):
		"""
		Returns true if the pen has a solid fill, otherwise false.
		"""
		res = super(QPen,self).isSolid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def joinStyle(self):
		"""
		Returns the pens join style.
		"""
		res = super(QPen,self).joinStyle()
		isinstance(res,QtCore.Qt.PenJoinStyle)
		return res
	#----------------------------------------------------------------------
	def miterLimit(self):
		"""
		Returns the miter limit of the pen
		The miter limit is only relevant when the join style is set to Qt.MiterJoin .
		"""
		res = super(QPen,self).miterLimit()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the pen style.
		"""
		res = super(QPen,self).style()
		isinstance(res,QtCore.Qt.PenStyle)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the pen width with integer precision.
		"""
		res = super(QPen,self).width()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def widthF(self):
		"""
		Returns the pen width with floating point precision.
		"""
		res = super(QPen,self).widthF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,p):
		"""
		__ne__(p)
			p=QtGui.QPen

		Returns true if the pen is different from the given pen ; otherwise false
		Two pens are different if they have different styles, widths or colors.
		"""
		res = super(QPen,self).__ne__(p)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,p):
		"""
		__eq__(p)
			p=QtGui.QPen

		Returns true if the pen is equal to the given pen ; otherwise false
		Two pens are equal if they have equal styles, widths and colors.
		"""
		res = super(QPen,self).__eq__(p)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setBrush(self,brush):
		"""
		setBrush(brush)
			brush=QtGui.QBrush

		Sets the brush used to fill strokes generated with this pen to the given brush .
		"""
		res = super(QPen,self).setBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setCapStyle(self,pcs):
		"""
		setCapStyle(pcs)
			pcs=QtCore.Qt.PenCapStyle


		"""
		res = super(QPen,self).setCapStyle(pcs)
		return res
	#----------------------------------------------------------------------
	def setColor(self,color):
		"""
		setColor(color)
			color=QtGui.QColor

		Sets the color of this pens brush to the given color .
		"""
		res = super(QPen,self).setColor(color)
		return res
	#----------------------------------------------------------------------
	def setCosmetic(self,cosmetic):
		"""
		setCosmetic(cosmetic)
			cosmetic=QtCore.bool

		Sets this pen to cosmetic or non-cosmetic, depending on the value of cosmetic .
		"""
		res = super(QPen,self).setCosmetic(cosmetic)
		return res
	#----------------------------------------------------------------------
	def setDashOffset(self,doffset):
		"""
		setDashOffset(doffset)
			doffset=QtCore.qreal

		Sets the dash offset (the starting point on the dash pattern) for this pen to the offset specified
		The offset is measured in terms of the units used to specify the dash pattern.
		"""
		res = super(QPen,self).setDashOffset(doffset)
		return res
	#----------------------------------------------------------------------
	def setDashPattern(self,pattern):
		"""
		setDashPattern(pattern)
			pattern=unKnown


		"""
		res = super(QPen,self).setDashPattern(pattern)
		return res
	#----------------------------------------------------------------------
	def setJoinStyle(self,pcs):
		"""
		setJoinStyle(pcs)
			pcs=QtCore.Qt.PenJoinStyle


		"""
		res = super(QPen,self).setJoinStyle(pcs)
		return res
	#----------------------------------------------------------------------
	def setMiterLimit(self,limit):
		"""
		setMiterLimit(limit)
			limit=QtCore.qreal

		Sets the miter limit of this pen to the given limit .
		The miter limit describes how far a miter join can extend from the join point
		This is used to reduce artifacts between line joins where the lines are close to parallel.
		This value does only have effect when the pen style is set to Qt.MiterJoin
		The value is specified in units of the pens width, e.g
		a miter limit of 5 in width 10 is 50 pixels long
		The default miter limit is 2, i.e
		twice the pen width in pixels.
		"""
		res = super(QPen,self).setMiterLimit(limit)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,arg__1):
		"""
		setStyle(arg__1)
			arg__1=QtCore.Qt.PenStyle


		"""
		res = super(QPen,self).setStyle(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,width):
		"""
		setWidth(width)
			width=QtCore.int

		Sets the pen width to the given width in pixels with integer precision.
		A line width of zero indicates a cosmetic pen
		This means that the pen width is always drawn one pixel wide, independent of the transformation set on the painter.
		Setting a pen width with a negative value is not supported.
		"""
		res = super(QPen,self).setWidth(width)
		return res
	#----------------------------------------------------------------------
	def setWidthF(self,width):
		"""
		setWidthF(width)
			width=QtCore.qreal

		Sets the pen width to the given width in pixels with floating point precision.
		A line width of zero indicates a cosmetic pen
		This means that the pen width is always drawn one pixel wide, independent of the transformation on the painter.
		Setting a pen width with a negative value is not supported.
		"""
		res = super(QPen,self).setWidthF(width)
		return res
