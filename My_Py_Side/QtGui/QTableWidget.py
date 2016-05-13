from PySide import QtGui, QtCore

class QTableWidget(QtGui.QTableWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTableWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		This property holds the number of columns in the table.
		By default, for a table constructed without row and column counts, this property contains a value of 0.
		"""
		res = super(QTableWidget,self).columnCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentColumn(self):
		"""
		Returns the column of the current item.
		"""
		res = super(QTableWidget,self).currentColumn()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item.
		"""
		res = super(QTableWidget,self).currentItem()
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def currentRow(self):
		"""
		Returns the row of the current item.
		"""
		res = super(QTableWidget,self).currentRow()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def itemPrototype(self):
		"""
		Returns the item prototype used by the table.
		"""
		res = super(QTableWidget,self).itemPrototype()
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemSelectionChanged(self):
		"""

		"""
		res = super(QTableWidget,self).itemSelectionChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of tablewidget items.
		"""
		res = super(QTableWidget,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		This property holds the number of rows in the table.
		By default, for a table constructed without row and column counts, this property contains a value of 0.
		"""
		res = super(QTableWidget,self).rowCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all selected items.
		This function returns a list of pointers to the contents of the selected cells
		Use the PySide.QtGui.QTableView.selectedIndexes() function to retrieve the complete selection including empty cells.
		"""
		res = super(QTableWidget,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def selectedRanges(self):
		"""
		Returns a list of all selected ranges.
		"""
		res = super(QTableWidget,self).selectedRanges()
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this view.
		"""
		res = super(QTableWidget,self).supportedDropActions()
		isinstance(res,QtCore.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def cellWidget(self,row,column):
		"""
		cellWidget(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the widget displayed in the cell in the given row and column .
		"""
		res = super(QTableWidget,self).cellWidget(row,column)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,item):
		"""
		closePersistentEditor(item)
			item=QtGui.QTableWidgetItem

		Closes the persistent editor for item .
		"""
		res = super(QTableWidget,self).closePersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def column(self,item):
		"""
		column(item)
			item=QtGui.QTableWidgetItem

		Returns the column for the item .
		"""
		res = super(QTableWidget,self).column(item)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,row,column,data,action):
		"""
		dropMimeData(row,column,data,action)
			row=QtCore.int
			column=QtCore.int
			data=QtCore.QMimeData
			action=QtCore.Qt.DropAction


		"""
		res = super(QTableWidget,self).dropMimeData(row,column,data,action)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def editItem(self,item):
		"""
		editItem(item)
			item=QtGui.QTableWidgetItem

		Starts editing the item if it is editable.
		"""
		res = super(QTableWidget,self).editItem(item)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags):
		"""
		findItems(text,flags)
			text=unicode
			flags=QtCore.Qt.MatchFlags


		"""
		res = super(QTableWidget,self).findItems(text,flags)
		return res
	#----------------------------------------------------------------------
	def horizontalHeaderItem(self,column):
		"""
		horizontalHeaderItem(column)
			column=QtCore.int

		Returns the horizontal header item for column, column , if one has been set; otherwise returns 0.
		"""
		res = super(QTableWidget,self).horizontalHeaderItem(column)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item):
		"""
		indexFromItem(item)
			item=QtGui.QTableWidgetItem

		Returns the PySide.QtCore.QModelIndex assocated with the given item .
		"""
		res = super(QTableWidget,self).indexFromItem(item)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def item(self,row,column):
		"""
		item(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the item for the given row and column if one has been set; otherwise returns 0.
		"""
		res = super(QTableWidget,self).item(row,column)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y)
			x=QtCore.int
			y=QtCore.int

		itemAt(p)
			p=QtCore.QPoint

		Returns the item at the position equivalent to PySide.QtCore.QPoint (ax , ay ) in the table widgets coordinate system, or returns 0 if the specified point is not covered by an item in the table widget.
		"""
		res = super(QTableWidget,self).itemAt(*args,**kwargs)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=QtCore.QModelIndex

		Returns a pointer to the PySide.QtGui.QTableWidgetItem assocated with the given index .
		"""
		res = super(QTableWidget,self).itemFromIndex(index)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def items(self,data):
		"""
		items(data)
			data=QtCore.QMimeData

		Returns a list of pointers to the items contained in the data object
		If the object was not created by a PySide.QtGui.QTreeWidget in the same process, the list is empty.
		"""
		res = super(QTableWidget,self).items(data)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,items):
		"""
		mimeData(items)
			items=unKnown


		"""
		res = super(QTableWidget,self).mimeData(items)
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,item):
		"""
		openPersistentEditor(item)
			item=QtGui.QTableWidgetItem

		Opens an editor for the give item
		The editor remains open after editing.
		"""
		res = super(QTableWidget,self).openPersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def removeCellWidget(self,row,column):
		"""
		removeCellWidget(row,column)
			row=QtCore.int
			column=QtCore.int

		Removes the widget set on the cell indicated by row and column .
		"""
		res = super(QTableWidget,self).removeCellWidget(row,column)
		return res
	#----------------------------------------------------------------------
	def row(self,item):
		"""
		row(item)
			item=QtGui.QTableWidgetItem

		Returns the row for the item .
		"""
		res = super(QTableWidget,self).row(item)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setCellWidget(self,row,column,widget):
		"""
		setCellWidget(row,column,widget)
			row=QtCore.int
			column=QtCore.int
			widget=QtGui.QWidget

		Sets the given widget to be displayed in the cell in the given row and column , passing the ownership of the widget to the table.
		If cell widget A is replaced with cell widget B, cell widget A will be deleted
		For example, in the code snippet below, the PySide.QtGui.QLineEdit object will be deleted.
		"""
		res = super(QTableWidget,self).setCellWidget(row,column,widget)
		return res
	#----------------------------------------------------------------------
	def setColumnCount(self,columns):
		"""
		setColumnCount(columns)
			columns=QtCore.int

		This property holds the number of columns in the table.
		By default, for a table constructed without row and column counts, this property contains a value of 0.
		"""
		res = super(QTableWidget,self).setColumnCount(columns)
		return res
	#----------------------------------------------------------------------
	def setCurrentCell(self,*args,**kwargs):
		"""
		setCurrentCell(row,column,command)
			row=QtCore.int
			column=QtCore.int
			command=QtGui.QItemSelectionModel.SelectionFlags

		setCurrentCell(row,column)
			row=QtCore.int
			column=QtCore.int


		"""
		res = super(QTableWidget,self).setCurrentCell(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setCurrentItem(self,*args,**kwargs):
		"""
		setCurrentItem(item)
			item=QtGui.QTableWidgetItem

		setCurrentItem(item,command)
			item=QtGui.QTableWidgetItem
			command=QtGui.QItemSelectionModel.SelectionFlags

		Sets the current item to item .
		Unless the selection mode is NoSelection , the item is also be selected.
		"""
		res = super(QTableWidget,self).setCurrentItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeaderItem(self,column,item):
		"""
		setHorizontalHeaderItem(column,item)
			column=QtCore.int
			item=QtGui.QTableWidgetItem

		Sets the horizontal header item for column column to item .
		"""
		res = super(QTableWidget,self).setHorizontalHeaderItem(column,item)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeaderLabels(self,labels):
		"""
		setHorizontalHeaderLabels(labels)
			labels=list

		Sets the horizontal header labels using labels .
		"""
		res = super(QTableWidget,self).setHorizontalHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def setItem(self,row,column,item):
		"""
		setItem(row,column,item)
			row=QtCore.int
			column=QtCore.int
			item=QtGui.QTableWidgetItem

		Sets the item for the given row and column to item .
		The table takes ownership of the item.
		Note that if sorting is enabled (see PySide.QtGui.QTableView.sortingEnabled() ) and column is the current sort column, the row will be moved to the sorted position determined by item .
		If you want to set several items of a particular row (say, by calling PySide.QtGui.QTableWidget.setItem() in a loop), you may want to turn off sorting before doing so, and turn it back on afterwards; this will allow you to use the same row argument for all items in the same row (i.e
		PySide.QtGui.QTableWidget.setItem() will not move the row).
		"""
		res = super(QTableWidget,self).setItem(row,column,item)
		return res
	#----------------------------------------------------------------------
	def setItemPrototype(self,item):
		"""
		setItemPrototype(item)
			item=QtGui.QTableWidgetItem

		Sets the item prototype for the table to the specified item .
		The table widget will use the item prototype clone function when it needs to create a new table item
		For example when the user is editing in an empty cell
		This is useful when you have a PySide.QtGui.QTableWidgetItem subclass and want to make sure that PySide.QtGui.QTableWidget creates instances of your subclass.
		The table takes ownership of the prototype.
		"""
		res = super(QTableWidget,self).setItemPrototype(item)
		return res
	#----------------------------------------------------------------------
	def setRangeSelected(self,range,select):
		"""
		setRangeSelected(range,select)
			range=QtGui.QTableWidgetSelectionRange
			select=QtCore.bool

		Selects or deselects the range depending on select .
		"""
		res = super(QTableWidget,self).setRangeSelected(range,select)
		return res
	#----------------------------------------------------------------------
	def setRowCount(self,rows):
		"""
		setRowCount(rows)
			rows=QtCore.int

		This property holds the number of rows in the table.
		By default, for a table constructed without row and column counts, this property contains a value of 0.
		"""
		res = super(QTableWidget,self).setRowCount(rows)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeaderItem(self,row,item):
		"""
		setVerticalHeaderItem(row,item)
			row=QtCore.int
			item=QtGui.QTableWidgetItem

		Sets the vertical header item for row row to item .
		"""
		res = super(QTableWidget,self).setVerticalHeaderItem(row,item)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeaderLabels(self,labels):
		"""
		setVerticalHeaderLabels(labels)
			labels=list

		Sets the vertical header labels using labels .
		"""
		res = super(QTableWidget,self).setVerticalHeaderLabels(labels)
		return res
	#----------------------------------------------------------------------
	def sortItems(self,column,order=None):
		"""
		sortItems(column,order=None)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QTableWidget,self).sortItems(column,order)
		return res
	#----------------------------------------------------------------------
	def takeHorizontalHeaderItem(self,column):
		"""
		takeHorizontalHeaderItem(column)
			column=QtCore.int

		Removes the horizontal header item at column from the header without deleting it.
		"""
		res = super(QTableWidget,self).takeHorizontalHeaderItem(column)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def takeItem(self,row,column):
		"""
		takeItem(row,column)
			row=QtCore.int
			column=QtCore.int

		Removes the item at row and column from the table without deleting it.
		"""
		res = super(QTableWidget,self).takeItem(row,column)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def takeVerticalHeaderItem(self,row):
		"""
		takeVerticalHeaderItem(row)
			row=QtCore.int

		Removes the vertical header item at row from the header without deleting it.
		"""
		res = super(QTableWidget,self).takeVerticalHeaderItem(row)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def verticalHeaderItem(self,row):
		"""
		verticalHeaderItem(row)
			row=QtCore.int

		Returns the vertical header item for row row .
		"""
		res = super(QTableWidget,self).verticalHeaderItem(row)
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def visualColumn(self,logicalColumn):
		"""
		visualColumn(logicalColumn)
			logicalColumn=QtCore.int

		Returns the visual column of the given logicalColumn .
		"""
		res = super(QTableWidget,self).visualColumn(logicalColumn)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def visualItemRect(self,item):
		"""
		visualItemRect(item)
			item=QtGui.QTableWidgetItem

		Returns the rectangle on the viewport occupied by the item at item .
		"""
		res = super(QTableWidget,self).visualItemRect(item)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def visualRow(self,logicalRow):
		"""
		visualRow(logicalRow)
			logicalRow=QtCore.int

		Returns the visual row of the given logicalRow .
		"""
		res = super(QTableWidget,self).visualRow(logicalRow)
		isinstance(res,QtCore.int)
		return res
