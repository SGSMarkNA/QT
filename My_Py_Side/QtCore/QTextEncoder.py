from PySide import QtGui, QtCore

class QTextEncoder(QtCore.QTextEncoder):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextEncoder,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasFailure(self):
		"""
		Determines whether the eecoder encountered a failure while decoding the input
		If an error was encountered, the produced result is undefined, and gets converted as according to the conversion flags.
		"""
		res = super(QTextEncoder,self).hasFailure()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fromUnicode(self,str):
		"""
		fromUnicode(str)
			str=unicode

		Converts the Unicode string str into an encoded PySide.QtCore.QByteArray .
		"""
		res = super(QTextEncoder,self).fromUnicode(str)
		isinstance(res,QtCore.QByteArray)
		return res
