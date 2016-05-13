from PySide import QtGui, QtCore

class QPersistentModelIndex(QtCore.QPersistentModelIndex):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPersistentModelIndex,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the column this persistent model index refers to.
		"""
		res = super(QPersistentModelIndex,self).column()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags for the item referred to by the index.
		"""
		res = super(QPersistentModelIndex,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def internalId(self):
		"""
		Returns a qint64 used by the model to associate the index with the internal data structure.
		"""
		res = super(QPersistentModelIndex,self).internalId()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def internalPointer(self):
		"""
		Returns a void* pointer used by the model to associate the index with the internal data structure.
		"""
		res = super(QPersistentModelIndex,self).internalPointer()
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this persistent model index is valid; otherwise returns false.
		A valid index belongs to a model, and has non-negative row and column numbers.
		"""
		res = super(QPersistentModelIndex,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that the index belongs to.
		"""
		res = super(QPersistentModelIndex,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the parent PySide.QtCore.QModelIndex for this persistent index, or an invalid PySide.QtCore.QModelIndex if it has no parent.
		"""
		res = super(QPersistentModelIndex,self).parent()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def row(self):
		"""
		Returns the row this persistent model index refers to.
		"""
		res = super(QPersistentModelIndex,self).row()
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
		res = super(QPersistentModelIndex,self).child(row,column)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def data(self,role=None):
		"""
		data(role=None)
			role=QtCore.int

		Returns the data for the given role for the item referred to by the index.
		"""
		res = super(QPersistentModelIndex,self).data(role)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,*args,**kwargs):
		"""
		__ne__(other)
			other=QtCore.QModelIndex

		__ne__(other)
			other=QtCore.QPersistentModelIndex

		Returns true if this persistent model index does not refer to the same location as the other model index; otherwise returns false.
		"""
		res = super(QPersistentModelIndex,self).__ne__(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QPersistentModelIndex

		Returns true if this persistent model index is smaller than the other persistent model index; otherwise returns false.
		All values in the persistent model index are used when comparing with another persistent model index.
		"""
		res = super(QPersistentModelIndex,self).__lt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,*args,**kwargs):
		"""
		__eq__(other)
			other=QtCore.QPersistentModelIndex

		__eq__(other)
			other=QtCore.QModelIndex

		Returns true if this persistent model index is equal to the other persistent model index; otherwise returns false.
		All values in the persistent model index are used when comparing with another persistent model index.
		"""
		res = super(QPersistentModelIndex,self).__eq__(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sibling(self,row,column):
		"""
		sibling(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the sibling at row and column or an invalid PySide.QtCore.QModelIndex if there is no sibling at this position.
		"""
		res = super(QPersistentModelIndex,self).sibling(row,column)
		isinstance(res,QtCore.QModelIndex)
		return res
