from PySide import QtGui, QtCore

class QItemDelegate(QtGui.QItemDelegate):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QItemDelegate,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasClipping(self):
		"""
		This property holds if the delegate should clip the paint events.
		This property will set the paint clip to the size of the item
		The default value is on
		It is useful for cases such as when images are larger than the size of the item.
		"""
		res = super(QItemDelegate,self).hasClipping()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def itemEditorFactory(self):
		"""
		Returns the editor factory used by the item delegate
		If no editor factory is set, the function will return null.
		"""
		res = super(QItemDelegate,self).itemEditorFactory()
		isinstance(res,QtGui.QItemEditorFactory)
		return res
	#----------------------------------------------------------------------
	def check(self,option,bounding,variant):
		"""
		check(option,bounding,variant)
			option=QtGui.QStyleOptionViewItem
			bounding=QtCore.QRect
			variant=object

		Note that on Mac, if /usr/include/AssertMacros.h is included prior to PySide.QtGui.QItemDelegate , and the application is building in debug mode, the check(assertion) will conflict with QItemDelegate::check.
		To avoid this problem, add
		#ifdef check #undef check #endif
		after including AssertMacros.h
		"""
		res = super(QItemDelegate,self).check(option,bounding,variant)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def decoration(self,option,variant):
		"""
		decoration(option,variant)
			option=QtGui.QStyleOptionViewItem
			variant=object

		Returns the pixmap used to decorate the root of the item view
		The style option controls the appearance of the root; the variant refers to the data associated with an item.
		"""
		res = super(QItemDelegate,self).decoration(option,variant)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def drawBackground(self,painter,option,index):
		"""
		drawBackground(painter,option,index)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionViewItem
			index=QtCore.QModelIndex

		Renders the item background for the given index , using the given painter and style option .
		"""
		res = super(QItemDelegate,self).drawBackground(painter,option,index)
		return res
	#----------------------------------------------------------------------
	def drawCheck(self,painter,option,rect,state):
		"""
		drawCheck(painter,option,rect,state)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionViewItem
			rect=QtCore.QRect
			state=QtCore.Qt.CheckState


		"""
		res = super(QItemDelegate,self).drawCheck(painter,option,rect,state)
		return res
	#----------------------------------------------------------------------
	def drawDecoration(self,painter,option,rect,pixmap):
		"""
		drawDecoration(painter,option,rect,pixmap)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionViewItem
			rect=QtCore.QRect
			pixmap=QtGui.QPixmap

		Renders the decoration pixmap within the rectangle specified by rect using the given painter and style option .
		"""
		res = super(QItemDelegate,self).drawDecoration(painter,option,rect,pixmap)
		return res
	#----------------------------------------------------------------------
	def drawDisplay(self,painter,option,rect,text):
		"""
		drawDisplay(painter,option,rect,text)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionViewItem
			rect=QtCore.QRect
			text=unicode

		Renders the item view text within the rectangle specified by rect using the given painter and style option .
		"""
		res = super(QItemDelegate,self).drawDisplay(painter,option,rect,text)
		return res
	#----------------------------------------------------------------------
	def drawFocus(self,painter,option,rect):
		"""
		drawFocus(painter,option,rect)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionViewItem
			rect=QtCore.QRect

		Renders the region within the rectangle specified by rect , indicating that it has the focus, using the given painter and style option .
		"""
		res = super(QItemDelegate,self).drawFocus(painter,option,rect)
		return res
	#----------------------------------------------------------------------
	def rect(self,option,index,role):
		"""
		rect(option,index,role)
			option=QtGui.QStyleOptionViewItem
			index=QtCore.QModelIndex
			role=QtCore.int


		"""
		res = super(QItemDelegate,self).rect(option,index,role)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def setClipping(self,clip):
		"""
		setClipping(clip)
			clip=QtCore.bool

		This property holds if the delegate should clip the paint events.
		This property will set the paint clip to the size of the item
		The default value is on
		It is useful for cases such as when images are larger than the size of the item.
		"""
		res = super(QItemDelegate,self).setClipping(clip)
		return res
	#----------------------------------------------------------------------
	def setItemEditorFactory(self,factory):
		"""
		setItemEditorFactory(factory)
			factory=QtGui.QItemEditorFactory

		Sets the editor factory to be used by the item delegate to be the factory specified
		If no editor factory is set, the item delegate will use the default editor factory.
		"""
		res = super(QItemDelegate,self).setItemEditorFactory(factory)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,index,option):
		"""
		setOptions(index,option)
			index=QtCore.QModelIndex
			option=QtGui.QStyleOptionViewItem


		"""
		res = super(QItemDelegate,self).setOptions(index,option)
		isinstance(res,QtGui.QStyleOptionViewItem)
		return res
	#----------------------------------------------------------------------
	def textRectangle(self,painter,rect,font,text):
		"""
		textRectangle(painter,rect,font,text)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			font=QtGui.QFont
			text=unicode


		"""
		res = super(QItemDelegate,self).textRectangle(painter,rect,font,text)
		isinstance(res,QtCore.QRect)
		return res
