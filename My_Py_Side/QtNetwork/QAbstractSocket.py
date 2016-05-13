from PySide import QtGui, QtCore

class QAbstractSocket(QtNetwork.QAbstractSocket):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractSocket,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def abort(self):
		"""
		Aborts the current connection and resets the socket
		Unlike PySide.QtNetwork.QAbstractSocket.disconnectFromHost() , this function immediately closes the socket, discarding any pending data in the write buffer.
		"""
		res = super(QAbstractSocket,self).abort()
		return res
	#----------------------------------------------------------------------
	def connected(self):
		"""

		"""
		res = super(QAbstractSocket,self).connected()
		return res
	#----------------------------------------------------------------------
	def disconnectFromHost(self):
		"""
		Attempts to close the socket
		If there is pending data waiting to be written, PySide.QtNetwork.QAbstractSocket will enter ClosingState and wait until all data has been written
		Eventually, it will enter UnconnectedState and emit the PySide.QtNetwork.QAbstractSocket.disconnected() signal.
		"""
		res = super(QAbstractSocket,self).disconnectFromHost()
		return res
	#----------------------------------------------------------------------
	def disconnected(self):
		"""

		"""
		res = super(QAbstractSocket,self).disconnected()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that last occurred.
		"""
		res = super(QAbstractSocket,self).error()
		isinstance(res,QtNetwork.QAbstractSocket.SocketError)
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		This function writes as much as possible from the internal write buffer to the underlying network socket, without blocking
		If any data was written, this function returns true; otherwise false is returned.
		Call this function if you need PySide.QtNetwork.QAbstractSocket to start sending buffered data immediately
		The number of bytes successfully written depends on the operating system
		In most cases, you do not need to call this function, because PySide.QtNetwork.QAbstractSocket will start sending data automatically once control goes back to the event loop
		In the absence of an event loop, call PySide.QtNetwork.QAbstractSocket.waitForBytesWritten() instead.
		"""
		res = super(QAbstractSocket,self).flush()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hostFound(self):
		"""

		"""
		res = super(QAbstractSocket,self).hostFound()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the socket is valid and ready for use; otherwise returns false.
		"""
		res = super(QAbstractSocket,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def localAddress(self):
		"""
		Returns the host address of the local socket if available; otherwise returns QHostAddress.Null .
		This is normally the main IP address of the host, but can be QHostAddress.LocalHost (127.0.0.1) for connections to the local host.
		"""
		res = super(QAbstractSocket,self).localAddress()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def localPort(self):
		"""
		Returns the host port number (in native byte order) of the local socket if available; otherwise returns 0.
		"""
		res = super(QAbstractSocket,self).localPort()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def peerAddress(self):
		"""
		Returns the address of the connected peer if the socket is in ConnectedState ; otherwise returns QHostAddress.Null .
		"""
		res = super(QAbstractSocket,self).peerAddress()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def peerName(self):
		"""
		Returns the name of the peer as specified by PySide.QtNetwork.QAbstractSocket.connectToHost() , or an empty PySide.QtCore.QString if PySide.QtNetwork.QAbstractSocket.connectToHost() has not been called.
		"""
		res = super(QAbstractSocket,self).peerName()
		return res
	#----------------------------------------------------------------------
	def peerPort(self):
		"""
		Returns the port of the connected peer if the socket is in ConnectedState ; otherwise returns 0.
		"""
		res = super(QAbstractSocket,self).peerPort()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def proxy(self):
		"""
		Returns the network proxy for this socket
		By default QNetworkProxy.DefaultProxy is used, which means this socket will query the default proxy settings for the application.
		"""
		res = super(QAbstractSocket,self).proxy()
		isinstance(res,QtNetwork.QNetworkProxy)
		return res
	#----------------------------------------------------------------------
	def readBufferSize(self):
		"""
		Returns the size of the internal read buffer
		This limits the amount of data that the client can receive before you call PySide.QtCore.QIODevice.read() or PySide.QtCore.QIODevice.readAll() .
		A read buffer size of 0 (the default) means that the buffer has no size limit, ensuring that no data is lost.
		"""
		res = super(QAbstractSocket,self).readBufferSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def socketDescriptor(self):
		"""
		Returns the native socket descriptor of the PySide.QtNetwork.QAbstractSocket object if this is available; otherwise returns -1.
		If the socket is using PySide.QtNetwork.QNetworkProxy , the returned descriptor may not be usable with native socket functions.
		The socket descriptor is not available when PySide.QtNetwork.QAbstractSocket is in UnconnectedState .
		"""
		res = super(QAbstractSocket,self).socketDescriptor()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def socketType(self):
		"""
		Returns the socket type (TCP, UDP, or other).
		"""
		res = super(QAbstractSocket,self).socketType()
		isinstance(res,QtNetwork.QAbstractSocket.SocketType)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the state of the socket.
		"""
		res = super(QAbstractSocket,self).state()
		isinstance(res,QtNetwork.QAbstractSocket.SocketState)
		return res
	#----------------------------------------------------------------------
	def connectToHost(self,*args,**kwargs):
		"""
		connectToHost(hostName,port,mode=None)
			hostName=unicode
			port=QtCore.quint16
			mode=QtCore.QIODevice.OpenMode

		connectToHost(address,port,mode=None)
			address=QtNetwork.QHostAddress
			port=QtCore.quint16
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QAbstractSocket,self).connectToHost(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def error(self,arg__1):
		"""
		error(arg__1)
			arg__1=QtNetwork.QAbstractSocket.SocketError


		"""
		res = super(QAbstractSocket,self).error(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLocalAddress(self,address):
		"""
		setLocalAddress(address)
			address=QtNetwork.QHostAddress

		Sets the address on the local side of a connection to address .
		You can call this function in a subclass of PySide.QtNetwork.QAbstractSocket to change the return value of the PySide.QtNetwork.QAbstractSocket.localAddress() function after a connection has been established
		This feature is commonly used by proxy connections for virtual connection settings.
		Note that this function does not bind the local address of the socket prior to a connection (e.g., QUdpSocket.bind() ).
		"""
		res = super(QAbstractSocket,self).setLocalAddress(address)
		return res
	#----------------------------------------------------------------------
	def setLocalPort(self,port):
		"""
		setLocalPort(port)
			port=QtCore.quint16

		Sets the port on the local side of a connection to port .
		You can call this function in a subclass of PySide.QtNetwork.QAbstractSocket to change the return value of the PySide.QtNetwork.QAbstractSocket.localPort() function after a connection has been established
		This feature is commonly used by proxy connections for virtual connection settings.
		Note that this function does not bind the local port of the socket prior to a connection (e.g., QUdpSocket.bind() ).
		"""
		res = super(QAbstractSocket,self).setLocalPort(port)
		return res
	#----------------------------------------------------------------------
	def setPeerAddress(self,address):
		"""
		setPeerAddress(address)
			address=QtNetwork.QHostAddress

		Sets the address of the remote side of the connection to address .
		You can call this function in a subclass of PySide.QtNetwork.QAbstractSocket to change the return value of the PySide.QtNetwork.QAbstractSocket.peerAddress() function after a connection has been established
		This feature is commonly used by proxy connections for virtual connection settings.
		"""
		res = super(QAbstractSocket,self).setPeerAddress(address)
		return res
	#----------------------------------------------------------------------
	def setPeerName(self,name):
		"""
		setPeerName(name)
			name=unicode

		Sets the host name of the remote peer to name .
		You can call this function in a subclass of PySide.QtNetwork.QAbstractSocket to change the return value of the PySide.QtNetwork.QAbstractSocket.peerName() function after a connection has been established
		This feature is commonly used by proxy connections for virtual connection settings.
		"""
		res = super(QAbstractSocket,self).setPeerName(name)
		return res
	#----------------------------------------------------------------------
	def setPeerPort(self,port):
		"""
		setPeerPort(port)
			port=QtCore.quint16

		Sets the port of the remote side of the connection to port .
		You can call this function in a subclass of PySide.QtNetwork.QAbstractSocket to change the return value of the PySide.QtNetwork.QAbstractSocket.peerPort() function after a connection has been established
		This feature is commonly used by proxy connections for virtual connection settings.
		"""
		res = super(QAbstractSocket,self).setPeerPort(port)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,networkProxy):
		"""
		setProxy(networkProxy)
			networkProxy=QtNetwork.QNetworkProxy

		Sets the explicit network proxy for this socket to networkProxy .
		To disable the use of a proxy for this socket, use the QNetworkProxy.NoProxy proxy type:
		The default value for the proxy is QNetworkProxy.DefaultProxy , which means the socket will use the application settings: if a proxy is set with QNetworkProxy::setApplicationProxy, it will use that; otherwise, if a factory is set with QNetworkProxyFactory::setApplicationProxyFactory, it will query that factory with type QNetworkProxyQuery.TcpSocket .
		"""
		res = super(QAbstractSocket,self).setProxy(networkProxy)
		return res
	#----------------------------------------------------------------------
	def setReadBufferSize(self,size):
		"""
		setReadBufferSize(size)
			size=QtCore.qint64

		Sets the size of PySide.QtNetwork.QAbstractSocket s internal read buffer to be size bytes.
		If the buffer size is limited to a certain size, PySide.QtNetwork.QAbstractSocket wont buffer more than this size of data
		Exceptionally, a buffer size of 0 means that the read buffer is unlimited and all incoming data is buffered
		This is the default.
		This option is useful if you only read the data at certain points in time (e.g., in a real-time streaming application) or if you want to protect your socket against receiving too much data, which may eventually cause your application to run out of memory.
		Only PySide.QtNetwork.QTcpSocket uses PySide.QtNetwork.QAbstractSocket s internal buffer; PySide.QtNetwork.QUdpSocket does not use any buffering at all, but rather relies on the implicit buffering provided by the operating system
		Because of this, calling this function on PySide.QtNetwork.QUdpSocket has no effect.
		"""
		res = super(QAbstractSocket,self).setReadBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setSocketDescriptor(self,socketDescriptor,state=None,openMode=None):
		"""
		setSocketDescriptor(socketDescriptor,state=None,openMode=None)
			socketDescriptor=QtCore.int
			state=QtNetwork.QAbstractSocket.SocketState
			openMode=QtCore.QIODevice.OpenMode


		"""
		res = super(QAbstractSocket,self).setSocketDescriptor(socketDescriptor,state,openMode)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setSocketError(self,socketError):
		"""
		setSocketError(socketError)
			socketError=QtNetwork.QAbstractSocket.SocketError

		Sets the type of error that last occurred to socketError .
		"""
		res = super(QAbstractSocket,self).setSocketError(socketError)
		return res
	#----------------------------------------------------------------------
	def setSocketOption(self,option,value):
		"""
		setSocketOption(option,value)
			option=QtNetwork.QAbstractSocket.SocketOption
			value=object


		"""
		res = super(QAbstractSocket,self).setSocketOption(option,value)
		return res
	#----------------------------------------------------------------------
	def setSocketState(self,state):
		"""
		setSocketState(state)
			state=QtNetwork.QAbstractSocket.SocketState

		Sets the state of the socket to state .
		"""
		res = super(QAbstractSocket,self).setSocketState(state)
		return res
	#----------------------------------------------------------------------
	def socketOption(self,option):
		"""
		socketOption(option)
			option=QtNetwork.QAbstractSocket.SocketOption


		"""
		res = super(QAbstractSocket,self).socketOption(option)
		return res
	#----------------------------------------------------------------------
	def waitForConnected(self,msecs=None):
		"""
		waitForConnected(msecs=None)
			msecs=QtCore.int

		Waits until the socket is connected, up to msecs milliseconds
		If the connection has been established, this function returns true; otherwise it returns false
		In the case where it returns false, you can call PySide.QtNetwork.QAbstractSocket.error() to determine the cause of the error.
		The following example waits up to one second for a connection to be established:
		If msecs is -1, this function will not time out.
		"""
		res = super(QAbstractSocket,self).waitForConnected(msecs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def waitForDisconnected(self,msecs=None):
		"""
		waitForDisconnected(msecs=None)
			msecs=QtCore.int

		Waits until the socket has disconnected, up to msecs milliseconds
		If the connection has been disconnected, this function returns true; otherwise it returns false
		In the case where it returns false, you can call PySide.QtNetwork.QAbstractSocket.error() to determine the cause of the error.
		The following example waits up to one second for a connection to be closed:
		If msecs is -1, this function will not time out.
		"""
		res = super(QAbstractSocket,self).waitForDisconnected(msecs)
		isinstance(res,QtCore.bool)
		return res
