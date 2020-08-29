from PySide import QtGui, QtCore

class QScriptValue(QtScript.QScriptValue):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptValue,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __iter__(self):
		"""

		"""
		res = super(QScriptValue,self).__iter__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __mgetitem__(self):
		"""

		"""
		res = super(QScriptValue,self).__mgetitem__()
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QScriptValue,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the internal data of this PySide.QtScript.QScriptValue object
		QtScript uses this property to store the primitive value of Date, String, Number and Boolean objects
		For other types of object, custom data may be stored using PySide.QtScript.QScriptValue.setData() .
		"""
		res = super(QScriptValue,self).data()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns the PySide.QtScript.QScriptEngine that created this PySide.QtScript.QScriptValue , or 0 if this PySide.QtScript.QScriptValue is invalid or the value is not associated with a particular engine.
		"""
		res = super(QScriptValue,self).engine()
		isinstance(res,QtScript.QScriptEngine)
		return res
	#----------------------------------------------------------------------
	def isArray(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is an object of the Array class; otherwise returns false.
		"""
		res = super(QScriptValue,self).isArray()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isBool(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the primitive type Boolean; otherwise returns false.
		"""
		res = super(QScriptValue,self).isBool()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isBoolean(self):
		"""
		Use PySide.QtScript.QScriptValue.isBool() instead.
		"""
		res = super(QScriptValue,self).isBoolean()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDate(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is an object of the Date class; otherwise returns false.
		"""
		res = super(QScriptValue,self).isDate()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isError(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is an object of the Error class; otherwise returns false.
		"""
		res = super(QScriptValue,self).isError()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFunction(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is a function; otherwise returns false.
		"""
		res = super(QScriptValue,self).isFunction()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the primitive type Null; otherwise returns false.
		"""
		res = super(QScriptValue,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNumber(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the primitive type Number; otherwise returns false.
		"""
		res = super(QScriptValue,self).isNumber()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isObject(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the Object type; otherwise returns false.
		Note that function values, variant values, and PySide.QtCore.QObject values are objects, so this function returns true for such values.
		"""
		res = super(QScriptValue,self).isObject()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isQMetaObject(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is a PySide.QtCore.QMetaObject ; otherwise returns false.
		"""
		res = super(QScriptValue,self).isQMetaObject()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isQObject(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is a PySide.QtCore.QObject ; otherwise returns false.
		Note: This function returns true even if the PySide.QtCore.QObject that this PySide.QtScript.QScriptValue wraps has been deleted.
		"""
		res = super(QScriptValue,self).isQObject()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isRegExp(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is an object of the RegExp class; otherwise returns false.
		"""
		res = super(QScriptValue,self).isRegExp()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isString(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the primitive type String; otherwise returns false.
		"""
		res = super(QScriptValue,self).isString()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isUndefined(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is of the primitive type Undefined; otherwise returns false.
		"""
		res = super(QScriptValue,self).isUndefined()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is valid; otherwise returns false.
		"""
		res = super(QScriptValue,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isVariant(self):
		"""
		Returns true if this PySide.QtScript.QScriptValue is a variant value; otherwise returns false.
		"""
		res = super(QScriptValue,self).isVariant()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def objectId(self):
		"""
		Returns the ID of this object, or -1 if this PySide.QtScript.QScriptValue is not an object.
		"""
		res = super(QScriptValue,self).objectId()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def prototype(self):
		"""
		If this PySide.QtScript.QScriptValue is an object, returns the internal prototype (__proto__ property) of this object; otherwise returns an invalid PySide.QtScript.QScriptValue .
		"""
		res = super(QScriptValue,self).prototype()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def scope(self):
		"""

		"""
		res = super(QScriptValue,self).scope()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def scriptClass(self):
		"""
		Returns the custom script class that this script object is an instance of, or 0 if the object is not of a custom class.
		"""
		res = super(QScriptValue,self).scriptClass()
		isinstance(res,QtScript.QScriptClass)
		return res
	#----------------------------------------------------------------------
	def toBool(self):
		"""
		Returns the boolean value of this PySide.QtScript.QScriptValue , using the conversion rules described in ECMA-262 section 9.2, ToBoolean.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toBool()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toBoolean(self):
		"""
		Use PySide.QtScript.QScriptValue.toBool() instead.
		"""
		res = super(QScriptValue,self).toBoolean()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toDateTime(self):
		"""
		Returns a PySide.QtCore.QDateTime representation of this value, in local time
		If this PySide.QtScript.QScriptValue is not a date, or the value of the date is NaN (Not-a-Number), an invalid PySide.QtCore.QDateTime is returned.
		"""
		res = super(QScriptValue,self).toDateTime()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def toInt32(self):
		"""
		Returns the signed 32-bit integer value of this PySide.QtScript.QScriptValue , using the conversion rules described in ECMA-262 section 9.5, ToInt32.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toInt32()
		isinstance(res,QtCore.qint32)
		return res
	#----------------------------------------------------------------------
	def toInteger(self):
		"""
		Returns the integer value of this PySide.QtScript.QScriptValue , using the conversion rules described in ECMA-262 section 9.4, ToInteger.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toInteger()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def toNumber(self):
		"""
		Returns the number value of this PySide.QtScript.QScriptValue , as defined in ECMA-262 section 9.3, ToNumber.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toNumber()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def toObject(self):
		"""
		This function is obsolete; use QScriptEngine.toObject() instead.
		"""
		res = super(QScriptValue,self).toObject()
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def toQMetaObject(self):
		"""
		If this PySide.QtScript.QScriptValue is a PySide.QtCore.QMetaObject , returns the PySide.QtCore.QMetaObject pointer that the PySide.QtScript.QScriptValue represents; otherwise, returns 0.
		"""
		res = super(QScriptValue,self).toQMetaObject()
		isinstance(res,QtCore.QMetaObject)
		return res
	#----------------------------------------------------------------------
	def toQObject(self):
		"""
		If this PySide.QtScript.QScriptValue is a PySide.QtCore.QObject , returns the PySide.QtCore.QObject pointer that the PySide.QtScript.QScriptValue represents; otherwise, returns 0.
		If the PySide.QtCore.QObject that this PySide.QtScript.QScriptValue wraps has been deleted, this function returns 0 (i.e
		it is possible for PySide.QtScript.QScriptValue.toQObject() to return 0 even when PySide.QtScript.QScriptValue.isQObject() returns true).
		"""
		res = super(QScriptValue,self).toQObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def toRegExp(self):
		"""
		Returns the PySide.QtCore.QRegExp representation of this value
		If this PySide.QtScript.QScriptValue is not a regular expression, an empty PySide.QtCore.QRegExp is returned.
		"""
		res = super(QScriptValue,self).toRegExp()
		isinstance(res,QtCore.QRegExp)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns the string value of this PySide.QtScript.QScriptValue , as defined in ECMA-262 section 9.8, ToString.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects PySide.QtScript.QScriptValue.toString() function (and possibly valueOf()) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toString()
		return res
	#----------------------------------------------------------------------
	def toUInt16(self):
		"""
		Returns the unsigned 16-bit integer value of this PySide.QtScript.QScriptValue , using the conversion rules described in ECMA-262 section 9.7, ToUint16.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toUInt16()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def toUInt32(self):
		"""
		Returns the unsigned 32-bit integer value of this PySide.QtScript.QScriptValue , using the conversion rules described in ECMA-262 section 9.6, ToUint32.
		Note that if this PySide.QtScript.QScriptValue is an object, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).toUInt32()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def toVariant(self):
		"""
		Returns the PySide.QtCore.QVariant value of this PySide.QtScript.QScriptValue , if it can be converted to a PySide.QtCore.QVariant ; otherwise returns an invalid PySide.QtCore.QVariant
		The conversion is performed according to the following table:
		"""
		res = super(QScriptValue,self).toVariant()
		return res
	#----------------------------------------------------------------------
	def call(self,*args,**kwargs):
		"""
		call(thisObject,arguments)
			thisObject=QtScript.QScriptValue
			arguments=QtScript.QScriptValue

		call(thisObject=None,args=None)
			thisObject=QtScript.QScriptValue
			args=unKnown

		Calls this PySide.QtScript.QScriptValue as a function, using thisObject as the this object in the function call, and passing ``arguments` as arguments to the function
		Returns the value returned from the function.
		If this PySide.QtScript.QScriptValue is not a function, PySide.QtScript.QScriptValue.call() does nothing and returns an invalid PySide.QtScript.QScriptValue .
		arguments can be an arguments object, an array, null or undefined; any other type will cause a TypeError to be thrown.
		Note that if thisObject is not an object, the global object (see QScriptEngine.globalObject() ) will be used as the `this object.
		One common usage of this function is to forward native function calls to another function:
		"""
		res = super(QScriptValue,self).call(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def construct(self,*args,**kwargs):
		"""
		construct(args=None)
			args=unKnown

		construct(arguments)
			arguments=QtScript.QScriptValue


		"""
		res = super(QScriptValue,self).construct(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def equals(self,other):
		"""
		equals(other)
			other=QtScript.QScriptValue

		Returns true if this PySide.QtScript.QScriptValue is equal to other , otherwise returns false
		The comparison follows the behavior described in ECMA-262 section 11.9.3, The Abstract Equality Comparison Algorithm.
		This function can return true even if the type of this PySide.QtScript.QScriptValue is different from the type of the other value; i.e
		the comparison is not strict
		For example, comparing the number 9 to the string 9 returns true; comparing an undefined value to a null value returns true; comparing a Number object whose primitive value is 6 to a String object whose primitive value is 6 returns true; and comparing the number 1 to the boolean value true returns true
		If you want to perform a comparison without such implicit value conversion, use PySide.QtScript.QScriptValue.strictlyEquals() .
		Note that if this PySide.QtScript.QScriptValue or the other value are objects, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).equals(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def instanceOf(self,other):
		"""
		instanceOf(other)
			other=QtScript.QScriptValue

		Returns true if this PySide.QtScript.QScriptValue is an instance of other ; otherwise returns false.
		This PySide.QtScript.QScriptValue is considered to be an instance of other if other is a function and the value of the prototype property of other is in the prototype chain of this PySide.QtScript.QScriptValue .
		"""
		res = super(QScriptValue,self).instanceOf(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lessThan(self,other):
		"""
		lessThan(other)
			other=QtScript.QScriptValue

		Returns true if this PySide.QtScript.QScriptValue is less than other , otherwise returns false
		The comparison follows the behavior described in ECMA-262 section 11.8.5, The Abstract Relational Comparison Algorithm.
		Note that if this PySide.QtScript.QScriptValue or the other value are objects, calling this function has side effects on the script engine, since the engine will call the objects valueOf() function (and possibly PySide.QtScript.QScriptValue.toString() ) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).
		"""
		res = super(QScriptValue,self).lessThan(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def property(self,*args,**kwargs):
		"""
		property(arrayIndex,mode=None)
			arrayIndex=QtCore.quint32
			mode=QtScript.QScriptValue.ResolveFlags

		property(name,mode=None)
			name=unicode
			mode=QtScript.QScriptValue.ResolveFlags

		property(name,mode=None)
			name=QtScript.QScriptString
			mode=QtScript.QScriptValue.ResolveFlags

		This is an overloaded function.
		Returns the property at the given arrayIndex , using the given mode to resolve the property.
		This function is provided for convenience and performance when working with array objects.
		If this PySide.QtScript.QScriptValue is not an Array object, this function behaves as if PySide.QtScript.QScriptValue.property() was called with the string representation of arrayIndex .
		"""
		res = super(QScriptValue,self).property(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def propertyFlags(self,*args,**kwargs):
		"""
		propertyFlags(name,mode=None)
			name=unicode
			mode=QtScript.QScriptValue.ResolveFlags

		propertyFlags(name,mode=None)
			name=QtScript.QScriptString
			mode=QtScript.QScriptValue.ResolveFlags

		Returns the flags of the property with the given name , using the given mode to resolve the property.
		"""
		res = super(QScriptValue,self).propertyFlags(*args,**kwargs)
		isinstance(res,QtScript.QScriptValue.PropertyFlags)
		return res
	#----------------------------------------------------------------------
	def setData(self,data):
		"""
		setData(data)
			data=QtScript.QScriptValue

		Sets the internal data of this PySide.QtScript.QScriptValue object
		You can use this function to set object-specific data that wont be directly accessible to scripts, but may be retrieved in C++ using the PySide.QtScript.QScriptValue.data() function.
		"""
		res = super(QScriptValue,self).setData(data)
		return res
	#----------------------------------------------------------------------
	def setProperty(self,*args,**kwargs):
		"""
		setProperty(name,value,flags=None)
			name=unicode
			value=QtScript.QScriptValue
			flags=QtScript.QScriptValue.PropertyFlags

		setProperty(arrayIndex,value,flags=None)
			arrayIndex=QtCore.quint32
			value=QtScript.QScriptValue
			flags=QtScript.QScriptValue.PropertyFlags

		setProperty(name,value,flags=None)
			name=QtScript.QScriptString
			value=QtScript.QScriptValue
			flags=QtScript.QScriptValue.PropertyFlags

		Sets the value of this PySide.QtScript.QScriptValue s property with the given name to the given value .
		If this PySide.QtScript.QScriptValue is not an object, this function does nothing.
		If this PySide.QtScript.QScriptValue does not already have a property with name name , a new property is created; the given flags then specify how this property may be accessed by script code.
		If value is invalid, the property is removed.
		If the property is implemented using a setter function (i.e
		has the PropertySetter flag set), calling PySide.QtScript.QScriptValue.setProperty() has side-effects on the script engine, since the setter function will be called with the given value as argument (possibly resulting in an uncaught script exception).
		Note that you cannot specify custom getter or setter functions for built-in properties, such as the length property of Array objects or meta properties of PySide.QtCore.QObject objects.
		"""
		res = super(QScriptValue,self).setProperty(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPrototype(self,prototype):
		"""
		setPrototype(prototype)
			prototype=QtScript.QScriptValue

		If this PySide.QtScript.QScriptValue is an object, sets the internal prototype (__proto__ property) of this object to be prototype ; otherwise does nothing.
		The internal prototype should not be confused with the public property with name prototype; the public prototype is usually only set on functions that act as constructors.
		"""
		res = super(QScriptValue,self).setPrototype(prototype)
		return res
	#----------------------------------------------------------------------
	def setScope(self,scope):
		"""
		setScope(scope)
			scope=QtScript.QScriptValue


		"""
		res = super(QScriptValue,self).setScope(scope)
		return res
	#----------------------------------------------------------------------
	def setScriptClass(self,scriptClass):
		"""
		setScriptClass(scriptClass)
			scriptClass=QtScript.QScriptClass

		Sets the custom script class of this script object to scriptClass
		This can be used to promote a plain script object (e.g
		created by the new operator in a script, or by QScriptEngine.newObject() in C++) to an object of a custom type.
		If scriptClass is 0, the object will be demoted to a plain script object.
		"""
		res = super(QScriptValue,self).setScriptClass(scriptClass)
		return res
	#----------------------------------------------------------------------
	def strictlyEquals(self,other):
		"""
		strictlyEquals(other)
			other=QtScript.QScriptValue

		Returns true if this PySide.QtScript.QScriptValue is equal to other using strict comparison (no conversion), otherwise returns false
		The comparison follows the behavior described in ECMA-262 section 11.9.6, The Strict Equality Comparison Algorithm.
		If the type of this PySide.QtScript.QScriptValue is different from the type of the other value, this function returns false
		If the types are equal, the result depends on the type, as shown in the following table:
		"""
		res = super(QScriptValue,self).strictlyEquals(other)
		isinstance(res,bool)
		return res
