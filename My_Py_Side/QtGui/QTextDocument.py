from PySide import QtGui, QtCore

class QTextDocument(QtGui.QTextDocument):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextDocument,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def adjustSize(self):
		"""
		Adjusts the document to a reasonable size.
		"""
		res = super(QTextDocument,self).adjustSize()
		return res
	#----------------------------------------------------------------------
	def allFormats(self):
		"""
		Returns a vector of text formats for all the formats used in the document.
		"""
		res = super(QTextDocument,self).allFormats()
		return res
	#----------------------------------------------------------------------
	def availableRedoSteps(self):
		"""
		Returns the number of available redo steps.
		"""
		res = super(QTextDocument,self).availableRedoSteps()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def availableUndoSteps(self):
		"""
		Returns the number of available undo steps.
		"""
		res = super(QTextDocument,self).availableUndoSteps()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def begin(self):
		"""
		Returns the documents first text block.
		"""
		res = super(QTextDocument,self).begin()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def blockCount(self):
		"""
		Returns the number of text blocks in the document.
		The value of this property is undefined in documents with tables or frames.
		By default, if defined, this property contains a value of 1.
		"""
		res = super(QTextDocument,self).blockCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def characterCount(self):
		"""
		Returns the number of characters of this document.
		"""
		res = super(QTextDocument,self).characterCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the document.
		"""
		res = super(QTextDocument,self).clear()
		return res
	#----------------------------------------------------------------------
	def contentsChanged(self):
		"""

		"""
		res = super(QTextDocument,self).contentsChanged()
		return res
	#----------------------------------------------------------------------
	def defaultFont(self):
		"""
		This property holds the default font used to display the documents text.
		"""
		res = super(QTextDocument,self).defaultFont()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def defaultStyleSheet(self):
		"""
		The default style sheet is applied to all newly HTML formatted text that is inserted into the document, for example using PySide.QtGui.QTextDocument.setHtml() or QTextCursor.insertHtml() .
		The style sheet needs to be compliant to CSS 2.1 syntax.
		"""
		res = super(QTextDocument,self).defaultStyleSheet()
		return res
	#----------------------------------------------------------------------
	def defaultTextOption(self):
		"""
		The default text option is used on all PySide.QtGui.QTextLayout objects in the document
		This allows setting global properties for the document such as the default word wrap mode.
		"""
		res = super(QTextDocument,self).defaultTextOption()
		isinstance(res,QtGui.QTextOption)
		return res
	#----------------------------------------------------------------------
	def documentLayout(self):
		"""
		Returns the document layout for this document.
		"""
		res = super(QTextDocument,self).documentLayout()
		isinstance(res,QtGui.QAbstractTextDocumentLayout)
		return res
	#----------------------------------------------------------------------
	def documentLayoutChanged(self):
		"""

		"""
		res = super(QTextDocument,self).documentLayoutChanged()
		return res
	#----------------------------------------------------------------------
	def documentMargin(self):
		"""
		The margin around the document
		The default is 4.
		"""
		res = super(QTextDocument,self).documentMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def end(self):
		"""
		This function returns a block to test for the end of the document while iterating over it.
		The block returned is invalid and represents the block after the last block in the document
		You can use PySide.QtGui.QTextDocument.lastBlock() to retrieve the last valid block of the document.
		"""
		res = super(QTextDocument,self).end()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def firstBlock(self):
		"""
		Returns the documents first text block.
		"""
		res = super(QTextDocument,self).firstBlock()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def idealWidth(self):
		"""
		Returns the ideal width of the text document
		The ideal width is the actually used width of the document without optional alignments taken into account
		It is always <= PySide.QtGui.QTextDocument.size()
		width() .
		"""
		res = super(QTextDocument,self).idealWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def indentWidth(self):
		"""
		Returns the width used for text list and text block indenting.
		The indent properties of PySide.QtGui.QTextListFormat and PySide.QtGui.QTextBlockFormat specify multiples of this value
		The default indent width is 40.
		"""
		res = super(QTextDocument,self).indentWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the document is empty; otherwise returns false.
		"""
		res = super(QTextDocument,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isModified(self):
		"""
		This property holds whether the document has been modified by the user.
		By default, this property is false.
		"""
		res = super(QTextDocument,self).isModified()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRedoAvailable(self):
		"""
		Returns true if redo is available; otherwise returns false.
		"""
		res = super(QTextDocument,self).isRedoAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUndoAvailable(self):
		"""
		Returns true if undo is available; otherwise returns false.
		"""
		res = super(QTextDocument,self).isUndoAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUndoRedoEnabled(self):
		"""
		This property holds whether undo/redo are enabled for this document.
		This defaults to true
		If disabled, the undo stack is cleared and no items will be added to it.
		"""
		res = super(QTextDocument,self).isUndoRedoEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lastBlock(self):
		"""
		Returns the documents last (valid) text block.
		"""
		res = super(QTextDocument,self).lastBlock()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def lineCount(self):
		"""
		Returns the number of lines of this document (if the layout supports this)
		Otherwise, this is identical to the number of blocks.
		"""
		res = super(QTextDocument,self).lineCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maximumBlockCount(self):
		"""
		This property Specifies the limit for blocks in the document..
		Specifies the maximum number of blocks the document may have
		If there are more blocks in the document that specified with this property blocks are removed from the beginning of the document.
		A negative or zero value specifies that the document may contain an unlimited amount of blocks.
		The default value is 0.
		Note that setting this property will apply the limit immediately to the document contents.
		Setting this property also disables the undo redo history.
		This property is undefined in documents with tables or frames.
		"""
		res = super(QTextDocument,self).maximumBlockCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pageCount(self):
		"""
		returns the number of pages in this document.
		"""
		res = super(QTextDocument,self).pageCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pageSize(self):
		"""
		This property holds the page size that should be used for laying out the document.
		By default, for a newly-created, empty document, this property contains an undefined size.
		"""
		res = super(QTextDocument,self).pageSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def revision(self):
		"""
		Returns the documents revision (if undo is enabled).
		The revision is guaranteed to increase when a document that is not modified is edited.
		"""
		res = super(QTextDocument,self).revision()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def rootFrame(self):
		"""
		Returns the documents root frame.
		"""
		res = super(QTextDocument,self).rootFrame()
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the actual size of the document
		This is equivalent to PySide.QtGui.QTextDocument.documentLayout() ->documentSize();
		The size of the document can be changed either by setting a text width or setting an entire page size.
		Note that the width is always >= PySide.QtGui.QTextDocument.pageSize()
		width() .
		By default, for a newly-created, empty document, this property contains a configuration-dependent size.
		"""
		res = super(QTextDocument,self).size()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def textWidth(self):
		"""
		The text width specifies the preferred width for text in the document
		If the text (or content in general) is wider than the specified with it is broken into multiple lines and grows vertically
		If the text cannot be broken into multiple lines to fit into the specified text width it will be larger and the PySide.QtGui.QTextDocument.size() and the PySide.QtGui.QTextDocument.idealWidth() property will reflect that.
		If the text width is set to -1 then the text will not be broken into multiple lines unless it is enforced through an explicit line break or a new paragraph.
		The default value is -1.
		Setting the text width will also set the page height to -1, causing the document to grow or shrink vertically in a continuous way
		If you want the document layout to break the text into multiple pages then you have to set the PySide.QtGui.QTextDocument.pageSize() property instead.
		"""
		res = super(QTextDocument,self).textWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		Returns the plain text contained in the document
		If you want formatting information use a PySide.QtGui.QTextCursor instead.
		"""
		res = super(QTextDocument,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def undoCommandAdded(self):
		"""

		"""
		res = super(QTextDocument,self).undoCommandAdded()
		return res
	#----------------------------------------------------------------------
	def useDesignMetrics(self):
		"""
		This property holds whether the document uses design metrics of fonts to improve the accuracy of text layout.
		If this property is set to true, the layout will use design metrics
		Otherwise, the metrics of the paint device as set on QAbstractTextDocumentLayout.setPaintDevice() will be used.
		Using design metrics makes a layout have a width that is no longer dependent on hinting and pixel-rounding
		This means that WYSIWYG text layout becomes possible because the width scales much more linearly based on paintdevice metrics than it would otherwise.
		By default, this property is false.
		"""
		res = super(QTextDocument,self).useDesignMetrics()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def addResource(self,type,name,resource):
		"""
		addResource(type,name,resource)
			type=QtCore.int
			name=QtCore.QUrl
			resource=object

		Adds the resource resource to the resource cache, using type and name as identifiers
		type should be a value from QTextDocument.ResourceType .
		For example, you can add an image as a resource in order to reference it from within the document:
		The image can be inserted into the document using the PySide.QtGui.QTextCursor API:
		Alternatively, you can insert images using the HTML img tag:
		"""
		res = super(QTextDocument,self).addResource(type,name,resource)
		return res
	#----------------------------------------------------------------------
	def characterAt(self,pos):
		"""
		characterAt(pos)
			pos=QtCore.int

		Returns the character at position pos , or a null character if the position is out of range.
		"""
		res = super(QTextDocument,self).characterAt(pos)
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def clearUndoRedoStacks(self,historyToClear=None):
		"""
		clearUndoRedoStacks(historyToClear=None)
			historyToClear=QtGui.QTextDocument.Stacks

		Clears the stacks specified by stacksToClear .
		This method clears any commands on the undo stack, the redo stack, or both (the default)
		If commands are cleared, the appropriate signals are emitted, QTextDocument.undoAvailable() or QTextDocument.redoAvailable() .
		"""
		res = super(QTextDocument,self).clearUndoRedoStacks(historyToClear)
		return res
	#----------------------------------------------------------------------
	def clone(self,parent=None):
		"""
		clone(parent=None)
			parent=QtCore.QObject

		Creates a new PySide.QtGui.QTextDocument that is a copy of this text document
		parent is the parent of the returned text document.
		"""
		res = super(QTextDocument,self).clone(parent)
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def createObject(self,f):
		"""
		createObject(f)
			f=QtGui.QTextFormat

		Creates and returns a new document object (a PySide.QtGui.QTextObject ), based on the given format .
		QTextObjects will always get created through this method, so you must reimplement it if you use custom text objects inside your document.
		"""
		res = super(QTextDocument,self).createObject(f)
		isinstance(res,QtGui.QTextObject)
		return res
	#----------------------------------------------------------------------
	def drawContents(self,painter,rect=None):
		"""
		drawContents(painter,rect=None)
			painter=QtGui.QPainter
			rect=QtCore.QRectF

		Draws the content of the document with painter p , clipped to rect
		If rect is a null rectangle (default) then the document is painted unclipped.
		"""
		res = super(QTextDocument,self).drawContents(painter,rect)
		return res
	#----------------------------------------------------------------------
	def find(self,*args,**kwargs):
		"""
		find(subString,from=None,options=None)
			subString=unicode
			from=QtCore.int
			options=QtGui.QTextDocument.FindFlags

		find(subString,from,options=None)
			subString=unicode
			from=QtGui.QTextCursor
			options=QtGui.QTextDocument.FindFlags

		find(expr,from=None,options=None)
			expr=QtCore.QRegExp
			from=QtCore.int
			options=QtGui.QTextDocument.FindFlags

		find(expr,from,options=None)
			expr=QtCore.QRegExp
			from=QtGui.QTextCursor
			options=QtGui.QTextDocument.FindFlags


		"""
		res = super(QTextDocument,self).find(*args,**kwargs)
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def findBlock(self,pos):
		"""
		findBlock(pos)
			pos=QtCore.int

		Returns the text block that contains the pos -th character.
		"""
		res = super(QTextDocument,self).findBlock(pos)
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def findBlockByLineNumber(self,blockNumber):
		"""
		findBlockByLineNumber(blockNumber)
			blockNumber=QtCore.int

		Returns the text block that contains the specified lineNumber .
		"""
		res = super(QTextDocument,self).findBlockByLineNumber(blockNumber)
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def findBlockByNumber(self,blockNumber):
		"""
		findBlockByNumber(blockNumber)
			blockNumber=QtCore.int

		Returns the text block with the specified blockNumber .
		"""
		res = super(QTextDocument,self).findBlockByNumber(blockNumber)
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def frameAt(self,pos):
		"""
		frameAt(pos)
			pos=QtCore.int

		Returns the frame that contains the text cursor position pos .
		"""
		res = super(QTextDocument,self).frameAt(pos)
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def loadResource(self,type,name):
		"""
		loadResource(type,name)
			type=QtCore.int
			name=QtCore.QUrl

		Loads data of the specified type from the resource with the given name .
		This function is called by the rich text engine to request data that isnt directly stored by PySide.QtGui.QTextDocument , but still associated with it
		For example, images are referenced indirectly by the name attribute of a PySide.QtGui.QTextImageFormat object.
		When called by Qt, type is one of the values of QTextDocument.ResourceType .
		If the PySide.QtGui.QTextDocument is a child object of a PySide.QtGui.QTextEdit , PySide.QtGui.QTextBrowser , or a PySide.QtGui.QTextDocument itself then the default implementation tries to retrieve the data from the parent.
		"""
		res = super(QTextDocument,self).loadResource(type,name)
		return res
	#----------------------------------------------------------------------
	def markContentsDirty(self,from,length):
		"""
		markContentsDirty(from,length)
			from=QtCore.int
			length=QtCore.int

		Marks the contents specified by the given position and length as dirty, informing the document that it needs to be laid out again.
		"""
		res = super(QTextDocument,self).markContentsDirty(from,length)
		return res
	#----------------------------------------------------------------------
	def metaInformation(self,info):
		"""
		metaInformation(info)
			info=QtGui.QTextDocument.MetaInformation

		Returns meta information about the document of the type specified by info .
		"""
		res = super(QTextDocument,self).metaInformation(info)
		return res
	#----------------------------------------------------------------------
	def object(self,objectIndex):
		"""
		object(objectIndex)
			objectIndex=QtCore.int

		Returns the text object associated with the given objectIndex .
		"""
		res = super(QTextDocument,self).object(objectIndex)
		isinstance(res,QtGui.QTextObject)
		return res
	#----------------------------------------------------------------------
	def objectForFormat(self,arg__1):
		"""
		objectForFormat(arg__1)
			arg__1=QtGui.QTextFormat

		Returns the text object associated with the format f .
		"""
		res = super(QTextDocument,self).objectForFormat(arg__1)
		isinstance(res,QtGui.QTextObject)
		return res
	#----------------------------------------------------------------------
	def print_(self,printer):
		"""
		print_(printer)
			printer=QtGui.QPrinter

		Prints the document to the given printer
		The PySide.QtGui.QPrinter must be set up before being used with this function.
		This is only a convenience method to print the whole document to the printer.
		If the document is already paginated through a specified height in the PySide.QtGui.QTextDocument.pageSize() property it is printed as-is.
		If the document is not paginated, like for example a document used in a PySide.QtGui.QTextEdit , then a temporary copy of the document is created and the copy is broken into multiple pages according to the size of the PySide.QtGui.QPrinter s paperRect()
		By default a 2 cm margin is set around the document contents
		In addition the current page number is printed at the bottom of each page.
		Note that QPrinter.Selection is not supported as print range with this function since the selection is a property of PySide.QtGui.QTextCursor
		If you have a PySide.QtGui.QTextEdit associated with your PySide.QtGui.QTextDocument then you can use PySide.QtGui.QTextEdit s print() function because PySide.QtGui.QTextEdit has access to the users selection.
		"""
		res = super(QTextDocument,self).print_(printer)
		return res
	#----------------------------------------------------------------------
	def redo(self,cursor):
		"""
		redo(cursor)
			cursor=QtGui.QTextCursor

		Redoes the last editing operation on the document if redo is available .
		The provided cursor is positioned at the end of the location where the edition operation was redone.
		"""
		res = super(QTextDocument,self).redo(cursor)
		return res
	#----------------------------------------------------------------------
	def resource(self,type,name):
		"""
		resource(type,name)
			type=QtCore.int
			name=QtCore.QUrl

		Returns data of the specified type from the resource with the given name .
		This function is called by the rich text engine to request data that isnt directly stored by PySide.QtGui.QTextDocument , but still associated with it
		For example, images are referenced indirectly by the name attribute of a PySide.QtGui.QTextImageFormat object.
		Resources are cached internally in the document
		If a resource can not be found in the cache, loadResource is called to try to load the resource
		loadResource should then use addResource to add the resource to the cache.
		"""
		res = super(QTextDocument,self).resource(type,name)
		return res
	#----------------------------------------------------------------------
	def setDefaultFont(self,font):
		"""
		setDefaultFont(font)
			font=QtGui.QFont

		This property holds the default font used to display the documents text.
		"""
		res = super(QTextDocument,self).setDefaultFont(font)
		return res
	#----------------------------------------------------------------------
	def setDefaultStyleSheet(self,sheet):
		"""
		setDefaultStyleSheet(sheet)
			sheet=unicode

		The default style sheet is applied to all newly HTML formatted text that is inserted into the document, for example using PySide.QtGui.QTextDocument.setHtml() or QTextCursor.insertHtml() .
		The style sheet needs to be compliant to CSS 2.1 syntax.
		"""
		res = super(QTextDocument,self).setDefaultStyleSheet(sheet)
		return res
	#----------------------------------------------------------------------
	def setDefaultTextOption(self,option):
		"""
		setDefaultTextOption(option)
			option=QtGui.QTextOption

		Sets the default text option.
		"""
		res = super(QTextDocument,self).setDefaultTextOption(option)
		return res
	#----------------------------------------------------------------------
	def setDocumentLayout(self,layout):
		"""
		setDocumentLayout(layout)
			layout=QtGui.QAbstractTextDocumentLayout

		Sets the document to use the given layout
		The previous layout is deleted.
		"""
		res = super(QTextDocument,self).setDocumentLayout(layout)
		return res
	#----------------------------------------------------------------------
	def setDocumentMargin(self,margin):
		"""
		setDocumentMargin(margin)
			margin=QtCore.qreal

		The margin around the document
		The default is 4.
		"""
		res = super(QTextDocument,self).setDocumentMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setHtml(self,html):
		"""
		setHtml(html)
			html=unicode

		Replaces the entire contents of the document with the given HTML-formatted text in the html string.
		The HTML formatting is respected as much as possible; for example, <b>bold</b> text will produce text where the first word has a font weight that gives it a bold appearance: bold text.
		"""
		res = super(QTextDocument,self).setHtml(html)
		return res
	#----------------------------------------------------------------------
	def setIndentWidth(self,width):
		"""
		setIndentWidth(width)
			width=QtCore.qreal

		Returns the width used for text list and text block indenting.
		The indent properties of PySide.QtGui.QTextListFormat and PySide.QtGui.QTextBlockFormat specify multiples of this value
		The default indent width is 40.
		"""
		res = super(QTextDocument,self).setIndentWidth(width)
		return res
	#----------------------------------------------------------------------
	def setMaximumBlockCount(self,maximum):
		"""
		setMaximumBlockCount(maximum)
			maximum=QtCore.int

		This property Specifies the limit for blocks in the document..
		Specifies the maximum number of blocks the document may have
		If there are more blocks in the document that specified with this property blocks are removed from the beginning of the document.
		A negative or zero value specifies that the document may contain an unlimited amount of blocks.
		The default value is 0.
		Note that setting this property will apply the limit immediately to the document contents.
		Setting this property also disables the undo redo history.
		This property is undefined in documents with tables or frames.
		"""
		res = super(QTextDocument,self).setMaximumBlockCount(maximum)
		return res
	#----------------------------------------------------------------------
	def setMetaInformation(self,info,arg__2):
		"""
		setMetaInformation(info,arg__2)
			info=QtGui.QTextDocument.MetaInformation
			arg__2=unicode

		Sets the documents meta information of the type specified by info to the given string .
		"""
		res = super(QTextDocument,self).setMetaInformation(info,arg__2)
		return res
	#----------------------------------------------------------------------
	def setPageSize(self,size):
		"""
		setPageSize(size)
			size=QtCore.QSizeF

		This property holds the page size that should be used for laying out the document.
		By default, for a newly-created, empty document, this property contains an undefined size.
		"""
		res = super(QTextDocument,self).setPageSize(size)
		return res
	#----------------------------------------------------------------------
	def setPlainText(self,text):
		"""
		setPlainText(text)
			text=unicode

		Replaces the entire contents of the document with the given plain text .
		"""
		res = super(QTextDocument,self).setPlainText(text)
		return res
	#----------------------------------------------------------------------
	def setTextWidth(self,width):
		"""
		setTextWidth(width)
			width=QtCore.qreal

		The text width specifies the preferred width for text in the document
		If the text (or content in general) is wider than the specified with it is broken into multiple lines and grows vertically
		If the text cannot be broken into multiple lines to fit into the specified text width it will be larger and the PySide.QtGui.QTextDocument.size() and the PySide.QtGui.QTextDocument.idealWidth() property will reflect that.
		If the text width is set to -1 then the text will not be broken into multiple lines unless it is enforced through an explicit line break or a new paragraph.
		The default value is -1.
		Setting the text width will also set the page height to -1, causing the document to grow or shrink vertically in a continuous way
		If you want the document layout to break the text into multiple pages then you have to set the PySide.QtGui.QTextDocument.pageSize() property instead.
		"""
		res = super(QTextDocument,self).setTextWidth(width)
		return res
	#----------------------------------------------------------------------
	def setUndoRedoEnabled(self,enable):
		"""
		setUndoRedoEnabled(enable)
			enable=QtCore.bool

		This property holds whether undo/redo are enabled for this document.
		This defaults to true
		If disabled, the undo stack is cleared and no items will be added to it.
		"""
		res = super(QTextDocument,self).setUndoRedoEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setUseDesignMetrics(self,b):
		"""
		setUseDesignMetrics(b)
			b=QtCore.bool

		This property holds whether the document uses design metrics of fonts to improve the accuracy of text layout.
		If this property is set to true, the layout will use design metrics
		Otherwise, the metrics of the paint device as set on QAbstractTextDocumentLayout.setPaintDevice() will be used.
		Using design metrics makes a layout have a width that is no longer dependent on hinting and pixel-rounding
		This means that WYSIWYG text layout becomes possible because the width scales much more linearly based on paintdevice metrics than it would otherwise.
		By default, this property is false.
		"""
		res = super(QTextDocument,self).setUseDesignMetrics(b)
		return res
	#----------------------------------------------------------------------
	def toHtml(self,encoding=None):
		"""
		toHtml(encoding=None)
			encoding=QtCore.QByteArray

		Returns a string containing an HTML representation of the document.
		The encoding parameter specifies the value for the charset attribute in the html header
		For example if utf-8 is specified then the beginning of the generated html will look like this:
		If no encoding is specified then no such meta information is generated.
		If you later on convert the returned html string into a byte array for transmission over a network or when saving to disk you should specify the encoding youre going to use for the conversion to a byte array here.
		"""
		res = super(QTextDocument,self).toHtml(encoding)
		return res
	#----------------------------------------------------------------------
	def undo(self,cursor):
		"""
		undo(cursor)
			cursor=QtGui.QTextCursor

		Undoes the last editing operation on the document if undo is available
		The provided cursor is positioned at the end of the location where the edition operation was undone.
		See the Qt Undo Framework documentation for details.
		"""
		res = super(QTextDocument,self).undo(cursor)
		return res
