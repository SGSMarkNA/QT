from PySide import QtGui, QtCore

class QDeclarativeComponent(QtDeclarative.QDeclarativeComponent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeComponent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def completeCreate(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).completeCreate()
		return res
	#----------------------------------------------------------------------
	def creationContext(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).creationContext()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).errorString()
		return res
	#----------------------------------------------------------------------
	def errors(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).errors()
		return res
	#----------------------------------------------------------------------
	def isError(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).isError()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isLoading(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).isLoading()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReady(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).isReady()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def progress(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).progress()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).status()
		isinstance(res,QtDeclarative.QDeclarativeComponent.Status)
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""

		"""
		res = super(QDeclarativeComponent,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def beginCreate(self,arg__1):
		"""
		beginCreate(arg__1)
			arg__1=QtDeclarative.QDeclarativeContext


		"""
		res = super(QDeclarativeComponent,self).beginCreate(arg__1)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def create(self,context=None):
		"""
		create(context=None)
			context=QtDeclarative.QDeclarativeContext


		"""
		res = super(QDeclarativeComponent,self).create(context)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def createObject(self,parent):
		"""
		createObject(parent)
			parent=QtCore.QObject


		"""
		res = super(QDeclarativeComponent,self).createObject(parent)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def loadUrl(self,url):
		"""
		loadUrl(url)
			url=QtCore.QUrl


		"""
		res = super(QDeclarativeComponent,self).loadUrl(url)
		return res
	#----------------------------------------------------------------------
	def setData(self,arg__1,baseUrl):
		"""
		setData(arg__1,baseUrl)
			arg__1=QtCore.QByteArray
			baseUrl=QtCore.QUrl


		"""
		res = super(QDeclarativeComponent,self).setData(arg__1,baseUrl)
		return res
