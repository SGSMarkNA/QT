from PySide import QtGui, QtCore

class QDomProcessingInstruction(QtXml.QDomProcessingInstruction):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomProcessingInstruction,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the content of this processing instruction.
		"""
		res = super(QDomProcessingInstruction,self).data()
		return res
	#----------------------------------------------------------------------
	def target(self):
		"""
		Returns the target of this processing instruction.
		"""
		res = super(QDomProcessingInstruction,self).target()
		return res
	#----------------------------------------------------------------------
	def setData(self,d):
		"""
		setData(d)
			d=unicode

		Sets the data contained in the processing instruction to d .
		"""
		res = super(QDomProcessingInstruction,self).setData(d)
		return res
