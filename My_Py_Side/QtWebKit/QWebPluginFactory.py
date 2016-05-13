from PySide import QtGui, QtCore

class QWebPluginFactory(QtWebKit.QWebPluginFactory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebPluginFactory,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtWebKit.QWebPluginFactory::MimeType

		Returns true if this mimetype is different from the other mime type.
		"""
		res = super(QWebPluginFactory,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtWebKit.QWebPluginFactory::MimeType

		Returns true if this mimetype is the same as the other mime type.
		"""
		res = super(QWebPluginFactory,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
