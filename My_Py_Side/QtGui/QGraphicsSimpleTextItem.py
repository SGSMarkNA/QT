from PySide import QtGui, QtCore

class QGraphicsSimpleTextItem(QtGui.QGraphicsSimpleTextItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSimpleTextItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font that is used to draw the items text.
		"""
		res = super(QGraphicsSimpleTextItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the items text.
		"""
		res = super(QGraphicsSimpleTextItem,self).text()
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font that is used to draw the items text to font .
		"""
		res = super(QGraphicsSimpleTextItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the items text to text
		The text will be displayed as plain text
		Newline characters (n) as well as characters of type QChar.LineSeparator will cause item to break the text into multiple lines.
		"""
		res = super(QGraphicsSimpleTextItem,self).setText(text)
		return res
