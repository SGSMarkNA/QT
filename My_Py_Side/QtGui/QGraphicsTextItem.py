from PySide import QtGui, QtCore

class QGraphicsTextItem(QtGui.QGraphicsTextItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsTextItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def adjustSize(self):
		"""
		Adjusts the text item to a reasonable size.
		"""
		res = super(QGraphicsTextItem,self).adjustSize()
		return res
	#----------------------------------------------------------------------
	def defaultTextColor(self):
		"""
		Returns the default text color that is used to for unformatted text.
		"""
		res = super(QGraphicsTextItem,self).defaultTextColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the items text document.
		"""
		res = super(QGraphicsTextItem,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the items font, which is used to render the text.
		"""
		res = super(QGraphicsTextItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def openExternalLinks(self):
		"""

		"""
		res = super(QGraphicsTextItem,self).openExternalLinks()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def tabChangesFocus(self):
		"""
		Returns true if the Tab key will cause the widget to change focus; otherwise, false is returned.
		By default, this behavior is disabled, and this function will return false.
		"""
		res = super(QGraphicsTextItem,self).tabChangesFocus()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def textCursor(self):
		"""

		"""
		res = super(QGraphicsTextItem,self).textCursor()
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def textInteractionFlags(self):
		"""
		Returns the current text interaction flags.
		"""
		res = super(QGraphicsTextItem,self).textInteractionFlags()
		isinstance(res,QtCore.Qt.TextInteractionFlags)
		return res
	#----------------------------------------------------------------------
	def textWidth(self):
		"""
		Returns the text width.
		The width is calculated with the PySide.QtGui.QTextDocument that PySide.QtGui.QGraphicsTextItem keeps internally.
		"""
		res = super(QGraphicsTextItem,self).textWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def toHtml(self):
		"""
		Returns the items text converted to HTML, or an empty PySide.QtCore.QString if no text has been set.
		"""
		res = super(QGraphicsTextItem,self).toHtml()
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		Returns the items text converted to plain text, or an empty PySide.QtCore.QString if no text has been set.
		"""
		res = super(QGraphicsTextItem,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def setDefaultTextColor(self,c):
		"""
		setDefaultTextColor(c)
			c=QtGui.QColor

		Sets the color for unformatted text to col .
		"""
		res = super(QGraphicsTextItem,self).setDefaultTextColor(c)
		return res
	#----------------------------------------------------------------------
	def setDocument(self,document):
		"""
		setDocument(document)
			document=QtGui.QTextDocument

		Sets the text document document on the item.
		"""
		res = super(QGraphicsTextItem,self).setDocument(document)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font used to render the text item to font .
		"""
		res = super(QGraphicsTextItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setHtml(self,html):
		"""
		setHtml(html)
			html=unicode

		Sets the items text to text , assuming that text is HTML formatted
		If the item has keyboard input focus, this function will also call PySide.QtGui.QGraphicsItem.ensureVisible() to ensure that the text is visible in all viewports.
		"""
		res = super(QGraphicsTextItem,self).setHtml(html)
		return res
	#----------------------------------------------------------------------
	def setOpenExternalLinks(self,open):
		"""
		setOpenExternalLinks(open)
			open=QtCore.bool


		"""
		res = super(QGraphicsTextItem,self).setOpenExternalLinks(open)
		return res
	#----------------------------------------------------------------------
	def setPlainText(self,text):
		"""
		setPlainText(text)
			text=unicode

		Sets the items text to text
		If the item has keyboard input focus, this function will also call PySide.QtGui.QGraphicsItem.ensureVisible() to ensure that the text is visible in all viewports.
		"""
		res = super(QGraphicsTextItem,self).setPlainText(text)
		return res
	#----------------------------------------------------------------------
	def setTabChangesFocus(self,b):
		"""
		setTabChangesFocus(b)
			b=QtCore.bool

		If b is true, the Tab key will cause the widget to change focus; otherwise, the tab key will insert a tab into the document.
		In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain
		The default is false.
		"""
		res = super(QGraphicsTextItem,self).setTabChangesFocus(b)
		return res
	#----------------------------------------------------------------------
	def setTextCursor(self,cursor):
		"""
		setTextCursor(cursor)
			cursor=QtGui.QTextCursor


		"""
		res = super(QGraphicsTextItem,self).setTextCursor(cursor)
		return res
	#----------------------------------------------------------------------
	def setTextInteractionFlags(self,flags):
		"""
		setTextInteractionFlags(flags)
			flags=QtCore.Qt.TextInteractionFlags


		"""
		res = super(QGraphicsTextItem,self).setTextInteractionFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setTextWidth(self,width):
		"""
		setTextWidth(width)
			width=QtCore.qreal

		Sets the preferred width for the items text
		If the actual text is wider than the specified width then it will be broken into multiple lines.
		If width is set to -1 then the text will not be broken into multiple lines unless it is enforced through an explicit line break or a new paragraph.
		The default value is -1.
		Note that PySide.QtGui.QGraphicsTextItem keeps a PySide.QtGui.QTextDocument internally, which is used to calculate the text width.
		"""
		res = super(QGraphicsTextItem,self).setTextWidth(width)
		return res
