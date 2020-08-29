from PySide import QtGui, QtCore

class QHttp(QtNetwork.QHttp):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHttp,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bytesAvailable(self):
		"""
		Returns the number of bytes that can be read from the response content at the moment.
		"""
		res = super(QHttp,self).bytesAvailable()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def clearPendingRequests(self):
		"""
		Deletes all pending requests from the list of scheduled requests
		This does not affect the request that is being executed
		If you want to stop this as well, use PySide.QtNetwork.QHttp.abort() .
		"""
		res = super(QHttp,self).clearPendingRequests()
		return res
	#----------------------------------------------------------------------
	def close(self):
		"""
		Closes the connection; this is useful if you have a keep-alive connection and want to close it.
		For the requests issued with PySide.QtNetwork.QHttp.get() , PySide.QtNetwork.QHttp.post() and PySide.QtNetwork.QHttp.head() , PySide.QtNetwork.QHttp sets the connection to be keep-alive
		You can also do this using the header you pass to the PySide.QtNetwork.QHttp.request() function
		PySide.QtNetwork.QHttp only closes the connection to the HTTP server if the response header requires it to do so.
		The function does not block; instead, it returns immediately
		The request is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QHttp.requestStarted() and PySide.QtNetwork.QHttp.requestFinished() .
		When the request is started the PySide.QtNetwork.QHttp.requestStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QHttp.requestFinished() signal is emitted.
		If you want to close the connection immediately, you have to use PySide.QtNetwork.QHttp.abort() instead.
		"""
		res = super(QHttp,self).close()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentDestinationDevice(self):
		"""
		Returns the PySide.QtCore.QIODevice pointer that is used as to store the data of the HTTP request being executed
		If there is no current request or if the request does not store the data to an IO device, this function returns 0.
		This function can be used to delete the PySide.QtCore.QIODevice in the slot connected to the PySide.QtNetwork.QHttp.requestFinished() signal.
		"""
		res = super(QHttp,self).currentDestinationDevice()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def currentId(self):
		"""
		Returns the identifier of the HTTP request being executed or 0 if there is no request being executed (i.e
		theyve all finished).
		"""
		res = super(QHttp,self).currentId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentRequest(self):
		"""
		Returns the request header of the HTTP request being executed
		If the request is one issued by PySide.QtNetwork.QHttp.setHost() or PySide.QtNetwork.QHttp.close() , it returns an invalid request header, i.e
		QHttpRequestHeader.isValid() returns false.
		"""
		res = super(QHttp,self).currentRequest()
		isinstance(res,QtNetwork.QHttpRequestHeader)
		return res
	#----------------------------------------------------------------------
	def currentSourceDevice(self):
		"""
		Returns the PySide.QtCore.QIODevice pointer that is used as the data source of the HTTP request being executed
		If there is no current request or if the request does not use an IO device as the data source, this function returns 0.
		This function can be used to delete the PySide.QtCore.QIODevice in the slot connected to the PySide.QtNetwork.QHttp.requestFinished() signal.
		"""
		res = super(QHttp,self).currentSourceDevice()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the last error that occurred
		This is useful to find out what happened when receiving a PySide.QtNetwork.QHttp.requestFinished() or a PySide.QtNetwork.QHttp.done() signal with the error argument true .
		If you start a new request, the error status is reset to NoError .
		"""
		res = super(QHttp,self).error()
		isinstance(res,QtNetwork.QHttp.Error)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human-readable description of the last error that occurred
		This is useful to present a error message to the user when receiving a PySide.QtNetwork.QHttp.requestFinished() or a PySide.QtNetwork.QHttp.done() signal with the error argument true .
		"""
		res = super(QHttp,self).errorString()
		return res
	#----------------------------------------------------------------------
	def hasPendingRequests(self):
		"""
		Returns true if there are any requests scheduled that have not yet been executed; otherwise returns false.
		The request that is being executed is not considered as a scheduled request.
		"""
		res = super(QHttp,self).hasPendingRequests()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastResponse(self):
		"""
		Returns the received response header of the most recently finished HTTP request
		If no response has yet been received QHttpResponseHeader.isValid() will return false.
		"""
		res = super(QHttp,self).lastResponse()
		isinstance(res,QtNetwork.QHttpResponseHeader)
		return res
	#----------------------------------------------------------------------
	def readAll(self):
		"""
		Reads all the bytes from the response content and returns them.
		"""
		res = super(QHttp,self).readAll()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of the object
		When the state changes, the PySide.QtNetwork.QHttp.stateChanged() signal is emitted.
		"""
		res = super(QHttp,self).state()
		isinstance(res,QtNetwork.QHttp.State)
		return res
	#----------------------------------------------------------------------
	def get(self,path,to=None):
		"""
		get(path,to=None)
			path=unicode
			to=QtCore.QIODevice

		Sends a get request for path to the server set by PySide.QtNetwork.QHttp.setHost() or as specified in the constructor.
		path must be a absolute path like /index.html or an absolute URI like http://example.com/index.html and must be encoded with either QUrl.toPercentEncoding() or QUrl.encodedPath() .
		If the IO device to is 0 the PySide.QtNetwork.QHttp.readyRead() signal is emitted every time new content data is available to read.
		If the IO device to is not 0, the content data of the response is written directly to the device
		Make sure that the to pointer is valid for the duration of the operation (it is safe to delete it when the PySide.QtNetwork.QHttp.requestFinished() signal is emitted).
		"""
		res = super(QHttp,self).get(path,to)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def head(self,path):
		"""
		head(path)
			path=unicode

		Sends a header request for path to the server set by PySide.QtNetwork.QHttp.setHost() or as specified in the constructor.
		path must be an absolute path like /index.html or an absolute URI like http://example.com/index.html .
		The function does not block; instead, it returns immediately
		The request is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QHttp.requestStarted() and PySide.QtNetwork.QHttp.requestFinished() .
		When the request is started the PySide.QtNetwork.QHttp.requestStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QHttp.requestFinished() signal is emitted.
		"""
		res = super(QHttp,self).head(path)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def post(self,*args,**kwargs):
		"""
		post(path,data,to=None)
			path=unicode
			data=QtCore.QByteArray
			to=QtCore.QIODevice

		post(path,data,to=None)
			path=unicode
			data=QtCore.QIODevice
			to=QtCore.QIODevice

		This is an overloaded function.
		data is used as the content data of the HTTP request.
		"""
		res = super(QHttp,self).post(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def read(self,maxlen):
		"""
		read(maxlen)
			maxlen=QtCore.qint64

		Reads maxlen bytes from the response content into data and returns the number of bytes read
		Returns -1 if an error occurred.
		"""
		res = super(QHttp,self).read(maxlen)
		return res
	#----------------------------------------------------------------------
	def request(self,*args,**kwargs):
		"""
		request(header,data,to=None)
			header=QtNetwork.QHttpRequestHeader
			data=QtCore.QByteArray
			to=QtCore.QIODevice

		request(header,device=None,to=None)
			header=QtNetwork.QHttpRequestHeader
			device=QtCore.QIODevice
			to=QtCore.QIODevice

		This is an overloaded function.
		data is used as the content data of the HTTP request.
		"""
		res = super(QHttp,self).request(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setHost(self,*args,**kwargs):
		"""
		setHost(hostname,port=None)
			hostname=unicode
			port=QtCore.quint16

		setHost(hostname,mode,port=None)
			hostname=unicode
			mode=QtNetwork.QHttp.ConnectionMode
			port=QtCore.quint16

		Sets the HTTP server that is used for requests to hostName on port port .
		The function does not block; instead, it returns immediately
		The request is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QHttp.requestStarted() and PySide.QtNetwork.QHttp.requestFinished() .
		When the request is started the PySide.QtNetwork.QHttp.requestStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QHttp.requestFinished() signal is emitted.
		"""
		res = super(QHttp,self).setHost(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,*args,**kwargs):
		"""
		setProxy(host,port,username=None,password=None)
			host=unicode
			port=QtCore.int
			username=unicode
			password=unicode

		setProxy(proxy)
			proxy=QtNetwork.QNetworkProxy

		Enables HTTP proxy support, using the proxy server host on port port
		username and password can be provided if the proxy server requires authentication.
		Example:
		PySide.QtNetwork.QHttp supports non-transparent web proxy servers only, such as the Squid Web proxy cache server (from http://www.squid.org/)
		For transparent proxying, such as SOCKS5, use PySide.QtNetwork.QNetworkProxy instead.
		"""
		res = super(QHttp,self).setProxy(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setSocket(self,socket):
		"""
		setSocket(socket)
			socket=QtNetwork.QTcpSocket

		Replaces the internal PySide.QtNetwork.QTcpSocket that PySide.QtNetwork.QHttp uses with socket
		This is useful if you want to use your own custom PySide.QtNetwork.QTcpSocket subclass instead of the plain PySide.QtNetwork.QTcpSocket that PySide.QtNetwork.QHttp uses by default
		PySide.QtNetwork.QHttp does not take ownership of the socket, and will not delete socket when destroyed.
		The function does not block; instead, it returns immediately
		The request is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QHttp.requestStarted() and PySide.QtNetwork.QHttp.requestFinished() .
		When the request is started the PySide.QtNetwork.QHttp.requestStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QHttp.requestFinished() signal is emitted.
		Note: If PySide.QtNetwork.QHttp is used in a non-GUI thread that runs its own event loop, you must move socket to that thread before calling PySide.QtNetwork.QHttp.setSocket() .
		"""
		res = super(QHttp,self).setSocket(socket)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setUser(self,username,password=None):
		"""
		setUser(username,password=None)
			username=unicode
			password=unicode

		This function sets the user name userName and password password for web pages that require authentication.
		The function does not block; instead, it returns immediately
		The request is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QHttp.requestStarted() and PySide.QtNetwork.QHttp.requestFinished() .
		When the request is started the PySide.QtNetwork.QHttp.requestStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QHttp.requestFinished() signal is emitted.
		"""
		res = super(QHttp,self).setUser(username,password)
		isinstance(res,int)
		return res
