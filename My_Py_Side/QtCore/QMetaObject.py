from PySide import QtGui, QtCore

class QMetaObject(QtCore.QMetaObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMetaObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def classInfoCount(self):
		"""
		Returns the number of items of class information in this class.
		"""
		res = super(QMetaObject,self).classInfoCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def classInfoOffset(self):
		"""
		Returns the class information offset for this class; i.e
		the index position of this classs first class information item.
		If the class has no superclasses with class information, the offset is 0; otherwise the offset is the sum of all the class information items in the classs superclasses.
		"""
		res = super(QMetaObject,self).classInfoOffset()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def className(self):
		"""
		Returns the class name.
		"""
		res = super(QMetaObject,self).className()
		return res
	#----------------------------------------------------------------------
	def constructorCount(self):
		"""
		Returns the number of constructors in this class.
		"""
		res = super(QMetaObject,self).constructorCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def enumeratorCount(self):
		"""
		Returns the number of enumerators in this class.
		"""
		res = super(QMetaObject,self).enumeratorCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def enumeratorOffset(self):
		"""
		Returns the enumerator offset for this class; i.e
		the index position of this classs first enumerator.
		If the class has no superclasses with enumerators, the offset is 0; otherwise the offset is the sum of all the enumerators in the classs superclasses.
		"""
		res = super(QMetaObject,self).enumeratorOffset()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def methodCount(self):
		"""
		Returns the number of methods in this class, including the number of properties provided by each base class
		These include signals and slots as well as normal member functions.
		Use code like the following to obtain a PySide.QtCore.QStringList containing the methods specific to a given class:
		"""
		res = super(QMetaObject,self).methodCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def methodOffset(self):
		"""
		Returns the method offset for this class; i.e
		the index position of this classs first member function.
		The offset is the sum of all the methods in the classs superclasses (which is always positive since PySide.QtCore.QObject has the deleteLater() slot and a destroyed() signal).
		"""
		res = super(QMetaObject,self).methodOffset()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def propertyCount(self):
		"""
		Returns the number of properties in this class, including the number of properties provided by each base class.
		Use code like the following to obtain a PySide.QtCore.QStringList containing the properties specific to a given class:
		"""
		res = super(QMetaObject,self).propertyCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def propertyOffset(self):
		"""
		Returns the property offset for this class; i.e
		the index position of this classs first property.
		The offset is the sum of all the properties in the classs superclasses (which is always positive since PySide.QtCore.QObject has the name() property).
		"""
		res = super(QMetaObject,self).propertyOffset()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def superClass(self):
		"""
		Returns the meta-object of the superclass, or 0 if there is no such object.
		"""
		res = super(QMetaObject,self).superClass()
		isinstance(res,QtCore.QMetaObject)
		return res
	#----------------------------------------------------------------------
	def userProperty(self):
		"""
		Returns the property that has the USER flag set to true.
		"""
		res = super(QMetaObject,self).userProperty()
		isinstance(res,QtCore.QMetaProperty)
		return res
	#----------------------------------------------------------------------
	def cast(self,obj):
		"""
		cast(obj)
			obj=QtCore.QObject

		Returns obj if object obj inherits from this meta-object; otherwise returns 0.
		"""
		res = super(QMetaObject,self).cast(obj)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def classInfo(self,index):
		"""
		classInfo(index)
			index=QtCore.int

		Returns the meta-data for the item of class information with the given index .
		Example:
		"""
		res = super(QMetaObject,self).classInfo(index)
		isinstance(res,QtCore.QMetaClassInfo)
		return res
	#----------------------------------------------------------------------
	def constructor(self,index):
		"""
		constructor(index)
			index=QtCore.int

		Returns the meta-data for the constructor with the given index .
		"""
		res = super(QMetaObject,self).constructor(index)
		isinstance(res,QtCore.QMetaMethod)
		return res
	#----------------------------------------------------------------------
	def enumerator(self,index):
		"""
		enumerator(index)
			index=QtCore.int

		Returns the meta-data for the enumerator with the given index .
		"""
		res = super(QMetaObject,self).enumerator(index)
		isinstance(res,QtCore.QMetaEnum)
		return res
	#----------------------------------------------------------------------
	def indexOfClassInfo(self,name):
		"""
		indexOfClassInfo(name)
			name=str

		Finds class information item name and returns its index; otherwise returns -1.
		"""
		res = super(QMetaObject,self).indexOfClassInfo(name)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfConstructor(self,constructor):
		"""
		indexOfConstructor(constructor)
			constructor=str

		Finds constructor and returns its index; otherwise returns -1.
		Note that the constructor has to be in normalized form, as returned by PySide.QtCore.QMetaObject.normalizedSignature() .
		"""
		res = super(QMetaObject,self).indexOfConstructor(constructor)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfEnumerator(self,name):
		"""
		indexOfEnumerator(name)
			name=str

		Finds enumerator name and returns its index; otherwise returns -1.
		"""
		res = super(QMetaObject,self).indexOfEnumerator(name)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfMethod(self,method):
		"""
		indexOfMethod(method)
			method=str

		Finds method and returns its index; otherwise returns -1.
		Note that the method has to be in normalized form, as returned by PySide.QtCore.QMetaObject.normalizedSignature() .
		"""
		res = super(QMetaObject,self).indexOfMethod(method)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfProperty(self,name):
		"""
		indexOfProperty(name)
			name=str

		Finds property name and returns its index; otherwise returns -1.
		"""
		res = super(QMetaObject,self).indexOfProperty(name)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfSignal(self,signal):
		"""
		indexOfSignal(signal)
			signal=str

		Finds signal and returns its index; otherwise returns -1.
		This is the same as PySide.QtCore.QMetaObject.indexOfMethod() , except that it will return -1 if the method exists but isnt a signal.
		Note that the signal has to be in normalized form, as returned by PySide.QtCore.QMetaObject.normalizedSignature() .
		"""
		res = super(QMetaObject,self).indexOfSignal(signal)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOfSlot(self,slot):
		"""
		indexOfSlot(slot)
			slot=str

		Finds slot and returns its index; otherwise returns -1.
		This is the same as PySide.QtCore.QMetaObject.indexOfMethod() , except that it will return -1 if the method exists but isnt a slot.
		"""
		res = super(QMetaObject,self).indexOfSlot(slot)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def method(self,index):
		"""
		method(index)
			index=QtCore.int

		Returns the meta-data for the method with the given index .
		"""
		res = super(QMetaObject,self).method(index)
		isinstance(res,QtCore.QMetaMethod)
		return res
	#----------------------------------------------------------------------
	def newInstance(self,val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None):
		"""
		newInstance(val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None)
			val0=QtCore.QGenericArgument
			val1=QtCore.QGenericArgument
			val2=QtCore.QGenericArgument
			val3=QtCore.QGenericArgument
			val4=QtCore.QGenericArgument
			val5=QtCore.QGenericArgument
			val6=QtCore.QGenericArgument
			val7=QtCore.QGenericArgument
			val8=QtCore.QGenericArgument
			val9=QtCore.QGenericArgument

		Constructs a new instance of this class
		You can pass up to ten arguments (val0 , val1 , val2 , val3 , val4 , val5 , val6 , val7 , val8 , and val9 ) to the constructor
		Returns the new object, or 0 if no suitable constructor is available.
		Note that only constructors that are declared with the Q_INVOKABLE() modifier are made available through the meta-object system.
		"""
		res = super(QMetaObject,self).newInstance(val0,val1,val2,val3,val4,val5,val6,val7,val8,val9)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def property(self,index):
		"""
		property(index)
			index=QtCore.int

		Returns the meta-data for the property with the given index
		If no such property exists, a null PySide.QtCore.QMetaProperty is returned.
		"""
		res = super(QMetaObject,self).property(index)
		isinstance(res,QtCore.QMetaProperty)
		return res
