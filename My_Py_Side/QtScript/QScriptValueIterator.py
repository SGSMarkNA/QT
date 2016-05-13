from PySide import QtGui, QtCore

class QScriptValueIterator(QtScript.QScriptValueIterator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptValueIterator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __iter__(self):
		"""

		"""
		res = super(QScriptValueIterator,self).__iter__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __next__(self):
		"""

		"""
		res = super(QScriptValueIterator,self).__next__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags of the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).flags()
		isinstance(res,QtScript.QScriptValue.PropertyFlags)
		return res
	#----------------------------------------------------------------------
	def hasNext(self):
		"""
		Returns true if there is at least one item ahead of the iterator (i.e
		the iterator is not at the back of the property sequence); otherwise returns false.
		"""
		res = super(QScriptValueIterator,self).hasNext()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasPrevious(self):
		"""
		Returns true if there is at least one item behind the iterator (i.e
		the iterator is not at the front of the property sequence); otherwise returns false.
		"""
		res = super(QScriptValueIterator,self).hasPrevious()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).name()
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		Advances the iterator by one position.
		Calling this function on an iterator located at the back of the container leads to undefined results.
		"""
		res = super(QScriptValueIterator,self).next()
		return res
	#----------------------------------------------------------------------
	def previous(self):
		"""
		Moves the iterator back by one position.
		Calling this function on an iterator located at the front of the container leads to undefined results.
		"""
		res = super(QScriptValueIterator,self).previous()
		return res
	#----------------------------------------------------------------------
	def remove(self):
		"""
		Removes the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).remove()
		return res
	#----------------------------------------------------------------------
	def scriptName(self):
		"""
		Returns the name of the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).scriptName()
		isinstance(res,QtScript.QScriptString)
		return res
	#----------------------------------------------------------------------
	def toBack(self):
		"""
		Moves the iterator to the back of the PySide.QtScript.QScriptValue (after the last property).
		"""
		res = super(QScriptValueIterator,self).toBack()
		return res
	#----------------------------------------------------------------------
	def toFront(self):
		"""
		Moves the iterator to the front of the PySide.QtScript.QScriptValue (before the first property).
		"""
		res = super(QScriptValueIterator,self).toFront()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the value of the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).value()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def setValue(self,value):
		"""
		setValue(value)
			value=QtScript.QScriptValue

		Sets the value of the last property that was jumped over using PySide.QtScript.QScriptValueIterator.next() or PySide.QtScript.QScriptValueIterator.previous() .
		"""
		res = super(QScriptValueIterator,self).setValue(value)
		return res
