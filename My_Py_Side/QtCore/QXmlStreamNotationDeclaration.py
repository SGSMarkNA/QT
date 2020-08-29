from PySide import QtGui, QtCore

class QXmlStreamNotationDeclaration(QtCore.QXmlStreamNotationDeclaration):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamNotationDeclaration,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the notation name.
		"""
		res = super(QXmlStreamNotationDeclaration,self).name()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier.
		"""
		res = super(QXmlStreamNotationDeclaration,self).publicId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier.
		"""
		res = super(QXmlStreamNotationDeclaration,self).systemId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QXmlStreamNotationDeclaration

		Compares this notation declaration with other and returns true if they are not equal; otherwise returns false.
		"""
		res = super(QXmlStreamNotationDeclaration,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QXmlStreamNotationDeclaration

		Compares this notation declaration with other and returns true if they are equal; otherwise returns false.
		"""
		res = super(QXmlStreamNotationDeclaration,self).__eq__(other)
		isinstance(res,bool)
		return res
