from PySide import QtGui, QtCore

class QSslCipher(QtNetwork.QSslCipher):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslCipher,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def authenticationMethod(self):
		"""
		Returns the ciphers authentication method as a PySide.QtCore.QString .
		"""
		res = super(QSslCipher,self).authenticationMethod()
		return res
	#----------------------------------------------------------------------
	def encryptionMethod(self):
		"""
		Returns the ciphers encryption method as a PySide.QtCore.QString .
		"""
		res = super(QSslCipher,self).encryptionMethod()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is a null cipher; otherwise returns false.
		"""
		res = super(QSslCipher,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def keyExchangeMethod(self):
		"""
		Returns the ciphers key exchange method as a PySide.QtCore.QString .
		"""
		res = super(QSslCipher,self).keyExchangeMethod()
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the cipher, or an empty PySide.QtCore.QString if this is a null cipher.
		"""
		res = super(QSslCipher,self).name()
		return res
	#----------------------------------------------------------------------
	def protocol(self):
		"""
		Returns the ciphers protocol type, or QSsl.UnknownProtocol if PySide.QtNetwork.QSslCipher is unable to determine the protocol ( PySide.QtNetwork.QSslCipher.protocolString() may contain more information).
		"""
		res = super(QSslCipher,self).protocol()
		isinstance(res,QtNetwork.QSsl.SslProtocol)
		return res
	#----------------------------------------------------------------------
	def protocolString(self):
		"""
		Returns the ciphers protocol as a PySide.QtCore.QString .
		"""
		res = super(QSslCipher,self).protocolString()
		return res
	#----------------------------------------------------------------------
	def supportedBits(self):
		"""
		Returns the number of bits supported by the cipher.
		"""
		res = super(QSslCipher,self).supportedBits()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def usedBits(self):
		"""
		Returns the number of bits used by the cipher.
		"""
		res = super(QSslCipher,self).usedBits()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QSslCipher

		Returns true if this cipher is not the same as other ; otherwise, false is returned.
		"""
		res = super(QSslCipher,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QSslCipher

		Returns true if this cipher is the same as other ; otherwise, false is returned.
		"""
		res = super(QSslCipher,self).__eq__(other)
		isinstance(res,bool)
		return res
