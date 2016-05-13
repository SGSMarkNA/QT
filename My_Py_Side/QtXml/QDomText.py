from PySide import QtGui, QtCore

class QDomText(QtXml.QDomText):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomText,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def splitText(self,offset):
		"""
		splitText(offset)
			offset=QtCore.int

		Splits this DOM text object into two PySide.QtXml.QDomText objects
		This object keeps its first offset characters and the second (newly created) object is inserted into the document tree after this object with the remaining characters.
		The function returns the newly created object.
		"""
		res = super(QDomText,self).splitText(offset)
		isinstance(res,QtXml.QDomText)
		return res
