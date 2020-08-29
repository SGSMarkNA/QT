from PySide import QtGui, QtCore

class QNetworkRequest(QtNetwork.QNetworkRequest):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkRequest,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def originatingObject(self):
		"""
		Returns a reference to the object that initiated this network request; returns 0 if not set or the object has been destroyed.
		"""
		res = super(QNetworkRequest,self).originatingObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def priority(self):
		"""
		Return the priority of this request.
		"""
		res = super(QNetworkRequest,self).priority()
		isinstance(res,QtNetwork.QNetworkRequest.Priority)
		return res
	#----------------------------------------------------------------------
	def rawHeaderList(self):
		"""
		Returns a list of all raw headers that are set in this network request
		The list is in the order that the headers were set.
		"""
		res = super(QNetworkRequest,self).rawHeaderList()
		return res
	#----------------------------------------------------------------------
	def sslConfiguration(self):
		"""
		Returns this network requests SSL configuration
		By default, no SSL settings are specified.
		"""
		res = super(QNetworkRequest,self).sslConfiguration()
		isinstance(res,QtNetwork.QSslConfiguration)
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the URL this network request is referring to.
		"""
		res = super(QNetworkRequest,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def attribute(self,code,defaultValue=None):
		"""
		attribute(code,defaultValue=None)
			code=QtNetwork.QNetworkRequest.Attribute
			defaultValue=object

		Returns the attribute associated with the code code
		If the attribute has not been set, it returns defaultValue .
		Note: this function does not apply the defaults listed in QNetworkRequest.Attribute .
		"""
		res = super(QNetworkRequest,self).attribute(code,defaultValue)
		return res
	#----------------------------------------------------------------------
	def hasRawHeader(self,headerName):
		"""
		hasRawHeader(headerName)
			headerName=QtCore.QByteArray

		Returns true if the raw header headerName is present in this network request.
		"""
		res = super(QNetworkRequest,self).hasRawHeader(headerName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def header(self,header):
		"""
		header(header)
			header=QtNetwork.QNetworkRequest.KnownHeaders

		Returns the value of the known network header header if it is present in this request
		If it is not present, returns QVariant() (i.e., an invalid variant).
		"""
		res = super(QNetworkRequest,self).header(header)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkRequest

		Returns false if this object is not the same as other .
		"""
		res = super(QNetworkRequest,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkRequest

		Returns true if this object is the same as other (i.e., if they have the same URL, same headers and same meta-data settings).
		"""
		res = super(QNetworkRequest,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rawHeader(self,headerName):
		"""
		rawHeader(headerName)
			headerName=QtCore.QByteArray

		Returns the raw form of header headerName
		If no such header is present, an empty PySide.QtCore.QByteArray is returned, which may be indistinguishable from a header that is present but has no content (use PySide.QtNetwork.QNetworkRequest.hasRawHeader() to find out if the header exists or not).
		Raw headers can be set with PySide.QtNetwork.QNetworkRequest.setRawHeader() or with PySide.QtNetwork.QNetworkRequest.setHeader() .
		"""
		res = super(QNetworkRequest,self).rawHeader(headerName)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,code,value):
		"""
		setAttribute(code,value)
			code=QtNetwork.QNetworkRequest.Attribute
			value=object

		Sets the attribute associated with code code to be value value
		If the attribute is already set, the previous value is discarded
		In special, if value is an invalid PySide.QtCore.QVariant , the attribute is unset.
		"""
		res = super(QNetworkRequest,self).setAttribute(code,value)
		return res
	#----------------------------------------------------------------------
	def setHeader(self,header,value):
		"""
		setHeader(header,value)
			header=QtNetwork.QNetworkRequest.KnownHeaders
			value=object

		Sets the value of the known header header to be value , overriding any previously set headers
		This operation also sets the equivalent raw HTTP header.
		"""
		res = super(QNetworkRequest,self).setHeader(header,value)
		return res
	#----------------------------------------------------------------------
	def setOriginatingObject(self,object):
		"""
		setOriginatingObject(object)
			object=QtCore.QObject

		Allows setting a reference to the object initiating the request.
		For example QtWebKit sets the originating object to the PySide.QtWebKit.QWebFrame that initiated the request.
		"""
		res = super(QNetworkRequest,self).setOriginatingObject(object)
		return res
	#----------------------------------------------------------------------
	def setPriority(self,priority):
		"""
		setPriority(priority)
			priority=QtNetwork.QNetworkRequest.Priority

		Set the priority of this request to priority .
		"""
		res = super(QNetworkRequest,self).setPriority(priority)
		return res
	#----------------------------------------------------------------------
	def setRawHeader(self,headerName,value):
		"""
		setRawHeader(headerName,value)
			headerName=QtCore.QByteArray
			value=QtCore.QByteArray

		Sets the header headerName to be of value headerValue
		If headerName corresponds to a known header (see QNetworkRequest.KnownHeaders ), the raw format will be parsed and the corresponding cooked header will be set as well.
		For example:
		will also set the known header LastModifiedHeader to be the PySide.QtCore.QDateTime object of the parsed date.
		Note: setting the same header twice overrides the previous setting
		To accomplish the behaviour of multiple HTTP headers of the same name, you should concatenate the two values, separating them with a comma (,) and set one single raw header.
		"""
		res = super(QNetworkRequest,self).setRawHeader(headerName,value)
		return res
	#----------------------------------------------------------------------
	def setSslConfiguration(self,configuration):
		"""
		setSslConfiguration(configuration)
			configuration=QtNetwork.QSslConfiguration

		Sets this network requests SSL configuration to be config
		The settings that apply are the private key, the local certificate, the SSL protocol (SSLv2, SSLv3, TLSv1 where applicable) and the ciphers that the SSL backend is allowed to use.
		By default, no SSL configuration is set, which allows the backends to choose freely what configuration is best for them.
		"""
		res = super(QNetworkRequest,self).setSslConfiguration(configuration)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		Sets the URL this network request is referring to to be url .
		"""
		res = super(QNetworkRequest,self).setUrl(url)
		return res
