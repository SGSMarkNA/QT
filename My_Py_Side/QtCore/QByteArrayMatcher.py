from PySide import QtGui, QtCore

class QByteArrayMatcher(QtCore.QByteArrayMatcher):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QByteArrayMatcher,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def pattern(self):
		"""
		Returns the byte array pattern that this byte array matcher will search for.
		"""
		res = super(QByteArrayMatcher,self).pattern()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def indexIn(self,*args,**kwargs):
		"""
		indexIn(str,len,from=None)
			str=str
			len=QtCore.int
			from=QtCore.int

		indexIn(ba,from=None)
			ba=QtCore.QByteArray
			from=QtCore.int

		Searches the char string str , which has length len , from byte position from (default 0, i.e
		from the first byte), for the byte array PySide.QtCore.QByteArrayMatcher.pattern() that was set in the constructor or in the most recent call to PySide.QtCore.QByteArrayMatcher.setPattern()
		Returns the position where the PySide.QtCore.QByteArrayMatcher.pattern() matched in str , or -1 if no match was found.
		"""
		res = super(QByteArrayMatcher,self).indexIn(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setPattern(self,pattern):
		"""
		setPattern(pattern)
			pattern=QtCore.QByteArray

		Sets the byte array that this byte array matcher will search for to pattern .
		"""
		res = super(QByteArrayMatcher,self).setPattern(pattern)
		return res
