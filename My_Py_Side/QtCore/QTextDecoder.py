from PySide import QtGui, QtCore

class QTextDecoder(QtCore.QTextDecoder):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextDecoder,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasFailure(self):
		"""
		Determines whether the decoder encountered a failure while decoding the input
		If an error was encountered, the produced result is undefined, and gets converted as according to the conversion flags.
		"""
		res = super(QTextDecoder,self).hasFailure()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toUnicode(self,ba):
		"""
		toUnicode(ba)
			ba=QtCore.QByteArray

		This is an overloaded function.
		Converts the bytes in the byte array specified by ba to Unicode and returns the result.
		"""
		res = super(QTextDecoder,self).toUnicode(ba)
		return res
