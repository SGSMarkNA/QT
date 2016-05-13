from PySide import QtGui, QtCore

class QTextFrameFormat(QtGui.QTextFrameFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextFrameFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def border(self):
		"""
		Returns the width of the border in pixels.
		"""
		res = super(QTextFrameFormat,self).border()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def borderBrush(self):
		"""
		Returns the brush used for the frames border.
		"""
		res = super(QTextFrameFormat,self).borderBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def borderStyle(self):
		"""
		Returns the style of the frames border.
		"""
		res = super(QTextFrameFormat,self).borderStyle()
		isinstance(res,QtGui.QTextFrameFormat.BorderStyle)
		return res
	#----------------------------------------------------------------------
	def bottomMargin(self):
		"""
		Returns the width of the frames bottom margin in pixels.
		"""
		res = super(QTextFrameFormat,self).bottomMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the frames border rectangle.
		"""
		res = super(QTextFrameFormat,self).height()
		isinstance(res,QtGui.QTextLength)
		return res
	#----------------------------------------------------------------------
	def leftMargin(self):
		"""
		Returns the width of the frames left margin in pixels.
		"""
		res = super(QTextFrameFormat,self).leftMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def margin(self):
		"""
		Returns the width of the frames external margin in pixels.
		"""
		res = super(QTextFrameFormat,self).margin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def padding(self):
		"""
		Returns the width of the frames internal padding in pixels.
		"""
		res = super(QTextFrameFormat,self).padding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def pageBreakPolicy(self):
		"""
		Returns the currently set page break policy for the frame/table
		The default is QTextFormat.PageBreak_Auto .
		"""
		res = super(QTextFrameFormat,self).pageBreakPolicy()
		isinstance(res,QtGui.QTextFormat.PageBreakFlags)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		Returns the positioning policy for frames with this frame format.
		"""
		res = super(QTextFrameFormat,self).position()
		isinstance(res,QtGui.QTextFrameFormat.Position)
		return res
	#----------------------------------------------------------------------
	def rightMargin(self):
		"""
		Returns the width of the frames right margin in pixels.
		"""
		res = super(QTextFrameFormat,self).rightMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def topMargin(self):
		"""
		Returns the width of the frames top margin in pixels.
		"""
		res = super(QTextFrameFormat,self).topMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width of the frames border rectangle.
		"""
		res = super(QTextFrameFormat,self).width()
		isinstance(res,QtGui.QTextLength)
		return res
	#----------------------------------------------------------------------
	def setBorder(self,border):
		"""
		setBorder(border)
			border=QtCore.qreal

		Sets the width (in pixels) of the frames border.
		"""
		res = super(QTextFrameFormat,self).setBorder(border)
		return res
	#----------------------------------------------------------------------
	def setBorderBrush(self,brush):
		"""
		setBorderBrush(brush)
			brush=QtGui.QBrush

		Sets the brush used for the frames border.
		"""
		res = super(QTextFrameFormat,self).setBorderBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setBorderStyle(self,style):
		"""
		setBorderStyle(style)
			style=QtGui.QTextFrameFormat.BorderStyle

		Sets the style of the frames border.
		"""
		res = super(QTextFrameFormat,self).setBorderStyle(style)
		return res
	#----------------------------------------------------------------------
	def setBottomMargin(self,margin):
		"""
		setBottomMargin(margin)
			margin=QtCore.qreal

		Sets the frames bottom margin in pixels.
		"""
		res = super(QTextFrameFormat,self).setBottomMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,*args,**kwargs):
		"""
		setHeight(height)
			height=QtGui.QTextLength

		setHeight(height)
			height=QtCore.qreal

		Sets the frames height .
		"""
		res = super(QTextFrameFormat,self).setHeight(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setLeftMargin(self,margin):
		"""
		setLeftMargin(margin)
			margin=QtCore.qreal

		Sets the frames left margin in pixels.
		"""
		res = super(QTextFrameFormat,self).setLeftMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setMargin(self,margin):
		"""
		setMargin(margin)
			margin=QtCore.qreal

		Sets the frames margin in pixels
		This method also sets the left, right, top and bottom margins of the frame to the same value
		The individual margins override the general margin.
		"""
		res = super(QTextFrameFormat,self).setMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setPadding(self,padding):
		"""
		setPadding(padding)
			padding=QtCore.qreal

		Sets the width of the frames internal padding in pixels.
		"""
		res = super(QTextFrameFormat,self).setPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setPageBreakPolicy(self,flags):
		"""
		setPageBreakPolicy(flags)
			flags=QtGui.QTextFormat.PageBreakFlags


		"""
		res = super(QTextFrameFormat,self).setPageBreakPolicy(flags)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,f):
		"""
		setPosition(f)
			f=QtGui.QTextFrameFormat.Position

		Sets the policy for positioning frames with this frame format.
		"""
		res = super(QTextFrameFormat,self).setPosition(f)
		return res
	#----------------------------------------------------------------------
	def setRightMargin(self,margin):
		"""
		setRightMargin(margin)
			margin=QtCore.qreal

		Sets the frames right margin in pixels.
		"""
		res = super(QTextFrameFormat,self).setRightMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setTopMargin(self,margin):
		"""
		setTopMargin(margin)
			margin=QtCore.qreal

		Sets the frames top margin in pixels.
		"""
		res = super(QTextFrameFormat,self).setTopMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,*args,**kwargs):
		"""
		setWidth(width)
			width=QtCore.qreal

		setWidth(length)
			length=QtGui.QTextLength

		This is an overloaded function.
		Convenience method that sets the width of the frames border rectangles width to the specified fixed width .
		"""
		res = super(QTextFrameFormat,self).setWidth(*args,**kwargs)
		return res
