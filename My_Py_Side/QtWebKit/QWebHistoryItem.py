from PySide import QtGui, QtCore

class QWebHistoryItem(QtWebKit.QWebHistoryItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebHistoryItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def icon(self):
		"""
		Returns the icon associated with the history item.
		"""
		res = super(QWebHistoryItem,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns whether this is a valid history item.
		"""
		res = super(QWebHistoryItem,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lastVisited(self):
		"""
		Returns the date and time that the page associated with the item was last visited.
		"""
		res = super(QWebHistoryItem,self).lastVisited()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def originalUrl(self):
		"""
		Returns the original URL associated with the history item.
		"""
		res = super(QWebHistoryItem,self).originalUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		Returns the title of the page associated with the history item.
		"""
		res = super(QWebHistoryItem,self).title()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the URL associated with the history item.
		"""
		res = super(QWebHistoryItem,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def userData(self):
		"""
		Returns the user specific data that was stored with the history item.
		"""
		res = super(QWebHistoryItem,self).userData()
		return res
	#----------------------------------------------------------------------
	def setUserData(self,userData):
		"""
		setUserData(userData)
			userData=object

		Stores user specific data userData with the history item.
		"""
		res = super(QWebHistoryItem,self).setUserData(userData)
		return res
