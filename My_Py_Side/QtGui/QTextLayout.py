from PySide import QtGui, QtCore

class QTextLayout(QtGui.QTextLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def additionalFormats(self):
		"""
		Returns the list of additional formats supported by the text layout.
		"""
		res = super(QTextLayout,self).additionalFormats()
		return res
	#----------------------------------------------------------------------
	def beginLayout(self):
		"""
		Begins the layout process.
		"""
		res = super(QTextLayout,self).beginLayout()
		return res
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		The smallest rectangle that contains all the lines in the layout.
		"""
		res = super(QTextLayout,self).boundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def cacheEnabled(self):
		"""
		Returns true if the complete layout information is cached; otherwise returns false.
		"""
		res = super(QTextLayout,self).cacheEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def clearAdditionalFormats(self):
		"""
		Clears the list of additional formats supported by the text layout.
		"""
		res = super(QTextLayout,self).clearAdditionalFormats()
		return res
	#----------------------------------------------------------------------
	def clearLayout(self):
		"""
		Clears the line information in the layout
		After having called this function, PySide.QtGui.QTextLayout.lineCount() returns 0.
		"""
		res = super(QTextLayout,self).clearLayout()
		return res
	#----------------------------------------------------------------------
	def createLine(self):
		"""
		Returns a new text line to be laid out if there is text to be inserted into the layout; otherwise returns an invalid text line.
		The text layout creates a new line object that starts after the last line in the layout, or at the beginning if the layout is empty
		The layout maintains an internal cursor, and each line is filled with text from the cursor position onwards when the QTextLine.setLineWidth() function is called.
		Once QTextLine.setLineWidth() is called, a new line can be created and filled with text
		Repeating this process will lay out the whole block of text contained in the PySide.QtGui.QTextLayout
		If there is no text left to be inserted into the layout, the PySide.QtGui.QTextLine returned will not be valid ( isValid() will return false).
		"""
		res = super(QTextLayout,self).createLine()
		isinstance(res,QtGui.QTextLine)
		return res
	#----------------------------------------------------------------------
	def endLayout(self):
		"""
		Ends the layout process.
		"""
		res = super(QTextLayout,self).endLayout()
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the current font that is used for the layout, or a default font if none is set.
		"""
		res = super(QTextLayout,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def lineCount(self):
		"""
		Returns the number of lines in this text layout.
		"""
		res = super(QTextLayout,self).lineCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def maximumWidth(self):
		"""
		The maximum width the layout could expand to; this is essentially the width of the entire text.
		"""
		res = super(QTextLayout,self).maximumWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def minimumWidth(self):
		"""
		The minimum width the layout needs
		This is the width of the layouts smallest non-breakable substring.
		"""
		res = super(QTextLayout,self).minimumWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		The global position of the layout
		This is independent of the bounding rectangle and of the layout process.
		"""
		res = super(QTextLayout,self).position()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def preeditAreaPosition(self):
		"""
		Returns the position of the area in the text layout that will be processed before editing occurs.
		"""
		res = super(QTextLayout,self).preeditAreaPosition()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def preeditAreaText(self):
		"""
		Returns the text that is inserted in the layout before editing occurs.
		"""
		res = super(QTextLayout,self).preeditAreaText()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the layouts text.
		"""
		res = super(QTextLayout,self).text()
		return res
	#----------------------------------------------------------------------
	def textOption(self):
		"""
		Returns the current text option used to control the layout process.
		"""
		res = super(QTextLayout,self).textOption()
		isinstance(res,QtGui.QTextOption)
		return res
	#----------------------------------------------------------------------
	def draw(self,p,pos,selections=None,clip=None):
		"""
		draw(p,pos,selections=None,clip=None)
			p=QtGui.QPainter
			pos=QtCore.QPointF
			selections=unKnown
			clip=QtCore.QRectF


		"""
		res = super(QTextLayout,self).draw(p,pos,selections,clip)
		return res
	#----------------------------------------------------------------------
	def drawCursor(self,*args,**kwargs):
		"""
		drawCursor(p,pos,cursorPosition,width)
			p=QtGui.QPainter
			pos=QtCore.QPointF
			cursorPosition=QtCore.int
			width=QtCore.int

		drawCursor(p,pos,cursorPosition)
			p=QtGui.QPainter
			pos=QtCore.QPointF
			cursorPosition=QtCore.int

		Draws a text cursor with the current pen and the specified width at the given position using the painter specified
		The corresponding position within the text is specified by cursorPosition .
		"""
		res = super(QTextLayout,self).drawCursor(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def isValidCursorPosition(self,pos):
		"""
		isValidCursorPosition(pos)
			pos=QtCore.int

		Returns true if position pos is a valid cursor position.
		In a Unicode context some positions in the text are not valid cursor positions, because the position is inside a Unicode surrogate or a grapheme cluster.
		A grapheme cluster is a sequence of two or more Unicode characters that form one indivisible entity on the screen
		For example the latin character ` .
		raw:: html &Auml;  can be represented in Unicode by two characters, `A (0x41), and the combining diaresis (0x308)
		A text cursor can only validly be positioned before or after these two characters, never between them since that wouldnt make sense
		In indic languages every syllable forms a grapheme cluster.
		"""
		res = super(QTextLayout,self).isValidCursorPosition(pos)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lineAt(self,i):
		"""
		lineAt(i)
			i=QtCore.int

		Returns the i -th line of text in this text layout.
		"""
		res = super(QTextLayout,self).lineAt(i)
		isinstance(res,QtGui.QTextLine)
		return res
	#----------------------------------------------------------------------
	def lineForTextPosition(self,pos):
		"""
		lineForTextPosition(pos)
			pos=QtCore.int

		Returns the line that contains the cursor position specified by pos .
		"""
		res = super(QTextLayout,self).lineForTextPosition(pos)
		isinstance(res,QtGui.QTextLine)
		return res
	#----------------------------------------------------------------------
	def nextCursorPosition(self,oldPos,mode=None):
		"""
		nextCursorPosition(oldPos,mode=None)
			oldPos=QtCore.int
			mode=QtGui.QTextLayout.CursorMode

		Returns the next valid cursor position after oldPos that respects the given cursor mode .
		"""
		res = super(QTextLayout,self).nextCursorPosition(oldPos,mode)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def previousCursorPosition(self,oldPos,mode=None):
		"""
		previousCursorPosition(oldPos,mode=None)
			oldPos=QtCore.int
			mode=QtGui.QTextLayout.CursorMode

		Returns the first valid cursor position before oldPos that respects the given cursor mode .
		"""
		res = super(QTextLayout,self).previousCursorPosition(oldPos,mode)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setAdditionalFormats(self,overrides):
		"""
		setAdditionalFormats(overrides)
			overrides=unKnown


		"""
		res = super(QTextLayout,self).setAdditionalFormats(overrides)
		return res
	#----------------------------------------------------------------------
	def setCacheEnabled(self,enable):
		"""
		setCacheEnabled(enable)
			enable=QtCore.bool

		Enables caching of the complete layout information if enable is true; otherwise disables layout caching
		Usually PySide.QtGui.QTextLayout throws most of the layouting information away after a call to PySide.QtGui.QTextLayout.endLayout() to reduce memory consumption
		If you however want to draw the laid out text directly afterwards enabling caching might speed up drawing significantly.
		"""
		res = super(QTextLayout,self).setCacheEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.int


		"""
		res = super(QTextLayout,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,f):
		"""
		setFont(f)
			f=QtGui.QFont

		Sets the layouts font to the given font
		The layout is invalidated and must be laid out again.
		"""
		res = super(QTextLayout,self).setFont(f)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,p):
		"""
		setPosition(p)
			p=QtCore.QPointF

		Moves the text layout to point p .
		"""
		res = super(QTextLayout,self).setPosition(p)
		return res
	#----------------------------------------------------------------------
	def setPreeditArea(self,position,text):
		"""
		setPreeditArea(position,text)
			position=QtCore.int
			text=unicode

		Sets the position and text of the area in the layout that is processed before editing occurs.
		"""
		res = super(QTextLayout,self).setPreeditArea(position,text)
		return res
	#----------------------------------------------------------------------
	def setText(self,string):
		"""
		setText(string)
			string=unicode

		Sets the layouts text to the given string
		The layout is invalidated and must be laid out again.
		Notice that when using this PySide.QtGui.QTextLayout as part of a PySide.QtGui.QTextDocument this method will have no effect.
		"""
		res = super(QTextLayout,self).setText(string)
		return res
	#----------------------------------------------------------------------
	def setTextOption(self,option):
		"""
		setTextOption(option)
			option=QtGui.QTextOption

		Sets the text option structure that controls the layout process to the given option .
		"""
		res = super(QTextLayout,self).setTextOption(option)
		return res
