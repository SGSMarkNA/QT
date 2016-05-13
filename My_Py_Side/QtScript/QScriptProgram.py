from PySide import QtGui, QtCore

class QScriptProgram(QtScript.QScriptProgram):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptProgram,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the filename associated with this program.
		"""
		res = super(QScriptProgram,self).fileName()
		return res
	#----------------------------------------------------------------------
	def firstLineNumber(self):
		"""
		Returns the line number associated with this program.
		"""
		res = super(QScriptProgram,self).firstLineNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this PySide.QtScript.QScriptProgram is null; otherwise returns false.
		"""
		res = super(QScriptProgram,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sourceCode(self):
		"""
		Returns the source code of this program.
		"""
		res = super(QScriptProgram,self).sourceCode()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtScript.QScriptProgram

		Returns true if this PySide.QtScript.QScriptProgram is not equal to other ; otherwise returns false.
		"""
		res = super(QScriptProgram,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtScript.QScriptProgram

		Returns true if this PySide.QtScript.QScriptProgram is equal to other ; otherwise returns false.
		"""
		res = super(QScriptProgram,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
