from PySide import QtGui, QtCore

class QHostInfo(QtNetwork.QHostInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHostInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def addresses(self):
		"""
		Returns the list of IP addresses associated with PySide.QtNetwork.QHostInfo.hostName()
		This list may be empty.
		Example:
		"""
		res = super(QHostInfo,self).addresses()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that occurred if the host name lookup failed; otherwise returns NoError .
		"""
		res = super(QHostInfo,self).error()
		isinstance(res,QtNetwork.QHostInfo.HostInfoError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		If the lookup failed, this function returns a human readable description of the error; otherwise Unknown error is returned.
		"""
		res = super(QHostInfo,self).errorString()
		return res
	#----------------------------------------------------------------------
	def hostName(self):
		"""
		Returns the name of the host whose IP addresses were looked up.
		"""
		res = super(QHostInfo,self).hostName()
		return res
	#----------------------------------------------------------------------
	def lookupId(self):
		"""
		Returns the ID of this lookup.
		"""
		res = super(QHostInfo,self).lookupId()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setAddresses(self,addresses):
		"""
		setAddresses(addresses)
			addresses=unKnown


		"""
		res = super(QHostInfo,self).setAddresses(addresses)
		return res
	#----------------------------------------------------------------------
	def setError(self,error):
		"""
		setError(error)
			error=QtNetwork.QHostInfo.HostInfoError

		Sets the error type of this PySide.QtNetwork.QHostInfo to error .
		"""
		res = super(QHostInfo,self).setError(error)
		return res
	#----------------------------------------------------------------------
	def setErrorString(self,errorString):
		"""
		setErrorString(errorString)
			errorString=unicode

		Sets the human readable description of the error that occurred to str if the lookup failed.
		"""
		res = super(QHostInfo,self).setErrorString(errorString)
		return res
	#----------------------------------------------------------------------
	def setHostName(self,name):
		"""
		setHostName(name)
			name=unicode

		Sets the host name of this PySide.QtNetwork.QHostInfo to hostName .
		"""
		res = super(QHostInfo,self).setHostName(name)
		return res
	#----------------------------------------------------------------------
	def setLookupId(self,id):
		"""
		setLookupId(id)
			id=QtCore.int

		Sets the ID of this lookup to id .
		"""
		res = super(QHostInfo,self).setLookupId(id)
		return res
