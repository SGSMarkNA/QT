from PySide import QtGui, QtCore

class QFileOpenEvent(QtGui.QFileOpenEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFileOpenEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def file(self):
		"""
		Returns the file that is being opened.
		"""
		res = super(QFileOpenEvent,self).file()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the url that is being opened.
		"""
		res = super(QFileOpenEvent,self).url()
		isinstance(res,QtCore.QUrl)
		return res
