from PySide import QtGui, QtCore

class QModelIndex(QtCore.QModelIndex):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QModelIndex,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the column this model index refers to.
		"""
		res = super(QModelIndex,self).column()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags for the item referred to by the index.
		"""
		res = super(QModelIndex,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def internalId(self):
		"""
		Returns a qint64 used by the model to associate the index with the internal data structure.
		"""
		res = super(QModelIndex,self).internalId()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def internalPointer(self):
		"""
		Returns a void* pointer used by the model to associate the index with the internal data structure.
		"""
		res = super(QModelIndex,self).internalPointer()
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this model index is valid; otherwise returns false.
		A valid index belongs to a model, and has non-negative row and column numbers.
		"""
		res = super(QModelIndex,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns a pointer to the model containing the item that this index refers to.
		A const pointer to the model is returned because calls to non-const functions of the model might invalidate the model index and possibly crash your application.
		"""
		res = super(QModelIndex,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the parent of the model index, or PySide.QtCore.QModelIndex.QModelIndex() if it has no parent.
		"""
		res = super(QModelIndex,self).parent()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def row(self):
		"""
		Returns the row this model index refers to.
		"""
		res = super(QModelIndex,self).row()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def child(self,row,column):
		"""
		child(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the child of the model index that is stored in the given row and column .
		"""
		res = super(QModelIndex,self).child(row,column)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def data(self,role=None):
		"""
		data(role=None)
			role=QtCore.int

		Returns the data for the given role for the item referred to by the index.
		"""
		res = super(QModelIndex,self).data(role)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QModelIndex

		Returns true if this model index does not refer to the same location as the other model index; otherwise returns false.
		"""
		res = super(QModelIndex,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QModelIndex

		Returns true if this model index is smaller than the other model index; otherwise returns false.
		"""
		res = super(QModelIndex,self).__lt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QModelIndex

		Returns true if this model index refers to the same location as the other model index; otherwise returns false.
		All values in the model index are used when comparing with another model index.
		"""
		res = super(QModelIndex,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sibling(self,row,column):
		"""
		sibling(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the sibling at row and column
		If there is no sibling at this position, an invalid PySide.QtCore.QModelIndex is returned.
		"""
		res = super(QModelIndex,self).sibling(row,column)
		isinstance(res,QtCore.QModelIndex)
		return res
