from PySide import QtGui, QtCore

class QMetaEnum(QtCore.QMetaEnum):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMetaEnum,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isFlag(self):
		"""
		Returns true if this enumerator is used as a flag; otherwise returns false.
		When used as flags, enumerators can be combined using the OR operator.
		"""
		res = super(QMetaEnum,self).isFlag()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this enum is valid (has a name); otherwise returns false.
		"""
		res = super(QMetaEnum,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def keyCount(self):
		"""
		Returns the number of keys.
		"""
		res = super(QMetaEnum,self).keyCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the enumerator (without the scope).
		For example, the Qt.AlignmentFlag enumeration has AlignmentFlag as the name and Qt as the scope.
		"""
		res = super(QMetaEnum,self).name()
		return res
	#----------------------------------------------------------------------
	def scope(self):
		"""
		Returns the scope this enumerator was declared in.
		For example, the Qt.AlignmentFlag enumeration has Qt as the scope and AlignmentFlag as the name.
		"""
		res = super(QMetaEnum,self).scope()
		return res
	#----------------------------------------------------------------------
	def key(self,index):
		"""
		key(index)
			index=QtCore.int

		Returns the key with the given index , or 0 if no such key exists.
		"""
		res = super(QMetaEnum,self).key(index)
		return res
	#----------------------------------------------------------------------
	def keyToValue(self,key):
		"""
		keyToValue(key)
			key=str

		Returns the integer value of the given enumeration key , or -1 if key is not defined.
		For flag types, use PySide.QtCore.QMetaEnum.keysToValue() .
		"""
		res = super(QMetaEnum,self).keyToValue(key)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def keysToValue(self,keys):
		"""
		keysToValue(keys)
			keys=str

		Returns the value derived from combining together the values of the keys using the OR operator, or -1 if keys is not defined
		Note that the strings in keys must be |-separated.
		"""
		res = super(QMetaEnum,self).keysToValue(keys)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def value(self,index):
		"""
		value(index)
			index=QtCore.int

		Returns the value with the given index ; or returns -1 if there is no such value.
		"""
		res = super(QMetaEnum,self).value(index)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def valueToKey(self,value):
		"""
		valueToKey(value)
			value=QtCore.int

		Returns the string that is used as the name of the given enumeration value , or 0 if value is not defined.
		For flag types, use PySide.QtCore.QMetaEnum.valueToKeys() .
		"""
		res = super(QMetaEnum,self).valueToKey(value)
		return res
	#----------------------------------------------------------------------
	def valueToKeys(self,value):
		"""
		valueToKeys(value)
			value=QtCore.int

		Returns a byte array of |-separated keys that represents the given value .
		"""
		res = super(QMetaEnum,self).valueToKeys(value)
		isinstance(res,QtCore.QByteArray)
		return res
