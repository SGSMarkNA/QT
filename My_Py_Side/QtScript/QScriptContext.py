from PySide import QtGui, QtCore

class QScriptContext(QtScript.QScriptContext):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptContext,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activationObject(self):
		"""
		Returns the activation object of this PySide.QtScript.QScriptContext
		The activation object provides access to the local variables associated with this context.
		"""
		res = super(QScriptContext,self).activationObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def argumentCount(self):
		"""
		Returns the number of arguments passed to the function in this invocation.
		Note that the argument count can be different from the formal number of arguments (the length property of PySide.QtScript.QScriptContext.callee() ).
		"""
		res = super(QScriptContext,self).argumentCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def argumentsObject(self):
		"""
		Returns the arguments object of this PySide.QtScript.QScriptContext .
		The arguments object has properties callee (equal to PySide.QtScript.QScriptContext.callee() ) and length (equal to PySide.QtScript.QScriptContext.argumentCount() ), and properties 0 , 1 , ..., PySide.QtScript.QScriptContext.argumentCount() - 1 that provide access to the argument values
		Initially, property P (0 <= P < PySide.QtScript.QScriptContext.argumentCount() ) has the same value as argument(P )
		In the case when P is less than the number of formal parameters of the function, P shares its value with the corresponding property of the activation object ( PySide.QtScript.QScriptContext.activationObject() )
		This means that changing this property changes the corresponding property of the activation object and vice versa.
		"""
		res = super(QScriptContext,self).argumentsObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def backtrace(self):
		"""
		Returns a human-readable backtrace of this PySide.QtScript.QScriptContext .
		Each line is of the form <function-name>(<arguments>)@<file-name>:<line-number> .
		To access individual pieces of debugging-related information (for example, to construct your own backtrace representation), use PySide.QtScript.QScriptContextInfo .
		"""
		res = super(QScriptContext,self).backtrace()
		return res
	#----------------------------------------------------------------------
	def callee(self):
		"""
		Returns the callee
		The callee is the function object that this PySide.QtScript.QScriptContext represents an invocation of.
		"""
		res = super(QScriptContext,self).callee()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns the PySide.QtScript.QScriptEngine that this PySide.QtScript.QScriptContext belongs to.
		"""
		res = super(QScriptContext,self).engine()
		isinstance(res,QtScript.QScriptEngine)
		return res
	#----------------------------------------------------------------------
	def isCalledAsConstructor(self):
		"""
		Returns true if the function was called as a constructor (e.g
		"new foo()" ); otherwise returns false.
		When a function is called as constructor, the PySide.QtScript.QScriptContext.thisObject() contains the newly constructed object to be initialized.
		"""
		res = super(QScriptContext,self).isCalledAsConstructor()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def parentContext(self):
		"""
		Returns the parent context of this PySide.QtScript.QScriptContext .
		"""
		res = super(QScriptContext,self).parentContext()
		isinstance(res,QtScript.QScriptContext)
		return res
	#----------------------------------------------------------------------
	def popScope(self):
		"""
		Removes the front object from this contexts scope chain, and returns the removed object.
		If the scope chain is already empty, this function returns an invalid PySide.QtScript.QScriptValue .
		"""
		res = super(QScriptContext,self).popScope()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def returnValue(self):
		"""

		"""
		res = super(QScriptContext,self).returnValue()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def scopeChain(self):
		"""
		Returns the scope chain of this PySide.QtScript.QScriptContext .
		"""
		res = super(QScriptContext,self).scopeChain()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the frameution state of this PySide.QtScript.QScriptContext .
		"""
		res = super(QScriptContext,self).state()
		isinstance(res,QtScript.QScriptContext.ExecutionState)
		return res
	#----------------------------------------------------------------------
	def thisObject(self):
		"""
		Returns the this object associated with this :class:`PySide.QtScript.QScriptContext .
		"""
		res = super(QScriptContext,self).thisObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns a string representation of this context
		This is useful for debugging.
		"""
		res = super(QScriptContext,self).toString()
		return res
	#----------------------------------------------------------------------
	def argument(self,index):
		"""
		argument(index)
			index=QtCore.int

		Returns the function argument at the given index .
		If index >= PySide.QtScript.QScriptContext.argumentCount() , a PySide.QtScript.QScriptValue of the primitive type Undefined is returned.
		"""
		res = super(QScriptContext,self).argument(index)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def pushScope(self,object):
		"""
		pushScope(object)
			object=QtScript.QScriptValue

		Adds the given object to the front of this contexts scope chain.
		If object is not an object, this function does nothing.
		"""
		res = super(QScriptContext,self).pushScope(object)
		return res
	#----------------------------------------------------------------------
	def setActivationObject(self,activation):
		"""
		setActivationObject(activation)
			activation=QtScript.QScriptValue

		Sets the activation object of this PySide.QtScript.QScriptContext to be the given activation .
		If activation is not an object, this function does nothing.
		"""
		res = super(QScriptContext,self).setActivationObject(activation)
		return res
	#----------------------------------------------------------------------
	def setReturnValue(self,result):
		"""
		setReturnValue(result)
			result=QtScript.QScriptValue


		"""
		res = super(QScriptContext,self).setReturnValue(result)
		return res
	#----------------------------------------------------------------------
	def setThisObject(self,thisObject):
		"""
		setThisObject(thisObject)
			thisObject=QtScript.QScriptValue

		Sets the this object associated with this :class:`PySide.QtScript.QScriptContext to be thisObject .
		If thisObject is not an object, this function does nothing.
		"""
		res = super(QScriptContext,self).setThisObject(thisObject)
		return res
	#----------------------------------------------------------------------
	def throwError(self,*args,**kwargs):
		"""
		throwError(text)
			text=unicode

		throwError(error,text)
			error=QtScript.QScriptContext.Error
			text=unicode

		This is an overloaded function.
		Throws an error with the given text
		Returns the created error object.
		"""
		res = super(QScriptContext,self).throwError(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def throwValue(self,value):
		"""
		throwValue(value)
			value=QtScript.QScriptValue

		Throws an exception with the given value
		Returns the value thrown (the same as the argument).
		"""
		res = super(QScriptContext,self).throwValue(value)
		isinstance(res,QtScript.QScriptValue)
		return res
