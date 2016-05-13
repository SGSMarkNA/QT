from PySide import QtGui, QtCore

class QScriptClassPropertyIterator(QtScript.QScriptClassPropertyIterator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptClassPropertyIterator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags of the last property that was jumped over using PySide.QtScript.QScriptClassPropertyIterator.next() or PySide.QtScript.QScriptClassPropertyIterator.previous() .
		The default implementation calls the propertyFlags() function of PySide.QtScript.QScriptClassPropertyIterator.object() with argument PySide.QtScript.QScriptClassPropertyIterator.name() .
		"""
		res = super(QScriptClassPropertyIterator,self).flags()
		isinstance(res,QtScript.QScriptValue.PropertyFlags)
		return res
	#----------------------------------------------------------------------
	def hasNext(self):
		"""
		Returns true if there is at least one item ahead of the iterator (i.e
		the iterator is not at the back of the property sequence); otherwise returns false.
		"""
		res = super(QScriptClassPropertyIterator,self).hasNext()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasPrevious(self):
		"""
		Returns true if there is at least one item behind the iterator (i.e
		the iterator is not at the front of the property sequence); otherwise returns false.
		"""
		res = super(QScriptClassPropertyIterator,self).hasPrevious()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def id(self):
		"""
		Returns the id of the last property that was jumped over using PySide.QtScript.QScriptClassPropertyIterator.next() or PySide.QtScript.QScriptClassPropertyIterator.previous() .
		The default implementation returns 0.
		"""
		res = super(QScriptClassPropertyIterator,self).id()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the last property that was jumped over using PySide.QtScript.QScriptClassPropertyIterator.next() or PySide.QtScript.QScriptClassPropertyIterator.previous() .
		"""
		res = super(QScriptClassPropertyIterator,self).name()
		isinstance(res,QtScript.QScriptString)
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		Advances the iterator by one position.
		Calling this function on an iterator located at the back of the container leads to undefined results.
		"""
		res = super(QScriptClassPropertyIterator,self).next()
		return res
	#----------------------------------------------------------------------
	def object(self):
		"""
		Returns the Qt Script object this iterator is traversing.
		"""
		res = super(QScriptClassPropertyIterator,self).object()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def previous(self):
		"""
		Moves the iterator back by one position.
		Calling this function on an iterator located at the front of the container leads to undefined results.
		"""
		res = super(QScriptClassPropertyIterator,self).previous()
		return res
	#----------------------------------------------------------------------
	def toBack(self):
		"""
		Moves the iterator to the back of the PySide.QtScript.QScriptValue (after the last property).
		"""
		res = super(QScriptClassPropertyIterator,self).toBack()
		return res
	#----------------------------------------------------------------------
	def toFront(self):
		"""
		Moves the iterator to the front of the PySide.QtScript.QScriptValue (before the first property).
		"""
		res = super(QScriptClassPropertyIterator,self).toFront()
		return res
