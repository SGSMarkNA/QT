from PySide import QtGui, QtCore

class QTextDocumentFragment(QtGui.QTextDocumentFragment):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextDocumentFragment,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the fragment is empty; otherwise returns false.
		"""
		res = super(QTextDocumentFragment,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toHtml(self):
		"""
		This is an overloaded function.
		"""
		res = super(QTextDocumentFragment,self).toHtml()
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		Returns the document fragments text as plain text (i.e
		with no formatting information).
		"""
		res = super(QTextDocumentFragment,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def toHtml(self,encoding):
		"""
		toHtml(encoding)
			encoding=QtCore.QByteArray

		Returns the contents of the document fragment as HTML, using the specified encoding (e.g., UTF-8, ISO 8859-1).
		"""
		res = super(QTextDocumentFragment,self).toHtml(encoding)
		return res
