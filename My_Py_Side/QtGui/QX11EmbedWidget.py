from PySide import QtGui, QtCore

class QX11EmbedWidget(QtGui.QX11EmbedWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QX11EmbedWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def containerClosed(self):
		"""

		"""
		res = super(QX11EmbedWidget,self).containerClosed()
		return res
	#----------------------------------------------------------------------
	def containerWinId(self):
		"""
		If the widget is embedded, returns the window ID of the container; otherwize returns 0.
		"""
		res = super(QX11EmbedWidget,self).containerWinId()
		return res
	#----------------------------------------------------------------------
	def embedded(self):
		"""

		"""
		res = super(QX11EmbedWidget,self).embedded()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that occurred last
		This is the same error code that is emitted by the PySide.QtGui.QX11EmbedWidget.error() signal.
		"""
		res = super(QX11EmbedWidget,self).error()
		isinstance(res,QtGui.QX11EmbedWidget.Error)
		return res
	#----------------------------------------------------------------------
	def embedInto(self,id):
		"""
		embedInto(id)
			id=long


		"""
		res = super(QX11EmbedWidget,self).embedInto(id)
		return res
	#----------------------------------------------------------------------
	def error(self,error):
		"""
		error(error)
			error=QtGui.QX11EmbedWidget.Error


		"""
		res = super(QX11EmbedWidget,self).error(error)
		return res
