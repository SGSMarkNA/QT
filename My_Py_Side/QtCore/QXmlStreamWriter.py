from PySide import QtGui, QtCore

class QXmlStreamWriter(QtCore.QXmlStreamWriter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamWriter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoFormatting(self):
		"""
		Returns true if auto formattting is enabled, otherwise false .
		"""
		res = super(QXmlStreamWriter,self).autoFormatting()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def autoFormattingIndent(self):
		"""

		"""
		res = super(QXmlStreamWriter,self).autoFormattingIndent()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def codec(self):
		"""
		Returns the codec that is currently assigned to the stream.
		"""
		res = super(QXmlStreamWriter,self).codec()
		isinstance(res,QtCore.QTextCodec)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the current device associated with the PySide.QtCore.QXmlStreamWriter , or 0 if no device has been assigned.
		"""
		res = super(QXmlStreamWriter,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def writeEndDocument(self):
		"""
		Closes all remaining open start elements and writes a newline.
		"""
		res = super(QXmlStreamWriter,self).writeEndDocument()
		return res
	#----------------------------------------------------------------------
	def writeEndElement(self):
		"""
		Closes the previous start element.
		"""
		res = super(QXmlStreamWriter,self).writeEndElement()
		return res
	#----------------------------------------------------------------------
	def writeStartDocument(self):
		"""
		This is an overloaded function.
		Writes a document start with XML version number 1.0
		This also writes the encoding information.
		"""
		res = super(QXmlStreamWriter,self).writeStartDocument()
		return res
	#----------------------------------------------------------------------
	def setAutoFormatting(self,arg__1):
		"""
		setAutoFormatting(arg__1)
			arg__1=QtCore.bool

		Enables auto formatting if enable is true , otherwise disables it.
		The default value is false .
		"""
		res = super(QXmlStreamWriter,self).setAutoFormatting(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAutoFormattingIndent(self,spacesOrTabs):
		"""
		setAutoFormattingIndent(spacesOrTabs)
			spacesOrTabs=QtCore.int


		"""
		res = super(QXmlStreamWriter,self).setAutoFormattingIndent(spacesOrTabs)
		return res
	#----------------------------------------------------------------------
	def setCodec(self,*args,**kwargs):
		"""
		setCodec(codec)
			codec=QtCore.QTextCodec

		setCodec(codecName)
			codecName=str

		Sets the codec for this stream to codec
		The codec is used for encoding any data that is written
		By default, PySide.QtCore.QXmlStreamWriter uses UTF-8.
		The encoding information is stored in the initial xml tag which gets written when you call PySide.QtCore.QXmlStreamWriter.writeStartDocument()
		Call this function before calling PySide.QtCore.QXmlStreamWriter.writeStartDocument() .
		"""
		res = super(QXmlStreamWriter,self).setCodec(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets the current device to device
		If you want the stream to write into a PySide.QtCore.QByteArray , you can create a PySide.QtCore.QBuffer device.
		"""
		res = super(QXmlStreamWriter,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def writeAttribute(self,*args,**kwargs):
		"""
		writeAttribute(qualifiedName,value)
			qualifiedName=unicode
			value=unicode

		writeAttribute(attribute)
			attribute=QtCore.QXmlStreamAttribute

		writeAttribute(namespaceUri,name,value)
			namespaceUri=unicode
			name=unicode
			value=unicode

		This is an overloaded function.
		Writes an attribute with qualifiedName and value .
		This function can only be called after PySide.QtCore.QXmlStreamWriter.writeStartElement() before any content is written, or after PySide.QtCore.QXmlStreamWriter.writeEmptyElement() .
		"""
		res = super(QXmlStreamWriter,self).writeAttribute(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def writeAttributes(self,attributes):
		"""
		writeAttributes(attributes)
			attributes=QtCore.QXmlStreamAttributes

		Writes the attribute vector attributes
		If a namespace referenced in an attribute not been declared yet, PySide.QtCore.QXmlStreamWriter will generate a namespace declaration for it.
		This function can only be called after PySide.QtCore.QXmlStreamWriter.writeStartElement() before any content is written, or after PySide.QtCore.QXmlStreamWriter.writeEmptyElement() .
		"""
		res = super(QXmlStreamWriter,self).writeAttributes(attributes)
		return res
	#----------------------------------------------------------------------
	def writeCDATA(self,text):
		"""
		writeCDATA(text)
			text=unicode

		Writes text as CDATA section
		If text contains the forbidden character sequence ]]>, it is split into different CDATA sections.
		This function mainly exists for completeness
		Normally you should not need use it, because PySide.QtCore.QXmlStreamWriter.writeCharacters() automatically escapes all non-content characters.
		"""
		res = super(QXmlStreamWriter,self).writeCDATA(text)
		return res
	#----------------------------------------------------------------------
	def writeCharacters(self,text):
		"""
		writeCharacters(text)
			text=unicode

		Writes text
		The characters <, &, and  are escaped as entity references &lt;, &amp;, and &quot;
		To avoid the forbidden sequence ]]>, > is also escaped as &gt;.
		"""
		res = super(QXmlStreamWriter,self).writeCharacters(text)
		return res
	#----------------------------------------------------------------------
	def writeComment(self,text):
		"""
		writeComment(text)
			text=unicode

		Writes text as XML comment, where text must not contain the forbidden sequence  or end with -
		Note that XML does not provide any way to escape - in a comment.
		"""
		res = super(QXmlStreamWriter,self).writeComment(text)
		return res
	#----------------------------------------------------------------------
	def writeCurrentToken(self,reader):
		"""
		writeCurrentToken(reader)
			reader=QtCore.QXmlStreamReader

		Writes the current state of the reader
		All possible valid states are supported.
		The purpose of this function is to support chained processing of XML data.
		"""
		res = super(QXmlStreamWriter,self).writeCurrentToken(reader)
		return res
	#----------------------------------------------------------------------
	def writeDTD(self,dtd):
		"""
		writeDTD(dtd)
			dtd=unicode

		Writes a DTD section
		The dtd represents the entire doctypedecl production from the XML 1.0 specification.
		"""
		res = super(QXmlStreamWriter,self).writeDTD(dtd)
		return res
	#----------------------------------------------------------------------
	def writeDefaultNamespace(self,namespaceUri):
		"""
		writeDefaultNamespace(namespaceUri)
			namespaceUri=unicode

		Writes a default namespace declaration for namespaceUri .
		If PySide.QtCore.QXmlStreamWriter.writeStartElement() or PySide.QtCore.QXmlStreamWriter.writeEmptyElement() was called, the declaration applies to the current element; otherwise it applies to the next child element.
		Note that the namespaces http://www.w3.org/XML/1998/namespace (bound to xmlns ) and http://www.w3.org/2000/xmlns/ (bound to xml ) by definition cannot be declared as default.
		"""
		res = super(QXmlStreamWriter,self).writeDefaultNamespace(namespaceUri)
		return res
	#----------------------------------------------------------------------
	def writeEmptyElement(self,*args,**kwargs):
		"""
		writeEmptyElement(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		writeEmptyElement(qualifiedName)
			qualifiedName=unicode

		Writes an empty element with name , prefixed for the specified namespaceUri
		If the namespace has not been declared, PySide.QtCore.QXmlStreamWriter will generate a namespace declaration for it
		Subsequent calls to PySide.QtCore.QXmlStreamWriter.writeAttribute() will add attributes to this element.
		"""
		res = super(QXmlStreamWriter,self).writeEmptyElement(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def writeEntityReference(self,name):
		"""
		writeEntityReference(name)
			name=unicode

		Writes the entity reference name to the stream, as &``name`` ;.
		"""
		res = super(QXmlStreamWriter,self).writeEntityReference(name)
		return res
	#----------------------------------------------------------------------
	def writeNamespace(self,namespaceUri,prefix=None):
		"""
		writeNamespace(namespaceUri,prefix=None)
			namespaceUri=unicode
			prefix=unicode

		Writes a namespace declaration for namespaceUri with prefix
		If prefix is empty, PySide.QtCore.QXmlStreamWriter assigns a unique prefix consisting of the letter n followed by a number.
		If PySide.QtCore.QXmlStreamWriter.writeStartElement() or PySide.QtCore.QXmlStreamWriter.writeEmptyElement() was called, the declaration applies to the current element; otherwise it applies to the next child element.
		Note that the prefix xml is both predefined and reserved for http://www.w3.org/XML/1998/namespace , which in turn cannot be bound to any other prefix
		The prefix xmlns and its URI http://www.w3.org/2000/xmlns/ are used for the namespace mechanism itself and thus completely forbidden in declarations.
		"""
		res = super(QXmlStreamWriter,self).writeNamespace(namespaceUri,prefix)
		return res
	#----------------------------------------------------------------------
	def writeProcessingInstruction(self,target,data=None):
		"""
		writeProcessingInstruction(target,data=None)
			target=unicode
			data=unicode

		Writes an XML processing instruction with target and data , where data must not contain the sequence ?>.
		"""
		res = super(QXmlStreamWriter,self).writeProcessingInstruction(target,data)
		return res
	#----------------------------------------------------------------------
	def writeStartDocument(self,*args,**kwargs):
		"""
		writeStartDocument(version)
			version=unicode

		writeStartDocument(version,standalone)
			version=unicode
			standalone=QtCore.bool

		Writes a document start with the XML version number version .
		"""
		res = super(QXmlStreamWriter,self).writeStartDocument(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def writeStartElement(self,*args,**kwargs):
		"""
		writeStartElement(qualifiedName)
			qualifiedName=unicode

		writeStartElement(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		This is an overloaded function.
		Writes a start element with qualifiedName
		Subsequent calls to PySide.QtCore.QXmlStreamWriter.writeAttribute() will add attributes to this element.
		"""
		res = super(QXmlStreamWriter,self).writeStartElement(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def writeTextElement(self,*args,**kwargs):
		"""
		writeTextElement(namespaceUri,name,text)
			namespaceUri=unicode
			name=unicode
			text=unicode

		writeTextElement(qualifiedName,text)
			qualifiedName=unicode
			text=unicode

		Writes a text element with name , prefixed for the specified namespaceUri , and text
		If the namespace has not been declared, PySide.QtCore.QXmlStreamWriter will generate a namespace declaration for it.
		This is a convenience function equivalent to:
		"""
		res = super(QXmlStreamWriter,self).writeTextElement(*args,**kwargs)
		return res
