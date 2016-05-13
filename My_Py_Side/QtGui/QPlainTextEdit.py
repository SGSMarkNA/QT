from PySide import QtGui, QtCore

class QPlainTextEdit(QtGui.QPlainTextEdit):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPlainTextEdit,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def backgroundVisible(self):
		"""
		This property holds whether the palette background is visible outside the document area.
		If set to true, the plain text edit paints the palette background on the viewport area not covered by the text document
		Otherwise, if set to false, it wont
		The feature makes it possible for the user to visually distinguish between the area of the document, painted with the base color of the palette, and the empty area not covered by any document.
		The default is false.
		"""
		res = super(QPlainTextEdit,self).backgroundVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def blockCount(self):
		"""
		This property holds the number of text blocks in the document..
		By default, in an empty document, this property contains a value of 1.
		"""
		res = super(QPlainTextEdit,self).blockCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def canPaste(self):
		"""
		Returns whether text can be pasted from the clipboard into the textedit.
		"""
		res = super(QPlainTextEdit,self).canPaste()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def centerOnScroll(self):
		"""
		This property holds whether the cursor should be centered on screen.
		If set to true, the plain text edit scrolls the document vertically to make the cursor visible at the center of the viewport
		This also allows the text edit to scroll below the end of the document
		Otherwise, if set to false, the plain text edit scrolls the smallest amount possible to ensure the cursor is visible
		The same algorithm is applied to any new line appended through PySide.QtGui.QPlainTextEdit.appendPlainText() .
		The default is false.
		"""
		res = super(QPlainTextEdit,self).centerOnScroll()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def contentOffset(self):
		"""
		Returns the contents origin in viewport coordinates.
		The origin of the content of a plain text edit is always the top left corner of the first visible text block
		The content offset is different from (0,0) when the text has been scrolled horizontally, or when the first visible block has been scrolled partially off the screen, i.e
		the visible text does not start with the first line of the first visible block, or when the first visible block is the very first block and the editor displays a margin.
		"""
		res = super(QPlainTextEdit,self).contentOffset()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def createMimeDataFromSelection(self):
		"""
		This function returns a new MIME data object to represent the contents of the text edits current selection
		It is called when the selection needs to be encapsulated into a new PySide.QtCore.QMimeData object; for example, when a drag and drop operation is started, or when data is copied to the clipboard.
		If you reimplement this function, note that the ownership of the returned PySide.QtCore.QMimeData object is passed to the caller
		The selection can be retrieved by using the PySide.QtGui.QPlainTextEdit.textCursor() function.
		"""
		res = super(QPlainTextEdit,self).createMimeDataFromSelection()
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def createStandardContextMenu(self):
		"""
		This function creates the standard context menu which is shown when the user clicks on the line edit with the right mouse button
		It is called from the default PySide.QtGui.QPlainTextEdit.contextMenuEvent() handler
		The popup menus ownership is transferred to the caller.
		"""
		res = super(QPlainTextEdit,self).createStandardContextMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def currentCharFormat(self):
		"""
		Returns the char format that is used when inserting new text.
		"""
		res = super(QPlainTextEdit,self).currentCharFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def cursorPositionChanged(self):
		"""

		"""
		res = super(QPlainTextEdit,self).cursorPositionChanged()
		return res
	#----------------------------------------------------------------------
	def cursorRect(self):
		"""
		returns a rectangle (in viewport coordinates) that includes the cursor of the text edit.
		"""
		res = super(QPlainTextEdit,self).cursorRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def cursorWidth(self):
		"""
		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QPlainTextEdit,self).cursorWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns a pointer to the underlying document.
		"""
		res = super(QPlainTextEdit,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def documentTitle(self):
		"""
		This property holds the title of the document parsed from the text..
		By default, this property contains an empty string.
		"""
		res = super(QPlainTextEdit,self).documentTitle()
		return res
	#----------------------------------------------------------------------
	def ensureCursorVisible(self):
		"""
		Ensures that the cursor is visible by scrolling the text edit if necessary.
		"""
		res = super(QPlainTextEdit,self).ensureCursorVisible()
		return res
	#----------------------------------------------------------------------
	def extraSelections(self):
		"""
		Returns previously set extra selections.
		"""
		res = super(QPlainTextEdit,self).extraSelections()
		return res
	#----------------------------------------------------------------------
	def firstVisibleBlock(self):
		"""
		Returns the first visible block.
		"""
		res = super(QPlainTextEdit,self).firstVisibleBlock()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def getPaintContext(self):
		"""
		Returns the paint context for the PySide.QtGui.QAbstractScrollArea.viewport() , useful only when reimplementing PySide.QtGui.QPlainTextEdit.paintEvent() .
		"""
		res = super(QPlainTextEdit,self).getPaintContext()
		isinstance(res,QtGui.QAbstractTextDocumentLayout::PaintContext)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds whether the text edit is read-only.
		In a read-only text edit the user can only navigate through the text and select text; modifying the text is not possible.
		This propertys default is false.
		"""
		res = super(QPlainTextEdit,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUndoRedoEnabled(self):
		"""
		This property holds whether undo and redo are enabled.
		Users are only able to undo or redo actions if this property is true, and if there is an action that can be undone (or redone).
		By default, this property is true.
		"""
		res = super(QPlainTextEdit,self).isUndoRedoEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lineWrapMode(self):
		"""
		This property holds the line wrap mode.
		The default mode is WidgetWidth which causes words to be wrapped at the right edge of the text edit
		Wrapping occurs at whitespace, keeping whole words intact
		If you want wrapping to occur within words use PySide.QtGui.QPlainTextEdit.setWordWrapMode() .
		"""
		res = super(QPlainTextEdit,self).lineWrapMode()
		isinstance(res,QtGui.QPlainTextEdit.LineWrapMode)
		return res
	#----------------------------------------------------------------------
	def maximumBlockCount(self):
		"""
		This property holds the limit for blocks in the document..
		Specifies the maximum number of blocks the document may have
		If there are more blocks in the document that specified with this property blocks are removed from the beginning of the document.
		A negative or zero value specifies that the document may contain an unlimited amount of blocks.
		The default value is 0.
		Note that setting this property will apply the limit immediately to the document contents
		Setting this property also disables the undo redo history.
		"""
		res = super(QPlainTextEdit,self).maximumBlockCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def overwriteMode(self):
		"""
		This property holds whether text entered by the user will overwrite existing text.
		As with many text editors, the plain text editor widget can be configured to insert or overwrite existing text with new text entered by the user.
		If this property is true, existing text is overwritten, character-for-character by new text; otherwise, text is inserted at the cursor position, displacing existing text.
		By default, this property is false (new text does not overwrite existing text).
		"""
		res = super(QPlainTextEdit,self).overwriteMode()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QPlainTextEdit,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def tabChangesFocus(self):
		"""
		This property holds whether Tab changes focus or is accepted as input.
		In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain
		The default is false.
		"""
		res = super(QPlainTextEdit,self).tabChangesFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def tabStopWidth(self):
		"""
		This property holds the tab stop width in pixels.
		By default, this property contains a value of 80.
		"""
		res = super(QPlainTextEdit,self).tabStopWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def textChanged(self):
		"""

		"""
		res = super(QPlainTextEdit,self).textChanged()
		return res
	#----------------------------------------------------------------------
	def textCursor(self):
		"""
		Returns a copy of the PySide.QtGui.QTextCursor that represents the currently visible cursor
		Note that changes on the returned cursor do not affect PySide.QtGui.QPlainTextEdit s cursor; use PySide.QtGui.QPlainTextEdit.setTextCursor() to update the visible cursor.
		"""
		res = super(QPlainTextEdit,self).textCursor()
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def textInteractionFlags(self):
		"""
		Specifies how the label should interact with user input if it displays text.
		If the flags contain either Qt.LinksAccessibleByKeyboard or Qt.TextSelectableByKeyboard then the focus policy is also automatically set to Qt.ClickFocus .
		The default value depends on whether the PySide.QtGui.QPlainTextEdit is read-only or editable.
		"""
		res = super(QPlainTextEdit,self).textInteractionFlags()
		isinstance(res,QtCore.Qt.TextInteractionFlags)
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		This property gets and sets the plain text editors contents
		The previous contents are removed and undo/redo history is reset when this property is set.
		By default, for an editor with no contents, this property contains an empty string.
		"""
		res = super(QPlainTextEdit,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def wordWrapMode(self):
		"""

		"""
		res = super(QPlainTextEdit,self).wordWrapMode()
		isinstance(res,QtGui.QTextOption.WrapMode)
		return res
	#----------------------------------------------------------------------
	def anchorAt(self,pos):
		"""
		anchorAt(pos)
			pos=QtCore.QPoint

		Returns the reference of the anchor at position pos , or an empty string if no anchor exists at that point.
		"""
		res = super(QPlainTextEdit,self).anchorAt(pos)
		return res
	#----------------------------------------------------------------------
	def blockBoundingGeometry(self,block):
		"""
		blockBoundingGeometry(block)
			block=QtGui.QTextBlock

		Returns the bounding rectangle of the text block in content coordinates
		Translate the rectangle with the PySide.QtGui.QPlainTextEdit.contentOffset() to get visual coordinates on the viewport.
		"""
		res = super(QPlainTextEdit,self).blockBoundingGeometry(block)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def blockBoundingRect(self,block):
		"""
		blockBoundingRect(block)
			block=QtGui.QTextBlock

		Returns the bounding rectangle of the text block in the blocks own coordinates.
		"""
		res = super(QPlainTextEdit,self).blockBoundingRect(block)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def canInsertFromMimeData(self,source):
		"""
		canInsertFromMimeData(source)
			source=QtCore.QMimeData

		This function returns true if the contents of the MIME data object, specified by source , can be decoded and inserted into the document
		It is called for example when during a drag operation the mouse enters this widget and it is necessary to determine whether it is possible to accept the drag.
		"""
		res = super(QPlainTextEdit,self).canInsertFromMimeData(source)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def cursorForPosition(self,pos):
		"""
		cursorForPosition(pos)
			pos=QtCore.QPoint

		returns a PySide.QtGui.QTextCursor at position pos (in viewport coordinates).
		"""
		res = super(QPlainTextEdit,self).cursorForPosition(pos)
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def cursorRect(self,cursor):
		"""
		cursorRect(cursor)
			cursor=QtGui.QTextCursor

		returns a rectangle (in viewport coordinates) that includes the cursor .
		"""
		res = super(QPlainTextEdit,self).cursorRect(cursor)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def find(self,exp,options=None):
		"""
		find(exp,options=None)
			exp=unicode
			options=QtGui.QTextDocument.FindFlags


		"""
		res = super(QPlainTextEdit,self).find(exp,options)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insertFromMimeData(self,source):
		"""
		insertFromMimeData(source)
			source=QtCore.QMimeData

		This function inserts the contents of the MIME data object, specified by source , into the text edit at the current cursor position
		It is called whenever text is inserted as the result of a clipboard paste operation, or when the text edit accepts data from a drag and drop operation.
		"""
		res = super(QPlainTextEdit,self).insertFromMimeData(source)
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
		res = super(QPlainTextEdit,self).loadResource(type,name)
		return res
	#----------------------------------------------------------------------
	def mergeCurrentCharFormat(self,modifier):
		"""
		mergeCurrentCharFormat(modifier)
			modifier=QtGui.QTextCharFormat

		Merges the properties specified in modifier into the current character format by calling QTextCursor::mergeCharFormat on the editors cursor
		If the editor has a selection then the properties of modifier are directly applied to the selection.
		"""
		res = super(QPlainTextEdit,self).mergeCurrentCharFormat(modifier)
		return res
	#----------------------------------------------------------------------
	def moveCursor(self,operation,mode=None):
		"""
		moveCursor(operation,mode=None)
			operation=QtGui.QTextCursor.MoveOperation
			mode=QtGui.QTextCursor.MoveMode


		"""
		res = super(QPlainTextEdit,self).moveCursor(operation,mode)
		return res
	#----------------------------------------------------------------------
	def print_(self,printer):
		"""
		print_(printer)
			printer=QtGui.QPrinter

		Convenience function to print the text edits document to the given printer
		This is equivalent to calling the print method on the document directly except that this function also supports QPrinter.Selection as print range.
		"""
		res = super(QPlainTextEdit,self).print_(printer)
		return res
	#----------------------------------------------------------------------
	def setBackgroundVisible(self,visible):
		"""
		setBackgroundVisible(visible)
			visible=QtCore.bool

		This property holds whether the palette background is visible outside the document area.
		If set to true, the plain text edit paints the palette background on the viewport area not covered by the text document
		Otherwise, if set to false, it wont
		The feature makes it possible for the user to visually distinguish between the area of the document, painted with the base color of the palette, and the empty area not covered by any document.
		The default is false.
		"""
		res = super(QPlainTextEdit,self).setBackgroundVisible(visible)
		return res
	#----------------------------------------------------------------------
	def setCenterOnScroll(self,enabled):
		"""
		setCenterOnScroll(enabled)
			enabled=QtCore.bool

		This property holds whether the cursor should be centered on screen.
		If set to true, the plain text edit scrolls the document vertically to make the cursor visible at the center of the viewport
		This also allows the text edit to scroll below the end of the document
		Otherwise, if set to false, the plain text edit scrolls the smallest amount possible to ensure the cursor is visible
		The same algorithm is applied to any new line appended through PySide.QtGui.QPlainTextEdit.appendPlainText() .
		The default is false.
		"""
		res = super(QPlainTextEdit,self).setCenterOnScroll(enabled)
		return res
	#----------------------------------------------------------------------
	def setCurrentCharFormat(self,format):
		"""
		setCurrentCharFormat(format)
			format=QtGui.QTextCharFormat

		Sets the char format that is be used when inserting new text to format by calling QTextCursor.setCharFormat() on the editors cursor
		If the editor has a selection then the char format is directly applied to the selection.
		"""
		res = super(QPlainTextEdit,self).setCurrentCharFormat(format)
		return res
	#----------------------------------------------------------------------
	def setCursorWidth(self,width):
		"""
		setCursorWidth(width)
			width=QtCore.int

		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QPlainTextEdit,self).setCursorWidth(width)
		return res
	#----------------------------------------------------------------------
	def setDocument(self,document):
		"""
		setDocument(document)
			document=QtGui.QTextDocument

		Makes document the new document of the text editor.
		The parent PySide.QtCore.QObject of the provided document remains the owner of the object
		If the current document is a child of the text editor, then it is deleted.
		The document must have a document layout that inherits PySide.QtGui.QPlainTextDocumentLayout (see QTextDocument.setDocumentLayout() ).
		"""
		res = super(QPlainTextEdit,self).setDocument(document)
		return res
	#----------------------------------------------------------------------
	def setDocumentTitle(self,title):
		"""
		setDocumentTitle(title)
			title=unicode

		This property holds the title of the document parsed from the text..
		By default, this property contains an empty string.
		"""
		res = super(QPlainTextEdit,self).setDocumentTitle(title)
		return res
	#----------------------------------------------------------------------
	def setExtraSelections(self,selections):
		"""
		setExtraSelections(selections)
			selections=unKnown


		"""
		res = super(QPlainTextEdit,self).setExtraSelections(selections)
		return res
	#----------------------------------------------------------------------
	def setLineWrapMode(self,mode):
		"""
		setLineWrapMode(mode)
			mode=QtGui.QPlainTextEdit.LineWrapMode

		This property holds the line wrap mode.
		The default mode is WidgetWidth which causes words to be wrapped at the right edge of the text edit
		Wrapping occurs at whitespace, keeping whole words intact
		If you want wrapping to occur within words use PySide.QtGui.QPlainTextEdit.setWordWrapMode() .
		"""
		res = super(QPlainTextEdit,self).setLineWrapMode(mode)
		return res
	#----------------------------------------------------------------------
	def setMaximumBlockCount(self,maximum):
		"""
		setMaximumBlockCount(maximum)
			maximum=QtCore.int

		This property holds the limit for blocks in the document..
		Specifies the maximum number of blocks the document may have
		If there are more blocks in the document that specified with this property blocks are removed from the beginning of the document.
		A negative or zero value specifies that the document may contain an unlimited amount of blocks.
		The default value is 0.
		Note that setting this property will apply the limit immediately to the document contents
		Setting this property also disables the undo redo history.
		"""
		res = super(QPlainTextEdit,self).setMaximumBlockCount(maximum)
		return res
	#----------------------------------------------------------------------
	def setOverwriteMode(self,overwrite):
		"""
		setOverwriteMode(overwrite)
			overwrite=QtCore.bool

		This property holds whether text entered by the user will overwrite existing text.
		As with many text editors, the plain text editor widget can be configured to insert or overwrite existing text with new text entered by the user.
		If this property is true, existing text is overwritten, character-for-character by new text; otherwise, text is inserted at the cursor position, displacing existing text.
		By default, this property is false (new text does not overwrite existing text).
		"""
		res = super(QPlainTextEdit,self).setOverwriteMode(overwrite)
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
		res = super(QPlainTextEdit,self).setReadOnly(ro)
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
		res = super(QPlainTextEdit,self).setTabChangesFocus(b)
		return res
	#----------------------------------------------------------------------
	def setTabStopWidth(self,width):
		"""
		setTabStopWidth(width)
			width=QtCore.int

		This property holds the tab stop width in pixels.
		By default, this property contains a value of 80.
		"""
		res = super(QPlainTextEdit,self).setTabStopWidth(width)
		return res
	#----------------------------------------------------------------------
	def setTextCursor(self,cursor):
		"""
		setTextCursor(cursor)
			cursor=QtGui.QTextCursor

		Sets the visible cursor .
		"""
		res = super(QPlainTextEdit,self).setTextCursor(cursor)
		return res
	#----------------------------------------------------------------------
	def setTextInteractionFlags(self,flags):
		"""
		setTextInteractionFlags(flags)
			flags=QtCore.Qt.TextInteractionFlags

		Specifies how the label should interact with user input if it displays text.
		If the flags contain either Qt.LinksAccessibleByKeyboard or Qt.TextSelectableByKeyboard then the focus policy is also automatically set to Qt.ClickFocus .
		The default value depends on whether the PySide.QtGui.QPlainTextEdit is read-only or editable.
		"""
		res = super(QPlainTextEdit,self).setTextInteractionFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setUndoRedoEnabled(self,enable):
		"""
		setUndoRedoEnabled(enable)
			enable=QtCore.bool

		This property holds whether undo and redo are enabled.
		Users are only able to undo or redo actions if this property is true, and if there is an action that can be undone (or redone).
		By default, this property is true.
		"""
		res = super(QPlainTextEdit,self).setUndoRedoEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setWordWrapMode(self,policy):
		"""
		setWordWrapMode(policy)
			policy=QtGui.QTextOption.WrapMode


		"""
		res = super(QPlainTextEdit,self).setWordWrapMode(policy)
		return res
