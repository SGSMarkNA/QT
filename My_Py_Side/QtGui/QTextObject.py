from PySide import QtGui, QtCore

class QTextObject(QtGui.QTextObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def document(self):
		"""
		Returns the document this object belongs to.
		"""
		res = super(QTextObject,self).document()
		isinstance(res,QtGui.QTextDocument)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the text objects format.
		"""
		res = super(QTextObject,self).format()
		isinstance(res,QtGui.QTextFormat)
		return res
	#----------------------------------------------------------------------
	def formatIndex(self):
		"""
		Returns the index of the objects format in the documents internal list of formats.
		"""
		res = super(QTextObject,self).formatIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def objectIndex(self):
		"""
		Returns the object index of this object
		This can be used together with QTextFormat.setObjectIndex() .
		"""
		res = super(QTextObject,self).objectIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtGui.QTextFormat

		Sets the text objects format .
		"""
		res = super(QTextObject,self).setFormat(format)
		return res
