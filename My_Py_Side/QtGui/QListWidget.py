from PySide import QtGui, QtCore

class QListWidget(QtGui.QListWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QListWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of items in the list including any hidden items..
		"""
		res = super(QListWidget,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item.
		"""
		res = super(QListWidget,self).currentItem()
		isinstance(res,QtGui.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def currentRow(self):
		"""
		This property holds the row of the current item..
		Depending on the current selection mode, the row may also be selected.
		"""
		res = super(QListWidget,self).currentRow()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isSortingEnabled(self):
		"""
		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the list; if the property is false, sorting is not enabled.
		The default value is false.
		"""
		res = super(QListWidget,self).isSortingEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def itemSelectionChanged(self):
		"""

		"""
		res = super(QListWidget,self).itemSelectionChanged()
		return res
	#----------------------------------------------------------------------
	def mimeTypes(self):
		"""
		Returns a list of MIME types that can be used to describe a list of listwidget items.
		"""
		res = super(QListWidget,self).mimeTypes()
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all selected items in the list widget.
		"""
		res = super(QListWidget,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def sortOrder(self):
		"""

		"""
		res = super(QListWidget,self).sortOrder()
		isinstance(res,QtCore.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def supportedDropActions(self):
		"""
		Returns the drop actions supported by this view.
		"""
		res = super(QListWidget,self).supportedDropActions()
		isinstance(res,QtCore.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def addItem(self,*args,**kwargs):
		"""
		addItem(label)
			label=unicode

		addItem(item)
			item=QtGui.QListWidgetItem

		Inserts an item with the text label at the end of the list widget.
		"""
		res = super(QListWidget,self).addItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addItems(self,labels):
		"""
		addItems(labels)
			labels=list

		Inserts items with the text labels at the end of the list widget.
		"""
		res = super(QListWidget,self).addItems(labels)
		return res
	#----------------------------------------------------------------------
	def closePersistentEditor(self,item):
		"""
		closePersistentEditor(item)
			item=QtGui.QListWidgetItem

		Closes the persistent editor for the given item .
		"""
		res = super(QListWidget,self).closePersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def dropMimeData(self,index,data,action):
		"""
		dropMimeData(index,data,action)
			index=QtCore.int
			data=QtCore.QMimeData
			action=QtCore.Qt.DropAction


		"""
		res = super(QListWidget,self).dropMimeData(index,data,action)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def editItem(self,item):
		"""
		editItem(item)
			item=QtGui.QListWidgetItem

		Starts editing the item if it is editable.
		"""
		res = super(QListWidget,self).editItem(item)
		return res
	#----------------------------------------------------------------------
	def findItems(self,text,flags):
		"""
		findItems(text,flags)
			text=unicode
			flags=QtCore.Qt.MatchFlags


		"""
		res = super(QListWidget,self).findItems(text,flags)
		return res
	#----------------------------------------------------------------------
	def indexFromItem(self,item):
		"""
		indexFromItem(item)
			item=QtGui.QListWidgetItem

		Returns the PySide.QtCore.QModelIndex assocated with the given item .
		"""
		res = super(QListWidget,self).indexFromItem(item)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,*args,**kwargs):
		"""
		insertItem(row,label)
			row=QtCore.int
			label=unicode

		insertItem(row,item)
			row=QtCore.int
			item=QtGui.QListWidgetItem

		Inserts an item with the text label in the list widget at the position given by row .
		"""
		res = super(QListWidget,self).insertItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def insertItems(self,row,labels):
		"""
		insertItems(row,labels)
			row=QtCore.int
			labels=list

		Inserts items from the list of labels into the list, starting at the given row .
		"""
		res = super(QListWidget,self).insertItems(row,labels)
		return res
	#----------------------------------------------------------------------
	def item(self,row):
		"""
		item(row)
			row=QtCore.int

		Returns the item that occupies the given row in the list if one has been set; otherwise returns 0.
		"""
		res = super(QListWidget,self).item(row)
		isinstance(res,QtGui.QListWidgetItem)
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
		res = super(QListWidget,self).itemAt(*args,**kwargs)
		isinstance(res,QtGui.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemFromIndex(self,index):
		"""
		itemFromIndex(index)
			index=QtCore.QModelIndex

		Returns a pointer to the PySide.QtGui.QListWidgetItem assocated with the given index .
		"""
		res = super(QListWidget,self).itemFromIndex(index)
		isinstance(res,QtGui.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def itemWidget(self,item):
		"""
		itemWidget(item)
			item=QtGui.QListWidgetItem

		Returns the widget displayed in the given item .
		"""
		res = super(QListWidget,self).itemWidget(item)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def items(self,data):
		"""
		items(data)
			data=QtCore.QMimeData

		Returns a list of pointers to the items contained in the data object
		If the object was not created by a PySide.QtGui.QListWidget in the same process, the list is empty.
		"""
		res = super(QListWidget,self).items(data)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,items):
		"""
		mimeData(items)
			items=unKnown


		"""
		res = super(QListWidget,self).mimeData(items)
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def openPersistentEditor(self,item):
		"""
		openPersistentEditor(item)
			item=QtGui.QListWidgetItem

		Opens an editor for the given item
		The editor remains open after editing.
		"""
		res = super(QListWidget,self).openPersistentEditor(item)
		return res
	#----------------------------------------------------------------------
	def removeItemWidget(self,item):
		"""
		removeItemWidget(item)
			item=QtGui.QListWidgetItem

		Removes the widget set on the given item .
		"""
		res = super(QListWidget,self).removeItemWidget(item)
		return res
	#----------------------------------------------------------------------
	def row(self,item):
		"""
		row(item)
			item=QtGui.QListWidgetItem

		Returns the row containing the given item .
		"""
		res = super(QListWidget,self).row(item)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setCurrentItem(self,*args,**kwargs):
		"""
		setCurrentItem(item)
			item=QtGui.QListWidgetItem

		setCurrentItem(item,command)
			item=QtGui.QListWidgetItem
			command=QtGui.QItemSelectionModel.SelectionFlags

		Sets the current item to item .
		Unless the selection mode is NoSelection , the item is also be selected.
		"""
		res = super(QListWidget,self).setCurrentItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setCurrentRow(self,*args,**kwargs):
		"""
		setCurrentRow(row,command)
			row=QtCore.int
			command=QtGui.QItemSelectionModel.SelectionFlags

		setCurrentRow(row)
			row=QtCore.int


		"""
		res = super(QListWidget,self).setCurrentRow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setItemWidget(self,item,widget):
		"""
		setItemWidget(item,widget)
			item=QtGui.QListWidgetItem
			widget=QtGui.QWidget

		Sets the widget to be displayed in the give item .
		This function should only be used to display static content in the place of a list widget item
		If you want to display custom dynamic content or implement a custom editor widget, use PySide.QtGui.QListView and subclass PySide.QtGui.QItemDelegate instead.
		"""
		res = super(QListWidget,self).setItemWidget(item,widget)
		return res
	#----------------------------------------------------------------------
	def setSortingEnabled(self,enable):
		"""
		setSortingEnabled(enable)
			enable=QtCore.bool

		This property holds whether sorting is enabled.
		If this property is true, sorting is enabled for the list; if the property is false, sorting is not enabled.
		The default value is false.
		"""
		res = super(QListWidget,self).setSortingEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def sortItems(self,order=None):
		"""
		sortItems(order=None)
			order=QtCore.Qt.SortOrder


		"""
		res = super(QListWidget,self).sortItems(order)
		return res
	#----------------------------------------------------------------------
	def takeItem(self,row):
		"""
		takeItem(row)
			row=QtCore.int

		Removes and returns the item from the given row in the list widget; otherwise returns 0.
		Items removed from a list widget will not be managed by Qt, and will need to be deleted manually.
		"""
		res = super(QListWidget,self).takeItem(row)
		isinstance(res,QtGui.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def visualItemRect(self,item):
		"""
		visualItemRect(item)
			item=QtGui.QListWidgetItem

		Returns the rectangle on the viewport occupied by the item at item .
		"""
		res = super(QListWidget,self).visualItemRect(item)
		isinstance(res,QtCore.QRect)
		return res
