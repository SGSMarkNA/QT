from PySide import QtGui, QtCore

class QSslError(QtNetwork.QSslError):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslError,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def certificate(self):
		"""
		Returns the certificate associated with this error, or a null certificate if the error does not relate to any certificate.
		"""
		res = super(QSslError,self).certificate()
		isinstance(res,QtNetwork.QSslCertificate)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of the error.
		"""
		res = super(QSslError,self).error()
		isinstance(res,QtNetwork.QSslError.SslError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a short localized human-readable description of the error.
		"""
		res = super(QSslError,self).errorString()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QSslError

		Returns true if this error is not equal to other ; otherwise returns false.
		"""
		res = super(QSslError,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QSslError

		Returns true if this error is equal to other ; otherwise returns false.
		"""
		res = super(QSslError,self).__eq__(other)
		isinstance(res,bool)
		return res
