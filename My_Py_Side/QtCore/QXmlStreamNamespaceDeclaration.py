from PySide import QtGui, QtCore

class QXmlStreamNamespaceDeclaration(QtCore.QXmlStreamNamespaceDeclaration):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamNamespaceDeclaration,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def namespaceUri(self):
		"""
		Returns the namespaceUri.
		"""
		res = super(QXmlStreamNamespaceDeclaration,self).namespaceUri()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		Returns the prefix.
		"""
		res = super(QXmlStreamNamespaceDeclaration,self).prefix()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QXmlStreamNamespaceDeclaration

		Compares this namespace declaration with other and returns true if they are not equal; otherwise returns false.
		"""
		res = super(QXmlStreamNamespaceDeclaration,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QXmlStreamNamespaceDeclaration

		Compares this namespace declaration with other and returns true if they are equal; otherwise returns false.
		"""
		res = super(QXmlStreamNamespaceDeclaration,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
