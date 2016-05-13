import QT
import QT.DataModels.Qt_Roles_And_Enums

Qt_Roles_And_Enums = QT.DataModels.Qt_Roles_And_Enums
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
user_type_counter = QT.user_type_counter
Item_Data_Roles   = QT.DataModels.Qt_Roles_And_Enums.Standered_Item_Data_Roles
AbstractItemView  = QT.DataModels.Qt_Roles_And_Enums.AbstractItemView
Constants         = QT.DataModels.Qt_Roles_And_Enums.Constants


class QListView(QtGui.QListView):
	''''''
	Item_Data_Roles = Item_Data_Roles
	def __init__(self,*args,**kwargs):
		''''''
		super(QListView,self).__init__(*args,**kwargs)
	
	def dropEvent(self, event):
		md =  event.mimeData()
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drop_destination  =  self
		md.setData("AW/INFO/DragDrop-Destination", self.objectName())
		return super(QListView,self).dropEvent(event)
		
	#def dragMoveEvent(self, event):
		#md =  event.mimeData()
		#if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			#md.drop_destination  =  self
		#md.setData("AW/INFO/DragDrop-Destination", self.objectName())
		#return super(QListView,self).dragMoveEvent(event)
	
	def dragEnterEvent(self, event):
		self.setAcceptDrops(True)
		md =  event.mimeData()
		if isinstance(md, MimeData.Drag_And_Drop_MimeData):
			md.drag_source = event.source()
		md.setData("AW/INFO/DragDrop-Source", self.objectName())
		return super(QListView,self).dragEnterEvent(event)
	#----------------------------------------------------------------------
	def batchSize(self):
		"""
		This property holds the number of items laid out in each batch if PySide.QtGui.QListView.layoutMode() is set to Batched .
		The default value is 100.
		"""
		res = super(QListView,self).batchSize()

		return res
	#----------------------------------------------------------------------
	def clearPropertyFlags(self):
		"""
		Clears the PySide.QtGui.QListView -specific property flags
		See PySide.QtGui.QListView.viewMode() .
		Properties inherited from PySide.QtGui.QAbstractItemView are not covered by the property flags
		Specifically, PySide.QtGui.QAbstractItemView.dragEnabled() and acceptsDrops are computed by PySide.QtGui.QListView when calling PySide.QtGui.QListView.setMovement() or PySide.QtGui.QListView.setViewMode() .
		"""
		res = super(QListView,self).clearPropertyFlags()
		return res
	#----------------------------------------------------------------------
	def contentsSize(self):
		"""

		"""
		res = super(QListView,self).contentsSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def flow(self):
		"""
		This property holds which direction the items layout should flow..
		If this property is LeftToRight , the items will be laid out left to right
		If the PySide.QtGui.QListView.isWrapping() property is true, the layout will wrap when it reaches the right side of the visible area
		If this property is TopToBottom , the items will be laid out from the top of the visible area, wrapping when it reaches the bottom.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is set to TopToBottom .
		"""
		res = super(QListView,self).flow()
		isinstance(res,QtGui.QListView.Flow)
		return res
	#----------------------------------------------------------------------
	def gridSize(self):
		"""
		This property holds the size of the layout grid.
		This property is the size of the grid in which the items are laid out
		The default is an empty size which means that there is no grid and the layout is not done in a grid
		Setting this property to a non-empty size switches on the grid layout
		(When a grid layout is in force the PySide.QtGui.QListView.spacing() property is ignored.)
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QListView,self).gridSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isSelectionRectVisible(self):
		"""
		This property holds if the selection rectangle should be visible.
		If this property is true then the selection rectangle is visible; otherwise it will be hidden.
		By default, this property is false.
		"""
		res = super(QListView,self).isSelectionRectVisible()

		return res
	#----------------------------------------------------------------------
	def isWrapping(self):
		"""
		This property holds whether the items layout should wrap..
		This property holds whether the layout should wrap when there is no more space in the visible area
		The point at which the layout wraps depends on the PySide.QtGui.QListView.flow() property.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is false.
		"""
		res = super(QListView,self).isWrapping()

		return res
	#----------------------------------------------------------------------
	def layoutMode(self):
		"""
		This property determines whether the layout of items should happen immediately or be delayed..
		This property holds the layout mode for the items
		When the mode is SinglePass (the default), the items are laid out all in one go
		When the mode is Batched , the items are laid out in batches of PySide.QtGui.QListView.batchSize() items, while processing events
		This makes it possible to instantly view and interact with the visible items while the rest are being laid out.
		"""
		res = super(QListView,self).layoutMode()
		isinstance(res,QtGui.QListView.LayoutMode)
		return res
	#----------------------------------------------------------------------
	def modelColumn(self):
		"""
		This property holds the column in the model that is visible.
		By default, this property contains 0, indicating that the first column in the model will be shown.
		"""
		res = super(QListView,self).modelColumn()

		return res
	#----------------------------------------------------------------------
	def movement(self):
		"""
		This property holds whether the items can be moved freely, are snapped to a grid, or cannot be moved at all..
		This property determines how the user can move the items in the view
		Static means that the items cant be moved the user
		Free means that the user can drag and drop the items to any position in the view
		Snap means that the user can drag and drop the items, but only to the positions in a notional grid signified by the PySide.QtGui.QListView.gridSize() property.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is set to Static .
		"""
		res = super(QListView,self).movement()
		isinstance(res,QtGui.QListView.Movement)
		return res
	#----------------------------------------------------------------------
	def resizeMode(self):
		"""
		This property holds whether the items are laid out again when the view is resized..
		If this property is Adjust , the items will be laid out again when the view is resized
		If the value is Fixed , the items will not be laid out when the view is resized.
		By default, this property is set to Fixed .
		"""
		res = super(QListView,self).resizeMode()
		isinstance(res,QtGui.QListView.ResizeMode)
		return res
	#----------------------------------------------------------------------
	def spacing(self):
		"""
		This property holds the space around the items in the layout.
		This property is the size of the empty space that is padded around an item in the layout.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property contains a value of 0.
		"""
		res = super(QListView,self).spacing()

		return res
	#----------------------------------------------------------------------
	def uniformItemSizes(self):
		"""
		This property holds whether all items in the listview have the same size.
		This property should only be set to true if it is guaranteed that all items in the view have the same size
		This enables the view to do some optimizations for performance purposes.
		By default, this property is false.
		"""
		res = super(QListView,self).uniformItemSizes()

		return res
	#----------------------------------------------------------------------
	def viewMode(self):
		"""
		This property holds the view mode of the PySide.QtGui.QListView ..
		This property will change the other unset properties to conform with the set view mode
		PySide.QtGui.QListView -specific properties that have already been set will not be changed, unless PySide.QtGui.QListView.clearPropertyFlags() has been called.
		Setting the view mode will enable or disable drag and drop based on the selected movement
		For ListMode , the default movement is Static (drag and drop disabled); for IconMode , the default movement is Free (drag and drop enabled).
		"""
		res = super(QListView,self).viewMode()
		isinstance(res,QtGui.QListView.ViewMode)
		return res
	#----------------------------------------------------------------------
	def wordWrap(self):
		"""
		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is false by default.
		Please note that even if wrapping is enabled, the cell will not be expanded to make room for the text
		It will print ellipsis for text that cannot be shown, according to the views PySide.QtGui.QAbstractItemView.textElideMode() .
		"""
		res = super(QListView,self).wordWrap()

		return res
	#----------------------------------------------------------------------
	def internalDrag(self,supportedActions):
		"""
		internalDrag(supportedActions)
			supportedActions=QtCore.Qt.DropActions


		"""
		res = super(QListView,self).internalDrag(supportedActions)
		return res
	#----------------------------------------------------------------------
	def internalDrop(self,e):
		"""
		internalDrop(e)
			e=QtGui.QDropEvent

		Called whenever items from the view is dropped on the viewport
		The event provides additional information.
		"""
		res = super(QListView,self).internalDrop(e)
		return res
	#----------------------------------------------------------------------
	def isRowHidden(self,row):
		"""
		isRowHidden(row)
			row=QtCore.int

		Returns true if the row is hidden; otherwise returns false.
		"""
		res = super(QListView,self).isRowHidden(row)

		return res
	#----------------------------------------------------------------------
	def rectForIndex(self,index):
		"""
		rectForIndex(index)
			index=QtCore.QModelIndex

		Returns the rectangle of the item at position index in the model
		The rectangle is in contents coordinates.
		"""
		res = super(QListView,self).rectForIndex(index)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def resizeContents(self,width,height):
		"""
		resizeContents(width,height)
			width=QtCore.int
			height=QtCore.int

		Resize the internal contents to width and height and set the scroll bar ranges accordingly.
		"""
		res = super(QListView,self).resizeContents(width,height)
		return res
	#----------------------------------------------------------------------
	def setBatchSize(self,batchSize):
		"""
		setBatchSize(batchSize)
			batchSize=QtCore.int

		This property holds the number of items laid out in each batch if PySide.QtGui.QListView.layoutMode() is set to Batched .
		The default value is 100.
		"""
		res = super(QListView,self).setBatchSize(batchSize)
		return res
	#----------------------------------------------------------------------
	def setFlow(self,flow):
		"""
		setFlow(flow)
			flow=QtGui.QListView.Flow

		This property holds which direction the items layout should flow..
		If this property is LeftToRight , the items will be laid out left to right
		If the PySide.QtGui.QListView.isWrapping() property is true, the layout will wrap when it reaches the right side of the visible area
		If this property is TopToBottom , the items will be laid out from the top of the visible area, wrapping when it reaches the bottom.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is set to TopToBottom .
		"""
		res = super(QListView,self).setFlow(flow)
		return res
	#----------------------------------------------------------------------
	def setGridSize(self,size):
		"""
		setGridSize(size)
			size=QtCore.QSize

		This property holds the size of the layout grid.
		This property is the size of the grid in which the items are laid out
		The default is an empty size which means that there is no grid and the layout is not done in a grid
		Setting this property to a non-empty size switches on the grid layout
		(When a grid layout is in force the PySide.QtGui.QListView.spacing() property is ignored.)
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QListView,self).setGridSize(size)
		return res
	#----------------------------------------------------------------------
	def setLayoutMode(self,mode):
		"""
		setLayoutMode(mode)
			mode=QtGui.QListView.LayoutMode

		This property determines whether the layout of items should happen immediately or be delayed..
		This property holds the layout mode for the items
		When the mode is SinglePass (the default), the items are laid out all in one go
		When the mode is Batched , the items are laid out in batches of PySide.QtGui.QListView.batchSize() items, while processing events
		This makes it possible to instantly view and interact with the visible items while the rest are being laid out.
		"""
		res = super(QListView,self).setLayoutMode(mode)
		return res
	#----------------------------------------------------------------------
	def setModelColumn(self,column):
		"""
		setModelColumn(column)
			column=QtCore.int

		This property holds the column in the model that is visible.
		By default, this property contains 0, indicating that the first column in the model will be shown.
		"""
		res = super(QListView,self).setModelColumn(column)
		return res
	#----------------------------------------------------------------------
	def setMovement(self,movement):
		"""
		setMovement(movement)
			movement=QtGui.QListView.Movement

		This property holds whether the items can be moved freely, are snapped to a grid, or cannot be moved at all..
		This property determines how the user can move the items in the view
		Static means that the items cant be moved the user
		Free means that the user can drag and drop the items to any position in the view
		Snap means that the user can drag and drop the items, but only to the positions in a notional grid signified by the PySide.QtGui.QListView.gridSize() property.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is set to Static .
		"""
		res = super(QListView,self).setMovement(movement)
		return res
	#----------------------------------------------------------------------
	def setPositionForIndex(self,position,index):
		"""
		setPositionForIndex(position,index)
			position=QtCore.QPoint
			index=QtCore.QModelIndex

		Sets the contents position of the item at index in the model to the given position
		If the list views movement mode is Static or its view mode is ListView , this function will have no effect.
		"""
		res = super(QListView,self).setPositionForIndex(position,index)
		return res
	#----------------------------------------------------------------------
	def setResizeMode(self,mode):
		"""
		setResizeMode(mode)
			mode=QtGui.QListView.ResizeMode

		This property holds whether the items are laid out again when the view is resized..
		If this property is Adjust , the items will be laid out again when the view is resized
		If the value is Fixed , the items will not be laid out when the view is resized.
		By default, this property is set to Fixed .
		"""
		res = super(QListView,self).setResizeMode(mode)
		return res
	#----------------------------------------------------------------------
	def setRowHidden(self,row,hide):
		"""
		setRowHidden(row,hide)
			row=QtCore.int
			hide=QtCore.bool

		If hide is true, the given row will be hidden; otherwise the row will be shown.
		"""
		res = super(QListView,self).setRowHidden(row,hide)
		return res
	#----------------------------------------------------------------------
	def setSelectionRectVisible(self,show):
		"""
		setSelectionRectVisible(show)
			show=QtCore.bool

		This property holds if the selection rectangle should be visible.
		If this property is true then the selection rectangle is visible; otherwise it will be hidden.
		By default, this property is false.
		"""
		res = super(QListView,self).setSelectionRectVisible(show)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,space):
		"""
		setSpacing(space)
			space=QtCore.int

		This property holds the space around the items in the layout.
		This property is the size of the empty space that is padded around an item in the layout.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property contains a value of 0.
		"""
		res = super(QListView,self).setSpacing(space)
		return res
	#----------------------------------------------------------------------
	def setUniformItemSizes(self,enable):
		"""
		setUniformItemSizes(enable)
			enable=QtCore.bool

		This property holds whether all items in the listview have the same size.
		This property should only be set to true if it is guaranteed that all items in the view have the same size
		This enables the view to do some optimizations for performance purposes.
		By default, this property is false.
		"""
		res = super(QListView,self).setUniformItemSizes(enable)
		return res
	#----------------------------------------------------------------------
	def setViewMode(self,mode):
		"""
		setViewMode(mode)
			mode=QtGui.QListView.ViewMode

		This property holds the view mode of the PySide.QtGui.QListView ..
		This property will change the other unset properties to conform with the set view mode
		PySide.QtGui.QListView -specific properties that have already been set will not be changed, unless PySide.QtGui.QListView.clearPropertyFlags() has been called.
		Setting the view mode will enable or disable drag and drop based on the selected movement
		For ListMode , the default movement is Static (drag and drop disabled); for IconMode , the default movement is Free (drag and drop enabled).
		"""
		res = super(QListView,self).setViewMode(mode)
		return res
	#----------------------------------------------------------------------
	def setWordWrap(self,on):
		"""
		setWordWrap(on)
			on=QtCore.bool

		This property holds the item text word-wrapping policy.
		If this property is true then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all
		This property is false by default.
		Please note that even if wrapping is enabled, the cell will not be expanded to make room for the text
		It will print ellipsis for text that cannot be shown, according to the views PySide.QtGui.QAbstractItemView.textElideMode() .
		"""
		res = super(QListView,self).setWordWrap(on)
		return res
	#----------------------------------------------------------------------
	def setWrapping(self,enable):
		"""
		setWrapping(enable)
			enable=QtCore.bool

		This property holds whether the items layout should wrap..
		This property holds whether the layout should wrap when there is no more space in the visible area
		The point at which the layout wraps depends on the PySide.QtGui.QListView.flow() property.
		Setting this property when the view is visible will cause the items to be laid out again.
		By default, this property is false.
		"""
		res = super(QListView,self).setWrapping(enable)
		return res
	#----------------------------------------------------------------------
	def visualIndex(self,index):
		"""
		visualIndex(index)
			index=QtCore.QModelIndex


		"""
		res = super(QListView,self).visualIndex(index)

		return res



	#----------------------------------------------------------------------
	def alternatingRowColors(self):
		"""
		This property holds whether to draw the background using alternating colors.
		If this property is true, the item background will be drawn using QPalette.Base and QPalette.AlternateBase ; otherwise the background will be drawn using the QPalette.Base color.
		By default, this property is false.
		"""
		res = super(QListView,self).alternatingRowColors()

		return res
	#----------------------------------------------------------------------
	def autoScrollMargin(self):
		"""
		This property holds the size of the area when auto scrolling is triggered.
		This property controls the size of the area at the edge of the viewport that triggers autoscrolling
		The default value is 16 pixels.
		"""
		res = super(QListView,self).autoScrollMargin()

		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		Returns the model index of the current item.
		"""
		res = super(QListView,self).currentIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def defaultDropAction(self):
		"""
		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QListView,self).defaultDropAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def dirtyRegionOffset(self):
		"""
		Returns the offset of the dirty regions in the view.
		If you use PySide.QtGui.QAbstractItemView.scrollDirtyRegion() and implement a PySide.QtGui.QAbstractScrollArea.paintEvent() in a subclass of PySide.QtGui.QAbstractItemView , you should translate the area given by the paint event with the offset returned from this function.
		"""
		res = super(QListView,self).dirtyRegionOffset()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def doAutoScroll(self):
		"""

		"""
		res = super(QListView,self).doAutoScroll()
		return res
	#----------------------------------------------------------------------
	def doItemsLayout(self):
		"""
		This function is intended to lay out the items in the view
		The default implementation just calls PySide.QtGui.QAbstractItemView.updateGeometries() and updates the viewport.
		"""
		res = super(QListView,self).doItemsLayout()
		return res
	#----------------------------------------------------------------------
	def dragDropMode(self):
		"""
		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QListView,self).dragDropMode()
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
		res = super(QListView,self).dragDropOverwriteMode()

		return res
	#----------------------------------------------------------------------
	def dragEnabled(self):
		"""
		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QListView,self).dragEnabled()

		return res
	#----------------------------------------------------------------------
	def dropIndicatorPosition(self):
		"""
		Returns the position of the drop indicator in relation to the closest item.
		"""
		res = super(QListView,self).dropIndicatorPosition()
		isinstance(res,QtGui.QAbstractItemView.DropIndicatorPosition)
		return res
	#----------------------------------------------------------------------
	def editTriggers(self):
		"""
		This property holds which actions will initiate item editing.
		This property is a selection of flags defined by QAbstractItemView.EditTrigger , combined using the OR operator
		The view will only initiate the editing of an item if the action performed is set in this property.
		"""
		res = super(QListView,self).editTriggers()
		isinstance(res,QtGui.QAbstractItemView.EditTriggers)
		return res
	#----------------------------------------------------------------------
	def executeDelayedItemsLayout(self):
		"""
		Executes the scheduled layouts without waiting for the event processing to begin.
		"""
		res = super(QListView,self).executeDelayedItemsLayout()
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
		res = super(QListView,self).hasAutoScroll()

		return res
	#----------------------------------------------------------------------
	def horizontalOffset(self):
		"""
		Returns the horizontal offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QListView,self).horizontalOffset()

		return res
	#----------------------------------------------------------------------
	def horizontalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the horizontal direction.
		This property controls how the view scroll its contents horizontally
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QListView,self).horizontalScrollMode()
		isinstance(res,QtGui.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QListView,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the item delegate used by this view and model
		This is either one set with PySide.QtGui.QAbstractItemView.setItemDelegate() , or the default one.
		"""
		res = super(QListView,self).itemDelegate()
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that this view is presenting.
		"""
		res = super(QListView,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Reset the internal state of the view.
		"""
		res = super(QListView,self).reset()
		return res
	#----------------------------------------------------------------------
	def rootIndex(self):
		"""
		Returns the model index of the models root item
		The root item is the parent item to the views toplevel items
		The root can be invalid.
		"""
		res = super(QListView,self).rootIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def scheduleDelayedItemsLayout(self):
		"""
		Schedules a layout of the items in the view to be executed when the event processing starts.
		Even if PySide.QtGui.QAbstractItemView.scheduleDelayedItemsLayout() is called multiple times before events are processed, the view will only do the layout once.
		"""
		res = super(QListView,self).scheduleDelayedItemsLayout()
		return res
	#----------------------------------------------------------------------
	def selectAll(self):
		"""
		Selects all items in the view
		This function will use the selection behavior set on the view when selecting.
		"""
		res = super(QListView,self).selectAll()
		return res
	#----------------------------------------------------------------------
	def selectedIndexes(self):
		"""
		This convenience function returns a list of all selected and non-hidden item indexes in the view
		The list contains no duplicates, and is not sorted.
		"""
		res = super(QListView,self).selectedIndexes()
		return res
	#----------------------------------------------------------------------
	def selectionBehavior(self):
		"""
		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QListView,self).selectionBehavior()
		isinstance(res,QtGui.QAbstractItemView.SelectionBehavior)
		return res
	#----------------------------------------------------------------------
	def selectionMode(self):
		"""
		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QListView,self).selectionMode()
		isinstance(res,QtGui.QAbstractItemView.SelectionMode)
		return res
	#----------------------------------------------------------------------
	def selectionModel(self):
		"""
		Returns the current selection model.
		"""
		res = super(QListView,self).selectionModel()
		isinstance(res,QtGui.QItemSelectionModel)
		return res
	#----------------------------------------------------------------------
	def showDropIndicator(self):
		"""
		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QListView,self).showDropIndicator()

		return res
	#----------------------------------------------------------------------
	def startAutoScroll(self):
		"""

		"""
		res = super(QListView,self).startAutoScroll()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the item views state.
		"""
		res = super(QListView,self).state()
		isinstance(res,QtGui.QAbstractItemView.State)
		return res
	#----------------------------------------------------------------------
	def stopAutoScroll(self):
		"""

		"""
		res = super(QListView,self).stopAutoScroll()
		return res
	#----------------------------------------------------------------------
	def tabKeyNavigation(self):
		"""
		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QListView,self).tabKeyNavigation()

		return res
	#----------------------------------------------------------------------
	def textElideMode(self):
		"""
		This property holds the position of the ..
		in elided text..
		The default value for all item views is Qt.ElideRight .
		"""
		res = super(QListView,self).textElideMode()
		isinstance(res,QtCore.Qt.TextElideMode)
		return res
	#----------------------------------------------------------------------
	def updateEditorData(self):
		"""
		Updates the data shown in the open editor widgets in the view.
		"""
		res = super(QListView,self).updateEditorData()
		return res
	#----------------------------------------------------------------------
	def updateEditorGeometries(self):
		"""
		Updates the geometry of the open editor widgets in the view.
		"""
		res = super(QListView,self).updateEditorGeometries()
		return res
	#----------------------------------------------------------------------
	def updateGeometries(self):
		"""
		Updates the geometry of the child widgets of the view.
		"""
		res = super(QListView,self).updateGeometries()
		return res
	#----------------------------------------------------------------------
	def verticalOffset(self):
		"""
		Returns the vertical offset of the view.
		In the base class this is a pure virtual function.
		"""
		res = super(QListView,self).verticalOffset()

		return res
	#----------------------------------------------------------------------
	def verticalScrollMode(self):
		"""
		This property holds how the view scrolls its contents in the vertical direction.
		This property controls how the view scroll its contents vertically
		Scrolling can be done either per pixel or per item.
		"""
		res = super(QListView,self).verticalScrollMode()
		isinstance(res,QtGui.QAbstractItemView.ScrollMode)
		return res
	#----------------------------------------------------------------------
	def viewOptions(self):
		"""
		Returns a PySide.QtGui.QStyleOptionViewItem structure populated with the views palette, font, state, alignments etc.
		"""
		res = super(QListView,self).viewOptions()
		isinstance(res,QtGui.QStyleOptionViewItem)
		return res
	#----------------------------------------------------------------------
	def viewportEntered(self):
		"""

		"""
		res = super(QListView,self).viewportEntered()
		return res
	#----------------------------------------------------------------------
	def closeEditor(self,editor,hint):
		"""
		closeEditor(editor,hint)
			editor=QtGui.QWidget
			hint=QtGui.QAbstractItemDelegate.EndEditHint


		"""
		res = super(QListView,self).closeEditor(editor,hint)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,index):
		"""
		closePersistentEditor(index)
			index=QtCore.QModelIndex

		Closes the persistent editor for the item at the given index .
		"""
		res = super(QListView,self).closePersistentEditor(index)
		return res
	#----------------------------------------------------------------------
	def commitData(self,editor):
		"""
		commitData(editor)
			editor=QtGui.QWidget

		Commit the data in the editor to the model.
		"""
		res = super(QListView,self).commitData(editor)
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
		res = super(QListView,self).currentChanged(current,previous)
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
		res = super(QListView,self).dataChanged(topLeft,bottomRight)
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
		res = super(QListView,self).edit(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def editorDestroyed(self,editor):
		"""
		editorDestroyed(editor)
			editor=QtCore.QObject

		This function is called when the given editor has been destroyed.
		"""
		res = super(QListView,self).editorDestroyed(editor)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarAction(self,action):
		"""
		horizontalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QListView,self).horizontalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollbarValueChanged(self,value):
		"""
		horizontalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QListView,self).horizontalScrollbarValueChanged(value)
		return res
	#----------------------------------------------------------------------
	def indexAt(self,point):
		"""
		indexAt(point)
			point=QtCore.QPoint

		Returns the model index of the item at the viewport coordinates point .
		In the base class this is a pure virtual function.
		"""
		res = super(QListView,self).indexAt(point)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexWidget(self,index):
		"""
		indexWidget(index)
			index=QtCore.QModelIndex

		Returns the widget for the item at the given index .
		"""
		res = super(QListView,self).indexWidget(index)
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
		res = super(QListView,self).isIndexHidden(index)

		return res
	#----------------------------------------------------------------------
	def itemDelegate(self,index):
		"""
		itemDelegate(index)
			index=QtCore.QModelIndex

		Returns the item delegate used by this view and model for the given index .
		"""
		res = super(QListView,self).itemDelegate(index)
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
		res = super(QListView,self).itemDelegateForColumn(column)
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
		res = super(QListView,self).itemDelegateForRow(row)
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
		res = super(QListView,self).keyboardSearch(search)
		return res
	#----------------------------------------------------------------------
	def moveCursor(self,cursorAction,modifiers):
		"""
		moveCursor(cursorAction,modifiers)
			cursorAction=QtGui.QAbstractItemView.CursorAction
			modifiers=QtCore.Qt.KeyboardModifiers


		"""
		res = super(QListView,self).moveCursor(cursorAction,modifiers)
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
		res = super(QListView,self).openPersistentEditor(index)
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
		res = super(QListView,self).rowsAboutToBeRemoved(parent,start,end)
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
		res = super(QListView,self).rowsInserted(parent,start,end)
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
		res = super(QListView,self).scrollDirtyRegion(dx,dy)
		return res
	#----------------------------------------------------------------------
	def scrollTo(self,index,hint=QtGui.QAbstractItemView.EnsureVisible):
		"""
		scrollTo(index,hint=None)
			index=QtCore.QModelIndex
			hint=QtGui.QAbstractItemView.ScrollHint

		Scrolls the view if necessary to ensure that the item at index is visible
		The view will try to position the item according to the given hint .
		In the base class this is a pure virtual function.
		"""
		res = super(QListView,self).scrollTo(index,hint)
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
		res = super(QListView,self).selectionChanged(selected,deselected)
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
		res = super(QListView,self).selectionCommand(index,event)
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
		res = super(QListView,self).setAlternatingRowColors(enable)
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
		res = super(QListView,self).setAutoScroll(enable)
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
		res = super(QListView,self).setAutoScrollMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setDefaultDropAction(self,dropAction):
		"""
		setDefaultDropAction(dropAction)
			dropAction=QtCore.Qt.DropAction

		This property holds the drop action that will be used by default in QAbstractItemView::drag().
		If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.
		"""
		res = super(QListView,self).setDefaultDropAction(dropAction)
		return res
	#----------------------------------------------------------------------
	def setDirtyRegion(self,region):
		"""
		setDirtyRegion(region)
			region=QtGui.QRegion

		Marks the given region as dirty and schedules it to be updated
		You only need to call this function if you are implementing your own view subclass.
		"""
		res = super(QListView,self).setDirtyRegion(region)
		return res
	#----------------------------------------------------------------------
	def setDragDropMode(self,behavior):
		"""
		setDragDropMode(behavior)
			behavior=QtGui.QAbstractItemView.DragDropMode

		This property holds the drag and drop event the view will act upon.
		"""
		res = super(QListView,self).setDragDropMode(behavior)
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
		res = super(QListView,self).setDragDropOverwriteMode(overwrite)
		return res
	#----------------------------------------------------------------------
	def setDragEnabled(self,enable):
		"""
		setDragEnabled(enable)
			enable=QtCore.bool

		This property holds whether the view supports dragging of its own items.
		"""
		res = super(QListView,self).setDragEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setDropIndicatorShown(self,enable):
		"""
		setDropIndicatorShown(enable)
			enable=QtCore.bool

		This property holds whether the drop indicator is shown when dragging items and dropping..
		"""
		res = super(QListView,self).setDropIndicatorShown(enable)
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
		res = super(QListView,self).setEditTriggers(triggers)
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
		res = super(QListView,self).setHorizontalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QtCore.QSize

		This property holds the size of items icons.
		Setting this property when the view is visible will cause the items to be laid out again.
		"""
		res = super(QListView,self).setIconSize(size)
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
		res = super(QListView,self).setIndexWidget(index,widget)
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
		res = super(QListView,self).setItemDelegate(delegate)
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
		res = super(QListView,self).setItemDelegateForColumn(column,delegate)
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
		res = super(QListView,self).setItemDelegateForRow(row,delegate)
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
		res = super(QListView,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setRootIndex(self,index):
		"""
		setRootIndex(index)
			index=QtCore.QModelIndex

		Sets the root item to the item at the given index .
		"""
		#if isinstance(self.Model,QtGui.QSortFilterProxyModel):
			#index = self.model().mapFromSource(index)
		res = super(QListView,self).setRootIndex(index)
		return res
	#----------------------------------------------------------------------
	def setSelection(self,rect,command):
		"""
		setSelection(rect,command)
			rect=QtCore.QRect
			command=QtGui.QItemSelectionModel.SelectionFlags


		"""
		res = super(QListView,self).setSelection(rect,command)
		return res
	#----------------------------------------------------------------------
	def setSelectionBehavior(self,behavior):
		"""
		setSelectionBehavior(behavior)
			behavior=QtGui.QAbstractItemView.SelectionBehavior

		This property holds which selection behavior the view uses.
		This property holds whether selections are done in terms of single items, rows or columns.
		"""
		res = super(QListView,self).setSelectionBehavior(behavior)
		return res
	#----------------------------------------------------------------------
	def setSelectionMode(self,mode):
		"""
		setSelectionMode(mode)
			mode=QtGui.QAbstractItemView.SelectionMode

		This property holds which selection mode the view operates in.
		This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.
		"""
		res = super(QListView,self).setSelectionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setSelectionModel(self,selectionModel):
		"""
		setSelectionModel(selectionModel)
			selectionModel=QtGui.QItemSelectionModel

		Sets the current selection model to the given selectionModel .
		Note that, if you call PySide.QtGui.QAbstractItemView.setModel() after this function, the given selectionModel will be replaced by one created by the view.
		"""
		res = super(QListView,self).setSelectionModel(selectionModel)
		return res
	#----------------------------------------------------------------------
	def setState(self,state):
		"""
		setState(state)
			state=QtGui.QAbstractItemView.State

		Sets the item views state to the given state .
		"""
		res = super(QListView,self).setState(state)
		return res
	#----------------------------------------------------------------------
	def setTabKeyNavigation(self,enable):
		"""
		setTabKeyNavigation(enable)
			enable=QtCore.bool

		This property holds whether item navigation with tab and backtab is enabled..
		"""
		res = super(QListView,self).setTabKeyNavigation(enable)
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
		res = super(QListView,self).setTextElideMode(mode)
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
		res = super(QListView,self).setVerticalScrollMode(mode)
		return res
	#----------------------------------------------------------------------
	def sizeHintForColumn(self,column):
		"""
		sizeHintForColumn(column)
			column=QtCore.int

		Returns the width size hint for the specified column or -1 if there is no model.
		This function is used in views with a horizontal header to find the size hint for a header section based on the contents of the given column .
		"""
		res = super(QListView,self).sizeHintForColumn(column)

		return res
	#----------------------------------------------------------------------
	def sizeHintForIndex(self,index):
		"""
		sizeHintForIndex(index)
			index=QtCore.QModelIndex

		Returns the size hint for the item with the specified index or an invalid size for invalid indexes.
		"""
		res = super(QListView,self).sizeHintForIndex(index)
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
		res = super(QListView,self).sizeHintForRow(row)

		return res
	#----------------------------------------------------------------------
	def startDrag(self,supportedActions):
		"""
		startDrag(supportedActions)
			supportedActions=QtCore.Qt.DropActions


		"""
		res = super(QListView,self).startDrag(supportedActions)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarAction(self,action):
		"""
		verticalScrollbarAction(action)
			action=QtCore.int


		"""
		res = super(QListView,self).verticalScrollbarAction(action)
		return res
	#----------------------------------------------------------------------
	def verticalScrollbarValueChanged(self,value):
		"""
		verticalScrollbarValueChanged(value)
			value=QtCore.int


		"""
		res = super(QListView,self).verticalScrollbarValueChanged(value)
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
		res = super(QListView,self).visualRect(index)
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
		res = super(QListView,self).visualRegionForSelection(selection)
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

	BatchSize              = property(batchSize)
	ClearPropertyFlags     = property(clearPropertyFlags)
	ContentsSize           = property(contentsSize)
	Flow                   = property(flow)
	GridSize               = property(gridSize)
	IsSelectionRectVisible = property(isSelectionRectVisible)
	IsWrapping             = property(isWrapping)
	LayoutMode             = property(layoutMode)
	ModelColumn            = property(modelColumn)
	Movement               = property(movement)
	ResizeMode             = property(resizeMode)
	Spacing                = property(spacing)
	UniformItemSizes       = property(uniformItemSizes)
	ViewMode               = property(viewMode)
	WordWrap               = property(wordWrap)


