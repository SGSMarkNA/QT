from PySide import QtGui, QtCore

class QFileSystemModel(QtGui.QFileSystemModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFileSystemModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def filter(self):
		"""
		Returns the filter specified for the directory model.
		If a filter has not been set, the default filter is QDir.AllEntries | QDir.NoDotAndDotDot | QDir.AllDirs .
		"""
		res = super(QFileSystemModel,self).filter()
		isinstance(res,QtCore.QDir.Filters)
		return res
	#----------------------------------------------------------------------
	def iconProvider(self):
		"""
		Returns the file icon provider for this directory model.
		"""
		res = super(QFileSystemModel,self).iconProvider()
		isinstance(res,QtGui.QFileIconProvider)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds Whether the directory model allows writing to the file system.
		If this property is set to false, the directory model will allow renaming, copying and deleting of files and directories.
		This property is true by default
		"""
		res = super(QFileSystemModel,self).isReadOnly()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def nameFilterDisables(self):
		"""
		This property holds Whether files that dont pass the name filter are hidden or disabled.
		This property is true by default
		"""
		res = super(QFileSystemModel,self).nameFilterDisables()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def nameFilters(self):
		"""
		Returns a list of filters applied to the names in the model.
		"""
		res = super(QFileSystemModel,self).nameFilters()
		return res
	#----------------------------------------------------------------------
	def resolveSymlinks(self):
		"""
		This property holds Whether the directory model should resolve symbolic links.
		This is only relevant on operating systems that support symbolic links.
		By default, this property is false.
		"""
		res = super(QFileSystemModel,self).resolveSymlinks()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rootDirectory(self):
		"""
		The currently set directory
		"""
		res = super(QFileSystemModel,self).rootDirectory()
		isinstance(res,QtCore.QDir)
		return res
	#----------------------------------------------------------------------
	def rootPath(self):
		"""
		The currently set root path
		"""
		res = super(QFileSystemModel,self).rootPath()
		return res
	#----------------------------------------------------------------------
	def fileIcon(self,index):
		"""
		fileIcon(index)
			index=QtCore.QModelIndex

		Returns the icon for the item stored in the model under the given index .
		"""
		res = super(QFileSystemModel,self).fileIcon(index)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def fileInfo(self,index):
		"""
		fileInfo(index)
			index=QtCore.QModelIndex

		Returns the PySide.QtCore.QFileInfo for the item stored in the model under the given index .
		"""
		res = super(QFileSystemModel,self).fileInfo(index)
		isinstance(res,QtCore.QFileInfo)
		return res
	#----------------------------------------------------------------------
	def fileName(self,index):
		"""
		fileName(index)
			index=QtCore.QModelIndex

		Returns the file name for the item stored in the model under the given index .
		"""
		res = super(QFileSystemModel,self).fileName(index)
		return res
	#----------------------------------------------------------------------
	def filePath(self,index):
		"""
		filePath(index)
			index=QtCore.QModelIndex

		Returns the path of the item stored in the model under the index given.
		"""
		res = super(QFileSystemModel,self).filePath(index)
		return res
	#----------------------------------------------------------------------
	def isDir(self,index):
		"""
		isDir(index)
			index=QtCore.QModelIndex

		Returns true if the model item index represents a directory; otherwise returns false.
		"""
		res = super(QFileSystemModel,self).isDir(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastModified(self,index):
		"""
		lastModified(index)
			index=QtCore.QModelIndex

		Returns the date and time when index was last modified.
		"""
		res = super(QFileSystemModel,self).lastModified(index)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def mkdir(self,parent,name):
		"""
		mkdir(parent,name)
			parent=QtCore.QModelIndex
			name=unicode

		Create a directory with the name in the parent model index.
		"""
		res = super(QFileSystemModel,self).mkdir(parent,name)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def myComputer(self,role=None):
		"""
		myComputer(role=None)
			role=QtCore.int

		Returns the data stored under the given role for the item My Computer.
		"""
		res = super(QFileSystemModel,self).myComputer(role)
		return res
	#----------------------------------------------------------------------
	def permissions(self,index):
		"""
		permissions(index)
			index=QtCore.QModelIndex

		Returns the complete OR-ed together combination of QFile.Permission for the index .
		"""
		res = super(QFileSystemModel,self).permissions(index)
		isinstance(res,QtCore.QFile.Permissions)
		return res
	#----------------------------------------------------------------------
	def remove(self,index):
		"""
		remove(index)
			index=QtCore.QModelIndex

		Removes the model item index from the file system model and deletes the corresponding file from the file system , returning true if successful
		If the item cannot be removed, false is returned.
		"""
		res = super(QFileSystemModel,self).remove(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rmdir(self,index):
		"""
		rmdir(index)
			index=QtCore.QModelIndex

		Removes the directory corresponding to the model item index in the file system model and deletes the corresponding directory from the file system , returning true if successful
		If the directory cannot be removed, false is returned.
		"""
		res = super(QFileSystemModel,self).rmdir(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setFilter(self,filters):
		"""
		setFilter(filters)
			filters=QtCore.QDir.Filters


		"""
		res = super(QFileSystemModel,self).setFilter(filters)
		return res
	#----------------------------------------------------------------------
	def setIconProvider(self,provider):
		"""
		setIconProvider(provider)
			provider=QtGui.QFileIconProvider

		Sets the provider of file icons for the directory model.
		"""
		res = super(QFileSystemModel,self).setIconProvider(provider)
		return res
	#----------------------------------------------------------------------
	def setNameFilterDisables(self,enable):
		"""
		setNameFilterDisables(enable)
			enable=QtCore.bool

		This property holds Whether files that dont pass the name filter are hidden or disabled.
		This property is true by default
		"""
		res = super(QFileSystemModel,self).setNameFilterDisables(enable)
		return res
	#----------------------------------------------------------------------
	def setNameFilters(self,filters):
		"""
		setNameFilters(filters)
			filters=list

		Sets the name filters to apply against the existing files.
		"""
		res = super(QFileSystemModel,self).setNameFilters(filters)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,enable):
		"""
		setReadOnly(enable)
			enable=QtCore.bool

		This property holds Whether the directory model allows writing to the file system.
		If this property is set to false, the directory model will allow renaming, copying and deleting of files and directories.
		This property is true by default
		"""
		res = super(QFileSystemModel,self).setReadOnly(enable)
		return res
	#----------------------------------------------------------------------
	def setResolveSymlinks(self,enable):
		"""
		setResolveSymlinks(enable)
			enable=QtCore.bool

		This property holds Whether the directory model should resolve symbolic links.
		This is only relevant on operating systems that support symbolic links.
		By default, this property is false.
		"""
		res = super(QFileSystemModel,self).setResolveSymlinks(enable)
		return res
	#----------------------------------------------------------------------
	def setRootPath(self,path):
		"""
		setRootPath(path)
			path=unicode

		Sets the directory that is being watched by the model to newPath by installing a file system watcher on it
		Any changes to files and directories within this directory will be reflected in the model.
		If the path is changed, the PySide.QtGui.QFileSystemModel.rootPathChanged() signal will be emitted.
		"""
		res = super(QFileSystemModel,self).setRootPath(path)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def size(self,index):
		"""
		size(index)
			index=QtCore.QModelIndex

		Returns the size in bytes of index
		If the file does not exist, 0 is returned.
		"""
		res = super(QFileSystemModel,self).size(index)
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def type(self,index):
		"""
		type(index)
			index=QtCore.QModelIndex

		Returns the type of file index such as Directory or JPEG file.
		"""
		res = super(QFileSystemModel,self).type(index)
		return res
