from PySide import QtGui, QtCore

class QScriptable(QtScript.QScriptable):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptable,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def argumentCount(self):
		"""
		Returns the number of arguments passed to the function in this invocation, or -1 if the Qt function was not invoked from script code.
		"""
		res = super(QScriptable,self).argumentCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def context(self):
		"""
		Returns a pointer to the PySide.QtScript.QScriptContext associated with the current Qt function call, or 0 if the Qt function was not invoked from script code.
		"""
		res = super(QScriptable,self).context()
		isinstance(res,QtScript.QScriptContext)
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns a pointer to the PySide.QtScript.QScriptEngine associated with the current Qt function call, or 0 if the Qt function was not invoked from script code.
		"""
		res = super(QScriptable,self).engine()
		isinstance(res,QtScript.QScriptEngine)
		return res
	#----------------------------------------------------------------------
	def thisObject(self):
		"""
		Returns the this object associated with the current Qt function call, or an invalid :class:`PySide.QtScript.QScriptValue if the Qt function was not invoked from script code.
		"""
		res = super(QScriptable,self).thisObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def argument(self,index):
		"""
		argument(index)
			index=QtCore.int

		Returns the function argument at the given index , or an invalid PySide.QtScript.QScriptValue if the Qt function was not invoked from script code.
		"""
		res = super(QScriptable,self).argument(index)
		isinstance(res,QtScript.QScriptValue)
		return res
