from PySide import QtGui, QtCore

class QXmlStreamReader(QtCore.QXmlStreamReader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamReader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the reader has read until the end of the XML document, or if an PySide.QtCore.QXmlStreamReader.error() has occurred and reading has been aborted
		Otherwise, it returns false.
		When PySide.QtCore.QXmlStreamReader.atEnd() and PySide.QtCore.QXmlStreamReader.hasError() return true and PySide.QtCore.QXmlStreamReader.error() returns PrematureEndOfDocumentError , it means the XML has been well-formed so far, but a complete XML document has not been parsed
		The next chunk of XML can be added with PySide.QtCore.QXmlStreamReader.addData() , if the XML is being read from a PySide.QtCore.QByteArray , or by waiting for more data to arrive if the XML is being read from a PySide.QtCore.QIODevice
		Either way, PySide.QtCore.QXmlStreamReader.atEnd() will return false once more data is available.
		"""
		res = super(QXmlStreamReader,self).atEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def attributes(self):
		"""
		Returns the attributes of a StartElement .
		"""
		res = super(QXmlStreamReader,self).attributes()
		isinstance(res,QtCore.QXmlStreamAttributes)
		return res
	#----------------------------------------------------------------------
	def characterOffset(self):
		"""
		Returns the current character offset, starting with 0.
		"""
		res = super(QXmlStreamReader,self).characterOffset()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes any PySide.QtCore.QXmlStreamReader.device() or data from the reader and resets its internal state to the initial state.
		"""
		res = super(QXmlStreamReader,self).clear()
		return res
	#----------------------------------------------------------------------
	def columnNumber(self):
		"""
		Returns the current column number, starting with 0.
		"""
		res = super(QXmlStreamReader,self).columnNumber()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the current device associated with the PySide.QtCore.QXmlStreamReader , or 0 if no device has been assigned.
		"""
		res = super(QXmlStreamReader,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def documentEncoding(self):
		"""
		If the state() is StartDocument , this function returns the encoding string as specified in the XML declaration
		Otherwise an empty string is returned.
		"""
		res = super(QXmlStreamReader,self).documentEncoding()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def documentVersion(self):
		"""
		If the state() is StartDocument , this function returns the version string as specified in the XML declaration
		Otherwise an empty string is returned.
		"""
		res = super(QXmlStreamReader,self).documentVersion()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def dtdName(self):
		"""
		If the state() is DTD , this function returns the DTDs name
		Otherwise an empty string is returned.
		"""
		res = super(QXmlStreamReader,self).dtdName()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def dtdPublicId(self):
		"""
		If the state() is DTD , this function returns the DTDs public identifier
		Otherwise an empty string is returned.
		"""
		res = super(QXmlStreamReader,self).dtdPublicId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def dtdSystemId(self):
		"""
		If the state() is DTD , this function returns the DTDs system identifier
		Otherwise an empty string is returned.
		"""
		res = super(QXmlStreamReader,self).dtdSystemId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def entityDeclarations(self):
		"""
		If the state() is DTD , this function returns the DTDs unparsed (external) entity declarations
		Otherwise an empty vector is returned.
		The QXmlStreamEntityDeclarations class is defined to be a QVector of PySide.QtCore.QXmlStreamEntityDeclaration .
		"""
		res = super(QXmlStreamReader,self).entityDeclarations()
		return res
	#----------------------------------------------------------------------
	def entityResolver(self):
		"""
		Returns the entity resolver, or 0 if there is no entity resolver.
		"""
		res = super(QXmlStreamReader,self).entityResolver()
		isinstance(res,QtCore.QXmlStreamEntityResolver)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of the current error, or NoError if no error occurred.
		"""
		res = super(QXmlStreamReader,self).error()
		isinstance(res,QtCore.QXmlStreamReader.Error)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns the error message that was set with PySide.QtCore.QXmlStreamReader.raiseError() .
		"""
		res = super(QXmlStreamReader,self).errorString()
		return res
	#----------------------------------------------------------------------
	def hasError(self):
		"""
		Returns true if an error has occurred, otherwise false .
		"""
		res = super(QXmlStreamReader,self).hasError()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isCDATA(self):
		"""
		Returns true if the reader reports characters that stem from a CDATA section; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isCDATA()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isCharacters(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals Characters ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isCharacters()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isComment(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals Comment ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isComment()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isDTD(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals DTD ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isDTD()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEndDocument(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals EndDocument ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isEndDocument()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEndElement(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals EndElement ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isEndElement()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEntityReference(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals EntityReference ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isEntityReference()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isProcessingInstruction(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals ProcessingInstruction ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isProcessingInstruction()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isStandaloneDocument(self):
		"""
		Returns true if this document has been declared standalone in the XML declaration; otherwise returns false.
		If no XML declaration has been parsed, this function returns false.
		"""
		res = super(QXmlStreamReader,self).isStandaloneDocument()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isStartDocument(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals StartDocument ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isStartDocument()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isStartElement(self):
		"""
		Returns true if PySide.QtCore.QXmlStreamReader.tokenType() equals StartElement ; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isStartElement()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isWhitespace(self):
		"""
		Returns true if the reader reports characters that only consist of white-space; otherwise returns false.
		"""
		res = super(QXmlStreamReader,self).isWhitespace()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		Returns the current line number, starting with 1.
		"""
		res = super(QXmlStreamReader,self).lineNumber()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the local name of a StartElement , EndElement , or an EntityReference .
		"""
		res = super(QXmlStreamReader,self).name()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def namespaceDeclarations(self):
		"""
		If the state() is StartElement , this function returns the elements namespace declarations
		Otherwise an empty vector is returned.
		The PySide.QtCore.QXmlStreamNamespaceDeclaration class is defined to be a QVector of PySide.QtCore.QXmlStreamNamespaceDeclaration .
		"""
		res = super(QXmlStreamReader,self).namespaceDeclarations()
		return res
	#----------------------------------------------------------------------
	def namespaceProcessing(self):
		"""

		"""
		res = super(QXmlStreamReader,self).namespaceProcessing()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def namespaceUri(self):
		"""
		Returns the namespaceUri of a StartElement or EndElement .
		"""
		res = super(QXmlStreamReader,self).namespaceUri()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def notationDeclarations(self):
		"""
		If the state() is DTD , this function returns the DTDs notation declarations
		Otherwise an empty vector is returned.
		The QXmlStreamNotationDeclarations class is defined to be a QVector of PySide.QtCore.QXmlStreamNotationDeclaration .
		"""
		res = super(QXmlStreamReader,self).notationDeclarations()
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		Returns the prefix of a StartElement or EndElement .
		"""
		res = super(QXmlStreamReader,self).prefix()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def processingInstructionData(self):
		"""
		Returns the data of a ProcessingInstruction .
		"""
		res = super(QXmlStreamReader,self).processingInstructionData()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def processingInstructionTarget(self):
		"""
		Returns the target of a ProcessingInstruction .
		"""
		res = super(QXmlStreamReader,self).processingInstructionTarget()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def qualifiedName(self):
		"""
		Returns the qualified name of a StartElement or EndElement ;
		A qualified name is the raw name of an element in the XML data
		It consists of the namespace prefix, followed by colon, followed by the elements local name
		Since the namespace prefix is not unique (the same prefix can point to different namespaces and different prefixes can point to the same namespace), you shouldnt use PySide.QtCore.QXmlStreamReader.qualifiedName() , but the resolved PySide.QtCore.QXmlStreamReader.namespaceUri() and the attributes local PySide.QtCore.QXmlStreamReader.name() .
		"""
		res = super(QXmlStreamReader,self).qualifiedName()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def readElementText(self):
		"""
		This function overloads PySide.QtCore.QXmlStreamReader.readElementText() .
		Calling this function is equivalent to calling readElementText( ErrorOnUnexpectedElement ).
		"""
		res = super(QXmlStreamReader,self).readElementText()
		return res
	#----------------------------------------------------------------------
	def readNext(self):
		"""
		Reads the next token and returns its type.
		With one exception, once an PySide.QtCore.QXmlStreamReader.error() is reported by PySide.QtCore.QXmlStreamReader.readNext() , further reading of the XML stream is not possible
		Then PySide.QtCore.QXmlStreamReader.atEnd() returns true, PySide.QtCore.QXmlStreamReader.hasError() returns true, and this function returns QXmlStreamReader.Invalid .
		The exception is when PySide.QtCore.QXmlStreamReader.error() returns PrematureEndOfDocumentError
		This error is reported when the end of an otherwise well-formed chunk of XML is reached, but the chunk doesnt represent a complete XML document
		In that case, parsing can be resumed by calling PySide.QtCore.QXmlStreamReader.addData() to add the next chunk of XML, when the stream is being read from a PySide.QtCore.QByteArray , or by waiting for more data to arrive when the stream is being read from a PySide.QtCore.QXmlStreamReader.device() .
		"""
		res = super(QXmlStreamReader,self).readNext()
		isinstance(res,QtCore.QXmlStreamReader.TokenType)
		return res
	#----------------------------------------------------------------------
	def readNextStartElement(self):
		"""
		Reads until the next start element within the current element
		Returns true when a start element was reached
		When the end element was reached, or when an error occurred, false is returned.
		The current element is the element matching the most recently parsed start element of which a matching end element has not yet been reached
		When the parser has reached the end element, the current element becomes the parent element.
		This is a convenience function for when youre only concerned with parsing XML elements
		The QXmlStream Bookmarks Example makes extensive use of this function.
		"""
		res = super(QXmlStreamReader,self).readNextStartElement()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def skipCurrentElement(self):
		"""
		Reads until the end of the current element, skipping any child nodes
		This function is useful for skipping unknown elements.
		The current element is the element matching the most recently parsed start element of which a matching end element has not yet been reached
		When the parser has reached the end element, the current element becomes the parent element.
		"""
		res = super(QXmlStreamReader,self).skipCurrentElement()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the text of Characters , Comment , DTD , or EntityReference .
		"""
		res = super(QXmlStreamReader,self).text()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def tokenString(self):
		"""
		Returns the readers current token as string.
		"""
		res = super(QXmlStreamReader,self).tokenString()
		return res
	#----------------------------------------------------------------------
	def tokenType(self):
		"""
		Returns the type of the current token.
		The current token can also be queried with the convenience functions PySide.QtCore.QXmlStreamReader.isStartDocument() , PySide.QtCore.QXmlStreamReader.isEndDocument() , PySide.QtCore.QXmlStreamReader.isStartElement() , PySide.QtCore.QXmlStreamReader.isEndElement() , PySide.QtCore.QXmlStreamReader.isCharacters() , PySide.QtCore.QXmlStreamReader.isComment() , PySide.QtCore.QXmlStreamReader.isDTD() , PySide.QtCore.QXmlStreamReader.isEntityReference() , and PySide.QtCore.QXmlStreamReader.isProcessingInstruction() .
		"""
		res = super(QXmlStreamReader,self).tokenType()
		isinstance(res,QtCore.QXmlStreamReader.TokenType)
		return res
	#----------------------------------------------------------------------
	def addData(self,*args,**kwargs):
		"""
		addData(data)
			data=str

		addData(data)
			data=unicode

		addData(data)
			data=QtCore.QByteArray

		Adds more data for the reader to read
		This function does nothing if the reader has a PySide.QtCore.QXmlStreamReader.device() .
		"""
		res = super(QXmlStreamReader,self).addData(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addExtraNamespaceDeclaration(self,extraNamespaceDeclaraction):
		"""
		addExtraNamespaceDeclaration(extraNamespaceDeclaraction)
			extraNamespaceDeclaraction=QtCore.QXmlStreamNamespaceDeclaration

		Adds an extraNamespaceDeclaration
		The declaration will be valid for children of the current element, or - should the function be called before any elements are read - for the entire XML document.
		"""
		res = super(QXmlStreamReader,self).addExtraNamespaceDeclaration(extraNamespaceDeclaraction)
		return res
	#----------------------------------------------------------------------
	def addExtraNamespaceDeclarations(self,extraNamespaceDeclaractions):
		"""
		addExtraNamespaceDeclarations(extraNamespaceDeclaractions)
			extraNamespaceDeclaractions=unKnown


		"""
		res = super(QXmlStreamReader,self).addExtraNamespaceDeclarations(extraNamespaceDeclaractions)
		return res
	#----------------------------------------------------------------------
	def raiseError(self,message=None):
		"""
		raiseError(message=None)
			message=unicode

		Raises a custom error with an optional error message .
		"""
		res = super(QXmlStreamReader,self).raiseError(message)
		return res
	#----------------------------------------------------------------------
	def readElementText(self,behaviour):
		"""
		readElementText(behaviour)
			behaviour=QtCore.QXmlStreamReader.ReadElementTextBehaviour

		Convenience function to be called in case a StartElement was read
		Reads until the corresponding EndElement and returns all text in-between
		In case of no error, the current token (see PySide.QtCore.QXmlStreamReader.tokenType() ) after having called this function is EndElement .
		The function concatenates PySide.QtCore.QXmlStreamReader.text() when it reads either Characters or EntityReference tokens, but skips ProcessingInstruction and Comment
		If the current token is not StartElement , an empty string is returned.
		The behaviour defines what happens in case anything else is read before reaching EndElement
		The function can include the text from child elements (useful for example for HTML), ignore child elements, or raise an UnexpectedElementError and return what was read so far.
		"""
		res = super(QXmlStreamReader,self).readElementText(behaviour)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets the current device to device
		Setting the device resets the stream to its initial state.
		"""
		res = super(QXmlStreamReader,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setEntityResolver(self,resolver):
		"""
		setEntityResolver(resolver)
			resolver=QtCore.QXmlStreamEntityResolver

		Makes resolver the new PySide.QtCore.QXmlStreamReader.entityResolver() .
		The stream reader does not take ownership of the resolver
		Its the callers responsibility to ensure that the resolver is valid during the entire life-time of the stream reader object, or until another resolver or 0 is set.
		"""
		res = super(QXmlStreamReader,self).setEntityResolver(resolver)
		return res
	#----------------------------------------------------------------------
	def setNamespaceProcessing(self,arg__1):
		"""
		setNamespaceProcessing(arg__1)
			arg__1=QtCore.bool


		"""
		res = super(QXmlStreamReader,self).setNamespaceProcessing(arg__1)
		return res
