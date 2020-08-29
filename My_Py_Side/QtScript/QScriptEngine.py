from PySide import QtGui, QtCore

class QScriptEngine(QtScript.QScriptEngine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptEngine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def agent(self):
		"""
		Returns the agent currently installed on this engine, or 0 if no agent is installed.
		"""
		res = super(QScriptEngine,self).agent()
		isinstance(res,QtScript.QScriptEngineAgent)
		return res
	#----------------------------------------------------------------------
	def availableExtensions(self):
		"""
		Returns a list naming the available extensions that can be imported using the PySide.QtScript.QScriptEngine.importExtension() function
		This list includes extensions that have been imported.
		"""
		res = super(QScriptEngine,self).availableExtensions()
		return res
	#----------------------------------------------------------------------
	def clearExceptions(self):
		"""
		Clears any uncaught exceptions in this engine.
		"""
		res = super(QScriptEngine,self).clearExceptions()
		return res
	#----------------------------------------------------------------------
	def collectGarbage(self):
		"""
		Runs the garbage collector.
		The garbage collector will attempt to reclaim memory by locating and disposing of objects that are no longer reachable in the script environment.
		Normally you dont need to call this function; the garbage collector will automatically be invoked when the PySide.QtScript.QScriptEngine decides that its wise to do so (i.e
		when a certain number of new objects have been created)
		However, you can call this function to explicitly request that garbage collection should be performed as soon as possible.
		"""
		res = super(QScriptEngine,self).collectGarbage()
		return res
	#----------------------------------------------------------------------
	def currentContext(self):
		"""
		Returns the current context.
		The current context is typically accessed to retrieve the arguments and this object in native functions; for convenience, it is available as the first argument in :class:`QScriptEngine.FunctionSignature<~PySide.QtScript.QScriptEngine.FunctionSignature> .
		"""
		res = super(QScriptEngine,self).currentContext()
		isinstance(res,QtScript.QScriptContext)
		return res
	#----------------------------------------------------------------------
	def globalObject(self):
		"""
		Returns this engines Global Object.
		By default, the Global Object contains the built-in objects that are part of ECMA-262 , such as Math, Date and String
		Additionally, you can set properties of the Global Object to make your own extensions available to all script code
		Non-local variables in script code will be created as properties of the Global Object, as well as local variables in global code.
		"""
		res = super(QScriptEngine,self).globalObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def hasUncaughtException(self):
		"""
		Returns true if the last script evaluation resulted in an uncaught exception; otherwise returns false.
		The exception state is cleared when PySide.QtScript.QScriptEngine.evaluate() is called.
		"""
		res = super(QScriptEngine,self).hasUncaughtException()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def importedExtensions(self):
		"""
		Returns a list naming the extensions that have been imported using the PySide.QtScript.QScriptEngine.importExtension() function.
		"""
		res = super(QScriptEngine,self).importedExtensions()
		return res
	#----------------------------------------------------------------------
	def isEvaluating(self):
		"""
		Returns true if this engine is currently evaluating a script, otherwise returns false.
		"""
		res = super(QScriptEngine,self).isEvaluating()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def newActivationObject(self):
		"""

		"""
		res = super(QScriptEngine,self).newActivationObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newObject(self):
		"""
		Creates a QtScript object of class Object.
		The prototype of the created object will be the Object prototype object.
		"""
		res = super(QScriptEngine,self).newObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def nullValue(self):
		"""
		Returns a PySide.QtScript.QScriptValue of the primitive type Null.
		"""
		res = super(QScriptEngine,self).nullValue()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def popContext(self):
		"""
		Pops the current execution context and restores the previous one
		This function must be used in conjunction with PySide.QtScript.QScriptEngine.pushContext() .
		"""
		res = super(QScriptEngine,self).popContext()
		return res
	#----------------------------------------------------------------------
	def processEventsInterval(self):
		"""
		Returns the interval in milliseconds between calls to QCoreApplication.processEvents() while the interpreter is running.
		"""
		res = super(QScriptEngine,self).processEventsInterval()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def pushContext(self):
		"""
		Enters a new execution context and returns the associated PySide.QtScript.QScriptContext object.
		Once you are done with the context, you should call PySide.QtScript.QScriptEngine.popContext() to restore the old context.
		By default, the this object of the new context is the Global Object
		The contexts :meth:`PySide.QtScript.QScriptContext.callee () will be invalid.
		This function is useful when you want to evaluate script code as if it were the body of a function
		You can use the contexts PySide.QtScript.QScriptContext.activationObject() () to initialize local variables that will be available to scripts
		Example:
		In the above example, the new variable tmp defined in the script will be local to the context; in other words, the script doesnt have any effect on the global environment.
		Returns 0 in case of stack overflow
		"""
		res = super(QScriptEngine,self).pushContext()
		isinstance(res,QtScript.QScriptContext)
		return res
	#----------------------------------------------------------------------
	def uncaughtException(self):
		"""
		Returns the current uncaught exception, or an invalid PySide.QtScript.QScriptValue if there is no uncaught exception.
		The exception value is typically an Error object; in that case, you can call toString() on the return value to obtain an error message.
		"""
		res = super(QScriptEngine,self).uncaughtException()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def uncaughtExceptionBacktrace(self):
		"""
		Returns a human-readable backtrace of the last uncaught exception.
		It is in the form <function-name>()@<file-name>:<line-number> .
		"""
		res = super(QScriptEngine,self).uncaughtExceptionBacktrace()
		return res
	#----------------------------------------------------------------------
	def uncaughtExceptionLineNumber(self):
		"""
		Returns the line number where the last uncaught exception occurred.
		Line numbers are 1-based, unless a different base was specified as the second argument to PySide.QtScript.QScriptEngine.evaluate() .
		"""
		res = super(QScriptEngine,self).uncaughtExceptionLineNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def undefinedValue(self):
		"""
		Returns a PySide.QtScript.QScriptValue of the primitive type Undefined.
		"""
		res = super(QScriptEngine,self).undefinedValue()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def abortEvaluation(self,result=None):
		"""
		abortEvaluation(result=None)
			result=QtScript.QScriptValue

		Aborts any script evaluation currently taking place in this engine
		The given result is passed back as the result of the evaluation (i.e
		it is returned from the call to PySide.QtScript.QScriptEngine.evaluate() being aborted).
		If the engine isnt evaluating a script (i.e
		PySide.QtScript.QScriptEngine.isEvaluating() returns false), this function does nothing.
		Call this function if you need to abort a running script for some reason, e.g
		when you have detected that the script has been running for several seconds without completing.
		"""
		res = super(QScriptEngine,self).abortEvaluation(result)
		return res
	#----------------------------------------------------------------------
	def canEvaluate(self,program):
		"""
		canEvaluate(program)
			program=unicode

		Returns true if program can be evaluated; i.e
		the code is sufficient to determine whether it appears to be a syntactically correct program, or contains a syntax error.
		This function returns false if program is incomplete; i.e
		the input is syntactically correct up to the point where the input is terminated.
		Note that this function only does a static check of program ; e.g
		it does not check whether references to variables are valid, and so on.
		A typical usage of PySide.QtScript.QScriptEngine.canEvaluate() is to implement an interactive interpreter for QtScript
		The user is repeatedly queried for individual lines of code; the lines are concatened internally, and only when PySide.QtScript.QScriptEngine.canEvaluate() returns true for the resulting program is it passed to PySide.QtScript.QScriptEngine.evaluate() .
		The following are some examples to illustrate the behavior of PySide.QtScript.QScriptEngine.canEvaluate()
		(Note that all example inputs are assumed to have an explicit newline as their last character, since otherwise the QtScript parser would automatically insert a semi-colon character at the end of the input, and this could cause PySide.QtScript.QScriptEngine.canEvaluate() to produce different results.)
		Given the input
		PySide.QtScript.QScriptEngine.canEvaluate() will return true, since the program appears to be complete.
		Given the input
		PySide.QtScript.QScriptEngine.canEvaluate() will return false, since the if-statement is not complete, but is syntactically correct so far.
		Given the input
		PySide.QtScript.QScriptEngine.canEvaluate() will return true, but PySide.QtScript.QScriptEngine.evaluate() will throw a SyntaxError given the same input.
		Given the input
		PySide.QtScript.QScriptEngine.canEvaluate() will return true, even though the code is clearly not syntactically valid QtScript code
		PySide.QtScript.QScriptEngine.evaluate() will throw a SyntaxError when this code is evaluated.
		Given the input
		PySide.QtScript.QScriptEngine.canEvaluate() will return true, but PySide.QtScript.QScriptEngine.evaluate() will throw a ReferenceError if foo is not defined in the script environment.
		"""
		res = super(QScriptEngine,self).canEvaluate(program)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def convert(self,value,type,ptr):
		"""
		convert(value,type,ptr)
			value=QtScript.QScriptValue
			type=QtCore.int
			ptr=void


		"""
		res = super(QScriptEngine,self).convert(value,type,ptr)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def create(self,type,ptr):
		"""
		create(type,ptr)
			type=QtCore.int
			ptr=void


		"""
		res = super(QScriptEngine,self).create(type,ptr)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def defaultPrototype(self,metaTypeId):
		"""
		defaultPrototype(metaTypeId)
			metaTypeId=QtCore.int

		Returns the default prototype associated with the given metaTypeId , or an invalid PySide.QtScript.QScriptValue if no default prototype has been set.
		"""
		res = super(QScriptEngine,self).defaultPrototype(metaTypeId)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def evaluate(self,*args,**kwargs):
		"""
		evaluate(program,fileName=None,lineNumber=None)
			program=unicode
			fileName=unicode
			lineNumber=QtCore.int

		evaluate(program)
			program=QtScript.QScriptProgram

		Evaluates program , using lineNumber as the base line number, and returns the result of the evaluation.
		The script code will be evaluated in the current context.
		The evaluation of program can cause an exception in the engine; in this case the return value will be the exception that was thrown (typically an Error object)
		You can call PySide.QtScript.QScriptEngine.hasUncaughtException() to determine if an exception occurred in the last call to PySide.QtScript.QScriptEngine.evaluate() .
		lineNumber is used to specify a starting line number for program ; line number information reported by the engine that pertain to this evaluation (e.g
		PySide.QtScript.QScriptEngine.uncaughtExceptionLineNumber() ) will be based on this argument
		For example, if program consists of two lines of code, and the statement on the second line causes a script exception, PySide.QtScript.QScriptEngine.uncaughtExceptionLineNumber() would return the given lineNumber plus one
		When no starting line number is specified, line numbers will be 1-based.
		fileName is used for error reporting
		For example in error objects the file name is accessible through the fileName property if its provided with this function.
		"""
		res = super(QScriptEngine,self).evaluate(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def importExtension(self,extension):
		"""
		importExtension(extension)
			extension=unicode

		Imports the given extension into this PySide.QtScript.QScriptEngine
		Returns PySide.QtScript.QScriptEngine.undefinedValue() if the extension was successfully imported
		You can call PySide.QtScript.QScriptEngine.hasUncaughtException() to check if an error occurred; in that case, the return value is the value that was thrown by the exception (usually an Error object).
		PySide.QtScript.QScriptEngine ensures that a particular extension is only imported once; subsequent calls to PySide.QtScript.QScriptEngine.importExtension() with the same extension name will do nothing and return PySide.QtScript.QScriptEngine.undefinedValue() .
		"""
		res = super(QScriptEngine,self).importExtension(extension)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def installTranslatorFunctions(self,object=None):
		"""
		installTranslatorFunctions(object=None)
			object=QtScript.QScriptValue

		Installs translator functions on the given object , or on the Global Object if no object is specified.
		The relation between Qt Script translator functions and C++ translator functions is described in the following table:
		"""
		res = super(QScriptEngine,self).installTranslatorFunctions(object)
		return res
	#----------------------------------------------------------------------
	def newArray(self,length=None):
		"""
		newArray(length=None)
			length=QtCore.uint

		Creates a QtScript object of class Array with the given length .
		"""
		res = super(QScriptEngine,self).newArray(length)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newDate(self,*args,**kwargs):
		"""
		newDate(value)
			value=QtCore.double

		newDate(value)
			value=QtCore.QDateTime


		"""
		res = super(QScriptEngine,self).newDate(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newObject(self,scriptClass,data=None):
		"""
		newObject(scriptClass,data=None)
			scriptClass=QtScript.QScriptClass
			data=QtScript.QScriptValue

		This is an overloaded function.
		Creates a QtScript Object of the given class, scriptClass .
		The prototype of the created object will be the Object prototype object.
		data , if specified, is set as the internal data of the new object (using QScriptValue.setData() ).
		"""
		res = super(QScriptEngine,self).newObject(scriptClass,data)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newQMetaObject(self,metaObject,ctor=None):
		"""
		newQMetaObject(metaObject,ctor=None)
			metaObject=QtCore.QMetaObject
			ctor=QtScript.QScriptValue

		Creates a QtScript object that represents a PySide.QtCore.QObject class, using the the given metaObject and constructor ctor .
		Enums of metaObject (declared with Q_ENUMS) are available as properties of the created PySide.QtScript.QScriptValue
		When the class is called as a function, ctor will be called to create a new instance of the class.
		Example:
		"""
		res = super(QScriptEngine,self).newQMetaObject(metaObject,ctor)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newQObject(self,*args,**kwargs):
		"""
		newQObject(object,ownership=None,options=None)
			object=QtCore.QObject
			ownership=QtScript.QScriptEngine.ValueOwnership
			options=QtScript.QScriptEngine.QObjectWrapOptions

		newQObject(scriptObject,qtObject,ownership=None,options=None)
			scriptObject=QtScript.QScriptValue
			qtObject=QtCore.QObject
			ownership=QtScript.QScriptEngine.ValueOwnership
			options=QtScript.QScriptEngine.QObjectWrapOptions

		Creates a QtScript object that wraps the given PySide.QtCore.QObject object , using the given ownership
		The given options control various aspects of the interaction with the resulting script object.
		Signals and slots, properties and children of object are available as properties of the created PySide.QtScript.QScriptValue
		For more information, see the QtScript documentation.
		If object is a null pointer, this function returns PySide.QtScript.QScriptEngine.nullValue() .
		If a default prototype has been registered for the object s class (or its superclass, recursively), the prototype of the new script object will be set to be that default prototype.
		If the given object is deleted outside of QtScript s control, any attempt to access the deleted PySide.QtCore.QObject s members through the QtScript wrapper object (either by script code or C++) will result in a script exception.
		"""
		res = super(QScriptEngine,self).newQObject(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newRegExp(self,*args,**kwargs):
		"""
		newRegExp(pattern,flags)
			pattern=unicode
			flags=unicode

		newRegExp(regexp)
			regexp=QtCore.QRegExp

		Creates a QtScript object of class RegExp with the given pattern and flags .
		The legal flags are g (global), i (ignore case), and m (multiline).
		"""
		res = super(QScriptEngine,self).newRegExp(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def newVariant(self,*args,**kwargs):
		"""
		newVariant(value)
			value=object

		newVariant(object,value)
			object=QtScript.QScriptValue
			value=object

		Creates a QtScript object holding the given variant value .
		If a default prototype has been registered with the meta type id of value , then the prototype of the created object will be that prototype; otherwise, the prototype will be the Object prototype object.
		"""
		res = super(QScriptEngine,self).newVariant(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def objectById(self,id):
		"""
		objectById(id)
			id=QtCore.qint64

		Returns the object with the given id , or an invalid PySide.QtScript.QScriptValue if there is no object with that id.
		"""
		res = super(QScriptEngine,self).objectById(id)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def reportAdditionalMemoryCost(self,size):
		"""
		reportAdditionalMemoryCost(size)
			size=QtCore.int

		Reports an additional memory cost of the given size , measured in bytes, to the garbage collector.
		This function can be called to indicate that a Qt Script object has memory associated with it that isnt managed by Qt Script itself
		Reporting the additional cost makes it more likely that the garbage collector will be triggered.
		Note that if the additional memory is shared with objects outside the scripting environment, the cost should not be reported, since collecting the Qt Script object would not cause the memory to be freed anyway.
		Negative size values are ignored, i.e
		this function cant be used to report that the additional memory has been deallocated.
		"""
		res = super(QScriptEngine,self).reportAdditionalMemoryCost(size)
		return res
	#----------------------------------------------------------------------
	def setAgent(self,agent):
		"""
		setAgent(agent)
			agent=QtScript.QScriptEngineAgent

		Installs the given agent on this engine
		The agent will be notified of various events pertaining to script execution
		This is useful when you want to find out exactly what the engine is doing, e.g
		when PySide.QtScript.QScriptEngine.evaluate() is called
		The agent interface is the basis of tools like debuggers and profilers.
		The engine maintains ownership of the agent .
		Calling this function will replace the existing agent, if any.
		"""
		res = super(QScriptEngine,self).setAgent(agent)
		return res
	#----------------------------------------------------------------------
	def setDefaultPrototype(self,metaTypeId,prototype):
		"""
		setDefaultPrototype(metaTypeId,prototype)
			metaTypeId=QtCore.int
			prototype=QtScript.QScriptValue

		Sets the default prototype of the C++ type identified by the given metaTypeId to prototype .
		The default prototype provides a script interface for values of type metaTypeId when a value of that type is accessed from script code
		Whenever the script engine (implicitly or explicitly) creates a PySide.QtScript.QScriptValue from a value of type metaTypeId , the default prototype will be set as the PySide.QtScript.QScriptValue s prototype.
		The prototype object itself may be constructed using one of two principal techniques; the simplest is to subclass PySide.QtScript.QScriptable , which enables you to define the scripting API of the type through PySide.QtCore.QObject properties and slots
		Another possibility is to create a script object by calling PySide.QtScript.QScriptEngine.newObject() , and populate the object with the desired properties (e.g
		native functions wrapped with newFunction() ).
		"""
		res = super(QScriptEngine,self).setDefaultPrototype(metaTypeId,prototype)
		return res
	#----------------------------------------------------------------------
	def setGlobalObject(self,object):
		"""
		setGlobalObject(object)
			object=QtScript.QScriptValue

		Sets this engines Global Object to be the given object
		If object is not a valid script object, this function does nothing.
		When setting a custom global object, you may want to use PySide.QtScript.QScriptValueIterator to copy the properties of the standard Global Object; alternatively, you can set the internal prototype of your custom object to be the original Global Object.
		"""
		res = super(QScriptEngine,self).setGlobalObject(object)
		return res
	#----------------------------------------------------------------------
	def setProcessEventsInterval(self,interval):
		"""
		setProcessEventsInterval(interval)
			interval=QtCore.int

		Sets the interval between calls to QCoreApplication::processEvents to interval milliseconds.
		While the interpreter is running, all event processing is by default blocked
		This means for instance that the gui will not be updated and timers will not be fired
		To allow event processing during interpreter execution one can specify the processing interval to be a positive value, indicating the number of milliseconds between each time QCoreApplication.processEvents() is called.
		The default value is -1, which disables event processing during interpreter execution.
		You can use QCoreApplication.postEvent() to post an event that performs custom processing at the next interval
		For example, you could keep track of the total running time of the script and call PySide.QtScript.QScriptEngine.abortEvaluation() when you detect that the script has been running for a long time without completing.
		"""
		res = super(QScriptEngine,self).setProcessEventsInterval(interval)
		return res
	#----------------------------------------------------------------------
	def toObject(self,value):
		"""
		toObject(value)
			value=QtScript.QScriptValue

		Converts the given value to an object, if such a conversion is possible; otherwise returns an invalid PySide.QtScript.QScriptValue
		The conversion is performed according to the following table:
		"""
		res = super(QScriptEngine,self).toObject(value)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def toStringHandle(self,str):
		"""
		toStringHandle(str)
			str=unicode

		Returns a handle that represents the given string, str .
		PySide.QtScript.QScriptString can be used to quickly look up properties, and compare property names, of script objects.
		"""
		res = super(QScriptEngine,self).toStringHandle(str)
		isinstance(res,QtScript.QScriptString)
		return res
