from PySide import QtGui, QtCore

class QDomDocumentType(QtXml.QDomDocumentType):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomDocumentType,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def entities(self):
		"""
		Returns a map of all entities described in the DTD.
		"""
		res = super(QDomDocumentType,self).entities()
		isinstance(res,QtXml.QDomNamedNodeMap)
		return res
	#----------------------------------------------------------------------
	def internalSubset(self):
		"""
		Returns the internal subset of the document type or an empty string if there is no internal subset.
		"""
		res = super(QDomDocumentType,self).internalSubset()
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the document type as specified in the &lt;!DOCTYPE name&gt; tag.
		"""
		res = super(QDomDocumentType,self).name()
		return res
	#----------------------------------------------------------------------
	def notations(self):
		"""
		Returns a map of all notations described in the DTD.
		"""
		res = super(QDomDocumentType,self).notations()
		isinstance(res,QtXml.QDomNamedNodeMap)
		return res
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier of the external DTD subset or an empty string if there is no public identifier.
		"""
		res = super(QDomDocumentType,self).publicId()
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier of the external DTD subset or an empty string if there is no system identifier.
		"""
		res = super(QDomDocumentType,self).systemId()
		return res
