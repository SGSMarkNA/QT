from PySide import QtGui, QtCore

class QUuid(QtCore.QUuid):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUuid,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QUuid,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QUuid,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is the null UUID {00000000-0000-0000-0000-000000000000}; otherwise returns false.
		"""
		res = super(QUuid,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns the string representation of this PySide.QtCore.QUuid
		The string is formatted as five hex fields separated by - and enclosed in curly braces, i.e., {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx} where x is a hex digit
		From left to right, the five hex fields are obtained from the four public data members in PySide.QtCore.QUuid as follows:
		"""
		res = super(QUuid,self).toString()
		return res
	#----------------------------------------------------------------------
	def variant(self):
		"""
		Returns the value in the variant field of the UUID
		If the return value is QUuid.DCE , call PySide.QtCore.QUuid.version() to see which layout it uses
		The null UUID is considered to be of an unknown variant.
		"""
		res = super(QUuid,self).variant()
		isinstance(res,QtCore.QUuid.Variant)
		return res
	#----------------------------------------------------------------------
	def version(self):
		"""
		Returns the version field of the UUID, if the UUIDs variant field is QUuid.DCE
		Otherwise it returns QUuid.VerUnknown .
		"""
		res = super(QUuid,self).version()
		isinstance(res,QtCore.QUuid.Version)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,orig):
		"""
		__ne__(orig)
			orig=QtCore.QUuid

		Returns true if this PySide.QtCore.QUuid and the otherPySide.QtCore.QUuid are different; otherwise returns false.
		"""
		res = super(QUuid,self).__ne__(orig)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QUuid

		Returns true if this PySide.QtCore.QUuid has the same variant field as the otherPySide.QtCore.QUuid and is lexicographically before the otherPySide.QtCore.QUuid
		If the otherPySide.QtCore.QUuid has a different variant field, the return value is determined by comparing the two variants .
		"""
		res = super(QUuid,self).__lt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,orig):
		"""
		__eq__(orig)
			orig=QtCore.QUuid

		Returns true if this PySide.QtCore.QUuid and the otherPySide.QtCore.QUuid are identical; otherwise returns false.
		"""
		res = super(QUuid,self).__eq__(orig)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,other):
		"""
		__gt__(other)
			other=QtCore.QUuid

		Returns true if this PySide.QtCore.QUuid has the same variant field as the otherPySide.QtCore.QUuid and is lexicographically after the otherPySide.QtCore.QUuid
		If the otherPySide.QtCore.QUuid has a different variant field, the return value is determined by comparing the two variants .
		"""
		res = super(QUuid,self).__gt__(other)
		isinstance(res,QtCore.bool)
		return res
