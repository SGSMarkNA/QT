from PySide import QtGui, QtCore

class QSslCertificate(QtNetwork.QSslCertificate):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSslCertificate,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alternateSubjectNames(self):
		"""
		Returns the list of alternative subject names for this certificate
		The alternate subject names typically contain host names, optionally with wildcards, that are valid for this certificate.
		These names are tested against the connected peers host name, if either the subject information for CommonName doesnt define a valid host name, or the subject info name doesnt match the peers host name.
		"""
		res = super(QSslCertificate,self).alternateSubjectNames()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the contents of this certificate, making it a null certificate.
		"""
		res = super(QSslCertificate,self).clear()
		return res
	#----------------------------------------------------------------------
	def effectiveDate(self):
		"""
		Returns the date-time that the certificate becomes valid, or an empty PySide.QtCore.QDateTime if this is a null certificate.
		"""
		res = super(QSslCertificate,self).effectiveDate()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def expiryDate(self):
		"""
		Returns the date-time that the certificate expires, or an empty PySide.QtCore.QDateTime if this is a null certificate.
		"""
		res = super(QSslCertificate,self).expiryDate()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns a pointer to the native certificate handle, if there is one, or a null pointer otherwise.
		You can use this handle, together with the native API, to access extended information about the certificate.
		"""
		res = super(QSslCertificate,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is a null certificate (i.e., a certificate with no contents); otherwise returns false.
		By default, PySide.QtNetwork.QSslCertificate constructs a null certificate.
		"""
		res = super(QSslCertificate,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this certificate is valid; otherwise returns false.
		Note: Currently, this function checks that the current data-time is within the date-time range during which the certificate is considered valid, and checks that the certificate is not in a blacklist of fraudulent certificates.
		"""
		res = super(QSslCertificate,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def publicKey(self):
		"""
		Returns the certificate subjects public key.
		"""
		res = super(QSslCertificate,self).publicKey()
		isinstance(res,QtNetwork.QSslKey)
		return res
	#----------------------------------------------------------------------
	def serialNumber(self):
		"""
		Returns the certificates serial number string in decimal format
		In case the serial number cannot be converted to decimal format (i.e
		if it is bigger than 4294967295, which means it does not fit into 4 bytes), its hexadecimal version is returned.
		"""
		res = super(QSslCertificate,self).serialNumber()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toDer(self):
		"""
		Returns this certificate converted to a DER (binary) encoded representation.
		"""
		res = super(QSslCertificate,self).toDer()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toPem(self):
		"""
		Returns this certificate converted to a PEM (Base64) encoded representation.
		"""
		res = super(QSslCertificate,self).toPem()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def version(self):
		"""
		Returns the certificates version string.
		"""
		res = super(QSslCertificate,self).version()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def digest(self,algorithm=None):
		"""
		digest(algorithm=None)
			algorithm=QtCore.QCryptographicHash.Algorithm


		"""
		res = super(QSslCertificate,self).digest(algorithm)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def issuerInfo(self,*args,**kwargs):
		"""
		issuerInfo(info)
			info=QtNetwork.QSslCertificate.SubjectInfo

		issuerInfo(tag)
			tag=QtCore.QByteArray

		Returns the issuer information for the subject from the certificate, or an empty string if there is no information for subject in the certificate.
		"""
		res = super(QSslCertificate,self).issuerInfo(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QSslCertificate

		Returns true if this certificate is not the same as other ; otherwise returns false.
		"""
		res = super(QSslCertificate,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QSslCertificate

		Returns true if this certificate is the same as other ; otherwise returns false.
		"""
		res = super(QSslCertificate,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def subjectInfo(self,*args,**kwargs):
		"""
		subjectInfo(info)
			info=QtNetwork.QSslCertificate.SubjectInfo

		subjectInfo(tag)
			tag=QtCore.QByteArray

		Returns the information for the subject , or an empty string if there is no information for subject in the certificate.
		"""
		res = super(QSslCertificate,self).subjectInfo(*args,**kwargs)
		return res
