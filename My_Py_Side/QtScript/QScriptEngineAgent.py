from PySide import QtGui, QtCore

class QScriptEngineAgent(QtScript.QScriptEngineAgent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptEngineAgent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def contextPop(self):
		"""
		This function is called when the current script context is about to be popped.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).contextPop()
		return res
	#----------------------------------------------------------------------
	def contextPush(self):
		"""
		This function is called when a new script context has been pushed.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).contextPush()
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns the PySide.QtScript.QScriptEngine that this agent is associated with.
		"""
		res = super(QScriptEngineAgent,self).engine()
		isinstance(res,QtScript.QScriptEngine)
		return res
	#----------------------------------------------------------------------
	def exceptionCatch(self,scriptId,exception):
		"""
		exceptionCatch(scriptId,exception)
			scriptId=QtCore.qint64
			exception=QtScript.QScriptValue

		This function is called when the given exception is about to be caught, in the script identified by scriptId .
		Reimplement this function if you want to handle this event.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).exceptionCatch(scriptId,exception)
		return res
	#----------------------------------------------------------------------
	def exceptionThrow(self,scriptId,exception,hasHandler):
		"""
		exceptionThrow(scriptId,exception,hasHandler)
			scriptId=QtCore.qint64
			exception=QtScript.QScriptValue
			hasHandler=QtCore.bool

		This function is called when the given exception has occurred in the engine, in the script identified by scriptId
		If the exception was thrown by a native Qt Script function, scriptId is -1.
		If hasHandler is true, there is a catch or finally block that will handle the exception
		If hasHandler is false, there is no handler for the exception.
		Reimplement this function if you want to handle this event
		For example, a debugger can notify the user when an uncaught exception occurs (i.e
		hasHandler is false).
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).exceptionThrow(scriptId,exception,hasHandler)
		return res
	#----------------------------------------------------------------------
	def extension(self,extension,argument=None):
		"""
		extension(extension,argument=None)
			extension=QtScript.QScriptEngineAgent.Extension
			argument=object

		This virtual function can be reimplemented in a PySide.QtScript.QScriptEngineAgent subclass to provide support for extensions
		The optional argument can be provided as input to the extension ; the result must be returned in the form of a PySide.QtCore.QVariant
		You can call PySide.QtScript.QScriptEngineAgent.supportsExtension() to check if an extension is supported by the PySide.QtScript.QScriptEngineAgent
		By default, no extensions are supported, and this function returns an invalid PySide.QtCore.QVariant .
		If you implement the DebuggerInvocationRequest extension, Qt Script will call this function when a debugger statement is encountered in a script
		The argument is a QVariantList containing three items: The first item is the scriptId (a qint64), the second item is the line number (an int), and the third item is the column number (an int).
		"""
		res = super(QScriptEngineAgent,self).extension(extension,argument)
		return res
	#----------------------------------------------------------------------
	def functionEntry(self,scriptId):
		"""
		functionEntry(scriptId)
			scriptId=QtCore.qint64

		This function is called when a script function is called in the engine
		If the script function is not a native Qt Script function, it resides in the script identified by scriptId ; otherwise, scriptId is -1.
		This function is called just before execution of the script function begins
		You can obtain the PySide.QtScript.QScriptContext associated with the function call with QScriptEngine.currentContext()
		The arguments passed to the function are available.
		Reimplement this function to handle this event
		For example, a debugger implementation could reimplement this function (and PySide.QtScript.QScriptEngineAgent.functionExit() ) to keep track of the call stack and provide step-over functionality.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).functionEntry(scriptId)
		return res
	#----------------------------------------------------------------------
	def functionExit(self,scriptId,returnValue):
		"""
		functionExit(scriptId,returnValue)
			scriptId=QtCore.qint64
			returnValue=QtScript.QScriptValue

		This function is called when the currently executing script function is about to return
		If the script function is not a native Qt Script function, it resides in the script identified by scriptId ; otherwise, scriptId is -1
		The returnValue is the value that the script function will return.
		This function is called just before the script function returns
		You can still access the PySide.QtScript.QScriptContext associated with the script function call with QScriptEngine.currentContext() .
		If the engines PySide.QtScript.QScriptEngine.hasUncaughtException() () function returns true, the script function is exiting due to an exception; otherwise, the script function is returning normally.
		Reimplement this function to handle this event; typically you will then also want to reimplement PySide.QtScript.QScriptEngineAgent.functionEntry() .
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).functionExit(scriptId,returnValue)
		return res
	#----------------------------------------------------------------------
	def positionChange(self,scriptId,lineNumber,columnNumber):
		"""
		positionChange(scriptId,lineNumber,columnNumber)
			scriptId=QtCore.qint64
			lineNumber=QtCore.int
			columnNumber=QtCore.int

		This function is called when the engine is about to execute a new statement in the script identified by scriptId
		The statement begins on the line and column specified by lineNumber This event is not generated for native Qt Script functions.
		Reimplement this function to handle this event
		For example, a debugger implementation could reimplement this function to provide line-by-line stepping, and a profiler implementation could use it to count the number of times each statement is executed.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).positionChange(scriptId,lineNumber,columnNumber)
		return res
	#----------------------------------------------------------------------
	def scriptLoad(self,id,program,fileName,baseLineNumber):
		"""
		scriptLoad(id,program,fileName,baseLineNumber)
			id=QtCore.qint64
			program=unicode
			fileName=unicode
			baseLineNumber=QtCore.int

		This function is called when the engine has parsed a script and has associated it with the given id
		The id can be used to identify this particular script in subsequent event notifications.
		program , fileName and baseLineNumber are the original arguments to the QScriptEngine.evaluate() call that triggered this event.
		This function is called just before the script is about to be evaluated.
		You can reimplement this function to record information about the script; for example, by retaining the script text, you can obtain the line of text corresponding to a line number in a subsequent call to PySide.QtScript.QScriptEngineAgent.positionChange() .
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).scriptLoad(id,program,fileName,baseLineNumber)
		return res
	#----------------------------------------------------------------------
	def scriptUnload(self,id):
		"""
		scriptUnload(id)
			id=QtCore.qint64

		This function is called when the engine has discarded the script identified by the given id .
		You can reimplement this function to clean up any resources you have associated with the script.
		The default implementation does nothing.
		"""
		res = super(QScriptEngineAgent,self).scriptUnload(id)
		return res
	#----------------------------------------------------------------------
	def supportsExtension(self,extension):
		"""
		supportsExtension(extension)
			extension=QtScript.QScriptEngineAgent.Extension

		Returns true if the PySide.QtScript.QScriptEngineAgent supports the given extension ; otherwise, false is returned
		By default, no extensions are supported.
		"""
		res = super(QScriptEngineAgent,self).supportsExtension(extension)
		isinstance(res,bool)
		return res
