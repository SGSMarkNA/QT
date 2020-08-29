from PySide import QtGui, QtCore

class QNetworkProxyQuery(QtNetwork.QNetworkProxyQuery):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkProxyQuery,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def localPort(self):
		"""
		Returns the port number of the socket that will accept incoming packets from remote servers or -1 if the port is not known.
		"""
		res = super(QNetworkProxyQuery,self).localPort()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def peerHostName(self):
		"""
		Returns the host name or IP address being of the outgoing connection being requested, or an empty string if the remote hostname is not known.
		If the query type is QNetworkProxyQuery.UrlRequest , this function returns the host component of the URL being requested.
		"""
		res = super(QNetworkProxyQuery,self).peerHostName()
		return res
	#----------------------------------------------------------------------
	def peerPort(self):
		"""
		Returns the port number for the outgoing request or -1 if the port number is not known.
		If the query type is QNetworkProxyQuery.UrlRequest , this function returns the port number of the URL being requested
		In general, frameworks will fill in the port number from their default values.
		"""
		res = super(QNetworkProxyQuery,self).peerPort()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def protocolTag(self):
		"""
		Returns the protocol tag for this PySide.QtNetwork.QNetworkProxyQuery object, or an empty PySide.QtCore.QString in case the protocol tag is unknown.
		In the case of queries of type QNetworkProxyQuery.UrlRequest , this function returns the value of the scheme component of the URL.
		"""
		res = super(QNetworkProxyQuery,self).protocolTag()
		return res
	#----------------------------------------------------------------------
	def queryType(self):
		"""
		Returns the query type.
		"""
		res = super(QNetworkProxyQuery,self).queryType()
		isinstance(res,QtNetwork.QNetworkProxyQuery.QueryType)
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the URL component of this PySide.QtNetwork.QNetworkProxyQuery object in case of a query of type QNetworkProxyQuery.UrlRequest .
		"""
		res = super(QNetworkProxyQuery,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkProxyQuery

		Returns true if this PySide.QtNetwork.QNetworkProxyQuery object does not contain the same data as other .
		"""
		res = super(QNetworkProxyQuery,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkProxyQuery

		Returns true if this PySide.QtNetwork.QNetworkProxyQuery object contains the same data as other .
		"""
		res = super(QNetworkProxyQuery,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setLocalPort(self,port):
		"""
		setLocalPort(port)
			port=QtCore.int

		Sets the port number that the socket wishes to use locally to accept incoming packets from remote servers to port
		The local port is most often used with the QNetworkProxyQuery.TcpServer and QNetworkProxyQuery.UdpSocket query types.
		Valid values are 0 to 65535 (with 0 indicating that any port number will be acceptable) or -1, which means the local port number is unknown or not applicable.
		In some circumstances, for special protocols, its the local port number can also be used with a query of type QNetworkProxyQuery.TcpSocket
		When that happens, the socket is indicating it wishes to use the port number port when connecting to a remote host.
		"""
		res = super(QNetworkProxyQuery,self).setLocalPort(port)
		return res
	#----------------------------------------------------------------------
	def setPeerHostName(self,hostname):
		"""
		setPeerHostName(hostname)
			hostname=unicode

		Sets the hostname of the outgoing connection being requested to hostname
		An empty hostname can be used to indicate that the remote host is unknown.
		The peer host name can also be used to indicate the expected source address of an incoming connection in the case of QNetworkProxyQuery.UdpSocket or QNetworkProxyQuery.TcpServer query types.
		"""
		res = super(QNetworkProxyQuery,self).setPeerHostName(hostname)
		return res
	#----------------------------------------------------------------------
	def setPeerPort(self,port):
		"""
		setPeerPort(port)
			port=QtCore.int

		Sets the requested port number for the outgoing connection to be port
		Valid values are 1 to 65535, or -1 to indicate that the remote port number is unknown.
		The peer port number can also be used to indicate the expected port number of an incoming connection in the case of QNetworkProxyQuery.UdpSocket or QNetworkProxyQuery.TcpServer query types.
		"""
		res = super(QNetworkProxyQuery,self).setPeerPort(port)
		return res
	#----------------------------------------------------------------------
	def setProtocolTag(self,protocolTag):
		"""
		setProtocolTag(protocolTag)
			protocolTag=unicode

		Sets the protocol tag for this PySide.QtNetwork.QNetworkProxyQuery object to be protocolTag .
		The protocol tag is an arbitrary string that indicates which protocol is being talked over the socket, such as http, xmpp, telnet, etc
		The protocol tag is used by the backend to return a request that is more specific to the protocol in question: for example, a HTTP connection could be use a caching HTTP proxy server, while all other connections use a more powerful SOCKSv5 proxy server.
		"""
		res = super(QNetworkProxyQuery,self).setProtocolTag(protocolTag)
		return res
	#----------------------------------------------------------------------
	def setQueryType(self,type):
		"""
		setQueryType(type)
			type=QtNetwork.QNetworkProxyQuery.QueryType

		Sets the query type of this object to be type .
		"""
		res = super(QNetworkProxyQuery,self).setQueryType(type)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		Sets the URL component of this PySide.QtNetwork.QNetworkProxyQuery object to be url
		Setting the URL will also set the protocol tag, the remote host name and port number
		This is done so as to facilitate the implementation of the code that determines the proxy server to be used.
		"""
		res = super(QNetworkProxyQuery,self).setUrl(url)
		return res
