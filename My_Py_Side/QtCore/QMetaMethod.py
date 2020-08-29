from PySide import QtGui, QtCore

class QMetaMethod(QtCore.QMetaMethod):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMetaMethod,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def access(self):
		"""
		Returns the access specification of this method (private, protected, or public).
		Signals are always protected, meaning that you can only emit them from the class or from a subclass.
		"""
		res = super(QMetaMethod,self).access()
		isinstance(res,QtCore.QMetaMethod.Access)
		return res
	#----------------------------------------------------------------------
	def enclosingMetaObject(self):
		"""

		"""
		res = super(QMetaMethod,self).enclosingMetaObject()
		isinstance(res,QtCore.QMetaObject)
		return res
	#----------------------------------------------------------------------
	def methodIndex(self):
		"""
		Returns this methods index.
		"""
		res = super(QMetaMethod,self).methodIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def methodType(self):
		"""
		Returns the type of this method (signal, slot, or method).
		"""
		res = super(QMetaMethod,self).methodType()
		isinstance(res,QtCore.QMetaMethod.MethodType)
		return res
	#----------------------------------------------------------------------
	def parameterNames(self):
		"""
		Returns a list of parameter names.
		"""
		res = super(QMetaMethod,self).parameterNames()
		return res
	#----------------------------------------------------------------------
	def parameterTypes(self):
		"""
		Returns a list of parameter types.
		"""
		res = super(QMetaMethod,self).parameterTypes()
		return res
	#----------------------------------------------------------------------
	def signature(self):
		"""
		Returns the signature of this method (e.g., setValue(double) ).
		"""
		res = super(QMetaMethod,self).signature()
		return res
	#----------------------------------------------------------------------
	def tag(self):
		"""
		Returns the tag associated with this method.
		Tags are special macros recognized by moc that make it possible to add extra information about a method
		For the moment, moc doesnt support any special tags.
		"""
		res = super(QMetaMethod,self).tag()
		return res
	#----------------------------------------------------------------------
	def typeName(self):
		"""
		Returns the return type of this method, or an empty string if the return type is void .
		"""
		res = super(QMetaMethod,self).typeName()
		return res
	#----------------------------------------------------------------------
	def invoke(self,*args,**kwargs):
		"""
		invoke(object,connectionType,val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None)
			object=QtCore.QObject
			connectionType=QtCore.Qt.ConnectionType
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

		invoke(object,connectionType,returnValue,val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None)
			object=QtCore.QObject
			connectionType=QtCore.Qt.ConnectionType
			returnValue=QtCore.QGenericReturnArgument
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

		invoke(object,returnValue,val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None)
			object=QtCore.QObject
			returnValue=QtCore.QGenericReturnArgument
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

		invoke(object,val0=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None)
			object=QtCore.QObject
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


		"""
		res = super(QMetaMethod,self).invoke(*args,**kwargs)
		isinstance(res,bool)
		return res
