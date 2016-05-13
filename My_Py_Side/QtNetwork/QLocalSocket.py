from PySide import QtGui, QtCore

class QLocalSocket(QtNetwork.QLocalSocket):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLocalSocket,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def abort(self):
		"""
		Aborts the current connection and resets the socket
		Unlike PySide.QtNetwork.QLocalSocket.disconnectFromServer() , this function immediately closes the socket, clearing any pending data in the write buffer.
		"""
		res = super(QLocalSocket,self).abort()
		return res
	#----------------------------------------------------------------------
	def connected(self):
		"""

		"""
		res = super(QLocalSocket,self).connected()
		return res
	#----------------------------------------------------------------------
	def disconnectFromServer(self):
		"""
		Attempts to close the socket
		If there is pending data waiting to be written, PySide.QtNetwork.QLocalSocket will enter ClosingState and wait until all data has been written
		Eventually, it will enter UnconnectedState and emit the disconnectedFromServer() signal.
		"""
		res = super(QLocalSocket,self).disconnectFromServer()
		return res
	#----------------------------------------------------------------------
	def disconnected(self):
		"""

		"""
		res = super(QLocalSocket,self).disconnected()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that last occurred.
		"""
		res = super(QLocalSocket,self).error()
		isinstance(res,QtNetwork.QLocalSocket.LocalSocketError)
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		This function writes as much as possible from the internal write buffer to the socket, without blocking
		If any data was written, this function returns true; otherwise false is returned.
		Call this function if you need PySide.QtNetwork.QLocalSocket to start sending buffered data immediately
		The number of bytes successfully written depends on the operating system
		In most cases, you do not need to call this function, because PySide.QtNetwork.QLocalSocket will start sending data automatically once control goes back to the event loop
		In the absence of an event loop, call PySide.QtNetwork.QLocalSocket.waitForBytesWritten() instead.
		"""
		res = super(QLocalSocket,self).flush()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fullServerName(self):
		"""
		Returns the server path that the socket is connected to.
		"""
		res = super(QLocalSocket,self).fullServerName()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the socket is valid and ready for use; otherwise returns false.
		"""
		res = super(QLocalSocket,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def readBufferSize(self):
		"""
		Returns the size of the internal read buffer
		This limits the amount of data that the client can receive before you call PySide.QtCore.QIODevice.read() or PySide.QtCore.QIODevice.readAll()
		A read buffer size of 0 (the default) means that the buffer has no size limit, ensuring that no data is lost.
		"""
		res = super(QLocalSocket,self).readBufferSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def serverName(self):
		"""
		Returns the name of the peer as specified by PySide.QtNetwork.QLocalSocket.connectToServer() , or an empty PySide.QtCore.QString if PySide.QtNetwork.QLocalSocket.connectToServer() has not been called or it failed.
		"""
		res = super(QLocalSocket,self).serverName()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the state of the socket.
		"""
		res = super(QLocalSocket,self).state()
		isinstance(res,QtNetwork.QLocalSocket.LocalSocketState)
		return res
	#----------------------------------------------------------------------
	def connectToServer(self,name,openMode=None):
		"""
		connectToServer(name,openMode=None)
			name=unicode
			openMode=QtCore.QIODevice.OpenMode


		"""
		res = super(QLocalSocket,self).connectToServer(name,openMode)
		return res
	#----------------------------------------------------------------------
	def error(self,socketError):
		"""
		error(socketError)
			socketError=QtNetwork.QLocalSocket.LocalSocketError


		"""
		res = super(QLocalSocket,self).error(socketError)
		return res
	#----------------------------------------------------------------------
	def setReadBufferSize(self,size):
		"""
		setReadBufferSize(size)
			size=QtCore.qint64

		Sets the size of PySide.QtNetwork.QLocalSocket s internal read buffer to be size bytes.
		If the buffer size is limited to a certain size, PySide.QtNetwork.QLocalSocket wont buffer more than this size of data
		Exceptionally, a buffer size of 0 means that the read buffer is unlimited and all incoming data is buffered
		This is the default.
		This option is useful if you only read the data at certain points in time (e.g., in a real-time streaming application) or if you want to protect your socket against receiving too much data, which may eventually cause your application to run out of memory.
		"""
		res = super(QLocalSocket,self).setReadBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def waitForConnected(self,msecs=None):
		"""
		waitForConnected(msecs=None)
			msecs=QtCore.int

		Waits until the socket is connected, up to msecs milliseconds
		If the connection has been established, this function returns true; otherwise it returns false
		In the case where it returns false, you can call PySide.QtNetwork.QLocalSocket.error() to determine the cause of the error.
		The following example waits up to one second for a connection to be established:
		If msecs is -1, this function will not time out.
		"""
		res = super(QLocalSocket,self).waitForConnected(msecs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def waitForDisconnected(self,msecs=None):
		"""
		waitForDisconnected(msecs=None)
			msecs=QtCore.int

		Waits until the socket has disconnected, up to msecs milliseconds
		If the connection has been disconnected, this function returns true; otherwise it returns false
		In the case where it returns false, you can call PySide.QtNetwork.QLocalSocket.error() to determine the cause of the error.
		The following example waits up to one second for a connection to be closed:
		If msecs is -1, this function will not time out.
		"""
		res = super(QLocalSocket,self).waitForDisconnected(msecs)
		isinstance(res,QtCore.bool)
		return res
