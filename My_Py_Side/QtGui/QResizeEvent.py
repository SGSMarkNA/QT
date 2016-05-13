from PySide import QtGui, QtCore

class QResizeEvent(QtGui.QResizeEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QResizeEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def oldSize(self):
		"""
		Returns the old size of the widget.
		"""
		res = super(QResizeEvent,self).oldSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the new size of the widget
		This is the same as QWidget.size() .
		"""
		res = super(QResizeEvent,self).size()
		isinstance(res,QtCore.QSize)
		return res
