from PySide import QtGui, QtCore

class QNetworkCacheMetaData(QtNetwork.QNetworkCacheMetaData):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkCacheMetaData,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def attributes(self):
		"""
		Returns all the attributes stored with this cache item.
		"""
		res = super(QNetworkCacheMetaData,self).attributes()
		return res
	#----------------------------------------------------------------------
	def expirationDate(self):
		"""
		Returns the date and time when the meta data expires.
		"""
		res = super(QNetworkCacheMetaData,self).expirationDate()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this network cache meta data has attributes that have been set otherwise false.
		"""
		res = super(QNetworkCacheMetaData,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lastModified(self):
		"""
		Returns the date and time when the meta data was last modified.
		"""
		res = super(QNetworkCacheMetaData,self).lastModified()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def rawHeaders(self):
		"""
		Returns a list of all raw headers that are set in this meta data
		The list is in the same order that the headers were set.
		"""
		res = super(QNetworkCacheMetaData,self).rawHeaders()
		return res
	#----------------------------------------------------------------------
	def saveToDisk(self):
		"""
		Returns is this cache should be allowed to be stored on disk.
		Some cache implementations can keep these cache items in memory for performance reasons, but for security reasons they should not be written to disk.
		Specifically with http, documents marked with Pragma: no-cache, or have a Cache-control set to no-store or no-cache or any https document that doesnt have Cache-control: public set will set the saveToDisk to false.
		"""
		res = super(QNetworkCacheMetaData,self).saveToDisk()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the URL this network cache meta data is referring to.
		"""
		res = super(QNetworkCacheMetaData,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkCacheMetaData

		Returns true if this meta data is not equal to the other meta data; otherwise returns false.
		"""
		res = super(QNetworkCacheMetaData,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkCacheMetaData

		Returns true if this meta data is equal to the other meta data; otherwise returns false.
		"""
		res = super(QNetworkCacheMetaData,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAttributes(self,attributes):
		"""
		setAttributes(attributes)
			attributes=unKnown


		"""
		res = super(QNetworkCacheMetaData,self).setAttributes(attributes)
		return res
	#----------------------------------------------------------------------
	def setExpirationDate(self,dateTime):
		"""
		setExpirationDate(dateTime)
			dateTime=QtCore.QDateTime

		Sets the date and time when the meta data expires to dateTime .
		"""
		res = super(QNetworkCacheMetaData,self).setExpirationDate(dateTime)
		return res
	#----------------------------------------------------------------------
	def setLastModified(self,dateTime):
		"""
		setLastModified(dateTime)
			dateTime=QtCore.QDateTime

		Sets the date and time when the meta data was last modified to dateTime .
		"""
		res = super(QNetworkCacheMetaData,self).setLastModified(dateTime)
		return res
	#----------------------------------------------------------------------
	def setRawHeaders(self,headers):
		"""
		setRawHeaders(headers)
			headers=unKnown


		"""
		res = super(QNetworkCacheMetaData,self).setRawHeaders(headers)
		return res
	#----------------------------------------------------------------------
	def setSaveToDisk(self,allow):
		"""
		setSaveToDisk(allow)
			allow=QtCore.bool

		Sets whether this network cache meta data and associated content should be allowed to be stored on disk to allow .
		"""
		res = super(QNetworkCacheMetaData,self).setSaveToDisk(allow)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		Sets the URL this network cache meta data to to be url .
		The password and fragment are removed from the url.
		"""
		res = super(QNetworkCacheMetaData,self).setUrl(url)
		return res
