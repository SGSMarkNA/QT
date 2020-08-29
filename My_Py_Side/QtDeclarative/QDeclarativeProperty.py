from PySide import QtGui, QtCore

class QDeclarativeProperty(QtDeclarative.QDeclarativeProperty):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeProperty,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasNotifySignal(self):
		"""
		Returns true if the property has a change notifier signal, otherwise false.
		"""
		res = super(QDeclarativeProperty,self).hasNotifySignal()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def index(self):
		"""
		Return the Qt metaobject index of the property.
		"""
		res = super(QDeclarativeProperty,self).index()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isDesignable(self):
		"""
		Returns true if the property is designable, otherwise false.
		"""
		res = super(QDeclarativeProperty,self).isDesignable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isProperty(self):
		"""
		Returns true if this PySide.QtDeclarative.QDeclarativeProperty represents a regular Qt property.
		"""
		res = super(QDeclarativeProperty,self).isProperty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isResettable(self):
		"""
		Returns true if the property is resettable, otherwise false.
		"""
		res = super(QDeclarativeProperty,self).isResettable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSignalProperty(self):
		"""
		Returns true if this PySide.QtDeclarative.QDeclarativeProperty represents a QML signal property.
		"""
		res = super(QDeclarativeProperty,self).isSignalProperty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the PySide.QtDeclarative.QDeclarativeProperty refers to a valid property, otherwise false.
		"""
		res = super(QDeclarativeProperty,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if the property is writable, otherwise false.
		"""
		res = super(QDeclarativeProperty,self).isWritable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def method(self):
		"""
		Return the PySide.QtCore.QMetaMethod for this property if it is a SignalProperty , otherwise returns an invalid PySide.QtCore.QMetaMethod .
		"""
		res = super(QDeclarativeProperty,self).method()
		isinstance(res,QtCore.QMetaMethod)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Return the name of this QML property.
		"""
		res = super(QDeclarativeProperty,self).name()
		return res
	#----------------------------------------------------------------------
	def needsNotifySignal(self):
		"""
		Returns true if the property needs a change notifier signal for bindings to remain upto date, false otherwise.
		Some properties, such as attached properties or those whose value never changes, do not require a change notifier.
		"""
		res = super(QDeclarativeProperty,self).needsNotifySignal()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def object(self):
		"""
		Returns the PySide.QtDeclarative.QDeclarativeProperty s PySide.QtCore.QObject .
		"""
		res = super(QDeclarativeProperty,self).object()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def property(self):
		"""
		Returns the Qt property associated with this QML property.
		"""
		res = super(QDeclarativeProperty,self).property()
		isinstance(res,QtCore.QMetaProperty)
		return res
	#----------------------------------------------------------------------
	def propertyType(self):
		"""
		Returns the PySide.QtCore.QVariant type of the property, or QVariant.Invalid if the property has no PySide.QtCore.QVariant type.
		"""
		res = super(QDeclarativeProperty,self).propertyType()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def propertyTypeCategory(self):
		"""
		Returns the property category.
		"""
		res = super(QDeclarativeProperty,self).propertyTypeCategory()
		isinstance(res,QtDeclarative.QDeclarativeProperty.PropertyTypeCategory)
		return res
	#----------------------------------------------------------------------
	def propertyTypeName(self):
		"""
		Returns the type name of the property, or 0 if the property has no type name.
		"""
		res = super(QDeclarativeProperty,self).propertyTypeName()
		return res
	#----------------------------------------------------------------------
	def read(self):
		"""
		Returns the property value.
		"""
		res = super(QDeclarativeProperty,self).read()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the property and returns true if the property is resettable
		If the property is not resettable, nothing happens and false is returned.
		"""
		res = super(QDeclarativeProperty,self).reset()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of the property.
		"""
		res = super(QDeclarativeProperty,self).type()
		isinstance(res,QtDeclarative.QDeclarativeProperty.Type)
		return res
	#----------------------------------------------------------------------
	def connectNotifySignal(self,*args,**kwargs):
		"""
		connectNotifySignal(dest,method)
			dest=QtCore.QObject
			method=QtCore.int

		connectNotifySignal(dest,slot)
			dest=QtCore.QObject
			slot=str

		Connects the propertys change notifier signal to the specified method of the dest object and returns true
		Returns false if this metaproperty does not represent a regular Qt property or if it has no change notifier signal, or if the dest object does not have the specified method .
		"""
		res = super(QDeclarativeProperty,self).connectNotifySignal(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtDeclarative.QDeclarativeProperty

		Returns true if other and this PySide.QtDeclarative.QDeclarativeProperty represent the same property.
		"""
		res = super(QDeclarativeProperty,self).__eq__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def write(self,arg__1):
		"""
		write(arg__1)
			arg__1=object

		Sets the property value to value and returns true
		Returns false if the property cant be set because the value is the wrong type, for example.
		"""
		res = super(QDeclarativeProperty,self).write(arg__1)
		isinstance(res,bool)
		return res
