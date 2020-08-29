from PySide import QtGui, QtCore

class QLayoutItem(QtGui.QLayoutItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLayoutItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		Returns the alignment of this item.
		"""
		res = super(QLayoutItem,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def controlTypes(self):
		"""
		Returns the control type(s) for the layout item
		For a PySide.QtGui.QWidgetItem , the control type comes from the widgets size policy; for a PySide.QtGui.QLayoutItem , the control types is derived from the layouts contents.
		"""
		res = super(QLayoutItem,self).controlTypes()
		isinstance(res,QtGui.QSizePolicy.ControlTypes)
		return res
	#----------------------------------------------------------------------
	def expandingDirections(self):
		"""
		Returns whether this layout item can make use of more space than PySide.QtGui.QLayoutItem.sizeHint()
		A value of Qt.Vertical or Qt.Horizontal means that it wants to grow in only one dimension, whereas Qt.Vertical | Qt.Horizontal means that it wants to grow in both dimensions.
		"""
		res = super(QLayoutItem,self).expandingDirections()
		isinstance(res,QtCore.Qt.Orientations)
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		Returns the rectangle covered by this layout item.
		"""
		res = super(QLayoutItem,self).geometry()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def hasHeightForWidth(self):
		"""
		Returns true if this layouts preferred height depends on its width; otherwise returns false
		The default implementation returns false.
		Reimplement this function in layout managers that support height for width.
		"""
		res = super(QLayoutItem,self).hasHeightForWidth()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def invalidate(self):
		"""
		Invalidates any cached information in this layout item.
		"""
		res = super(QLayoutItem,self).invalidate()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Implemented in subclasses to return whether this item is empty, i.e
		whether it contains any widgets.
		"""
		res = super(QLayoutItem,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def layout(self):
		"""
		If this item is a PySide.QtGui.QLayout , it is returned as a PySide.QtGui.QLayout ; otherwise 0 is returned
		This function provides type-safe casting.
		"""
		res = super(QLayoutItem,self).layout()
		isinstance(res,QtGui.QLayout)
		return res
	#----------------------------------------------------------------------
	def maximumSize(self):
		"""
		Implemented in subclasses to return the maximum size of this item.
		"""
		res = super(QLayoutItem,self).maximumSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def minimumSize(self):
		"""
		Implemented in subclasses to return the minimum size of this item.
		"""
		res = super(QLayoutItem,self).minimumSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		Implemented in subclasses to return the preferred size of this item.
		"""
		res = super(QLayoutItem,self).sizeHint()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def spacerItem(self):
		"""
		If this item is a PySide.QtGui.QSpacerItem , it is returned as a PySide.QtGui.QSpacerItem ; otherwise 0 is returned
		This function provides type-safe casting.
		"""
		res = super(QLayoutItem,self).spacerItem()
		isinstance(res,QtGui.QSpacerItem)
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		If this item is a PySide.QtGui.QWidget , it is returned as a PySide.QtGui.QWidget ; otherwise 0 is returned
		This function provides type-safe casting.
		"""
		res = super(QLayoutItem,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def heightForWidth(self,arg__1):
		"""
		heightForWidth(arg__1)
			arg__1=QtCore.int

		Returns the preferred height for this layout item, given the width w .
		The default implementation returns -1, indicating that the preferred height is independent of the width of the item
		Using the function PySide.QtGui.QLayoutItem.hasHeightForWidth() will typically be much faster than calling this function and testing for -1.
		Reimplement this function in layout managers that support height for width
		A typical implementation will look like this:
		Caching is strongly recommended; without it layout will take exponential time.
		"""
		res = super(QLayoutItem,self).heightForWidth(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minimumHeightForWidth(self,arg__1):
		"""
		minimumHeightForWidth(arg__1)
			arg__1=QtCore.int

		Returns the minimum height this widget needs for the given width, w
		The default implementation simply returns heightForWidth(w ).
		"""
		res = super(QLayoutItem,self).minimumHeightForWidth(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,a):
		"""
		setAlignment(a)
			a=QtCore.Qt.Alignment


		"""
		res = super(QLayoutItem,self).setAlignment(a)
		return res
	#----------------------------------------------------------------------
	def setGeometry(self,arg__1):
		"""
		setGeometry(arg__1)
			arg__1=QtCore.QRect

		Implemented in subclasses to set this items geometry to r .
		"""
		res = super(QLayoutItem,self).setGeometry(arg__1)
		return res
