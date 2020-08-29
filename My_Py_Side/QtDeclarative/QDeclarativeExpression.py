from PySide import QtGui, QtCore

class QDeclarativeExpression(QtDeclarative.QDeclarativeExpression):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeExpression,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clearError(self):
		"""
		Clear any expression errors
		Calls to PySide.QtDeclarative.QDeclarativeExpression.hasError() following this will return false.
		"""
		res = super(QDeclarativeExpression,self).clearError()
		return res
	#----------------------------------------------------------------------
	def context(self):
		"""
		Returns the PySide.QtDeclarative.QDeclarativeContext this expression is associated with, or 0 if there is no association or the PySide.QtDeclarative.QDeclarativeContext has been destroyed.
		"""
		res = super(QDeclarativeExpression,self).context()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns the PySide.QtDeclarative.QDeclarativeEngine this expression is associated with, or 0 if there is no association or the PySide.QtDeclarative.QDeclarativeEngine has been destroyed.
		"""
		res = super(QDeclarativeExpression,self).engine()
		isinstance(res,QtDeclarative.QDeclarativeEngine)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Return any error from the last call to PySide.QtDeclarative.QDeclarativeExpression.evaluate()
		If there was no error, this returns an invalid PySide.QtDeclarative.QDeclarativeError instance.
		"""
		res = super(QDeclarativeExpression,self).error()
		isinstance(res,QtDeclarative.QDeclarativeError)
		return res
	#----------------------------------------------------------------------
	def expression(self):
		"""
		Returns the expression string.
		"""
		res = super(QDeclarativeExpression,self).expression()
		return res
	#----------------------------------------------------------------------
	def hasError(self):
		"""
		Returns true if the last call to PySide.QtDeclarative.QDeclarativeExpression.evaluate() resulted in an error, otherwise false.
		"""
		res = super(QDeclarativeExpression,self).hasError()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		Returns the source file line number for this expression
		The source location must have been previously set by calling PySide.QtDeclarative.QDeclarativeExpression.setSourceLocation() .
		"""
		res = super(QDeclarativeExpression,self).lineNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def notifyOnValueChanged(self):
		"""
		Returns true if the PySide.QtDeclarative.QDeclarativeExpression.valueChanged() signal is emitted when the expressions evaluated value changes.
		"""
		res = super(QDeclarativeExpression,self).notifyOnValueChanged()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def scopeObject(self):
		"""
		Returns the expressions scope object, if provided, otherwise 0.
		In addition to data provided by the expressions PySide.QtDeclarative.QDeclarativeContext , the scope objects properties are also in scope during the expressions evaluation.
		"""
		res = super(QDeclarativeExpression,self).scopeObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def sourceFile(self):
		"""
		Returns the source file URL for this expression
		The source location must have been previously set by calling PySide.QtDeclarative.QDeclarativeExpression.setSourceLocation() .
		"""
		res = super(QDeclarativeExpression,self).sourceFile()
		return res
	#----------------------------------------------------------------------
	def valueChanged(self):
		"""

		"""
		res = super(QDeclarativeExpression,self).valueChanged()
		return res
	#----------------------------------------------------------------------
	def evaluate(self,valueIsUndefined=None):
		"""
		evaluate(valueIsUndefined=None)
			valueIsUndefined=QtCore.bool

		Evaulates the expression, returning the result of the evaluation, or an invalid PySide.QtCore.QVariant if the expression is invalid or has an error.
		valueIsUndefined is set to true if the expression resulted in an undefined value.
		"""
		res = super(QDeclarativeExpression,self).evaluate(valueIsUndefined)
		return res
	#----------------------------------------------------------------------
	def setExpression(self,arg__1):
		"""
		setExpression(arg__1)
			arg__1=unicode

		Set the expression to expression .
		"""
		res = super(QDeclarativeExpression,self).setExpression(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNotifyOnValueChanged(self,arg__1):
		"""
		setNotifyOnValueChanged(arg__1)
			arg__1=QtCore.bool

		Sets whether the PySide.QtDeclarative.QDeclarativeExpression.valueChanged() signal is emitted when the expressions evaluated value changes.
		If notifyOnChange is true, the PySide.QtDeclarative.QDeclarativeExpression will monitor properties involved in the expressions evaluation, and emit QDeclarativeExpression.valueChanged() if they have changed
		This allows an application to ensure that any value associated with the result of the expression remains up to date.
		If notifyOnChange is false (default), the PySide.QtDeclarative.QDeclarativeExpression will not montitor properties involved in the expressions evaluation, and QDeclarativeExpression.valueChanged() will never be emitted
		This is more efficient if an application wants a one off evaluation of the expression.
		"""
		res = super(QDeclarativeExpression,self).setNotifyOnValueChanged(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSourceLocation(self,fileName,line):
		"""
		setSourceLocation(fileName,line)
			fileName=unicode
			line=QtCore.int

		Set the location of this expression to line of url
		This information is used by the script engine.
		"""
		res = super(QDeclarativeExpression,self).setSourceLocation(fileName,line)
		return res
