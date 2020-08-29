from PySide import QtGui, QtCore

class QTextCharFormat(QtGui.QTextCharFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextCharFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def anchorHref(self):
		"""
		Returns the text formats hypertext link, or an empty string if none has been set.
		"""
		res = super(QTextCharFormat,self).anchorHref()
		return res
	#----------------------------------------------------------------------
	def anchorNames(self):
		"""
		Returns the anchor names associated with this text format, or an empty string list if none has been set
		If the anchor names are set, text with this format can be the destination of a hypertext link.
		"""
		res = super(QTextCharFormat,self).anchorNames()
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font for this character format.
		"""
		res = super(QTextCharFormat,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def fontCapitalization(self):
		"""
		Returns the current capitalization type of the font.
		"""
		res = super(QTextCharFormat,self).fontCapitalization()
		isinstance(res,QtGui.QFont.Capitalization)
		return res
	#----------------------------------------------------------------------
	def fontFamily(self):
		"""
		Returns the text formats font family.
		"""
		res = super(QTextCharFormat,self).fontFamily()
		return res
	#----------------------------------------------------------------------
	def fontFixedPitch(self):
		"""
		Returns true if the text formats font is fixed pitch; otherwise returns false.
		"""
		res = super(QTextCharFormat,self).fontFixedPitch()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontItalic(self):
		"""
		Returns true if the text formats font is italic; otherwise returns false.
		"""
		res = super(QTextCharFormat,self).fontItalic()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontKerning(self):
		"""
		Returns true if the font kerning is enabled.
		"""
		res = super(QTextCharFormat,self).fontKerning()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontLetterSpacing(self):
		"""
		Returns the current letter spacing percentage.
		"""
		res = super(QTextCharFormat,self).fontLetterSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def fontOverline(self):
		"""
		Returns true if the text formats font is overlined; otherwise returns false.
		"""
		res = super(QTextCharFormat,self).fontOverline()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontPointSize(self):
		"""
		Returns the font size used to display text in this format.
		"""
		res = super(QTextCharFormat,self).fontPointSize()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def fontStrikeOut(self):
		"""
		Returns true if the text formats font is struck out (has a horizontal line drawn through it); otherwise returns false.
		"""
		res = super(QTextCharFormat,self).fontStrikeOut()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontStyleHint(self):
		"""
		Returns the font style hint.
		"""
		res = super(QTextCharFormat,self).fontStyleHint()
		isinstance(res,QtGui.QFont.StyleHint)
		return res
	#----------------------------------------------------------------------
	def fontStyleStrategy(self):
		"""
		Returns the current font style strategy.
		"""
		res = super(QTextCharFormat,self).fontStyleStrategy()
		isinstance(res,QtGui.QFont.StyleStrategy)
		return res
	#----------------------------------------------------------------------
	def fontUnderline(self):
		"""
		Returns true if the text formats font is underlined; otherwise returns false.
		"""
		res = super(QTextCharFormat,self).fontUnderline()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fontWeight(self):
		"""
		Returns the text formats font weight.
		"""
		res = super(QTextCharFormat,self).fontWeight()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def fontWordSpacing(self):
		"""
		Returns the current word spacing value.
		"""
		res = super(QTextCharFormat,self).fontWordSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isAnchor(self):
		"""
		Returns true if the text is formatted as an anchor; otherwise returns false.
		"""
		res = super(QTextCharFormat,self).isAnchor()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def tableCellColumnSpan(self):
		"""
		If this character format is applied to characters in a table cell, this function returns the number of columns spanned by the text (this may be 1); otherwise it returns 1.
		"""
		res = super(QTextCharFormat,self).tableCellColumnSpan()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def tableCellRowSpan(self):
		"""
		If this character format is applied to characters in a table cell, this function returns the number of rows spanned by the text (this may be 1); otherwise it returns 1.
		"""
		res = super(QTextCharFormat,self).tableCellRowSpan()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def textOutline(self):
		"""
		Returns the pen used to draw the outlines of characters in this format.
		"""
		res = super(QTextCharFormat,self).textOutline()
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the tool tip that is displayed for a fragment of text.
		"""
		res = super(QTextCharFormat,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def underlineColor(self):
		"""
		Returns the color used to underline the characters with this format.
		"""
		res = super(QTextCharFormat,self).underlineColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def underlineStyle(self):
		"""
		Returns the style of underlining the text.
		"""
		res = super(QTextCharFormat,self).underlineStyle()
		isinstance(res,QtGui.QTextCharFormat.UnderlineStyle)
		return res
	#----------------------------------------------------------------------
	def verticalAlignment(self):
		"""
		Returns the vertical alignment used for characters with this format.
		"""
		res = super(QTextCharFormat,self).verticalAlignment()
		isinstance(res,QtGui.QTextCharFormat.VerticalAlignment)
		return res
	#----------------------------------------------------------------------
	def setAnchor(self,anchor):
		"""
		setAnchor(anchor)
			anchor=QtCore.bool

		If anchor is true, text with this format represents an anchor, and is formatted in the appropriate way; otherwise the text is formatted normally
		(Anchors are hyperlinks which are often shown underlined and in a different color from plain text.)
		The way the text is rendered is independent of whether or not the format has a valid anchor defined
		Use PySide.QtGui.QTextCharFormat.setAnchorHref() , and optionally PySide.QtGui.QTextCharFormat.setAnchorNames() to create a hypertext link.
		"""
		res = super(QTextCharFormat,self).setAnchor(anchor)
		return res
	#----------------------------------------------------------------------
	def setAnchorHref(self,value):
		"""
		setAnchorHref(value)
			value=unicode

		Sets the hypertext link for the text format to the given value
		This is typically a URL like http://example.com/index.html.
		The anchor will be displayed with the value as its display text; if you want to display different text call PySide.QtGui.QTextCharFormat.setAnchorNames() .
		To format the text as a hypertext link use PySide.QtGui.QTextCharFormat.setAnchor() .
		"""
		res = super(QTextCharFormat,self).setAnchorHref(value)
		return res
	#----------------------------------------------------------------------
	def setAnchorNames(self,names):
		"""
		setAnchorNames(names)
			names=list

		Sets the text formats anchor names
		For the anchor to work as a hyperlink, the destination must be set with PySide.QtGui.QTextCharFormat.setAnchorHref() and the anchor must be enabled with PySide.QtGui.QTextCharFormat.setAnchor() .
		"""
		res = super(QTextCharFormat,self).setAnchorNames(names)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the text formats font .
		"""
		res = super(QTextCharFormat,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setFontCapitalization(self,capitalization):
		"""
		setFontCapitalization(capitalization)
			capitalization=QtGui.QFont.Capitalization


		"""
		res = super(QTextCharFormat,self).setFontCapitalization(capitalization)
		return res
	#----------------------------------------------------------------------
	def setFontFamily(self,family):
		"""
		setFontFamily(family)
			family=unicode

		Sets the text formats font family .
		"""
		res = super(QTextCharFormat,self).setFontFamily(family)
		return res
	#----------------------------------------------------------------------
	def setFontFixedPitch(self,fixedPitch):
		"""
		setFontFixedPitch(fixedPitch)
			fixedPitch=QtCore.bool

		If fixedPitch is true, sets the text formats font to be fixed pitch; otherwise a non-fixed pitch font is used.
		"""
		res = super(QTextCharFormat,self).setFontFixedPitch(fixedPitch)
		return res
	#----------------------------------------------------------------------
	def setFontItalic(self,italic):
		"""
		setFontItalic(italic)
			italic=QtCore.bool

		If italic is true, sets the text formats font to be italic; otherwise the font will be non-italic.
		"""
		res = super(QTextCharFormat,self).setFontItalic(italic)
		return res
	#----------------------------------------------------------------------
	def setFontKerning(self,enable):
		"""
		setFontKerning(enable)
			enable=QtCore.bool

		Enables kerning for this font if enable is true; otherwise disables it.
		When kerning is enabled, glyph metrics do not add up anymore, even for Latin text
		In other words, the assumption that width(a) + width(b) is equal to width(ab) is not neccesairly true.
		"""
		res = super(QTextCharFormat,self).setFontKerning(enable)
		return res
	#----------------------------------------------------------------------
	def setFontLetterSpacing(self,spacing):
		"""
		setFontLetterSpacing(spacing)
			spacing=QtCore.qreal

		Sets the letter spacing of this format to the given spacing , in percent
		A value of 100 indicates default spacing; a value of 200 doubles the amount of space a letter takes.
		"""
		res = super(QTextCharFormat,self).setFontLetterSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setFontOverline(self,overline):
		"""
		setFontOverline(overline)
			overline=QtCore.bool

		If overline is true, sets the text formats font to be overlined; otherwise the font is displayed non-overlined.
		"""
		res = super(QTextCharFormat,self).setFontOverline(overline)
		return res
	#----------------------------------------------------------------------
	def setFontPointSize(self,size):
		"""
		setFontPointSize(size)
			size=QtCore.qreal

		Sets the text formats font size .
		"""
		res = super(QTextCharFormat,self).setFontPointSize(size)
		return res
	#----------------------------------------------------------------------
	def setFontStrikeOut(self,strikeOut):
		"""
		setFontStrikeOut(strikeOut)
			strikeOut=QtCore.bool

		If strikeOut is true, sets the text formats font with strike-out enabled (with a horizontal line through it); otherwise it is displayed without strikeout.
		"""
		res = super(QTextCharFormat,self).setFontStrikeOut(strikeOut)
		return res
	#----------------------------------------------------------------------
	def setFontStyleHint(self,hint,strategy=None):
		"""
		setFontStyleHint(hint,strategy=None)
			hint=QtGui.QFont.StyleHint
			strategy=QtGui.QFont.StyleStrategy


		"""
		res = super(QTextCharFormat,self).setFontStyleHint(hint,strategy)
		return res
	#----------------------------------------------------------------------
	def setFontStyleStrategy(self,strategy):
		"""
		setFontStyleStrategy(strategy)
			strategy=QtGui.QFont.StyleStrategy


		"""
		res = super(QTextCharFormat,self).setFontStyleStrategy(strategy)
		return res
	#----------------------------------------------------------------------
	def setFontUnderline(self,underline):
		"""
		setFontUnderline(underline)
			underline=QtCore.bool

		If underline is true, sets the text formats font to be underlined; otherwise it is displayed non-underlined.
		"""
		res = super(QTextCharFormat,self).setFontUnderline(underline)
		return res
	#----------------------------------------------------------------------
	def setFontWeight(self,weight):
		"""
		setFontWeight(weight)
			weight=QtCore.int

		Sets the text formats font weight to weight .
		"""
		res = super(QTextCharFormat,self).setFontWeight(weight)
		return res
	#----------------------------------------------------------------------
	def setFontWordSpacing(self,spacing):
		"""
		setFontWordSpacing(spacing)
			spacing=QtCore.qreal

		Sets the word spacing of this format to the given spacing , in pixels.
		"""
		res = super(QTextCharFormat,self).setFontWordSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setTableCellColumnSpan(self,tableCellColumnSpan):
		"""
		setTableCellColumnSpan(tableCellColumnSpan)
			tableCellColumnSpan=QtCore.int

		If this character format is applied to characters in a table cell, the cell will span tableCellColumnSpan columns.
		"""
		res = super(QTextCharFormat,self).setTableCellColumnSpan(tableCellColumnSpan)
		return res
	#----------------------------------------------------------------------
	def setTableCellRowSpan(self,tableCellRowSpan):
		"""
		setTableCellRowSpan(tableCellRowSpan)
			tableCellRowSpan=QtCore.int

		If this character format is applied to characters in a table cell, the cell will span tableCellRowSpan rows.
		"""
		res = super(QTextCharFormat,self).setTableCellRowSpan(tableCellRowSpan)
		return res
	#----------------------------------------------------------------------
	def setTextOutline(self,pen):
		"""
		setTextOutline(pen)
			pen=QtGui.QPen

		Sets the pen used to draw the outlines of characters to the given pen .
		"""
		res = super(QTextCharFormat,self).setTextOutline(pen)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,tip):
		"""
		setToolTip(tip)
			tip=unicode

		Sets the tool tip for a fragment of text to the given text .
		"""
		res = super(QTextCharFormat,self).setToolTip(tip)
		return res
	#----------------------------------------------------------------------
	def setUnderlineColor(self,color):
		"""
		setUnderlineColor(color)
			color=QtGui.QColor

		Sets the underline color used for the characters with this format to the color specified.
		"""
		res = super(QTextCharFormat,self).setUnderlineColor(color)
		return res
	#----------------------------------------------------------------------
	def setUnderlineStyle(self,style):
		"""
		setUnderlineStyle(style)
			style=QtGui.QTextCharFormat.UnderlineStyle

		Sets the style of underlining the text to style .
		"""
		res = super(QTextCharFormat,self).setUnderlineStyle(style)
		return res
	#----------------------------------------------------------------------
	def setVerticalAlignment(self,alignment):
		"""
		setVerticalAlignment(alignment)
			alignment=QtGui.QTextCharFormat.VerticalAlignment

		Sets the vertical alignment used for the characters with this format to the alignment specified.
		"""
		res = super(QTextCharFormat,self).setVerticalAlignment(alignment)
		return res
