from PySide import QtGui, QtCore

class QFileDialog(QtGui.QFileDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFileDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceptMode(self):
		"""
		This property holds the accept mode of the dialog.
		The action mode defines whether the dialog is for opening or saving files.
		By default, this property is set to AcceptOpen .
		"""
		res = super(QFileDialog,self).acceptMode()
		isinstance(res,QtGui.QFileDialog.AcceptMode)
		return res
	#----------------------------------------------------------------------
	def confirmOverwrite(self):
		"""
		This property holds whether the filedialog should ask before accepting a selected file, when the accept mode is AcceptSave .
		Use setOption( DontConfirmOverwrite , !*enabled* ) or !testOption( DontConfirmOverwrite ) instead.
		"""
		res = super(QFileDialog,self).confirmOverwrite()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def defaultSuffix(self):
		"""
		This property holds suffix added to the filename if no other suffix was specified.
		This property specifies a string that will be added to the filename if it has no suffix already
		The suffix is typically used to indicate the file type (e.g
		txt indicates a text file).
		"""
		res = super(QFileDialog,self).defaultSuffix()
		return res
	#----------------------------------------------------------------------
	def directory(self):
		"""
		Returns the directory currently being displayed in the dialog.
		"""
		res = super(QFileDialog,self).directory()
		isinstance(res,QtCore.QDir)
		return res
	#----------------------------------------------------------------------
	def fileMode(self):
		"""
		This property holds the file mode of the dialog.
		The file mode defines the number and type of items that the user is expected to select in the dialog.
		By default, this property is set to AnyFile .
		This function will set the labels for the FileName and Accept QFileDialog.DialogLabel s
		It is possible to set custom text after the call to PySide.QtGui.QFileDialog.setFileMode() .
		"""
		res = super(QFileDialog,self).fileMode()
		isinstance(res,QtGui.QFileDialog.FileMode)
		return res
	#----------------------------------------------------------------------
	def filter(self):
		"""
		Returns the filter that is used when displaying files.
		"""
		res = super(QFileDialog,self).filter()
		isinstance(res,QtCore.QDir.Filters)
		return res
	#----------------------------------------------------------------------
	def filters(self):
		"""
		Use PySide.QtGui.QFileDialog.nameFilters() instead.
		"""
		res = super(QFileDialog,self).filters()
		return res
	#----------------------------------------------------------------------
	def history(self):
		"""
		Returns the browsing history of the filedialog as a list of paths.
		"""
		res = super(QFileDialog,self).history()
		return res
	#----------------------------------------------------------------------
	def iconProvider(self):
		"""
		Returns the icon provider used by the filedialog.
		"""
		res = super(QFileDialog,self).iconProvider()
		isinstance(res,QtGui.QFileIconProvider)
		return res
	#----------------------------------------------------------------------
	def isNameFilterDetailsVisible(self):
		"""

		"""
		res = super(QFileDialog,self).isNameFilterDetailsVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds Whether the filedialog is read-only.
		If this property is set to false, the file dialog will allow renaming, and deleting of files and directories and creating directories.
		Use setOption( ReadOnly , enabled ) or testOption( ReadOnly ) instead.
		"""
		res = super(QFileDialog,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the item delegate used to render the items in the views in the filedialog.
		"""
		res = super(QFileDialog,self).itemDelegate()
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def nameFilters(self):
		"""
		Returns the file type filters that are in operation on this file dialog.
		"""
		res = super(QFileDialog,self).nameFilters()
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""

		"""
		res = super(QFileDialog,self).options()
		isinstance(res,QtGui.QFileDialog.Options)
		return res
	#----------------------------------------------------------------------
	def proxyModel(self):
		"""
		Returns the proxy model used by the file dialog
		By default no proxy is set.
		"""
		res = super(QFileDialog,self).proxyModel()
		isinstance(res,QtGui.QAbstractProxyModel)
		return res
	#----------------------------------------------------------------------
	def resolveSymlinks(self):
		"""
		This property holds whether the filedialog should resolve shortcuts.
		If this property is set to true, the file dialog will resolve shortcuts or symbolic links.
		Use setOption( DontResolveSymlinks , !``enabled`` ) or !testOption( DontResolveSymlinks ).
		"""
		res = super(QFileDialog,self).resolveSymlinks()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def saveState(self):
		"""
		Saves the state of the dialogs layout, history and current directory.
		Typically this is used in conjunction with PySide.QtCore.QSettings to remember the size for a future session
		A version number is stored as part of the data.
		"""
		res = super(QFileDialog,self).saveState()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def selectedFiles(self):
		"""
		Returns a list of strings containing the absolute paths of the selected files in the dialog
		If no files are selected, or the mode is not ExistingFiles or ExistingFile , PySide.QtGui.QFileDialog.selectedFiles() contains the current path in the viewport.
		"""
		res = super(QFileDialog,self).selectedFiles()
		return res
	#----------------------------------------------------------------------
	def selectedFilter(self):
		"""
		Use PySide.QtGui.QFileDialog.selectedNameFilter() instead.
		"""
		res = super(QFileDialog,self).selectedFilter()
		return res
	#----------------------------------------------------------------------
	def selectedNameFilter(self):
		"""
		Returns the filter that the user selected in the file dialog.
		"""
		res = super(QFileDialog,self).selectedNameFilter()
		return res
	#----------------------------------------------------------------------
	def sidebarUrls(self):
		"""
		Returns a list of urls that are currently in the sidebar
		"""
		res = super(QFileDialog,self).sidebarUrls()
		return res
	#----------------------------------------------------------------------
	def viewMode(self):
		"""
		This property holds the way files and directories are displayed in the dialog.
		By default, the Detail mode is used to display information about files and directories.
		"""
		res = super(QFileDialog,self).viewMode()
		isinstance(res,QtGui.QFileDialog.ViewMode)
		return res
	#----------------------------------------------------------------------
	def labelText(self,label):
		"""
		labelText(label)
			label=QtGui.QFileDialog.DialogLabel

		Returns the text shown in the filedialog in the specified label .
		"""
		res = super(QFileDialog,self).labelText(label)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		This function connects one of its signals to the slot specified by receiver and member
		The specific signal depends is PySide.QtGui.QFileDialog.filesSelected() if PySide.QtGui.QFileDialog.fileMode() is ExistingFiles and PySide.QtGui.QFileDialog.fileSelected() if PySide.QtGui.QFileDialog.fileMode() is anything else.
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QFileDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def restoreState(self,state):
		"""
		restoreState(state)
			state=QtCore.QByteArray

		Restores the dialogss layout, history and current directory to the state specified.
		Typically this is used in conjunction with PySide.QtCore.QSettings to restore the size from a past session.
		Returns false if there are errors
		"""
		res = super(QFileDialog,self).restoreState(state)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def selectFile(self,filename):
		"""
		selectFile(filename)
			filename=unicode

		Selects the given filename in the file dialog.
		"""
		res = super(QFileDialog,self).selectFile(filename)
		return res
	#----------------------------------------------------------------------
	def selectFilter(self,filter):
		"""
		selectFilter(filter)
			filter=unicode

		Use PySide.QtGui.QFileDialog.selectNameFilter() instead.
		"""
		res = super(QFileDialog,self).selectFilter(filter)
		return res
	#----------------------------------------------------------------------
	def selectNameFilter(self,filter):
		"""
		selectNameFilter(filter)
			filter=unicode

		Sets the current file type filter
		Multiple filters can be passed in filter by separating them with semicolons or spaces.
		"""
		res = super(QFileDialog,self).selectNameFilter(filter)
		return res
	#----------------------------------------------------------------------
	def setAcceptMode(self,mode):
		"""
		setAcceptMode(mode)
			mode=QtGui.QFileDialog.AcceptMode

		This property holds the accept mode of the dialog.
		The action mode defines whether the dialog is for opening or saving files.
		By default, this property is set to AcceptOpen .
		"""
		res = super(QFileDialog,self).setAcceptMode(mode)
		return res
	#----------------------------------------------------------------------
	def setConfirmOverwrite(self,enabled):
		"""
		setConfirmOverwrite(enabled)
			enabled=QtCore.bool

		This property holds whether the filedialog should ask before accepting a selected file, when the accept mode is AcceptSave .
		Use setOption( DontConfirmOverwrite , !*enabled* ) or !testOption( DontConfirmOverwrite ) instead.
		"""
		res = super(QFileDialog,self).setConfirmOverwrite(enabled)
		return res
	#----------------------------------------------------------------------
	def setDefaultSuffix(self,suffix):
		"""
		setDefaultSuffix(suffix)
			suffix=unicode

		This property holds suffix added to the filename if no other suffix was specified.
		This property specifies a string that will be added to the filename if it has no suffix already
		The suffix is typically used to indicate the file type (e.g
		txt indicates a text file).
		"""
		res = super(QFileDialog,self).setDefaultSuffix(suffix)
		return res
	#----------------------------------------------------------------------
	def setDirectory(self,*args,**kwargs):
		"""
		setDirectory(directory)
			directory=unicode

		setDirectory(directory)
			directory=QtCore.QDir

		Sets the file dialogs current directory .
		"""
		res = super(QFileDialog,self).setDirectory(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFileMode(self,mode):
		"""
		setFileMode(mode)
			mode=QtGui.QFileDialog.FileMode

		This property holds the file mode of the dialog.
		The file mode defines the number and type of items that the user is expected to select in the dialog.
		By default, this property is set to AnyFile .
		This function will set the labels for the FileName and Accept QFileDialog.DialogLabel s
		It is possible to set custom text after the call to PySide.QtGui.QFileDialog.setFileMode() .
		"""
		res = super(QFileDialog,self).setFileMode(mode)
		return res
	#----------------------------------------------------------------------
	def setFilter(self,*args,**kwargs):
		"""
		setFilter(filters)
			filters=QtCore.QDir.Filters

		setFilter(filter)
			filter=unicode


		"""
		res = super(QFileDialog,self).setFilter(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFilters(self,filters):
		"""
		setFilters(filters)
			filters=list

		Use PySide.QtGui.QFileDialog.setNameFilters() instead.
		"""
		res = super(QFileDialog,self).setFilters(filters)
		return res
	#----------------------------------------------------------------------
	def setHistory(self,paths):
		"""
		setHistory(paths)
			paths=list

		Sets the browsing history of the filedialog to contain the given paths .
		"""
		res = super(QFileDialog,self).setHistory(paths)
		return res
	#----------------------------------------------------------------------
	def setIconProvider(self,provider):
		"""
		setIconProvider(provider)
			provider=QtGui.QFileIconProvider

		Sets the icon provider used by the filedialog to the specified provider .
		"""
		res = super(QFileDialog,self).setIconProvider(provider)
		return res
	#----------------------------------------------------------------------
	def setItemDelegate(self,delegate):
		"""
		setItemDelegate(delegate)
			delegate=QtGui.QAbstractItemDelegate

		Sets the item delegate used to render items in the views in the file dialog to the given delegate .
		Note that the model used is PySide.QtGui.QFileSystemModel
		It has custom item data roles, which is described by the QFileSystemModel.Roles enum
		You can use a PySide.QtGui.QFileIconProvider if you only want custom icons.
		"""
		res = super(QFileDialog,self).setItemDelegate(delegate)
		return res
	#----------------------------------------------------------------------
	def setLabelText(self,label,text):
		"""
		setLabelText(label,text)
			label=QtGui.QFileDialog.DialogLabel
			text=unicode

		Sets the text shown in the filedialog in the specified label .
		"""
		res = super(QFileDialog,self).setLabelText(label,text)
		return res
	#----------------------------------------------------------------------
	def setNameFilter(self,filter):
		"""
		setNameFilter(filter)
			filter=unicode

		Sets the filter used in the file dialog to the given filter .
		If filter contains a pair of parentheses containing one or more of anything*something , separated by spaces, then only the text contained in the parentheses is used as the filter
		This means that these calls are all equivalent:
		"""
		res = super(QFileDialog,self).setNameFilter(filter)
		return res
	#----------------------------------------------------------------------
	def setNameFilterDetailsVisible(self,enabled):
		"""
		setNameFilterDetailsVisible(enabled)
			enabled=QtCore.bool


		"""
		res = super(QFileDialog,self).setNameFilterDetailsVisible(enabled)
		return res
	#----------------------------------------------------------------------
	def setNameFilters(self,filters):
		"""
		setNameFilters(filters)
			filters=list

		Sets the filters used in the file dialog.
		"""
		res = super(QFileDialog,self).setNameFilters(filters)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QFileDialog.Option
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QFileDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QFileDialog.Options


		"""
		res = super(QFileDialog,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def setProxyModel(self,model):
		"""
		setProxyModel(model)
			model=QtGui.QAbstractProxyModel

		Sets the model for the views to the given proxyModel
		This is useful if you want to modify the underlying model; for example, to add columns, filter data or add drives.
		Any existing proxy model will be removed, but not deleted
		The file dialog will take ownership of the proxyModel .
		"""
		res = super(QFileDialog,self).setProxyModel(model)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,enabled):
		"""
		setReadOnly(enabled)
			enabled=QtCore.bool

		This property holds Whether the filedialog is read-only.
		If this property is set to false, the file dialog will allow renaming, and deleting of files and directories and creating directories.
		Use setOption( ReadOnly , enabled ) or testOption( ReadOnly ) instead.
		"""
		res = super(QFileDialog,self).setReadOnly(enabled)
		return res
	#----------------------------------------------------------------------
	def setResolveSymlinks(self,enabled):
		"""
		setResolveSymlinks(enabled)
			enabled=QtCore.bool

		This property holds whether the filedialog should resolve shortcuts.
		If this property is set to true, the file dialog will resolve shortcuts or symbolic links.
		Use setOption( DontResolveSymlinks , !``enabled`` ) or !testOption( DontResolveSymlinks ).
		"""
		res = super(QFileDialog,self).setResolveSymlinks(enabled)
		return res
	#----------------------------------------------------------------------
	def setSidebarUrls(self,urls):
		"""
		setSidebarUrls(urls)
			urls=unKnown


		"""
		res = super(QFileDialog,self).setSidebarUrls(urls)
		return res
	#----------------------------------------------------------------------
	def setViewMode(self,mode):
		"""
		setViewMode(mode)
			mode=QtGui.QFileDialog.ViewMode

		This property holds the way files and directories are displayed in the dialog.
		By default, the Detail mode is used to display information about files and directories.
		"""
		res = super(QFileDialog,self).setViewMode(mode)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QFileDialog.Option

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QFileDialog,self).testOption(option)
		isinstance(res,QtCore.bool)
		return res
