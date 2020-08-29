from PySide import QtGui, QtCore

class QSslSocket(QtNetwork.QSslSocket):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslSocket,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def caCertificates(self):
		"""
		Returns this sockets CA certificate database
		The CA certificate database is used by the socket during the handshake phase to validate the peers certificate
		It can be moodified prior to the handshake with PySide.QtNetwork.QSslSocket.addCaCertificate() , PySide.QtNetwork.QSslSocket.addCaCertificates() , and PySide.QtNetwork.QSslSocket.setCaCertificates() .
		"""
		res = super(QSslSocket,self).caCertificates()
		return res
	#----------------------------------------------------------------------
	def ciphers(self):
		"""
		Returns this sockets current cryptographic cipher suite
		This list is used during the sockets handshake phase for choosing a session cipher
		The returned list of ciphers is ordered by descending preference
		(i.e., the first cipher in the list is the most preferred cipher)
		The session cipher will be the first one in the list that is also supported by the peer.
		By default, the handshake phase can choose any of the ciphers supported by this systems SSL libraries, which may vary from system to system
		The list of ciphers supported by this systems SSL libraries is returned by PySide.QtNetwork.QSslSocket.supportedCiphers()
		You can restrict the list of ciphers used for choosing the session cipher for this socket by calling PySide.QtNetwork.QSslSocket.setCiphers() with a subset of the supported ciphers
		You can revert to using the entire set by calling PySide.QtNetwork.QSslSocket.setCiphers() with the list returned by PySide.QtNetwork.QSslSocket.supportedCiphers() .
		You can restrict the list of ciphers used for choosing the session cipher for all sockets by calling PySide.QtNetwork.QSslSocket.setDefaultCiphers() with a subset of the supported ciphers
		You can revert to using the entire set by calling PySide.QtNetwork.QSslSocket.setCiphers() with the list returned by PySide.QtNetwork.QSslSocket.supportedCiphers() .
		"""
		res = super(QSslSocket,self).ciphers()
		return res
	#----------------------------------------------------------------------
	def encrypted(self):
		"""

		"""
		res = super(QSslSocket,self).encrypted()
		return res
	#----------------------------------------------------------------------
	def encryptedBytesAvailable(self):
		"""
		Returns the number of encrypted bytes that are awaiting decryption
		Normally, this function will return 0 because PySide.QtNetwork.QSslSocket decrypts its incoming data as soon as it can.
		"""
		res = super(QSslSocket,self).encryptedBytesAvailable()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def encryptedBytesToWrite(self):
		"""
		Returns the number of encrypted bytes that are waiting to be written to the network.
		"""
		res = super(QSslSocket,self).encryptedBytesToWrite()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def isEncrypted(self):
		"""
		Returns true if the socket is encrypted; otherwise, false is returned.
		An encrypted socket encrypts all data that is written by calling PySide.QtCore.QIODevice.write() or PySide.QtCore.QIODevice.putChar() before the data is written to the network, and decrypts all incoming data as the data is received from the network, before you call PySide.QtCore.QIODevice.read() , PySide.QtCore.QIODevice.readLine() or PySide.QtCore.QIODevice.getChar() .
		PySide.QtNetwork.QSslSocket emits PySide.QtNetwork.QSslSocket.encrypted() when it enters encrypted mode.
		You can call PySide.QtNetwork.QSslSocket.sessionCipher() to find which cryptographic cipher is used to encrypt and decrypt your data.
		"""
		res = super(QSslSocket,self).isEncrypted()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def localCertificate(self):
		"""
		Returns the sockets local certificate , or an empty certificate if no local certificate has been assigned.
		"""
		res = super(QSslSocket,self).localCertificate()
		isinstance(res,QtNetwork.QSslCertificate)
		return res
	#----------------------------------------------------------------------
	def mode(self):
		"""
		Returns the current mode for the socket; either UnencryptedMode , where PySide.QtNetwork.QSslSocket behaves identially to PySide.QtNetwork.QTcpSocket , or one of SslClientMode or SslServerMode , where the client is either negotiating or in encrypted mode.
		When the mode changes, PySide.QtNetwork.QSslSocket emits PySide.QtNetwork.QSslSocket.modeChanged()
		"""
		res = super(QSslSocket,self).mode()
		isinstance(res,QtNetwork.QSslSocket.SslMode)
		return res
	#----------------------------------------------------------------------
	def peerCertificate(self):
		"""
		Returns the peers digital certificate (i.e., the immediate certificate of the host you are connected to), or a null certificate, if the peer has not assigned a certificate.
		The peer certificate is checked automatically during the handshake phase, so this function is normally used to fetch the certificate for display or for connection diagnostic purposes
		It contains information about the peer, including its host name, the certificate issuer, and the peers public key.
		Because the peer certificate is set during the handshake phase, it is safe to access the peer certificate from a slot connected to the PySide.QtNetwork.QSslSocket.sslErrors() signal or the PySide.QtNetwork.QSslSocket.encrypted() signal.
		If a null certificate is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesnt have a certificate, or it can mean there is no connection.
		If you want to check the peers complete chain of certificates, use PySide.QtNetwork.QSslSocket.peerCertificateChain() to get them all at once.
		"""
		res = super(QSslSocket,self).peerCertificate()
		isinstance(res,QtNetwork.QSslCertificate)
		return res
	#----------------------------------------------------------------------
	def peerCertificateChain(self):
		"""
		Returns the peers chain of digital certificates, or an empty list of certificates.
		Peer certificates are checked automatically during the handshake phase
		This function is normally used to fetch certificates for display, or for performing connection diagnostics
		Certificates contain information about the peer and the certificate issuers, including host name, issuer names, and issuer public keys.
		The peer certificates are set in PySide.QtNetwork.QSslSocket during the handshake phase, so it is safe to call this function from a slot connected to the PySide.QtNetwork.QSslSocket.sslErrors() signal or the PySide.QtNetwork.QSslSocket.encrypted() signal.
		If an empty list is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesnt have a certificate, or it can mean there is no connection.
		If you want to get only the peers immediate certificate, use PySide.QtNetwork.QSslSocket.peerCertificate() .
		"""
		res = super(QSslSocket,self).peerCertificateChain()
		return res
	#----------------------------------------------------------------------
	def peerVerifyDepth(self):
		"""
		Returns the maximum number of certificates in the peers certificate chain to be checked during the SSL handshake phase, or 0 (the default) if no maximum depth has been set, indicating that the whole certificate chain should be checked.
		The certificates are checked in issuing order, starting with the peers own certificate, then its issuers certificate, and so on.
		"""
		res = super(QSslSocket,self).peerVerifyDepth()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def peerVerifyMode(self):
		"""
		Returns the sockets verify mode
		This mode mode decides whether PySide.QtNetwork.QSslSocket should request a certificate from the peer (i.e., the client requests a certificate from the server, or a server requesting a certificate from the client), and whether it should require that this certificate is valid.
		The default mode is AutoVerifyPeer , which tells PySide.QtNetwork.QSslSocket to use VerifyPeer for clients and QueryPeer for servers.
		"""
		res = super(QSslSocket,self).peerVerifyMode()
		isinstance(res,QtNetwork.QSslSocket.PeerVerifyMode)
		return res
	#----------------------------------------------------------------------
	def privateKey(self):
		"""
		Returns this sockets private key.
		"""
		res = super(QSslSocket,self).privateKey()
		isinstance(res,QtNetwork.QSslKey)
		return res
	#----------------------------------------------------------------------
	def protocol(self):
		"""
		Returns the sockets SSL protocol
		By default, QSsl.SslV3 is used.
		"""
		res = super(QSslSocket,self).protocol()
		isinstance(res,QtNetwork.QSsl.SslProtocol)
		return res
	#----------------------------------------------------------------------
	def sessionCipher(self):
		"""
		Returns the sockets cryptographic cipher , or a null cipher if the connection isnt encrypted
		The sockets cipher for the session is set during the handshake phase
		The cipher is used to encrypt and decrypt data transmitted through the socket.
		PySide.QtNetwork.QSslSocket also provides functions for setting the ordered list of ciphers from which the handshake phase will eventually select the session cipher
		This ordered list must be in place before the handshake phase begins.
		"""
		res = super(QSslSocket,self).sessionCipher()
		isinstance(res,QtNetwork.QSslCipher)
		return res
	#----------------------------------------------------------------------
	def sslConfiguration(self):
		"""
		Returns the sockets SSL configuration state
		The default SSL configuration of a socket is to use the default ciphers, default CA certificates, no local private key or certificate.
		The SSL configuration also contains fields that can change with time without notice.
		"""
		res = super(QSslSocket,self).sslConfiguration()
		isinstance(res,QtNetwork.QSslConfiguration)
		return res
	#----------------------------------------------------------------------
	def sslErrors(self):
		"""
		Returns a list of the last SSL errors that occurred
		This is the same list as PySide.QtNetwork.QSslSocket passes via the PySide.QtNetwork.QSslSocket.sslErrors() signal
		If the connection has been encrypted with no errors, this function will return an empty list.
		"""
		res = super(QSslSocket,self).sslErrors()
		return res
	#----------------------------------------------------------------------
	def addCaCertificate(self,certificate):
		"""
		addCaCertificate(certificate)
			certificate=QtNetwork.QSslCertificate

		Adds the certificate to this sockets CA certificate database
		The CA certificate database is used by the socket during the handshake phase to validate the peers certificate.
		To add multiple certificates, use PySide.QtNetwork.QSslSocket.addCaCertificates() .
		"""
		res = super(QSslSocket,self).addCaCertificate(certificate)
		return res
	#----------------------------------------------------------------------
	def addCaCertificates(self,*args,**kwargs):
		"""
		addCaCertificates(path,format=None,syntax=None)
			path=unicode
			format=QtNetwork.QSsl.EncodingFormat
			syntax=QtCore.QRegExp.PatternSyntax

		addCaCertificates(certificates)
			certificates=unKnown


		"""
		res = super(QSslSocket,self).addCaCertificates(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def connectToHostEncrypted(self,*args,**kwargs):
		"""
		connectToHostEncrypted(hostName,port,sslPeerName,mode=None)
			hostName=unicode
			port=QtCore.quint16
			sslPeerName=unicode
			mode=QtCore.QIODevice.OpenMode

		connectToHostEncrypted(hostName,port,mode=None)
			hostName=unicode
			port=QtCore.quint16
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QSslSocket,self).connectToHostEncrypted(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def ignoreSslErrors(self,errors):
		"""
		ignoreSslErrors(errors)
			errors=unKnown


		"""
		res = super(QSslSocket,self).ignoreSslErrors(errors)
		return res
	#----------------------------------------------------------------------
	def setCaCertificates(self,certificates):
		"""
		setCaCertificates(certificates)
			certificates=unKnown


		"""
		res = super(QSslSocket,self).setCaCertificates(certificates)
		return res
	#----------------------------------------------------------------------
	def setCiphers(self,*args,**kwargs):
		"""
		setCiphers(ciphers)
			ciphers=unKnown

		setCiphers(ciphers)
			ciphers=unicode


		"""
		res = super(QSslSocket,self).setCiphers(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setLocalCertificate(self,*args,**kwargs):
		"""
		setLocalCertificate(fileName,format=None)
			fileName=unicode
			format=QtNetwork.QSsl.EncodingFormat

		setLocalCertificate(certificate)
			certificate=QtNetwork.QSslCertificate


		"""
		res = super(QSslSocket,self).setLocalCertificate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPeerVerifyDepth(self,depth):
		"""
		setPeerVerifyDepth(depth)
			depth=QtCore.int

		Sets the maximum number of certificates in the peers certificate chain to be checked during the SSL handshake phase, to depth
		Setting a depth of 0 means that no maximum depth is set, indicating that the whole certificate chain should be checked.
		The certificates are checked in issuing order, starting with the peers own certificate, then its issuers certificate, and so on.
		"""
		res = super(QSslSocket,self).setPeerVerifyDepth(depth)
		return res
	#----------------------------------------------------------------------
	def setPeerVerifyMode(self,mode):
		"""
		setPeerVerifyMode(mode)
			mode=QtNetwork.QSslSocket.PeerVerifyMode


		"""
		res = super(QSslSocket,self).setPeerVerifyMode(mode)
		return res
	#----------------------------------------------------------------------
	def setPrivateKey(self,*args,**kwargs):
		"""
		setPrivateKey(fileName,algorithm=None,format=None,passPhrase=None)
			fileName=unicode
			algorithm=QtNetwork.QSsl.KeyAlgorithm
			format=QtNetwork.QSsl.EncodingFormat
			passPhrase=QtCore.QByteArray

		setPrivateKey(key)
			key=QtNetwork.QSslKey


		"""
		res = super(QSslSocket,self).setPrivateKey(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setProtocol(self,protocol):
		"""
		setProtocol(protocol)
			protocol=QtNetwork.QSsl.SslProtocol


		"""
		res = super(QSslSocket,self).setProtocol(protocol)
		return res
	#----------------------------------------------------------------------
	def setSslConfiguration(self,config):
		"""
		setSslConfiguration(config)
			config=QtNetwork.QSslConfiguration

		Sets the sockets SSL configuration to be the contents of configuration
		This function sets the local certificate, the ciphers, the private key and the CA certificates to those stored in configuration .
		It is not possible to set the SSL-state related fields.
		"""
		res = super(QSslSocket,self).setSslConfiguration(config)
		return res
	#----------------------------------------------------------------------
	def sslErrors(self,errors):
		"""
		sslErrors(errors)
			errors=unKnown


		"""
		res = super(QSslSocket,self).sslErrors(errors)
		return res
	#----------------------------------------------------------------------
	def waitForEncrypted(self,msecs=None):
		"""
		waitForEncrypted(msecs=None)
			msecs=QtCore.int

		Waits until the socket has completed the SSL handshake and has emitted PySide.QtNetwork.QSslSocket.encrypted() , or msecs milliseconds, whichever comes first
		If PySide.QtNetwork.QSslSocket.encrypted() has been emitted, this function returns true; otherwise (e.g., the socket is disconnected, or the SSL handshake fails), false is returned.
		The following example waits up to one second for the socket to be encrypted:
		If msecs is -1, this function will not time out.
		"""
		res = super(QSslSocket,self).waitForEncrypted(msecs)
		isinstance(res,bool)
		return res
