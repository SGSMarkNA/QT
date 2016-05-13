from PySide import QtGui, QtCore

class QXmlAttributes(QtXml.QXmlAttributes):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlAttributes,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the list of attributes.
		"""
		res = super(QXmlAttributes,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of attributes in the list
		This function is equivalent to PySide.QtXml.QXmlAttributes.length() .
		"""
		res = super(QXmlAttributes,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the number of attributes in the list.
		"""
		res = super(QXmlAttributes,self).length()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def append(self,qName,uri,localPart,value):
		"""
		append(qName,uri,localPart,value)
			qName=unicode
			uri=unicode
			localPart=unicode
			value=unicode

		Appends a new attribute entry to the list of attributes
		The qualified name of the attribute is qName , the namespace URI is uri and the local name is localPart
		The value of the attribute is value .
		"""
		res = super(QXmlAttributes,self).append(qName,uri,localPart,value)
		return res
	#----------------------------------------------------------------------
	def index(self,*args,**kwargs):
		"""
		index(qName)
			qName=unicode

		index(uri,localPart)
			uri=unicode
			localPart=unicode

		Looks up the index of an attribute by the qualified name qName .
		Returns the index of the attribute or -1 if it wasnt found.
		"""
		res = super(QXmlAttributes,self).index(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def localName(self,index):
		"""
		localName(index)
			index=QtCore.int

		Looks up an attributes local name for the attribute at position index
		If no namespace processing is done, the local name is an empty string.
		"""
		res = super(QXmlAttributes,self).localName(index)
		return res
	#----------------------------------------------------------------------
	def qName(self,index):
		"""
		qName(index)
			index=QtCore.int

		Looks up an attributes XML 1.0 qualified name for the attribute at position index .
		"""
		res = super(QXmlAttributes,self).qName(index)
		return res
	#----------------------------------------------------------------------
	def type(self,*args,**kwargs):
		"""
		type(index)
			index=QtCore.int

		type(uri,localName)
			uri=unicode
			localName=unicode

		type(qName)
			qName=unicode

		Looks up an attributes type for the attribute at position index .
		Currently only CDATA is returned.
		"""
		res = super(QXmlAttributes,self).type(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def uri(self,index):
		"""
		uri(index)
			index=QtCore.int

		Looks up an attributes namespace URI for the attribute at position index
		If no namespace processing is done or if the attribute has no namespace, the namespace URI is an empty string.
		"""
		res = super(QXmlAttributes,self).uri(index)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(qName)
			qName=unicode

		value(uri,localName)
			uri=unicode
			localName=unicode

		value(index)
			index=QtCore.int

		This is an overloaded function.
		Returns an attributes value for the qualified name qName , or an empty string if no attribute exists for the name given.
		"""
		res = super(QXmlAttributes,self).value(*args,**kwargs)
		return res
