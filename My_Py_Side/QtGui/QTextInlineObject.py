from PySide import QtGui, QtCore

class QTextInlineObject(QtGui.QTextInlineObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextInlineObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def ascent(self):
		"""
		Returns the inline objects ascent.
		"""
		res = super(QTextInlineObject,self).ascent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def descent(self):
		"""
		Returns the inline objects descent.
		"""
		res = super(QTextInlineObject,self).descent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns format of the inline object within the text layout.
		"""
		res = super(QTextInlineObject,self).format()
		isinstance(res,QtGui.QTextFormat)
		return res
	#----------------------------------------------------------------------
	def formatIndex(self):
		"""
		Returns an integer describing the format of the inline object within the text layout.
		"""
		res = super(QTextInlineObject,self).formatIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the inline objects total height
		This is equal to PySide.QtGui.QTextInlineObject.ascent() + PySide.QtGui.QTextInlineObject.descent() + 1.
		"""
		res = super(QTextInlineObject,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this inline object is valid; otherwise returns false.
		"""
		res = super(QTextInlineObject,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the inline objects rectangle.
		"""
		res = super(QTextInlineObject,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def textDirection(self):
		"""
		Returns if the object should be laid out right-to-left or left-to-right.
		"""
		res = super(QTextInlineObject,self).textDirection()
		isinstance(res,QtCore.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def textPosition(self):
		"""
		The position of the inline object within the text layout.
		"""
		res = super(QTextInlineObject,self).textPosition()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the inline objects width.
		"""
		res = super(QTextInlineObject,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setAscent(self,a):
		"""
		setAscent(a)
			a=QtCore.qreal

		Sets the inline objects ascent to a .
		"""
		res = super(QTextInlineObject,self).setAscent(a)
		return res
	#----------------------------------------------------------------------
	def setDescent(self,d):
		"""
		setDescent(d)
			d=QtCore.qreal

		Sets the inline objects decent to d .
		"""
		res = super(QTextInlineObject,self).setDescent(d)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,w):
		"""
		setWidth(w)
			w=QtCore.qreal

		Sets the inline objects width to w .
		"""
		res = super(QTextInlineObject,self).setWidth(w)
		return res
