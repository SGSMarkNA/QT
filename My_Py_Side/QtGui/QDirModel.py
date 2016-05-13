from PySide import QtGui, QtCore

class QDirModel(QtGui.QDirModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDirModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def filter(self):
		"""
		Returns the filter specification for the directory model.
		"""
		res = super(QDirModel,self).filter()
		isinstance(res,QtCore.QDir.Filters)
		return res
	#----------------------------------------------------------------------
	def iconProvider(self):
		"""
		Returns the file icon provider for this directory model.
		"""
		res = super(QDirModel,self).iconProvider()
		isinstance(res,QtGui.QFileIconProvider)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds Whether the directory model allows writing to the file system.
		If this property is set to false, the directory model will allow renaming, copying and deleting of files and directories.
		This property is true by default
		"""
		res = super(QDirModel,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lazyChildCount(self):
		"""
		This property holds Whether the directory model optimizes the hasChildren function to only check if the item is a directory..
		If this property is set to false, the directory model will make sure that a directory actually containes any files before reporting that it has children
		Otherwise the directory model will report that an item has children if the item is a directory.
		This property is false by default
		"""
		res = super(QDirModel,self).lazyChildCount()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def nameFilters(self):
		"""
		Returns a list of filters applied to the names in the model.
		"""
		res = super(QDirModel,self).nameFilters()
		return res
	#----------------------------------------------------------------------
	def resolveSymlinks(self):
		"""
		This property holds Whether the directory model should resolve symbolic links.
		This is only relevant on operating systems that support symbolic links.
		"""
		res = super(QDirModel,self).resolveSymlinks()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sorting(self):
		"""
		Returns the sorting method used for the directory model.
		"""
		res = super(QDirModel,self).sorting()
		isinstance(res,QtCore.QDir.SortFlags)
		return res
	#----------------------------------------------------------------------
	def fileIcon(self,index):
		"""
		fileIcon(index)
			index=QtCore.QModelIndex

		Returns the icons for the item stored in the model under the given index .
		"""
		res = super(QDirModel,self).fileIcon(index)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def fileInfo(self,index):
		"""
		fileInfo(index)
			index=QtCore.QModelIndex

		Returns the file information for the specified model index .
		"""
		res = super(QDirModel,self).fileInfo(index)
		isinstance(res,QtCore.QFileInfo)
		return res
	#----------------------------------------------------------------------
	def fileName(self,index):
		"""
		fileName(index)
			index=QtCore.QModelIndex

		Returns the name of the item stored in the model under the index given.
		"""
		res = super(QDirModel,self).fileName(index)
		return res
	#----------------------------------------------------------------------
	def filePath(self,index):
		"""
		filePath(index)
			index=QtCore.QModelIndex

		Returns the path of the item stored in the model under the index given.
		"""
		res = super(QDirModel,self).filePath(index)
		return res
	#----------------------------------------------------------------------
	def index(self,path,column=None):
		"""
		index(path,column=None)
			path=unicode
			column=QtCore.int

		This is an overloaded function.
		Returns the model item index for the given path .
		"""
		res = super(QDirModel,self).index(path,column)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def isDir(self,index):
		"""
		isDir(index)
			index=QtCore.QModelIndex

		Returns true if the model item index represents a directory; otherwise returns false.
		"""
		res = super(QDirModel,self).isDir(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def mkdir(self,parent,name):
		"""
		mkdir(parent,name)
			parent=QtCore.QModelIndex
			name=unicode

		Create a directory with the name in the parent model item.
		"""
		res = super(QDirModel,self).mkdir(parent,name)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def remove(self,index):
		"""
		remove(index)
			index=QtCore.QModelIndex

		Removes the model item index from the directory model and deletes the corresponding file from the file system , returning true if successful
		If the item cannot be removed, false is returned.
		"""
		res = super(QDirModel,self).remove(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rmdir(self,index):
		"""
		rmdir(index)
			index=QtCore.QModelIndex

		Removes the directory corresponding to the model item index in the directory model and deletes the corresponding directory from the file system , returning true if successful
		If the directory cannot be removed, false is returned.
		"""
		res = super(QDirModel,self).rmdir(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setFilter(self,filters):
		"""
		setFilter(filters)
			filters=QtCore.QDir.Filters


		"""
		res = super(QDirModel,self).setFilter(filters)
		return res
	#----------------------------------------------------------------------
	def setIconProvider(self,provider):
		"""
		setIconProvider(provider)
			provider=QtGui.QFileIconProvider

		Sets the provider of file icons for the directory model.
		"""
		res = super(QDirModel,self).setIconProvider(provider)
		return res
	#----------------------------------------------------------------------
	def setLazyChildCount(self,enable):
		"""
		setLazyChildCount(enable)
			enable=QtCore.bool

		This property holds Whether the directory model optimizes the hasChildren function to only check if the item is a directory..
		If this property is set to false, the directory model will make sure that a directory actually containes any files before reporting that it has children
		Otherwise the directory model will report that an item has children if the item is a directory.
		This property is false by default
		"""
		res = super(QDirModel,self).setLazyChildCount(enable)
		return res
	#----------------------------------------------------------------------
	def setNameFilters(self,filters):
		"""
		setNameFilters(filters)
			filters=list

		Sets the name filters for the directory model.
		"""
		res = super(QDirModel,self).setNameFilters(filters)
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
		res = super(QDirModel,self).setReadOnly(enable)
		return res
	#----------------------------------------------------------------------
	def setResolveSymlinks(self,enable):
		"""
		setResolveSymlinks(enable)
			enable=QtCore.bool

		This property holds Whether the directory model should resolve symbolic links.
		This is only relevant on operating systems that support symbolic links.
		"""
		res = super(QDirModel,self).setResolveSymlinks(enable)
		return res
	#----------------------------------------------------------------------
	def setSorting(self,sort):
		"""
		setSorting(sort)
			sort=QtCore.QDir.SortFlags


		"""
		res = super(QDirModel,self).setSorting(sort)
		return res
