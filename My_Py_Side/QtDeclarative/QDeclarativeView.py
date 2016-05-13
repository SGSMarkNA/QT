from PySide import QtGui, QtCore

class QDeclarativeView(QtDeclarative.QDeclarativeView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def engine(self):
		"""
		Returns a pointer to the PySide.QtDeclarative.QDeclarativeEngine used for instantiating QML Components.
		"""
		res = super(QDeclarativeView,self).engine()
		isinstance(res,QtDeclarative.QDeclarativeEngine)
		return res
	#----------------------------------------------------------------------
	def errors(self):
		"""
		Return the list of errors that occurred during the last compile or create operation
		When the status is not Error, an empty list is returned.
		"""
		res = super(QDeclarativeView,self).errors()
		return res
	#----------------------------------------------------------------------
	def initialSize(self):
		"""
		Returns the initial size of the root object
		"""
		res = super(QDeclarativeView,self).initialSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def resizeMode(self):
		"""
		This property holds whether the view should resize the canvas contents.
		If this property is set to SizeViewToRootObject (the default), the view resizes with the root item in the QML.
		If this property is set to SizeRootObjectToView , the view will automatically resize the root item.
		Regardless of this property, the sizeHint of the view is the initial size of the root item
		Note though that since QML may load dynamically, that size may change.
		"""
		res = super(QDeclarativeView,self).resizeMode()
		isinstance(res,QtDeclarative.QDeclarativeView.ResizeMode)
		return res
	#----------------------------------------------------------------------
	def rootContext(self):
		"""
		This function returns the root of the context hierarchy
		Each QML component is instantiated in a PySide.QtDeclarative.QDeclarativeContext
		PySide.QtDeclarative.QDeclarativeContext s are essential for passing data to QML components
		In QML, contexts are arranged hierarchically and this hierarchy is managed by the PySide.QtDeclarative.QDeclarativeEngine .
		"""
		res = super(QDeclarativeView,self).rootContext()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def rootObject(self):
		"""
		Returns the views root item .
		"""
		res = super(QDeclarativeView,self).rootObject()
		isinstance(res,QtGui.QGraphicsObject)
		return res
	#----------------------------------------------------------------------
	def source(self):
		"""
		This property holds The URL of the source of the QML component..
		Changing this property causes the QML component to be reloaded.
		Ensure that the URL provided is full and correct, in particular, use QUrl.fromLocalFile() when loading a file from the local filesystem.
		"""
		res = super(QDeclarativeView,self).source()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""
		The components current status .
		"""
		res = super(QDeclarativeView,self).status()
		isinstance(res,QtDeclarative.QDeclarativeView.Status)
		return res
	#----------------------------------------------------------------------
	def setResizeMode(self,arg__1):
		"""
		setResizeMode(arg__1)
			arg__1=QtDeclarative.QDeclarativeView.ResizeMode

		This property holds whether the view should resize the canvas contents.
		If this property is set to SizeViewToRootObject (the default), the view resizes with the root item in the QML.
		If this property is set to SizeRootObjectToView , the view will automatically resize the root item.
		Regardless of this property, the sizeHint of the view is the initial size of the root item
		Note though that since QML may load dynamically, that size may change.
		"""
		res = super(QDeclarativeView,self).setResizeMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRootObject(self,obj):
		"""
		setRootObject(obj)
			obj=QtCore.QObject


		"""
		res = super(QDeclarativeView,self).setRootObject(obj)
		return res
	#----------------------------------------------------------------------
	def setSource(self,arg__1):
		"""
		setSource(arg__1)
			arg__1=QtCore.QUrl

		This property holds The URL of the source of the QML component..
		Changing this property causes the QML component to be reloaded.
		Ensure that the URL provided is full and correct, in particular, use QUrl.fromLocalFile() when loading a file from the local filesystem.
		"""
		res = super(QDeclarativeView,self).setSource(arg__1)
		return res
