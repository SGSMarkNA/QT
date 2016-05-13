from PySide import QtGui, QtCore

class QScriptString(QtScript.QScriptString):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptString,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this PySide.QtScript.QScriptString is valid; otherwise returns false.
		"""
		res = super(QScriptString,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns the string that this PySide.QtScript.QScriptString represents, or a null string if this PySide.QtScript.QScriptString is not valid.
		"""
		res = super(QScriptString,self).toString()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtScript.QScriptString

		Returns true if this PySide.QtScript.QScriptString is not equal to other ; otherwise returns false.
		"""
		res = super(QScriptString,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtScript.QScriptString

		Returns true if this PySide.QtScript.QScriptString is equal to other ; otherwise returns false.
		"""
		res = super(QScriptString,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toArrayIndex(self,ok=None):
		"""
		toArrayIndex(ok=None)
			ok=QtCore.bool

		Attempts to convert this PySide.QtScript.QScriptString to a QtScript array index, and returns the result.
		If a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QScriptString,self).toArrayIndex(ok)
		isinstance(res,QtCore.quint32)
		return res
