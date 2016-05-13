from PySide import QtGui, QtCore

class QTextItem(QtGui.QTextItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def ascent(self):
		"""
		Corresponds to the PySide.QtGui.QFontMetrics.ascent() of the piece of text that is drawn.
		"""
		res = super(QTextItem,self).ascent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def descent(self):
		"""
		Corresponds to the PySide.QtGui.QFontMetrics.descent() of the piece of text that is drawn.
		"""
		res = super(QTextItem,self).descent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font that should be used to draw the text.
		"""
		res = super(QTextItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def renderFlags(self):
		"""
		Returns the render flags used.
		"""
		res = super(QTextItem,self).renderFlags()
		isinstance(res,QtGui.QTextItem.RenderFlags)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the text that should be drawn.
		"""
		res = super(QTextItem,self).text()
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Specifies the total width of the text to be drawn.
		"""
		res = super(QTextItem,self).width()
		isinstance(res,QtCore.qreal)
		return res
