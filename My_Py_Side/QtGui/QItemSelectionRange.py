from PySide import QtGui, QtCore

class QItemSelectionRange(QtGui.QItemSelectionRange):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QItemSelectionRange,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		Returns the row index corresponding to the lowermost selected row in the selection range.
		"""
		res = super(QItemSelectionRange,self).bottom()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def bottomRight(self):
		"""
		Returns the index for the item located at the bottom-right corner of the selection range.
		"""
		res = super(QItemSelectionRange,self).bottomRight()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the number of selected rows in the selection range.
		"""
		res = super(QItemSelectionRange,self).height()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def indexes(self):
		"""
		Returns the list of model index items stored in the selection.
		"""
		res = super(QItemSelectionRange,self).indexes()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the selection range contains no selectable item
		"""
		res = super(QItemSelectionRange,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the selection range is valid; otherwise returns false.
		"""
		res = super(QItemSelectionRange,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def left(self):
		"""
		Returns the column index corresponding to the leftmost selected column in the selection range.
		"""
		res = super(QItemSelectionRange,self).left()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that the items in the selection range belong to.
		"""
		res = super(QItemSelectionRange,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the parent model item index of the items in the selection range.
		"""
		res = super(QItemSelectionRange,self).parent()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def right(self):
		"""
		Returns the column index corresponding to the rightmost selected column in the selection range.
		"""
		res = super(QItemSelectionRange,self).right()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		Returns the row index corresponding to the uppermost selected row in the selection range.
		"""
		res = super(QItemSelectionRange,self).top()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def topLeft(self):
		"""
		Returns the index for the item located at the top-left corner of the selection range.
		"""
		res = super(QItemSelectionRange,self).topLeft()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the number of selected columns in the selection range.
		"""
		res = super(QItemSelectionRange,self).width()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def contains(self,*args,**kwargs):
		"""
		contains(row,column,parentIndex)
			row=QtCore.int
			column=QtCore.int
			parentIndex=QtCore.QModelIndex

		contains(index)
			index=QtCore.QModelIndex

		This is an overloaded function.
		Returns true if the model item specified by (row , column ) and with parentIndex as the parent item lies within the range of selected items; otherwise returns false.
		"""
		res = super(QItemSelectionRange,self).contains(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def intersected(self,other):
		"""
		intersected(other)
			other=QtGui.QItemSelectionRange

		Returns a new selection range containing only the items that are found in both the selection range and the other selection range.
		"""
		res = super(QItemSelectionRange,self).intersected(other)
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def intersects(self,other):
		"""
		intersects(other)
			other=QtGui.QItemSelectionRange

		Returns true if this selection range intersects (overlaps with) the other range given; otherwise returns false.
		"""
		res = super(QItemSelectionRange,self).intersects(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QItemSelectionRange

		Returns true if the selection range differs from the other range given; otherwise returns false.
		"""
		res = super(QItemSelectionRange,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QItemSelectionRange

		Returns true if the selection range is exactly the same as the other range given; otherwise returns false.
		"""
		res = super(QItemSelectionRange,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
