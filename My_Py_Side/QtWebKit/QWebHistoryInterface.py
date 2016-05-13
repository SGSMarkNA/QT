from PySide import QtGui, QtCore

class QWebHistoryInterface(QtWebKit.QWebHistoryInterface):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebHistoryInterface,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def addHistoryEntry(self,url):
		"""
		addHistoryEntry(url)
			url=unicode

		Called by WebKit to add another url to the list of visited pages.
		"""
		res = super(QWebHistoryInterface,self).addHistoryEntry(url)
		return res
	#----------------------------------------------------------------------
	def historyContains(self,url):
		"""
		historyContains(url)
			url=unicode

		Called by the WebKit engine to query whether a certain url has been visited by the user already
		Returns true if the url is part of the history of visited links; otherwise returns false.
		"""
		res = super(QWebHistoryInterface,self).historyContains(url)
		isinstance(res,QtCore.bool)
		return res
