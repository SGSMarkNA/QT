from PySide import QtGui, QtCore

class QSyntaxHighlighter(QtGui.QSyntaxHighlighter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSyntaxHighlighter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentBlock(self):
		"""
		Returns the current text block.
		"""
		res = super(QSyntaxHighlighter,self).currentBlock()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def currentBlockState(self):
		"""
		Returns the state of the current text block
		If no value is set, the returned value is -1.
		"""
		res = super(QSyntaxHighlighter,self).currentBlockState()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentBlockUserData(self):
		"""
		Returns the PySide.QtGui.QTextBlockUserData object previously attached to the current text block.
		"""
		res = super(QSyntaxHighlighter,self).currentBlockUserData()
		isinstance(res,QtGui.QTextBlockUserData)
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the PySide.QtGui.QTextDocument on which this syntax highlighter is installed.
		"""
		res = super(QSyntaxHighlighter,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def previousBlockState(self):
		"""
		Returns the end state of the text block previous to the syntax highlighters current block
		If no value was previously set, the returned value is -1.
		"""
		res = super(QSyntaxHighlighter,self).previousBlockState()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def format(self,pos):
		"""
		format(pos)
			pos=QtCore.int

		Returns the format at position inside the syntax highlighters current text block.
		"""
		res = super(QSyntaxHighlighter,self).format(pos)
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def highlightBlock(self,text):
		"""
		highlightBlock(text)
			text=unicode

		Highlights the given text block
		This function is called when necessary by the rich text engine, i.e
		on text blocks which have changed.
		To provide your own syntax highlighting, you must subclass PySide.QtGui.QSyntaxHighlighter and reimplement PySide.QtGui.QSyntaxHighlighter.highlightBlock()
		In your reimplementation you should parse the blocks text and call PySide.QtGui.QSyntaxHighlighter.setFormat() as often as necessary to apply any font and color changes that you require
		For example:
		Some syntaxes can have constructs that span several text blocks
		For example, a C++ syntax highlighter should be able to cope with /*...*/ multiline comments
		To deal with these cases it is necessary to know the end state of the previous text block (e.g
		in comment).
		Inside your PySide.QtGui.QSyntaxHighlighter.highlightBlock() implementation you can query the end state of the previous text block using the PySide.QtGui.QSyntaxHighlighter.previousBlockState() function
		After parsing the block you can save the last state using PySide.QtGui.QSyntaxHighlighter.setCurrentBlockState() .
		The PySide.QtGui.QSyntaxHighlighter.currentBlockState() and PySide.QtGui.QSyntaxHighlighter.previousBlockState() functions return an int value
		If no state is set, the returned value is -1
		You can designate any other value to identify any given state using the PySide.QtGui.QSyntaxHighlighter.setCurrentBlockState() function
		Once the state is set the PySide.QtGui.QTextBlock keeps that value until it is set set again or until the corresponding paragraph of text gets deleted.
		For example, if youre writing a simple C++ syntax highlighter, you might designate 1 to signify in comment
		For a text block that ended in the middle of a comment youd set 1 using setCurrentBlockState, and for other paragraphs youd set 0
		In your parsing code if the return value of PySide.QtGui.QSyntaxHighlighter.previousBlockState() is 1, you would highlight the text as a C++ comment until you reached the closing */ .
		"""
		res = super(QSyntaxHighlighter,self).highlightBlock(text)
		return res
	#----------------------------------------------------------------------
	def setCurrentBlockState(self,newState):
		"""
		setCurrentBlockState(newState)
			newState=QtCore.int

		Sets the state of the current text block to newState .
		"""
		res = super(QSyntaxHighlighter,self).setCurrentBlockState(newState)
		return res
	#----------------------------------------------------------------------
	def setCurrentBlockUserData(self,data):
		"""
		setCurrentBlockUserData(data)
			data=QtGui.QTextBlockUserData

		Attaches the given data to the current text block
		The ownership is passed to the underlying text document, i.e
		the provided PySide.QtGui.QTextBlockUserData object will be deleted if the corresponding text block gets deleted.
		PySide.QtGui.QTextBlockUserData can be used to store custom settings
		In the case of syntax highlighting, it is in particular interesting as cache storage for information that you may figure out while parsing the paragraphs text.
		For example while parsing the text, you can keep track of parenthesis characters that you encounter ({[( and the like), and store their relative position and the actual PySide.QtCore.QChar in a simple class derived from PySide.QtGui.QTextBlockUserData :
		During cursor navigation in the associated editor, you can ask the current PySide.QtGui.QTextBlock (retrieved using the QTextCursor.block() function) if it has a user data object set and cast it to your BlockData object
		Then you can check if the current cursor position matches with a previously recorded parenthesis position, and, depending on the type of parenthesis (opening or closing), find the next opening or closing parenthesis on the same level.
		In this way you can do a visual parenthesis matching and highlight from the current cursor position to the matching parenthesis
		That makes it easier to spot a missing parenthesis in your code and to find where a corresponding opening/closing parenthesis is when editing parenthesis intensive code.
		"""
		res = super(QSyntaxHighlighter,self).setCurrentBlockUserData(data)
		return res
	#----------------------------------------------------------------------
	def setDocument(self,doc):
		"""
		setDocument(doc)
			doc=QtGui.QTextDocument

		Installs the syntax highlighter on the given PySide.QtGui.QTextDocument doc
		A PySide.QtGui.QSyntaxHighlighter can only be used with one document at a time.
		"""
		res = super(QSyntaxHighlighter,self).setDocument(doc)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,*args,**kwargs):
		"""
		setFormat(start,count,font)
			start=QtCore.int
			count=QtCore.int
			font=QtGui.QFont

		setFormat(start,count,color)
			start=QtCore.int
			count=QtCore.int
			color=QtGui.QColor

		setFormat(start,count,format)
			start=QtCore.int
			count=QtCore.int
			format=QtGui.QTextCharFormat

		This is an overloaded function.
		The specified font is applied to the current text block from the start position for a length of count characters.
		The other attributes of the current text block, e.g
		the font and background color, are reset to default values.
		"""
		res = super(QSyntaxHighlighter,self).setFormat(*args,**kwargs)
		return res
