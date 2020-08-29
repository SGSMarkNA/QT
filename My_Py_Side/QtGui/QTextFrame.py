from PySide import QtGui, QtCore

class QTextFrame(QtGui.QTextFrame):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextFrame,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __iter__(self):
		"""

		"""
		res = super(QTextFrame,self).__iter__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __next__(self):
		"""

		"""
		res = super(QTextFrame,self).__next__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the current item is the last item in the text frame.
		"""
		res = super(QTextFrame,self).atEnd()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def currentBlock(self):
		"""
		Returns the current block the iterator points to
		If the iterator points to a child frame, the returned block is invalid.
		"""
		res = super(QTextFrame,self).currentBlock()
		isinstance(res,QtGui.QTextBlock)
		return res
	#----------------------------------------------------------------------
	def currentFrame(self):
		"""
		Returns the current frame pointed to by the iterator, or 0 if the iterator currently points to a block.
		"""
		res = super(QTextFrame,self).currentFrame()
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QTextFrame.iterator.operator++(arg__1)(self):
		"""
		The postfix ++ operator (i++ ) advances the iterator to the next item in the text frame, and returns an iterator to the old item.
		"""
		res = super(QTextFrame,self).PySide.QtGui.QTextFrame.iterator.operator++(arg__1)()
		isinstance(res,QtGui.QTextFrame::iterator)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QTextFrame.iterator.operator--(arg__1)(self):
		"""
		The postfix  operator (i-- ) makes the preceding item in the current frame, and returns an iterator to the old item.
		"""
		res = super(QTextFrame,self).PySide.QtGui.QTextFrame.iterator.operator--(arg__1)()
		isinstance(res,QtGui.QTextFrame::iterator)
		return res
	#----------------------------------------------------------------------
	def parentFrame(self):
		"""
		Returns the parent frame of the current frame.
		"""
		res = super(QTextFrame,self).parentFrame()
		isinstance(res,QtGui.QTextFrame)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,o):
		"""
		__ne__(o)
			o=QtGui.QTextFrame::iterator

		Retuns true if the iterator is different from the other iterator; otherwise returns false.
		"""
		res = super(QTextFrame,self).__ne__(o)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,o):
		"""
		__eq__(o)
			o=QtGui.QTextFrame::iterator

		Retuns true if the iterator is the same as the other iterator; otherwise returns false.
		"""
		res = super(QTextFrame,self).__eq__(o)
		isinstance(res,bool)
		return res
