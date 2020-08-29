from PySide import QtGui, QtCore

class QWebElement(QtWebKit.QWebElement):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebElement,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def classes(self):
		"""
		Returns the list of classes of this element.
		"""
		res = super(QWebElement,self).classes()
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Returns a clone of this element.
		The clone may be inserted at any point in the document.
		"""
		res = super(QWebElement,self).clone()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the document which this element belongs to.
		"""
		res = super(QWebElement,self).document()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def firstChild(self):
		"""
		Returns the elements first child.
		"""
		res = super(QWebElement,self).firstChild()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		Returns the geometry of this element, relative to its containing frame.
		"""
		res = super(QWebElement,self).geometry()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def hasAttributes(self):
		"""
		Returns true if the element has any attributes defined; otherwise returns false;
		"""
		res = super(QWebElement,self).hasAttributes()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasFocus(self):
		"""
		Returns true if the element has keyboard input focus; otherwise, returns false
		"""
		res = super(QWebElement,self).hasFocus()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the element is a null element; otherwise returns false.
		"""
		res = super(QWebElement,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastChild(self):
		"""
		Returns the elements last child.
		"""
		res = super(QWebElement,self).lastChild()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def localName(self):
		"""
		Returns the local name of the element
		If the element does not use namespaces, an empty string is returned.
		"""
		res = super(QWebElement,self).localName()
		return res
	#----------------------------------------------------------------------
	def namespaceUri(self):
		"""
		Returns the namespace URI of this element
		If the element has no namespace URI, an empty string is returned.
		"""
		res = super(QWebElement,self).namespaceUri()
		return res
	#----------------------------------------------------------------------
	def nextSibling(self):
		"""
		Returns the elements next sibling.
		"""
		res = super(QWebElement,self).nextSibling()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the parent element of this elemen
		If this element is the root document element, a null element is returned.
		"""
		res = super(QWebElement,self).parent()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		Returns the namespace prefix of the element
		If the element has no namespace prefix, empty string is returned.
		"""
		res = super(QWebElement,self).prefix()
		return res
	#----------------------------------------------------------------------
	def previousSibling(self):
		"""
		Returns the elements previous sibling.
		"""
		res = super(QWebElement,self).previousSibling()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def removeAllChildren(self):
		"""
		Removes all children from this element.
		"""
		res = super(QWebElement,self).removeAllChildren()
		return res
	#----------------------------------------------------------------------
	def removeFromDocument(self):
		"""
		Removes this element from the document and makes it a null element.
		"""
		res = super(QWebElement,self).removeFromDocument()
		return res
	#----------------------------------------------------------------------
	def setFocus(self):
		"""
		Gives keyboard input focus to this element
		"""
		res = super(QWebElement,self).setFocus()
		return res
	#----------------------------------------------------------------------
	def tagName(self):
		"""
		Returns the tag name of this element.
		"""
		res = super(QWebElement,self).tagName()
		return res
	#----------------------------------------------------------------------
	def takeFromDocument(self):
		"""
		Removes this element from the document and returns a reference to it.
		The element is still valid after removal, and can be inserted into other parts of the document.
		"""
		res = super(QWebElement,self).takeFromDocument()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def toInnerXml(self):
		"""
		Returns the XML content between the elements start and end tags.
		"""
		res = super(QWebElement,self).toInnerXml()
		return res
	#----------------------------------------------------------------------
	def toOuterXml(self):
		"""
		Returns this element converted to XML, including the start and the end tags as well as its attributes.
		"""
		res = super(QWebElement,self).toOuterXml()
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		Returns the text between the start and the end tag of this element.
		This is equivalent to reading the HTML innerText property.
		"""
		res = super(QWebElement,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def webFrame(self):
		"""
		Returns the web frame which this element is a part of
		If the element is a null element, null is returned.
		"""
		res = super(QWebElement,self).webFrame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def addClass(self,name):
		"""
		addClass(name)
			name=unicode

		Adds the specified class with the given name to the element.
		"""
		res = super(QWebElement,self).addClass(name)
		return res
	#----------------------------------------------------------------------
	def appendInside(self,*args,**kwargs):
		"""
		appendInside(element)
			element=QtWebKit.QWebElement

		appendInside(markup)
			markup=unicode

		Appends the given element as the elements last child.
		If element is the child of another element, it is re-parented to this element
		If element is a child of this element, then its position in the list of children is changed.
		Calling this function on a null element does nothing.
		"""
		res = super(QWebElement,self).appendInside(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def appendOutside(self,*args,**kwargs):
		"""
		appendOutside(markup)
			markup=unicode

		appendOutside(element)
			element=QtWebKit.QWebElement

		Inserts the result of parsing markup after this element.
		Calling this function on a null element does nothing.
		"""
		res = super(QWebElement,self).appendOutside(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def attribute(self,name,defaultValue=None):
		"""
		attribute(name,defaultValue=None)
			name=unicode
			defaultValue=unicode

		Returns the attribute with the given name
		If the attribute does not exist, defaultValue is returned.
		"""
		res = super(QWebElement,self).attribute(name,defaultValue)
		return res
	#----------------------------------------------------------------------
	def attributeNS(self,namespaceUri,name,defaultValue=None):
		"""
		attributeNS(namespaceUri,name,defaultValue=None)
			namespaceUri=unicode
			name=unicode
			defaultValue=unicode

		Returns the attribute with the given name in namespaceUri
		If the attribute does not exist, defaultValue is returned.
		"""
		res = super(QWebElement,self).attributeNS(namespaceUri,name,defaultValue)
		return res
	#----------------------------------------------------------------------
	def attributeNames(self,namespaceUri=None):
		"""
		attributeNames(namespaceUri=None)
			namespaceUri=unicode

		Return the list of attributes for the namespace given as namespaceUri .
		"""
		res = super(QWebElement,self).attributeNames(namespaceUri)
		return res
	#----------------------------------------------------------------------
	def encloseContentsWith(self,*args,**kwargs):
		"""
		encloseContentsWith(markup)
			markup=unicode

		encloseContentsWith(element)
			element=QtWebKit.QWebElement

		Encloses the contents of this element with the result of parsing markup
		This element becomes the child of the deepest descendant within markup .
		"""
		res = super(QWebElement,self).encloseContentsWith(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def encloseWith(self,*args,**kwargs):
		"""
		encloseWith(element)
			element=QtWebKit.QWebElement

		encloseWith(markup)
			markup=unicode

		Encloses this element with element
		This element becomes the child of the deepest descendant within element .
		"""
		res = super(QWebElement,self).encloseWith(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def evaluateJavaScript(self,scriptSource):
		"""
		evaluateJavaScript(scriptSource)
			scriptSource=unicode

		Executes scriptSource with this element as this object.
		"""
		res = super(QWebElement,self).evaluateJavaScript(scriptSource)
		return res
	#----------------------------------------------------------------------
	def findAll(self,selectorQuery):
		"""
		findAll(selectorQuery)
			selectorQuery=unicode

		Returns a new list of child elements matching the given CSS selector selectorQuery
		If there are no matching elements, an empty list is returned.
		Standard CSS2 selector syntax is used for the query.
		"""
		res = super(QWebElement,self).findAll(selectorQuery)
		isinstance(res,QtWebKit.QWebElementCollection)
		return res
	#----------------------------------------------------------------------
	def findFirst(self,selectorQuery):
		"""
		findFirst(selectorQuery)
			selectorQuery=unicode

		Returns the first child element that matches the given CSS selector selectorQuery .
		Standard CSS2 selector syntax is used for the query.
		"""
		res = super(QWebElement,self).findFirst(selectorQuery)
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def hasAttribute(self,name):
		"""
		hasAttribute(name)
			name=unicode

		Returns true if this element has an attribute with the given name ; otherwise returns false.
		"""
		res = super(QWebElement,self).hasAttribute(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasAttributeNS(self,namespaceUri,name):
		"""
		hasAttributeNS(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		Returns true if this element has an attribute with the given name , in namespaceUri ; otherwise returns false.
		"""
		res = super(QWebElement,self).hasAttributeNS(namespaceUri,name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasClass(self,name):
		"""
		hasClass(name)
			name=unicode

		Returns true if this element has a class with the given name ; otherwise returns false.
		"""
		res = super(QWebElement,self).hasClass(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,o):
		"""
		__ne__(o)
			o=QtWebKit.QWebElement

		Returns true if this element points to a different underlying DOM object than o ; otherwise returns false.
		"""
		res = super(QWebElement,self).__ne__(o)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,o):
		"""
		__eq__(o)
			o=QtWebKit.QWebElement

		Returns true if this element points to the same underlying DOM object as o ; otherwise returns false.
		"""
		res = super(QWebElement,self).__eq__(o)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prependInside(self,*args,**kwargs):
		"""
		prependInside(markup)
			markup=unicode

		prependInside(element)
			element=QtWebKit.QWebElement

		Prepends the result of parsing markup as the elements first child.
		Calling this function on a null element does nothing.
		"""
		res = super(QWebElement,self).prependInside(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def prependOutside(self,*args,**kwargs):
		"""
		prependOutside(element)
			element=QtWebKit.QWebElement

		prependOutside(markup)
			markup=unicode

		Inserts the given element before this element.
		If element is the child of another element, it is re-parented to the parent of this element.
		Calling this function on a null element does nothing.
		"""
		res = super(QWebElement,self).prependOutside(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def removeAttribute(self,name):
		"""
		removeAttribute(name)
			name=unicode

		Removes the attribute with the given name from this element.
		"""
		res = super(QWebElement,self).removeAttribute(name)
		return res
	#----------------------------------------------------------------------
	def removeAttributeNS(self,namespaceUri,name):
		"""
		removeAttributeNS(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		Removes the attribute with the given name , in namespaceUri , from this element.
		"""
		res = super(QWebElement,self).removeAttributeNS(namespaceUri,name)
		return res
	#----------------------------------------------------------------------
	def removeClass(self,name):
		"""
		removeClass(name)
			name=unicode

		Removes the specified class with the given name from the element.
		"""
		res = super(QWebElement,self).removeClass(name)
		return res
	#----------------------------------------------------------------------
	def render(self,painter):
		"""
		render(painter)
			painter=QtGui.QPainter

		Render the element into painter .
		"""
		res = super(QWebElement,self).render(painter)
		return res
	#----------------------------------------------------------------------
	def replace(self,*args,**kwargs):
		"""
		replace(element)
			element=QtWebKit.QWebElement

		replace(markup)
			markup=unicode

		Replaces this element with element .
		This method will not replace the <html>, <head> or <body> elements.
		"""
		res = super(QWebElement,self).replace(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,name,value):
		"""
		setAttribute(name,value)
			name=unicode
			value=unicode

		Adds an attribute with the given name and value
		If an attribute with the same name exists, its value is replaced by value .
		"""
		res = super(QWebElement,self).setAttribute(name,value)
		return res
	#----------------------------------------------------------------------
	def setAttributeNS(self,namespaceUri,name,value):
		"""
		setAttributeNS(namespaceUri,name,value)
			namespaceUri=unicode
			name=unicode
			value=unicode

		Adds an attribute with the given name in namespaceUri with value
		If an attribute with the same name exists, its value is replaced by value .
		"""
		res = super(QWebElement,self).setAttributeNS(namespaceUri,name,value)
		return res
	#----------------------------------------------------------------------
	def setInnerXml(self,markup):
		"""
		setInnerXml(markup)
			markup=unicode

		Replaces the contents of this element with markup
		The string may contain HTML or XML tags, which is parsed and formatted before insertion into the document.
		"""
		res = super(QWebElement,self).setInnerXml(markup)
		return res
	#----------------------------------------------------------------------
	def setOuterXml(self,markup):
		"""
		setOuterXml(markup)
			markup=unicode

		Replaces the contents of this element as well as its own tag with markup
		The string may contain HTML or XML tags, which is parsed and formatted before insertion into the document.
		"""
		res = super(QWebElement,self).setOuterXml(markup)
		return res
	#----------------------------------------------------------------------
	def setPlainText(self,text):
		"""
		setPlainText(text)
			text=unicode

		Replaces the existing content of this element with text .
		This is equivalent to setting the HTML innerText property.
		"""
		res = super(QWebElement,self).setPlainText(text)
		return res
	#----------------------------------------------------------------------
	def setStyleProperty(self,name,value):
		"""
		setStyleProperty(name,value)
			name=unicode
			value=unicode

		Sets the value of the inline style with the given name to value .
		Setting a value, does not necessarily mean that it will become the applied value, due to the fact that the style propertys value might have been set earlier with a higher priority in external or embedded style declarations.
		In order to ensure that the value will be applied, you may have to append !important to the value.
		"""
		res = super(QWebElement,self).setStyleProperty(name,value)
		return res
	#----------------------------------------------------------------------
	def styleProperty(self,name,strategy):
		"""
		styleProperty(name,strategy)
			name=unicode
			strategy=QtWebKit.QWebElement.StyleResolveStrategy

		Returns the value of the style with the given name using the specified strategy
		If a style with name does not exist, an empty string is returned.
		In CSS, the cascading part depends on which CSS rule has priority and is thus applied
		Generally, the last defined rule has priority
		Thus, an inline style rule has priority over an embedded block style rule, which in return has priority over an external style rule.
		If the !important declaration is set on one of those, the declaration receives highest priority, unless other declarations also use the !important declaration
		Then, the last !important declaration takes predecence.
		"""
		res = super(QWebElement,self).styleProperty(name,strategy)
		return res
	#----------------------------------------------------------------------
	def toggleClass(self,name):
		"""
		toggleClass(name)
			name=unicode

		Adds the specified class with the given name if it is not present
		If the class is already present, it will be removed.
		"""
		res = super(QWebElement,self).toggleClass(name)
		return res
