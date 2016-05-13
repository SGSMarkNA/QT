from PySide import QtGui, QtCore

class QItemSelectionModel(QtGui.QItemSelectionModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QItemSelectionModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the selection model
		Emits PySide.QtGui.QItemSelectionModel.selectionChanged() and PySide.QtGui.QItemSelectionModel.currentChanged() .
		"""
		res = super(QItemSelectionModel,self).clear()
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		Returns the model item index for the current item, or an invalid index if there is no current item.
		"""
		res = super(QItemSelectionModel,self).currentIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def hasSelection(self):
		"""
		Returns true if the selection model contains any selection ranges; otherwise returns false.
		"""
		res = super(QItemSelectionModel,self).hasSelection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the item model operated on by the selection model.
		"""
		res = super(QItemSelectionModel,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Clears the selection model
		Does not emit any signals.
		"""
		res = super(QItemSelectionModel,self).reset()
		return res
	#----------------------------------------------------------------------
	def selectedIndexes(self):
		"""
		Returns a list of all selected model item indexes
		The list contains no duplicates, and is not sorted.
		"""
		res = super(QItemSelectionModel,self).selectedIndexes()
		return res
	#----------------------------------------------------------------------
	def selection(self):
		"""
		Returns the selection ranges stored in the selection model.
		"""
		res = super(QItemSelectionModel,self).selection()
		isinstance(res,QtGui.QItemSelection)
		return res
	#----------------------------------------------------------------------
	def columnIntersectsSelection(self,column,parent):
		"""
		columnIntersectsSelection(column,parent)
			column=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if there are any items selected in the column with the given parent .
		"""
		res = super(QItemSelectionModel,self).columnIntersectsSelection(column,parent)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def emitSelectionChanged(self,newSelection,oldSelection):
		"""
		emitSelectionChanged(newSelection,oldSelection)
			newSelection=QtGui.QItemSelection
			oldSelection=QtGui.QItemSelection

		Compares the two selections newSelection and oldSelection and emits PySide.QtGui.QItemSelectionModel.selectionChanged() with the deselected and selected items.
		"""
		res = super(QItemSelectionModel,self).emitSelectionChanged(newSelection,oldSelection)
		return res
	#----------------------------------------------------------------------
	def isColumnSelected(self,column,parent):
		"""
		isColumnSelected(column,parent)
			column=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if all items are selected in the column with the given parent .
		Note that this function is usually faster than calling PySide.QtGui.QItemSelectionModel.isSelected() on all items in the same column and that unselectable items are ignored.
		"""
		res = super(QItemSelectionModel,self).isColumnSelected(column,parent)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRowSelected(self,row,parent):
		"""
		isRowSelected(row,parent)
			row=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if all items are selected in the row with the given parent .
		Note that this function is usually faster than calling PySide.QtGui.QItemSelectionModel.isSelected() on all items in the same row and that unselectable items are ignored.
		"""
		res = super(QItemSelectionModel,self).isRowSelected(row,parent)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSelected(self,index):
		"""
		isSelected(index)
			index=QtCore.QModelIndex

		Returns true if the given model item index is selected.
		"""
		res = super(QItemSelectionModel,self).isSelected(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rowIntersectsSelection(self,row,parent):
		"""
		rowIntersectsSelection(row,parent)
			row=QtCore.int
			parent=QtCore.QModelIndex

		Returns true if there are any items selected in the row with the given parent .
		"""
		res = super(QItemSelectionModel,self).rowIntersectsSelection(row,parent)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def select(self,*args,**kwargs):
		"""
		select(index,command)
			index=QtCore.QModelIndex
			command=QtGui.QItemSelectionModel.SelectionFlags

		select(selection,command)
			selection=QtGui.QItemSelection
			command=QtGui.QItemSelectionModel.SelectionFlags


		"""
		res = super(QItemSelectionModel,self).select(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def selectedColumns(self,row=None):
		"""
		selectedColumns(row=None)
			row=QtCore.int

		Returns the indexes in the given row for columns where all rows are selected.
		"""
		res = super(QItemSelectionModel,self).selectedColumns(row)
		return res
	#----------------------------------------------------------------------
	def selectedRows(self,column=None):
		"""
		selectedRows(column=None)
			column=QtCore.int

		Returns the indexes in the given column for the rows where all columns are selected.
		"""
		res = super(QItemSelectionModel,self).selectedRows(column)
		return res
