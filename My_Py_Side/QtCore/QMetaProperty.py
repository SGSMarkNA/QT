from PySide import QtGui, QtCore

class QMetaProperty(QtCore.QMetaProperty):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMetaProperty,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def enumerator(self):
		"""
		Returns the enumerator if this propertys type is an enumerator type; otherwise the returned value is undefined.
		"""
		res = super(QMetaProperty,self).enumerator()
		isinstance(res,QtCore.QMetaEnum)
		return res
	#----------------------------------------------------------------------
	def hasNotifySignal(self):
		"""
		Returns true if this property has a corresponding change notify signal; otherwise returns false.
		"""
		res = super(QMetaProperty,self).hasNotifySignal()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasStdCppSet(self):
		"""
		Returns true if the property has a C++ setter function that follows Qts standard name / setName pattern
		Designer and uic query PySide.QtCore.QMetaProperty.hasStdCppSet() in order to avoid expensive QObject.setProperty() calls
		All properties in Qt [should] follow this pattern.
		"""
		res = super(QMetaProperty,self).hasStdCppSet()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isConstant(self):
		"""
		Returns true if the property is constant; otherwise returns false.
		A property is constant if the Q_PROPERTY() s CONSTANT attribute is set.
		"""
		res = super(QMetaProperty,self).isConstant()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEnumType(self):
		"""
		Returns true if the propertys type is an enumeration value; otherwise returns false.
		"""
		res = super(QMetaProperty,self).isEnumType()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isFinal(self):
		"""
		Returns true if the property is final; otherwise returns false.
		A property is final if the Q_PROPERTY() s FINAL attribute is set.
		"""
		res = super(QMetaProperty,self).isFinal()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isFlagType(self):
		"""
		Returns true if the propertys type is an enumeration value that is used as a flag; otherwise returns false.
		Flags can be combined using the OR operator
		A flag type is implicitly also an enum type.
		"""
		res = super(QMetaProperty,self).isFlagType()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadable(self):
		"""
		Returns true if this property is readable; otherwise returns false.
		"""
		res = super(QMetaProperty,self).isReadable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isResettable(self):
		"""
		Returns true if this property can be reset to a default value; otherwise returns false.
		"""
		res = super(QMetaProperty,self).isResettable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this property is valid (readable); otherwise returns false.
		"""
		res = super(QMetaProperty,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if this property is writable; otherwise returns false.
		"""
		res = super(QMetaProperty,self).isWritable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns this propertys name.
		"""
		res = super(QMetaProperty,self).name()
		return res
	#----------------------------------------------------------------------
	def notifySignal(self):
		"""
		Returns the PySide.QtCore.QMetaMethod instance of the property change notifying signal if one was specified, otherwise returns an invalid PySide.QtCore.QMetaMethod .
		"""
		res = super(QMetaProperty,self).notifySignal()
		isinstance(res,QtCore.QMetaMethod)
		return res
	#----------------------------------------------------------------------
	def notifySignalIndex(self):
		"""
		Returns the index of the property change notifying signal if one was specified, otherwise returns -1.
		"""
		res = super(QMetaProperty,self).notifySignalIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def propertyIndex(self):
		"""
		Returns this propertys index.
		"""
		res = super(QMetaProperty,self).propertyIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns this propertys type
		The return value is one of the values of the QVariant.Type enumeration.
		"""
		res = super(QMetaProperty,self).type()
		isinstance(res,QtCore.QVariant::Type)
		return res
	#----------------------------------------------------------------------
	def typeName(self):
		"""
		Returns the name of this propertys type.
		"""
		res = super(QMetaProperty,self).typeName()
		return res
	#----------------------------------------------------------------------
	def userType(self):
		"""
		Returns this propertys user type
		The return value is one of the values that are registered with QMetaType , or 0 if the type is not registered.
		"""
		res = super(QMetaProperty,self).userType()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isDesignable(self,obj=None):
		"""
		isDesignable(obj=None)
			obj=QtCore.QObject

		Returns true if this property is designable for the given object ; otherwise returns false.
		If no object is given, the function returns false if the Q_PROPERTY() s DESIGNABLE attribute is false; otherwise returns true (if the attribute is true or is a function or expression).
		"""
		res = super(QMetaProperty,self).isDesignable(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEditable(self,obj=None):
		"""
		isEditable(obj=None)
			obj=QtCore.QObject

		Returns true if the property is editable for the given object ; otherwise returns false.
		If no object is given, the function returns false if the Q_PROPERTY() s EDITABLE attribute is false; otherwise returns true (if the attribute is true or is a function or expression).
		"""
		res = super(QMetaProperty,self).isEditable(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isScriptable(self,obj=None):
		"""
		isScriptable(obj=None)
			obj=QtCore.QObject

		Returns true if the property is scriptable for the given object ; otherwise returns false.
		If no object is given, the function returns false if the Q_PROPERTY() s SCRIPTABLE attribute is false; otherwise returns true (if the attribute is true or is a function or expression).
		"""
		res = super(QMetaProperty,self).isScriptable(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isStored(self,obj=None):
		"""
		isStored(obj=None)
			obj=QtCore.QObject

		Returns true if the property is stored for object ; otherwise returns false.
		If no object is given, the function returns false if the Q_PROPERTY() s STORED attribute is false; otherwise returns true (if the attribute is true or is a function or expression).
		"""
		res = super(QMetaProperty,self).isStored(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isUser(self,obj=None):
		"""
		isUser(obj=None)
			obj=QtCore.QObject

		Returns true if this property is designated as the USER property, i.e., the one that the user can edit for object or that is significant in some other way
		Otherwise it returns false
		e.g., the text property is the USER editable property of a PySide.QtGui.QLineEdit .
		If object is null, the function returns false if the Q_PROPERTY() s USER attribute is false
		Otherwise it returns true.
		"""
		res = super(QMetaProperty,self).isUser(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def read(self,obj):
		"""
		read(obj)
			obj=QtCore.QObject

		Reads the propertys value from the given object
		Returns the value if it was able to read it; otherwise returns an invalid variant.
		"""
		res = super(QMetaProperty,self).read(obj)
		return res
	#----------------------------------------------------------------------
	def reset(self,obj):
		"""
		reset(obj)
			obj=QtCore.QObject

		Resets the property for the given object with a reset method
		Returns true if the reset worked; otherwise returns false.
		Reset methods are optional; only a few properties support them.
		"""
		res = super(QMetaProperty,self).reset(obj)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def write(self,obj,value):
		"""
		write(obj,value)
			obj=QtCore.QObject
			value=object

		Writes value as the propertys value to the given object
		Returns true if the write succeeded; otherwise returns false.
		"""
		res = super(QMetaProperty,self).write(obj,value)
		isinstance(res,QtCore.bool)
		return res
