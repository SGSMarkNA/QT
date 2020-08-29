from PySide import QtGui, QtCore

class QFontMetricsF(QtGui.QFontMetricsF):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontMetricsF,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def ascent(self):
		"""
		Returns the ascent of the font.
		The ascent of a font is the distance from the baseline to the highest position characters extend to
		In practice, some font designers break this rule, e.g
		when they put more than one accent on top of a character, or to accommodate an unusual character in an exotic language, so it is possible (though rare) that this value will be too small.
		"""
		res = super(QFontMetricsF,self).ascent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def averageCharWidth(self):
		"""
		Returns the average width of glyphs in the font.
		"""
		res = super(QFontMetricsF,self).averageCharWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def descent(self):
		"""
		Returns the descent of the font.
		The descent is the distance from the base line to the lowest point characters extend to
		(Note that this is different from X, which adds 1 pixel.) In practice, some font designers break this rule, e.g
		to accommodate an unusual character in an exotic language, so it is possible (though rare) that this value will be too small.
		"""
		res = super(QFontMetricsF,self).descent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the font.
		This is always equal to PySide.QtGui.QFontMetricsF.ascent() + PySide.QtGui.QFontMetricsF.descent() +1 (the 1 is for the base line).
		"""
		res = super(QFontMetricsF,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def leading(self):
		"""
		Returns the leading of the font.
		This is the natural inter-line spacing.
		"""
		res = super(QFontMetricsF,self).leading()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lineSpacing(self):
		"""
		Returns the distance from one base line to the next.
		This value is always equal to PySide.QtGui.QFontMetricsF.leading() + PySide.QtGui.QFontMetricsF.height() .
		"""
		res = super(QFontMetricsF,self).lineSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def lineWidth(self):
		"""
		Returns the width of the underline and strikeout lines, adjusted for the point size of the font.
		"""
		res = super(QFontMetricsF,self).lineWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def maxWidth(self):
		"""
		Returns the width of the widest character in the font.
		"""
		res = super(QFontMetricsF,self).maxWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def minLeftBearing(self):
		"""
		Returns the minimum left bearing of the font.
		This is the smallest leftBearing(char) of all characters in the font.
		Note that this function can be very slow if the font is large.
		"""
		res = super(QFontMetricsF,self).minLeftBearing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def minRightBearing(self):
		"""
		Returns the minimum right bearing of the font.
		This is the smallest rightBearing(char) of all characters in the font.
		Note that this function can be very slow if the font is large.
		"""
		res = super(QFontMetricsF,self).minRightBearing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def overlinePos(self):
		"""
		Returns the distance from the base line to where an overline should be drawn.
		"""
		res = super(QFontMetricsF,self).overlinePos()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def strikeOutPos(self):
		"""
		Returns the distance from the base line to where the strikeout line should be drawn.
		"""
		res = super(QFontMetricsF,self).strikeOutPos()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def underlinePos(self):
		"""
		Returns the distance from the base line to where an underscore should be drawn.
		"""
		res = super(QFontMetricsF,self).underlinePos()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def xHeight(self):
		"""
		Returns the x height of the font
		This is often but not always the same as the height of the character x.
		"""
		res = super(QFontMetricsF,self).xHeight()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def boundingRect(self,*args,**kwargs):
		"""
		boundingRect(r,flags,string,tabstops=None,tabarray=None)
			r=QtCore.QRectF
			flags=QtCore.int
			string=unicode
			tabstops=QtCore.int
			tabarray=QtCore.int

		boundingRect(string)
			string=unicode

		This is an overloaded function.
		Returns the bounding rectangle of the characters in the given text
		This is the set of pixels the text would cover if drawn when constrained to the bounding rectangle specified by rect .
		The flags argument is the bitwise OR of the following flags:
		Qt.Horizontal alignment defaults to Qt.AlignLeft and vertical alignment defaults to Qt.AlignTop .
		If several of the horizontal or several of the vertical alignment flags are set, the resulting alignment is undefined.
		These flags are defined in Qt.AlignmentFlag .
		If Qt.TextExpandTabs is set in flags , the following behavior is used to interpret tab characters in the text:
		Note that the bounding rectangle may extend to the left of (0, 0), e.g
		for italicized fonts.
		Newline characters are processed as line breaks.
		Despite the different actual character heights, the heights of the bounding rectangles of Yes and yes are the same.
		The bounding rectangle returned by this function is somewhat larger than that calculated by the simpler PySide.QtGui.QFontMetricsF.boundingRect() function
		This function uses the maximum left and right font bearings as is necessary for multi-line text to align correctly
		Also, fontHeight() and PySide.QtGui.QFontMetricsF.lineSpacing() are used to calculate the height, rather than individual character heights.
		"""
		res = super(QFontMetricsF,self).boundingRect(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def boundingRectChar(self,arg__1):
		"""
		boundingRectChar(arg__1)
			arg__1=QtCore.QChar

		Returns the bounding rectangle of the character ch relative to the left-most point on the base line.
		Note that the bounding rectangle may extend to the left of (0, 0), e.g
		for italicized fonts, and that the text output may cover all pixels in the bounding rectangle.
		Note that the rectangle usually extends both above and below the base line.
		"""
		res = super(QFontMetricsF,self).boundingRectChar(arg__1)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def elidedText(self,text,mode,width,flags=None):
		"""
		elidedText(text,mode,width,flags=None)
			text=unicode
			mode=QtCore.Qt.TextElideMode
			width=QtCore.qreal
			flags=QtCore.int


		"""
		res = super(QFontMetricsF,self).elidedText(text,mode,width,flags)
		return res
	#----------------------------------------------------------------------
	def inFont(self,arg__1):
		"""
		inFont(arg__1)
			arg__1=QtCore.QChar

		Returns true if character ch is a valid character in the font; otherwise returns false.
		"""
		res = super(QFontMetricsF,self).inFont(arg__1)
		isinstance(res,bool)
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
		res = super(QFontMetricsF,self).leftBearing(arg__1)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QFontMetricsF

		This is an overloaded function.
		Returns true if the font metrics are not equal to the other font metrics; otherwise returns false.
		"""
		res = super(QFontMetricsF,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QFontMetricsF

		This is an overloaded function.
		Returns true if the font metrics are equal to the other font metrics; otherwise returns false.
		Two font metrics are considered equal if they were constructed from the same PySide.QtGui.QFont and the paint devices they were constructed for are considered to be compatible.
		"""
		res = super(QFontMetricsF,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rightBearing(self,arg__1):
		"""
		rightBearing(arg__1)
			arg__1=QtCore.QChar

		Returns the right bearing of character ch in the font.
		The right bearing is the left-ward distance of the right-most pixel of the character from the logical origin of a subsequent character
		This value is negative if the pixels of the character extend to the right of the PySide.QtGui.QFontMetricsF.width() of the character.
		See PySide.QtGui.QFontMetricsF.width() for a graphical description of this metric.
		"""
		res = super(QFontMetricsF,self).rightBearing(arg__1)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def size(self,flags,str,tabstops=None,tabarray=None):
		"""
		size(flags,str,tabstops=None,tabarray=None)
			flags=QtCore.int
			str=unicode
			tabstops=QtCore.int
			tabarray=QtCore.int

		Returns the size in pixels of the characters in the given text .
		The flags argument is the bitwise OR of the following flags:
		These flags are defined in Qt.TextFlags .
		If Qt.TextExpandTabs is set in flags , the following behavior is used to interpret tab characters in the text:
		Newline characters are processed as line breaks.
		Note: Despite the different actual character heights, the heights of the bounding rectangles of Yes and yes are the same.
		"""
		res = super(QFontMetricsF,self).size(flags,str,tabstops,tabarray)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def tightBoundingRect(self,text):
		"""
		tightBoundingRect(text)
			text=unicode

		Returns a tight bounding rectangle around the characters in the string specified by text
		The bounding rectangle always covers at least the set of pixels the text would cover if drawn at (0, 0).
		Note that the bounding rectangle may extend to the left of (0, 0), e.g
		for italicized fonts, and that the width of the returned rectangle might be different than what the PySide.QtGui.QFontMetricsF.width() method returns.
		If you want to know the advance width of the string (to layout a set of strings next to each other), use PySide.QtGui.QFontMetricsF.width() instead.
		Newline characters are processed as normal characters, not as linebreaks.
		"""
		res = super(QFontMetricsF,self).tightBoundingRect(text)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def width(self,string):
		"""
		width(string)
			string=unicode

		Returns the width in pixels of the characters in the given text .
		Note that this value is not equal to the width returned by PySide.QtGui.QFontMetricsF.boundingRect()
		PySide.QtGui.QFontMetricsF.width() because PySide.QtGui.QFontMetricsF.boundingRect() returns a rectangle describing the pixels this string will cover whereas PySide.QtGui.QFontMetricsF.width() returns the distance to where the next string should be drawn.
		"""
		res = super(QFontMetricsF,self).width(string)
		isinstance(res,QtCore.qreal)
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
		The central dark rectangles cover the logical PySide.QtGui.QFontMetricsF.width() of each character
		The outer pale rectangles cover the PySide.QtGui.QFontMetricsF.leftBearing() and PySide.QtGui.QFontMetricsF.rightBearing() of each character
		Notice that the bearings of f in this particular font are both negative, while the bearings of o are both positive.
		"""
		res = super(QFontMetricsF,self).widthChar(arg__1)
		isinstance(res,QtCore.qreal)
		return res
