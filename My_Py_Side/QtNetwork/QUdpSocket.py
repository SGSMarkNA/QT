from PySide import QtGui, QtCore

class QUdpSocket(QtNetwork.QUdpSocket):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUdpSocket,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasPendingDatagrams(self):
		"""
		Returns true if at least one datagram is waiting to be read; otherwise returns false.
		"""
		res = super(QUdpSocket,self).hasPendingDatagrams()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pendingDatagramSize(self):
		"""
		Returns the size of the first pending UDP datagram
		If there is no datagram available, this function returns -1.
		"""
		res = super(QUdpSocket,self).pendingDatagramSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def bind(self,*args,**kwargs):
		"""
		bind(port,mode)
			port=QtCore.quint16
			mode=QtNetwork.QUdpSocket.BindMode

		bind(port=None)
			port=QtCore.quint16

		bind(address,port,mode)
			address=QtNetwork.QHostAddress
			port=QtCore.quint16
			mode=QtNetwork.QUdpSocket.BindMode

		bind(address,port)
			address=QtNetwork.QHostAddress
			port=QtCore.quint16


		"""
		res = super(QUdpSocket,self).bind(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def readDatagram(self,maxlen):
		"""
		readDatagram(maxlen)
			maxlen=QtCore.qint64

		Receives a datagram no larger than maxSize bytes and stores it in data
		The senders host address and port is stored in *``address`` and *``port`` (unless the pointers are 0).
		Returns the size of the datagram on success; otherwise returns -1.
		If maxSize is too small, the rest of the datagram will be lost
		To avoid loss of data, call PySide.QtNetwork.QUdpSocket.pendingDatagramSize() to determine the size of the pending datagram before attempting to read it
		If maxSize is 0, the datagram will be discarded.
		"""
		res = super(QUdpSocket,self).readDatagram(maxlen)
		return res
	#----------------------------------------------------------------------
	def writeDatagram(self,datagram,host,port):
		"""
		writeDatagram(datagram,host,port)
			datagram=QtCore.QByteArray
			host=QtNetwork.QHostAddress
			port=QtCore.quint16

		This is an overloaded function.
		Sends the datagram datagram to the host address host and at port port .
		"""
		res = super(QUdpSocket,self).writeDatagram(datagram,host,port)
		isinstance(res,QtCore.qint64)
		return res
