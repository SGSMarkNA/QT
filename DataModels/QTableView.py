import QT
import MimeData
import Qt_Roles_And_Enums
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
user_type_counter = QT.user_type_counter
Item_Data_Roles   = Qt_Roles_And_Enums.Standered_Item_Data_Roles
AbstractItemView  = Qt_Roles_And_Enums.AbstractItemView
Constants         = Qt_Roles_And_Enums.Constants

class QTableView(QtGui.QTableView):
	''''''
	Item_Data_Roles = Item_Data_Roles
	
	def __init__(self,*args,**kwargs):
		''''''
		super(QTableView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def dropEvent(self, event):
		md =  event.mimeData()
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drag_source =  self
		md.setData("AW/INFO/DragDrop-Destination", self.objectName())
		return super(QTableView,self).dropEvent(event)
	#----------------------------------------------------------------------
	def dragEnterEvent(self, event):
		md =  event.mimeData()
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drop_destination = self
		md.setData("AW/INFO/DragDrop-Source", self.objectName())
		return super(QTableView,self).dragEnterEvent(event)
	#----------------------------------------------------------------------
	def clearSpans(self):
		"""
		Removes all row and column spans in the table view.
		"""
		res = super(QTableView,self).clearSpans()
		return res
	#----------------------------------------------------------------------
	def gridStyle(self):
		"""
		This property holds the pen style used to draw the grid..
		This property holds the style used when drawing the grid (see PySide.QtGui.QTableView.showGrid() ).
		"""
		res = super(QTableView,self).gridStyle()
		isinstance(res,QtCore.Qt.PenStyle)
		return res
	#----------------------------------------------------------------------
	def horizontalHeader(self):
		"""
		Returns the table views horizontal header.
		"""
		res = super(QTableView,self).horizontalHeader()
		isinstance(res,QtGui.QHeaderView)
		return res
	#----------------------------------------------------------------------
	def isCornerButtonEnabled(self):
		"""
		This property holds whether the button in the top-left corner is enabled.
		If this property is true then button in the top-left corner of the table view is enabled
		Clicking on this button will select all the cells in the table view.
		This property is true by default.
		"""
		res = super(QTableView,self).isCornerButtonEnabled()

		return res
	#----------------------------------------------------------------------
	def isSortingEnabled(self):
		"""
		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the table
		If this property is false, sorting is not enabled
		The default value is false.
		"""
		res = super(QTableView,self).isSortingEnabled()

		return res
	#----------------------------------------------------------------------
	def showGrid(self):
		"""
		This property holds whether the grid is shown.
		If this property is true a grid is drawn for the table; if the property is false, no grid is drawn
		The default value is true.
		"""
		res = super(QTableView,self).showGrid()

		return res
	#----------------------------------------------------------------------
	def verticalHeader(self):
		"""
		Returns the table views vertical header.
		"""
		res = super(QTableView,self).verticalHeader()
		isinstance(res,QtGui.QHeaderView)
		return res
	#----------------------------------------------------------------------
	def wordWrap(self):
		"""
		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is true by default.
		Note that even of wrapping is enabled, the cell will not be expanded to fit all text
		Ellipsis will be inserted according to the current PySide.QtGui.QAbstractItemView.textElideMode() .
		"""
		res = super(QTableView,self).wordWrap()

		return res
	#----------------------------------------------------------------------
	def columnAt(self,x):
		"""
		columnAt(x)
			x=QtCore.int

		Returns the column in which the given x-coordinate, x , in contents coordinates is located.
		"""
		res = super(QTableView,self).columnAt(x)

		return res
	#----------------------------------------------------------------------
	def columnSpan(self,row,column):
		"""
		columnSpan(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the column span of the table element at (row , column )
		The default is 1.
		"""
		res = super(QTableView,self).columnSpan(row,column)

		return res
	#----------------------------------------------------------------------
	def columnViewportPosition(self,column):
		"""
		columnViewportPosition(column)
			column=QtCore.int

		Returns the x-coordinate in contents coordinates of the given column .
		"""
		res = super(QTableView,self).columnViewportPosition(column)

		return res
	#----------------------------------------------------------------------
	def columnWidth(self,column):
		"""
		columnWidth(column)
			column=QtCore.int

		Returns the width of the given column .
		"""
		res = super(QTableView,self).columnWidth(column)

		return res
	#----------------------------------------------------------------------
	def isColumnHidden(self,column):
		"""
		isColumnHidden(column)
			column=QtCore.int

		Returns true if the given column is hidden; otherwise returns false.
		"""
		res = super(QTableView,self).isColumnHidden(column)

		return res
	#----------------------------------------------------------------------
	def isRowHidden(self,row):
		"""
		isRowHidden(row)
			row=QtCore.int

		Returns true if the given row is hidden; otherwise returns false.
		"""
		res = super(QTableView,self).isRowHidden(row)

		return res
	#----------------------------------------------------------------------
	def rowAt(self,y):
		"""
		rowAt(y)
			y=QtCore.int

		Returns the row in which the given y-coordinate, y , in contents coordinates is located.
		"""
		res = super(QTableView,self).rowAt(y)

		return res
	#----------------------------------------------------------------------
	def rowHeight(self,row):
		"""
		rowHeight(row)
			row=QtCore.int

		Returns the height of the given row .
		"""
		res = super(QTableView,self).rowHeight(row)

		return res
	#----------------------------------------------------------------------
	def rowSpan(self,row,column):
		"""
		rowSpan(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the row span of the table element at (row , column )
		The default is 1.
		"""
		res = super(QTableView,self).rowSpan(row,column)

		return res
	#----------------------------------------------------------------------
	def rowViewportPosition(self,row):
		"""
		rowViewportPosition(row)
			row=QtCore.int

		Returns the y-coordinate in contents coordinates of the given row .
		"""
		res = super(QTableView,self).rowViewportPosition(row)

		return res
	#----------------------------------------------------------------------
	def setColumnHidden(self,column,hide):
		"""
		setColumnHidden(column,hide)
			column=QtCore.int
			hide=QtCore.bool

		If hide is true the given column will be hidden; otherwise it will be shown.
		"""
		res = super(QTableView,self).setColumnHidden(column,hide)
		return res
	#----------------------------------------------------------------------
	def setColumnWidth(self,column,width):
		"""
		setColumnWidth(column,width)
			column=QtCore.int
			width=QtCore.int

		Sets the width of the given column to be width .
		"""
		res = super(QTableView,self).setColumnWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setCornerButtonEnabled(self,enable):
		"""
		setCornerButtonEnabled(enable)
			enable=QtCore.bool

		This property holds whether the button in the top-left corner is enabled.
		If this property is true then button in the top-left corner of the table view is enabled
		Clicking on this button will select all the cells in the table view.
		This property is true by default.
		"""
		res = super(QTableView,self).setCornerButtonEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setGridStyle(self,style):
		"""
		setGridStyle(style)
			style=QtCore.Qt.PenStyle

		This property holds the pen style used to draw the grid..
		This property holds the style used when drawing the grid (see PySide.QtGui.QTableView.showGrid() ).
		"""
		res = super(QTableView,self).setGridStyle(style)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeader(self,header):
		"""
		setHorizontalHeader(header)
			header=QtGui.QHeaderView

		Sets the widget to use for the horizontal header to header .
		"""
		res = super(QTableView,self).setHorizontalHeader(header)
		return res
	#----------------------------------------------------------------------
	def setRowHeight(self,row,height):
		"""
		setRowHeight(row,height)
			row=QtCore.int
			height=QtCore.int

		Sets the height of the given row to be height .
		"""
		res = super(QTableView,self).setRowHeight(row,height)
		return res
	#----------------------------------------------------------------------
	def setRowHidden(self,row,hide):
		"""
		setRowHidden(row,hide)
			row=QtCore.int
			hide=QtCore.bool

		If hide is true row will be hidden, otherwise it will be shown.
		"""
		res = super(QTableView,self).setRowHidden(row,hide)
		return res
	#----------------------------------------------------------------------
	def setSortingEnabled(self,enable):
		"""
		setSortingEnabled(enable)
			enable=QtCore.bool

		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the table
		If this property is false, sorting is not enabled
		The default value is false.
		"""
		res = super(QTableView,self).setSortingEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setSpan(self,row,column,rowSpan,columnSpan):
		"""
		setSpan(row,column,rowSpan,columnSpan)
			row=QtCore.int
			column=QtCore.int
			rowSpan=QtCore.int
			columnSpan=QtCore.int

		Sets the span of the table element at (row , column ) to the number of rows and columns specified by (rowSpanCount , columnSpanCount ).
		"""
		res = super(QTableView,self).setSpan(row,column,rowSpan,columnSpan)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeader(self,header):
		"""
		setVerticalHeader(header)
			header=QtGui.QHeaderView

		Sets the widget to use for the vertical header to header .
		"""
		res = super(QTableView,self).setVerticalHeader(header)
		return res
	#----------------------------------------------------------------------
	def setWordWrap(self,on):
		"""
		setWordWrap(on)
			on=QtCore.bool

		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is true by default.
		Note that even of wrapping is enabled, the cell will not be expanded to fit all text
		Ellipsis will be inserted according to the current PySide.QtGui.QAbstractItemView.textElideMode() .
		"""
		res = super(QTableView,self).setWordWrap(on)
		return res
	#----------------------------------------------------------------------
	def sortByColumn(self,column,order):
		"""
		sortByColumn(column,order)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QTableView,self).sortByColumn(column,order)
		return res
	#----------------------------------------------------------------------
	def visualIndex(self,index):
		"""
		visualIndex(index)
			index=QtCore.QModelIndex


		"""
		res = super(QTableView,self).visualIndex(index)

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
		res = super(QTableView,self).alternatingRowColors()

		return res
	#----------------------------------------------------------------------
	def autoScrollMargin(self):
		"""
		This property holds the size of the area when auto scrolling is triggered.
		This property controls the size of the area at the edge of the viewport that triggers autoscrolling
		The default value is 16 pixels.
		"""
		res = super(QTableView,self).autoScrollMargin()

		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		Returns the model index of the current item.
		"""
		res = super(QTableView,self).currentIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def defaultDropAction(self):
		"""
		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QTableView,self).defaultDropAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def dirtyRegionOffset(self):
		"""
		Returns the offset of the dirty regions in the view.
		If you use PySide.QtGui.QAbstractItemView.scrollDirtyRegion() and implement a PySide.QtGui.QAbstractScrollArea.paintEvent() in a subclass of PySide.QtGui.QAbstractItemView , you should translate the area given by the paint event with the offset returned from this function.
		"""
		res = super(QTableView,self).dirtyRegionOffset()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def doAutoScroll(self):
		"""

		"""
		res = super(QTableView,self).doAutoScroll()
		return res
	#----------------------------------------------------------------------
	def doItemsLayout(self):
		"""
		This function is intended to lay out the items in the view
		The default implementation just calls PySide.QtGui.QAbstractItemView.updateGeometries() and updates the viewport.
		"""
		res = super(QTableView,self).doItemsLayout()
		return res
	#----------------------------------------------------------------------
	def dragDropMode(self):
		"""
		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QTableView,self).dragDropMode()
		isinstance(res,QtGui.QAbstractItemView.DragDropMode)
		return res
	#----------------------------------------------------------------------
	def dragDropOverwriteMode(self):
		"""
		This property holds the views drag and drop behavior.
		If its value is true , the selected data will overwrite the existing item data when dropped, while moving the data will clear the item
		If its value is false , the selected data will be inserted as a new item when the data is dropped
		When the data is moved, the item is removed as well.
		The default value is false , as in the PySide.QtGui.QListView and PySide.QtGui.QTreeView subclasses
		In the PySide.QtGui.QTableView subclass, on the other hand, the property has been set to true .
		Note: This is not intended to prevent overwriting of items
		The models implementation of flags() should do that by not returning Qt.ItemIsDropEnabled .
		"""
		res = super(QTableView,self).dragDropOverwriteMode()

		return res
	#----------------------------------------------------------------------
	def dragEnabled(self):
		"""
		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QTableView,self).dragEnabled()

		return res
	#----------------------------------------------------------------------
	def dropIndicatorPosition(self):
		"""
		Returns the position of the drop indicator in relation to the closest item.
		"""
		res = super(QTableView,self).dropIndicatorPosition()
		isinstance(res,QtGui.QAbstractItemView.DropIndicatorPosition)
		return res
	#----------------------------------------------------------------------
	def editTriggers(self):
		"""
		This property holds which actions will initiate item editing.
		This property is a selection of flags defined by QAbstractItemView.EditTrigger , combined using the OR operator
		The view will only initiate the editing of an item if the action performed is set in this property.
		"""
		res = super(QTableView,self).editTriggers()
		isinstance(res,QtGui.QAbstractItemView.EditTriggers)
		return res
	#----------------------------------------------------------------------
	def executeDelayedItemsLayout(self):
		"""
		Executes the scheduled layouts without waiting for the event processing to begin.
		"""
		res = super(QTableView,self).executeDelayedItemsLayout()
		return res
	#----------------------------------------------------------------------
	def hasAutoScroll(self):
		"""
		This property holds whether autoscrolling in drag move events is enabled.
		If this property is set to true (the default), the PySide.QtGui.QAbstractItemView automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge
		If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.
		This property only works if the viewport accepts drops
		Autoscroll is switched off by setting this property to false.
		"""
		res = super(QTableView,self).hasAutoScroll()

		return res
	#----------------------------------------------------------------------
	def horizontalOffset(self):
		"""
		Returns the horizontal offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QTableView,self).horizontalOffset()

		return res
	#----------------------------------------------------------------------
	def horizontalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the horizontal direction.
		This property controls how the view scroll its contents horizontally
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTableView,self).horizontalScrollMode()
		isinstance(res,QtGui.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QTableView,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the item delegate used by this view and model
		This is either one set with PySide.QtGui.QAbstractItemView.setItemDelegate() , or the default one.
		"""
		res = super(QTableView,self).itemDelegate()
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that this view is presenting.
		"""
		res = super(QTableView,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Reset the internal state of the view.
		"""
		res = super(QTableView,self).reset()
		return res
	#----------------------------------------------------------------------
	def rootIndex(self):
		"""
		Returns the model index of the models root item
		The root item is the parent item to the views toplevel items
		The root can be invalid.
		"""
		res = super(QTableView,self).rootIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def scheduleDelayedItemsLayout(self):
		"""
		Schedules a layout of the items in the view to be executed when the event processing starts.
		Even if PySide.QtGui.QAbstractItemView.scheduleDelayedItemsLayout() is called multiple times before events are processed, the view will only do the layout once.
		"""
		res = super(QTableView,self).scheduleDelayedItemsLayout()
		return res
	#----------------------------------------------------------------------
	def selectAll(self):
		"""
		Selects all items in the view
		This function will use the selection behavior set on the view when selecting.
		"""
		res = super(QTableView,self).selectAll()
		return res
	#----------------------------------------------------------------------
	def selectedIndexes(self):
		"""
		This convenience function returns a list of all selected and non-hidden item indexes in the view
		The list contains no duplicates, and is not sorted.
		"""
		res = super(QTableView,self).selectedIndexes()
		return res
	#----------------------------------------------------------------------
	def selectionBehavior(self):
		"""
		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QTableView,self).selectionBehavior()
		isinstance(res,QtGui.QAbstractItemView.SelectionBehavior)
		return res
	#----------------------------------------------------------------------
	def selectionMode(self):
		"""
		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QTableView,self).selectionMode()
		isinstance(res,QtGui.QAbstractItemView.SelectionMode)
		return res
	#----------------------------------------------------------------------
	def selectionModel(self):
		"""
		Returns the current selection model.
		"""
		res = super(QTableView,self).selectionModel()
		isinstance(res,QtGui.QItemSelectionModel)
		return res
	#----------------------------------------------------------------------
	def showDropIndicator(self):
		"""
		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QTableView,self).showDropIndicator()

		return res
	#----------------------------------------------------------------------
	def startAutoScroll(self):
		"""

		"""
		res = super(QTableView,self).startAutoScroll()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the item views state.
		"""
		res = super(QTableView,self).state()
		isinstance(res,QtGui.QAbstractItemView.State)
		return res
	#----------------------------------------------------------------------
	def stopAutoScroll(self):
		"""

		"""
		res = super(QTableView,self).stopAutoScroll()
		return res
	#----------------------------------------------------------------------
	def tabKeyNavigation(self):
		"""
		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QTableView,self).tabKeyNavigation()

		return res
	#----------------------------------------------------------------------
	def textElideMode(self):
		"""
		This property holds the position of the ..
		in elided text..
		The default value for all item views is Qt.ElideRight .
		"""
		res = super(QTableView,self).textElideMode()
		isinstance(res,QtCore.Qt.TextElideMode)
		return res
	#----------------------------------------------------------------------
	def updateEditorData(self):
		"""
		Updates the data shown in the open editor widgets in the view.
		"""
		res = super(QTableView,self).updateEditorData()
		return res
	#----------------------------------------------------------------------
	def updateEditorGeometries(self):
		"""
		Updates the geometry of the open editor widgets in the view.
		"""
		res = super(QTableView,self).updateEditorGeometries()
		return res
	#----------------------------------------------------------------------
	def updateGeometries(self):
		"""
		Updates the geometry of the child widgets of the view.
		"""
		res = super(QTableView,self).updateGeometries()
		return res
	#----------------------------------------------------------------------
	def verticalOffset(self):
		"""
		Returns the vertical offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QTableView,self).verticalOffset()

		return res
	#----------------------------------------------------------------------
	def verticalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the vertical direction.
		This property controls how the view scroll its contents vertically
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTableView,self).verticalScrollMode()
		isinstance(res,QtGui.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def viewOptions(self):
		"""
		Returns a PySide.QtGui.QStyleOptionViewItem structure populated with the views palette, font, state, alignments etc.
		"""
		res = super(QTableView,self).viewOptions()
		isinstance(res,QtGui.QStyleOptionViewItem)
		return res
	#----------------------------------------------------------------------
	def viewportEntered(self):
		"""

		"""
		res = super(QTableView,self).viewportEntered()
		return res
	#----------------------------------------------------------------------
	def closeEditor(self,editor,hint):
		"""
		closeEditor(editor,hint)
			editor=QtGui.QWidget
			hint=QtGui.QAbstractItemDelegate.EndEditHint


		"""
		res = super(QTableView,self).closeEditor(editor,hint)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,index):
		"""
		closePersistentEditor(index)
			index=QtCore.QModelIndex

		Closes the persistent editor for the item at the given index .
		"""
		res = super(QTableView,self).closePersistentEditor(index)
		return res
	#----------------------------------------------------------------------
	def commitData(self,editor):
		"""
		commitData(editor)
			editor=QtGui.QWidget

		Commit the data in the editor to the model.
		"""
		res = super(QTableView,self).commitData(editor)
		return res
	#----------------------------------------------------------------------
	def currentChanged(self,current,previous):
		"""
		currentChanged(current,previous)
			current=QtCore.QModelIndex
			previous=QtCore.QModelIndex

		This slot is called when a new item becomes the current item
		The previous current item is specified by the previous index, and the new item by the current index.
		If you want to know about changes to items see the PySide.QtGui.QAbstractItemView.dataChanged() signal.
		"""
		res = super(QTableView,self).currentChanged(current,previous)
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
		res = super(QTableView,self).dataChanged(topLeft,bottomRight)
		return res
	#----------------------------------------------------------------------
	def edit(self,*args,**kwargs):
		"""
		edit(index,trigger,event)
			index=QtCore.QModelIndex
			trigger=QtGui.QAbstractItemView.EditTrigger
			event=QtCore.QEvent

		edit(index)
			index=QtCore.QModelIndex

		Starts editing the item at index , creating an editor if necessary, and returns true if the views QAbstractItemView.State is now EditingState ; otherwise returns false.
		The action that caused the editing process is described by trigger , and the associated event is specified by event .
		Editing can be forced by specifying the trigger to be QAbstractItemView.AllEditTriggers .
		"""
		res = super(QTableView,self).edit(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def editorDestroyed(self,editor):
		"""
		editorDestroyed(editor)
			editor=QtCore.QObject

		This function is called when the given editor has been destroyed.
		"""
		res = super(QTableView,self).editorDestroyed(editor)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarAction(self,action):
		"""
		horizontalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QTableView,self).horizontalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarValueChanged(self,value):
		"""
		horizontalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QTableView,self).horizontalScrollbarValueChanged(value)
		return res
	#----------------------------------------------------------------------
	def indexAt(self,point):
		"""
		indexAt(point)
			point=QtCore.QPoint

		Returns the model index of the item at the viewport coordinates point .
		In the base class this is a pure virtual function.
		"""
		res = super(QTableView,self).indexAt(point)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexWidget(self,index):
		"""
		indexWidget(index)
			index=QtCore.QModelIndex

		Returns the widget for the item at the given index .
		"""
		res = super(QTableView,self).indexWidget(index)
		isinstance(res,QtGui.QWidget)
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
		res = super(QTableView,self).isIndexHidden(index)

		return res
	#----------------------------------------------------------------------
	def itemDelegate(self,index):
		"""
		itemDelegate(index)
			index=QtCore.QModelIndex

		Returns the item delegate used by this view and model for the given index .
		"""
		res = super(QTableView,self).itemDelegate(index)
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def itemDelegateForColumn(self,column):
		"""
		itemDelegateForColumn(column)
			column=QtCore.int

		Returns the item delegate used by this view and model for the given column
		You can call PySide.QtGui.QAbstractItemView.itemDelegate() to get a pointer to the current delegate for a given index.
		"""
		res = super(QTableView,self).itemDelegateForColumn(column)
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def itemDelegateForRow(self,row):
		"""
		itemDelegateForRow(row)
			row=QtCore.int

		Returns the item delegate used by this view and model for the given row , or 0 if no delegate has been assigned
		You can call PySide.QtGui.QAbstractItemView.itemDelegate() to get a pointer to the current delegate for a given index.
		"""
		res = super(QTableView,self).itemDelegateForRow(row)
		isinstance(res,QtGui.QAbstractItemDelegate)
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
		res = super(QTableView,self).keyboardSearch(search)
		return res
	#----------------------------------------------------------------------
	def moveCursor(self,cursorAction,modifiers):
		"""
		moveCursor(cursorAction,modifiers)
			cursorAction=QtGui.QAbstractItemView.CursorAction
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QTableView,self).moveCursor(cursorAction,modifiers)
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
		res = super(QTableView,self).openPersistentEditor(index)
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
		res = super(QTableView,self).rowsAboutToBeRemoved(parent,start,end)
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
		res = super(QTableView,self).rowsInserted(parent,start,end)
		return res
	#----------------------------------------------------------------------
	def scrollDirtyRegion(self,dx,dy):
		"""
		scrollDirtyRegion(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		Prepares the view for scrolling by (dx ,``dy`` ) pixels by moving the dirty regions in the opposite direction
		You only need to call this function if you are implementing a scrolling viewport in your view subclass.
		If you implement PySide.QtGui.QAbstractScrollArea.scrollContentsBy() in a subclass of PySide.QtGui.QAbstractItemView , call this function before you call QWidget.scroll() on the viewport
		Alternatively, just call PySide.QtGui.QAbstractItemView.update() .
		"""
		res = super(QTableView,self).scrollDirtyRegion(dx,dy)
		return res
	#----------------------------------------------------------------------
	def scrollTo(self,index,hint=None):
		"""
		scrollTo(index,hint=None)
			index=QtCore.QModelIndex
			hint=QtGui.QAbstractItemView.ScrollHint

		Scrolls the view if necessary to ensure that the item at index is visible
		The view will try to position the item according to the given hint .
		In the base class this is a pure virtual function.
		"""
		res = super(QTableView,self).scrollTo(index,hint)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self,selected,deselected):
		"""
		selectionChanged(selected,deselected)
			selected=QtGui.QItemSelection
			deselected=QtGui.QItemSelection

		This slot is called when the selection is changed
		The previous selection (which may be empty), is specified by deselected , and the new selection by selected .
		"""
		res = super(QTableView,self).selectionChanged(selected,deselected)
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
		res = super(QTableView,self).selectionCommand(index,event)
		isinstance(res,QtGui.QItemSelectionModel.SelectionFlags)
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
		res = super(QTableView,self).setAlternatingRowColors(enable)
		return res
	#----------------------------------------------------------------------
	def setAutoScroll(self,enable):
		"""
		setAutoScroll(enable)
			enable=QtCore.bool

		This property holds whether autoscrolling in drag move events is enabled.
		If this property is set to true (the default), the PySide.QtGui.QAbstractItemView automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge
		If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.
		This property only works if the viewport accepts drops
		Autoscroll is switched off by setting this property to false.
		"""
		res = super(QTableView,self).setAutoScroll(enable)
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
		res = super(QTableView,self).setAutoScrollMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setDefaultDropAction(self,dropAction):
		"""
		setDefaultDropAction(dropAction)
			dropAction=QtCore.Qt.DropAction

		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QTableView,self).setDefaultDropAction(dropAction)
		return res
	#----------------------------------------------------------------------
	def setDirtyRegion(self,region):
		"""
		setDirtyRegion(region)
			region=QtGui.QRegion

		Marks the given region as dirty and schedules it to be updated
		You only need to call this function if you are implementing your own view subclass.
		"""
		res = super(QTableView,self).setDirtyRegion(region)
		return res
	#----------------------------------------------------------------------
	def setDragDropMode(self,behavior):
		"""
		setDragDropMode(behavior)
			behavior=QtGui.QAbstractItemView.DragDropMode

		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QTableView,self).setDragDropMode(behavior)
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
		The default value is false , as in the PySide.QtGui.QListView and PySide.QtGui.QTreeView subclasses
		In the PySide.QtGui.QTableView subclass, on the other hand, the property has been set to true .
		Note: This is not intended to prevent overwriting of items
		The models implementation of flags() should do that by not returning Qt.ItemIsDropEnabled .
		"""
		res = super(QTableView,self).setDragDropOverwriteMode(overwrite)
		return res
	#----------------------------------------------------------------------
	def setDragEnabled(self,enable):
		"""
		setDragEnabled(enable)
			enable=QtCore.bool

		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QTableView,self).setDragEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setDropIndicatorShown(self,enable):
		"""
		setDropIndicatorShown(enable)
			enable=QtCore.bool

		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QTableView,self).setDropIndicatorShown(enable)
		return res
	#----------------------------------------------------------------------
	def setEditTriggers(self,triggers):
		"""
		setEditTriggers(triggers)
			triggers=QtGui.QAbstractItemView.EditTriggers

		This property holds which actions will initiate item editing.
		This property is a selection of flags defined by QAbstractItemView.EditTrigger , combined using the OR operator
		The view will only initiate the editing of an item if the action performed is set in this property.
		"""
		res = super(QTableView,self).setEditTriggers(triggers)
		return res
	#----------------------------------------------------------------------
	def setHorizontalScrollMode(self,mode):
		"""
		setHorizontalScrollMode(mode)
			mode=QtGui.QAbstractItemView.ScrollMode

		This property holds how the view scrolls its contents in the horizontal direction.
		This property controls how the view scroll its contents horizontally
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTableView,self).setHorizontalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QtCore.QSize

		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QTableView,self).setIconSize(size)
		return res
	#----------------------------------------------------------------------
	def setIndexWidget(self,index,widget):
		"""
		setIndexWidget(index,widget)
			index=QtCore.QModelIndex
			widget=QtGui.QWidget

		Sets the given widget on the item at the given index , passing the ownership of the widget to the viewport.
		If index is invalid (e.g., if you pass the root index), this function will do nothing.
		The given widget s autoFillBackground property must be set to true, otherwise the widgets background will be transparent, showing both the model data and the item at the given index .
		If index widget A is replaced with index widget B, index widget A will be deleted
		For example, in the code snippet below, the PySide.QtGui.QLineEdit object will be deleted.
		This function should only be used to display static content within the visible area corresponding to an item of data
		If you want to display custom dynamic content or implement a custom editor widget, subclass PySide.QtGui.QItemDelegate instead.
		"""
		res = super(QTableView,self).setIndexWidget(index,widget)
		return res
	#----------------------------------------------------------------------
	def setItemDelegate(self,delegate):
		"""
		setItemDelegate(delegate)
			delegate=QtGui.QAbstractItemDelegate

		Sets the item delegate for this view and its model to delegate
		This is useful if you want complete control over the editing and display of items.
		Any existing delegate will be removed, but not deleted
		PySide.QtGui.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTableView,self).setItemDelegate(delegate)
		return res
	#----------------------------------------------------------------------
	def setItemDelegateForColumn(self,column,delegate):
		"""
		setItemDelegateForColumn(column,delegate)
			column=QtCore.int
			delegate=QtGui.QAbstractItemDelegate

		Sets the given item delegate used by this view and model for the given column
		All items on column will be drawn and managed by delegate instead of using the default delegate (i.e., PySide.QtGui.QAbstractItemView.itemDelegate() ).
		Any existing column delegate for column will be removed, but not deleted
		PySide.QtGui.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTableView,self).setItemDelegateForColumn(column,delegate)
		return res
	#----------------------------------------------------------------------
	def setItemDelegateForRow(self,row,delegate):
		"""
		setItemDelegateForRow(row,delegate)
			row=QtCore.int
			delegate=QtGui.QAbstractItemDelegate

		Sets the given item delegate used by this view and model for the given row
		All items on row will be drawn and managed by delegate instead of using the default delegate (i.e., PySide.QtGui.QAbstractItemView.itemDelegate() ).
		Any existing row delegate for row will be removed, but not deleted
		PySide.QtGui.QAbstractItemView does not take ownership of delegate .
		"""
		res = super(QTableView,self).setItemDelegateForRow(row,delegate)
		return res
	#----------------------------------------------------------------------
	def setModel(self,model):
		"""
		setModel(model)
			model=QtCore.QAbstractItemModel

		Sets the model for the view to present.
		This function will create and set a new selection model, replacing any model that was previously set with PySide.QtGui.QAbstractItemView.setSelectionModel()
		However, the old selection model will not be deleted as it may be shared between several views
		We recommend that you delete the old selection model if it is no longer required
		This is done with the following code:
		If both the old model and the old selection model do not have parents, or if their parents are long-lived objects, it may be preferable to call their deleteLater() functions to explicitly delete them.
		The view does not take ownership of the model unless it is the models parent object because the view may be shared between many different views.
		"""
		res = super(QTableView,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setRootIndex(self,index):
		"""
		setRootIndex(index)
			index=QtCore.QModelIndex

		Sets the root item to the item at the given index .
		"""
		res = super(QTableView,self).setRootIndex(index)
		return res
	#----------------------------------------------------------------------
	def setSelection(self,rect,command):
		"""
		setSelection(rect,command)
			rect=QtCore.QRect
			command=QtGui.QItemSelectionModel.SelectionFlags


		"""
		res = super(QTableView,self).setSelection(rect,command)
		return res
	#----------------------------------------------------------------------
	def setSelectionBehavior(self,behavior):
		"""
		setSelectionBehavior(behavior)
			behavior=QtGui.QAbstractItemView.SelectionBehavior

		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QTableView,self).setSelectionBehavior(behavior)
		return res
	#----------------------------------------------------------------------
	def setSelectionMode(self,mode):
		"""
		setSelectionMode(mode)
			mode=QtGui.QAbstractItemView.SelectionMode

		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QTableView,self).setSelectionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setSelectionModel(self,selectionModel):
		"""
		setSelectionModel(selectionModel)
			selectionModel=QtGui.QItemSelectionModel

		Sets the current selection model to the given selectionModel .
		Note that, if you call PySide.QtGui.QAbstractItemView.setModel() after this function, the given selectionModel will be replaced by one created by the view.
		"""
		res = super(QTableView,self).setSelectionModel(selectionModel)
		return res
	#----------------------------------------------------------------------
	def setState(self,state):
		"""
		setState(state)
			state=QtGui.QAbstractItemView.State

		Sets the item views state to the given state .
		"""
		res = super(QTableView,self).setState(state)
		return res
	#----------------------------------------------------------------------
	def setTabKeyNavigation(self,enable):
		"""
		setTabKeyNavigation(enable)
			enable=QtCore.bool

		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QTableView,self).setTabKeyNavigation(enable)
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
		res = super(QTableView,self).setTextElideMode(mode)
		return res
	#----------------------------------------------------------------------
	def setVerticalScrollMode(self,mode):
		"""
		setVerticalScrollMode(mode)
			mode=QtGui.QAbstractItemView.ScrollMode

		This property holds how the view scrolls its contents in the vertical direction.
		This property controls how the view scroll its contents vertically
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QTableView,self).setVerticalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def sizeHintForColumn(self,column):
		"""
		sizeHintForColumn(column)
			column=QtCore.int

		Returns the width size hint for the specified column or -1 if there is no model.
		This function is used in views with a horizontal header to find the size hint for a header section based on the contents of the given column .
		"""
		res = super(QTableView,self).sizeHintForColumn(column)

		return res
	#----------------------------------------------------------------------
	def sizeHintForIndex(self,index):
		"""
		sizeHintForIndex(index)
			index=QtCore.QModelIndex

		Returns the size hint for the item with the specified index or an invalid size for invalid indexes.
		"""
		res = super(QTableView,self).sizeHintForIndex(index)
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
		res = super(QTableView,self).sizeHintForRow(row)

		return res
	#----------------------------------------------------------------------
	def startDrag(self,supportedActions):
		"""
		startDrag(supportedActions)
			supportedActions=QtCore.Qt.DropActions


		"""
		res = super(QTableView,self).startDrag(supportedActions)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarAction(self,action):
		"""
		verticalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QTableView,self).verticalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarValueChanged(self,value):
		"""
		verticalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QTableView,self).verticalScrollbarValueChanged(value)
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
		res = super(QTableView,self).visualRect(index)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def visualRegionForSelection(self,selection):
		"""
		visualRegionForSelection(selection)
			selection=QtGui.QItemSelection

		Returns the region from the viewport of the items in the given selection .
		In the base class this is a pure virtual function.
		"""
		res = super(QTableView,self).visualRegionForSelection(selection)
		isinstance(res,QtGui.QRegion)
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

	ClearSpans            = property(clearSpans)
	GridStyle             = property(gridStyle)
	HorizontalHeader      = property(horizontalHeader)
	IsCornerButtonEnabled = property(isCornerButtonEnabled)
	IsSortingEnabled      = property(isSortingEnabled)
	ShowGrid              = property(showGrid)
	VerticalHeader        = property(verticalHeader)
	WordWrap              = property(wordWrap)

