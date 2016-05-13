from PySide import QtGui, QtCore

class QPlainTextDocumentLayout(QtGui.QPlainTextDocumentLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPlainTextDocumentLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cursorWidth(self):
		"""
		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QPlainTextDocumentLayout,self).cursorWidth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def requestUpdate(self):
		"""
		Requests a complete update on all views.
		"""
		res = super(QPlainTextDocumentLayout,self).requestUpdate()
		return res
	#----------------------------------------------------------------------
	def textWidth(self):
		"""

		"""
		res = super(QPlainTextDocumentLayout,self).textWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def blockWidth(self,block):
		"""
		blockWidth(block)
			block=QtGui.QTextBlock


		"""
		res = super(QPlainTextDocumentLayout,self).blockWidth(block)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def ensureBlockLayout(self,block):
		"""
		ensureBlockLayout(block)
			block=QtGui.QTextBlock

		Ensures that block has a valid layout
		"""
		res = super(QPlainTextDocumentLayout,self).ensureBlockLayout(block)
		return res
	#----------------------------------------------------------------------
	def layoutBlock(self,block):
		"""
		layoutBlock(block)
			block=QtGui.QTextBlock


		"""
		res = super(QPlainTextDocumentLayout,self).layoutBlock(block)
		return res
	#----------------------------------------------------------------------
	def setCursorWidth(self,width):
		"""
		setCursorWidth(width)
			width=QtCore.int

		This property specifies the width of the cursor in pixels
		The default value is 1.
		"""
		res = super(QPlainTextDocumentLayout,self).setCursorWidth(width)
		return res
	#----------------------------------------------------------------------
	def setTextWidth(self,newWidth):
		"""
		setTextWidth(newWidth)
			newWidth=QtCore.qreal


		"""
		res = super(QPlainTextDocumentLayout,self).setTextWidth(newWidth)
		return res
