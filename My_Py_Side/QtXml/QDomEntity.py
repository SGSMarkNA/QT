from PySide import QtGui, QtCore

class QDomEntity(QtXml.QDomEntity):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomEntity,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def notationName(self):
		"""
		For unparsed entities this function returns the name of the notation for the entity
		For parsed entities this function returns an empty string.
		"""
		res = super(QDomEntity,self).notationName()
		return res
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier associated with this entity
		If the public identifier was not specified an empty string is returned.
		"""
		res = super(QDomEntity,self).publicId()
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier associated with this entity
		If the system identifier was not specified an empty string is returned.
		"""
		res = super(QDomEntity,self).systemId()
		return res
