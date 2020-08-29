from PySide import QtGui, QtCore

class QDeclarativeListReference(QtDeclarative.QDeclarativeListReference):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeListReference,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def canAppend(self):
		"""
		Returns true if the list property can be appended to, otherwise false
		Returns false if the reference is invalid.
		"""
		res = super(QDeclarativeListReference,self).canAppend()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canAt(self):
		"""
		Returns true if the list property can queried by index, otherwise false
		Returns false if the reference is invalid.
		"""
		res = super(QDeclarativeListReference,self).canAt()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canClear(self):
		"""
		Returns true if the list property can be cleared, otherwise false
		Returns false if the reference is invalid.
		"""
		res = super(QDeclarativeListReference,self).canClear()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canCount(self):
		"""
		Returns true if the list property can be queried for its element count, otherwise false
		Returns false if the reference is invalid.
		"""
		res = super(QDeclarativeListReference,self).canCount()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the list
		Returns true if the operation succeeded, otherwise false.
		"""
		res = super(QDeclarativeListReference,self).clear()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of objects in the list, or 0 if the operation failed.
		"""
		res = super(QDeclarativeListReference,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the instance refers to a valid list property, otherwise false.
		"""
		res = super(QDeclarativeListReference,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def listElementType(self):
		"""
		Returns the PySide.QtCore.QMetaObject for the elements stored in the list property
		Returns 0 if the reference is invalid.
		The PySide.QtCore.QMetaObject can be used ahead of time to determine whether a given instance can be added to a list.
		"""
		res = super(QDeclarativeListReference,self).listElementType()
		isinstance(res,QtCore.QMetaObject)
		return res
	#----------------------------------------------------------------------
	def object(self):
		"""
		Returns the list propertys object
		Returns 0 if the reference is invalid.
		"""
		res = super(QDeclarativeListReference,self).object()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def append(self,arg__1):
		"""
		append(arg__1)
			arg__1=QtCore.QObject

		Appends object to the list
		Returns true if the operation succeeded, otherwise false.
		"""
		res = super(QDeclarativeListReference,self).append(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def at(self,arg__1):
		"""
		at(arg__1)
			arg__1=QtCore.int

		Returns the list element at index , or 0 if the operation failed.
		"""
		res = super(QDeclarativeListReference,self).at(arg__1)
		isinstance(res,QtCore.QObject)
		return res
