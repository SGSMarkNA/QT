from PySide import QtGui, QtCore

class QPluginLoader(QtCore.QPluginLoader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPluginLoader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a text string with the description of the last error that occurred.
		"""
		res = super(QPluginLoader,self).errorString()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		This property holds the file name of the plugin.
		To be loadable, the files suffix must be a valid suffix for a loadable library in accordance with the platform, e.g
		.so on Unix, .dylib on Mac OS X, and .dll on Windows
		The suffix can be verified with QLibrary.isLibrary() .
		If the file name does not exist, it will not be set
		This property will then contain an empty string.
		By default, this property contains an empty string.
		Note: In Symbian the fileName must point to plugin stub file.
		"""
		res = super(QPluginLoader,self).fileName()
		return res
	#----------------------------------------------------------------------
	def instance(self):
		"""
		Returns the root component object of the plugin
		The plugin is loaded if necessary
		The function returns 0 if the plugin could not be loaded or if the root component object could not be instantiated.
		If the root component object was destroyed, calling this function creates a new instance.
		The root component, returned by this function, is not deleted when the PySide.QtCore.QPluginLoader is destroyed
		If you want to ensure that the root component is deleted, you should call PySide.QtCore.QPluginLoader.unload() as soon you dont need to access the core component anymore
		When the library is finally unloaded, the root component will automatically be deleted.
		The component object is a PySide.QtCore.QObject
		Use qobject_cast() to access interfaces you are interested in.
		"""
		res = super(QPluginLoader,self).instance()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def isLoaded(self):
		"""
		Returns true if the plugin is loaded; otherwise returns false.
		"""
		res = super(QPluginLoader,self).isLoaded()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def load(self):
		"""
		Loads the plugin and returns true if the plugin was loaded successfully; otherwise returns false
		Since PySide.QtCore.QPluginLoader.instance() always calls this function before resolving any symbols it is not necessary to call it explicitly
		In some situations you might want the plugin loaded in advance, in which case you would use this function.
		"""
		res = super(QPluginLoader,self).load()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def unload(self):
		"""
		Unloads the plugin and returns true if the plugin could be unloaded; otherwise returns false.
		This happens automatically on application termination, so you shouldnt normally need to call this function.
		If other instances of PySide.QtCore.QPluginLoader are using the same plugin, the call will fail, and unloading will only happen when every instance has called PySide.QtCore.QPluginLoader.unload() .
		Dont try to delete the root component
		Instead rely on that PySide.QtCore.QPluginLoader.unload() will automatically delete it when needed.
		"""
		res = super(QPluginLoader,self).unload()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,fileName):
		"""
		setFileName(fileName)
			fileName=unicode

		This property holds the file name of the plugin.
		To be loadable, the files suffix must be a valid suffix for a loadable library in accordance with the platform, e.g
		.so on Unix, .dylib on Mac OS X, and .dll on Windows
		The suffix can be verified with QLibrary.isLibrary() .
		If the file name does not exist, it will not be set
		This property will then contain an empty string.
		By default, this property contains an empty string.
		Note: In Symbian the fileName must point to plugin stub file.
		"""
		res = super(QPluginLoader,self).setFileName(fileName)
		return res
