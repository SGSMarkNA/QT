from PySide import QtGui, QtCore

class QNetworkProxy(QtNetwork.QNetworkProxy):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkProxy,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def capabilities(self):
		"""
		Returns the capabilities of this proxy server.
		"""
		res = super(QNetworkProxy,self).capabilities()
		isinstance(res,QtNetwork.QNetworkProxy.Capabilities)
		return res
	#----------------------------------------------------------------------
	def hostName(self):
		"""
		Returns the host name of the proxy host.
		"""
		res = super(QNetworkProxy,self).hostName()
		return res
	#----------------------------------------------------------------------
	def isCachingProxy(self):
		"""
		Returns true if this proxy supports the QNetworkProxy.CachingCapability capability.
		In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to remove the capability of caching from a proxy by calling PySide.QtNetwork.QNetworkProxy.setCapabilities() .
		"""
		res = super(QNetworkProxy,self).isCachingProxy()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isTransparentProxy(self):
		"""
		Returns true if this proxy supports transparent tunneling of TCP connections
		This matches the QNetworkProxy.TunnelingCapability capability.
		In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to remove the capability of caching from a proxy by calling PySide.QtNetwork.QNetworkProxy.setCapabilities() .
		"""
		res = super(QNetworkProxy,self).isTransparentProxy()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def password(self):
		"""
		Returns the password used for authentication.
		"""
		res = super(QNetworkProxy,self).password()
		return res
	#----------------------------------------------------------------------
	def port(self):
		"""
		Returns the port of the proxy host.
		"""
		res = super(QNetworkProxy,self).port()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the proxy type for this instance.
		"""
		res = super(QNetworkProxy,self).type()
		isinstance(res,QtNetwork.QNetworkProxy.ProxyType)
		return res
	#----------------------------------------------------------------------
	def user(self):
		"""
		Returns the user name used for authentication.
		"""
		res = super(QNetworkProxy,self).user()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkProxy

		Compares the value of this network proxy to other and returns true if they differ.
		"""
		res = super(QNetworkProxy,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkProxy

		Compares the value of this network proxy to other and returns true if they are equal (same proxy type, server as well as username and password)
		"""
		res = super(QNetworkProxy,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setCapabilities(self,capab):
		"""
		setCapabilities(capab)
			capab=QtNetwork.QNetworkProxy.Capabilities


		"""
		res = super(QNetworkProxy,self).setCapabilities(capab)
		return res
	#----------------------------------------------------------------------
	def setHostName(self,hostName):
		"""
		setHostName(hostName)
			hostName=unicode

		Sets the host name of the proxy host to be hostName .
		"""
		res = super(QNetworkProxy,self).setHostName(hostName)
		return res
	#----------------------------------------------------------------------
	def setPassword(self,password):
		"""
		setPassword(password)
			password=unicode

		Sets the password for proxy authentication to be password .
		"""
		res = super(QNetworkProxy,self).setPassword(password)
		return res
	#----------------------------------------------------------------------
	def setPort(self,port):
		"""
		setPort(port)
			port=QtCore.quint16

		Sets the port of the proxy host to be port .
		"""
		res = super(QNetworkProxy,self).setPort(port)
		return res
	#----------------------------------------------------------------------
	def setType(self,type):
		"""
		setType(type)
			type=QtNetwork.QNetworkProxy.ProxyType


		"""
		res = super(QNetworkProxy,self).setType(type)
		return res
	#----------------------------------------------------------------------
	def setUser(self,userName):
		"""
		setUser(userName)
			userName=unicode

		Sets the user name for proxy authentication to be user .
		"""
		res = super(QNetworkProxy,self).setUser(userName)
		return res
