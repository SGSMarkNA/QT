from PySide import QtGui, QtCore

class QFontMetrics(QtGui.QFontMetrics):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontMetrics,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def ascent(self):
		"""
		Returns the ascent of the font.
		The ascent of a font is the distance from the baseline to the highest position characters extend to
		In practice, some font designers break this rule, e.g
		when they put more than one accent on top of a character, or to accommodate an unusual character in an exotic language, so it is possible (though rare) that this value will be too small.
		"""
		res = super(QFontMetrics,self).ascent()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def averageCharWidth(self):
		"""
		Returns the average width of glyphs in the font.
		"""
		res = super(QFontMetrics,self).averageCharWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def descent(self):
		"""
		Returns the descent of the font.
		The descent is the distance from the base line to the lowest point characters extend to
		In practice, some font designers break this rule, e.g
		to accommodate an unusual character in an exotic language, so it is possible (though rare) that this value will be too small.
		"""
		res = super(QFontMetrics,self).descent()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the font.
		This is always equal to PySide.QtGui.QFontMetrics.ascent() + PySide.QtGui.QFontMetrics.descent() +1 (the 1 is for the base line).
		"""
		res = super(QFontMetrics,self).height()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def leading(self):
		"""
		Returns the leading of the font.
		This is the natural inter-line spacing.
		"""
		res = super(QFontMetrics,self).leading()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def lineSpacing(self):
		"""
		Returns the distance from one base line to the next.
		This value is always equal to PySide.QtGui.QFontMetrics.leading() + PySide.QtGui.QFontMetrics.height() .
		"""
		res = super(QFontMetrics,self).lineSpacing()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def lineWidth(self):
		"""
		Returns the width of the underline and strikeout lines, adjusted for the point size of the font.
		"""
		res = super(QFontMetrics,self).lineWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maxWidth(self):
		"""
		Returns the width of the widest character in the font.
		"""
		res = super(QFontMetrics,self).maxWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minLeftBearing(self):
		"""
		Returns the minimum left bearing of the font.
		This is the smallest leftBearing(char) of all characters in the font.
		Note that this function can be very slow if the font is large.
		"""
		res = super(QFontMetrics,self).minLeftBearing()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minRightBearing(self):
		"""
		Returns the minimum right bearing of the font.
		This is the smallest rightBearing(char) of all characters in the font.
		Note that this function can be very slow if the font is large.
		"""
		res = super(QFontMetrics,self).minRightBearing()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def overlinePos(self):
		"""
		Returns the distance from the base line to where an overline should be drawn.
		"""
		res = super(QFontMetrics,self).overlinePos()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def strikeOutPos(self):
		"""
		Returns the distance from the base line to where the strikeout line should be drawn.
		"""
		res = super(QFontMetrics,self).strikeOutPos()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def underlinePos(self):
		"""
		Returns the distance from the base line to where an underscore should be drawn.
		"""
		res = super(QFontMetrics,self).underlinePos()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def xHeight(self):
		"""
		Returns the x height of the font
		This is often but not always the same as the height of the character x.
		"""
		res = super(QFontMetrics,self).xHeight()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def boundingRect(self,*args,**kwargs):
		"""
		boundingRect(r,flags,text,tabstops=None,tabarray=None)
			r=QtCore.QRect
			flags=QtCore.int
			text=unicode
			tabstops=QtCore.int
			tabarray=QtCore.int

		boundingRect(text)
			text=unicode

		boundingRect(x,y,w,h,flags,text,tabstops=None,tabarray=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			flags=QtCore.int
			text=unicode
			tabstops=QtCore.int
			tabarray=QtCore.int

		This is an overloaded function.
		Returns the bounding rectangle of the characters in the string specified by text , which is the set of pixels the text would cover if drawn at (0, 0)
		The drawing, and hence the bounding rectangle, is constrained to the rectangle rect .
		The flags argument is the bitwise OR of the following flags:
		Qt.Horizontal alignment defaults to Qt.AlignLeft and vertical alignment defaults to Qt.AlignTop .
		If several of the horizontal or several of the vertical alignment flags are set, the resulting alignment is undefined.
		If Qt.TextExpandTabs is set in flags , then: if tabArray is non-null, it specifies a 0-terminated sequence of pixel-positions for tabs; otherwise if tabStops is non-zero, it is used as the tab spacing (in pixels).
		Note that the bounding rectangle may extend to the left of (0, 0), e.g
		for italicized fonts, and that the text output may cover all pixels in the bounding rectangle.
		Newline characters are processed as linebreaks.
		Despite the different actual character heights, the heights of the bounding rectangles of Yes and yes are the same.
		The bounding rectangle returned by this function is somewhat larger than that calculated by the simpler PySide.QtGui.QFontMetrics.boundingRect() function
		This function uses the maximum left and right font bearings as is necessary for multi-line text to align correctly
		Also, fontHeight() and PySide.QtGui.QFontMetrics.lineSpacing() are used to calculate the height, rather than individual character heights.
		"""
		res = super(QFontMetrics,self).boundingRect(*args,**kwargs)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def boundingRectChar(self,arg__1):
		"""
		boundingRectChar(arg__1)
			arg__1=QtCore.QChar

		Returns the rectangle that is covered by ink if character ch were to be drawn at the origin of the coordinate system.
		Note that the bounding rectangle may extend to the left of (0, 0) (e.g., for italicized fonts), and that the text output may cover all pixels in the bounding rectangle
		For a space character the rectangle will usually be empty.
		Note that the rectangle usually extends both above and below the base line.
		"""
		res = super(QFontMetrics,self).boundingRectChar(arg__1)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def charWidth(self,str,pos):
		"""
		charWidth(str,pos)
			str=unicode
			pos=QtCore.int

		Returns the width of the character at position pos in the string text .
		The whole string is needed, as the glyph drawn may change depending on the context (the letter before and after the current one) for some languages (e.g
		Arabic).
		This function also takes non spacing marks and ligatures into account.
		"""
		res = super(QFontMetrics,self).charWidth(str,pos)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def elidedText(self,text,mode,width,flags=None):
		"""
		elidedText(text,mode,width,flags=None)
			text=unicode
			mode=QtCore.Qt.TextElideMode
			width=QtCore.int
			flags=QtCore.int


		"""
		res = super(QFontMetrics,self).elidedText(text,mode,width,flags)
		return res
	#----------------------------------------------------------------------
	def inFont(self,arg__1):
		"""
		inFont(arg__1)
			arg__1=QtCore.QChar

		Returns true if character ch is a valid character in the font; otherwise returns false.
		"""
		res = super(QFontMetrics,self).inFont(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def leftBearing(self,arg__1):
		"""
		leftBearing(arg__1)
			arg__1=QtCore.QChar

		Returns the left bearing of character ch in the font.
		The left bearing is the right-ward distance of the left-most pixel of the character from the logical origin of the character
		This value is negative if the pixels of the character extend to the left of the logical origin.
		See width( PySide.QtCore.QChar ) for a graphical description of this metric.
		"""
		res = super(QFontMetrics,self).leftBearing(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QFontMetrics

		Returns true if other is not equal to this object; otherwise returns false.
		Two font metrics are considered equal if they were constructed from the same PySide.QtGui.QFont and the paint devices they were constructed for are considered compatible.
		"""
		res = super(QFontMetrics,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QFontMetrics

		This is an overloaded function.
		Returns true if other is equal to this object; otherwise returns false.
		Two font metrics are considered equal if they were constructed from the same PySide.QtGui.QFont and the paint devices they were constructed for are considered compatible.
		"""
		res = super(QFontMetrics,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rightBearing(self,arg__1):
		"""
		rightBearing(arg__1)
			arg__1=QtCore.QChar

		Returns the right bearing of character ch in the font.
		The right bearing is the left-ward distance of the right-most pixel of the character from the logical origin of a subsequent character
		This value is negative if the pixels of the character extend to the right of the PySide.QtGui.QFontMetrics.width() of the character.
		See PySide.QtGui.QFontMetrics.width() for a graphical description of this metric.
		"""
		res = super(QFontMetrics,self).rightBearing(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def size(self,flags,str,tabstops=None,tabarray=None):
		"""
		size(flags,str,tabstops=None,tabarray=None)
			flags=QtCore.int
			str=unicode
			tabstops=QtCore.int
			tabarray=QtCore.int

		Returns the size in pixels of text .
		The flags argument is the bitwise OR of the following flags:
		If Qt.TextExpandTabs is set in flags , then: if tabArray is non-null, it specifies a 0-terminated sequence of pixel-positions for tabs; otherwise if tabStops is non-zero, it is used as the tab spacing (in pixels).
		Newline characters are processed as linebreaks.
		Despite the different actual character heights, the heights of the bounding rectangles of Yes and yes are the same.
		"""
		res = super(QFontMetrics,self).size(flags,str,tabstops,tabarray)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def tightBoundingRect(self,text):
		"""
		tightBoundingRect(text)
			text=unicode

		Returns a tight bounding rectangle around the characters in the string specified by text
		The bounding rectangle always covers at least the set of pixels the text would cover if drawn at (0, 0).
		Note that the bounding rectangle may extend to the left of (0, 0), e.g
		for italicized fonts, and that the width of the returned rectangle might be different than what the PySide.QtGui.QFontMetrics.width() method returns.
		If you want to know the advance width of the string (to layout a set of strings next to each other), use PySide.QtGui.QFontMetrics.width() instead.
		Newline characters are processed as normal characters, not as linebreaks.
		"""
		res = super(QFontMetrics,self).tightBoundingRect(text)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def width(self,*args,**kwargs):
		"""
		width(arg__1,len,flags)
			arg__1=unicode
			len=QtCore.int
			flags=QtCore.int

		width(arg__1,len=None)
			arg__1=unicode
			len=QtCore.int


		"""
		res = super(QFontMetrics,self).width(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def widthChar(self,arg__1):
		"""
		widthChar(arg__1)
			arg__1=QtCore.QChar

		This is an overloaded function.
		Returns the logical width of character ch in pixels
		This is a distance appropriate for drawing a subsequent character after ch .
		Some of the metrics are described in the image to the right
		The central dark rectangles cover the logical PySide.QtGui.QFontMetrics.width() of each character
		The outer pale rectangles cover the PySide.QtGui.QFontMetrics.leftBearing() and PySide.QtGui.QFontMetrics.rightBearing() of each character
		Notice that the bearings of f in this particular font are both negative, while the bearings of o are both positive.
		"""
		res = super(QFontMetrics,self).widthChar(arg__1)
		isinstance(res,QtCore.int)
		return res
