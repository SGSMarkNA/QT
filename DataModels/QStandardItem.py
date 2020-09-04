import QT
import Qt_Roles_And_Enums
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
user_type_counter = QT.user_type_counter
Item_Data_Roles   = Qt_Roles_And_Enums.Standered_Item_Data_Roles

class QStandardItem(QtGui.QStandardItem):
	''''''
	ITEM_TYPE =  user_type_counter()
	ItemFlag        = Qt_Roles_And_Enums.ItemFlag
	AlignmentFlag   = Qt_Roles_And_Enums.AlignmentFlag
	Item_Data_Roles = Qt_Roles_And_Enums.Standered_Item_Data_Roles
	def __init__(self,*args,**kwargs):
		'''
		QStandardItem(icon, text)
		QStandardItem(other)
		QStandardItem(text)
		QStandardItem(rows[, columns=1])
		'''
		try:
			super(QStandardItem,self).__init__(*args,**kwargs)
		except TypeError:
			super(QStandardItem,self).__init__(0,**kwargs)
	#----------------------------------------------------------------------
	def find_child_items(self, value, role=Item_Data_Roles.DISPLAY, recurive=True):
		""""""
		res = []
		for child in self.rowChildren():
			if child.data(role) == value:
				res.append(child)
			if recurive:
				res.extend(child.find_child_items(value, role, recurive))
		return res
	
	#----------------------------------------------------------------------
	def child_item_exists(self, value, role=Item_Data_Roles.DISPLAY, recurive=True):
		""""""
		items = self.find_child_items(value, role=role, recurive=recurive)
		if len(items):
			return True
		else:
			return False
	
	#----------------------------------------------------------------------
	def find_child_item_types(self, itemType, recurive=True):
		""""""
		res = []
		for child in self.rowChildren():
			if child.type() == itemType:
				res.append(child)
			if recurive:
				res.extend(child.find_child_item_types(itemType, recurive))
		return res
		
	#----------------------------------------------------------------------
	def clear_Children(self):
		""""""
		for child in self.Children:
			child.clear_Children()
			self.removeRow(child.row())
	
	#----------------------------------------------------------------------
	def accessibleDescription(self):
		"""
		Returns the items accessible description.
		The accessible description is used by assistive technologies (i.e
		for users who cannot use conventional means of interaction).
		"""
		res = super(QStandardItem,self).accessibleDescription()
		return res
	#----------------------------------------------------------------------
	def accessibleText(self):
		"""
		Returns the items accessible text.
		The accessible text is used by assistive technologies (i.e
		for users who cannot use conventional means of interaction).
		"""
		res = super(QStandardItem,self).accessibleText()
		return res
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the brush used to render the items background.
		"""
		res = super(QStandardItem,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self):
		"""
		Returns the checked state of the item.
		"""
		res = super(QStandardItem,self).checkState()
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Returns a copy of this item
		The items children are not copied.
		When subclassing PySide.QtGui.QStandardItem , you can reimplement this function to provide PySide.QtGui.QStandardItemModel with a factory that it can use to create new items on demand.
		"""
		res = super(QStandardItem,self).clone()
		isinstance(res,QtGui.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the column where the item is located in its parents child table, or -1 if the item has no parent.
		"""
		res = super(QStandardItem,self).column()

		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of child item columns that the item has.
		"""
		res = super(QStandardItem,self).columnCount()

		return res
	#----------------------------------------------------------------------
	def emitDataChanged(self):
		"""
		Causes the model associated with this item to emit a PySide.QtCore.QAbstractItemModel.dataChanged() () signal for this item.
		You normally only need to call this function if you have subclassed PySide.QtGui.QStandardItem and reimplemented PySide.QtGui.QStandardItem.data() and/or PySide.QtGui.QStandardItem.setData() .
		"""
		res = super(QStandardItem,self).emitDataChanged()
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the item flags for the item.
		The item flags determine how the user can interact with the item.
		By default, items are enabled, editable, selectable, checkable, and can be used both as the source of a drag and drop operation and as a drop target.
		"""
		res = super(QStandardItem,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font used to render the items text.
		"""
		res = super(QStandardItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self):
		"""
		Returns the brush used to render the items foreground (e.g
		text).
		"""
		res = super(QStandardItem,self).foreground()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def hasChildren(self):
		"""
		Returns true if this item has any children; otherwise returns false.
		"""
		res = super(QStandardItem,self).hasChildren()

		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		Returns the items icon.
		"""
		res = super(QStandardItem,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isCheckable(self):
		"""
		Returns whether the item is user-checkable.
		The default value is false.
		"""
		res = super(QStandardItem,self).isCheckable()

		return res
	#----------------------------------------------------------------------
	def isDragEnabled(self):
		"""
		Returns whether the item is drag enabled
		An item that is drag enabled can be dragged by the user.
		The default value is true.
		Note that item dragging must be enabled in the view for dragging to work; see QAbstractItemView.dragEnabled .
		"""
		res = super(QStandardItem,self).isDragEnabled()

		return res
	#----------------------------------------------------------------------
	def isDropEnabled(self):
		"""
		Returns whether the item is drop enabled
		When an item is drop enabled, it can be used as a drop target.
		The default value is true.
		"""
		res = super(QStandardItem,self).isDropEnabled()

		return res
	#----------------------------------------------------------------------
	def isEditable(self):
		"""
		Returns whether the item can be edited by the user.
		When an item is editable (and enabled), the user can edit the item by invoking one of the views edit triggers; see QAbstractItemView.editTriggers .
		The default value is true.
		"""
		res = super(QStandardItem,self).isEditable()

		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		Returns whether the item is enabled.
		When an item is enabled, the user can interact with it
		The possible types of interaction are specified by the other item flags, such as PySide.QtGui.QStandardItem.isEditable() and PySide.QtGui.QStandardItem.isSelectable() .
		The default value is true.
		"""
		res = super(QStandardItem,self).isEnabled()

		return res
	#----------------------------------------------------------------------
	def isSelectable(self):
		"""
		Returns whether the item is selectable by the user.
		The default value is true.
		"""
		res = super(QStandardItem,self).isSelectable()

		return res
	#----------------------------------------------------------------------
	def isTristate(self):
		"""
		Returns whether the item is tristate; that is, if its checkable with three separate states.
		The default value is false.
		"""
		res = super(QStandardItem,self).isTristate()

		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the PySide.QtGui.QStandardItemModel that this item belongs to.
		If the item is not a child of another item that belongs to the model, this function returns 0.
		"""
		res = super(QStandardItem,self).model()
		isinstance(res,QtGui.QStandardItemModel)
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the items parent item, or 0 if the item has no parent.
		"""
		res = super(QStandardItem,self).parent()
		isinstance(res,QtGui.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def row(self):
		"""
		Returns the row where the item is located in its parents child table, or -1 if the item has no parent.
		"""
		res = super(QStandardItem,self).row()

		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		Returns the number of child item rows that the item has.
		"""
		res = super(QStandardItem,self).rowCount()

		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		Returns the size hint set for the item, or an invalid PySide.QtCore.QSize if no size hint has been set.
		If no size hint has been set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(QStandardItem,self).sizeHint()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		Returns the items status tip.
		"""
		res = super(QStandardItem,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the items text
		This is the text thats presented to the user in a view.
		"""
		res = super(QStandardItem,self).text()
		return res
	#----------------------------------------------------------------------
	def textAlignment(self):
		"""
		Returns the text alignment for the items text.
		"""
		res = super(QStandardItem,self).textAlignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the items tooltip.
		"""
		res = super(QStandardItem,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of this item
		The type is used to distinguish custom items from the base class
		When subclassing PySide.QtGui.QStandardItem , you should reimplement this function and return a new value greater than or equal to UserType .
		"""
		
		return self.ITEM_TYPE
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		Returns the items Whats This? help.
		"""
		res = super(QStandardItem,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def appendColumn(self,items):
		"""
		appendColumn(items)
			items=unKnown


		"""
		res = super(QStandardItem,self).appendColumn(items)
		return res
	#----------------------------------------------------------------------
	def appendRow(self,item):
		"""
		appendRow(item)
			item=QtGui.QStandardItem

		appendRow(items)
			items=unKnown

		This is an overloaded function.
		Appends a row containing item .
		When building a list or a tree that has only one column, this function provides a convenient way to append a single new item.
		"""
		res = super(QStandardItem,self).appendRow(item)
		return res
	#----------------------------------------------------------------------
	def appendRows(self,items):
		"""
		appendRows(items)
			items=unKnown


		"""
		res = super(QStandardItem,self).appendRows(items)
		return res
	#----------------------------------------------------------------------
	def child(self,row,column=0):
		"""
		child(row,column=None)
			row=QtCore.int
			column=QtCore.int

		Returns the child item at (row , column ) if one has been set; otherwise returns 0.
		"""
		res = super(QStandardItem,self).child(row,column)
		isinstance(res,QtGui.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def data(self,role=Item_Data_Roles.DISPLAY):
		"""
		data(role=None)
			role=QtCore.int

		Returns the items data for the given role , or an invalid PySide.QtCore.QVariant if there is no data for the role.
		"""
		# if role > Qt.UserRole:
			# print self.__class__.__name__
		res = super(QStandardItem,self).data(role)
		return res
	#----------------------------------------------------------------------
	def insertColumn(self,column,items):
		"""
		insertColumn(column,items)
			column=QtCore.int
			items=unKnown


		"""
		res = super(QStandardItem,self).insertColumn(column,items)
		return res
	#----------------------------------------------------------------------
	def insertColumns(self,column,count):
		"""
		insertColumns(column,count)
			column=QtCore.int
			count=QtCore.int

		Inserts count columns of child items at column column .
		"""
		res = super(QStandardItem,self).insertColumns(column,count)
		return res
	#----------------------------------------------------------------------
	def insertRow(self,row,items):
		"""
		insertRow(row,items)
			row=QtCore.int
			items=unKnown

		insertRow(row,item)
			row=QtCore.int
			item=QtGui.QStandardItem


		"""
		if not isinstance(items, list):
			items = [items]
		res = super(QStandardItem,self).insertRow(row,items)
		return res
	#----------------------------------------------------------------------
	def insertRows(self,row,items):
		"""
		insertRows(row,items)
			row=QtCore.int
			items=unKnown

		insertRows(row,count)
			row=QtCore.int
			count=QtCore.int


		"""
		res = super(QStandardItem,self).insertRows(row,items)
		return res
	#----------------------------------------------------------------------
	def read(self,stream):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in
		Only the data and flags of the item are read, not the child items.
		"""
		res = super(QStandardItem,self).read(stream)
		return res
	#----------------------------------------------------------------------
	def removeColumn(self,column):
		"""
		removeColumn(column)
			column=QtCore.int

		Removes the given column
		The items that were in the column are deleted.
		"""
		res = super(QStandardItem,self).removeColumn(column)
		return res
	#----------------------------------------------------------------------
	def removeColumns(self,column,count):
		"""
		removeColumns(column,count)
			column=QtCore.int
			count=QtCore.int

		Removes count columns at column column
		The items that were in those columns are deleted.
		"""
		res = super(QStandardItem,self).removeColumns(column,count)
		return res
	#----------------------------------------------------------------------
	def removeRow(self,row):
		"""
		removeRow(row)
			row=QtCore.int

		Removes the given row
		The items that were in the row are deleted.
		"""
		res = self.takeChild(row)
		super(QStandardItem,self).removeRow(row)
		return res
	#----------------------------------------------------------------------
	def removeRows(self,row,count):
		"""
		removeRows(row,count)
			row=QtCore.int
			count=QtCore.int

		Removes count rows at row row
		The items that were in those rows are deleted.
		"""
		res = super(QStandardItem,self).removeRows(row,count)
		return res
	#----------------------------------------------------------------------
	def setAccessibleDescription(self,accessibleDescription):
		"""
		setAccessibleDescription(accessibleDescription)
			accessibleDescription=unicode

		Sets the items accessible description to the string specified by accessibleDescription .
		The accessible description is used by assistive technologies (i.e
		for users who cannot use conventional means of interaction).
		"""
		res = super(QStandardItem,self).setAccessibleDescription(accessibleDescription)
		return res
	#----------------------------------------------------------------------
	def setAccessibleText(self,accessibleText):
		"""
		setAccessibleText(accessibleText)
			accessibleText=unicode

		Sets the items accessible text to the string specified by accessibleText .
		The accessible text is used by assistive technologies (i.e
		for users who cannot use conventional means of interaction).
		"""
		res = super(QStandardItem,self).setAccessibleText(accessibleText)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,brush):
		"""
		setBackground(brush)
			brush=QtGui.QBrush

		Sets the items background brush to the specified brush .
		"""
		res = super(QStandardItem,self).setBackground(brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,checkState):
		"""
		setCheckState(checkState)
			checkState=QtCore.Qt.CheckState


		"""
		res = super(QStandardItem,self).setCheckState(checkState)
		return res
	#----------------------------------------------------------------------
	def setCheckable(self,checkable):
		"""
		setCheckable(checkable)
			checkable=QtCore.bool

		Sets whether the item is user-checkable
		If checkable is true, the item can be checked by the user; otherwise, the user cannot check the item.
		The item delegate will render a checkable item with a check box next to the items text.
		"""
		res = super(QStandardItem,self).setCheckable(checkable)
		return res
	#----------------------------------------------------------------------
	def setChild(self,row,item,column=0):
		"""
		setChild(row,column,item)
			row=QtCore.int
			column=QtCore.int
			item=QtGui.QStandardItem

		setChild(row,item)
			row=QtCore.int
			item=QtGui.QStandardItem

		Sets the child item at (row , column ) to item
		This item (the parent item) takes ownership of item
		If necessary, the row count and column count are increased to fit the item.
		"""
		if isinstance(item, int):
			if not isinstance(column, int):
				item, column = column, item
		res = super(QStandardItem,self).setChild(row,column,item)
		return res
	#----------------------------------------------------------------------
	def setColumnCount(self,columns):
		"""
		setColumnCount(columns)
			columns=QtCore.int

		Sets the number of child item columns to columns
		If this is less than PySide.QtGui.QStandardItem.columnCount() , the data in the unwanted columns is discarded.
		"""
		res = super(QStandardItem,self).setColumnCount(columns)
		return res
	#----------------------------------------------------------------------
	def setData(self,value,role=Item_Data_Roles.DISPLAY):
		"""
		setData(value,role=None)
			value=object
			role=QtCore.int

		Sets the items data for the given role to the specified value .
		If you subclass PySide.QtGui.QStandardItem and reimplement this function, your reimplementation should call PySide.QtGui.QStandardItem.emitDataChanged() if you do not call the base implementation of PySide.QtGui.QStandardItem.setData()
		This will ensure that e.g
		views using the model are notified of the changes.
		"""
		res = super(QStandardItem,self).setData(value,role)
		return res
	#----------------------------------------------------------------------
	def setDragEnabled(self,dragEnabled):
		"""
		setDragEnabled(dragEnabled)
			dragEnabled=QtCore.bool

		Sets whether the item is drag enabled
		If dragEnabled is true, the item can be dragged by the user; otherwise, the user cannot drag the item.
		Note that you also need to ensure that item dragging is enabled in the view; see QAbstractItemView.dragEnabled .
		"""
		res = super(QStandardItem,self).setDragEnabled(dragEnabled)
		return res
	#----------------------------------------------------------------------
	def setDropEnabled(self,dropEnabled):
		"""
		setDropEnabled(dropEnabled)
			dropEnabled=QtCore.bool

		Sets whether the item is drop enabled
		If dropEnabled is true, the item can be used as a drop target; otherwise, it cannot.
		Note that you also need to ensure that drops are enabled in the view; see QWidget.acceptDrops() ; and that the model supports the desired drop actions; see QAbstractItemModel.supportedDropActions() .
		"""
		res = super(QStandardItem,self).setDropEnabled(dropEnabled)
		return res
	#----------------------------------------------------------------------
	def setEditable(self,editable):
		"""
		setEditable(editable)
			editable=QtCore.bool

		Sets whether the item is editable
		If editable is true, the item can be edited by the user; otherwise, the user cannot edit the item.
		How the user can edit items in a view is determined by the views edit triggers; see QAbstractItemView.editTriggers .
		"""
		res = super(QStandardItem,self).setEditable(editable)
		return res
	#----------------------------------------------------------------------
	def setEnabled(self,enabled):
		"""
		setEnabled(enabled)
			enabled=QtCore.bool

		Sets whether the item is enabled
		If enabled is true, the item is enabled, meaning that the user can interact with the item; if enabled is false, the user cannot interact with the item.
		This flag takes precedence over the other item flags; e.g
		if an item is not enabled, it cannot be selected by the user, even if the Qt.ItemIsSelectable flag has been set.
		"""
		res = super(QStandardItem,self).setEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.Qt.ItemFlags


		"""
		res = super(QStandardItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font used to display the items text to the given font .
		"""
		res = super(QStandardItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,brush):
		"""
		setForeground(brush)
			brush=QtGui.QBrush

		Sets the brush used to display the items foreground (e.g
		text) to the given brush .
		"""
		res = super(QStandardItem,self).setForeground(brush)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		Sets the items icon to the icon specified.
		"""
		res = super(QStandardItem,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setRowCount(self,rows):
		"""
		setRowCount(rows)
			rows=QtCore.int

		Sets the number of child item rows to rows
		If this is less than PySide.QtGui.QStandardItem.rowCount() , the data in the unwanted rows is discarded.
		"""
		res = super(QStandardItem,self).setRowCount(rows)
		return res
	#----------------------------------------------------------------------
	def setSelectable(self,selectable):
		"""
		setSelectable(selectable)
			selectable=QtCore.bool

		Sets whether the item is selectable
		If selectable is true, the item can be selected by the user; otherwise, the user cannot select the item.
		You can control the selection behavior and mode by manipulating their view properties; see QAbstractItemView.selectionMode and QAbstractItemView.selectionBehavior .
		"""
		res = super(QStandardItem,self).setSelectable(selectable)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,sizeHint):
		"""
		setSizeHint(sizeHint)
			sizeHint=QtCore.QSize

		Sets the size hint for the item to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(QStandardItem,self).setSizeHint(sizeHint)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,statusTip):
		"""
		setStatusTip(statusTip)
			statusTip=unicode

		Sets the items status tip to the string specified by statusTip .
		"""
		res = super(QStandardItem,self).setStatusTip(statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the items text to the text specified.
		"""
		res = super(QStandardItem,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,textAlignment):
		"""
		setTextAlignment(textAlignment)
			textAlignment=QtCore.Qt.Alignment


		"""
		res = super(QStandardItem,self).setTextAlignment(textAlignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,toolTip):
		"""
		setToolTip(toolTip)
			toolTip=unicode

		Sets the items tooltip to the string specified by toolTip .
		"""
		res = super(QStandardItem,self).setToolTip(toolTip)
		return res
	#----------------------------------------------------------------------
	def setTristate(self,tristate):
		"""
		setTristate(tristate)
			tristate=QtCore.bool

		Sets whether the item is tristate
		If tristate is true, the item is checkable with three separate states; otherwise, the item is checkable with two states
		(Note that this also requires that the item is checkable; see PySide.QtGui.QStandardItem.isCheckable() .)
		"""
		res = super(QStandardItem,self).setTristate(tristate)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,whatsThis):
		"""
		setWhatsThis(whatsThis)
			whatsThis=unicode

		Sets the items Whats This? help to the string specified by whatsThis .
		"""
		res = super(QStandardItem,self).setWhatsThis(whatsThis)
		return res
	#----------------------------------------------------------------------
	def sortChildren(self,column=0,order=QtCore.Qt.AscendingOrder):
		"""
		sortChildren(column,order=None)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QStandardItem,self).sortChildren(column,order)
		return res
	#----------------------------------------------------------------------
	def takeChild(self,row,column=0):
		"""
		takeChild(row,column=None)
			row=QtCore.int
			column=QtCore.int

		Removes the child item at (row , column ) without deleting it, and returns a pointer to the item
		If there was no child at the given location, then this function returns 0.
		Note that this function, unlike PySide.QtGui.QStandardItem.takeRow() and PySide.QtGui.QStandardItem.takeColumn() , does not affect the dimensions of the child table.
		"""
		res = super(QStandardItem,self).takeChild(row,column)
		isinstance(res,QtGui.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def extractChild(self, row):
		""""""
		res = self.takeChild(row, 0)
		self.removeRow(row)
		isinstance(res,QtGui.QStandardItem)
		return res
	#----------------------------------------------------------------------
	def setParent(self, newParent):
		""""""
		row       =  self.row()
		oldParent =  self.parent()
		item      =  oldParent.takeChild(row, 0)
		oldParent.removeRow(row)
		newParent.appendRow(item)
		
	#----------------------------------------------------------------------
	def takeColumn(self,column):
		"""
		takeColumn(column)
			column=QtCore.int

		Removes column without deleting the column items, and returns a list of pointers to the removed items
		For items in the column that have not been set, the corresponding pointers in the list will be 0.
		"""
		res = super(QStandardItem,self).takeColumn(column)
		return res
	#----------------------------------------------------------------------
	def takeRow(self,row):
		"""
		takeRow(row)
			row=QtCore.int

		Removes row without deleting the row items, and returns a list of pointers to the removed items
		For items in the row that have not been set, the corresponding pointers in the list will be 0.
		"""
		res = super(QStandardItem,self).takeRow(row)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out
		Only the data and flags of the item are written, not the child items.
		"""
		res = super(QStandardItem,self).write(out)
		return res
	@property
	def Index(self):
		return self.index()
	#----------------------------------------------------------------------
	def rowChildren(self):
		return [self.child(i) for i in range(self.rowCount())]
	Children              = property(rowChildren)
	AccessibleDescription = property(accessibleDescription,setAccessibleDescription)
	AccessibleText        = property(accessibleText,setAccessibleText)
	CheckState            = property(checkState,setCheckState)
	Clone                 = property(clone)
	Column                = property(column)
	ColumnCount           = property(columnCount)
	Row                   = property(row)
	RowCount              = property(rowCount, setRowCount)
	EmitDataChanged       = property(emitDataChanged)
	Flags                 = property(flags,setFlags)
	Font                  = property(font,setFont)
	Icon                  = property(icon,setIcon)
	Text                  = property(text,setText)
	ToolTip               = property(toolTip,setToolTip)
	SizeHint              = property(sizeHint,setSizeHint)
	StatusTip             = property(statusTip,setStatusTip)
	TextAlignment         = property(textAlignment,setTextAlignment)
	Background            = property(background,setBackground)
	Foreground            = property(foreground,setForeground)
	HasChildren           = property(hasChildren)
	#Index                 = property(index)
	IsCheckable           = property(isCheckable,setCheckable)
	IsDragEnabled         = property(isDragEnabled,setDragEnabled)
	IsDropEnabled         = property(isDropEnabled,setDropEnabled)
	IsEditable            = property(isEditable,setEditable)
	IsEnabled             = property(isEnabled,setEnabled)
	IsSelectable          = property(isSelectable,setSelectable)
	IsTristate            = property(isTristate,setTristate)
	Model                 = property(model)
	Parent                = property(parent)
	Type                  = property(type)
	WhatsThis             = property(whatsThis)
