from PySide import QtGui, QtCore

class QDomNode(QtXml.QDomNode):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomNode,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def attributes(self):
		"""
		Returns a named node map of all attributes
		Attributes are only provided for PySide.QtXml.QDomElement s.
		Changing the attributes in the map will also change the attributes of this PySide.QtXml.QDomNode .
		"""
		res = super(QDomNode,self).attributes()
		isinstance(res,QtXml.QDomNamedNodeMap)
		return res
	#----------------------------------------------------------------------
	def childNodes(self):
		"""
		Returns a list of all direct child nodes.
		Most often you will call this function on a PySide.QtXml.QDomElement object.
		For example, if the XML document looks like this:
		Then the list of child nodes for the body-element will contain the node created by the &lt;h1&gt; tag and the node created by the &lt;p&gt; tag.
		The nodes in the list are not copied; so changing the nodes in the list will also change the children of this node.
		"""
		res = super(QDomNode,self).childNodes()
		isinstance(res,QtXml.QDomNodeList)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Converts the node into a null node; if it was not a null node before, its type and contents are deleted.
		"""
		res = super(QDomNode,self).clear()
		return res
	#----------------------------------------------------------------------
	def columnNumber(self):
		"""
		For nodes created by QDomDocument.setContent() , this function returns the column number in the XML document where the node was parsed
		Otherwise, -1 is returned.
		"""
		res = super(QDomNode,self).columnNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def firstChild(self):
		"""
		Returns the first child of the node
		If there is no child node, a null node is returned
		Changing the returned node will also change the node in the document tree.
		"""
		res = super(QDomNode,self).firstChild()
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def hasAttributes(self):
		"""
		Returns true if the node has attributes; otherwise returns false.
		"""
		res = super(QDomNode,self).hasAttributes()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasChildNodes(self):
		"""
		Returns true if the node has one or more children; otherwise returns false.
		"""
		res = super(QDomNode,self).hasChildNodes()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isAttr(self):
		"""
		Returns true if the node is an attribute; otherwise returns false.
		If this function returns true, it does not imply that this object is a QDomAttribute; you can get the QDomAttribute with toAttribute().
		"""
		res = super(QDomNode,self).isAttr()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isCDATASection(self):
		"""
		Returns true if the node is a CDATA section; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomCDATASection ; you can get the PySide.QtXml.QDomCDATASection with PySide.QtXml.QDomNode.toCDATASection() .
		"""
		res = super(QDomNode,self).isCDATASection()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isCharacterData(self):
		"""
		Returns true if the node is a character data node; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomCharacterData ; you can get the PySide.QtXml.QDomCharacterData with PySide.QtXml.QDomNode.toCharacterData() .
		"""
		res = super(QDomNode,self).isCharacterData()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isComment(self):
		"""
		Returns true if the node is a comment; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomComment ; you can get the PySide.QtXml.QDomComment with PySide.QtXml.QDomNode.toComment() .
		"""
		res = super(QDomNode,self).isComment()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDocument(self):
		"""
		Returns true if the node is a document; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomDocument ; you can get the PySide.QtXml.QDomDocument with PySide.QtXml.QDomNode.toDocument() .
		"""
		res = super(QDomNode,self).isDocument()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDocumentFragment(self):
		"""
		Returns true if the node is a document fragment; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomDocumentFragment ; you can get the PySide.QtXml.QDomDocumentFragment with PySide.QtXml.QDomNode.toDocumentFragment() .
		"""
		res = super(QDomNode,self).isDocumentFragment()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDocumentType(self):
		"""
		Returns true if the node is a document type; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomDocumentType ; you can get the PySide.QtXml.QDomDocumentType with PySide.QtXml.QDomNode.toDocumentType() .
		"""
		res = super(QDomNode,self).isDocumentType()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isElement(self):
		"""
		Returns true if the node is an element; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomElement ; you can get the PySide.QtXml.QDomElement with PySide.QtXml.QDomNode.toElement() .
		"""
		res = super(QDomNode,self).isElement()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isEntity(self):
		"""
		Returns true if the node is an entity; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomEntity ; you can get the PySide.QtXml.QDomEntity with PySide.QtXml.QDomNode.toEntity() .
		"""
		res = super(QDomNode,self).isEntity()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isEntityReference(self):
		"""
		Returns true if the node is an entity reference; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomEntityReference ; you can get the PySide.QtXml.QDomEntityReference with PySide.QtXml.QDomNode.toEntityReference() .
		"""
		res = super(QDomNode,self).isEntityReference()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNotation(self):
		"""
		Returns true if the node is a notation; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomNotation ; you can get the PySide.QtXml.QDomNotation with PySide.QtXml.QDomNode.toNotation() .
		"""
		res = super(QDomNode,self).isNotation()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this node is null (i.e
		if it has no type or contents); otherwise returns false.
		"""
		res = super(QDomNode,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isProcessingInstruction(self):
		"""
		Returns true if the node is a processing instruction; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomProcessingInstruction ; you can get the QProcessingInstruction with PySide.QtXml.QDomNode.toProcessingInstruction() .
		"""
		res = super(QDomNode,self).isProcessingInstruction()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isText(self):
		"""
		Returns true if the node is a text node; otherwise returns false.
		If this function returns true, it does not imply that this object is a PySide.QtXml.QDomText ; you can get the PySide.QtXml.QDomText with PySide.QtXml.QDomNode.toText() .
		"""
		res = super(QDomNode,self).isText()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastChild(self):
		"""
		Returns the last child of the node
		If there is no child node, a null node is returned
		Changing the returned node will also change the node in the document tree.
		"""
		res = super(QDomNode,self).lastChild()
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		For nodes created by QDomDocument.setContent() , this function returns the line number in the XML document where the node was parsed
		Otherwise, -1 is returned.
		"""
		res = super(QDomNode,self).lineNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def localName(self):
		"""
		If the node uses namespaces, this function returns the local name of the node; otherwise it returns an empty string.
		Only nodes of type ElementNode or AttributeNode can have namespaces
		A namespace must have been specified at creation time; it is not possible to add a namespace afterwards.
		QDomDocument.createAttributeNS()
		"""
		res = super(QDomNode,self).localName()
		return res
	#----------------------------------------------------------------------
	def namespaceURI(self):
		"""
		Returns the namespace URI of this node or an empty string if the node has no namespace URI.
		Only nodes of type ElementNode or AttributeNode can have namespaces
		A namespace URI must be specified at creation time and cannot be changed later.
		QDomDocument.createAttributeNS()
		"""
		res = super(QDomNode,self).namespaceURI()
		return res
	#----------------------------------------------------------------------
	def nextSibling(self):
		"""
		Returns the next sibling in the document tree
		Changing the returned node will also change the node in the document tree.
		If you have XML like this:
		and this PySide.QtXml.QDomNode represents the <p> tag, PySide.QtXml.QDomNode.nextSibling() will return the node representing the <h2> tag.
		"""
		res = super(QDomNode,self).nextSibling()
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def nodeName(self):
		"""
		Returns the name of the node.
		The meaning of the name depends on the subclass:
		"""
		res = super(QDomNode,self).nodeName()
		return res
	#----------------------------------------------------------------------
	def nodeType(self):
		"""
		Returns the type of the node.
		"""
		res = super(QDomNode,self).nodeType()
		isinstance(res,QtXml.QDomNode.NodeType)
		return res
	#----------------------------------------------------------------------
	def nodeValue(self):
		"""
		Returns the value of the node.
		The meaning of the value depends on the subclass:
		All the other subclasses do not have a node value and will return an empty string.
		"""
		res = super(QDomNode,self).nodeValue()
		return res
	#----------------------------------------------------------------------
	def normalize(self):
		"""
		Calling PySide.QtXml.QDomNode.normalize() on an element converts all its children into a standard form
		This means that adjacent PySide.QtXml.QDomText objects will be merged into a single text object ( PySide.QtXml.QDomCDATASection nodes are not merged).
		"""
		res = super(QDomNode,self).normalize()
		return res
	#----------------------------------------------------------------------
	def ownerDocument(self):
		"""
		Returns the document to which this node belongs.
		"""
		res = super(QDomNode,self).ownerDocument()
		isinstance(res,QtXml.QDomDocument)
		return res
	#----------------------------------------------------------------------
	def parentNode(self):
		"""
		Returns the parent node
		If this node has no parent, a null node is returned (i.e
		a node for which PySide.QtXml.QDomNode.isNull() returns true).
		"""
		res = super(QDomNode,self).parentNode()
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		Returns the namespace prefix of the node or an empty string if the node has no namespace prefix.
		Only nodes of type ElementNode or AttributeNode can have namespaces
		A namespace prefix must be specified at creation time
		If a node was created with a namespace prefix, you can change it later with PySide.QtXml.QDomNode.setPrefix() .
		If you create an element or attribute with QDomDocument.createElement() or QDomDocument.createAttribute() , the prefix will be an empty string
		If you use QDomDocument.createElementNS() or QDomDocument.createAttributeNS() instead, the prefix will not be an empty string; but it might be an empty string if the name does not have a prefix.
		QDomDocument.createElementNS() QDomDocument.createAttributeNS()
		"""
		res = super(QDomNode,self).prefix()
		return res
	#----------------------------------------------------------------------
	def previousSibling(self):
		"""
		Returns the previous sibling in the document tree
		Changing the returned node will also change the node in the document tree.
		For example, if you have XML like this:
		and this PySide.QtXml.QDomNode represents the &lt;p&gt; tag, PySide.QtXml.QDomNode.previousSibling() will return the node representing the &lt;h1&gt; tag.
		"""
		res = super(QDomNode,self).previousSibling()
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def toAttr(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomAttr
		If the node is not an attribute, the returned object will be null .
		"""
		res = super(QDomNode,self).toAttr()
		isinstance(res,QtXml.QDomAttr)
		return res
	#----------------------------------------------------------------------
	def toCDATASection(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomCDATASection
		If the node is not a CDATA section, the returned object will be null .
		"""
		res = super(QDomNode,self).toCDATASection()
		isinstance(res,QtXml.QDomCDATASection)
		return res
	#----------------------------------------------------------------------
	def toCharacterData(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomCharacterData
		If the node is not a character data node the returned object will be null .
		"""
		res = super(QDomNode,self).toCharacterData()
		isinstance(res,QtXml.QDomCharacterData)
		return res
	#----------------------------------------------------------------------
	def toComment(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomComment
		If the node is not a comment the returned object will be null .
		"""
		res = super(QDomNode,self).toComment()
		isinstance(res,QtXml.QDomComment)
		return res
	#----------------------------------------------------------------------
	def toDocument(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomDocument
		If the node is not a document the returned object will be null .
		"""
		res = super(QDomNode,self).toDocument()
		isinstance(res,QtXml.QDomDocument)
		return res
	#----------------------------------------------------------------------
	def toDocumentFragment(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomDocumentFragment
		If the node is not a document fragment the returned object will be null .
		"""
		res = super(QDomNode,self).toDocumentFragment()
		isinstance(res,QtXml.QDomDocumentFragment)
		return res
	#----------------------------------------------------------------------
	def toDocumentType(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomDocumentType
		If the node is not a document type the returned object will be null .
		"""
		res = super(QDomNode,self).toDocumentType()
		isinstance(res,QtXml.QDomDocumentType)
		return res
	#----------------------------------------------------------------------
	def toElement(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomElement
		If the node is not an element the returned object will be null .
		"""
		res = super(QDomNode,self).toElement()
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def toEntity(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomEntity
		If the node is not an entity the returned object will be null .
		"""
		res = super(QDomNode,self).toEntity()
		isinstance(res,QtXml.QDomEntity)
		return res
	#----------------------------------------------------------------------
	def toEntityReference(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomEntityReference
		If the node is not an entity reference, the returned object will be null .
		"""
		res = super(QDomNode,self).toEntityReference()
		isinstance(res,QtXml.QDomEntityReference)
		return res
	#----------------------------------------------------------------------
	def toNotation(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomNotation
		If the node is not a notation the returned object will be null .
		"""
		res = super(QDomNode,self).toNotation()
		isinstance(res,QtXml.QDomNotation)
		return res
	#----------------------------------------------------------------------
	def toProcessingInstruction(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomProcessingInstruction
		If the node is not a processing instruction the returned object will be null .
		"""
		res = super(QDomNode,self).toProcessingInstruction()
		isinstance(res,QtXml.QDomProcessingInstruction)
		return res
	#----------------------------------------------------------------------
	def toText(self):
		"""
		Converts a PySide.QtXml.QDomNode into a PySide.QtXml.QDomText
		If the node is not a text, the returned object will be null .
		"""
		res = super(QDomNode,self).toText()
		isinstance(res,QtXml.QDomText)
		return res
	#----------------------------------------------------------------------
	def appendChild(self,newChild):
		"""
		appendChild(newChild)
			newChild=QtXml.QDomNode

		Appends newChild as the nodes last child.
		If newChild is the child of another node, it is reparented to this node
		If newChild is a child of this node, then its position in the list of children is changed.
		If newChild is a PySide.QtXml.QDomDocumentFragment , then the children of the fragment are removed from the fragment and appended.
		If newChild is a PySide.QtXml.QDomElement and this node is a PySide.QtXml.QDomDocument that already has an element node as a child, newChild is not added as a child and a null node is returned.
		Returns a new reference to newChild on success or a null node on failure.
		Calling this function on a null node(created, for example, with the default constructor) does nothing and returns a null node .
		The DOM specification disallow inserting attribute nodes, but for historical reasons, QDom accepts them anyway.
		"""
		res = super(QDomNode,self).appendChild(newChild)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def cloneNode(self,deep=None):
		"""
		cloneNode(deep=None)
			deep=QtCore.bool

		Creates a deep (not shallow) copy of the PySide.QtXml.QDomNode .
		If deep is true, then the cloning is done recursively which means that all the nodes children are deep copied too
		If deep is false only the node itself is copied and the copy will have no child nodes.
		"""
		res = super(QDomNode,self).cloneNode(deep)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def firstChildElement(self,tagName=None):
		"""
		firstChildElement(tagName=None)
			tagName=unicode

		Returns the first child element with tag name tagName if tagName is non-empty; otherwise returns the first child element
		Returns a null element if no such child exists.
		"""
		res = super(QDomNode,self).firstChildElement(tagName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def insertAfter(self,newChild,refChild):
		"""
		insertAfter(newChild,refChild)
			newChild=QtXml.QDomNode
			refChild=QtXml.QDomNode

		Inserts the node newChild after the child node refChild
		refChild must be a direct child of this node
		If refChild is null then newChild is appended as this nodes last child.
		If newChild is the child of another node, it is reparented to this node
		If newChild is a child of this node, then its position in the list of children is changed.
		If newChild is a PySide.QtXml.QDomDocumentFragment , then the children of the fragment are removed from the fragment and inserted after refChild .
		Returns a new reference to newChild on success or a null node on failure.
		The DOM specification disallow inserting attribute nodes, but due to historical reasons QDom accept them nevertheless.
		"""
		res = super(QDomNode,self).insertAfter(newChild,refChild)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def insertBefore(self,newChild,refChild):
		"""
		insertBefore(newChild,refChild)
			newChild=QtXml.QDomNode
			refChild=QtXml.QDomNode

		Inserts the node newChild before the child node refChild
		refChild must be a direct child of this node
		If refChild is null then newChild is inserted as the nodes first child.
		If newChild is the child of another node, it is reparented to this node
		If newChild is a child of this node, then its position in the list of children is changed.
		If newChild is a PySide.QtXml.QDomDocumentFragment , then the children of the fragment are removed from the fragment and inserted before refChild .
		Returns a new reference to newChild on success or a null node on failure.
		The DOM specification disallow inserting attribute nodes, but due to historical reasons QDom accept them nevertheless.
		"""
		res = super(QDomNode,self).insertBefore(newChild,refChild)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def isSupported(self,feature,version):
		"""
		isSupported(feature,version)
			feature=unicode
			version=unicode

		Returns true if the DOM implementation implements the feature feature and this feature is supported by this node in the version version ; otherwise returns false.
		"""
		res = super(QDomNode,self).isSupported(feature,version)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastChildElement(self,tagName=None):
		"""
		lastChildElement(tagName=None)
			tagName=unicode

		Returns the last child element with tag name tagName if tagName is non-empty; otherwise returns the first child element
		Returns a null element if no such child exists.
		"""
		res = super(QDomNode,self).lastChildElement(tagName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def namedItem(self,name):
		"""
		namedItem(name)
			name=unicode

		Returns the first direct child node for which PySide.QtXml.QDomNode.nodeName() equals name .
		If no such direct child exists, a null node is returned.
		"""
		res = super(QDomNode,self).namedItem(name)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def nextSiblingElement(self,taName=None):
		"""
		nextSiblingElement(taName=None)
			taName=unicode

		Returns the next sibling element with tag name tagName if tagName is non-empty; otherwise returns any next sibling element
		Returns a null element if no such sibling exists.
		"""
		res = super(QDomNode,self).nextSiblingElement(taName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtXml.QDomNode

		Returns true if n and this DOM node are not equal; otherwise returns false.
		"""
		res = super(QDomNode,self).__ne__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtXml.QDomNode

		Returns true if n and this DOM node are equal; otherwise returns false.
		Any instance of PySide.QtXml.QDomNode acts as a reference to an underlying data structure in PySide.QtXml.QDomDocument
		The test for equality checks if the two references point to the same underlying node
		For example:
		The two nodes ( PySide.QtXml.QDomElement is a PySide.QtXml.QDomNode subclass) both refer to the documents root element, and element1 == element2 will return true
		On the other hand:
		Even though both nodes are empty elements carrying the same name, element3 == element4 will return false because they refer to two different nodes in the underlying data structure.
		"""
		res = super(QDomNode,self).__eq__(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def previousSiblingElement(self,tagName=None):
		"""
		previousSiblingElement(tagName=None)
			tagName=unicode

		Returns the previous sibilng element with tag name tagName if tagName is non-empty; otherwise returns any previous sibling element
		Returns a null element if no such sibling exists.
		"""
		res = super(QDomNode,self).previousSiblingElement(tagName)
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def removeChild(self,oldChild):
		"""
		removeChild(oldChild)
			oldChild=QtXml.QDomNode

		Removes oldChild from the list of children
		oldChild must be a direct child of this node.
		Returns a new reference to oldChild on success or a null node on failure.
		"""
		res = super(QDomNode,self).removeChild(oldChild)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def replaceChild(self,newChild,oldChild):
		"""
		replaceChild(newChild,oldChild)
			newChild=QtXml.QDomNode
			oldChild=QtXml.QDomNode

		Replaces oldChild with newChild
		oldChild must be a direct child of this node.
		If newChild is the child of another node, it is reparented to this node
		If newChild is a child of this node, then its position in the list of children is changed.
		If newChild is a PySide.QtXml.QDomDocumentFragment , then oldChild is replaced by all of the children of the fragment.
		Returns a new reference to oldChild on success or a null node an failure.
		"""
		res = super(QDomNode,self).replaceChild(newChild,oldChild)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def save(self,*args,**kwargs):
		"""
		save(arg__1,arg__2,arg__3)
			arg__1=QtCore.QTextStream
			arg__2=QtCore.int
			arg__3=QtXml.QDomNode.EncodingPolicy

		save(arg__1,arg__2)
			arg__1=QtCore.QTextStream
			arg__2=QtCore.int

		If encodingPolicy is QDomNode.EncodingFromDocument , this function behaves as save( PySide.QtCore.QTextStream &str, int indent).
		If encodingPolicy is EncodingFromTextStream and this node is a document node, this function behaves as save( PySide.QtCore.QTextStream &str, int indent) with the exception that the encoding specified in the text stream str is used.
		If the document contains invalid XML characters or characters that cannot be encoded in the given encoding, the result and behavior is undefined.
		"""
		res = super(QDomNode,self).save(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setNodeValue(self,arg__1):
		"""
		setNodeValue(arg__1)
			arg__1=unicode

		Sets the nodes value to v .
		"""
		res = super(QDomNode,self).setNodeValue(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPrefix(self,pre):
		"""
		setPrefix(pre)
			pre=unicode

		If the node has a namespace prefix, this function changes the namespace prefix of the node to pre
		Otherwise this function does nothing.
		Only nodes of type ElementNode or AttributeNode can have namespaces
		A namespace prefix must have be specified at creation time; it is not possible to add a namespace prefix afterwards.
		QDomDocument.createElementNS() QDomDocument.createAttributeNS()
		"""
		res = super(QDomNode,self).setPrefix(pre)
		return res
