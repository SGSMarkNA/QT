from PySide import QtGui, QtCore

class QXmlStreamEntityDeclaration(QtCore.QXmlStreamEntityDeclaration):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamEntityDeclaration,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the entity name.
		"""
		res = super(QXmlStreamEntityDeclaration,self).name()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def notationName(self):
		"""
		Returns the notation name.
		"""
		res = super(QXmlStreamEntityDeclaration,self).notationName()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier.
		"""
		res = super(QXmlStreamEntityDeclaration,self).publicId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier.
		"""
		res = super(QXmlStreamEntityDeclaration,self).systemId()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the entitys value.
		"""
		res = super(QXmlStreamEntityDeclaration,self).value()
		isinstance(res,QtCore.QStringRef)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QXmlStreamEntityDeclaration

		Compares this entity declaration with other and returns true if they are not equal; otherwise returns false.
		"""
		res = super(QXmlStreamEntityDeclaration,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QXmlStreamEntityDeclaration

		Compares this entity declaration with other and returns true if they are equal; otherwise returns false.
		"""
		res = super(QXmlStreamEntityDeclaration,self).__eq__(other)
		isinstance(res,bool)
		return res
