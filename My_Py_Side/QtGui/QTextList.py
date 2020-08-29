from PySide import QtGui, QtCore

class QTextList(QtGui.QTextList):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextList,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of items in the list.
		"""
		res = super(QTextList,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def add(self,block):
		"""
		add(block)
			block=QtGui.QTextBlock

		Makes the given block part of the list.
		"""
		res = super(QTextList,self).add(block)
		return res
	#----------------------------------------------------------------------
	def item(self,i):
		"""
		item(i)
			i=QtCore.int

		Returns the i -th text block in the list.
		"""
		res = super(QTextList,self).item(i)
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def itemNumber(self,arg__1):
		"""
		itemNumber(arg__1)
			arg__1=QtGui.QTextBlock

		Returns the index of the list item that corresponds to the given block
		Returns -1 if the block was not present in the list.
		"""
		res = super(QTextList,self).itemNumber(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def itemText(self,arg__1):
		"""
		itemText(arg__1)
			arg__1=QtGui.QTextBlock

		Returns the text of the list item that corresponds to the given block .
		"""
		res = super(QTextList,self).itemText(arg__1)
		return res
	#----------------------------------------------------------------------
	def remove(self,arg__1):
		"""
		remove(arg__1)
			arg__1=QtGui.QTextBlock

		Removes the given block from the list.
		"""
		res = super(QTextList,self).remove(arg__1)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,i):
		"""
		removeItem(i)
			i=QtCore.int

		Removes the item at item position i from the list
		When the last item in the list is removed, the list is automatically deleted by the PySide.QtGui.QTextDocument that owns it.
		"""
		res = super(QTextList,self).removeItem(i)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtGui.QTextListFormat

		Sets the lists format to format .
		"""
		res = super(QTextList,self).setFormat(format)
		return res
