from PySide import QtGui, QtCore

class QHttpRequestHeader(QtNetwork.QHttpRequestHeader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHttpRequestHeader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def method(self):
		"""
		Returns the method of the HTTP request header.
		"""
		res = super(QHttpRequestHeader,self).method()
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the request-URI of the HTTP request header.
		"""
		res = super(QHttpRequestHeader,self).path()
		return res
	#----------------------------------------------------------------------
	def setRequest(self,method,path,majorVer=None,minorVer=None):
		"""
		setRequest(method,path,majorVer=None,minorVer=None)
			method=unicode
			path=unicode
			majorVer=QtCore.int
			minorVer=QtCore.int

		This function sets the request method to method , the request-URI to path and the protocol-version to majorVer and minorVer
		The path argument must be properly encoded for an HTTP request.
		"""
		res = super(QHttpRequestHeader,self).setRequest(method,path,majorVer,minorVer)
		return res
