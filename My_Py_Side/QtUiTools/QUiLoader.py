from PySide import QtGui, QtCore

class QUiLoader(QtUiTools.QUiLoader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUiLoader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def availableLayouts(self):
		"""
		Returns a list naming all available layouts that can be built using the PySide.QtUiTools.QUiLoader.createLayout() function
		"""
		res = super(QUiLoader,self).availableLayouts()
		return res
	#----------------------------------------------------------------------
	def availableWidgets(self):
		"""
		Returns a list naming all available widgets that can be built using the PySide.QtUiTools.QUiLoader.createWidget() function, i.e all the widgets specified within the given plugin paths.
		"""
		res = super(QUiLoader,self).availableWidgets()
		return res
	#----------------------------------------------------------------------
	def clearPluginPaths(self):
		"""
		Clears the list of paths in which the loader will search when locating plugins.
		"""
		res = super(QUiLoader,self).clearPluginPaths()
		return res
	#----------------------------------------------------------------------
	def isLanguageChangeEnabled(self):
		"""
		Returns true if dynamic retranslation on language change is enabled; returns false otherwise.
		"""
		res = super(QUiLoader,self).isLanguageChangeEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isScriptingEnabled(self):
		"""
		Returns true if execution of scripts is enabled; returns false otherwise.
		"""
		res = super(QUiLoader,self).isScriptingEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTranslationEnabled(self):
		"""
		Returns true if translation is enabled; returns false otherwise.
		"""
		res = super(QUiLoader,self).isTranslationEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pluginPaths(self):
		"""
		Returns a list naming the paths in which the loader will search when locating custom widget plugins.
		"""
		res = super(QUiLoader,self).pluginPaths()
		return res
	#----------------------------------------------------------------------
	def workingDirectory(self):
		"""
		Returns the working directory of the loader.
		"""
		res = super(QUiLoader,self).workingDirectory()
		isinstance(res,QtCore.QDir)
		return res
	#----------------------------------------------------------------------
	def addPluginPath(self,path):
		"""
		addPluginPath(path)
			path=unicode

		Adds the given path to the list of paths in which the loader will search when locating plugins.
		"""
		res = super(QUiLoader,self).addPluginPath(path)
		return res
	#----------------------------------------------------------------------
	def createAction(self,parent=None,name=None):
		"""
		createAction(parent=None,name=None)
			parent=QtCore.QObject
			name=unicode

		Creates a new action with the given parent and name .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(QUiLoader,self).createAction(parent,name)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def createActionGroup(self,parent=None,name=None):
		"""
		createActionGroup(parent=None,name=None)
			parent=QtCore.QObject
			name=unicode

		Creates a new action group with the given parent and name .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(QUiLoader,self).createActionGroup(parent,name)
		isinstance(res,QtGui.QActionGroup)
		return res
	#----------------------------------------------------------------------
	def createLayout(self,className,parent=None,name=None):
		"""
		createLayout(className,parent=None,name=None)
			className=unicode
			parent=QtCore.QObject
			name=unicode

		Creates a new layout with the given parent and name using the class specified by className .
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(QUiLoader,self).createLayout(className,parent,name)
		isinstance(res,QtGui.QLayout)
		return res
	#----------------------------------------------------------------------
	def createWidget(self,className,parent=None,name=None):
		"""
		createWidget(className,parent=None,name=None)
			className=unicode
			parent=QtGui.QWidget
			name=unicode

		Creates a new widget with the given parent and name using the class specified by className
		You can use this function to create any of the widgets returned by the PySide.QtUiTools.QUiLoader.availableWidgets() function.
		The function is also used internally by the PySide.QtUiTools.QUiLoader class whenever it creates a widget
		Hence, you can subclass PySide.QtUiTools.QUiLoader and reimplement this function to intervene process of constructing a user interface or widget
		However, in your implementation, ensure that you call PySide.QtUiTools.QUiLoader s version first.
		"""
		res = super(QUiLoader,self).createWidget(className,parent,name)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(device,parentWidget=None)
			device=QtCore.QIODevice
			parentWidget=QtGui.QWidget

		load(arg__1,parentWidget=None)
			arg__1=unicode
			parentWidget=QtGui.QWidget

		Loads a form from the given device and creates a new widget with the given parentWidget to hold its contents.
		"""
		res = super(QUiLoader,self).load(*args,**kwargs)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def registerCustomWidget(self,customWidgetType):
		"""
		registerCustomWidget(customWidgetType)
			customWidgetType=Object

		Registers a Python created custom widget to QUiLoader, so it can be recognized when
                loading a .ui file
		The custom widget type is passed via the customWidgetType argument.
                This is needed when you want to override a virtual method of some widget in the interface,
                since duck punching will not work with widgets created by QUiLoader based on the contents
                of the .ui file.
		(Remember that duck punching virtual methods is an invitation for your own demise!)
		Lets see an obvious example
		If you want to create a new widget its probable youll end up
                overriding QWidgets paintEvent() method.
		"""
		res = super(QUiLoader,self).registerCustomWidget(customWidgetType)
		return res
	#----------------------------------------------------------------------
	def setLanguageChangeEnabled(self,enabled):
		"""
		setLanguageChangeEnabled(enabled)
			enabled=QtCore.bool

		If enabled is true, user interfaces loaded by this loader will automatically retranslate themselves upon receiving a language change event
		Otherwise, the user interfaces will not be retranslated.
		"""
		res = super(QUiLoader,self).setLanguageChangeEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setScriptingEnabled(self,enabled):
		"""
		setScriptingEnabled(enabled)
			enabled=QtCore.bool

		If enabled is true, the loader will be able to execute scripts
		Otherwise, execution of scripts will be disabled.
		"""
		res = super(QUiLoader,self).setScriptingEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setTranslationEnabled(self,enabled):
		"""
		setTranslationEnabled(enabled)
			enabled=QtCore.bool

		If enabled is true, user interfaces loaded by this loader will be translated
		Otherwise, the user interfaces will not be translated.
		"""
		res = super(QUiLoader,self).setTranslationEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setWorkingDirectory(self,dir):
		"""
		setWorkingDirectory(dir)
			dir=QtCore.QDir

		Sets the working directory of the loader to dir
		The loader will look for other resources, such as icons and resource files, in paths relative to this directory.
		"""
		res = super(QUiLoader,self).setWorkingDirectory(dir)
		return res
