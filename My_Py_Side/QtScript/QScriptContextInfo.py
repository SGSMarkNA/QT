from PySide import QtGui, QtCore

class QScriptContextInfo(QtScript.QScriptContextInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptContextInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnNumber(self):
		"""

		"""
		res = super(QScriptContextInfo,self).columnNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the name of the file where the code being executed was defined, if available; otherwise returns an empty string.
		For Qt Script code, this function returns the fileName argument that was passed to QScriptEngine.evaluate() .
		"""
		res = super(QScriptContextInfo,self).fileName()
		return res
	#----------------------------------------------------------------------
	def functionEndLineNumber(self):
		"""
		Returns the line number where the definition of the called function ends, or -1 if the line number is not available.
		The ending line number is only available if the PySide.QtScript.QScriptContextInfo.functionType() is ScriptFunction .
		"""
		res = super(QScriptContextInfo,self).functionEndLineNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def functionMetaIndex(self):
		"""
		Returns the meta index of the called function, or -1 if the meta index is not available.
		The meta index is only available if the PySide.QtScript.QScriptContextInfo.functionType() is QtFunction or QtPropertyFunction
		For QtFunction , the meta index can be passed to QMetaObject.method() to obtain the corresponding method definition; for QtPropertyFunction , the meta index can be passed to QMetaObject.property() to obtain the corresponding property definition.
		"""
		res = super(QScriptContextInfo,self).functionMetaIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def functionName(self):
		"""
		Returns the name of the called function, or an empty string if the name is not available.
		For script functions of type QtPropertyFunction , this function always returns the name of the property; you can use QScriptContext.argumentCount() to differentiate between reads and writes.
		"""
		res = super(QScriptContextInfo,self).functionName()
		return res
	#----------------------------------------------------------------------
	def functionParameterNames(self):
		"""
		Returns the names of the formal parameters of the called function, or an empty PySide.QtCore.QStringList if the parameter names are not available.
		"""
		res = super(QScriptContextInfo,self).functionParameterNames()
		return res
	#----------------------------------------------------------------------
	def functionStartLineNumber(self):
		"""
		Returns the line number where the definition of the called function starts, or -1 if the line number is not available.
		The starting line number is only available if the PySide.QtScript.QScriptContextInfo.functionType() is ScriptFunction .
		"""
		res = super(QScriptContextInfo,self).functionStartLineNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def functionType(self):
		"""
		Returns the type of the called function.
		"""
		res = super(QScriptContextInfo,self).functionType()
		isinstance(res,QtScript.QScriptContextInfo.FunctionType)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this PySide.QtScript.QScriptContextInfo is null, i.e
		does not contain any information.
		"""
		res = super(QScriptContextInfo,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		Returns the line number corresponding to the statement being executed, or -1 if the line number is not available.
		The line number is only available if Qt Script code is being executed.
		"""
		res = super(QScriptContextInfo,self).lineNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def scriptId(self):
		"""
		Returns the ID of the script where the code being executed was defined, or -1 if the ID is not available (i.e
		a native function is being executed).
		"""
		res = super(QScriptContextInfo,self).scriptId()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtScript.QScriptContextInfo

		Returns true if this PySide.QtScript.QScriptContextInfo is not equal to the other info, otherwise returns false.
		"""
		res = super(QScriptContextInfo,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtScript.QScriptContextInfo

		Returns true if this PySide.QtScript.QScriptContextInfo is equal to the other info, otherwise returns false.
		"""
		res = super(QScriptContextInfo,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
