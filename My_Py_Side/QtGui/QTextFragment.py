from PySide import QtGui, QtCore

class QTextFragment(QtGui.QTextFragment):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextFragment,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def charFormat(self):
		"""
		Returns the text fragments character format.
		"""
		res = super(QTextFragment,self).charFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def charFormatIndex(self):
		"""
		Returns an index into the documents internal list of character formats for the text fragments character format.
		"""
		res = super(QTextFragment,self).charFormatIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this is a valid text fragment (i.e
		has a valid position in a document); otherwise returns false.
		"""
		res = super(QTextFragment,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the number of characters in the text fragment.
		"""
		res = super(QTextFragment,self).length()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		Returns the position of this text fragment in the document.
		"""
		res = super(QTextFragment,self).position()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the text fragments as plain text.
		"""
		res = super(QTextFragment,self).text()
		return res
	#----------------------------------------------------------------------
	def contains(self,position):
		"""
		contains(position)
			position=QtCore.int

		Returns true if the text fragment contains the text at the given position in the document; otherwise returns false.
		"""
		res = super(QTextFragment,self).contains(position)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,o):
		"""
		__ne__(o)
			o=QtGui.QTextFragment

		Returns true if this text fragment is different (at a different position) from the other text fragment; otherwise returns false.
		"""
		res = super(QTextFragment,self).__ne__(o)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,o):
		"""
		__lt__(o)
			o=QtGui.QTextFragment

		Returns true if this text fragment appears earlier in the document than the other text fragment; otherwise returns false.
		"""
		res = super(QTextFragment,self).__lt__(o)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,o):
		"""
		__eq__(o)
			o=QtGui.QTextFragment

		Returns true if this text fragment is the same (at the same position) as the other text fragment; otherwise returns false.
		"""
		res = super(QTextFragment,self).__eq__(o)
		isinstance(res,bool)
		return res
