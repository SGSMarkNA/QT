from PySide import QtGui, QtCore

class QTextLine(QtGui.QTextLine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextLine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def ascent(self):
		"""
		Returns the lines ascent.
		"""
		res = super(QTextLine,self).ascent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def descent(self):
		"""
		Returns the lines descent.
		"""
		res = super(QTextLine,self).descent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the lines height
		This is equal to PySide.QtGui.QTextLine.ascent() + PySide.QtGui.QTextLine.descent() + 1 if leading is not included
		If leading is included, this equals to PySide.QtGui.QTextLine.ascent() + PySide.QtGui.QTextLine.descent() + PySide.QtGui.QTextLine.leading() + 1.
		"""
		res = super(QTextLine,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def horizontalAdvance(self):
		"""
		Returns the horizontal advance of the text
		The advance of the text is the distance from its position to the next position at which text would naturally be drawn.
		By adding the advance to the position of the text line and using this as the position of a second text line, you will be able to position the two lines side-by-side without gaps in-between.
		"""
		res = super(QTextLine,self).horizontalAdvance()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this text line is valid; otherwise returns false.
		"""
		res = super(QTextLine,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def leading(self):
		"""
		Returns the lines leading.
		"""
		res = super(QTextLine,self).leading()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def leadingIncluded(self):
		"""
		Returns true if positive leading is included into the lines height; otherwise returns false.
		By default, leading is not included.
		"""
		res = super(QTextLine,self).leadingIncluded()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		Returns the position of the line in the text engine.
		"""
		res = super(QTextLine,self).lineNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def naturalTextRect(self):
		"""
		Returns the rectangle covered by the line.
		"""
		res = super(QTextLine,self).naturalTextRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def naturalTextWidth(self):
		"""
		Returns the width of the line that is occupied by text
		This is always <= to PySide.QtGui.QTextLine.width() , and is the minimum width that could be used by layout() without changing the line break position.
		"""
		res = super(QTextLine,self).naturalTextWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		Returns the lines position relative to the text layouts position.
		"""
		res = super(QTextLine,self).position()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the lines bounding rectangle.
		"""
		res = super(QTextLine,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def textLength(self):
		"""
		Returns the length of the text in the line.
		"""
		res = super(QTextLine,self).textLength()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def textStart(self):
		"""
		Returns the start of the line from the beginning of the string passed to the PySide.QtGui.QTextLayout .
		"""
		res = super(QTextLine,self).textStart()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the lines width as specified by the layout() function.
		"""
		res = super(QTextLine,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		Returns the lines x position.
		"""
		res = super(QTextLine,self).x()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		Returns the lines y position.
		"""
		res = super(QTextLine,self).y()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def cursorToX(self,cursorPos,edge=None):
		"""
		cursorToX(cursorPos,edge=None)
			cursorPos=QtCore.int
			edge=QtGui.QTextLine.Edge

		This is an overloaded function.
		"""
		res = super(QTextLine,self).cursorToX(cursorPos,edge)
		return res
	#----------------------------------------------------------------------
	def draw(self,p,point,selection=None):
		"""
		draw(p,point,selection=None)
			p=QtGui.QPainter
			point=QtCore.QPointF
			selection=QtGui.QTextLayout::FormatRange


		"""
		res = super(QTextLine,self).draw(p,point,selection)
		return res
	#----------------------------------------------------------------------
	def layout_helper(self,numGlyphs):
		"""
		layout_helper(numGlyphs)
			numGlyphs=QtCore.int


		"""
		res = super(QTextLine,self).layout_helper(numGlyphs)
		return res
	#----------------------------------------------------------------------
	def setLeadingIncluded(self,included):
		"""
		setLeadingIncluded(included)
			included=QtCore.bool

		Includes positive leading into the lines height if included is true; otherwise does not include leading.
		By default, leading is not included.
		Note that negative leading is ignored, it must be handled in the code using the text lines by letting the lines overlap.
		"""
		res = super(QTextLine,self).setLeadingIncluded(included)
		return res
	#----------------------------------------------------------------------
	def setLineWidth(self,width):
		"""
		setLineWidth(width)
			width=QtCore.qreal

		Lays out the line with the given width
		The line is filled from its starting position with as many characters as will fit into the line
		In case the text cannot be split at the end of the line, it will be filled with additional characters to the next whitespace or end of the text.
		"""
		res = super(QTextLine,self).setLineWidth(width)
		return res
	#----------------------------------------------------------------------
	def setNumColumns(self,*args,**kwargs):
		"""
		setNumColumns(columns)
			columns=QtCore.int

		setNumColumns(columns,alignmentWidth)
			columns=QtCore.int
			alignmentWidth=QtCore.qreal

		Lays out the line
		The line is filled from its starting position with as many characters as are specified by numColumns
		In case the text cannot be split until numColumns characters, the line will be filled with as many characters to the next whitespace or end of the text.
		"""
		res = super(QTextLine,self).setNumColumns(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,pos):
		"""
		setPosition(pos)
			pos=QtCore.QPointF

		Moves the line to position pos .
		"""
		res = super(QTextLine,self).setPosition(pos)
		return res
	#----------------------------------------------------------------------
	def xToCursor(self,x,edge=None):
		"""
		xToCursor(x,edge=None)
			x=QtCore.qreal
			edge=QtGui.QTextLine.CursorPosition

		Converts the x-coordinate x , to the nearest matching cursor position, depending on the cursor position type, cpos .
		"""
		res = super(QTextLine,self).xToCursor(x,edge)
		isinstance(res,int)
		return res
