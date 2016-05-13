from PySide import QtGui, QtCore

class QAbstractTextDocumentLayout(QtGui.QAbstractTextDocumentLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractTextDocumentLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the text document that this layout is operating on.
		"""
		res = super(QAbstractTextDocumentLayout,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def documentSize(self):
		"""
		Returns the total size of the documents layout.
		This information can be used by display widgets to update their scroll bars correctly.
		"""
		res = super(QAbstractTextDocumentLayout,self).documentSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def pageCount(self):
		"""
		Returns the number of pages contained in the layout.
		"""
		res = super(QAbstractTextDocumentLayout,self).pageCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def paintDevice(self):
		"""
		Returns the paint device used to render the documents layout.
		"""
		res = super(QAbstractTextDocumentLayout,self).paintDevice()
		isinstance(res,QtGui.QPaintDevice)
		return res
	#----------------------------------------------------------------------
	def anchorAt(self,pos):
		"""
		anchorAt(pos)
			pos=QtCore.QPointF

		Returns the reference of the anchor the given position , or an empty string if no anchor exists at that point.
		"""
		res = super(QAbstractTextDocumentLayout,self).anchorAt(pos)
		return res
	#----------------------------------------------------------------------
	def blockBoundingRect(self,block):
		"""
		blockBoundingRect(block)
			block=QtGui.QTextBlock

		Returns the bounding rectangle of block .
		"""
		res = super(QAbstractTextDocumentLayout,self).blockBoundingRect(block)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def documentChanged(self,from,charsRemoved,charsAdded):
		"""
		documentChanged(from,charsRemoved,charsAdded)
			from=QtCore.int
			charsRemoved=QtCore.int
			charsAdded=QtCore.int

		This function is called whenever the contents of the document change
		A change occurs when text is inserted, removed, or a combination of these two
		The change is specified by position , charsRemoved , and charsAdded corresponding to the starting character position of the change, the number of characters removed from the document, and the number of characters added.
		For example, when inserting the text Hello into an empty document, charsRemoved would be 0 and charsAdded would be 5 (the length of the string).
		Replacing text is a combination of removing and inserting
		For example, if the text Hello gets replaced by Hi, charsRemoved would be 5 and charsAdded would be 2.
		For subclasses of PySide.QtGui.QAbstractTextDocumentLayout , this is the central function where a large portion of the work to lay out and position document contents is done.
		For example, in a subclass that only arranges blocks of text, an implementation of this function would have to do the following:
		"""
		res = super(QAbstractTextDocumentLayout,self).documentChanged(from,charsRemoved,charsAdded)
		return res
	#----------------------------------------------------------------------
	def draw(self,painter,context):
		"""
		draw(painter,context)
			painter=QtGui.QPainter
			context=QtGui.QAbstractTextDocumentLayout::PaintContext

		Draws the layout with the given painter using the given context .
		"""
		res = super(QAbstractTextDocumentLayout,self).draw(painter,context)
		return res
	#----------------------------------------------------------------------
	def drawInlineObject(self,painter,rect,object,posInDocument,format):
		"""
		drawInlineObject(painter,rect,object,posInDocument,format)
			painter=QtGui.QPainter
			rect=QtCore.QRectF
			object=QtGui.QTextInlineObject
			posInDocument=QtCore.int
			format=QtGui.QTextFormat

		This function is called to draw the inline object, object , with the given painter within the rectangle specified by rect using the specified text format .
		posInDocument specifies the position of the object within the document.
		The default implementation calls drawObject() on the object handlers
		This function is called only within Qt
		Subclasses can reimplement this function to customize the drawing of inline objects.
		"""
		res = super(QAbstractTextDocumentLayout,self).drawInlineObject(painter,rect,object,posInDocument,format)
		return res
	#----------------------------------------------------------------------
	def format(self,pos):
		"""
		format(pos)
			pos=QtCore.int

		Returns the character format that is applicable at the given position .
		"""
		res = super(QAbstractTextDocumentLayout,self).format(pos)
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def formatIndex(self,pos):
		"""
		formatIndex(pos)
			pos=QtCore.int

		Returns the index of the format at position pos .
		"""
		res = super(QAbstractTextDocumentLayout,self).formatIndex(pos)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def frameBoundingRect(self,frame):
		"""
		frameBoundingRect(frame)
			frame=QtGui.QTextFrame

		Returns the bounding rectangle of frame .
		"""
		res = super(QAbstractTextDocumentLayout,self).frameBoundingRect(frame)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def handlerForObject(self,objectType):
		"""
		handlerForObject(objectType)
			objectType=QtCore.int

		Returns a handler for objects of the given objectType .
		"""
		res = super(QAbstractTextDocumentLayout,self).handlerForObject(objectType)
		isinstance(res,QtGui.QTextObjectInterface)
		return res
	#----------------------------------------------------------------------
	def hitTest(self,point,accuracy):
		"""
		hitTest(point,accuracy)
			point=QtCore.QPointF
			accuracy=QtCore.Qt.HitTestAccuracy


		"""
		res = super(QAbstractTextDocumentLayout,self).hitTest(point,accuracy)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def positionInlineObject(self,item,posInDocument,format):
		"""
		positionInlineObject(item,posInDocument,format)
			item=QtGui.QTextInlineObject
			posInDocument=QtCore.int
			format=QtGui.QTextFormat

		Lays out the inline object item using the given text format .
		posInDocument specifies the position of the object within the document.
		The default implementation does nothing
		This function is called only within Qt
		Subclasses can reimplement this function to customize the position of inline objects.
		"""
		res = super(QAbstractTextDocumentLayout,self).positionInlineObject(item,posInDocument,format)
		return res
	#----------------------------------------------------------------------
	def registerHandler(self,objectType,component):
		"""
		registerHandler(objectType,component)
			objectType=QtCore.int
			component=QtCore.QObject

		Registers the given component as a handler for items of the given objectType .
		"""
		res = super(QAbstractTextDocumentLayout,self).registerHandler(objectType,component)
		return res
	#----------------------------------------------------------------------
	def resizeInlineObject(self,item,posInDocument,format):
		"""
		resizeInlineObject(item,posInDocument,format)
			item=QtGui.QTextInlineObject
			posInDocument=QtCore.int
			format=QtGui.QTextFormat

		Sets the size of the inline object item corresponding to the text format .
		posInDocument specifies the position of the object within the document.
		The default implementation resizes the item to the size returned by the object handlers intrinsicSize() function
		This function is called only within Qt
		Subclasses can reimplement this function to customize the resizing of inline objects.
		"""
		res = super(QAbstractTextDocumentLayout,self).resizeInlineObject(item,posInDocument,format)
		return res
	#----------------------------------------------------------------------
	def setPaintDevice(self,device):
		"""
		setPaintDevice(device)
			device=QtGui.QPaintDevice

		Sets the paint device used for rendering the documents layout to the given device .
		"""
		res = super(QAbstractTextDocumentLayout,self).setPaintDevice(device)
		return res
