from PySide import QtGui, QtCore

class QTextEdit(QtGui.QTextEdit):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextEdit,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceptRichText(self):
		"""
		This property holds whether the text edit accepts rich text insertions by the user.
		When this propery is set to false text edit will accept only plain text input from the user
		For example through clipboard or drag and drop.
		This propertys default is true.
		"""
		res = super(QTextEdit,self).acceptRichText()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		Returns the alignment of the current paragraph.
		"""
		res = super(QTextEdit,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def autoFormatting(self):
		"""
		This property holds the enabled set of auto formatting features.
		The value can be any combination of the values in the QTextEdit.AutoFormattingFlag enum
		The default is AutoNone
		Choose AutoAll to enable all automatic formatting.
		Currently, the only automatic formatting feature provided is AutoBulletList ; future versions of Qt may offer more.
		"""
		res = super(QTextEdit,self).autoFormatting()
		isinstance(res,QtGui.QTextEdit.AutoFormatting)
		return res
	#----------------------------------------------------------------------
	def canPaste(self):
		"""
		Returns whether text can be pasted from the clipboard into the textedit.
		"""
		res = super(QTextEdit,self).canPaste()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def createMimeDataFromSelection(self):
		"""
		This function returns a new MIME data object to represent the contents of the text edits current selection
		It is called when the selection needs to be encapsulated into a new PySide.QtCore.QMimeData object; for example, when a drag and drop operation is started, or when data is copyied to the clipboard.
		If you reimplement this function, note that the ownership of the returned PySide.QtCore.QMimeData object is passed to the caller
		The selection can be retrieved by using the PySide.QtGui.QTextEdit.textCursor() function.
		"""
		res = super(QTextEdit,self).createMimeDataFromSelection()
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def createStandardContextMenu(self):
		"""
		This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button
		It is called from the default PySide.QtGui.QTextEdit.contextMenuEvent() handler
		The popup menus ownership is transferred to the caller.
		We recommend that you use the createStandardContextMenu( PySide.QtCore.QPoint ) version instead which will enable the actions that are sensitive to where the user clicked.
		"""
		res = super(QTextEdit,self).createStandardContextMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def currentCharFormat(self):
		"""
		Returns the char format that is used when inserting new text.
		"""
		res = super(QTextEdit,self).currentCharFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def currentFont(self):
		"""
		Returns the font of the current format.
		"""
		res = super(QTextEdit,self).currentFont()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def cursorPositionChanged(self):
		"""

		"""
		res = super(QTextEdit,self).cursorPositionChanged()
		return res
	#----------------------------------------------------------------------
	def cursorRect(self):
		"""
		returns a rectangle (in viewport coordinates) that includes the cursor of the text edit.
		"""
		res = super(QTextEdit,self).cursorRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def cursorWidth(self):
		"""
		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QTextEdit,self).cursorWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns a pointer to the underlying document.
		"""
		res = super(QTextEdit,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def documentTitle(self):
		"""
		This property holds the title of the document parsed from the text..
		By default, for a newly-created, empty document, this property contains an empty string.
		"""
		res = super(QTextEdit,self).documentTitle()
		return res
	#----------------------------------------------------------------------
	def ensureCursorVisible(self):
		"""
		Ensures that the cursor is visible by scrolling the text edit if necessary.
		"""
		res = super(QTextEdit,self).ensureCursorVisible()
		return res
	#----------------------------------------------------------------------
	def extraSelections(self):
		"""
		Returns previously set extra selections.
		"""
		res = super(QTextEdit,self).extraSelections()
		return res
	#----------------------------------------------------------------------
	def fontFamily(self):
		"""
		Returns the font family of the current format.
		"""
		res = super(QTextEdit,self).fontFamily()
		return res
	#----------------------------------------------------------------------
	def fontItalic(self):
		"""
		Returns true if the font of the current format is italic; otherwise returns false.
		"""
		res = super(QTextEdit,self).fontItalic()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fontPointSize(self):
		"""
		Returns the point size of the font of the current format.
		"""
		res = super(QTextEdit,self).fontPointSize()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def fontUnderline(self):
		"""
		Returns true if the font of the current format is underlined; otherwise returns false.
		"""
		res = super(QTextEdit,self).fontUnderline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fontWeight(self):
		"""
		Returns the font weight of the current format.
		"""
		res = super(QTextEdit,self).fontWeight()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds whether the text edit is read-only.
		In a read-only text edit the user can only navigate through the text and select text; modifying the text is not possible.
		This propertys default is false.
		"""
		res = super(QTextEdit,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUndoRedoEnabled(self):
		"""
		This property holds whether undo and redo are enabled.
		Users are only able to undo or redo actions if this property is true, and if there is an action that can be undone (or redone).
		"""
		res = super(QTextEdit,self).isUndoRedoEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lineWrapColumnOrWidth(self):
		"""
		This property holds the position (in pixels or columns depending on the wrap mode) where text will be wrapped.
		If the wrap mode is FixedPixelWidth , the value is the number of pixels from the left edge of the text edit at which text should be wrapped
		If the wrap mode is FixedColumnWidth , the value is the column number (in character columns) from the left edge of the text edit at which text should be wrapped.
		By default, this property contains a value of 0.
		"""
		res = super(QTextEdit,self).lineWrapColumnOrWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def lineWrapMode(self):
		"""
		This property holds the line wrap mode.
		The default mode is WidgetWidth which causes words to be wrapped at the right edge of the text edit
		Wrapping occurs at whitespace, keeping whole words intact
		If you want wrapping to occur within words use PySide.QtGui.QTextEdit.setWordWrapMode()
		If you set a wrap mode of FixedPixelWidth or FixedColumnWidth you should also call PySide.QtGui.QTextEdit.setLineWrapColumnOrWidth() with the width you want.
		"""
		res = super(QTextEdit,self).lineWrapMode()
		isinstance(res,QtGui.QTextEdit.LineWrapMode)
		return res
	#----------------------------------------------------------------------
	def overwriteMode(self):
		"""
		This property holds whether text entered by the user will overwrite existing text.
		As with many text editors, the text editor widget can be configured to insert or overwrite existing text with new text entered by the user.
		If this property is true, existing text is overwritten, character-for-character by new text; otherwise, text is inserted at the cursor position, displacing existing text.
		By default, this property is false (new text does not overwrite existing text).
		"""
		res = super(QTextEdit,self).overwriteMode()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QTextEdit,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def tabChangesFocus(self):
		"""
		This property holds whether Tab changes focus or is accepted as input.
		In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain
		The default is false.
		"""
		res = super(QTextEdit,self).tabChangesFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def tabStopWidth(self):
		"""
		This property holds the tab stop width in pixels.
		By default, this property contains a value of 80 pixels.
		"""
		res = super(QTextEdit,self).tabStopWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def textBackgroundColor(self):
		"""
		Returns the text background color of the current format.
		"""
		res = super(QTextEdit,self).textBackgroundColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def textChanged(self):
		"""

		"""
		res = super(QTextEdit,self).textChanged()
		return res
	#----------------------------------------------------------------------
	def textColor(self):
		"""
		Returns the text color of the current format.
		"""
		res = super(QTextEdit,self).textColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def textCursor(self):
		"""
		Returns a copy of the PySide.QtGui.QTextCursor that represents the currently visible cursor
		Note that changes on the returned cursor do not affect PySide.QtGui.QTextEdit s cursor; use PySide.QtGui.QTextEdit.setTextCursor() to update the visible cursor.
		"""
		res = super(QTextEdit,self).textCursor()
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def textInteractionFlags(self):
		"""
		Specifies how the widget should interact with user input.
		The default value depends on whether the PySide.QtGui.QTextEdit is read-only or editable, and whether it is a PySide.QtGui.QTextBrowser or not.
		"""
		res = super(QTextEdit,self).textInteractionFlags()
		isinstance(res,QtCore.Qt.TextInteractionFlags)
		return res
	#----------------------------------------------------------------------
	def toHtml(self):
		"""
		This property provides an HTML interface to the text of the text edit.
		PySide.QtGui.QTextEdit.toHtml() returns the text of the text edit as html.
		PySide.QtGui.QTextEdit.setHtml() changes the text of the text edit
		Any previous text is removed and the undo/redo history is cleared
		The input text is interpreted as rich text in html format.
		By default, for a newly-created, empty document, this property contains text to describe an HTML 4.0 document with no body text.
		"""
		res = super(QTextEdit,self).toHtml()
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		This property gets and sets the text editors contents as plain text
		Previous contents are removed and undo/redo history is reset when the property is set.
		If the text edit has another content type, it will not be replaced by plain text if you call PySide.QtGui.QTextEdit.toPlainText()
		The only exception to this is the non-break space, nbsp; , that will be converted into standard space.
		By default, for an editor with no contents, this property contains an empty string.
		"""
		res = super(QTextEdit,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def wordWrapMode(self):
		"""

		"""
		res = super(QTextEdit,self).wordWrapMode()
		isinstance(res,QtGui.QTextOption.WrapMode)
		return res
	#----------------------------------------------------------------------
	def anchorAt(self,pos):
		"""
		anchorAt(pos)
			pos=QtCore.QPoint

		Returns the reference of the anchor at position pos , or an empty string if no anchor exists at that point.
		"""
		res = super(QTextEdit,self).anchorAt(pos)
		return res
	#----------------------------------------------------------------------
	def canInsertFromMimeData(self,source):
		"""
		canInsertFromMimeData(source)
			source=QtCore.QMimeData

		This function returns true if the contents of the MIME data object, specified by source , can be decoded and inserted into the document
		It is called for example when during a drag operation the mouse enters this widget and it is necessary to determine whether it is possible to accept the drag and drop operation.
		Reimplement this function to enable drag and drop support for additional MIME types.
		"""
		res = super(QTextEdit,self).canInsertFromMimeData(source)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def createStandardContextMenu(self,position):
		"""
		createStandardContextMenu(position)
			position=QtCore.QPoint

		This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button
		It is called from the default PySide.QtGui.QTextEdit.contextMenuEvent() handler and it takes the position of where the mouse click was
		This can enable actions that are sensitive to the position where the user clicked
		The popup menus ownership is transferred to the caller.
		"""
		res = super(QTextEdit,self).createStandardContextMenu(position)
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def cursorForPosition(self,pos):
		"""
		cursorForPosition(pos)
			pos=QtCore.QPoint

		returns a PySide.QtGui.QTextCursor at position pos (in viewport coordinates).
		"""
		res = super(QTextEdit,self).cursorForPosition(pos)
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def cursorRect(self,cursor):
		"""
		cursorRect(cursor)
			cursor=QtGui.QTextCursor

		returns a rectangle (in viewport coordinates) that includes the cursor .
		"""
		res = super(QTextEdit,self).cursorRect(cursor)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def find(self,exp,options=None):
		"""
		find(exp,options=None)
			exp=unicode
			options=QtGui.QTextDocument.FindFlags


		"""
		res = super(QTextEdit,self).find(exp,options)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insertFromMimeData(self,source):
		"""
		insertFromMimeData(source)
			source=QtCore.QMimeData

		This function inserts the contents of the MIME data object, specified by source , into the text edit at the current cursor position
		It is called whenever text is inserted as the result of a clipboard paste operation, or when the text edit accepts data from a drag and drop operation.
		Reimplement this function to enable drag and drop support for additional MIME types.
		"""
		res = super(QTextEdit,self).insertFromMimeData(source)
		return res
	#----------------------------------------------------------------------
	def loadResource(self,type,name):
		"""
		loadResource(type,name)
			type=QtCore.int
			name=QtCore.QUrl

		Loads the resource specified by the given type and name .
		This function is an extension of QTextDocument.loadResource() .
		"""
		res = super(QTextEdit,self).loadResource(type,name)
		return res
	#----------------------------------------------------------------------
	def mergeCurrentCharFormat(self,modifier):
		"""
		mergeCurrentCharFormat(modifier)
			modifier=QtGui.QTextCharFormat

		Merges the properties specified in modifier into the current character format by calling QTextCursor::mergeCharFormat on the editors cursor
		If the editor has a selection then the properties of modifier are directly applied to the selection.
		"""
		res = super(QTextEdit,self).mergeCurrentCharFormat(modifier)
		return res
	#----------------------------------------------------------------------
	def moveCursor(self,operation,mode=None):
		"""
		moveCursor(operation,mode=None)
			operation=QtGui.QTextCursor.MoveOperation
			mode=QtGui.QTextCursor.MoveMode


		"""
		res = super(QTextEdit,self).moveCursor(operation,mode)
		return res
	#----------------------------------------------------------------------
	def print_(self,printer):
		"""
		print_(printer)
			printer=QtGui.QPrinter

		Convenience function to print the text edits document to the given printer
		This is equivalent to calling the print method on the document directly except that this function also supports QPrinter.Selection as print range.
		"""
		res = super(QTextEdit,self).print_(printer)
		return res
	#----------------------------------------------------------------------
	def setAcceptRichText(self,accept):
		"""
		setAcceptRichText(accept)
			accept=QtCore.bool

		This property holds whether the text edit accepts rich text insertions by the user.
		When this propery is set to false text edit will accept only plain text input from the user
		For example through clipboard or drag and drop.
		This propertys default is true.
		"""
		res = super(QTextEdit,self).setAcceptRichText(accept)
		return res
	#----------------------------------------------------------------------
	def setAutoFormatting(self,features):
		"""
		setAutoFormatting(features)
			features=QtGui.QTextEdit.AutoFormatting

		This property holds the enabled set of auto formatting features.
		The value can be any combination of the values in the QTextEdit.AutoFormattingFlag enum
		The default is AutoNone
		Choose AutoAll to enable all automatic formatting.
		Currently, the only automatic formatting feature provided is AutoBulletList ; future versions of Qt may offer more.
		"""
		res = super(QTextEdit,self).setAutoFormatting(features)
		return res
	#----------------------------------------------------------------------
	def setCurrentCharFormat(self,format):
		"""
		setCurrentCharFormat(format)
			format=QtGui.QTextCharFormat

		Sets the char format that is be used when inserting new text to format by calling QTextCursor.setCharFormat() on the editors cursor
		If the editor has a selection then the char format is directly applied to the selection.
		"""
		res = super(QTextEdit,self).setCurrentCharFormat(format)
		return res
	#----------------------------------------------------------------------
	def setCursorWidth(self,width):
		"""
		setCursorWidth(width)
			width=QtCore.int

		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QTextEdit,self).setCursorWidth(width)
		return res
	#----------------------------------------------------------------------
	def setDocument(self,document):
		"""
		setDocument(document)
			document=QtGui.QTextDocument

		Makes document the new document of the text editor.
		The editor does not delete the current document, even if it is a child of the editor.
		"""
		res = super(QTextEdit,self).setDocument(document)
		return res
	#----------------------------------------------------------------------
	def setDocumentTitle(self,title):
		"""
		setDocumentTitle(title)
			title=unicode

		This property holds the title of the document parsed from the text..
		By default, for a newly-created, empty document, this property contains an empty string.
		"""
		res = super(QTextEdit,self).setDocumentTitle(title)
		return res
	#----------------------------------------------------------------------
	def setExtraSelections(self,selections):
		"""
		setExtraSelections(selections)
			selections=unKnown


		"""
		res = super(QTextEdit,self).setExtraSelections(selections)
		return res
	#----------------------------------------------------------------------
	def setLineWrapColumnOrWidth(self,w):
		"""
		setLineWrapColumnOrWidth(w)
			w=QtCore.int

		This property holds the position (in pixels or columns depending on the wrap mode) where text will be wrapped.
		If the wrap mode is FixedPixelWidth , the value is the number of pixels from the left edge of the text edit at which text should be wrapped
		If the wrap mode is FixedColumnWidth , the value is the column number (in character columns) from the left edge of the text edit at which text should be wrapped.
		By default, this property contains a value of 0.
		"""
		res = super(QTextEdit,self).setLineWrapColumnOrWidth(w)
		return res
	#----------------------------------------------------------------------
	def setLineWrapMode(self,mode):
		"""
		setLineWrapMode(mode)
			mode=QtGui.QTextEdit.LineWrapMode

		This property holds the line wrap mode.
		The default mode is WidgetWidth which causes words to be wrapped at the right edge of the text edit
		Wrapping occurs at whitespace, keeping whole words intact
		If you want wrapping to occur within words use PySide.QtGui.QTextEdit.setWordWrapMode()
		If you set a wrap mode of FixedPixelWidth or FixedColumnWidth you should also call PySide.QtGui.QTextEdit.setLineWrapColumnOrWidth() with the width you want.
		"""
		res = super(QTextEdit,self).setLineWrapMode(mode)
		return res
	#----------------------------------------------------------------------
	def setOverwriteMode(self,overwrite):
		"""
		setOverwriteMode(overwrite)
			overwrite=QtCore.bool

		This property holds whether text entered by the user will overwrite existing text.
		As with many text editors, the text editor widget can be configured to insert or overwrite existing text with new text entered by the user.
		If this property is true, existing text is overwritten, character-for-character by new text; otherwise, text is inserted at the cursor position, displacing existing text.
		By default, this property is false (new text does not overwrite existing text).
		"""
		res = super(QTextEdit,self).setOverwriteMode(overwrite)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,ro):
		"""
		setReadOnly(ro)
			ro=QtCore.bool

		This property holds whether the text edit is read-only.
		In a read-only text edit the user can only navigate through the text and select text; modifying the text is not possible.
		This propertys default is false.
		"""
		res = super(QTextEdit,self).setReadOnly(ro)
		return res
	#----------------------------------------------------------------------
	def setTabChangesFocus(self,b):
		"""
		setTabChangesFocus(b)
			b=QtCore.bool

		This property holds whether Tab changes focus or is accepted as input.
		In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain
		The default is false.
		"""
		res = super(QTextEdit,self).setTabChangesFocus(b)
		return res
	#----------------------------------------------------------------------
	def setTabStopWidth(self,width):
		"""
		setTabStopWidth(width)
			width=QtCore.int

		This property holds the tab stop width in pixels.
		By default, this property contains a value of 80 pixels.
		"""
		res = super(QTextEdit,self).setTabStopWidth(width)
		return res
	#----------------------------------------------------------------------
	def setTextCursor(self,cursor):
		"""
		setTextCursor(cursor)
			cursor=QtGui.QTextCursor

		Sets the visible cursor .
		"""
		res = super(QTextEdit,self).setTextCursor(cursor)
		return res
	#----------------------------------------------------------------------
	def setTextInteractionFlags(self,flags):
		"""
		setTextInteractionFlags(flags)
			flags=QtCore.Qt.TextInteractionFlags

		Specifies how the widget should interact with user input.
		The default value depends on whether the PySide.QtGui.QTextEdit is read-only or editable, and whether it is a PySide.QtGui.QTextBrowser or not.
		"""
		res = super(QTextEdit,self).setTextInteractionFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setUndoRedoEnabled(self,enable):
		"""
		setUndoRedoEnabled(enable)
			enable=QtCore.bool

		This property holds whether undo and redo are enabled.
		Users are only able to undo or redo actions if this property is true, and if there is an action that can be undone (or redone).
		"""
		res = super(QTextEdit,self).setUndoRedoEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setWordWrapMode(self,policy):
		"""
		setWordWrapMode(policy)
			policy=QtGui.QTextOption.WrapMode


		"""
		res = super(QTextEdit,self).setWordWrapMode(policy)
		return res
