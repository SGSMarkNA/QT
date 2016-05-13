from PySide import QtGui, QtCore

class QNetworkDiskCache(QtNetwork.QNetworkDiskCache):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkDiskCache,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cacheDirectory(self):
		"""
		Returns the location where cached files will be stored.
		"""
		res = super(QNetworkDiskCache,self).cacheDirectory()
		return res
	#----------------------------------------------------------------------
	def expire(self):
		"""
		Cleans the cache so that its size is under the maximum cache size
		Returns the current size of the cache.
		When the current size of the cache is greater than the PySide.QtNetwork.QNetworkDiskCache.maximumCacheSize() older cache files are removed until the total size is less then 90% of PySide.QtNetwork.QNetworkDiskCache.maximumCacheSize() starting with the oldest ones first using the file creation date to determine how old a cache file is.
		Subclasses can reimplement this function to change the order that cache files are removed taking into account information in the application knows about that PySide.QtNetwork.QNetworkDiskCache does not, for example the number of times a cache is accessed.
		Note: PySide.QtNetwork.QNetworkDiskCache.cacheSize() calls expire if the current cache size is unknown.
		"""
		res = super(QNetworkDiskCache,self).expire()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def maximumCacheSize(self):
		"""
		Returns the current maximum size for the disk cache.
		"""
		res = super(QNetworkDiskCache,self).maximumCacheSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def fileMetaData(self,fileName):
		"""
		fileMetaData(fileName)
			fileName=unicode

		Returns the PySide.QtNetwork.QNetworkCacheMetaData for the cache file fileName .
		If fileName is not a cache file PySide.QtNetwork.QNetworkCacheMetaData will be invalid.
		"""
		res = super(QNetworkDiskCache,self).fileMetaData(fileName)
		isinstance(res,QtNetwork.QNetworkCacheMetaData)
		return res
	#----------------------------------------------------------------------
	def setCacheDirectory(self,cacheDir):
		"""
		setCacheDirectory(cacheDir)
			cacheDir=unicode

		Sets the directory where cached files will be stored to cacheDir
		PySide.QtNetwork.QNetworkDiskCache will create this directory if it does not exists.
		Prepared cache items will be stored in the new cache directory when they are inserted.
		"""
		res = super(QNetworkDiskCache,self).setCacheDirectory(cacheDir)
		return res
	#----------------------------------------------------------------------
	def setMaximumCacheSize(self,size):
		"""
		setMaximumCacheSize(size)
			size=QtCore.qint64

		Sets the maximum size of the disk cache to be size .
		If the new size is smaller then the current cache size then the cache will call PySide.QtNetwork.QNetworkDiskCache.expire() .
		"""
		res = super(QNetworkDiskCache,self).setMaximumCacheSize(size)
		return res
