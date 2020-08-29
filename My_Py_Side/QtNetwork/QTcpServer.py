from PySide import QtGui, QtCore

class QTcpServer(QtNetwork.QTcpServer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTcpServer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def close(self):
		"""
		Closes the server
		The server will no longer listen for incoming connections.
		"""
		res = super(QTcpServer,self).close()
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human readable description of the last error that occurred.
		"""
		res = super(QTcpServer,self).errorString()
		return res
	#----------------------------------------------------------------------
	def hasPendingConnections(self):
		"""
		Returns true if the server has a pending connection; otherwise returns false.
		"""
		res = super(QTcpServer,self).hasPendingConnections()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isListening(self):
		"""
		Returns true if the server is currently listening for incoming connections; otherwise returns false.
		"""
		res = super(QTcpServer,self).isListening()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def maxPendingConnections(self):
		"""
		Returns the maximum number of pending accepted connections
		The default is 30.
		"""
		res = super(QTcpServer,self).maxPendingConnections()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def newConnection(self):
		"""

		"""
		res = super(QTcpServer,self).newConnection()
		return res
	#----------------------------------------------------------------------
	def nextPendingConnection(self):
		"""
		Returns the next pending connection as a connected PySide.QtNetwork.QTcpSocket object.
		The socket is created as a child of the server, which means that it is automatically deleted when the PySide.QtNetwork.QTcpServer object is destroyed
		It is still a good idea to delete the object explicitly when you are done with it, to avoid wasting memory.
		0 is returned if this function is called when there are no pending connections.
		"""
		res = super(QTcpServer,self).nextPendingConnection()
		isinstance(res,QtNetwork.QTcpSocket)
		return res
	#----------------------------------------------------------------------
	def proxy(self):
		"""
		Returns the network proxy for this socket
		By default QNetworkProxy.DefaultProxy is used.
		"""
		res = super(QTcpServer,self).proxy()
		isinstance(res,QtNetwork.QNetworkProxy)
		return res
	#----------------------------------------------------------------------
	def serverAddress(self):
		"""
		Returns the servers address if the server is listening for connections; otherwise returns QHostAddress.Null .
		"""
		res = super(QTcpServer,self).serverAddress()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def serverError(self):
		"""
		Returns an error code for the last error that occurred.
		"""
		res = super(QTcpServer,self).serverError()
		isinstance(res,QtNetwork.QAbstractSocket.SocketError)
		return res
	#----------------------------------------------------------------------
	def serverPort(self):
		"""
		Returns the servers port if the server is listening for connections; otherwise returns 0.
		"""
		res = super(QTcpServer,self).serverPort()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def socketDescriptor(self):
		"""
		Returns the native socket descriptor the server uses to listen for incoming instructions, or -1 if the server is not listening.
		If the server is using PySide.QtNetwork.QNetworkProxy , the returned descriptor may not be usable with native socket functions.
		"""
		res = super(QTcpServer,self).socketDescriptor()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addPendingConnection(self,socket):
		"""
		addPendingConnection(socket)
			socket=QtNetwork.QTcpSocket

		This function is called by QTcpServer.incomingConnection() to add the socket to the list of pending incoming connections.
		"""
		res = super(QTcpServer,self).addPendingConnection(socket)
		return res
	#----------------------------------------------------------------------
	def incomingConnection(self,handle):
		"""
		incomingConnection(handle)
			handle=QtCore.int

		This virtual function is called by PySide.QtNetwork.QTcpServer when a new connection is available
		The socketDescriptor argument is the native socket descriptor for the accepted connection.
		The base implementation creates a PySide.QtNetwork.QTcpSocket , sets the socket descriptor and then stores the PySide.QtNetwork.QTcpSocket in an internal list of pending connections
		Finally PySide.QtNetwork.QTcpServer.newConnection() is emitted.
		Reimplement this function to alter the servers behavior when a connection is available.
		If this server is using PySide.QtNetwork.QNetworkProxy then the socketDescriptor may not be usable with native socket functions, and should only be used with QTcpSocket.setSocketDescriptor() .
		"""
		res = super(QTcpServer,self).incomingConnection(handle)
		return res
	#----------------------------------------------------------------------
	def listen(self,address=None,port=None):
		"""
		listen(address=None,port=None)
			address=QtNetwork.QHostAddress
			port=QtCore.quint16

		Tells the server to listen for incoming connections on address address and port port
		If port is 0, a port is chosen automatically
		If address is QHostAddress.Any , the server will listen on all network interfaces.
		Returns true on success; otherwise returns false.
		"""
		res = super(QTcpServer,self).listen(address,port)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setMaxPendingConnections(self,numConnections):
		"""
		setMaxPendingConnections(numConnections)
			numConnections=QtCore.int

		Sets the maximum number of pending accepted connections to numConnections
		PySide.QtNetwork.QTcpServer will accept no more than numConnections incoming connections before PySide.QtNetwork.QTcpServer.nextPendingConnection() is called
		By default, the limit is 30 pending connections.
		Clients may still able to connect after the server has reached its maximum number of pending connections (i.e., PySide.QtNetwork.QTcpSocket can still emit the connected() signal)
		PySide.QtNetwork.QTcpServer will stop accepting the new connections, but the operating system may still keep them in queue.
		"""
		res = super(QTcpServer,self).setMaxPendingConnections(numConnections)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,networkProxy):
		"""
		setProxy(networkProxy)
			networkProxy=QtNetwork.QNetworkProxy

		Sets the explicit network proxy for this socket to networkProxy .
		To disable the use of a proxy for this socket, use the QNetworkProxy.NoProxy proxy type:
		"""
		res = super(QTcpServer,self).setProxy(networkProxy)
		return res
	#----------------------------------------------------------------------
	def setSocketDescriptor(self,socketDescriptor):
		"""
		setSocketDescriptor(socketDescriptor)
			socketDescriptor=QtCore.int

		Sets the socket descriptor this server should use when listening for incoming connections to socketDescriptor
		Returns true if the socket is set successfully; otherwise returns false.
		The socket is assumed to be in listening state.
		"""
		res = super(QTcpServer,self).setSocketDescriptor(socketDescriptor)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def waitForNewConnection(self,msec):
		"""
		waitForNewConnection(msec)
			msec=QtCore.int

		Waits for at most msec milliseconds or until an incoming connection is available
		Returns true if a connection is available; otherwise returns false
		If the operation timed out and timedOut is not 0, *``timedOut`` will be set to true.
		This is a blocking function call
		Its use is disadvised in a single-threaded GUI application, since the whole application will stop responding until the function returns
		PySide.QtNetwork.QTcpServer.waitForNewConnection() is mostly useful when there is no event loop available.
		The non-blocking alternative is to connect to the PySide.QtNetwork.QTcpServer.newConnection() signal.
		If msec is -1, this function will not time out.
		"""
		res = super(QTcpServer,self).waitForNewConnection(msec)
		return res
