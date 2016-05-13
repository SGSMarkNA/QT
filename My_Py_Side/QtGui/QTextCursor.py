from PySide import QtGui, QtCore

class QTextCursor(QtGui.QTextCursor):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextCursor,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def anchor(self):
		"""
		Returns the anchor position; this is the same as PySide.QtGui.QTextCursor.position() unless there is a selection in which case PySide.QtGui.QTextCursor.position() marks one end of the selection and PySide.QtGui.QTextCursor.anchor() marks the other end
		Just like the cursor position, the anchor position is between characters.
		"""
		res = super(QTextCursor,self).anchor()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def atBlockEnd(self):
		"""
		Returns true if the cursor is at the end of a block; otherwise returns false.
		"""
		res = super(QTextCursor,self).atBlockEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def atBlockStart(self):
		"""
		Returns true if the cursor is at the start of a block; otherwise returns false.
		"""
		res = super(QTextCursor,self).atBlockStart()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the cursor is at the end of the document; otherwise returns false.
		"""
		res = super(QTextCursor,self).atEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def atStart(self):
		"""
		Returns true if the cursor is at the start of the document; otherwise returns false.
		"""
		res = super(QTextCursor,self).atStart()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def beginEditBlock(self):
		"""
		Indicates the start of a block of editing operations on the document that should appear as a single operation from an undo/redo point of view.
		For example:
		The call to undo() will cause both insertions to be undone, causing both World and Hello to be removed.
		It is possible to nest calls to beginEditBlock and endEditBlock
		The top-most pair will determine the scope of the undo/redo operation.
		"""
		res = super(QTextCursor,self).beginEditBlock()
		return res
	#----------------------------------------------------------------------
	def block(self):
		"""
		Returns the block that contains the cursor.
		"""
		res = super(QTextCursor,self).block()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def blockCharFormat(self):
		"""
		Returns the block character format of the block the cursor is in.
		The block char format is the format used when inserting text at the beginning of an empty block.
		"""
		res = super(QTextCursor,self).blockCharFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def blockFormat(self):
		"""
		Returns the block format of the block the cursor is in.
		"""
		res = super(QTextCursor,self).blockFormat()
		isinstance(res,QtGui.QTextBlockFormat)
		return res
	#----------------------------------------------------------------------
	def blockNumber(self):
		"""
		Returns the number of the block the cursor is in, or 0 if the cursor is invalid.
		Note that this function only makes sense in documents without complex objects such as tables or frames.
		"""
		res = super(QTextCursor,self).blockNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def charFormat(self):
		"""
		Returns the format of the character immediately before the cursor PySide.QtGui.QTextCursor.position()
		If the cursor is positioned at the beginning of a text block that is not empty then the format of the character immediately after the cursor is returned.
		"""
		res = super(QTextCursor,self).charFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def clearSelection(self):
		"""
		Clears the current selection by setting the anchor to the cursor position.
		Note that it does not delete the text of the selection.
		"""
		res = super(QTextCursor,self).clearSelection()
		return res
	#----------------------------------------------------------------------
	def columnNumber(self):
		"""
		Returns the position of the cursor within its containing line.
		Note that this is the column number relative to a wrapped line, not relative to the block (i.e
		the paragraph).
		You probably want to call PySide.QtGui.QTextCursor.positionInBlock() instead.
		"""
		res = super(QTextCursor,self).columnNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentFrame(self):
		"""
		Returns a pointer to the current frame
		Returns 0 if the cursor is invalid.
		"""
		res = super(QTextCursor,self).currentFrame()
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def currentList(self):
		"""
		Returns the current list if the cursor PySide.QtGui.QTextCursor.position() is inside a block that is part of a list; otherwise returns 0.
		"""
		res = super(QTextCursor,self).currentList()
		isinstance(res,QtGui.QTextList)
		return res
	#----------------------------------------------------------------------
	def currentTable(self):
		"""
		Returns a pointer to the current table if the cursor PySide.QtGui.QTextCursor.position() is inside a block that is part of a table; otherwise returns 0.
		"""
		res = super(QTextCursor,self).currentTable()
		isinstance(res,QtGui.QTextTable)
		return res
	#----------------------------------------------------------------------
	def deleteChar(self):
		"""
		If there is no selected text, deletes the character at the current cursor position; otherwise deletes the selected text.
		"""
		res = super(QTextCursor,self).deleteChar()
		return res
	#----------------------------------------------------------------------
	def deletePreviousChar(self):
		"""
		If there is no selected text, deletes the character before the current cursor position; otherwise deletes the selected text.
		"""
		res = super(QTextCursor,self).deletePreviousChar()
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the document this cursor is associated with.
		"""
		res = super(QTextCursor,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def endEditBlock(self):
		"""
		Indicates the end of a block of editing operations on the document that should appear as a single operation from an undo/redo point of view.
		"""
		res = super(QTextCursor,self).endEditBlock()
		return res
	#----------------------------------------------------------------------
	def hasComplexSelection(self):
		"""
		Returns true if the cursor contains a selection that is not simply a range from PySide.QtGui.QTextCursor.selectionStart() to PySide.QtGui.QTextCursor.selectionEnd() ; otherwise returns false.
		Complex selections are ones that span at least two cells in a table; their extent is specified by PySide.QtGui.QTextCursor.selectedTableCells() .
		"""
		res = super(QTextCursor,self).hasComplexSelection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasSelection(self):
		"""
		Returns true if the cursor contains a selection; otherwise returns false.
		"""
		res = super(QTextCursor,self).hasSelection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insertBlock(self):
		"""
		Inserts a new empty block at the cursor PySide.QtGui.QTextCursor.position() with the current PySide.QtGui.QTextCursor.blockFormat() and PySide.QtGui.QTextCursor.charFormat() .
		"""
		res = super(QTextCursor,self).insertBlock()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the cursor is null; otherwise returns false
		A null cursor is created by the default constructor.
		"""
		res = super(QTextCursor,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def joinPreviousEditBlock(self):
		"""
		Like PySide.QtGui.QTextCursor.beginEditBlock() indicates the start of a block of editing operations that should appear as a single operation for undo/redo
		However unlike PySide.QtGui.QTextCursor.beginEditBlock() it does not start a new block but reverses the previous call to PySide.QtGui.QTextCursor.endEditBlock() and therefore makes following operations part of the previous edit block created.
		For example:
		The call to undo() will cause all three insertions to be undone.
		"""
		res = super(QTextCursor,self).joinPreviousEditBlock()
		return res
	#----------------------------------------------------------------------
	def keepPositionOnInsert(self):
		"""
		Returns whether the cursor should keep its current position when text gets inserted at the position of the cursor.
		The default is false;
		"""
		res = super(QTextCursor,self).keepPositionOnInsert()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		Returns the absolute position of the cursor within the document
		The cursor is positioned between characters.
		"""
		res = super(QTextCursor,self).position()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def positionInBlock(self):
		"""
		Returns the relative position of the cursor within the block
		The cursor is positioned between characters.
		This is equivalent to position() - block().position() .
		"""
		res = super(QTextCursor,self).positionInBlock()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def removeSelectedText(self):
		"""
		If there is a selection, its content is deleted; otherwise does nothing.
		"""
		res = super(QTextCursor,self).removeSelectedText()
		return res
	#----------------------------------------------------------------------
	def selectedTableCells(self):
		"""
		If the selection spans over table cells, firstRow is populated with the number of the first row in the selection, firstColumn with the number of the first column in the selection, and numRows and numColumns with the number of rows and columns in the selection
		If the selection does not span any table cells the results are harmless but undefined.
		"""
		res = super(QTextCursor,self).selectedTableCells()
		return res
	#----------------------------------------------------------------------
	def selectedText(self):
		"""
		Returns the current selections text (which may be empty)
		This only returns the text, with no rich text formatting information
		If you want a document fragment (i.e
		formatted rich text) use PySide.QtGui.QTextCursor.selection() instead.
		"""
		res = super(QTextCursor,self).selectedText()
		return res
	#----------------------------------------------------------------------
	def selection(self):
		"""
		Returns the current selection (which may be empty) with all its formatting information
		If you just want the selected text (i.e
		plain text) use PySide.QtGui.QTextCursor.selectedText() instead.
		"""
		res = super(QTextCursor,self).selection()
		isinstance(res,QtGui.QTextDocumentFragment)
		return res
	#----------------------------------------------------------------------
	def selectionEnd(self):
		"""
		Returns the end of the selection or PySide.QtGui.QTextCursor.position() if the cursor doesnt have a selection.
		"""
		res = super(QTextCursor,self).selectionEnd()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def selectionStart(self):
		"""
		Returns the start of the selection or PySide.QtGui.QTextCursor.position() if the cursor doesnt have a selection.
		"""
		res = super(QTextCursor,self).selectionStart()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def verticalMovementX(self):
		"""
		Returns the visual x position for vertical cursor movements.
		A value of -1 indicates no predefined x position
		It will then be set automatically the next time the cursor moves up or down.
		"""
		res = super(QTextCursor,self).verticalMovementX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def visualNavigation(self):
		"""
		Returns true if the cursor does visual navigation; otherwise returns false.
		Visual navigation means skipping over hidden text pragraphs
		The default is false.
		"""
		res = super(QTextCursor,self).visualNavigation()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def createList(self,*args,**kwargs):
		"""
		createList(style)
			style=QtGui.QTextListFormat.Style

		createList(format)
			format=QtGui.QTextListFormat


		"""
		res = super(QTextCursor,self).createList(*args,**kwargs)
		isinstance(res,QtGui.QTextList)
		return res
	#----------------------------------------------------------------------
	def insertBlock(self,*args,**kwargs):
		"""
		insertBlock(format,charFormat)
			format=QtGui.QTextBlockFormat
			charFormat=QtGui.QTextCharFormat

		insertBlock(format)
			format=QtGui.QTextBlockFormat

		This is an overloaded function.
		Inserts a new empty block at the cursor PySide.QtGui.QTextCursor.position() with block format format and charFormat as block char format.
		"""
		res = super(QTextCursor,self).insertBlock(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def insertFragment(self,fragment):
		"""
		insertFragment(fragment)
			fragment=QtGui.QTextDocumentFragment

		Inserts the text fragment at the current PySide.QtGui.QTextCursor.position() .
		"""
		res = super(QTextCursor,self).insertFragment(fragment)
		return res
	#----------------------------------------------------------------------
	def insertFrame(self,format):
		"""
		insertFrame(format)
			format=QtGui.QTextFrameFormat

		Inserts a frame with the given format at the current cursor PySide.QtGui.QTextCursor.position() , moves the cursor PySide.QtGui.QTextCursor.position() inside the frame, and returns the frame.
		If the cursor holds a selection, the whole selection is moved inside the frame.
		"""
		res = super(QTextCursor,self).insertFrame(format)
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def insertHtml(self,html):
		"""
		insertHtml(html)
			html=unicode

		Inserts the text html at the current PySide.QtGui.QTextCursor.position()
		The text is interpreted as HTML.
		"""
		res = super(QTextCursor,self).insertHtml(html)
		return res
	#----------------------------------------------------------------------
	def insertImage(self,*args,**kwargs):
		"""
		insertImage(format,alignment)
			format=QtGui.QTextImageFormat
			alignment=QtGui.QTextFrameFormat.Position

		insertImage(format)
			format=QtGui.QTextImageFormat

		insertImage(image,name=None)
			image=QtGui.QImage
			name=unicode

		insertImage(name)
			name=unicode


		"""
		res = super(QTextCursor,self).insertImage(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def insertList(self,*args,**kwargs):
		"""
		insertList(format)
			format=QtGui.QTextListFormat

		insertList(style)
			style=QtGui.QTextListFormat.Style

		Inserts a new block at the current position and makes it the first list item of a newly created list with the given format
		Returns the created list.
		"""
		res = super(QTextCursor,self).insertList(*args,**kwargs)
		isinstance(res,QtGui.QTextList)
		return res
	#----------------------------------------------------------------------
	def insertTable(self,*args,**kwargs):
		"""
		insertTable(rows,cols)
			rows=QtCore.int
			cols=QtCore.int

		insertTable(rows,cols,format)
			rows=QtCore.int
			cols=QtCore.int
			format=QtGui.QTextTableFormat

		This is an overloaded function.
		Creates a new table with the given number of rows and columns , inserts it at the current cursor PySide.QtGui.QTextCursor.position() in the document, and returns the table object
		The cursor is moved to the beginning of the first cell.
		There must be at least one row and one column in the table.
		"""
		res = super(QTextCursor,self).insertTable(*args,**kwargs)
		isinstance(res,QtGui.QTextTable)
		return res
	#----------------------------------------------------------------------
	def insertText(self,*args,**kwargs):
		"""
		insertText(text)
			text=unicode

		insertText(text,format)
			text=unicode
			format=QtGui.QTextCharFormat

		Inserts text at the current position, using the current character format.
		If there is a selection, the selection is deleted and replaced by text , for example:
		This clears any existing selection, selects the word at the cursor (i.e
		from PySide.QtGui.QTextCursor.position() forward), and replaces the selection with the phrase Hello World.
		Any ASCII linefeed characters (n) in the inserted text are transformed into unicode block separators, corresponding to PySide.QtGui.QTextCursor.insertBlock() calls.
		"""
		res = super(QTextCursor,self).insertText(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def isCopyOf(self,other):
		"""
		isCopyOf(other)
			other=QtGui.QTextCursor

		Returns true if this cursor and other are copies of each other, i.e
		one of them was created as a copy of the other and neither has moved since
		This is much stricter than equality.
		"""
		res = super(QTextCursor,self).isCopyOf(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def mergeBlockCharFormat(self,modifier):
		"""
		mergeBlockCharFormat(modifier)
			modifier=QtGui.QTextCharFormat

		Modifies the block char format of the current block (or all blocks that are contained in the selection) with the block format specified by modifier .
		"""
		res = super(QTextCursor,self).mergeBlockCharFormat(modifier)
		return res
	#----------------------------------------------------------------------
	def mergeBlockFormat(self,modifier):
		"""
		mergeBlockFormat(modifier)
			modifier=QtGui.QTextBlockFormat

		Modifies the block format of the current block (or all blocks that are contained in the selection) with the block format specified by modifier .
		"""
		res = super(QTextCursor,self).mergeBlockFormat(modifier)
		return res
	#----------------------------------------------------------------------
	def mergeCharFormat(self,modifier):
		"""
		mergeCharFormat(modifier)
			modifier=QtGui.QTextCharFormat

		Merges the cursors current character format with the properties described by format modifier
		If the cursor has a selection, this function applies all the properties set in modifier to all the character formats that are part of the selection.
		"""
		res = super(QTextCursor,self).mergeCharFormat(modifier)
		return res
	#----------------------------------------------------------------------
	def movePosition(self,op,arg__2=None,n=None):
		"""
		movePosition(op,arg__2=None,n=None)
			op=QtGui.QTextCursor.MoveOperation
			arg__2=QtGui.QTextCursor.MoveMode
			n=QtCore.int

		Moves the cursor by performing the given operationn times, using the specified mode , and returns true if all operations were completed successfully; otherwise returns false.
		For example, if this function is repeatedly used to seek to the end of the next word, it will eventually fail when the end of the document is reached.
		By default, the move operation is performed once (n = 1).
		If mode is KeepAnchor , the cursor selects the text it moves over
		This is the same effect that the user achieves when they hold down the Shift key and move the cursor with the cursor keys.
		"""
		res = super(QTextCursor,self).movePosition(op,arg__2,n)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,rhs):
		"""
		__ne__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is at a different position in the document as this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__ne__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,rhs):
		"""
		__lt__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is positioned later in the document than this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__lt__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,rhs):
		"""
		__le__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is positioned later or at the same position in the document as this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__le__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,rhs):
		"""
		__eq__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is at the same position in the document as this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__eq__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,rhs):
		"""
		__gt__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is positioned earlier in the document than this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__gt__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,rhs):
		"""
		__ge__(rhs)
			rhs=QtGui.QTextCursor

		Returns true if the other cursor is positioned earlier or at the same position in the document as this cursor; otherwise returns false.
		"""
		res = super(QTextCursor,self).__ge__(rhs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def select(self,selection):
		"""
		select(selection)
			selection=QtGui.QTextCursor.SelectionType

		Selects text in the document according to the given selection .
		"""
		res = super(QTextCursor,self).select(selection)
		return res
	#----------------------------------------------------------------------
	def setBlockCharFormat(self,format):
		"""
		setBlockCharFormat(format)
			format=QtGui.QTextCharFormat

		Sets the block char format of the current block (or all blocks that are contained in the selection) to format .
		"""
		res = super(QTextCursor,self).setBlockCharFormat(format)
		return res
	#----------------------------------------------------------------------
	def setBlockFormat(self,format):
		"""
		setBlockFormat(format)
			format=QtGui.QTextBlockFormat

		Sets the block format of the current block (or all blocks that are contained in the selection) to format .
		"""
		res = super(QTextCursor,self).setBlockFormat(format)
		return res
	#----------------------------------------------------------------------
	def setCharFormat(self,format):
		"""
		setCharFormat(format)
			format=QtGui.QTextCharFormat

		Sets the cursors current character format to the given format
		If the cursor has a selection, the given format is applied to the current selection.
		"""
		res = super(QTextCursor,self).setCharFormat(format)
		return res
	#----------------------------------------------------------------------
	def setKeepPositionOnInsert(self,b):
		"""
		setKeepPositionOnInsert(b)
			b=QtCore.bool

		Defines whether the cursor should keep its current position when text gets inserted at the current position of the cursor.
		If b is true, the cursor keeps its current position when text gets inserted at the positing of the cursor
		If b is false, the cursor moves along with the inserted text.
		The default is false.
		Note that a cursor always moves when text is inserted before the current position of the cursor, and it always keeps its position when text is inserted after the current position of the cursor.
		"""
		res = super(QTextCursor,self).setKeepPositionOnInsert(b)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,pos,mode=None):
		"""
		setPosition(pos,mode=None)
			pos=QtCore.int
			mode=QtGui.QTextCursor.MoveMode

		Moves the cursor to the absolute position in the document specified by pos using a MoveMode specified by m
		The cursor is positioned between characters.
		"""
		res = super(QTextCursor,self).setPosition(pos,mode)
		return res
	#----------------------------------------------------------------------
	def setVerticalMovementX(self,x):
		"""
		setVerticalMovementX(x)
			x=QtCore.int

		Sets the visual x position for vertical cursor movements to x .
		The vertical movement x position is cleared automatically when the cursor moves horizontally, and kept unchanged when the cursor moves vertically
		The mechanism allows the cursor to move up and down on a visually straight line with proportional fonts, and to gently jump over short lines.
		A value of -1 indicates no predefined x position
		It will then be set automatically the next time the cursor moves up or down.
		"""
		res = super(QTextCursor,self).setVerticalMovementX(x)
		return res
	#----------------------------------------------------------------------
	def setVisualNavigation(self,b):
		"""
		setVisualNavigation(b)
			b=QtCore.bool

		Sets visual navigation to b .
		Visual navigation means skipping over hidden text pragraphs
		The default is false.
		"""
		res = super(QTextCursor,self).setVisualNavigation(b)
		return res
