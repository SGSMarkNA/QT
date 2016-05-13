from PySide import QtGui, QtCore

class QLabel(QtGui.QLabel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLabel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the labels contents.
		By default, the contents of the label are left-aligned and vertically-centered.
		"""
		res = super(QLabel,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def buddy(self):
		"""
		Returns this labels buddy, or 0 if no buddy is currently set.
		"""
		res = super(QLabel,self).buddy()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def hasScaledContents(self):
		"""
		This property holds whether the label will scale its contents to fill all available space..
		When enabled and the label shows a pixmap, it will scale the pixmap to fill the available space.
		This propertys default is false.
		"""
		res = super(QLabel,self).hasScaledContents()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasSelectedText(self):
		"""
		This property holds whether there is any text selected.
		PySide.QtGui.QLabel.hasSelectedText() returns true if some or all of the text has been selected by the user; otherwise returns false.
		By default, this property is false.
		"""
		res = super(QLabel,self).hasSelectedText()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def indent(self):
		"""
		This property holds the labels text indent in pixels.
		If a label displays text, the indent applies to the left edge if PySide.QtGui.QLabel.alignment() is Qt.AlignLeft , to the right edge if PySide.QtGui.QLabel.alignment() is Qt.AlignRight , to the top edge if PySide.QtGui.QLabel.alignment() is Qt.AlignTop , and to to the bottom edge if PySide.QtGui.QLabel.alignment() is Qt.AlignBottom .
		If indent is negative, or if no indent has been set, the label computes the effective indent as follows: If PySide.QtGui.QFrame.frameWidth() is 0, the effective indent becomes 0
		If PySide.QtGui.QFrame.frameWidth() is greater than 0, the effective indent becomes half the width of the x character of the widgets current PySide.QtGui.QWidget.font() .
		By default, the indent is -1, meaning that an effective indent is calculating in the manner described above.
		"""
		res = super(QLabel,self).indent()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def margin(self):
		"""
		This property holds the width of the margin.
		The margin is the distance between the innermost pixel of the frame and the outermost pixel of contents.
		The default margin is 0.
		"""
		res = super(QLabel,self).margin()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def movie(self):
		"""
		Returns a pointer to the labels movie, or 0 if no movie has been set.
		"""
		res = super(QLabel,self).movie()
		isinstance(res,QtGui.QMovie)
		return res
	#----------------------------------------------------------------------
	def openExternalLinks(self):
		"""
		Specifies whether PySide.QtGui.QLabel should automatically open links using QDesktopServices.openUrl() instead of emitting the PySide.QtGui.QLabel.linkActivated() signal.
		The default value is false.
		"""
		res = super(QLabel,self).openExternalLinks()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def picture(self):
		"""
		Returns the labels picture or 0 if the label doesnt have a picture.
		"""
		res = super(QLabel,self).picture()
		isinstance(res,QtGui.QPicture)
		return res
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		This property holds the labels pixmap.
		If no pixmap has been set this will return 0.
		Setting the pixmap clears any previous content
		The buddy shortcut, if any, is disabled.
		"""
		res = super(QLabel,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def selectedText(self):
		"""
		This property holds the selected text.
		If there is no selected text this propertys value is an empty string.
		By default, this property contains an empty string.
		"""
		res = super(QLabel,self).selectedText()
		return res
	#----------------------------------------------------------------------
	def selectionStart(self):
		"""
		PySide.QtGui.QLabel.selectionStart() returns the index of the first selected character in the label or -1 if no text is selected.
		"""
		res = super(QLabel,self).selectionStart()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the labels text.
		If no text has been set this will return an empty string
		Setting the text clears any previous content.
		The text will be interpreted either as plain text or as rich text, depending on the text format setting; see PySide.QtGui.QLabel.setTextFormat()
		The default setting is Qt.AutoText ; i.e
		PySide.QtGui.QLabel will try to auto-detect the format of the text set.
		If a buddy has been set, the buddy mnemonic key is updated from the new text.
		Note that PySide.QtGui.QLabel is well-suited to display small rich text documents, such as small documents that get their document specific settings (font, text color, link color) from the labels palette and font properties
		For large documents, use PySide.QtGui.QTextEdit in read-only mode instead
		PySide.QtGui.QTextEdit can also provide a scroll bar when necessary.
		"""
		res = super(QLabel,self).text()
		return res
	#----------------------------------------------------------------------
	def textFormat(self):
		"""
		This property holds the labels text format.
		See the Qt.TextFormat enum for an explanation of the possible options.
		The default format is Qt.AutoText .
		"""
		res = super(QLabel,self).textFormat()
		isinstance(res,QtCore.Qt.TextFormat)
		return res
	#----------------------------------------------------------------------
	def textInteractionFlags(self):
		"""
		Specifies how the label should interact with user input if it displays text.
		If the flags contain Qt.LinksAccessibleByKeyboard the focus policy is also automatically set to Qt.StrongFocus
		If Qt.TextSelectableByKeyboard is set then the focus policy is set to Qt.ClickFocus .
		The default value is Qt.LinksAccessibleByMouse .
		"""
		res = super(QLabel,self).textInteractionFlags()
		isinstance(res,QtCore.Qt.TextInteractionFlags)
		return res
	#----------------------------------------------------------------------
	def wordWrap(self):
		"""
		This property holds the labels word-wrapping policy.
		If this property is true then label text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all.
		By default, word wrap is disabled.
		"""
		res = super(QLabel,self).wordWrap()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,arg__1):
		"""
		setAlignment(arg__1)
			arg__1=QtCore.Qt.Alignment

		This property holds the alignment of the labels contents.
		By default, the contents of the label are left-aligned and vertically-centered.
		"""
		res = super(QLabel,self).setAlignment(arg__1)
		return res
	#----------------------------------------------------------------------
	def setBuddy(self,arg__1):
		"""
		setBuddy(arg__1)
			arg__1=QtGui.QWidget

		Sets this labels buddy to buddy .
		When the user presses the shortcut key indicated by this label, the keyboard focus is transferred to the labels buddy widget.
		The buddy mechanism is only available for QLabels that contain text in which one character is prefixed with an ampersand, &
		This character is set as the shortcut key
		See the QKeySequence.mnemonic() documentation for details (to display an actual ampersand, use &&).
		In a dialog, you might create two data entry widgets and a label for each, and set up the geometry layout so each label is just to the left of its data entry widget (its buddy), for example:
		With the code above, the focus jumps to the Name field when the user presses Alt+N, and to the Phone field when the user presses Alt+P.
		To unset a previously set buddy, call this function with buddy set to 0.
		"""
		res = super(QLabel,self).setBuddy(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIndent(self,arg__1):
		"""
		setIndent(arg__1)
			arg__1=QtCore.int

		This property holds the labels text indent in pixels.
		If a label displays text, the indent applies to the left edge if PySide.QtGui.QLabel.alignment() is Qt.AlignLeft , to the right edge if PySide.QtGui.QLabel.alignment() is Qt.AlignRight , to the top edge if PySide.QtGui.QLabel.alignment() is Qt.AlignTop , and to to the bottom edge if PySide.QtGui.QLabel.alignment() is Qt.AlignBottom .
		If indent is negative, or if no indent has been set, the label computes the effective indent as follows: If PySide.QtGui.QFrame.frameWidth() is 0, the effective indent becomes 0
		If PySide.QtGui.QFrame.frameWidth() is greater than 0, the effective indent becomes half the width of the x character of the widgets current PySide.QtGui.QWidget.font() .
		By default, the indent is -1, meaning that an effective indent is calculating in the manner described above.
		"""
		res = super(QLabel,self).setIndent(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMargin(self,arg__1):
		"""
		setMargin(arg__1)
			arg__1=QtCore.int

		This property holds the width of the margin.
		The margin is the distance between the innermost pixel of the frame and the outermost pixel of contents.
		The default margin is 0.
		"""
		res = super(QLabel,self).setMargin(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOpenExternalLinks(self,open):
		"""
		setOpenExternalLinks(open)
			open=QtCore.bool

		Specifies whether PySide.QtGui.QLabel should automatically open links using QDesktopServices.openUrl() instead of emitting the PySide.QtGui.QLabel.linkActivated() signal.
		The default value is false.
		"""
		res = super(QLabel,self).setOpenExternalLinks(open)
		return res
	#----------------------------------------------------------------------
	def setScaledContents(self,arg__1):
		"""
		setScaledContents(arg__1)
			arg__1=QtCore.bool

		This property holds whether the label will scale its contents to fill all available space..
		When enabled and the label shows a pixmap, it will scale the pixmap to fill the available space.
		This propertys default is false.
		"""
		res = super(QLabel,self).setScaledContents(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSelection(self,arg__1,arg__2):
		"""
		setSelection(arg__1,arg__2)
			arg__1=QtCore.int
			arg__2=QtCore.int

		Selects text from position start and for length characters.
		"""
		res = super(QLabel,self).setSelection(arg__1,arg__2)
		return res
	#----------------------------------------------------------------------
	def setTextFormat(self,arg__1):
		"""
		setTextFormat(arg__1)
			arg__1=QtCore.Qt.TextFormat

		This property holds the labels text format.
		See the Qt.TextFormat enum for an explanation of the possible options.
		The default format is Qt.AutoText .
		"""
		res = super(QLabel,self).setTextFormat(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTextInteractionFlags(self,flags):
		"""
		setTextInteractionFlags(flags)
			flags=QtCore.Qt.TextInteractionFlags

		Specifies how the label should interact with user input if it displays text.
		If the flags contain Qt.LinksAccessibleByKeyboard the focus policy is also automatically set to Qt.StrongFocus
		If Qt.TextSelectableByKeyboard is set then the focus policy is set to Qt.ClickFocus .
		The default value is Qt.LinksAccessibleByMouse .
		"""
		res = super(QLabel,self).setTextInteractionFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setWordWrap(self,on):
		"""
		setWordWrap(on)
			on=QtCore.bool

		This property holds the labels word-wrapping policy.
		If this property is true then label text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all.
		By default, word wrap is disabled.
		"""
		res = super(QLabel,self).setWordWrap(on)
		return res
