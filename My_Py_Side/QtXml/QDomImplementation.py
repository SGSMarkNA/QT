from PySide import QtGui, QtCore

class QDomImplementation(QtXml.QDomImplementation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomImplementation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns false if the object was created by QDomDocument.implementation() ; otherwise returns true.
		"""
		res = super(QDomImplementation,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def createDocument(self,nsURI,qName,doctype):
		"""
		createDocument(nsURI,qName,doctype)
			nsURI=unicode
			qName=unicode
			doctype=QtXml.QDomDocumentType

		Creates a DOM document with the document type doctype
		This function also adds a root element node with the qualified name qName and the namespace URI nsURI .
		"""
		res = super(QDomImplementation,self).createDocument(nsURI,qName,doctype)
		isinstance(res,QtXml.QDomDocument)
		return res
	#----------------------------------------------------------------------
	def createDocumentType(self,qName,publicId,systemId):
		"""
		createDocumentType(qName,publicId,systemId)
			qName=unicode
			publicId=unicode
			systemId=unicode

		Creates a document type node for the name qName .
		publicId specifies the public identifier of the external subset
		If you specify an empty string ( QString() ) as the publicId , this means that the document type has no public identifier.
		systemId specifies the system identifier of the external subset
		If you specify an empty string as the systemId , this means that the document type has no system identifier.
		Since you cannot have a public identifier without a system identifier, the public identifier is set to an empty string if there is no system identifier.
		DOM level 2 does not support any other document type declaration features.
		The only way you can use a document type that was created this way, is in combination with the PySide.QtXml.QDomImplementation.createDocument() function to create a PySide.QtXml.QDomDocument with this document type.
		In the DOM specification, this is the only way to create a non-null document
		For historical reasons, Qt also allows to create the document using the default empty constructor
		The resulting document is null, but becomes non-null when a factory function, for example QDomDocument.createElement() , is called
		The document also becomes non-null when setContent() is called.
		"""
		res = super(QDomImplementation,self).createDocumentType(qName,publicId,systemId)
		isinstance(res,QtXml.QDomDocumentType)
		return res
	#----------------------------------------------------------------------
	def hasFeature(self,feature,version):
		"""
		hasFeature(feature,version)
			feature=unicode
			version=unicode

		The function returns true if QDom implements the requested version of a feature ; otherwise returns false.
		The currently supported features and their versions:
		"""
		res = super(QDomImplementation,self).hasFeature(feature,version)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtXml.QDomImplementation

		Returns true if x and this DOM implementation object were created from different QDomDocuments; otherwise returns false.
		"""
		res = super(QDomImplementation,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtXml.QDomImplementation

		Returns true if x and this DOM implementation object were created from the same PySide.QtXml.QDomDocument ; otherwise returns false.
		"""
		res = super(QDomImplementation,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res
