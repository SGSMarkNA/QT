from PySide import QtGui, QtCore

class QSslConfiguration(QtNetwork.QSslConfiguration):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslConfiguration,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def caCertificates(self):
		"""
		Returns this connections CA certificate database
		The CA certificate database is used by the socket during the handshake phase to validate the peers certificate
		It can be modified prior to the handshake with PySide.QtNetwork.QSslConfiguration.setCaCertificates() , or with PySide.QtNetwork.QSslSocket s PySide.QtNetwork.QSslSocket.addCaCertificate() and PySide.QtNetwork.QSslSocket.addCaCertificates() .
		"""
		res = super(QSslConfiguration,self).caCertificates()
		return res
	#----------------------------------------------------------------------
	def ciphers(self):
		"""
		Returns this connections current cryptographic cipher suite
		This list is used during the handshake phase for choosing a session cipher
		The returned list of ciphers is ordered by descending preference
		(i.e., the first cipher in the list is the most preferred cipher)
		The session cipher will be the first one in the list that is also supported by the peer.
		By default, the handshake phase can choose any of the ciphers supported by this systems SSL libraries, which may vary from system to system
		The list of ciphers supported by this systems SSL libraries is returned by QSslSocket.supportedCiphers()
		You can restrict the list of ciphers used for choosing the session cipher for this socket by calling PySide.QtNetwork.QSslConfiguration.setCiphers() with a subset of the supported ciphers
		You can revert to using the entire set by calling PySide.QtNetwork.QSslConfiguration.setCiphers() with the list returned by QSslSocket.supportedCiphers() .
		"""
		res = super(QSslConfiguration,self).ciphers()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is a null PySide.QtNetwork.QSslConfiguration object.
		A PySide.QtNetwork.QSslConfiguration object is null if it has been default-constructed and no setter methods have been called.
		"""
		res = super(QSslConfiguration,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def localCertificate(self):
		"""
		Returns the certificate to be presented to the peer during the SSL handshake process.
		"""
		res = super(QSslConfiguration,self).localCertificate()
		isinstance(res,QtNetwork.QSslCertificate)
		return res
	#----------------------------------------------------------------------
	def peerCertificate(self):
		"""
		Returns the peers digital certificate (i.e., the immediate certificate of the host you are connected to), or a null certificate, if the peer has not assigned a certificate.
		The peer certificate is checked automatically during the handshake phase, so this function is normally used to fetch the certificate for display or for connection diagnostic purposes
		It contains information about the peer, including its host name, the certificate issuer, and the peers public key.
		Because the peer certificate is set during the handshake phase, it is safe to access the peer certificate from a slot connected to the QSslSocket.sslErrors() signal, QNetworkReply.sslErrors() signal, or the QSslSocket.encrypted() signal.
		If a null certificate is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesnt have a certificate, or it can mean there is no connection.
		If you want to check the peers complete chain of certificates, use PySide.QtNetwork.QSslConfiguration.peerCertificateChain() to get them all at once.
		"""
		res = super(QSslConfiguration,self).peerCertificate()
		isinstance(res,QtNetwork.QSslCertificate)
		return res
	#----------------------------------------------------------------------
	def peerCertificateChain(self):
		"""
		Returns the peers chain of digital certificates, starting with the peers immediate certificate and ending with the CAs certificate.
		Peer certificates are checked automatically during the handshake phase
		This function is normally used to fetch certificates for display, or for performing connection diagnostics
		Certificates contain information about the peer and the certificate issuers, including host name, issuer names, and issuer public keys.
		Because the peer certificate is set during the handshake phase, it is safe to access the peer certificate from a slot connected to the QSslSocket.sslErrors() signal, QNetworkReply.sslErrors() signal, or the QSslSocket.encrypted() signal.
		If an empty list is returned, it can mean the SSL handshake failed, or it can mean the host you are connected to doesnt have a certificate, or it can mean there is no connection.
		If you want to get only the peers immediate certificate, use PySide.QtNetwork.QSslConfiguration.peerCertificate() .
		"""
		res = super(QSslConfiguration,self).peerCertificateChain()
		return res
	#----------------------------------------------------------------------
	def peerVerifyDepth(self):
		"""
		Returns the maximum number of certificates in the peers certificate chain to be checked during the SSL handshake phase, or 0 (the default) if no maximum depth has been set, indicating that the whole certificate chain should be checked.
		The certificates are checked in issuing order, starting with the peers own certificate, then its issuers certificate, and so on.
		"""
		res = super(QSslConfiguration,self).peerVerifyDepth()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def peerVerifyMode(self):
		"""
		Returns the verify mode
		This mode decides whether PySide.QtNetwork.QSslSocket should request a certificate from the peer (i.e., the client requests a certificate from the server, or a server requesting a certificate from the client), and whether it should require that this certificate is valid.
		The default mode is AutoVerifyPeer, which tells PySide.QtNetwork.QSslSocket to use VerifyPeer for clients, QueryPeer for clients.
		"""
		res = super(QSslConfiguration,self).peerVerifyMode()
		isinstance(res,QtNetwork.QSslSocket.PeerVerifyMode)
		return res
	#----------------------------------------------------------------------
	def privateKey(self):
		"""
		Returns the SSL key assigned to this connection or a null key if none has been assigned yet.
		"""
		res = super(QSslConfiguration,self).privateKey()
		isinstance(res,QtNetwork.QSslKey)
		return res
	#----------------------------------------------------------------------
	def protocol(self):
		"""
		Returns the protocol setting for this SSL configuration.
		"""
		res = super(QSslConfiguration,self).protocol()
		isinstance(res,QtNetwork.QSsl.SslProtocol)
		return res
	#----------------------------------------------------------------------
	def sessionCipher(self):
		"""
		Returns the sockets cryptographic cipher , or a null cipher if the connection isnt encrypted
		The sockets cipher for the session is set during the handshake phase
		The cipher is used to encrypt and decrypt data transmitted through the socket.
		The SSL infrastructure also provides functions for setting the ordered list of ciphers from which the handshake phase will eventually select the session cipher
		This ordered list must be in place before the handshake phase begins.
		"""
		res = super(QSslConfiguration,self).sessionCipher()
		isinstance(res,QtNetwork.QSslCipher)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QSslConfiguration

		Returns true if this PySide.QtNetwork.QSslConfiguration differs from other
		Two PySide.QtNetwork.QSslConfiguration objects are considered different if any state or setting is different.
		"""
		res = super(QSslConfiguration,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QSslConfiguration

		Returns true if this PySide.QtNetwork.QSslConfiguration object is equal to other .
		Two PySide.QtNetwork.QSslConfiguration objects are considered equal if they have the exact same settings and state.
		"""
		res = super(QSslConfiguration,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setCaCertificates(self,certificates):
		"""
		setCaCertificates(certificates)
			certificates=unKnown


		"""
		res = super(QSslConfiguration,self).setCaCertificates(certificates)
		return res
	#----------------------------------------------------------------------
	def setCiphers(self,ciphers):
		"""
		setCiphers(ciphers)
			ciphers=unKnown


		"""
		res = super(QSslConfiguration,self).setCiphers(ciphers)
		return res
	#----------------------------------------------------------------------
	def setLocalCertificate(self,certificate):
		"""
		setLocalCertificate(certificate)
			certificate=QtNetwork.QSslCertificate

		Sets the certificate to be presented to the peer during SSL handshake to be certificate .
		Setting the certificate once the connection has been established has no effect.
		A certificate is the means of identification used in the SSL process
		The local certificate is used by the remote end to verify the local users identity against its list of Certification Authorities
		In most cases, such as in HTTP web browsing, only servers identify to the clients, so the client does not send a certificate.
		"""
		res = super(QSslConfiguration,self).setLocalCertificate(certificate)
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
		res = super(QSslConfiguration,self).setPeerVerifyDepth(depth)
		return res
	#----------------------------------------------------------------------
	def setPeerVerifyMode(self,mode):
		"""
		setPeerVerifyMode(mode)
			mode=QtNetwork.QSslSocket.PeerVerifyMode


		"""
		res = super(QSslConfiguration,self).setPeerVerifyMode(mode)
		return res
	#----------------------------------------------------------------------
	def setPrivateKey(self,key):
		"""
		setPrivateKey(key)
			key=QtNetwork.QSslKey

		Sets the connections private key to key
		The private key and the local certificate are used by clients and servers that must prove their identity to SSL peers.
		Both the key and the local certificate are required if you are creating an SSL server socket
		If you are creating an SSL client socket, the key and local certificate are required if your client must identify itself to an SSL server.
		"""
		res = super(QSslConfiguration,self).setPrivateKey(key)
		return res
	#----------------------------------------------------------------------
	def setProtocol(self,protocol):
		"""
		setProtocol(protocol)
			protocol=QtNetwork.QSsl.SslProtocol


		"""
		res = super(QSslConfiguration,self).setProtocol(protocol)
		return res
