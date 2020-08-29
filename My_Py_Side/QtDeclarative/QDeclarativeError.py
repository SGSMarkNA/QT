from PySide import QtGui, QtCore

class QDeclarativeError(QtDeclarative.QDeclarativeError):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeError,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the error column number.
		"""
		res = super(QDeclarativeError,self).column()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def description(self):
		"""
		Returns the error description.
		"""
		res = super(QDeclarativeError,self).description()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this error is valid, otherwise false.
		"""
		res = super(QDeclarativeError,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def line(self):
		"""
		Returns the error line number.
		"""
		res = super(QDeclarativeError,self).line()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns the error as a human readable string.
		"""
		res = super(QDeclarativeError,self).toString()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		Returns the url for the file that caused this error.
		"""
		res = super(QDeclarativeError,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def setColumn(self,arg__1):
		"""
		setColumn(arg__1)
			arg__1=QtCore.int

		Sets the error column number.
		"""
		res = super(QDeclarativeError,self).setColumn(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDescription(self,arg__1):
		"""
		setDescription(arg__1)
			arg__1=unicode

		Sets the error description .
		"""
		res = super(QDeclarativeError,self).setDescription(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLine(self,arg__1):
		"""
		setLine(arg__1)
			arg__1=QtCore.int

		Sets the error line number.
		"""
		res = super(QDeclarativeError,self).setLine(arg__1)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,arg__1):
		"""
		setUrl(arg__1)
			arg__1=QtCore.QUrl

		Sets the url for the file that caused this error.
		"""
		res = super(QDeclarativeError,self).setUrl(arg__1)
		return res
