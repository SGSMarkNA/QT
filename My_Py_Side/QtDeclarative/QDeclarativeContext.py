from PySide import QtGui, QtCore

class QDeclarativeContext(QtDeclarative.QDeclarativeContext):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeContext,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def baseUrl(self):
		"""

		"""
		res = super(QDeclarativeContext,self).baseUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def contextObject(self):
		"""

		"""
		res = super(QDeclarativeContext,self).contextObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def engine(self):
		"""

		"""
		res = super(QDeclarativeContext,self).engine()
		isinstance(res,QtDeclarative.QDeclarativeEngine)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""

		"""
		res = super(QDeclarativeContext,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def parentContext(self):
		"""

		"""
		res = super(QDeclarativeContext,self).parentContext()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def contextProperty(self,arg__1):
		"""
		contextProperty(arg__1)
			arg__1=unicode


		"""
		res = super(QDeclarativeContext,self).contextProperty(arg__1)
		return res
	#----------------------------------------------------------------------
	def resolvedUrl(self,arg__1):
		"""
		resolvedUrl(arg__1)
			arg__1=QtCore.QUrl


		"""
		res = super(QDeclarativeContext,self).resolvedUrl(arg__1)
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def setBaseUrl(self,arg__1):
		"""
		setBaseUrl(arg__1)
			arg__1=QtCore.QUrl


		"""
		res = super(QDeclarativeContext,self).setBaseUrl(arg__1)
		return res
	#----------------------------------------------------------------------
	def setContextObject(self,arg__1):
		"""
		setContextObject(arg__1)
			arg__1=QtCore.QObject


		"""
		res = super(QDeclarativeContext,self).setContextObject(arg__1)
		return res
	#----------------------------------------------------------------------
	def setContextProperty(self,*args,**kwargs):
		"""
		setContextProperty(arg__1,arg__2)
			arg__1=unicode
			arg__2=object

		setContextProperty(arg__1,arg__2)
			arg__1=unicode
			arg__2=QtCore.QObject


		"""
		res = super(QDeclarativeContext,self).setContextProperty(*args,**kwargs)
		return res
