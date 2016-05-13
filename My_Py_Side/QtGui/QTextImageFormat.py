from PySide import QtGui, QtCore

class QTextImageFormat(QtGui.QTextImageFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextImageFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def height(self):
		"""
		Returns the height of the rectangle occupied by the image.
		"""
		res = super(QTextImageFormat,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the image
		The name refers to an entry in the applications resources file.
		"""
		res = super(QTextImageFormat,self).name()
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width of the rectangle occupied by the image.
		"""
		res = super(QTextImageFormat,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,height):
		"""
		setHeight(height)
			height=QtCore.qreal

		Sets the height of the rectangle occupied by the image.
		"""
		res = super(QTextImageFormat,self).setHeight(height)
		return res
	#----------------------------------------------------------------------
	def setName(self,name):
		"""
		setName(name)
			name=unicode

		Sets the name of the image
		The name is used to locate the image in the applications resources.
		"""
		res = super(QTextImageFormat,self).setName(name)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,width):
		"""
		setWidth(width)
			width=QtCore.qreal

		Sets the width of the rectangle occupied by the image.
		"""
		res = super(QTextImageFormat,self).setWidth(width)
		return res
