from PySide import QtGui, QtCore

class QDomDocument(QtXml.QDomDocument):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomDocument,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def createDocumentFragment(self):
		"""
		Creates a new document fragment, that can be used to hold parts of the document, e.g
		when doing complex manipulations of the document tree.
		"""
		res = super(QDomDocument,self).createDocumentFragment()
		isinstance(res,QtXml.QDomDocumentFragment)
		return res
	#----------------------------------------------------------------------
	def doctype(self):
		"""
		Returns the document type of this document.
		"""
		res = super(QDomDocument,self).doctype()
		isinstance(res,QtXml.QDomDocumentType)
		return res
	#----------------------------------------------------------------------
	def documentElement(self):
		"""
		Returns the root element of the document.
		"""
		res = super(QDomDocument,self).documentElement()
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def implementation(self):
		"""
		Returns a PySide.QtXml.QDomImplementation object.
		"""
		res = super(QDomDocument,self).implementation()
		isinstance(res,QtXml.QDomImplementation)
		return res
	#----------------------------------------------------------------------
	def createAttribute(self,name):
		"""
		createAttribute(name)
			name=unicode

		Creates a new attribute called name that can be inserted into an element, e.g
		using QDomElement.setAttributeNode() .
		If name is not a valid XML name, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createAttribute(name)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def createAttributeNS(self,nsURI,qName):
		"""
		createAttributeNS(nsURI,qName)
			nsURI=unicode
			qName=unicode

		Creates a new attribute with namespace support that can be inserted into an element
		The name of the attribute is qName and the namespace URI is nsURI
		This function also sets QDomNode.prefix() and QDomNode.localName() to appropriate values (depending on qName ).
		If qName is not a valid XML name, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createAttributeNS(nsURI,qName)
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def createCDATASection(self,data):
		"""
		createCDATASection(data)
			data=unicode

		Creates a new CDATA section for the string value that can be inserted into the document, e.g
		using QDomNode.appendChild() .
		If value contains characters which cannot be stored in a CDATA section, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createCDATASection(data)
		isinstance(res,QtXml.QDomCDATASection)
		return res
	#----------------------------------------------------------------------
	def createComment(self,data):
		"""
		createComment(data)
			data=unicode

		Creates a new comment for the string value that can be inserted into the document, e.g
		using QDomNode.appendChild() .
		If value contains characters which cannot be stored in an XML comment, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createComment(data)
		isinstance(res,QtXml.QDomComment)
		return res
	#----------------------------------------------------------------------
	def createElement(self,tagName):
		"""
		createElement(tagName)
			tagName=unicode

		Creates a new element called tagName that can be inserted into the DOM tree, e.g
		using QDomNode.appendChild() .
		If tagName is not a valid XML name, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		QDomNode.insertAfter()
		"""
		res = super(QDomDocument,self).createElement(tagName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def createElementNS(self,nsURI,qName):
		"""
		createElementNS(nsURI,qName)
			nsURI=unicode
			qName=unicode

		Creates a new element with namespace support that can be inserted into the DOM tree
		The name of the element is qName and the namespace URI is nsURI
		This function also sets QDomNode.prefix() and QDomNode.localName() to appropriate values (depending on qName ).
		If qName is an empty string, returns a null element regardless of whether the invalid data policy is set.
		"""
		res = super(QDomDocument,self).createElementNS(nsURI,qName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def createEntityReference(self,name):
		"""
		createEntityReference(name)
			name=unicode

		Creates a new entity reference called name that can be inserted into the document, e.g
		using QDomNode.appendChild() .
		If name is not a valid XML name, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createEntityReference(name)
		isinstance(res,QtXml.QDomEntityReference)
		return res
	#----------------------------------------------------------------------
	def createProcessingInstruction(self,target,data):
		"""
		createProcessingInstruction(target,data)
			target=unicode
			data=unicode

		Creates a new processing instruction that can be inserted into the document, e.g
		using QDomNode.appendChild()
		This function sets the target for the processing instruction to target and the data to data .
		If target is not a valid XML name, or data if contains characters which cannot appear in a processing instruction, the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createProcessingInstruction(target,data)
		isinstance(res,QtXml.QDomProcessingInstruction)
		return res
	#----------------------------------------------------------------------
	def createTextNode(self,data):
		"""
		createTextNode(data)
			data=unicode

		Creates a text node for the string value that can be inserted into the document tree, e.g
		using QDomNode.appendChild() .
		If value contains characters which cannot be stored as character data of an XML document (even in the form of character references), the behavior of this function is governed by QDomImplementation.InvalidDataPolicy .
		"""
		res = super(QDomDocument,self).createTextNode(data)
		isinstance(res,QtXml.QDomText)
		return res
	#----------------------------------------------------------------------
	def elementById(self,elementId):
		"""
		elementById(elementId)
			elementId=unicode

		Returns the element whose ID is equal to elementId
		If no element with the ID was found, this function returns a null element .
		Since the QDomClasses do not know which attributes are element IDs, this function returns always a null element
		This may change in a future version.
		"""
		res = super(QDomDocument,self).elementById(elementId)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def elementsByTagName(self,tagname):
		"""
		elementsByTagName(tagname)
			tagname=unicode

		Returns a PySide.QtXml.QDomNodeList , that contains all the elements in the document with the name tagname
		The order of the node list is the order they are encountered in a preorder traversal of the element tree.
		"""
		res = super(QDomDocument,self).elementsByTagName(tagname)
		isinstance(res,QtXml.QDomNodeList)
		return res
	#----------------------------------------------------------------------
	def elementsByTagNameNS(self,nsURI,localName):
		"""
		elementsByTagNameNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Returns a PySide.QtXml.QDomNodeList that contains all the elements in the document with the local name localName and a namespace URI of nsURI
		The order of the node list is the order they are encountered in a preorder traversal of the element tree.
		"""
		res = super(QDomDocument,self).elementsByTagNameNS(nsURI,localName)
		isinstance(res,QtXml.QDomNodeList)
		return res
	#----------------------------------------------------------------------
	def importNode(self,importedNode,deep):
		"""
		importNode(importedNode,deep)
			importedNode=QtXml.QDomNode
			deep=QtCore.bool

		Imports the node importedNode from another document to this document
		importedNode remains in the original document; this function creates a copy that can be used within this document.
		This function returns the imported node that belongs to this document
		The returned node has no parent
		It is not possible to import PySide.QtXml.QDomDocument and PySide.QtXml.QDomDocumentType nodes
		In those cases this function returns a null node .
		If deep is true, this function imports not only the node importedNode but its whole subtree; if it is false, only the importedNode is imported
		The argument deep has no effect on PySide.QtXml.QDomAttr and PySide.QtXml.QDomEntityReference nodes, since the descendants of PySide.QtXml.QDomAttr nodes are always imported and those of PySide.QtXml.QDomEntityReference nodes are never imported.
		The behavior of this function is slightly different depending on the node types:
		QDomNode.insertAfter() QDomNode.replaceChild() QDomNode.removeChild() QDomNode.appendChild()
		"""
		res = super(QDomDocument,self).importNode(importedNode,deep)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def setContent(self,*args,**kwargs):
		"""
		setContent(text,namespaceProcessing)
			text=QtCore.QByteArray
			namespaceProcessing=QtCore.bool

		setContent(text)
			text=unicode

		setContent(text,namespaceProcessing)
			text=unicode
			namespaceProcessing=QtCore.bool

		setContent(text)
			text=QtCore.QByteArray

		setContent(dev,namespaceProcessing)
			dev=QtCore.QIODevice
			namespaceProcessing=QtCore.bool

		setContent(dev)
			dev=QtCore.QIODevice

		setContent(source,namespaceProcessing)
			source=QtXml.QXmlInputSource
			namespaceProcessing=QtCore.bool

		setContent(source,reader)
			source=QtXml.QXmlInputSource
			reader=QtXml.QXmlReader

		This function parses the XML document from the byte array data and sets it as the content of the document
		It tries to detect the encoding of the document as required by the XML specification.
		If namespaceProcessing is true, the parser recognizes namespaces in the XML file and sets the prefix name, local name and namespace URI to appropriate values
		If namespaceProcessing is false, the parser does no namespace processing when it reads the XML file.
		If a parse error occurs, this function returns false and the error message is placed in *errorMsg , the line number in *errorLine and the column number in *errorColumn (unless the associated pointer is set to 0); otherwise this function returns true
		The various error messages are described in the PySide.QtXml.QXmlParseException class documentation
		Note that, if you want to display these error messages to your applications users, they will be displayed in English unless they are explicitly translated.
		If namespaceProcessing is true, the function QDomNode.prefix() returns a string for all elements and attributes
		It returns an empty string if the element or attribute has no prefix.
		Text nodes consisting only of whitespace are stripped and wont appear in the PySide.QtXml.QDomDocument
		If this behavior is not desired, one can use the PySide.QtXml.QDomDocument.setContent() overload that allows a PySide.QtXml.QXmlReader to be supplied.
		If namespaceProcessing is false, the functions QDomNode.prefix() , QDomNode.localName() and QDomNode.namespaceURI() return an empty string.
		Entity references are handled as follows:
		QDomNode.prefix() QString.isNull() QString.isEmpty()
		"""
		res = super(QDomDocument,self).setContent(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def toByteArray(self,arg__1=None):
		"""
		toByteArray(arg__1=None)
			arg__1=QtCore.int

		Converts the parsed document back to its textual representation and returns a PySide.QtCore.QByteArray containing the data encoded as UTF-8.
		This function uses indent as the amount of space to indent subelements.
		"""
		res = super(QDomDocument,self).toByteArray(arg__1)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toString(self,arg__1=None):
		"""
		toString(arg__1=None)
			arg__1=QtCore.int

		Converts the parsed document back to its textual representation.
		This function uses indent as the amount of space to indent subelements.
		If indent is -1, no whitespace at all is added.
		"""
		res = super(QDomDocument,self).toString(arg__1)
		return res
