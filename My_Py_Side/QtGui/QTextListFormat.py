from PySide import QtGui, QtCore

class QTextListFormat(QtGui.QTextListFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextListFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def indent(self):
		"""
		Returns the list formats indentation
		The indentation is multiplied by the QTextDocument.indentWidth property to get the effective indent in pixels.
		"""
		res = super(QTextListFormat,self).indent()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the list formats style.
		"""
		res = super(QTextListFormat,self).style()
		isinstance(res,QtGui.QTextListFormat.Style)
		return res
	#----------------------------------------------------------------------
	def setIndent(self,indent):
		"""
		setIndent(indent)
			indent=QtCore.int

		Sets the list formats indentation
		The indentation is multiplied by the QTextDocument.indentWidth property to get the effective indent in pixels.
		"""
		res = super(QTextListFormat,self).setIndent(indent)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,style):
		"""
		setStyle(style)
			style=QtGui.QTextListFormat.Style

		Sets the list formats style .
		"""
		res = super(QTextListFormat,self).setStyle(style)
		return res
