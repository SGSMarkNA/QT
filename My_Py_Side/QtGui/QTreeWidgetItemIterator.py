from PySide import QtGui, QtCore

class QTreeWidgetItemIterator(QtGui.QTreeWidgetItemIterator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTreeWidgetItemIterator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __iter__(self):
		"""

		"""
		res = super(QTreeWidgetItemIterator,self).__iter__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __next__(self):
		"""

		"""
		res = super(QTreeWidgetItemIterator,self).__next__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""

		"""
		res = super(QTreeWidgetItemIterator,self).value()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def matchesFlags(self,item):
		"""
		matchesFlags(item)
			item=QtGui.QTreeWidgetItem


		"""
		res = super(QTreeWidgetItemIterator,self).matchesFlags(item)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,n):
		"""
		__iadd__(n)
			n=QtCore.int

		Makes the iterator go forward by n matching items
		(If n is negative, the iterator goes backward.)
		If the current item is beyond the last item, the current item pointer is set to 0
		Returns the resulting iterator.
		"""
		res = super(QTreeWidgetItemIterator,self).__iadd__(n)
		isinstance(res,QtGui.QTreeWidgetItemIterator)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,n):
		"""
		__isub__(n)
			n=QtCore.int

		Makes the iterator go backward by n matching items
		(If n is negative, the iterator goes forward.)
		If the current item is ahead of the last item, the current item pointer is set to 0
		Returns the resulting iterator.
		"""
		res = super(QTreeWidgetItemIterator,self).__isub__(n)
		isinstance(res,QtGui.QTreeWidgetItemIterator)
		return res
