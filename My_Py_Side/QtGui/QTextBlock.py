from PySide import QtGui, QtCore

class QTextBlock(QtGui.QTextBlock):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextBlock,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __iter__(self):
		"""

		"""
		res = super(QTextBlock,self).__iter__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __next__(self):
		"""

		"""
		res = super(QTextBlock,self).__next__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the current item is the last item in the text block.
		"""
		res = super(QTextBlock,self).atEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fragment(self):
		"""
		Returns the text fragment the iterator currently points to.
		"""
		res = super(QTextBlock,self).fragment()
		isinstance(res,QtGui.QTextFragment)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QTextBlock.iterator.operator++(arg__1)(self):
		"""
		The postfix ++ operator (i++ ) advances the iterator to the next item in the text block and returns an iterator to the old current item.
		"""
		res = super(QTextBlock,self).PySide.QtGui.QTextBlock.iterator.operator++(arg__1)()
		isinstance(res,QtGui.QTextBlock::iterator)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QTextBlock.iterator.operator--(arg__1)(self):
		"""
		The postfix  operator (i-- ) makes the preceding item current and returns an iterator to the old current item.
		"""
		res = super(QTextBlock,self).PySide.QtGui.QTextBlock.iterator.operator--(arg__1)()
		isinstance(res,QtGui.QTextBlock::iterator)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,o):
		"""
		__ne__(o)
			o=QtGui.QTextBlock::iterator

		Retuns true if this iterator is different from the other iterator; otherwise returns false.
		"""
		res = super(QTextBlock,self).__ne__(o)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,o):
		"""
		__eq__(o)
			o=QtGui.QTextBlock::iterator

		Retuns true if this iterator is the same as the other iterator; otherwise returns false.
		"""
		res = super(QTextBlock,self).__eq__(o)
		isinstance(res,QtCore.bool)
		return res
