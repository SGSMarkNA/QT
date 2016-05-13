from PySide import QtGui, QtCore

class QNetworkReply(QtNetwork.QNetworkReply):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkReply,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def abort(self):
		"""
		Aborts the operation immediately and close down any network connections still open
		Uploads still in progress are also aborted.
		"""
		res = super(QNetworkReply,self).abort()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the error that was found during the processing of this request
		If no error was found, returns NoError .
		"""
		res = super(QNetworkReply,self).error()
		isinstance(res,QtNetwork.QNetworkReply.NetworkError)
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QNetworkReply,self).finished()
		return res
	#----------------------------------------------------------------------
	def ignoreSslErrors(self):
		"""
		If this function is called, SSL errors related to network connection will be ignored, including certificate validation errors.
		Note that calling this function without restraint may pose a security risk for your application
		Use it with care.
		This function can be called from the slot connected to the PySide.QtNetwork.QNetworkReply.sslErrors() signal, which indicates which errors were found.
		"""
		res = super(QNetworkReply,self).ignoreSslErrors()
		return res
	#----------------------------------------------------------------------
	def isFinished(self):
		"""
		Returns true when the reply has finished or was aborted.
		"""
		res = super(QNetworkReply,self).isFinished()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRunning(self):
		"""
		Returns true when the request is still processing and the reply has not finished or was aborted yet.
		"""
		res = super(QNetworkReply,self).isRunning()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def manager(self):
		"""
		Returns the PySide.QtNetwork.QNetworkAccessManager that was used to create this PySide.QtNetwork.QNetworkReply object
		Initially, it is also the parent object.
		"""
		res = super(QNetworkReply,self).manager()
		isinstance(res,QtNetwork.QNetworkAccessManager)
		return res
	#----------------------------------------------------------------------
	def metaDataChanged(self):
		"""

		"""
		res = super(QNetworkReply,self).metaDataChanged()
		return res
	#----------------------------------------------------------------------
	def operation(self):
		"""
		Returns the operation that was posted for this reply.
		"""
		res = super(QNetworkReply,self).operation()
		isinstance(res,QtNetwork.QNetworkAccessManager.Operation)
		return res
	#----------------------------------------------------------------------
	def rawHeaderList(self):
		"""
		Returns a list of headers fields that were sent by the remote server, in the order that they were sent
		Duplicate headers are merged together and take place of the latter duplicate.
		"""
		res = super(QNetworkReply,self).rawHeaderList()
		return res
	#----------------------------------------------------------------------
	def rawHeaderPairs(self):
		"""
		Returns a list of raw header pairs.
		"""
		res = super(QNetworkReply,self).rawHeaderPairs()
		return res
	#----------------------------------------------------------------------
	def readBufferSize(self):
		"""
		Returns the size of the read buffer, in bytes.
		"""
		res = super(QNetworkReply,self).readBufferSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def request(self):
		"""
		Returns the request that was posted for this reply
		In special, note that the URL for the request may be different than that of the reply.
		"""
		res = super(QNetworkReply,self).request()
		isinstance(res,QtNetwork.QNetworkRequest)
		return res
	#----------------------------------------------------------------------
	def sslConfiguration(self):
		"""
		Returns the SSL configuration and state associated with this reply, if SSL was used
		It will contain the remote servers certificate, its certificate chain leading to the Certificate Authority as well as the encryption ciphers in use.
		The peers certificate and its certificate chain will be known by the time PySide.QtNetwork.QNetworkReply.sslErrors() is emitted, if its emitted.
		"""
		res = super(QNetworkReply,self).sslConfiguration()
		isinstance(res,QtNetwork.QSslConfiguration)
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the URL of the content downloaded or uploaded
		Note that the URL may be different from that of the original request.
		"""
		res = super(QNetworkReply,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def attribute(self,code):
		"""
		attribute(code)
			code=QtNetwork.QNetworkRequest.Attribute


		"""
		res = super(QNetworkReply,self).attribute(code)
		return res
	#----------------------------------------------------------------------
	def error(self,arg__1):
		"""
		error(arg__1)
			arg__1=QtNetwork.QNetworkReply.NetworkError


		"""
		res = super(QNetworkReply,self).error(arg__1)
		return res
	#----------------------------------------------------------------------
	def hasRawHeader(self,headerName):
		"""
		hasRawHeader(headerName)
			headerName=QtCore.QByteArray

		Returns true if the raw header of name headerName was sent by the remote server
		"""
		res = super(QNetworkReply,self).hasRawHeader(headerName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def header(self,header):
		"""
		header(header)
			header=QtNetwork.QNetworkRequest.KnownHeaders


		"""
		res = super(QNetworkReply,self).header(header)
		return res
	#----------------------------------------------------------------------
	def ignoreSslErrors(self,errors):
		"""
		ignoreSslErrors(errors)
			errors=unKnown


		"""
		res = super(QNetworkReply,self).ignoreSslErrors(errors)
		return res
	#----------------------------------------------------------------------
	def rawHeader(self,headerName):
		"""
		rawHeader(headerName)
			headerName=QtCore.QByteArray

		Returns the raw contents of the header headerName as sent by the remote server
		If there is no such header, returns an empty byte array, which may be indistinguishable from an empty header
		Use PySide.QtNetwork.QNetworkReply.hasRawHeader() to verify if the server sent such header field.
		"""
		res = super(QNetworkReply,self).rawHeader(headerName)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,code,value):
		"""
		setAttribute(code,value)
			code=QtNetwork.QNetworkRequest.Attribute
			value=object


		"""
		res = super(QNetworkReply,self).setAttribute(code,value)
		return res
	#----------------------------------------------------------------------
	def setError(self,errorCode,errorString):
		"""
		setError(errorCode,errorString)
			errorCode=QtNetwork.QNetworkReply.NetworkError
			errorString=unicode

		Sets the error condition to be errorCode
		The human-readable message is set with errorString .
		Calling PySide.QtNetwork.QNetworkReply.setError() does not emit the error( QNetworkReply.NetworkError ) signal.
		"""
		res = super(QNetworkReply,self).setError(errorCode,errorString)
		return res
	#----------------------------------------------------------------------
	def setHeader(self,header,value):
		"""
		setHeader(header,value)
			header=QtNetwork.QNetworkRequest.KnownHeaders
			value=object


		"""
		res = super(QNetworkReply,self).setHeader(header,value)
		return res
	#----------------------------------------------------------------------
	def setOperation(self,operation):
		"""
		setOperation(operation)
			operation=QtNetwork.QNetworkAccessManager.Operation


		"""
		res = super(QNetworkReply,self).setOperation(operation)
		return res
	#----------------------------------------------------------------------
	def setRawHeader(self,headerName,value):
		"""
		setRawHeader(headerName,value)
			headerName=QtCore.QByteArray
			value=QtCore.QByteArray

		Sets the raw header headerName to be of value value
		If headerName was previously set, it is overridden
		Multiple HTTP headers of the same name are functionally equivalent to one single header with the values concatenated, separated by commas.
		If headerName matches a known header, the value value will be parsed and the corresponding parsed form will also be set.
		"""
		res = super(QNetworkReply,self).setRawHeader(headerName,value)
		return res
	#----------------------------------------------------------------------
	def setReadBufferSize(self,size):
		"""
		setReadBufferSize(size)
			size=QtCore.qint64

		Sets the size of the read buffer to be size bytes
		The read buffer is the buffer that holds data that is being downloaded off the network, before it is read with QIODevice.read()
		Setting the buffer size to 0 will make the buffer unlimited in size.
		PySide.QtNetwork.QNetworkReply will try to stop reading from the network once this buffer is full (i.e., PySide.QtCore.QIODevice.bytesAvailable() returns size or more), thus causing the download to throttle down as well
		If the buffer is not limited in size, PySide.QtNetwork.QNetworkReply will try to download as fast as possible from the network.
		Unlike QAbstractSocket.setReadBufferSize() , PySide.QtNetwork.QNetworkReply cannot guarantee precision in the read buffer size
		That is, PySide.QtCore.QIODevice.bytesAvailable() can return more than size .
		"""
		res = super(QNetworkReply,self).setReadBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setRequest(self,request):
		"""
		setRequest(request)
			request=QtNetwork.QNetworkRequest

		Sets the associated request for this object to be request
		This value will be returned by PySide.QtNetwork.QNetworkReply.request() .
		Note: the request should be set when this object is created and not changed again.
		"""
		res = super(QNetworkReply,self).setRequest(request)
		return res
	#----------------------------------------------------------------------
	def setSslConfiguration(self,configuration):
		"""
		setSslConfiguration(configuration)
			configuration=QtNetwork.QSslConfiguration

		Sets the SSL configuration for the network connection associated with this request, if possible, to be that of config .
		"""
		res = super(QNetworkReply,self).setSslConfiguration(configuration)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		Sets the URL being processed to be url
		Normally, the URL matches that of the request that was posted, but for a variety of reasons it can be different (for example, a file path being made absolute or canonical).
		"""
		res = super(QNetworkReply,self).setUrl(url)
		return res
