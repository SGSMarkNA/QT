from PySide import QtGui, QtCore

class QMotifStyle(QtGui.QMotifStyle):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMotifStyle,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def useHighlightColors(self):
		"""
		Returns true if the style treats the highlight colors of the palette in a Motif-like manner, which is a simple inversion between the base and the text color; otherwise returns false
		The default is false.
		"""
		res = super(QMotifStyle,self).useHighlightColors()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setUseHighlightColors(self,arg__1):
		"""
		setUseHighlightColors(arg__1)
			arg__1=QtCore.bool

		If arg is false, the style will polish the applications color palette to emulate the Motif way of highlighting, which is a simple inversion between the base and the text color.
		The effect will show up the next time an application palette is set via QApplication.setPalette()
		The current color palette of the application remains unchanged.
		"""
		res = super(QMotifStyle,self).setUseHighlightColors(arg__1)
		return res
