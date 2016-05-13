from PySide import QtGui, QtCore

class QNetworkAccessManager(QtNetwork.QNetworkAccessManager):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkAccessManager,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeConfiguration(self):
		"""
		Returns the current active network configuration.
		If the network configuration returned by PySide.QtNetwork.QNetworkAccessManager.configuration() is of type QNetworkConfiguration.ServiceNetwork this function will return the current active child network configuration of that configuration
		Otherwise returns the same network configuration as PySide.QtNetwork.QNetworkAccessManager.configuration() .
		Use this function to return the actual network configuration currently in use by the network session.
		"""
		res = super(QNetworkAccessManager,self).activeConfiguration()
		isinstance(res,QtNetwork.QNetworkConfiguration)
		return res
	#----------------------------------------------------------------------
	def cache(self):
		"""
		Returns the cache that is used to store data obtained from the network.
		"""
		res = super(QNetworkAccessManager,self).cache()
		isinstance(res,QtNetwork.QAbstractNetworkCache)
		return res
	#----------------------------------------------------------------------
	def configuration(self):
		"""
		Returns the network configuration that will be used to create the network session which will be used when processing network requests.
		"""
		res = super(QNetworkAccessManager,self).configuration()
		isinstance(res,QtNetwork.QNetworkConfiguration)
		return res
	#----------------------------------------------------------------------
	def cookieJar(self):
		"""
		Returns the PySide.QtNetwork.QNetworkCookieJar that is used to store cookies obtained from the network as well as cookies that are about to be sent.
		"""
		res = super(QNetworkAccessManager,self).cookieJar()
		isinstance(res,QtNetwork.QNetworkCookieJar)
		return res
	#----------------------------------------------------------------------
	def networkAccessible(self):
		"""
		This property holds whether the network is currently accessible via this network access manager..
		If the network is not accessible the network access manager will not process any new network requests, all such requests will fail with an error
		Requests with URLs with the file:// scheme will still be processed.
		By default the value of this property reflects the physical state of the device
		Applications may override it to disable all network requests via this network access manager by calling
		Network requests can be reenabled again by calling
		"""
		res = super(QNetworkAccessManager,self).networkAccessible()
		isinstance(res,QtNetwork.QNetworkAccessManager.NetworkAccessibility)
		return res
	#----------------------------------------------------------------------
	def networkSessionConnected(self):
		"""

		"""
		res = super(QNetworkAccessManager,self).networkSessionConnected()
		return res
	#----------------------------------------------------------------------
	def proxy(self):
		"""
		Returns the PySide.QtNetwork.QNetworkProxy that the requests sent using this PySide.QtNetwork.QNetworkAccessManager object will use
		The default value for the proxy is QNetworkProxy.DefaultProxy .
		"""
		res = super(QNetworkAccessManager,self).proxy()
		isinstance(res,QtNetwork.QNetworkProxy)
		return res
	#----------------------------------------------------------------------
	def proxyFactory(self):
		"""
		Returns the proxy factory that this PySide.QtNetwork.QNetworkAccessManager object is using to determine the proxies to be used for requests.
		Note that the pointer returned by this function is managed by PySide.QtNetwork.QNetworkAccessManager and could be deleted at any time.
		"""
		res = super(QNetworkAccessManager,self).proxyFactory()
		isinstance(res,QtNetwork.QNetworkProxyFactory)
		return res
	#----------------------------------------------------------------------
	def createRequest(self,op,request,outgoingData=None):
		"""
		createRequest(op,request,outgoingData=None)
			op=QtNetwork.QNetworkAccessManager.Operation
			request=QtNetwork.QNetworkRequest
			outgoingData=QtCore.QIODevice

		Returns a new PySide.QtNetwork.QNetworkReply object to handle the operation op and request req
		The device outgoingData is always 0 for Get and Head requests, but is the value passed to PySide.QtNetwork.QNetworkAccessManager.post() and PySide.QtNetwork.QNetworkAccessManager.put() in those operations (the PySide.QtCore.QByteArray variants will pass a PySide.QtCore.QBuffer object).
		The default implementation calls QNetworkCookieJar.cookiesForUrl() on the cookie jar set with PySide.QtNetwork.QNetworkAccessManager.setCookieJar() to obtain the cookies to be sent to the remote server.
		The returned object must be in an open state.
		"""
		res = super(QNetworkAccessManager,self).createRequest(op,request,outgoingData)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def deleteResource(self,request):
		"""
		deleteResource(request)
			request=QtNetwork.QNetworkRequest

		Sends a request to delete the resource identified by the URL of request .
		"""
		res = super(QNetworkAccessManager,self).deleteResource(request)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def get(self,request):
		"""
		get(request)
			request=QtNetwork.QNetworkRequest

		Posts a request to obtain the contents of the target request and returns a new PySide.QtNetwork.QNetworkReply object opened for reading which emits the PySide.QtCore.QIODevice.readyRead() signal whenever new data arrives.
		The contents as well as associated headers will be downloaded.
		"""
		res = super(QNetworkAccessManager,self).get(request)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def head(self,request):
		"""
		head(request)
			request=QtNetwork.QNetworkRequest

		Posts a request to obtain the network headers for request and returns a new PySide.QtNetwork.QNetworkReply object which will contain such headers.
		The function is named after the HTTP request associated (HEAD).
		"""
		res = super(QNetworkAccessManager,self).head(request)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def post(self,*args,**kwargs):
		"""
		post(request,data)
			request=QtNetwork.QNetworkRequest
			data=QtCore.QIODevice

		post(request,data)
			request=QtNetwork.QNetworkRequest
			data=QtCore.QByteArray

		Sends an HTTP POST request to the destination specified by request and returns a new PySide.QtNetwork.QNetworkReply object opened for reading that will contain the reply sent by the server
		The contents of the data device will be uploaded to the server.
		data must be open for reading and must remain valid until the PySide.QtNetwork.QNetworkAccessManager.finished() signal is emitted for this reply.
		"""
		res = super(QNetworkAccessManager,self).post(*args,**kwargs)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def put(self,*args,**kwargs):
		"""
		put(request,data)
			request=QtNetwork.QNetworkRequest
			data=QtCore.QByteArray

		put(request,data)
			request=QtNetwork.QNetworkRequest
			data=QtCore.QIODevice

		This is an overloaded function.
		Sends the contents of the data byte array to the destination specified by request .
		"""
		res = super(QNetworkAccessManager,self).put(*args,**kwargs)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def sendCustomRequest(self,request,verb,data=None):
		"""
		sendCustomRequest(request,verb,data=None)
			request=QtNetwork.QNetworkRequest
			verb=QtCore.QByteArray
			data=QtCore.QIODevice

		Sends a custom request to the server identified by the URL of request .
		It is the users responsibility to send a verb to the server that is valid according to the HTTP specification.
		This method provides means to send verbs other than the common ones provided via PySide.QtNetwork.QNetworkAccessManager.get() or PySide.QtNetwork.QNetworkAccessManager.post() etc., for instance sending an HTTP OPTIONS command.
		If data is not empty, the contents of the data device will be uploaded to the server; in that case, data must be open for reading and must remain valid until the PySide.QtNetwork.QNetworkAccessManager.finished() signal is emitted for this reply.
		"""
		res = super(QNetworkAccessManager,self).sendCustomRequest(request,verb,data)
		isinstance(res,QtNetwork.QNetworkReply)
		return res
	#----------------------------------------------------------------------
	def setCache(self,cache):
		"""
		setCache(cache)
			cache=QtNetwork.QAbstractNetworkCache

		Sets the managers network cache to be the cache specified
		The cache is used for all requests dispatched by the manager.
		Use this function to set the network cache object to a class that implements additional features, like saving the cookies to permanent storage.
		PySide.QtNetwork.QNetworkAccessManager by default does not have a set cache
		Qt provides a simple disk cache, PySide.QtNetwork.QNetworkDiskCache , which can be used.
		"""
		res = super(QNetworkAccessManager,self).setCache(cache)
		return res
	#----------------------------------------------------------------------
	def setConfiguration(self,config):
		"""
		setConfiguration(config)
			config=QtNetwork.QNetworkConfiguration

		Sets the network configuration that will be used when creating the network session to config .
		The network configuration is used to create and open a network session before any request that requires network access is process
		If no network configuration is explicitly set via this function the network configuration returned by QNetworkConfigurationManager.defaultConfiguration() will be used.
		To restore the default network configuration set the network configuration to the value returned from QNetworkConfigurationManager.defaultConfiguration() .
		If an invalid network configuration is set, a network session will not be created
		In this case network requests will be processed regardless, but may fail
		For example:
		"""
		res = super(QNetworkAccessManager,self).setConfiguration(config)
		return res
	#----------------------------------------------------------------------
	def setCookieJar(self,cookieJar):
		"""
		setCookieJar(cookieJar)
			cookieJar=QtNetwork.QNetworkCookieJar

		Sets the managers cookie jar to be the cookieJar specified
		The cookie jar is used by all requests dispatched by the manager.
		Use this function to set the cookie jar object to a class that implements additional features, like saving the cookies to permanent storage.
		If cookieJar is in the same thread as this PySide.QtNetwork.QNetworkAccessManager , it will set the parent of the cookieJar so that the cookie jar is deleted when this object is deleted as well
		If you want to share cookie jars between different PySide.QtNetwork.QNetworkAccessManager objects, you may want to set the cookie jars parent to 0 after calling this function.
		PySide.QtNetwork.QNetworkAccessManager by default does not implement any cookie policy of its own: it accepts all cookies sent by the server, as long as they are well formed and meet the minimum security requirements (cookie domain matches the requests and cookie path matches the requests)
		In order to implement your own security policy, override the QNetworkCookieJar.cookiesForUrl() and QNetworkCookieJar.setCookiesFromUrl() virtual functions
		Those functions are called by PySide.QtNetwork.QNetworkAccessManager when it detects a new cookie.
		"""
		res = super(QNetworkAccessManager,self).setCookieJar(cookieJar)
		return res
	#----------------------------------------------------------------------
	def setNetworkAccessible(self,accessible):
		"""
		setNetworkAccessible(accessible)
			accessible=QtNetwork.QNetworkAccessManager.NetworkAccessibility

		This property holds whether the network is currently accessible via this network access manager..
		If the network is not accessible the network access manager will not process any new network requests, all such requests will fail with an error
		Requests with URLs with the file:// scheme will still be processed.
		By default the value of this property reflects the physical state of the device
		Applications may override it to disable all network requests via this network access manager by calling
		Network requests can be reenabled again by calling
		"""
		res = super(QNetworkAccessManager,self).setNetworkAccessible(accessible)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,proxy):
		"""
		setProxy(proxy)
			proxy=QtNetwork.QNetworkProxy

		Sets the proxy to be used in future requests to be proxy
		This does not affect requests that have already been sent
		The PySide.QtNetwork.QNetworkAccessManager.proxyAuthenticationRequired() signal will be emitted if the proxy requests authentication.
		A proxy set with this function will be used for all requests issued by PySide.QtNetwork.QNetworkAccessManager
		In some cases, it might be necessary to select different proxies depending on the type of request being sent or the destination host
		If thats the case, you should consider using PySide.QtNetwork.QNetworkAccessManager.setProxyFactory() .
		"""
		res = super(QNetworkAccessManager,self).setProxy(proxy)
		return res
	#----------------------------------------------------------------------
	def setProxyFactory(self,factory):
		"""
		setProxyFactory(factory)
			factory=QtNetwork.QNetworkProxyFactory

		Sets the proxy factory for this class to be factory
		A proxy factory is used to determine a more specific list of proxies to be used for a given request, instead of trying to use the same proxy value for all requests.
		All queries sent by PySide.QtNetwork.QNetworkAccessManager will have type QNetworkProxyQuery.UrlRequest .
		For example, a proxy factory could apply the following rules:
		The lifetime of the object factory will be managed by PySide.QtNetwork.QNetworkAccessManager
		It will delete the object when necessary.
		"""
		res = super(QNetworkAccessManager,self).setProxyFactory(factory)
		return res
