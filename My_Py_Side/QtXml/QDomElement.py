from PySide import QtGui, QtCore

class QDomElement(QtXml.QDomElement):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomElement,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def tagName(self):
		"""
		Returns the tag name of this element
		For an XML element like this:
		the tagname would return img.
		"""
		res = super(QDomElement,self).tagName()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the elements text or an empty string.
		Example:
		The function PySide.QtXml.QDomElement.text() of the PySide.QtXml.QDomElement for the <h1> tag, will return the following text:
		Comments are ignored by this function
		It only evaluates PySide.QtXml.QDomText and PySide.QtXml.QDomCDATASection objects.
		"""
		res = super(QDomElement,self).text()
		return res
	#----------------------------------------------------------------------
	def attribute(self,name,defValue=None):
		"""
		attribute(name,defValue=None)
			name=unicode
			defValue=unicode

		Returns the attribute called name
		If the attribute does not exist defValue is returned.
		"""
		res = super(QDomElement,self).attribute(name,defValue)
		return res
	#----------------------------------------------------------------------
	def attributeNS(self,nsURI,localName,defValue=None):
		"""
		attributeNS(nsURI,localName,defValue=None)
			nsURI=unicode
			localName=unicode
			defValue=unicode

		Returns the attribute with the local name localName and the namespace URI nsURI
		If the attribute does not exist defValue is returned.
		"""
		res = super(QDomElement,self).attributeNS(nsURI,localName,defValue)
		return res
	#----------------------------------------------------------------------
	def attributeNode(self,name):
		"""
		attributeNode(name)
			name=unicode

		Returns the PySide.QtXml.QDomAttr object that corresponds to the attribute called name
		If no such attribute exists a null attribute is returned.
		"""
		res = super(QDomElement,self).attributeNode(name)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def attributeNodeNS(self,nsURI,localName):
		"""
		attributeNodeNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Returns the PySide.QtXml.QDomAttr object that corresponds to the attribute with the local name localName and the namespace URI nsURI
		If no such attribute exists a null attribute is returned.
		"""
		res = super(QDomElement,self).attributeNodeNS(nsURI,localName)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def elementsByTagName(self,tagname):
		"""
		elementsByTagName(tagname)
			tagname=unicode

		Returns a PySide.QtXml.QDomNodeList containing all descendants of this element named tagname encountered during a preorder traversal of the element subtree with this element as its root
		The order of the elements in the returned list is the order they are encountered during the preorder traversal.
		"""
		res = super(QDomElement,self).elementsByTagName(tagname)
		isinstance(res,QtXml.QDomNodeList)
		return res
	#----------------------------------------------------------------------
	def elementsByTagNameNS(self,nsURI,localName):
		"""
		elementsByTagNameNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Returns a PySide.QtXml.QDomNodeList containing all descendants of this element with local name localName and namespace URI nsURI encountered during a preorder traversal of the element subtree with this element as its root
		The order of the elements in the returned list is the order they are encountered during the preorder traversal.
		"""
		res = super(QDomElement,self).elementsByTagNameNS(nsURI,localName)
		isinstance(res,QtXml.QDomNodeList)
		return res
	#----------------------------------------------------------------------
	def hasAttribute(self,name):
		"""
		hasAttribute(name)
			name=unicode

		Returns true if this element has an attribute called name ; otherwise returns false.
		Use PySide.QtXml.QDomElement.hasAttributeNS() to explicitly test for attributes with specific namespaces and names.
		"""
		res = super(QDomElement,self).hasAttribute(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasAttributeNS(self,nsURI,localName):
		"""
		hasAttributeNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Returns true if this element has an attribute with the local name localName and the namespace URI nsURI ; otherwise returns false.
		"""
		res = super(QDomElement,self).hasAttributeNS(nsURI,localName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def removeAttribute(self,name):
		"""
		removeAttribute(name)
			name=unicode

		Removes the attribute called name name from this element.
		"""
		res = super(QDomElement,self).removeAttribute(name)
		return res
	#----------------------------------------------------------------------
	def removeAttributeNS(self,nsURI,localName):
		"""
		removeAttributeNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Removes the attribute with the local name localName and the namespace URI nsURI from this element.
		"""
		res = super(QDomElement,self).removeAttributeNS(nsURI,localName)
		return res
	#----------------------------------------------------------------------
	def removeAttributeNode(self,oldAttr):
		"""
		removeAttributeNode(oldAttr)
			oldAttr=QtXml.QDomAttr

		Removes the attribute oldAttr from the element and returns it.
		"""
		res = super(QDomElement,self).removeAttributeNode(oldAttr)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,*args,**kwargs):
		"""
		setAttribute(name,value)
			name=unicode
			value=QtCore.qulonglong

		setAttribute(name,value)
			name=unicode
			value=QtCore.uint

		setAttribute(name,value)
			name=unicode
			value=QtCore.int

		setAttribute(name,value)
			name=unicode
			value=QtCore.qlonglong

		setAttribute(name,value)
			name=unicode
			value=QtCore.double

		setAttribute(name,value)
			name=unicode
			value=unicode

		setAttribute(name,value)
			name=unicode
			value=QtCore.float

		This is an overloaded function.
		The number is formatted according to the current locale.
		"""
		res = super(QDomElement,self).setAttribute(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeNS(self,*args,**kwargs):
		"""
		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=QtCore.qulonglong

		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=QtCore.uint

		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=QtCore.qlonglong

		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=QtCore.int

		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=QtCore.double

		setAttributeNS(nsURI,qName,value)
			nsURI=unicode
			qName=unicode
			value=unicode

		This is an overloaded function.
		"""
		res = super(QDomElement,self).setAttributeNS(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeNode(self,newAttr):
		"""
		setAttributeNode(newAttr)
			newAttr=QtXml.QDomAttr

		Adds the attribute newAttr to this element.
		If the element has another attribute that has the same name as newAttr , this function replaces that attribute and returns it; otherwise the function returns a null attribute .
		"""
		res = super(QDomElement,self).setAttributeNode(newAttr)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def setAttributeNodeNS(self,newAttr):
		"""
		setAttributeNodeNS(newAttr)
			newAttr=QtXml.QDomAttr

		Adds the attribute newAttr to this element.
		If the element has another attribute that has the same local name and namespace URI as newAttr , this function replaces that attribute and returns it; otherwise the function returns a null attribute .
		"""
		res = super(QDomElement,self).setAttributeNodeNS(newAttr)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def setTagName(self,name):
		"""
		setTagName(name)
			name=unicode

		Sets this elements tag name to name .
		"""
		res = super(QDomElement,self).setTagName(name)
		return res
