from PySide import QtGui, QtCore

class QLayout(QtGui.QLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activate(self):
		"""
		Redoes the layout for PySide.QtGui.QLayout.parentWidget() if necessary.
		You should generally not need to call this because it is automatically called at the most appropriate times
		It returns true if the layout was redone.
		"""
		res = super(QLayout,self).activate()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def contentsMargins(self):
		"""
		Returns the margins used around the layout.
		By default, PySide.QtGui.QLayout uses the values provided by the style
		On most platforms, the margin is 11 pixels in all directions.
		"""
		res = super(QLayout,self).contentsMargins()
		isinstance(res,QtCore.QMargins)
		return res
	#----------------------------------------------------------------------
	def contentsRect(self):
		"""
		Returns the layouts PySide.QtGui.QLayout.geometry() rectangle, but taking into account the contents margins.
		"""
		res = super(QLayout,self).contentsRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Must be implemented in subclasses to return the number of items in the layout.
		"""
		res = super(QLayout,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def getContentsMargins(self):
		"""
		Extracts the left, top, right, and bottom margins used around the layout, and assigns them to *``left`` , *``top`` , *``right`` , and *``bottom`` (unless they are null pointers).
		By default, PySide.QtGui.QLayout uses the values provided by the style
		On most platforms, the margin is 11 pixels in all directions.
		"""
		res = super(QLayout,self).getContentsMargins()
		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		Returns true if the layout is enabled; otherwise returns false.
		"""
		res = super(QLayout,self).isEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def menuBar(self):
		"""
		Returns the menu bar set for this layout, or 0 if no menu bar is set.
		"""
		res = super(QLayout,self).menuBar()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		"""
		Returns the parent widget of this layout, or 0 if this layout is not installed on any widget.
		If the layout is a sub-layout, this function returns the parent widget of the parent layout.
		"""
		res = super(QLayout,self).parentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def sizeConstraint(self):
		"""
		This property holds the resize mode of the layout.
		The default mode is SetDefaultConstraint .
		"""
		res = super(QLayout,self).sizeConstraint()
		isinstance(res,QtGui.QLayout.SizeConstraint)
		return res
	#----------------------------------------------------------------------
	def spacing(self):
		"""
		This property holds the spacing between widgets inside the layout.
		If no value is explicitly set, the layouts spacing is inherited from the parent layout, or from the style settings for the parent widget.
		For PySide.QtGui.QGridLayout and PySide.QtGui.QFormLayout , it is possible to set different horizontal and vertical spacings using PySide.QtGui.QGridLayout.setHorizontalSpacing() and PySide.QtGui.QGridLayout.setVerticalSpacing()
		In that case, PySide.QtGui.QLayout.spacing() returns -1.
		"""
		res = super(QLayout,self).spacing()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def totalMaximumSize(self):
		"""
		Also takes contentsMargins and menu bar into account.
		"""
		res = super(QLayout,self).totalMaximumSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def totalMinimumSize(self):
		"""
		Also takes contentsMargins and menu bar into account.
		"""
		res = super(QLayout,self).totalMinimumSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def totalSizeHint(self):
		"""
		Also takes contentsMargins and menu bar into account.
		"""
		res = super(QLayout,self).totalSizeHint()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def update(self):
		"""
		Updates the layout for PySide.QtGui.QLayout.parentWidget() .
		You should generally not need to call this because it is automatically called at the most appropriate times.
		"""
		res = super(QLayout,self).update()
		return res
	#----------------------------------------------------------------------
	def addChildLayout(self,l):
		"""
		addChildLayout(l)
			l=QtGui.QLayout

		This function is called from addLayout() or insertLayout() functions in subclasses to add layout l as a sub-layout.
		The only scenario in which you need to call it directly is if you implement a custom layout that supports nested layouts.
		"""
		res = super(QLayout,self).addChildLayout(l)
		return res
	#----------------------------------------------------------------------
	def addChildWidget(self,w):
		"""
		addChildWidget(w)
			w=QtGui.QWidget

		This function is called from addWidget() functions in subclasses to add w as a child widget.
		If w is already in a layout, this function will give a warning and remove w from the layout
		This function must therefore be called before adding w to the layouts data structure.
		"""
		res = super(QLayout,self).addChildWidget(w)
		return res
	#----------------------------------------------------------------------
	def addItem(self,arg__1):
		"""
		addItem(arg__1)
			arg__1=QtGui.QLayoutItem

		Implemented in subclasses to add an item
		How it is added is specific to each subclass.
		This function is not usually called in application code
		To add a widget to a layout, use the PySide.QtGui.QLayout.addWidget() function; to add a child layout, use the addLayout() function provided by the relevant PySide.QtGui.QLayout subclass.
		"""
		res = super(QLayout,self).addItem(arg__1)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,w):
		"""
		addWidget(w)
			w=QtGui.QWidget

		Adds widget w to this layout in a manner specific to the layout
		This function uses PySide.QtGui.QLayout.addItem() .
		"""
		res = super(QLayout,self).addWidget(w)
		return res
	#----------------------------------------------------------------------
	def alignmentRect(self,arg__1):
		"""
		alignmentRect(arg__1)
			arg__1=QtCore.QRect

		Returns the rectangle that should be covered when the geometry of this layout is set to r , provided that this layout supports PySide.QtGui.QLayout.setAlignment() .
		The result is derived from PySide.QtGui.QLayoutItem.sizeHint() and expanding()
		It is never larger than r .
		"""
		res = super(QLayout,self).alignmentRect(arg__1)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,arg__1):
		"""
		indexOf(arg__1)
			arg__1=QtGui.QWidget

		Searches for widget widget in this layout (not including child layouts).
		Returns the index of widget , or -1 if widget is not found.
		The default implementation iterates over all items using PySide.QtGui.QLayout.itemAt()
		"""
		res = super(QLayout,self).indexOf(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,index):
		"""
		itemAt(index)
			index=QtCore.int

		Must be implemented in subclasses to return the layout item at index
		If there is no such item, the function must return 0
		Items are numbered consecutively from 0
		If an item is deleted, other items will be renumbered.
		This function can be used to iterate over a layout
		The following code will draw a rectangle for each layout item in the layout structure of the widget.
		"""
		res = super(QLayout,self).itemAt(index)
		isinstance(res,QtGui.QLayoutItem)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,arg__1):
		"""
		removeItem(arg__1)
			arg__1=QtGui.QLayoutItem

		Removes the layout item item from the layout
		It is the callers responsibility to delete the item.
		Notice that item can be a layout (since PySide.QtGui.QLayout inherits PySide.QtGui.QLayoutItem ).
		"""
		res = super(QLayout,self).removeItem(arg__1)
		return res
	#----------------------------------------------------------------------
	def removeWidget(self,w):
		"""
		removeWidget(w)
			w=QtGui.QWidget

		Removes the widget widget from the layout
		After this call, it is the callers responsibility to give the widget a reasonable geometry or to put the widget back into a layout.
		"""
		res = super(QLayout,self).removeWidget(w)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,*args,**kwargs):
		"""
		setAlignment(w,alignment)
			w=QtGui.QWidget
			alignment=QtCore.Qt.Alignment

		setAlignment(l,alignment)
			l=QtGui.QLayout
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QLayout,self).setAlignment(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setContentsMargins(self,*args,**kwargs):
		"""
		setContentsMargins(left,top,right,bottom)
			left=QtCore.int
			top=QtCore.int
			right=QtCore.int
			bottom=QtCore.int

		setContentsMargins(margins)
			margins=QtCore.QMargins

		Sets the left , top , right , and bottom margins to use around the layout.
		By default, PySide.QtGui.QLayout uses the values provided by the style
		On most platforms, the margin is 11 pixels in all directions.
		"""
		res = super(QLayout,self).setContentsMargins(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setEnabled(self,arg__1):
		"""
		setEnabled(arg__1)
			arg__1=QtCore.bool

		Enables this layout if enable is true, otherwise disables it.
		An enabled layout adjusts dynamically to changes; a disabled layout acts as if it did not exist.
		By default all layouts are enabled.
		"""
		res = super(QLayout,self).setEnabled(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMenuBar(self,w):
		"""
		setMenuBar(w)
			w=QtGui.QWidget

		Tells the geometry manager to place the menu bar widget at the top of PySide.QtGui.QLayout.parentWidget() , outside QWidget.contentsMargins()
		All child widgets are placed below the bottom edge of the menu bar.
		"""
		res = super(QLayout,self).setMenuBar(w)
		return res
	#----------------------------------------------------------------------
	def setSizeConstraint(self,arg__1):
		"""
		setSizeConstraint(arg__1)
			arg__1=QtGui.QLayout.SizeConstraint

		This property holds the resize mode of the layout.
		The default mode is SetDefaultConstraint .
		"""
		res = super(QLayout,self).setSizeConstraint(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,arg__1):
		"""
		setSpacing(arg__1)
			arg__1=QtCore.int

		This property holds the spacing between widgets inside the layout.
		If no value is explicitly set, the layouts spacing is inherited from the parent layout, or from the style settings for the parent widget.
		For PySide.QtGui.QGridLayout and PySide.QtGui.QFormLayout , it is possible to set different horizontal and vertical spacings using PySide.QtGui.QGridLayout.setHorizontalSpacing() and PySide.QtGui.QGridLayout.setVerticalSpacing()
		In that case, PySide.QtGui.QLayout.spacing() returns -1.
		"""
		res = super(QLayout,self).setSpacing(arg__1)
		return res
	#----------------------------------------------------------------------
	def takeAt(self,index):
		"""
		takeAt(index)
			index=QtCore.int

		Must be implemented in subclasses to remove the layout item at index from the layout, and return the item
		If there is no such item, the function must do nothing and return 0
		Items are numbered consecutively from 0
		If an item is removed, other items will be renumbered.
		The following code fragment shows a safe way to remove all items from a layout:
		"""
		res = super(QLayout,self).takeAt(index)
		isinstance(res,QtGui.QLayoutItem)
		return res
	#----------------------------------------------------------------------
	def totalHeightForWidth(self,w):
		"""
		totalHeightForWidth(w)
			w=QtCore.int

		Also takes contentsMargins and menu bar into account.
		"""
		res = super(QLayout,self).totalHeightForWidth(w)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def widgetEvent(self,arg__1):
		"""
		widgetEvent(arg__1)
			arg__1=QtCore.QEvent

		Performs child widget layout when the parent widget is resized
		Also handles removal of widgets
		e is the event
		"""
		res = super(QLayout,self).widgetEvent(arg__1)
		return res
