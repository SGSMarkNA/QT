from PySide import QtGui, QtCore

class QXmlParseException(QtXml.QXmlParseException):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlParseException,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnNumber(self):
		"""
		Returns the column number where the error occurred.
		"""
		res = super(QXmlParseException,self).columnNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def lineNumber(self):
		"""
		Returns the line number where the error occurred.
		"""
		res = super(QXmlParseException,self).lineNumber()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def message(self):
		"""
		Returns the error message.
		"""
		res = super(QXmlParseException,self).message()
		return res
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier where the error occurred.
		"""
		res = super(QXmlParseException,self).publicId()
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier where the error occurred.
		"""
		res = super(QXmlParseException,self).systemId()
		return res
