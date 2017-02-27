import QT
import Qt_Roles_And_Enums
import MimeData
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
user_type_counter = QT.user_type_counter
Item_Data_Roles   = Qt_Roles_And_Enums.Standered_Item_Data_Roles
AbstractItemView  = Qt_Roles_And_Enums.AbstractItemView
Constants         = Qt_Roles_And_Enums.Constants


class QTreeView(QT.QTreeView):
	''''''
	#----------------------------------------------------------------------
	def __init__(self,*args,**kwargs):
		''''''
		super(QTreeView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def dropEvent(self, event):
		md =  event.mimeData()
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drop_destination =  self
			self.setAcceptDrops(True)
		md.setData("AW/INFO/DragDrop-Destination", self.objectName())
		return super(QTreeView,self).dropEvent(event)
	#----------------------------------------------------------------------
	def dragEnterEvent(self, event):
		md =  event.mimeData()
		self.setAcceptDrops(True)
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drag_source = event.source()
		md.setData("AW/INFO/DragDrop-Source", self.objectName())
		return super(QTreeView,self).dragEnterEvent(event)
	#----------------------------------------------------------------------
	def allColumnsShowFocus(self):
		"""
		This property holds whether items should show keyboard focus using all columns.
		If this property is true all columns will show focus, otherwise only one column will show focus.
		The default is false.
		"""
		res = super(QTreeView,self).allColumnsShowFocus()

		return res
	#----------------------------------------------------------------------
	def autoExpandDelay(self):
		"""
		This property holds The delay time before items in a tree are opened during a drag and drop operation..
		This property holds the amount of time in milliseconds that the user must wait over a node before that node will automatically open or close
		If the time is set to less then 0 then it will not be activated.
		By default, this property has a value of -1, meaning that auto-expansion is disabled.
		"""
		res = super(QTreeView,self).autoExpandDelay()

		return res
	#----------------------------------------------------------------------
	def expandsOnDoubleClick(self):
		"""
		This property holds whether the items can be expanded by double-clicking..
		This property holds whether the user can expand and collapse items by double-clicking
		The default value is true.
		"""
		res = super(QTreeView,self).expandsOnDoubleClick()

		return res
	#----------------------------------------------------------------------
	def header(self):
		"""
		Returns the header for the tree view.
		"""
		res = super(QTreeView,self).header()
		isinstance(res,QT.QHeaderView)
		return res
	#----------------------------------------------------------------------
	def indentation(self):
		"""
		This property holds indentation of the items in the tree view..
		This property holds the indentation measured in pixels of the items for each level in the tree view
		For top-level items, the indentation specifies the horizontal distance from the viewport edge to the items in the first column; for child items, it specifies their indentation from their parent items.
		By default, this property has a value of 20.
		"""
		res = super(QTreeView,self).indentation()

		return res
	#----------------------------------------------------------------------
	def isAnimated(self):
		"""
		This property holds whether animations are enabled.
		If this property is true the treeview will animate expandsion and collasping of branches
		If this property is false, the treeview will expand or collapse branches immediately without showing the animation.
		By default, this property is false.
		"""
		res = super(QTreeView,self).isAnimated()

		return res
	#----------------------------------------------------------------------
	def isHeaderHidden(self):
		"""
		This property holds whether the header is shown or not..
		If this property is true, the header is not shown otherwise it is
		The default value is false.
		"""
		res = super(QTreeView,self).isHeaderHidden()

		return res
	#----------------------------------------------------------------------
	def isSortingEnabled(self):
		"""
		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the tree; if the property is false, sorting is not enabled
		The default value is false.
		"""
		res = super(QTreeView,self).isSortingEnabled()

		return res
	#----------------------------------------------------------------------
	def itemsExpandable(self):
		"""
		This property holds whether the items are expandable by the user..
		This property holds whether the user can expand and collapse items interactively.
		By default, this property is true.
		"""
		res = super(QTreeView,self).itemsExpandable()

		return res
	#----------------------------------------------------------------------
	def rootIsDecorated(self):
		"""
		This property holds whether to show controls for expanding and collapsing top-level items.
		Items with children are typically shown with controls to expand and collapse them, allowing their children to be shown or hidden
		If this property is false, these controls are not shown for top-level items
		This can be used to make a single level tree structure appear like a simple list of items.
		By default, this property is true.
		"""
		res = super(QTreeView,self).rootIsDecorated()

		return res
	#----------------------------------------------------------------------
	def uniformRowHeights(self):
		"""
		This property holds whether all items in the treeview have the same height.
		This property should only be set to true if it is guaranteed that all items in the view has the same height
		This enables the view to do some optimizations.
		The height is obtained from the first item in the view
		It is updated when the data changes on that item.
		By default, this property is false.
		"""
		res = super(QTreeView,self).uniformRowHeights()

		return res
	#----------------------------------------------------------------------
	def wordWrap(self):
		"""
		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is false by default.
		Note that even if wrapping is enabled, the cell will not be expanded to fit all text
		Ellipsis will be inserted according to the current PySide.QT.stractItemView.textElideMode() .
		"""
		res = super(QTreeView,self).wordWrap()

		return res
	#----------------------------------------------------------------------
	def columnAt(self,x):
		"""
		columnAt(x)
			x=QtCore.int

		Returns the column in the tree view whose header covers the x coordinate given.
		"""
		res = super(QTreeView,self).columnAt(x)

		return res
	#----------------------------------------------------------------------
	def columnViewportPosition(self,column):
		"""
		columnViewportPosition(column)
			column=QtCore.int

		Returns the horizontal position of the column in the viewport.
		"""
		res = super(QTreeView,self).columnViewportPosition(column)

		return res
	#----------------------------------------------------------------------
	def columnWidth(self,column):
		"""
		columnWidth(column)
			column=QtCore.int

		Returns the width of the column .
		"""
		res = super(QTreeView,self).columnWidth(column)

		return res
	#----------------------------------------------------------------------
	def drawBranches(self,painter,rect,index):
		"""
		drawBranches(painter,rect,index)
			painter=QT.QPainter
			rect=QtCore.QRect
			index=QtCore.QModelIndex

		Draws the branches in the tree view on the same row as the model item index , using the painter given
		The branches are drawn in the rectangle specified by rect .
		"""
		res = super(QTreeView,self).drawBranches(painter,rect,index)
		return res
	#----------------------------------------------------------------------
	def drawRow(self,painter,options,index):
		"""
		drawRow(painter,options,index)
			painter=QT.QPainter
			options=QT.QStyleOptionViewItem
			index=QtCore.QModelIndex

		Draws the row in the tree view that contains the model item index , using the painter given
		The option control how the item is displayed.
		"""
		res = super(QTreeView,self).drawRow(painter,options,index)
		return res
	#----------------------------------------------------------------------
	def drawTree(self,painter,region):
		"""
		drawTree(painter,region)
			painter=QT.QPainter
			region=QT.QRegion

		Draws the part of the tree intersecting the given region using the specified painter .
		"""
		res = super(QTreeView,self).drawTree(painter,region)
		return res
	#----------------------------------------------------------------------
	def indexAbove(self,index):
		"""
		indexAbove(index)
			index=QtCore.QModelIndex

		Returns the model index of the item above index .
		"""
		res = super(QTreeView,self).indexAbove(index)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexBelow(self,index):
		"""
		indexBelow(index)
			index=QtCore.QModelIndex

		Returns the model index of the item below index .
		"""
		res = super(QTreeView,self).indexBelow(index)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexRowSizeHint(self,index):
		"""
		indexRowSizeHint(index)
			index=QtCore.QModelIndex

		Returns the size hint for the row indicated by index .
		"""
		res = super(QTreeView,self).indexRowSizeHint(index)

		return res
	#----------------------------------------------------------------------
	def isColumnHidden(self,column):
		"""
		isColumnHidden(column)
			column=QtCore.int

		Returns true if the column is hidden; otherwise returns false.
		"""
		res = super(QTreeView,self).isColumnHidden(column)

		return res
	#----------------------------------------------------------------------
	def isExpanded(self,index):
		"""
		isExpanded(index)
			index=QtCore.QModelIndex

		Returns true if the model item index is expanded; otherwise returns false.
		"""
		res = super(QTreeView,self).isExpanded(index)

		return res
	#----------------------------------------------------------------------
	def isFirstColumnSpanned(self,row,parent):
		"""
		isFirstColumnSpanned(row,parent)
			row=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if the item in first column in the given row of the parent is spanning all the columns; otherwise returns false.
		"""
		res = super(QTreeView,self).isFirstColumnSpanned(row,parent)

		return res
	#----------------------------------------------------------------------
	def isRowHidden(self,row,parent):
		"""
		isRowHidden(row,parent)
			row=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if the item in the given row of the parent is hidden; otherwise returns false.
		"""
		res = super(QTreeView,self).isRowHidden(row,parent)

		return res
	#----------------------------------------------------------------------
	def rowHeight(self,index):
		"""
		rowHeight(index)
			index=QtCore.QModelIndex

		Returns the height of the row indicated by the given index .
		"""
		res = super(QTreeView,self).rowHeight(index)

		return res
	#----------------------------------------------------------------------
	def setAllColumnsShowFocus(self,enable):
		"""
		setAllColumnsShowFocus(enable)
			enable=QtCore.bool

		This property holds whether items should show keyboard focus using all columns.
		If this property is true all columns will show focus, otherwise only one column will show focus.
		The default is false.
		"""
		res = super(QTreeView,self).setAllColumnsShowFocus(enable)
		return res
	#----------------------------------------------------------------------
	def setAnimated(self,enable):
		"""
		setAnimated(enable)
			enable=QtCore.bool

		This property holds whether animations are enabled.
		If this property is true the treeview will animate expandsion and collasping of branches
		If this property is false, the treeview will expand or collapse branches immediately without showing the animation.
		By default, this property is false.
		"""
		res = super(QTreeView,self).setAnimated(enable)
		return res
	#----------------------------------------------------------------------
	def setAutoExpandDelay(self,delay):
		"""
		setAutoExpandDelay(delay)
			delay=QtCore.int

		This property holds The delay time before items in a tree are opened during a drag and drop operation..
		This property holds the amount of time in milliseconds that the user must wait over a node before that node will automatically open or close
		If the time is set to less then 0 then it will not be activated.
		By default, this property has a value of -1, meaning that auto-expansion is disabled.
		"""
		res = super(QTreeView,self).setAutoExpandDelay(delay)
		return res
	#----------------------------------------------------------------------
	def setColumnHidden(self,column,hide):
		"""
		setColumnHidden(column,hide)
			column=QtCore.int
			hide=QtCore.bool

		If hide is true the column is hidden, otherwise the column is shown.
		"""
		res = super(QTreeView,self).setColumnHidden(column,hide)
		return res
	#----------------------------------------------------------------------
	def setColumnWidth(self,column,width):
		"""
		setColumnWidth(column,width)
			column=QtCore.int
			width=QtCore.int

		Sets the width of the given column to the width specified.
		"""
		res = super(QTreeView,self).setColumnWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setExpanded(self,index,expand):
		"""
		setExpanded(index,expand)
			index=QtCore.QModelIndex
			expand=QtCore.bool

		Sets the item referred to by index to either collapse or expanded, depending on the value of expanded .
		"""
		res = super(QTreeView,self).setExpanded(index,expand)
		return res
	#----------------------------------------------------------------------
	def setExpandsOnDoubleClick(self,enable):
		"""
		setExpandsOnDoubleClick(enable)
			enable=QtCore.bool

		This property holds whether the items can be expanded by double-clicking..
		This property holds whether the user can expand and collapse items by double-clicking
		The default value is true.
		"""
		res = super(QTreeView,self).setExpandsOnDoubleClick(enable)
		return res
	#----------------------------------------------------------------------
	def setFirstColumnSpanned(self,row,parent,span):
		"""
		setFirstColumnSpanned(row,parent,span)
			row=QtCore.int
			parent=QtCore.QModelIndex
			span=QtCore.bool

		If span is true the item in the first column in the row with the given parent is set to span all columns, otherwise all items on the row are shown.
		"""
		res = super(QTreeView,self).setFirstColumnSpanned(row,parent,span)
		return res
	#----------------------------------------------------------------------
	def setHeader(self,header):
		"""
		setHeader(header)
			header=QT.QHeaderView

		Sets the header for the tree view, to the given header .
		The view takes ownership over the given header and deletes it when a new header is set.
		"""
		res = super(QTreeView,self).setHeader(header)
		return res
	#----------------------------------------------------------------------
	def setHeaderHidden(self,hide):
		"""
		setHeaderHidden(hide)
			hide=QtCore.bool

		This property holds whether the header is shown or not..
		If this property is true, the header is not shown otherwise it is
		The default value is false.
		"""
		res = super(QTreeView,self).setHeaderHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIndentation(self,i):
		"""
		setIndentation(i)
			i=QtCore.int

		This property holds indentation of the items in the tree view..
		This property holds the indentation measured in pixels of the items for each level in the tree view
		For top-level items, the indentation specifies the horizontal distance from the viewport edge to the items in the first column; for child items, it specifies their indentation from their parent items.
		By default, this property has a value of 20.
		"""
		res = super(QTreeView,self).setIndentation(i)
		return res
	#----------------------------------------------------------------------
	def setItemsExpandable(self,enable):
		"""
		setItemsExpandable(enable)
			enable=QtCore.bool

		This property holds whether the items are expandable by the user..
		This property holds whether the user can expand and collapse items interactively.
		By default, this property is true.
		"""
		res = super(QTreeView,self).setItemsExpandable(enable)
		return res
	#----------------------------------------------------------------------
	def setRootIsDecorated(self,show):
		"""
		setRootIsDecorated(show)
			show=QtCore.bool

		This property holds whether to show controls for expanding and collapsing top-level items.
		Items with children are typically shown with controls to expand and collapse them, allowing their children to be shown or hidden
		If this property is false, these controls are not shown for top-level items
		This can be used to make a single level tree structure appear like a simple list of items.
		By default, this property is true.
		"""
		res = super(QTreeView,self).setRootIsDecorated(show)
		return res
	#----------------------------------------------------------------------
	def setRowHidden(self,row,parent,hide):
		"""
		setRowHidden(row,parent,hide)
			row=QtCore.int
			parent=QtCore.QModelIndex
			hide=QtCore.bool

		If hide is true the row with the given parent is hidden, otherwise the row is shown.
		"""
		res = super(QTreeView,self).setRowHidden(row,parent,hide)
		return res
	#----------------------------------------------------------------------
	def setSortingEnabled(self,enable):
		"""
		setSortingEnabled(enable)
			enable=QtCore.bool

		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the tree; if the property is false, sorting is not enabled
		The default value is false.
		"""
		res = super(QTreeView,self).setSortingEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setUniformRowHeights(self,uniform):
		"""
		setUniformRowHeights(uniform)
			uniform=QtCore.bool

		This property holds whether all items in the treeview have the same height.
		This property should only be set to true if it is guaranteed that all items in the view has the same height
		This enables the view to do some optimizations.
		The height is obtained from the first item in the view
		It is updated when the data changes on that item.
		By default, this property is false.
		"""
		res = super(QTreeView,self).setUniformRowHeights(uniform)
		return res
	#----------------------------------------------------------------------
	def setWordWrap(self,on):
		"""
		setWordWrap(on)
			on=QtCore.bool

		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is false by default.
		Note that even if wrapping is enabled, the cell will not be expanded to fit all text
		Ellipsis will be inserted according to the current PySide.QT.QAbstractItemView.textElideMode() .
		"""
		res = super(QTreeView,self).setWordWrap(on)
		return res
	#----------------------------------------------------------------------
	def sortByColumn(self,column,order):
		"""
		sortByColumn(column,order)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QTreeView,self).sortByColumn(column,order)
		return res
	#----------------------------------------------------------------------
	def visualIndex(self,index):
		"""
		visualIndex(index)
			index=QtCore.QModelIndex


		"""
		res = super(QTreeView,self).visualIndex(index)

		return res


	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	#----------------------------------------------------------------------
	def alternatingRowColors(self):
		"""
		This property holds whether to draw the background using alternating colors.
		If this property is true, the item background will be drawn using QPalette.Base and QPalette.AlternateBase ; otherwise the background will be drawn using the QPalette.Base color.
		By default, this property is false.
		"""
		res = super(QTreeView,self).alternatingRowColors()

		return res
	#----------------------------------------------------------------------
	def autoScrollMargin(self):
		"""
		This property holds the size of the area when auto scrolling is triggered.
		This property controls the size of the area at the edge of the viewport that triggers autoscrolling
		The default value is 16 pixels.
		"""
		res = super(QTreeView,self).autoScrollMargin()

		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		Returns the model index of the current item.
		"""
		res = super(QTreeView,self).currentIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def defaultDropAction(self):
		"""
		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QTreeView,self).defaultDropAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def dirtyRegionOffset(self):
		"""
		Returns the offset of the dirty regions in the view.
		If you use PySide.QT.QAbstractItemView.scrollDirtyRegion() and implement a PySide.QT.QAbstractScrollArea.paintEvent() in a subclass of PySide.QT.QAbstractItemView , you should translate the area given by the paint event with the offset returned from this function.
		"""
		res = super(QTreeView,self).dirtyRegionOffset()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def doAutoScroll(self):
		"""

		"""
		res = super(QTreeView,self).doAutoScroll()
		return res
	#----------------------------------------------------------------------
	def doItemsLayout(self):
		"""
		This function is intended to lay out the items in the view
		The default implementation just calls PySide.QT.QAbstractItemView.updateGeometries() and updates the viewport.
		"""
		res = super(QTreeView,self).doItemsLayout()
		return res
	#----------------------------------------------------------------------
	def dragDropMode(self):
		"""
		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QTreeView,self).dragDropMode()
		isinstance(res,QT.QAbstractItemView.DragDropMode)
		return res
	#----------------------------------------------------------------------
	def dragDropOverwriteMode(self):
		"""
		This property holds the views drag and drop behavior.
		If its value is true , the selected data will overwrite the existing item data when dropped, while moving the data will clear the item
		If its value is false , the selected data will be inserted as a new item when the data is dropped
		When the data is moved, the item is removed as well.
		The default value is false , as in the PySide.QT.QListView and PySide.QT.QTreeView subclasses
		In the PySide.QT.QTableView subclass, on the other hand, the property has been set to true .
		Note: This is not intended to prevent overwriting of items
		The models implementation of flags() should do that by not returning Qt.ItemIsDropEnabled .
		"""
		res = super(QTreeView,self).dragDropOverwriteMode()

		return res
	#----------------------------------------------------------------------
	def dragEnabled(self):
		"""
		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QTreeView,self).dragEnabled()

		return res
	#----------------------------------------------------------------------
	def dropIndicatorPosition(self):
		"""
		Returns the position of the drop indicator in relation to the closest item.
		"""
		res = super(QTreeView,self).dropIndicatorPosition()
		isinstance(res,QT.QAbstractItemView.DropIndicatorPosition)
		return res
	#----------------------------------------------------------------------
	def editTriggers(self):
		"""
		This property holds which actions will initiate item editing.
		This property is a selection of flags defined by QAbstractItemView.EditTrigger , combined using the OR operator
		The view will only initiate the editing of an item if the action performed is set in this property.
		"""
		res = super(QTreeView,self).editTriggers()
		isinstance(res,QT.QAbstractItemView.EditTriggers)
		return res
	#----------------------------------------------------------------------
	def executeDelayedItemsLayout(self):
		"""
		Executes the scheduled layouts without waiting for the event processing to begin.
		"""
		res = super(QTreeView,self).executeDelayedItemsLayout()
		return res
	#----------------------------------------------------------------------
	def hasAutoScroll(self):
		"""
		This property holds whether autoscrolling in drag move events is enabled.
		If this property is set to true (the default), the PySide.QT.QAbstractItemView automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge
		If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.
		This property only works if the viewport accepts drops
		Autoscroll is switched off by setting this property to false.
		"""
		res = super(QTreeView,self).hasAutoScroll()

		return res
	#----------------------------------------------------------------------
	def horizontalOffset(self):
		"""
		Returns the horizontal offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).horizontalOffset()

		return res
	#----------------------------------------------------------------------
	def horizontalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the horizontal direction.
		This property controls how the view scroll its contents horizontally
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTreeView,self).horizontalScrollMode()
		isinstance(res,QT.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QTreeView,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the item delegate used by this view and model
		This is either one set with PySide.QT.QAbstractItemView.setItemDelegate() , or the default one.
		"""
		res = super(QTreeView,self).itemDelegate()
		isinstance(res,QT.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that this view is presenting.
		"""
		res = super(QTreeView,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Reset the internal state of the view.
		"""
		res = super(QTreeView,self).reset()
		return res
	#----------------------------------------------------------------------
	def rootIndex(self):
		"""
		Returns the model index of the models root item
		The root item is the parent item to the views toplevel items
		The root can be invalid.
		"""
		res = super(QTreeView,self).rootIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def scheduleDelayedItemsLayout(self):
		"""
		Schedules a layout of the items in the view to be executed when the event processing starts.
		Even if PySide.QT.QAbstractItemView.scheduleDelayedItemsLayout() is called multiple times before events are processed, the view will only do the layout once.
		"""
		res = super(QTreeView,self).scheduleDelayedItemsLayout()
		return res
	#----------------------------------------------------------------------
	def selectAll(self):
		"""
		Selects all items in the view
		This function will use the selection behavior set on the view when selecting.
		"""
		res = super(QTreeView,self).selectAll()
		return res
	#----------------------------------------------------------------------
	def selectedIndexes(self):
		"""
		This convenience function returns a list of all selected and non-hidden item indexes in the view
		The list contains no duplicates, and is not sorted.
		"""
		res = super(QTreeView,self).selectedIndexes()
		return res
	#----------------------------------------------------------------------
	def selectionBehavior(self):
		"""
		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QTreeView,self).selectionBehavior()
		isinstance(res,QT.QAbstractItemView.SelectionBehavior)
		return res
	#----------------------------------------------------------------------
	def selectionMode(self):
		"""
		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QTreeView,self).selectionMode()
		isinstance(res,QT.QAbstractItemView.SelectionMode)
		return res
	#----------------------------------------------------------------------
	def selectionModel(self):
		"""
		Returns the current selection model.
		"""
		res = super(QTreeView,self).selectionModel()
		isinstance(res,QT.QItemSelectionModel)
		return res
	#----------------------------------------------------------------------
	def showDropIndicator(self):
		"""
		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QTreeView,self).showDropIndicator()

		return res
	#----------------------------------------------------------------------
	def startAutoScroll(self):
		"""

		"""
		res = super(QTreeView,self).startAutoScroll()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the item views state.
		"""
		res = super(QTreeView,self).state()
		isinstance(res,QT.QAbstractItemView.State)
		return res
	#----------------------------------------------------------------------
	def stopAutoScroll(self):
		"""

		"""
		res = super(QTreeView,self).stopAutoScroll()
		return res
	#----------------------------------------------------------------------
	def tabKeyNavigation(self):
		"""
		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QTreeView,self).tabKeyNavigation()

		return res
	#----------------------------------------------------------------------
	def textElideMode(self):
		"""
		This property holds the position of the ..
		in elided text..
		The default value for all item views is Qt.ElideRight .
		"""
		res = super(QTreeView,self).textElideMode()
		isinstance(res,QtCore.Qt.TextElideMode)
		return res
	#----------------------------------------------------------------------
	def updateEditorData(self):
		"""
		Updates the data shown in the open editor widgets in the view.
		"""
		res = super(QTreeView,self).updateEditorData()
		return res
	#----------------------------------------------------------------------
	def updateEditorGeometries(self):
		"""
		Updates the geometry of the open editor widgets in the view.
		"""
		res = super(QTreeView,self).updateEditorGeometries()
		return res
	#----------------------------------------------------------------------
	def updateGeometries(self):
		"""
		Updates the geometry of the child widgets of the view.
		"""
		res = super(QTreeView,self).updateGeometries()
		return res
	#----------------------------------------------------------------------
	def verticalOffset(self):
		"""
		Returns the vertical offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).verticalOffset()

		return res
	#----------------------------------------------------------------------
	def verticalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the vertical direction.
		This property controls how the view scroll its contents vertically
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTreeView,self).verticalScrollMode()
		isinstance(res,QT.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def viewOptions(self):
		"""
		Returns a PySide.QT.QStyleOptionViewItem structure populated with the views palette, font, state, alignments etc.
		"""
		res = super(QTreeView,self).viewOptions()
		isinstance(res,QT.QStyleOptionViewItem)
		return res
	#----------------------------------------------------------------------
	def viewportEntered(self):
		"""

		"""
		res = super(QTreeView,self).viewportEntered()
		return res
	#----------------------------------------------------------------------
	def closeEditor(self,editor,hint):
		"""
		closeEditor(editor,hint)
			editor=QT.QWidget
			hint=QT.QAbstractItemDelegate.EndEditHint


		"""
		res = super(QTreeView,self).closeEditor(editor,hint)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,index):
		"""
		closePersistentEditor(index)
			index=QtCore.QModelIndex

		Closes the persistent editor for the item at the given index .
		"""
		res = super(QTreeView,self).closePersistentEditor(index)
		return res
	#----------------------------------------------------------------------
	def commitData(self,editor):
		"""
		commitData(editor)
			editor=QT.QWidget

		Commit the data in the editor to the model.
		"""
		res = super(QTreeView,self).commitData(editor)
		return res
	#----------------------------------------------------------------------
	def currentChanged(self,current,previous):
		"""
		currentChanged(current,previous)
			current=QtCore.QModelIndex
			previous=QtCore.QModelIndex

		This slot is called when a new item becomes the current item
		The previous current item is specified by the previous index, and the new item by the current index.
		If you want to know about changes to items see the PySide.QT.QAbstractItemView.dataChanged() signal.
		"""
		res = super(QTreeView,self).currentChanged(current,previous)
		return res
	#----------------------------------------------------------------------
	def dataChanged(self,topLeft,bottomRight):
		"""
		dataChanged(topLeft,bottomRight)
			topLeft=QtCore.QModelIndex
			bottomRight=QtCore.QModelIndex

		This slot is called when items are changed in the model
		The changed items are those from topLeft to bottomRight inclusive
		If just one item is changed topLeft == bottomRight .
		"""
		res = super(QTreeView,self).dataChanged(topLeft,bottomRight)
		return res
	#----------------------------------------------------------------------
	def edit(self,*args,**kwargs):
		"""
		edit(index,trigger,event)
			index=QtCore.QModelIndex
			trigger=QT.QAbstractItemView.EditTrigger
			event=QtCore.QEvent

		edit(index)
			index=QtCore.QModelIndex

		Starts editing the item at index , creating an editor if necessary, and returns true if the views QAbstractItemView.State is now EditingState ; otherwise returns false.
		The action that caused the editing process is described by trigger , and the associated event is specified by event .
		Editing can be forced by specifying the trigger to be QAbstractItemView.AllEditTriggers .
		"""
		res = super(QTreeView,self).edit(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def editorDestroyed(self,editor):
		"""
		editorDestroyed(editor)
			editor=QtCore.QObject

		This function is called when the given editor has been destroyed.
		"""
		res = super(QTreeView,self).editorDestroyed(editor)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarAction(self,action):
		"""
		horizontalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QTreeView,self).horizontalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarValueChanged(self,value):
		"""
		horizontalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QTreeView,self).horizontalScrollbarValueChanged(value)
		return res
	#----------------------------------------------------------------------
	def indexAt(self,point):
		"""
		indexAt(point)
			point=QtCore.QPoint

		Returns the model index of the item at the viewport coordinates point .
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).indexAt(point)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexWidget(self,index):
		"""
		indexWidget(index)
			index=QtCore.QModelIndex

		Returns the widget for the item at the given index .
		"""
		res = super(QTreeView,self).indexWidget(index)
		isinstance(res,QT.QWidget)
		return res
	#----------------------------------------------------------------------
	def isIndexHidden(self,index):
		"""
		isIndexHidden(index)
			index=QtCore.QModelIndex

		Returns true if the item referred to by the given index is hidden in the view, otherwise returns false.
		Hiding is a view specific feature
		For example in TableView a column can be marked as hidden or a row in the TreeView.
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).isIndexHidden(index)

		return res
	#----------------------------------------------------------------------
	def itemDelegate(self,index):
		"""
		itemDelegate(index)
			index=QtCore.QModelIndex

		Returns the item delegate used by this view and model for the given index .
		"""
		res = super(QTreeView,self).itemDelegate(index)
		isinstance(res,QT.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def itemDelegateForColumn(self,column):
		"""
		itemDelegateForColumn(column)
			column=QtCore.int

		Returns the item delegate used by this view and model for the given column
		You can call PySide.QT.QAbstractItemView.itemDelegate() to get a pointer to the current delegate for a given index.
		"""
		res = super(QTreeView,self).itemDelegateForColumn(column)
		isinstance(res,QT.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def itemDelegateForRow(self,row):
		"""
		itemDelegateForRow(row)
			row=QtCore.int

		Returns the item delegate used by this view and model for the given row , or 0 if no delegate has been assigned
		You can call PySide.QT.QAbstractItemView.itemDelegate() to get a pointer to the current delegate for a given index.
		"""
		res = super(QTreeView,self).itemDelegateForRow(row)
		isinstance(res,QT.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def keyboardSearch(self,search):
		"""
		keyboardSearch(search)
			search=unicode

		Moves to and selects the item best matching the string search
		If no item is found nothing happens.
		In the default implementation, the search is reset if search is empty, or the time interval since the last search has exceeded QApplication.keyboardInputInterval() .
		"""
		res = super(QTreeView,self).keyboardSearch(search)
		return res
	#----------------------------------------------------------------------
	def moveCursor(self,cursorAction,modifiers):
		"""
		moveCursor(cursorAction,modifiers)
			cursorAction=QT.QAbstractItemView.CursorAction
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QTreeView,self).moveCursor(cursorAction,modifiers)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,index):
		"""
		openPersistentEditor(index)
			index=QtCore.QModelIndex

		Opens a persistent editor on the item at the given index
		If no editor exists, the delegate will create a new editor.
		"""
		res = super(QTreeView,self).openPersistentEditor(index)
		return res
	#----------------------------------------------------------------------
	def rowsAboutToBeRemoved(self,parent,start,end):
		"""
		rowsAboutToBeRemoved(parent,start,end)
			parent=QtCore.QModelIndex
			start=QtCore.int
			end=QtCore.int

		This slot is called when rows are about to be removed
		The deleted rows are those under the given parent from start to end inclusive.
		"""
		res = super(QTreeView,self).rowsAboutToBeRemoved(parent,start,end)
		return res
	#----------------------------------------------------------------------
	def rowsInserted(self,parent,start,end):
		"""
		rowsInserted(parent,start,end)
			parent=QtCore.QModelIndex
			start=QtCore.int
			end=QtCore.int

		This slot is called when rows are inserted
		The new rows are those under the given parent from start to end inclusive
		The base class implementation calls fetchMore() on the model to check for more data.
		"""
		res = super(QTreeView,self).rowsInserted(parent,start,end)
		return res
	#----------------------------------------------------------------------
	def scrollDirtyRegion(self,dx,dy):
		"""
		scrollDirtyRegion(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		Prepares the view for scrolling by (dx ,``dy`` ) pixels by moving the dirty regions in the opposite direction
		You only need to call this function if you are implementing a scrolling viewport in your view subclass.
		If you implement PySide.QT.QAbstractScrollArea.scrollContentsBy() in a subclass of PySide.QT.QAbstractItemView , call this function before you call QWidget.scroll() on the viewport
		Alternatively, just call PySide.QT.QAbstractItemView.update() .
		"""
		res = super(QTreeView,self).scrollDirtyRegion(dx,dy)
		return res
	#----------------------------------------------------------------------
	def scrollTo(self,index,hint=None):
		"""
		scrollTo(index,hint=None)
			index=QtCore.QModelIndex
			hint=QT.QAbstractItemView.ScrollHint

		Scrolls the view if necessary to ensure that the item at index is visible
		The view will try to position the item according to the given hint .
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).scrollTo(index,hint)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self,selected,deselected):
		"""
		selectionChanged(selected,deselected)
			selected=QT.QItemSelection
			deselected=QT.QItemSelection

		This slot is called when the selection is changed
		The previous selection (which may be empty), is specified by deselected , and the new selection by selected .
		"""
		res = super(QTreeView,self).selectionChanged(selected,deselected)
		return res
	#----------------------------------------------------------------------
	def selectionCommand(self,index,event=None):
		"""
		selectionCommand(index,event=None)
			index=QtCore.QModelIndex
			event=QtCore.QEvent

		Returns the SelectionFlags to be used when updating a selection with to include the index specified
		The event is a user input event, such as a mouse or keyboard event.
		Reimplement this function to define your own selection behavior.
		"""
		res = super(QTreeView,self).selectionCommand(index,event)
		isinstance(res,QT.QItemSelectionModel.SelectionFlags)
		return res
	#----------------------------------------------------------------------
	def setAlternatingRowColors(self,enable):
		"""
		setAlternatingRowColors(enable)
			enable=QtCore.bool

		This property holds whether to draw the background using alternating colors.
		If this property is true, the item background will be drawn using QPalette.Base and QPalette.AlternateBase ; otherwise the background will be drawn using the QPalette.Base color.
		By default, this property is false.
		"""
		res = super(QTreeView,self).setAlternatingRowColors(enable)
		return res
	#----------------------------------------------------------------------
	def setAutoScroll(self,enable):
		"""
		setAutoScroll(enable)
			enable=QtCore.bool

		This property holds whether autoscrolling in drag move events is enabled.
		If this property is set to true (the default), the PySide.QT.QAbstractItemView automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge
		If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.
		This property only works if the viewport accepts drops
		Autoscroll is switched off by setting this property to false.
		"""
		res = super(QTreeView,self).setAutoScroll(enable)
		return res
	#----------------------------------------------------------------------
	def setAutoScrollMargin(self,margin):
		"""
		setAutoScrollMargin(margin)
			margin=QtCore.int

		This property holds the size of the area when auto scrolling is triggered.
		This property controls the size of the area at the edge of the viewport that triggers autoscrolling
		The default value is 16 pixels.
		"""
		res = super(QTreeView,self).setAutoScrollMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setDefaultDropAction(self,dropAction):
		"""
		setDefaultDropAction(dropAction)
			dropAction=QtCore.Qt.DropAction

		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QTreeView,self).setDefaultDropAction(dropAction)
		return res
	#----------------------------------------------------------------------
	def setDirtyRegion(self,region):
		"""
		setDirtyRegion(region)
			region=QT.QRegion

		Marks the given region as dirty and schedules it to be updated
		You only need to call this function if you are implementing your own view subclass.
		"""
		res = super(QTreeView,self).setDirtyRegion(region)
		return res
	#----------------------------------------------------------------------
	def setDragDropMode(self,behavior):
		"""
		setDragDropMode(behavior)
			behavior=QT.QAbstractItemView.DragDropMode

		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QTreeView,self).setDragDropMode(behavior)
		return res
	#----------------------------------------------------------------------
	def setDragDropOverwriteMode(self,overwrite):
		"""
		setDragDropOverwriteMode(overwrite)
			overwrite=QtCore.bool

		This property holds the views drag and drop behavior.
		If its value is true , the selected data will overwrite the existing item data when dropped, while moving the data will clear the item
		If its value is false , the selected data will be inserted as a new item when the data is dropped
		When the data is moved, the item is removed as well.
		The default value is false , as in the PySide.QT.QListView and PySide.QT.QTreeView subclasses
		In the PySide.QT.QTableView subclass, on the other hand, the property has been set to true .
		Note: This is not intended to prevent overwriting of items
		The models implementation of flags() should do that by not returning Qt.ItemIsDropEnabled .
		"""
		res = super(QTreeView,self).setDragDropOverwriteMode(overwrite)
		return res
	#----------------------------------------------------------------------
	def setDragEnabled(self,enable):
		"""
		setDragEnabled(enable)
			enable=QtCore.bool

		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QTreeView,self).setDragEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setDropIndicatorShown(self,enable):
		"""
		setDropIndicatorShown(enable)
			enable=QtCore.bool

		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QTreeView,self).setDropIndicatorShown(enable)
		return res
	#----------------------------------------------------------------------
	def setEditTriggers(self,triggers):
		"""
		setEditTriggers(triggers)
			triggers=QT.QAbstractItemView.EditTriggers

		This property holds which actions will initiate item editing.
		This property is a selection of flags defined by QAbstractItemView.EditTrigger , combined using the OR operator
		The view will only initiate the editing of an item if the action performed is set in this property.
		"""
		res = super(QTreeView,self).setEditTriggers(triggers)
		return res
	#----------------------------------------------------------------------
	def setHorizontalScrollMode(self,mode):
		"""
		setHorizontalScrollMode(mode)
			mode=QT.QAbstractItemView.ScrollMode

		This property holds how the view scrolls its contents in the horizontal direction.
		This property controls how the view scroll its contents horizontally
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTreeView,self).setHorizontalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QtCore.QSize

		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QTreeView,self).setIconSize(size)
		return res
	#----------------------------------------------------------------------
	def setIndexWidget(self,index,widget):
		"""
		setIndexWidget(index,widget)
			index=QtCore.QModelIndex
			widget=QT.QWidget

		Sets the given widget on the item at the given index , passing the ownership of the widget to the viewport.
		If index is invalid (e.g., if you pass the root index), this function will do nothing.
		The given widget s autoFillBackground property must be set to true, otherwise the widgets background will be transparent, showing both the model data and the item at the given index .
		If index widget A is replaced with index widget B, index widget A will be deleted
		For example, in the code snippet below, the PySide.QT.QLineEdit object will be deleted.
		This function should only be used to display static content within the visible area corresponding to an item of data
		If you want to display custom dynamic content or implement a custom editor widget, subclass PySide.QT.QItemDelegate instead.
		"""
		res = super(QTreeView,self).setIndexWidget(index,widget)
		return res
	#----------------------------------------------------------------------
	def setItemDelegate(self,delegate):
		"""
		setItemDelegate(delegate)
			delegate=QT.QAbstractItemDelegate

		Sets the item delegate for this view and its model to delegate
		This is useful if you want complete control over the editing and display of items.
		Any existing delegate will be removed, but not deleted
		PySide.QT.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTreeView,self).setItemDelegate(delegate)
		return res
	#----------------------------------------------------------------------
	def setItemDelegateForColumn(self,column,delegate):
		"""
		setItemDelegateForColumn(column,delegate)
			column=QtCore.int
			delegate=QT.QAbstractItemDelegate

		Sets the given item delegate used by this view and model for the given column
		All items on column will be drawn and managed by delegate instead of using the default delegate (i.e., PySide.QT.QAbstractItemView.itemDelegate() ).
		Any existing column delegate for column will be removed, but not deleted
		PySide.QT.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTreeView,self).setItemDelegateForColumn(column,delegate)
		return res
	#----------------------------------------------------------------------
	def setItemDelegateForRow(self,row,delegate):
		"""
		setItemDelegateForRow(row,delegate)
			row=QtCore.int
			delegate=QT.QAbstractItemDelegate

		Sets the given item delegate used by this view and model for the given row
		All items on row will be drawn and managed by delegate instead of using the default delegate (i.e., PySide.QT.QAbstractItemView.itemDelegate() ).
		Any existing row delegate for row will be removed, but not deleted
		PySide.QT.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTreeView,self).setItemDelegateForRow(row,delegate)
		return res
	#----------------------------------------------------------------------
	def setModel(self,model):
		"""
		setModel(model)
			model=QtCore.QAbstractItemModel

		Sets the model for the view to present.
		This function will create and set a new selection model, replacing any model that was previously set with PySide.QT.QAbstractItemView.setSelectionModel()
		However, the old selection model will not be deleted as it may be shared between several views
		We recommend that you delete the old selection model if it is no longer required
		This is done with the following code:
		If both the old model and the old selection model do not have parents, or if their parents are long-lived objects, it may be preferable to call their deleteLater() functions to explicitly delete them.
		The view does not take ownership of the model unless it is the models parent object because the view may be shared between many different views.
		"""
		res = super(QTreeView,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setRootIndex(self,index):
		"""
		setRootIndex(index)
			index=QtCore.QModelIndex

		Sets the root item to the item at the given index .
		"""
		res = super(QTreeView,self).setRootIndex(index)
		return res
	#----------------------------------------------------------------------
	def setSelection(self,rect,command):
		"""
		setSelection(rect,command)
			rect=QtCore.QRect
			command=QT.QItemSelectionModel.SelectionFlags


		"""
		res = super(QTreeView,self).setSelection(rect,command)
		return res
	#----------------------------------------------------------------------
	def setSelectionBehavior(self,behavior):
		"""
		setSelectionBehavior(behavior)
			behavior=QT.QAbstractItemView.SelectionBehavior

		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QTreeView,self).setSelectionBehavior(behavior)
		return res
	#----------------------------------------------------------------------
	def setSelectionMode(self,mode):
		"""
		setSelectionMode(mode)
			mode=QT.QAbstractItemView.SelectionMode

		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QTreeView,self).setSelectionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setSelectionModel(self,selectionModel):
		"""
		setSelectionModel(selectionModel)
			selectionModel=QT.QItemSelectionModel

		Sets the current selection model to the given selectionModel .
		Note that, if you call PySide.QT.QAbstractItemView.setModel() after this function, the given selectionModel will be replaced by one created by the view.
		"""
		res = super(QTreeView,self).setSelectionModel(selectionModel)
		return res
	#----------------------------------------------------------------------
	def setState(self,state):
		"""
		setState(state)
			state=QT.QAbstractItemView.State

		Sets the item views state to the given state .
		"""
		res = super(QTreeView,self).setState(state)
		return res
	#----------------------------------------------------------------------
	def setTabKeyNavigation(self,enable):
		"""
		setTabKeyNavigation(enable)
			enable=QtCore.bool

		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QTreeView,self).setTabKeyNavigation(enable)
		return res
	#----------------------------------------------------------------------
	def setTextElideMode(self,mode):
		"""
		setTextElideMode(mode)
			mode=QtCore.Qt.TextElideMode

		This property holds the position of the ..
		in elided text..
		The default value for all item views is Qt.ElideRight .
		"""
		res = super(QTreeView,self).setTextElideMode(mode)
		return res
	#----------------------------------------------------------------------
	def setVerticalScrollMode(self,mode):
		"""
		setVerticalScrollMode(mode)
			mode=QT.QAbstractItemView.ScrollMode

		This property holds how the view scrolls its contents in the vertical direction.
		This property controls how the view scroll its contents vertically
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTreeView,self).setVerticalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def sizeHintForColumn(self,column):
		"""
		sizeHintForColumn(column)
			column=QtCore.int

		Returns the width size hint for the specified column or -1 if there is no model.
		This function is used in views with a horizontal header to find the size hint for a header section based on the contents of the given column .
		"""
		res = super(QTreeView,self).sizeHintForColumn(column)

		return res
	#----------------------------------------------------------------------
	def sizeHintForIndex(self,index):
		"""
		sizeHintForIndex(index)
			index=QtCore.QModelIndex

		Returns the size hint for the item with the specified index or an invalid size for invalid indexes.
		"""
		res = super(QTreeView,self).sizeHintForIndex(index)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def sizeHintForRow(self,row):
		"""
		sizeHintForRow(row)
			row=QtCore.int

		Returns the height size hint for the specified row or -1 if there is no model.
		The returned height is calculated using the size hints of the given row s items, i.e
		the returned value is the maximum height among the items
		Note that to control the height of a row, you must reimplement the QAbstractItemDelegate.sizeHint() function.
		This function is used in views with a vertical header to find the size hint for a header section based on the contents of the given row .
		"""
		res = super(QTreeView,self).sizeHintForRow(row)

		return res
	#----------------------------------------------------------------------
	def index(self, arg1, arg2=0):
		"""
		sizeHintForRow(row)
			row=QtCore.int

		Returns the height size hint for the specified row or -1 if there is no model.
		The returned height is calculated using the size hints of the given row s items, i.e
		the returned value is the maximum height among the items
		Note that to control the height of a row, you must reimplement the QAbstractItemDelegate.sizeHint() function.
		This function is used in views with a vertical header to find the size hint for a header section based on the contents of the given row .
		"""
		res = super(QTreeView,self).index(arg1, arg2)

		return res
	#----------------------------------------------------------------------
	def startDrag(self,supportedActions):
		"""
		startDrag(supportedActions)
			supportedActions=QtCore.Qt.DropActions


		"""
		res = super(QTreeView,self).startDrag(supportedActions)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarAction(self,action):
		"""
		verticalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QTreeView,self).verticalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarValueChanged(self,value):
		"""
		verticalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QTreeView,self).verticalScrollbarValueChanged(value)
		return res
	#----------------------------------------------------------------------
	def visualRect(self,index):
		"""
		visualRect(index)
			index=QtCore.QModelIndex

		Returns the rectangle on the viewport occupied by the item at index .
		If your item is displayed in several areas then visualRect should return the primary area that contains index and not the complete area that index might encompasses, touch or cause drawing.
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).visualRect(index)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def visualRegionForSelection(self,selection):
		"""
		visualRegionForSelection(selection)
			selection=QT.QItemSelection

		Returns the region from the viewport of the items in the given selection .
		In the base class this is a pure virtual function.
		"""
		res = super(QTreeView,self).visualRegionForSelection(selection)
		isinstance(res,QT.QRegion)
		return res



	AlternatingRowColors       = property(alternatingRowColors)
	AutoScrollMargin           = property(autoScrollMargin)
	CurrentIndex               = property(currentIndex)
	DefaultDropAction          = property(defaultDropAction)
	DirtyRegionOffset          = property(dirtyRegionOffset)
	DoAutoScroll               = property(doAutoScroll)
	DoItemsLayout              = property(doItemsLayout)
	DragDropMode               = property(dragDropMode)
	DragDropOverwriteMode      = property(dragDropOverwriteMode)
	DragEnabled                = property(dragEnabled)
	DropIndicatorPosition      = property(dropIndicatorPosition)
	EditTriggers               = property(editTriggers)
	ExecuteDelayedItemsLayout  = property(executeDelayedItemsLayout)
	HasAutoScroll              = property(hasAutoScroll)
	HorizontalOffset           = property(horizontalOffset)
	HorizontalScrollMode       = property(horizontalScrollMode)
	IconSize                   = property(iconSize)
	ItemDelegate               = property(itemDelegate)
	Model                      = property(model)
	Reset                      = property(reset)
	RootIndex                  = property(rootIndex)
	ScheduleDelayedItemsLayout = property(scheduleDelayedItemsLayout)
	SelectAll                  = property(selectAll)
	SelectedIndexes            = property(selectedIndexes)
	SelectionBehavior          = property(selectionBehavior)
	SelectionMode              = property(selectionMode)
	SelectionModel             = property(selectionModel)
	ShowDropIndicator          = property(showDropIndicator)
	StartAutoScroll            = property(startAutoScroll)
	State                      = property(state)
	StopAutoScroll             = property(stopAutoScroll)
	TabKeyNavigation           = property(tabKeyNavigation)
	TextElideMode              = property(textElideMode)
	UpdateEditorData           = property(updateEditorData)
	UpdateEditorGeometries     = property(updateEditorGeometries)
	UpdateGeometries           = property(updateGeometries)
	VerticalOffset             = property(verticalOffset)
	VerticalScrollMode         = property(verticalScrollMode)
	ViewOptions                = property(viewOptions)
	ViewportEntered            = property(viewportEntered)
	
	AllColumnsShowFocus  = property(allColumnsShowFocus)
	AutoExpandDelay      = property(autoExpandDelay)
	ExpandsOnDoubleClick = property(expandsOnDoubleClick)
	Header               = property(header)
	Indentation          = property(indentation)
	IsAnimated           = property(isAnimated)
	IsHeaderHidden       = property(isHeaderHidden)
	IsSortingEnabled     = property(isSortingEnabled)
	ItemsExpandable      = property(itemsExpandable)
	RootIsDecorated      = property(rootIsDecorated)
	UniformRowHeights    = property(uniformRowHeights)
	WordWrap             = property(wordWrap)

