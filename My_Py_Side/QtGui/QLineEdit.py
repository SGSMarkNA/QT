from PySide import QtGui, QtCore

class QLineEdit(QtGui.QLineEdit):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLineEdit,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the line edit.
		Both horizontal and vertical alignment is allowed here, Qt.AlignJustify will map to Qt.AlignLeft .
		By default, this property contains a combination of Qt.AlignLeft and Qt.AlignVCenter .
		"""
		res = super(QLineEdit,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def backspace(self):
		"""
		If no text is selected, deletes the character to the left of the text cursor and moves the cursor one position to the left
		If any text is selected, the cursor is moved to the beginning of the selected text and the selected text is deleted.
		"""
		res = super(QLineEdit,self).backspace()
		return res
	#----------------------------------------------------------------------
	def completer(self):
		"""
		Returns the current PySide.QtGui.QCompleter that provides completions.
		"""
		res = super(QLineEdit,self).completer()
		isinstance(res,QtGui.QCompleter)
		return res
	#----------------------------------------------------------------------
	def createStandardContextMenu(self):
		"""
		This function creates the standard context menu which is shown when the user clicks on the line edit with the right mouse button
		It is called from the default PySide.QtGui.QLineEdit.contextMenuEvent() handler
		The popup menus ownership is transferred to the caller.
		"""
		res = super(QLineEdit,self).createStandardContextMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def cursorPosition(self):
		"""
		This property holds the current cursor position for this line edit.
		Setting the cursor position causes a repaint when appropriate.
		By default, this property contains a value of 0.
		"""
		res = super(QLineEdit,self).cursorPosition()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def cursorRect(self):
		"""
		Returns a rectangle that includes the lineedit cursor.
		"""
		res = super(QLineEdit,self).cursorRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def del_(self):
		"""
		If no text is selected, deletes the character to the right of the text cursor
		If any text is selected, the cursor is moved to the beginning of the selected text and the selected text is deleted.
		"""
		res = super(QLineEdit,self).del_()
		return res
	#----------------------------------------------------------------------
	def deselect(self):
		"""
		Deselects any selected text.
		"""
		res = super(QLineEdit,self).deselect()
		return res
	#----------------------------------------------------------------------
	def displayText(self):
		"""
		This property holds the displayed text.
		If PySide.QtGui.QLineEdit.echoMode() is Normal this returns the same as PySide.QtGui.QLineEdit.text() ; if QLineEdit.EchoMode is Password or PasswordEchoOnEdit it returns a string of asterisks PySide.QtGui.QLineEdit.text()
		length() characters long, e.g
		******; if QLineEdit.EchoMode is NoEcho returns an empty string, .
		By default, this property contains an empty string.
		"""
		res = super(QLineEdit,self).displayText()
		return res
	#----------------------------------------------------------------------
	def dragEnabled(self):
		"""
		This property holds whether the lineedit starts a drag if the user presses and moves the mouse on some selected text.
		Dragging is disabled by default.
		"""
		res = super(QLineEdit,self).dragEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def echoMode(self):
		"""
		This property holds the line edits echo mode.
		The echo mode determines how the text entered in the line edit is displayed (or echoed) to the user.
		The most common setting is Normal , in which the text entered by the user is displayed verbatim, but PySide.QtGui.QLineEdit also supports modes that allow the entered text to be suppressed or obscured: these include NoEcho , Password and PasswordEchoOnEdit .
		The widgets display and the ability to copy or drag the text is affected by this setting.
		By default, this property is set to Normal .
		"""
		res = super(QLineEdit,self).echoMode()
		isinstance(res,QtGui.QLineEdit.EchoMode)
		return res
	#----------------------------------------------------------------------
	def editingFinished(self):
		"""

		"""
		res = super(QLineEdit,self).editingFinished()
		return res
	#----------------------------------------------------------------------
	def getTextMargins(self):
		"""
		Returns the widgets text margins for left , top , right , and bottom .
		"""
		res = super(QLineEdit,self).getTextMargins()
		return res
	#----------------------------------------------------------------------
	def hasAcceptableInput(self):
		"""
		This property holds whether the input satisfies the PySide.QtGui.QLineEdit.inputMask() and the validator..
		By default, this property is true.
		"""
		res = super(QLineEdit,self).hasAcceptableInput()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasFrame(self):
		"""
		This property holds whether the line edit draws itself with a frame.
		If enabled (the default) the line edit draws itself inside a frame, otherwise the line edit draws itself without any frame.
		"""
		res = super(QLineEdit,self).hasFrame()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasSelectedText(self):
		"""
		This property holds whether there is any text selected.
		PySide.QtGui.QLineEdit.hasSelectedText() returns true if some or all of the text has been selected by the user; otherwise returns false.
		By default, this property is false.
		"""
		res = super(QLineEdit,self).hasSelectedText()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def inputMask(self):
		"""
		This property holds The validation input mask.
		If no mask is set, PySide.QtGui.QLineEdit.inputMask() returns an empty string.
		Sets the PySide.QtGui.QLineEdit s validation mask
		Validators can be used instead of, or in conjunction with masks; see PySide.QtGui.QLineEdit.setValidator() .
		Unset the mask and return to normal PySide.QtGui.QLineEdit operation by passing an empty string () or just calling PySide.QtGui.QLineEdit.setInputMask() with no arguments.
		The table below shows the characters that can be used in an input mask
		A space character, the default character for a blank, is needed for cases where a character is permitted but not required .
		The mask consists of a string of mask characters and separators, optionally followed by a semicolon and the character used for blanks
		The blank characters are always removed from the text after editing.
		Examples:
		To get range control (e.g., for an IP address) use masks together with validators .
		"""
		res = super(QLineEdit,self).inputMask()
		return res
	#----------------------------------------------------------------------
	def isModified(self):
		"""
		This property holds whether the line edits contents has been modified by the user.
		The modified flag is never read by PySide.QtGui.QLineEdit ; it has a default value of false and is changed to true whenever the user changes the line edits contents.
		This is useful for things that need to provide a default value but do not start out knowing what the default should be (perhaps it depends on other fields on the form)
		Start the line edit without the best default, and when the default is known, if modified() returns false (the user hasnt entered any text), insert the default value.
		Calling PySide.QtGui.QLineEdit.setText() resets the modified flag to false.
		"""
		res = super(QLineEdit,self).isModified()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds whether the line edit is read only..
		In read-only mode, the user can still copy the text to the clipboard, or drag and drop the text (if PySide.QtGui.QLineEdit.echoMode() is Normal ), but cannot edit it.
		PySide.QtGui.QLineEdit does not show a cursor in read-only mode.
		By default, this property is false.
		"""
		res = super(QLineEdit,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRedoAvailable(self):
		"""
		This property holds whether redo is available.
		Redo becomes available once the user has performed one or more undo operations on text in the line edit.
		By default, this property is false.
		"""
		res = super(QLineEdit,self).isRedoAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUndoAvailable(self):
		"""
		This property holds whether undo is available.
		Undo becomes available once the user has modified the text in the line edit.
		By default, this property is false.
		"""
		res = super(QLineEdit,self).isUndoAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def maxLength(self):
		"""
		This property holds the maximum permitted length of the text.
		If the text is too long, it is truncated at the limit.
		If truncation occurs any selected text will be unselected, the cursor position is set to 0 and the first part of the string is shown.
		If the line edit has an input mask, the mask defines the maximum string length.
		By default, this property contains a value of 32767.
		"""
		res = super(QLineEdit,self).maxLength()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def placeholderText(self):
		"""
		This property holds the line edits placeholder text.
		Setting this property makes the line edit display a grayed-out placeholder text as long as the PySide.QtGui.QLineEdit.text() is empty and the widget doesnt have focus.
		By default, this property contains an empty string.
		"""
		res = super(QLineEdit,self).placeholderText()
		return res
	#----------------------------------------------------------------------
	def returnPressed(self):
		"""

		"""
		res = super(QLineEdit,self).returnPressed()
		return res
	#----------------------------------------------------------------------
	def selectedText(self):
		"""
		This property holds the selected text.
		If there is no selected text this propertys value is an empty string.
		By default, this property contains an empty string.
		"""
		res = super(QLineEdit,self).selectedText()
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QLineEdit,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def selectionStart(self):
		"""
		PySide.QtGui.QLineEdit.selectionStart() returns the index of the first selected character in the line edit or -1 if no text is selected.
		"""
		res = super(QLineEdit,self).selectionStart()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the line edits text.
		Setting this property clears the selection, clears the undo/redo history, moves the cursor to the end of the line and resets the modified() property to false
		The text is not validated when inserted with PySide.QtGui.QLineEdit.setText() .
		The text is truncated to PySide.QtGui.QLineEdit.maxLength() length.
		By default, this property contains an empty string.
		"""
		res = super(QLineEdit,self).text()
		return res
	#----------------------------------------------------------------------
	def textMargins(self):
		"""
		Returns the widgets text margins.
		"""
		res = super(QLineEdit,self).textMargins()
		isinstance(res,QtCore.QMargins)
		return res
	#----------------------------------------------------------------------
	def validator(self):
		"""
		Returns a pointer to the current input validator, or 0 if no validator has been set.
		"""
		res = super(QLineEdit,self).validator()
		isinstance(res,QtGui.QValidator)
		return res
	#----------------------------------------------------------------------
	def cursorBackward(self,mark,steps=None):
		"""
		cursorBackward(mark,steps=None)
			mark=QtCore.bool
			steps=QtCore.int

		Moves the cursor back steps characters
		If mark is true each character moved over is added to the selection; if mark is false the selection is cleared.
		"""
		res = super(QLineEdit,self).cursorBackward(mark,steps)
		return res
	#----------------------------------------------------------------------
	def cursorForward(self,mark,steps=None):
		"""
		cursorForward(mark,steps=None)
			mark=QtCore.bool
			steps=QtCore.int

		Moves the cursor forward steps characters
		If mark is true each character moved over is added to the selection; if mark is false the selection is cleared.
		"""
		res = super(QLineEdit,self).cursorForward(mark,steps)
		return res
	#----------------------------------------------------------------------
	def cursorPositionAt(self,pos):
		"""
		cursorPositionAt(pos)
			pos=QtCore.QPoint

		Returns the cursor position under the point pos .
		"""
		res = super(QLineEdit,self).cursorPositionAt(pos)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def cursorWordBackward(self,mark):
		"""
		cursorWordBackward(mark)
			mark=QtCore.bool

		Moves the cursor one word backward
		If mark is true, the word is also selected.
		"""
		res = super(QLineEdit,self).cursorWordBackward(mark)
		return res
	#----------------------------------------------------------------------
	def cursorWordForward(self,mark):
		"""
		cursorWordForward(mark)
			mark=QtCore.bool

		Moves the cursor one word forward
		If mark is true, the word is also selected.
		"""
		res = super(QLineEdit,self).cursorWordForward(mark)
		return res
	#----------------------------------------------------------------------
	def end(self,mark):
		"""
		end(mark)
			mark=QtCore.bool

		Moves the text cursor to the end of the line unless it is already there
		If mark is true, text is selected towards the last position; otherwise, any selected text is unselected if the cursor is moved.
		"""
		res = super(QLineEdit,self).end(mark)
		return res
	#----------------------------------------------------------------------
	def home(self,mark):
		"""
		home(mark)
			mark=QtCore.bool

		Moves the text cursor to the beginning of the line unless it is already there
		If mark is true, text is selected towards the first position; otherwise, any selected text is unselected if the cursor is moved.
		"""
		res = super(QLineEdit,self).home(mark)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionFrame

		Initialize option with the values from this PySide.QtGui.QLineEdit
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionFrame or PySide.QtGui.QStyleOptionFrameV2 , but dont want to fill in all the information themselves
		This function will check the version of the PySide.QtGui.QStyleOptionFrame and fill in the additional values for a PySide.QtGui.QStyleOptionFrameV2 .
		"""
		res = super(QLineEdit,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def insert(self,arg__1):
		"""
		insert(arg__1)
			arg__1=unicode

		Deletes any selected text, inserts newText , and validates the result
		If it is valid, it sets it as the new contents of the line edit.
		"""
		res = super(QLineEdit,self).insert(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,flag):
		"""
		setAlignment(flag)
			flag=QtCore.Qt.Alignment

		This property holds the alignment of the line edit.
		Both horizontal and vertical alignment is allowed here, Qt.AlignJustify will map to Qt.AlignLeft .
		By default, this property contains a combination of Qt.AlignLeft and Qt.AlignVCenter .
		"""
		res = super(QLineEdit,self).setAlignment(flag)
		return res
	#----------------------------------------------------------------------
	def setCompleter(self,completer):
		"""
		setCompleter(completer)
			completer=QtGui.QCompleter

		Sets this line edit to provide auto completions from the completer, c
		The completion mode is set using QCompleter.setCompletionMode() .
		To use a PySide.QtGui.QCompleter with a PySide.QtGui.QValidator or QLineEdit.inputMask , you need to ensure that the model provided to PySide.QtGui.QCompleter contains valid entries
		You can use the PySide.QtGui.QSortFilterProxyModel to ensure that the PySide.QtGui.QCompleter s model contains only valid entries.
		If c == 0, PySide.QtGui.QLineEdit.setCompleter() removes the current completer, effectively disabling auto completion.
		"""
		res = super(QLineEdit,self).setCompleter(completer)
		return res
	#----------------------------------------------------------------------
	def setCursorPosition(self,arg__1):
		"""
		setCursorPosition(arg__1)
			arg__1=QtCore.int

		This property holds the current cursor position for this line edit.
		Setting the cursor position causes a repaint when appropriate.
		By default, this property contains a value of 0.
		"""
		res = super(QLineEdit,self).setCursorPosition(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDragEnabled(self,b):
		"""
		setDragEnabled(b)
			b=QtCore.bool

		This property holds whether the lineedit starts a drag if the user presses and moves the mouse on some selected text.
		Dragging is disabled by default.
		"""
		res = super(QLineEdit,self).setDragEnabled(b)
		return res
	#----------------------------------------------------------------------
	def setEchoMode(self,arg__1):
		"""
		setEchoMode(arg__1)
			arg__1=QtGui.QLineEdit.EchoMode

		This property holds the line edits echo mode.
		The echo mode determines how the text entered in the line edit is displayed (or echoed) to the user.
		The most common setting is Normal , in which the text entered by the user is displayed verbatim, but PySide.QtGui.QLineEdit also supports modes that allow the entered text to be suppressed or obscured: these include NoEcho , Password and PasswordEchoOnEdit .
		The widgets display and the ability to copy or drag the text is affected by this setting.
		By default, this property is set to Normal .
		"""
		res = super(QLineEdit,self).setEchoMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFrame(self,arg__1):
		"""
		setFrame(arg__1)
			arg__1=QtCore.bool

		This property holds whether the line edit draws itself with a frame.
		If enabled (the default) the line edit draws itself inside a frame, otherwise the line edit draws itself without any frame.
		"""
		res = super(QLineEdit,self).setFrame(arg__1)
		return res
	#----------------------------------------------------------------------
	def setInputMask(self,inputMask):
		"""
		setInputMask(inputMask)
			inputMask=unicode

		This property holds The validation input mask.
		If no mask is set, PySide.QtGui.QLineEdit.inputMask() returns an empty string.
		Sets the PySide.QtGui.QLineEdit s validation mask
		Validators can be used instead of, or in conjunction with masks; see PySide.QtGui.QLineEdit.setValidator() .
		Unset the mask and return to normal PySide.QtGui.QLineEdit operation by passing an empty string () or just calling PySide.QtGui.QLineEdit.setInputMask() with no arguments.
		The table below shows the characters that can be used in an input mask
		A space character, the default character for a blank, is needed for cases where a character is permitted but not required .
		The mask consists of a string of mask characters and separators, optionally followed by a semicolon and the character used for blanks
		The blank characters are always removed from the text after editing.
		Examples:
		To get range control (e.g., for an IP address) use masks together with validators .
		"""
		res = super(QLineEdit,self).setInputMask(inputMask)
		return res
	#----------------------------------------------------------------------
	def setMaxLength(self,arg__1):
		"""
		setMaxLength(arg__1)
			arg__1=QtCore.int

		This property holds the maximum permitted length of the text.
		If the text is too long, it is truncated at the limit.
		If truncation occurs any selected text will be unselected, the cursor position is set to 0 and the first part of the string is shown.
		If the line edit has an input mask, the mask defines the maximum string length.
		By default, this property contains a value of 32767.
		"""
		res = super(QLineEdit,self).setMaxLength(arg__1)
		return res
	#----------------------------------------------------------------------
	def setModified(self,arg__1):
		"""
		setModified(arg__1)
			arg__1=QtCore.bool

		This property holds whether the line edits contents has been modified by the user.
		The modified flag is never read by PySide.QtGui.QLineEdit ; it has a default value of false and is changed to true whenever the user changes the line edits contents.
		This is useful for things that need to provide a default value but do not start out knowing what the default should be (perhaps it depends on other fields on the form)
		Start the line edit without the best default, and when the default is known, if modified() returns false (the user hasnt entered any text), insert the default value.
		Calling PySide.QtGui.QLineEdit.setText() resets the modified flag to false.
		"""
		res = super(QLineEdit,self).setModified(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPlaceholderText(self,arg__1):
		"""
		setPlaceholderText(arg__1)
			arg__1=unicode

		This property holds the line edits placeholder text.
		Setting this property makes the line edit display a grayed-out placeholder text as long as the PySide.QtGui.QLineEdit.text() is empty and the widget doesnt have focus.
		By default, this property contains an empty string.
		"""
		res = super(QLineEdit,self).setPlaceholderText(arg__1)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,arg__1):
		"""
		setReadOnly(arg__1)
			arg__1=QtCore.bool

		This property holds whether the line edit is read only..
		In read-only mode, the user can still copy the text to the clipboard, or drag and drop the text (if PySide.QtGui.QLineEdit.echoMode() is Normal ), but cannot edit it.
		PySide.QtGui.QLineEdit does not show a cursor in read-only mode.
		By default, this property is false.
		"""
		res = super(QLineEdit,self).setReadOnly(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSelection(self,arg__1,arg__2):
		"""
		setSelection(arg__1,arg__2)
			arg__1=QtCore.int
			arg__2=QtCore.int

		Selects text from position start and for length characters
		Negative lengths are allowed.
		"""
		res = super(QLineEdit,self).setSelection(arg__1,arg__2)
		return res
	#----------------------------------------------------------------------
	def setTextMargins(self,*args,**kwargs):
		"""
		setTextMargins(left,top,right,bottom)
			left=QtCore.int
			top=QtCore.int
			right=QtCore.int
			bottom=QtCore.int

		setTextMargins(margins)
			margins=QtCore.QMargins

		Sets the margins around the text inside the frame to have the sizes left , top , right , and bottom .
		See also PySide.QtGui.QLineEdit.getTextMargins() .
		"""
		res = super(QLineEdit,self).setTextMargins(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setValidator(self,arg__1):
		"""
		setValidator(arg__1)
			arg__1=QtGui.QValidator

		Sets this line edit to only accept input that the validator, v , will accept
		This allows you to place any arbitrary constraints on the text which may be entered.
		If v == 0, PySide.QtGui.QLineEdit.setValidator() removes the current input validator
		The initial setting is to have no input validator (i.e
		any input is accepted up to PySide.QtGui.QLineEdit.maxLength() ).
		"""
		res = super(QLineEdit,self).setValidator(arg__1)
		return res
