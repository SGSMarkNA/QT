from PySide import QtGui, QtCore

class QNetworkProxyFactory(QtNetwork.QNetworkProxyFactory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkProxyFactory,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def queryProxy(self,query=None):
		"""
		queryProxy(query=None)
			query=QtNetwork.QNetworkProxyQuery

		This function examines takes the query request, query , examines the details of the type of socket or request and returns a list of PySide.QtNetwork.QNetworkProxy objects that indicate the proxy servers to be used, in order of preference.
		When reimplementing this class, take care to return at least one element.
		If you cannot determine a better proxy alternative, use QNetworkProxy.DefaultProxy , which tells the code querying for a proxy to use a higher alternative
		For example, if this factory is set to a PySide.QtNetwork.QNetworkAccessManager object, DefaultProxy will tell it to query the application-level proxy settings.
		If this factory is set as the application proxy factory, DefaultProxy and NoProxy will have the same meaning.
		"""
		res = super(QNetworkProxyFactory,self).queryProxy(query)
		return res
