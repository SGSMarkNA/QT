from PySide import QtGui, QtCore

class QLocalServer(QtNetwork.QLocalServer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLocalServer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def close(self):
		"""
		Stop listening for incoming connections
		Existing connections are not effected, but any new connections will be refused.
		"""
		res = super(QLocalServer,self).close()
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns the human-readable message appropriate to the current error reported by PySide.QtNetwork.QLocalServer.serverError()
		If no suitable string is available, an empty string is returned.
		"""
		res = super(QLocalServer,self).errorString()
		return res
	#----------------------------------------------------------------------
	def fullServerName(self):
		"""
		Returns the full path that the server is listening on.
		Note: This is platform specific
		"""
		res = super(QLocalServer,self).fullServerName()
		return res
	#----------------------------------------------------------------------
	def hasPendingConnections(self):
		"""
		Returns true if the server has a pending connection; otherwise returns false.
		"""
		res = super(QLocalServer,self).hasPendingConnections()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isListening(self):
		"""
		Returns true if the server is listening for incoming connections otherwise false.
		"""
		res = super(QLocalServer,self).isListening()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def maxPendingConnections(self):
		"""
		Returns the maximum number of pending accepted connections
		The default is 30.
		"""
		res = super(QLocalServer,self).maxPendingConnections()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def newConnection(self):
		"""

		"""
		res = super(QLocalServer,self).newConnection()
		return res
	#----------------------------------------------------------------------
	def nextPendingConnection(self):
		"""
		Returns the next pending connection as a connected PySide.QtNetwork.QLocalSocket object.
		The socket is created as a child of the server, which means that it is automatically deleted when the PySide.QtNetwork.QLocalServer object is destroyed
		It is still a good idea to delete the object explicitly when you are done with it, to avoid wasting memory.
		0 is returned if this function is called when there are no pending connections.
		"""
		res = super(QLocalServer,self).nextPendingConnection()
		isinstance(res,QtNetwork.QLocalSocket)
		return res
	#----------------------------------------------------------------------
	def serverError(self):
		"""
		Returns the type of error that occurred last or NoError.
		"""
		res = super(QLocalServer,self).serverError()
		isinstance(res,QtNetwork.QAbstractSocket.SocketError)
		return res
	#----------------------------------------------------------------------
	def serverName(self):
		"""
		Returns the server name if the server is listening for connections; otherwise returns QString()
		"""
		res = super(QLocalServer,self).serverName()
		return res
	#----------------------------------------------------------------------
	def listen(self,name):
		"""
		listen(name)
			name=unicode

		Tells the server to listen for incoming connections on name
		If the server is currently listening then it will return false
		Return true on success otherwise false.
		name can be a single name and PySide.QtNetwork.QLocalServer will determine the correct platform specific path
		PySide.QtNetwork.QLocalServer.serverName() will return the name that is passed into listen.
		Usually you would just pass in a name like foo, but on Unix this could also be a path such as /tmp/foo and on Windows this could be a pipe path such as \.pipefoo
		Note: On Unix if the server crashes without closing listen will fail with AddressInUseError
		To create a new server the file should be removed
		On Windows two local servers can listen to the same pipe at the same time, but any connections will go to one of the server.
		"""
		res = super(QLocalServer,self).listen(name)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setMaxPendingConnections(self,numConnections):
		"""
		setMaxPendingConnections(numConnections)
			numConnections=QtCore.int

		Sets the maximum number of pending accepted connections to numConnections
		PySide.QtNetwork.QLocalServer will accept no more than numConnections incoming connections before PySide.QtNetwork.QLocalServer.nextPendingConnection() is called.
		Note: Even though PySide.QtNetwork.QLocalServer will stop accepting new connections after it has reached its maximum number of pending connections, the operating system may still keep them in queue which will result in clients signaling that it is connected.
		"""
		res = super(QLocalServer,self).setMaxPendingConnections(numConnections)
		return res
	#----------------------------------------------------------------------
	def waitForNewConnection(self,msec):
		"""
		waitForNewConnection(msec)
			msec=QtCore.int

		Waits for at most msec milliseconds or until an incoming connection is available
		Returns true if a connection is available; otherwise returns false
		If the operation timed out and timedOut is not 0, *timedOut will be set to true.
		This is a blocking function call
		Its use is ill-advised in a single-threaded GUI application, since the whole application will stop responding until the function returns
		PySide.QtNetwork.QLocalServer.waitForNewConnection() is mostly useful when there is no event loop available.
		The non-blocking alternative is to connect to the PySide.QtNetwork.QLocalServer.newConnection() signal.
		If msec is -1, this function will not time out.
		"""
		res = super(QLocalServer,self).waitForNewConnection(msec)
		return res
