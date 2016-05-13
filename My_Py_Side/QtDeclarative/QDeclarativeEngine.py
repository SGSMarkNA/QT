from PySide import QtGui, QtCore

class QDeclarativeEngine(QtDeclarative.QDeclarativeEngine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeEngine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def baseUrl(self):
		"""
		Return the base URL for this engine
		The base URL is only used to resolve components when a relative URL is passed to the PySide.QtDeclarative.QDeclarativeComponent constructor.
		If a base URL has not been explicitly set, this method returns the applications current working directory.
		"""
		res = super(QDeclarativeEngine,self).baseUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def clearComponentCache(self):
		"""
		Clears the engines internal component cache.
		Normally the PySide.QtDeclarative.QDeclarativeEngine caches components loaded from qml files
		This method clears this cache and forces the component to be reloaded.
		"""
		res = super(QDeclarativeEngine,self).clearComponentCache()
		return res
	#----------------------------------------------------------------------
	def importPathList(self):
		"""
		Returns the list of directories where the engine searches for installed modules in a URL-based directory structure.
		For example, if /opt/MyApp/lib/imports is in the path, then QML that imports com.mycompany.Feature will cause the PySide.QtDeclarative.QDeclarativeEngine to look in /opt/MyApp/lib/imports/com/mycompany/Feature/ for the components provided by that module
		A qmldir file is required for defining the type version mapping and possibly declarative extensions plugins.
		By default, the list contains the directory of the application executable, paths specified in the QML_IMPORT_PATH environment variable, and the builtin ImportsPath from PySide.QtCore.QLibraryInfo .
		"""
		res = super(QDeclarativeEngine,self).importPathList()
		return res
	#----------------------------------------------------------------------
	def networkAccessManager(self):
		"""
		Returns a common PySide.QtNetwork.QNetworkAccessManager which can be used by any QML element instantiated by this engine.
		If a PySide.QtDeclarative.QDeclarativeNetworkAccessManagerFactory has been set and a PySide.QtNetwork.QNetworkAccessManager has not yet been created, the PySide.QtDeclarative.QDeclarativeNetworkAccessManagerFactory will be used to create the PySide.QtNetwork.QNetworkAccessManager ; otherwise the returned PySide.QtNetwork.QNetworkAccessManager will have no proxy or cache set.
		"""
		res = super(QDeclarativeEngine,self).networkAccessManager()
		isinstance(res,QtNetwork.QNetworkAccessManager)
		return res
	#----------------------------------------------------------------------
	def networkAccessManagerFactory(self):
		"""
		Returns the current PySide.QtDeclarative.QDeclarativeNetworkAccessManagerFactory .
		"""
		res = super(QDeclarativeEngine,self).networkAccessManagerFactory()
		isinstance(res,QtDeclarative.QDeclarativeNetworkAccessManagerFactory)
		return res
	#----------------------------------------------------------------------
	def offlineStoragePath(self):
		"""
		This property holds the directory for storing offline user data.
		Returns the directory where SQL and other offline storage is placed.
		QDeclarativeWebView and the SQL databases created with openDatabase() are stored here.
		The default is QML/OfflineStorage in the platform-standard user application data directory.
		Note that the path may not currently exist on the filesystem, so callers wanting to create new files at this location should create it first - see QDir.mkpath() .
		"""
		res = super(QDeclarativeEngine,self).offlineStoragePath()
		return res
	#----------------------------------------------------------------------
	def outputWarningsToStandardError(self):
		"""
		Returns true if warning messages will be output to stderr in addition to being emitted by the PySide.QtDeclarative.QDeclarativeEngine.warnings() signal, otherwise false.
		The default value is true.
		"""
		res = super(QDeclarativeEngine,self).outputWarningsToStandardError()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pluginPathList(self):
		"""
		Returns the list of directories where the engine searches for native plugins for imported modules (referenced in the qmldir file).
		By default, the list contains only
		, i.e
		the engine searches in the directory of the qmldir file itself.
		"""
		res = super(QDeclarativeEngine,self).pluginPathList()
		return res
	#----------------------------------------------------------------------
	def quit(self):
		"""

		"""
		res = super(QDeclarativeEngine,self).quit()
		return res
	#----------------------------------------------------------------------
	def rootContext(self):
		"""
		Returns the engines root context.
		The root context is automatically created by the PySide.QtDeclarative.QDeclarativeEngine
		Data that should be available to all QML component instances instantiated by the engine should be put in the root context.
		Additional data that should only be available to a subset of component instances should be added to sub-contexts parented to the root context.
		"""
		res = super(QDeclarativeEngine,self).rootContext()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def addImageProvider(self,id,arg__2):
		"""
		addImageProvider(id,arg__2)
			id=unicode
			arg__2=QtDeclarative.QDeclarativeImageProvider

		Sets the provider to use for images requested via the image : url scheme, with host providerId
		The PySide.QtDeclarative.QDeclarativeEngine takes ownership of provider .
		Image providers enable support for pixmap and threaded image requests
		See the PySide.QtDeclarative.QDeclarativeImageProvider documentation for details on implementing and using image providers.
		All required image providers should be added to the engine before any QML sources files are loaded.
		Note that images loaded from a PySide.QtDeclarative.QDeclarativeImageProvider are cached by PySide.QtGui.QPixmapCache , similar to any image loaded by QML.
		"""
		res = super(QDeclarativeEngine,self).addImageProvider(id,arg__2)
		return res
	#----------------------------------------------------------------------
	def addImportPath(self,dir):
		"""
		addImportPath(dir)
			dir=unicode

		Adds path as a directory where the engine searches for installed modules in a URL-based directory structure
		The path may be a local filesystem directory or a URL.
		The newly added path will be first in the PySide.QtDeclarative.QDeclarativeEngine.importPathList() .
		"""
		res = super(QDeclarativeEngine,self).addImportPath(dir)
		return res
	#----------------------------------------------------------------------
	def addPluginPath(self,dir):
		"""
		addPluginPath(dir)
			dir=unicode

		Adds path as a directory where the engine searches for native plugins for imported modules (referenced in the qmldir file).
		By default, the list contains only
		, i.e
		the engine searches in the directory of the qmldir file itself.
		The newly added path will be first in the PySide.QtDeclarative.QDeclarativeEngine.pluginPathList() .
		"""
		res = super(QDeclarativeEngine,self).addPluginPath(dir)
		return res
	#----------------------------------------------------------------------
	def imageProvider(self,id):
		"""
		imageProvider(id)
			id=unicode

		Returns the PySide.QtDeclarative.QDeclarativeImageProvider set for providerId .
		"""
		res = super(QDeclarativeEngine,self).imageProvider(id)
		isinstance(res,QtDeclarative.QDeclarativeImageProvider)
		return res
	#----------------------------------------------------------------------
	def importPlugin(self,filePath,uri,errorString):
		"""
		importPlugin(filePath,uri,errorString)
			filePath=unicode
			uri=unicode
			errorString=unicode

		Imports the plugin named filePath with the uri provided
		Returns true if the plugin was successfully imported; otherwise returns false.
		On failure and if non-null, *``errorString`` will be set to a message describing the failure.
		The plugin has to be a Qt plugin which implements the PySide.QtDeclarative.QDeclarativeExtensionPlugin interface.
		"""
		res = super(QDeclarativeEngine,self).importPlugin(filePath,uri,errorString)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def removeImageProvider(self,id):
		"""
		removeImageProvider(id)
			id=unicode

		Removes the PySide.QtDeclarative.QDeclarativeImageProvider for providerId .
		Returns the provider if it was found; otherwise returns 0.
		"""
		res = super(QDeclarativeEngine,self).removeImageProvider(id)
		return res
	#----------------------------------------------------------------------
	def setBaseUrl(self,arg__1):
		"""
		setBaseUrl(arg__1)
			arg__1=QtCore.QUrl

		Set the base URL for this engine to url .
		"""
		res = super(QDeclarativeEngine,self).setBaseUrl(arg__1)
		return res
	#----------------------------------------------------------------------
	def setImportPathList(self,paths):
		"""
		setImportPathList(paths)
			paths=list

		Sets paths as the list of directories where the engine searches for installed modules in a URL-based directory structure.
		By default, the list contains the directory of the application executable, paths specified in the QML_IMPORT_PATH environment variable, and the builtin ImportsPath from PySide.QtCore.QLibraryInfo .
		"""
		res = super(QDeclarativeEngine,self).setImportPathList(paths)
		return res
	#----------------------------------------------------------------------
	def setNetworkAccessManagerFactory(self,arg__1):
		"""
		setNetworkAccessManagerFactory(arg__1)
			arg__1=QtDeclarative.QDeclarativeNetworkAccessManagerFactory

		Sets the factory to use for creating PySide.QtNetwork.QNetworkAccessManager (s).
		PySide.QtNetwork.QNetworkAccessManager is used for all network access by QML
		By implementing a factory it is possible to create custom PySide.QtNetwork.QNetworkAccessManager with specialized caching, proxy and cookie support.
		The factory must be set before executing the engine.
		"""
		res = super(QDeclarativeEngine,self).setNetworkAccessManagerFactory(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOfflineStoragePath(self,dir):
		"""
		setOfflineStoragePath(dir)
			dir=unicode

		This property holds the directory for storing offline user data.
		Returns the directory where SQL and other offline storage is placed.
		QDeclarativeWebView and the SQL databases created with openDatabase() are stored here.
		The default is QML/OfflineStorage in the platform-standard user application data directory.
		Note that the path may not currently exist on the filesystem, so callers wanting to create new files at this location should create it first - see QDir.mkpath() .
		"""
		res = super(QDeclarativeEngine,self).setOfflineStoragePath(dir)
		return res
	#----------------------------------------------------------------------
	def setOutputWarningsToStandardError(self,arg__1):
		"""
		setOutputWarningsToStandardError(arg__1)
			arg__1=QtCore.bool

		Set whether warning messages will be output to stderr to enabled .
		If enabled is true, any warning messages generated by QML will be output to stderr and emitted by the PySide.QtDeclarative.QDeclarativeEngine.warnings() signal
		If enabled is false, on the PySide.QtDeclarative.QDeclarativeEngine.warnings() signal will be emitted
		This allows applications to handle warning output themselves.
		The default value is true.
		"""
		res = super(QDeclarativeEngine,self).setOutputWarningsToStandardError(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPluginPathList(self,paths):
		"""
		setPluginPathList(paths)
			paths=list

		Sets the list of directories where the engine searches for native plugins for imported modules (referenced in the qmldir file) to paths .
		By default, the list contains only
		, i.e
		the engine searches in the directory of the qmldir file itself.
		"""
		res = super(QDeclarativeEngine,self).setPluginPathList(paths)
		return res
