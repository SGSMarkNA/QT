from PySide import QtGui, QtCore

class QWebInspector(QtWebKit.QWebInspector):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebInspector,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def page(self):
		"""
		Returns the inspected PySide.QtWebKit.QWebPage
		If no web page is currently associated, a null pointer is returned.
		"""
		res = super(QWebInspector,self).page()
		isinstance(res,QtWebKit.QWebPage)
		return res
	#----------------------------------------------------------------------
	def setPage(self,page):
		"""
		setPage(page)
			page=QtWebKit.QWebPage

		Bind this inspector to the PySide.QtWebKit.QWebPage to be inspected.
		Notes:
		"""
		res = super(QWebInspector,self).setPage(page)
		return res
