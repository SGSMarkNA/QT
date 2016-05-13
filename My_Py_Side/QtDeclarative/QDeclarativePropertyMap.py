from PySide import QtGui, QtCore

class QDeclarativePropertyMap(QtDeclarative.QDeclarativePropertyMap):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativePropertyMap,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This is an overloaded function.
		Same as PySide.QtDeclarative.QDeclarativePropertyMap.size() .
		"""
		res = super(QDeclarativePropertyMap,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the map contains no keys; otherwise returns false.
		"""
		res = super(QDeclarativePropertyMap,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def keys(self):
		"""

		"""
		res = super(QDeclarativePropertyMap,self).keys()
		return res
	#----------------------------------------------------------------------
	def PySide.QtDeclarative.QDeclarativePropertyMap.operator[](key)(self):
		"""
		This is an overloaded function.
		Same as PySide.QtDeclarative.QDeclarativePropertyMap.value() .
		"""
		res = super(QDeclarativePropertyMap,self).PySide.QtDeclarative.QDeclarativePropertyMap.operator[](key)()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the number of keys in the map.
		"""
		res = super(QDeclarativePropertyMap,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def clear(self,key):
		"""
		clear(key)
			key=unicode

		Clears the value (if any) associated with key .
		"""
		res = super(QDeclarativePropertyMap,self).clear(key)
		return res
	#----------------------------------------------------------------------
	def contains(self,key):
		"""
		contains(key)
			key=unicode

		Returns true if the map contains key .
		"""
		res = super(QDeclarativePropertyMap,self).contains(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insert(self,key,value):
		"""
		insert(key,value)
			key=unicode
			value=object

		Sets the value associated with key to value .
		If the key doesnt exist, it is automatically created.
		"""
		res = super(QDeclarativePropertyMap,self).insert(key,value)
		return res
	#----------------------------------------------------------------------
	def value(self,key):
		"""
		value(key)
			key=unicode

		Returns the value associated with key .
		If no value has been set for this key (or if the value has been cleared), an invalid PySide.QtCore.QVariant is returned.
		"""
		res = super(QDeclarativePropertyMap,self).value(key)
		return res
