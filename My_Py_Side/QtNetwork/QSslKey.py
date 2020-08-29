from PySide import QtGui, QtCore

class QSslKey(QtNetwork.QSslKey):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslKey,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def algorithm(self):
		"""
		Returns the key algorithm.
		"""
		res = super(QSslKey,self).algorithm()
		isinstance(res,QtNetwork.QSsl.KeyAlgorithm)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the contents of this key, making it a null key.
		"""
		res = super(QSslKey,self).clear()
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns a pointer to the native key handle, if it is available; otherwise a null pointer is returned.
		You can use this handle together with the native API to access extended information about the key.
		"""
		res = super(QSslKey,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is a null key; otherwise false.
		"""
		res = super(QSslKey,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the key in bits, or -1 if the key is null.
		"""
		res = super(QSslKey,self).length()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of the key (i.e., PublicKey or PrivateKey).
		"""
		res = super(QSslKey,self).type()
		isinstance(res,QtNetwork.QSsl.KeyType)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,key):
		"""
		__ne__(key)
			key=QtNetwork.QSslKey

		Returns true if this key is not equal to key other ; otherwise returns false.
		"""
		res = super(QSslKey,self).__ne__(key)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,key):
		"""
		__eq__(key)
			key=QtNetwork.QSslKey

		Returns true if this key is equal to other ; otherwise returns false.
		"""
		res = super(QSslKey,self).__eq__(key)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toDer(self,passPhrase=None):
		"""
		toDer(passPhrase=None)
			passPhrase=QtCore.QByteArray

		Returns the key in DER encoding
		The result is encrypted with passPhrase if the key is a private key and passPhrase is non-empty.
		"""
		res = super(QSslKey,self).toDer(passPhrase)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toPem(self,passPhrase=None):
		"""
		toPem(passPhrase=None)
			passPhrase=QtCore.QByteArray

		Returns the key in PEM encoding
		The result is encrypted with passPhrase if the key is a private key and passPhrase is non-empty.
		"""
		res = super(QSslKey,self).toPem(passPhrase)
		isinstance(res,QtCore.QByteArray)
		return res
