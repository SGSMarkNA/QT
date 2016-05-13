from PySide import QtGui, QtCore

class QTreeWidget(QtGui.QTreeWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTreeWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		This property holds the number of columns displayed in the tree widget.
		By default, this property has a value of 1.
		"""
		res = super(QTreeWidget,self).columnCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentColumn(self):
		"""
		Returns the current column in the tree widget.
		"""
		res = super(QTreeWidget,self).currentColumn()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item in the tree widget.
		"""
		res = super(QTreeWidget,self).currentItem()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def headerItem(self):
		"""
		Returns the item used for the tree widgets header.
		"""
		res = super(QTreeWidget,self).headerItem()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def invisibleRootItem(self):
		"""
		Returns the tree widgets invisible root item.
		The invisible root item provides access to the tree widgets top-level items through the PySide.QtGui.QTreeWidgetItem API, making it possible to write functions that can treat top-level items and their children in a uniform way; for example, recursive functions.
		"""
		res = super(QTreeWidget,self).invisibleRootItem()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemSelectionChanged(self):
		"""

		"""
		res = super(QTreeWidget,self).itemSelectionChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of treewidget items.
		"""
		res = super(QTreeWidget,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all selected non-hidden items.
		"""
		res = super(QTreeWidget,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def sortColumn(self):
		"""
		Returns the column used to sort the contents of the widget.
		"""
		res = super(QTreeWidget,self).sortColumn()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this view.
		"""
		res = super(QTreeWidget,self).supportedDropActions()
		isinstance(res,QtCore.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def topLevelItemCount(self):
		"""
		This property holds the number of top-level items.
		By default, this property has a value of 0.
		"""
		res = super(QTreeWidget,self).topLevelItemCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def addTopLevelItem(self,item):
		"""
		addTopLevelItem(item)
			item=QtGui.QTreeWidgetItem

		Appends the item as a top-level item in the widget.
		"""
		res = super(QTreeWidget,self).addTopLevelItem(item)
		return res
	#----------------------------------------------------------------------
	def addTopLevelItems(self,items):
		"""
		addTopLevelItems(items)
			items=unKnown


		"""
		res = super(QTreeWidget,self).addTopLevelItems(items)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,item,column=None):
		"""
		closePersistentEditor(item,column=None)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Closes the persistent editor for the item in the given column .
		This function has no effect if no persistent editor is open for this combination of item and column.
		"""
		res = super(QTreeWidget,self).closePersistentEditor(item,column)
		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,parent,index,data,action):
		"""
		dropMimeData(parent,index,data,action)
			parent=QtGui.QTreeWidgetItem
			index=QtCore.int
			data=QtCore.QMimeData
			action=QtCore.Qt.DropAction


		"""
		res = super(QTreeWidget,self).dropMimeData(parent,index,data,action)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def editItem(self,item,column=None):
		"""
		editItem(item,column=None)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Starts editing the item in the given column if it is editable.
		"""
		res = super(QTreeWidget,self).editItem(item,column)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags,column=None):
		"""
		findItems(text,flags,column=None)
			text=unicode
			flags=QtCore.Qt.MatchFlags
			column=QtCore.int


		"""
		res = super(QTreeWidget,self).findItems(text,flags,column)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item,column=None):
		"""
		indexFromItem(item,column=None)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Returns the PySide.QtCore.QModelIndex assocated with the given item in the given column .
		"""
		res = super(QTreeWidget,self).indexFromItem(item,column)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def indexOfTopLevelItem(self,item):
		"""
		indexOfTopLevelItem(item)
			item=QtGui.QTreeWidgetItem

		Returns the index of the given top-level item , or -1 if the item cannot be found.
		"""
		res = super(QTreeWidget,self).indexOfTopLevelItem(item)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def insertTopLevelItem(self,index,item):
		"""
		insertTopLevelItem(index,item)
			index=QtCore.int
			item=QtGui.QTreeWidgetItem

		Inserts the item at index in the top level in the view.
		If the item has already been inserted somewhere else it wont be inserted.
		"""
		res = super(QTreeWidget,self).insertTopLevelItem(index,item)
		return res
	#----------------------------------------------------------------------
	def insertTopLevelItems(self,index,items):
		"""
		insertTopLevelItems(index,items)
			index=QtCore.int
			items=unKnown


		"""
		res = super(QTreeWidget,self).insertTopLevelItems(index,items)
		return res
	#----------------------------------------------------------------------
	def isFirstItemColumnSpanned(self,item):
		"""
		isFirstItemColumnSpanned(item)
			item=QtGui.QTreeWidgetItem

		Returns true if the given item is set to show only one section over all columns; otherwise returns false.
		"""
		res = super(QTreeWidget,self).isFirstItemColumnSpanned(item)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isItemExpanded(self,item):
		"""
		isItemExpanded(item)
			item=QtGui.QTreeWidgetItem

		Returns true if the given item is open; otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isExpanded() instead.
		"""
		res = super(QTreeWidget,self).isItemExpanded(item)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isItemHidden(self,item):
		"""
		isItemHidden(item)
			item=QtGui.QTreeWidgetItem

		Returns true if the item is explicitly hidden, otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isHidden() instead.
		"""
		res = super(QTreeWidget,self).isItemHidden(item)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isItemSelected(self,item):
		"""
		isItemSelected(item)
			item=QtGui.QTreeWidgetItem

		Returns true if the item is selected; otherwise returns false.
		This function is deprecated
		Use QTreeWidgetItem.isSelected() instead.
		"""
		res = super(QTreeWidget,self).isItemSelected(item)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def itemAbove(self,item):
		"""
		itemAbove(item)
			item=QtGui.QTreeWidgetItem

		Returns the item above the given item .
		"""
		res = super(QTreeWidget,self).itemAbove(item)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y)
			x=QtCore.int
			y=QtCore.int

		itemAt(p)
			p=QtCore.QPoint

		This is an overloaded function.
		Returns a pointer to the item at the coordinates (x , y ).
		"""
		res = super(QTreeWidget,self).itemAt(*args,**kwargs)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemBelow(self,item):
		"""
		itemBelow(item)
			item=QtGui.QTreeWidgetItem

		Returns the item visually below the given item .
		"""
		res = super(QTreeWidget,self).itemBelow(item)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=QtCore.QModelIndex

		Returns a pointer to the PySide.QtGui.QTreeWidgetItem assocated with the given index .
		"""
		res = super(QTreeWidget,self).itemFromIndex(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemWidget(self,item,column):
		"""
		itemWidget(item,column)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Returns the widget displayed in the cell specified by item and the given column .
		"""
		res = super(QTreeWidget,self).itemWidget(item,column)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,items):
		"""
		mimeData(items)
			items=unKnown


		"""
		res = super(QTreeWidget,self).mimeData(items)
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,item,column=None):
		"""
		openPersistentEditor(item,column=None)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Opens a persistent editor for the item in the given column .
		"""
		res = super(QTreeWidget,self).openPersistentEditor(item,column)
		return res
	#----------------------------------------------------------------------
	def removeItemWidget(self,item,column):
		"""
		removeItemWidget(item,column)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		Removes the widget set in the given item in the given column .
		"""
		res = super(QTreeWidget,self).removeItemWidget(item,column)
		return res
	#----------------------------------------------------------------------
	def setColumnCount(self,columns):
		"""
		setColumnCount(columns)
			columns=QtCore.int

		This property holds the number of columns displayed in the tree widget.
		By default, this property has a value of 1.
		"""
		res = super(QTreeWidget,self).setColumnCount(columns)
		return res
	#----------------------------------------------------------------------
	def setCurrentItem(self,*args,**kwargs):
		"""
		setCurrentItem(item,column)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int

		setCurrentItem(item,column,command)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int
			command=QtGui.QItemSelectionModel.SelectionFlags

		setCurrentItem(item)
			item=QtGui.QTreeWidgetItem

		Sets the current item in the tree widget and the current column to column .
		"""
		res = super(QTreeWidget,self).setCurrentItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFirstItemColumnSpanned(self,item,span):
		"""
		setFirstItemColumnSpanned(item,span)
			item=QtGui.QTreeWidgetItem
			span=QtCore.bool

		Sets the given item to only show one section for all columns if span is true; otherwise the item will show one section per column.
		"""
		res = super(QTreeWidget,self).setFirstItemColumnSpanned(item,span)
		return res
	#----------------------------------------------------------------------
	def setHeaderItem(self,item):
		"""
		setHeaderItem(item)
			item=QtGui.QTreeWidgetItem

		Sets the header item for the tree widget
		The label for each column in the header is supplied by the corresponding label in the item.
		The tree widget takes ownership of the item.
		"""
		res = super(QTreeWidget,self).setHeaderItem(item)
		return res
	#----------------------------------------------------------------------
	def setHeaderLabel(self,label):
		"""
		setHeaderLabel(label)
			label=unicode

		Same as setHeaderLabels( PySide.QtCore.QStringList (label )).
		"""
		res = super(QTreeWidget,self).setHeaderLabel(label)
		return res
	#----------------------------------------------------------------------
	def setHeaderLabels(self,labels):
		"""
		setHeaderLabels(labels)
			labels=list

		Adds a column in the header for each item in the labels list, and sets the label for each column.
		Note that PySide.QtGui.QTreeWidget.setHeaderLabels() wont remove existing columns.
		"""
		res = super(QTreeWidget,self).setHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def setItemExpanded(self,item,expand):
		"""
		setItemExpanded(item,expand)
			item=QtGui.QTreeWidgetItem
			expand=QtCore.bool

		Sets the item referred to by item to either closed or opened, depending on the value of expand .
		This function is deprecated
		Use QTreeWidgetItem.setExpanded() instead.
		"""
		res = super(QTreeWidget,self).setItemExpanded(item,expand)
		return res
	#----------------------------------------------------------------------
	def setItemHidden(self,item,hide):
		"""
		setItemHidden(item,hide)
			item=QtGui.QTreeWidgetItem
			hide=QtCore.bool

		Hides the given item if hide is true; otherwise shows the item.
		This function is deprecated
		Use QTreeWidgetItem.setHidden() instead.
		"""
		res = super(QTreeWidget,self).setItemHidden(item,hide)
		return res
	#----------------------------------------------------------------------
	def setItemSelected(self,item,select):
		"""
		setItemSelected(item,select)
			item=QtGui.QTreeWidgetItem
			select=QtCore.bool

		If select is true, the given item is selected; otherwise it is deselected.
		This function is deprecated
		Use QTreeWidgetItem.setSelected() instead.
		"""
		res = super(QTreeWidget,self).setItemSelected(item,select)
		return res
	#----------------------------------------------------------------------
	def setItemWidget(self,item,column,widget):
		"""
		setItemWidget(item,column,widget)
			item=QtGui.QTreeWidgetItem
			column=QtCore.int
			widget=QtGui.QWidget

		Sets the given widget to be displayed in the cell specified by the given item and column .
		The given widget s PySide.QtGui.QWidget.autoFillBackground() property must be set to true, otherwise the widgets background will be transparent, showing both the model data and the tree widget item.
		This function should only be used to display static content in the place of a tree widget item
		If you want to display custom dynamic content or implement a custom editor widget, use PySide.QtGui.QTreeView and subclass PySide.QtGui.QItemDelegate instead.
		This function cannot be called before the item hierarchy has been set up, i.e., the PySide.QtGui.QTreeWidgetItem that will hold widget must have been added to the view before widget is set.
		"""
		res = super(QTreeWidget,self).setItemWidget(item,column,widget)
		return res
	#----------------------------------------------------------------------
	def sortItems(self,column,order):
		"""
		sortItems(column,order)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QTreeWidget,self).sortItems(column,order)
		return res
	#----------------------------------------------------------------------
	def takeTopLevelItem(self,index):
		"""
		takeTopLevelItem(index)
			index=QtCore.int

		Removes the top-level item at the given index in the tree and returns it, otherwise returns 0;
		"""
		res = super(QTreeWidget,self).takeTopLevelItem(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def topLevelItem(self,index):
		"""
		topLevelItem(index)
			index=QtCore.int

		Returns the top level item at the given index , or 0 if the item does not exist.
		"""
		res = super(QTreeWidget,self).topLevelItem(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def visualItemRect(self,item):
		"""
		visualItemRect(item)
			item=QtGui.QTreeWidgetItem

		Returns the rectangle on the viewport occupied by the item at item .
		"""
		res = super(QTreeWidget,self).visualItemRect(item)
		isinstance(res,QtCore.QRect)
		return res
