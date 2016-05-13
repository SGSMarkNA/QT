from PySide import QtGui, QtCore

class QDomNotation(QtXml.QDomNotation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomNotation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def publicId(self):
		"""
		Returns the public identifier of this notation.
		"""
		res = super(QDomNotation,self).publicId()
		return res
	#----------------------------------------------------------------------
	def systemId(self):
		"""
		Returns the system identifier of this notation.
		"""
		res = super(QDomNotation,self).systemId()
		return res
