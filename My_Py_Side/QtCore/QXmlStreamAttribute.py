from PySide import QtGui, QtCore

class QXmlStreamAttribute(QtCore.QXmlStreamAttribute):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamAttribute,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isDefault(self):
		"""
		Returns true if the parser added this attribute with a default value following an ATTLIST declaration in the DTD; otherwise returns false.
		"""
		res = super(QXmlStreamAttribute,self).isDefault()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the attributes local name.
		"""
		res = super(QXmlStreamAttribute,self).name()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def namespaceUri(self):
		"""
		Returns the attributes resolved namespaceUri, or an empty string reference if the attribute does not have a defined namespace.
		"""
		res = super(QXmlStreamAttribute,self).namespaceUri()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		Returns the attributes namespace prefix.
		"""
		res = super(QXmlStreamAttribute,self).prefix()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def qualifiedName(self):
		"""
		Returns the attributes qualified name.
		A qualified name is the raw name of an attribute in the XML data
		It consists of the namespace PySide.QtCore.QXmlStreamAttribute.prefix() , followed by colon, followed by the attributes local PySide.QtCore.QXmlStreamAttribute.name()
		Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldnt use PySide.QtCore.QXmlStreamAttribute.qualifiedName() , but the resolved PySide.QtCore.QXmlStreamAttribute.namespaceUri() and the attributes local PySide.QtCore.QXmlStreamAttribute.name() .
		"""
		res = super(QXmlStreamAttribute,self).qualifiedName()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the attributes value.
		"""
		res = super(QXmlStreamAttribute,self).value()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QXmlStreamAttribute

		Compares this attribute with other and returns true if they are not equal; otherwise returns false.
		"""
		res = super(QXmlStreamAttribute,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QXmlStreamAttribute

		Compares this attribute with other and returns true if they are equal; otherwise returns false.
		"""
		res = super(QXmlStreamAttribute,self).__eq__(other)
		isinstance(res,bool)
		return res
