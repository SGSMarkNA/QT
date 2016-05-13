from PySide import QtGui, QtCore

class QSvgWidget(QtSvg.QSvgWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSvgWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def renderer(self):
		"""
		Returns the renderer used to display the contents of the widget.
		"""
		res = super(QSvgWidget,self).renderer()
		isinstance(res,QtSvg.QSvgRenderer)
		return res
