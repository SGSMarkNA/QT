from PySide import QtGui, QtCore

class QScriptClass(QtScript.QScriptClass):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptClass,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns the engine that this PySide.QtScript.QScriptClass is associated with.
		"""
		res = super(QScriptClass,self).engine()
		isinstance(res,QtScript.QScriptEngine)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the script class.
		Qt Script uses this name to generate a default string representation of objects in case you do not provide a toString function.
		The default implementation returns a null string.
		"""
		res = super(QScriptClass,self).name()
		return res
	#----------------------------------------------------------------------
	def prototype(self):
		"""
		Returns the object to be used as the prototype of new instances of this class (created with QScriptEngine.newObject() ).
		The default implementation returns an invalid PySide.QtScript.QScriptValue , meaning that the standard Object prototype will be used
		Reimplement this function to provide your own custom prototype.
		Typically you initialize your prototype object in the constructor of your class, then return it in this function.
		See the Making Use of Prototype-Based Inheritance section in the QtScript documentation for more information on how prototypes are used.
		"""
		res = super(QScriptClass,self).prototype()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def extension(self,extension,argument=None):
		"""
		extension(extension,argument=None)
			extension=QtScript.QScriptClass.Extension
			argument=object

		This virtual function can be reimplemented in a PySide.QtScript.QScriptClass subclass to provide support for extensions
		The optional argument can be provided as input to the extension ; the result must be returned in the form of a PySide.QtCore.QVariant
		You can call PySide.QtScript.QScriptClass.supportsExtension() to check if an extension is supported by the PySide.QtScript.QScriptClass
		By default, no extensions are supported, and this function returns an invalid PySide.QtCore.QVariant .
		If you implement the Callable extension, Qt Script will call this function when an instance of your class is called as a function (e.g
		from a script or using QScriptValue.call() )
		The argument will contain a pointer to the PySide.QtScript.QScriptContext that represents the function call, and you should return a PySide.QtCore.QVariant that holds the result of the function call
		In the following example the sum of the arguments to the script function are added up and returned:
		If you implement the HasInstance extension, Qt Script will call this function as part of evaluating the instanceof operator, as described in ECMA-262 Section 11.8.6
		The argument is a QScriptValueList containing two items: The first item is the object that HasInstance is being applied to (an instance of your class), and the second item can be any value
		PySide.QtScript.QScriptClass.extension() should return true if the value delegates behavior to the object, false otherwise.
		"""
		res = super(QScriptClass,self).extension(extension,argument)
		return res
	#----------------------------------------------------------------------
	def newIterator(self,object):
		"""
		newIterator(object)
			object=QtScript.QScriptValue

		Returns an iterator for traversing custom properties of the given object .
		The default implementation returns 0, meaning that there are no custom properties to traverse.
		Reimplement this function if objects of your script class can have one or more custom properties (e.g
		those reported to be handled by queryProperty() ) that you want to appear when an objects properties are enumerated (e.g
		by a for-in statement in a script).
		Qt Script takes ownership of the new iterator object.
		"""
		res = super(QScriptClass,self).newIterator(object)
		isinstance(res,QtScript.QScriptClassPropertyIterator)
		return res
	#----------------------------------------------------------------------
	def property(self,object,name,id):
		"""
		property(object,name,id)
			object=QtScript.QScriptValue
			name=QtScript.QScriptString
			id=QtCore.uint

		Returns the value of the property with the given name of the given object .
		The id argument is only useful if you assigned a value to it in queryProperty() .
		The default implementation does nothing and returns an invalid PySide.QtScript.QScriptValue .
		"""
		res = super(QScriptClass,self).property(object,name,id)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def propertyFlags(self,object,name,id):
		"""
		propertyFlags(object,name,id)
			object=QtScript.QScriptValue
			name=QtScript.QScriptString
			id=QtCore.uint

		Returns the flags of the property with the given name of the given object .
		The id argument is only useful if you assigned a value to it in queryProperty() .
		The default implementation returns 0.
		"""
		res = super(QScriptClass,self).propertyFlags(object,name,id)
		isinstance(res,QtScript.QScriptValue.PropertyFlags)
		return res
	#----------------------------------------------------------------------
	def setProperty(self,object,name,id,value):
		"""
		setProperty(object,name,id,value)
			object=QtScript.QScriptValue
			name=QtScript.QScriptString
			id=QtCore.uint
			value=QtScript.QScriptValue

		Sets the property with the given name of the given object to the given value .
		The id argument is only useful if you assigned a value to it in queryProperty() .
		The default implementation does nothing.
		An invalid value represents a request to remove the property.
		"""
		res = super(QScriptClass,self).setProperty(object,name,id,value)
		return res
	#----------------------------------------------------------------------
	def supportsExtension(self,extension):
		"""
		supportsExtension(extension)
			extension=QtScript.QScriptClass.Extension

		Returns true if the PySide.QtScript.QScriptClass supports the given extension ; otherwise, false is returned
		By default, no extensions are supported.
		Reimplement this function to indicate which extensions your custom class supports.
		"""
		res = super(QScriptClass,self).supportsExtension(extension)
		isinstance(res,bool)
		return res
