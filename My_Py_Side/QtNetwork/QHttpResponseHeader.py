from PySide import QtGui, QtCore

class QHttpResponseHeader(QtNetwork.QHttpResponseHeader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHttpResponseHeader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def reasonPhrase(self):
		"""
		Returns the reason phrase of the HTTP response header.
		"""
		res = super(QHttpResponseHeader,self).reasonPhrase()
		return res
	#----------------------------------------------------------------------
	def statusCode(self):
		"""
		Returns the status code of the HTTP response header.
		"""
		res = super(QHttpResponseHeader,self).statusCode()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setStatusLine(self,code,text=None,majorVer=None,minorVer=None):
		"""
		setStatusLine(code,text=None,majorVer=None,minorVer=None)
			code=QtCore.int
			text=unicode
			majorVer=QtCore.int
			minorVer=QtCore.int

		Sets the status code to code , the reason phrase to text and the protocol-version to majorVer and minorVer .
		"""
		res = super(QHttpResponseHeader,self).setStatusLine(code,text,majorVer,minorVer)
		return res
