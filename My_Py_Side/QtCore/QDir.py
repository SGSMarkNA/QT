from PySide import QtGui, QtCore

class QDir(QtCore.QDir):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDir,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QDir,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def absolutePath(self):
		"""
		Returns the absolute path (a path that starts with / or with a drive specification), which may contain symbolic links, but never contains redundant ., .
		or multiple separators.
		"""
		res = super(QDir,self).absolutePath()
		return res
	#----------------------------------------------------------------------
	def canonicalPath(self):
		"""
		Returns the canonical path, i.e
		a path without symbolic links or redundant
		or .
		elements.
		On systems that do not have symbolic links this function will always return the same string that PySide.QtCore.QDir.absolutePath() returns
		If the canonical path does not exist (normally due to dangling symbolic links) PySide.QtCore.QDir.canonicalPath() returns an empty string.
		Example:
		"""
		res = super(QDir,self).canonicalPath()
		return res
	#----------------------------------------------------------------------
	def cdUp(self):
		"""
		Changes directory by moving one directory up from the PySide.QtCore.QDir s current directory.
		Returns true if the new directory exists and is readable; otherwise returns false
		Note that the logical PySide.QtCore.QDir.cdUp() operation is not performed if the new directory does not exist.
		"""
		res = super(QDir,self).cdUp()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the total number of directories and files in the directory.
		Equivalent to PySide.QtCore.QDir.entryList()
		PySide.QtCore.QDir.count() .
		"""
		res = super(QDir,self).count()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def dirName(self):
		"""
		Returns the name of the directory; this is not the same as the path, e.g
		a directory with the name mail, might have the path /var/spool/mail
		If the directory has no name (e.g
		it is the root directory) an empty string is returned.
		No check is made to ensure that a directory with this name actually exists; but see PySide.QtCore.QDir.exists() .
		"""
		res = super(QDir,self).dirName()
		return res
	#----------------------------------------------------------------------
	def exists(self):
		"""
		This is an overloaded function.
		Returns true if the directory exists; otherwise returns false
		(If a file with the same name is found this function will return false).
		The overload of this function that accepts an argument is used to test for the presence of files and directories within a directory.
		"""
		res = super(QDir,self).exists()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def filter(self):
		"""
		Returns the value set by PySide.QtCore.QDir.setFilter()
		"""
		res = super(QDir,self).filter()
		isinstance(res,QtCore.QDir.Filters)
		return res
	#----------------------------------------------------------------------
	def isAbsolute(self):
		"""
		Returns true if the directorys path is absolute; otherwise returns false
		See PySide.QtCore.QDir.isAbsolutePath() .
		"""
		res = super(QDir,self).isAbsolute()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadable(self):
		"""
		Returns true if the directory is readable and we can open files by name; otherwise returns false.
		"""
		res = super(QDir,self).isReadable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRelative(self):
		"""
		Returns true if the directory path is relative; otherwise returns false
		(Under Unix a path is relative if it does not start with a /).
		"""
		res = super(QDir,self).isRelative()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRoot(self):
		"""
		Returns true if the directory is the root directory; otherwise returns false.
		Note: If the directory is a symbolic link to the root directory this function returns false
		If you want to test for this use PySide.QtCore.QDir.canonicalPath() , e.g.
		"""
		res = super(QDir,self).isRoot()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def makeAbsolute(self):
		"""
		Converts the directory path to an absolute path
		If it is already absolute nothing happens
		Returns true if the conversion succeeded; otherwise returns false.
		"""
		res = super(QDir,self).makeAbsolute()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def nameFilters(self):
		"""
		Returns the string list set by PySide.QtCore.QDir.setNameFilters()
		"""
		res = super(QDir,self).nameFilters()
		return res
	#----------------------------------------------------------------------
	def PySide.QtCore.QDir.operator[](arg__1)(self):
		"""
		Returns the file name at position pos in the list of file names
		Equivalent to PySide.QtCore.QDir.entryList() .at(index)
		pos must be a valid index position in the list (i.e., 0 <= pos < PySide.QtCore.QDir.count() ).
		"""
		res = super(QDir,self).PySide.QtCore.QDir.operator[](arg__1)()
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the path
		This may contain symbolic links, but never contains redundant ., .
		or multiple separators.
		The returned path can be either absolute or relative (see PySide.QtCore.QDir.setPath() ).
		"""
		res = super(QDir,self).path()
		return res
	#----------------------------------------------------------------------
	def refresh(self):
		"""
		Refreshes the directory information.
		"""
		res = super(QDir,self).refresh()
		return res
	#----------------------------------------------------------------------
	def sorting(self):
		"""
		Returns the value set by PySide.QtCore.QDir.setSorting()
		"""
		res = super(QDir,self).sorting()
		isinstance(res,QtCore.QDir.SortFlags)
		return res
	#----------------------------------------------------------------------
	def absoluteFilePath(self,fileName):
		"""
		absoluteFilePath(fileName)
			fileName=unicode

		Returns the absolute path name of a file in the directory
		Does not check if the file actually exists in the directory; but see PySide.QtCore.QDir.exists()
		Redundant multiple separators or
		and .
		directories in fileName are not removed (see PySide.QtCore.QDir.cleanPath() ).
		"""
		res = super(QDir,self).absoluteFilePath(fileName)
		return res
	#----------------------------------------------------------------------
	def cd(self,dirName):
		"""
		cd(dirName)
			dirName=unicode

		Changes the PySide.QtCore.QDir s directory to dirName .
		Returns true if the new directory exists and is readable; otherwise returns false
		Note that the logical PySide.QtCore.QDir.cd() operation is not performed if the new directory does not exist.
		Calling cd(..) is equivalent to calling PySide.QtCore.QDir.cdUp() .
		"""
		res = super(QDir,self).cd(dirName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def entryInfoList(self,*args,**kwargs):
		"""
		entryInfoList(filters=None,sort=None)
			filters=QtCore.QDir.Filters
			sort=QtCore.QDir.SortFlags

		entryInfoList(nameFilters,filters=None,sort=None)
			nameFilters=list
			filters=QtCore.QDir.Filters
			sort=QtCore.QDir.SortFlags


		"""
		res = super(QDir,self).entryInfoList(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def entryList(self,*args,**kwargs):
		"""
		entryList(nameFilters,filters=None,sort=None)
			nameFilters=list
			filters=QtCore.QDir.Filters
			sort=QtCore.QDir.SortFlags

		entryList(filters=None,sort=None)
			filters=QtCore.QDir.Filters
			sort=QtCore.QDir.SortFlags


		"""
		res = super(QDir,self).entryList(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def exists(self,name):
		"""
		exists(name)
			name=unicode

		Returns true if the file called name exists; otherwise returns false.
		Unless name contains an absolute file path, the file name is assumed to be relative to the directory itself, so this function is typically used to check for the presence of files within a directory.
		"""
		res = super(QDir,self).exists(name)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def filePath(self,fileName):
		"""
		filePath(fileName)
			fileName=unicode

		Returns the path name of a file in the directory
		Does not check if the file actually exists in the directory; but see PySide.QtCore.QDir.exists()
		If the PySide.QtCore.QDir is relative the returned path name will also be relative
		Redundant multiple separators or
		and .
		directories in fileName are not removed (see PySide.QtCore.QDir.cleanPath() ).
		"""
		res = super(QDir,self).filePath(fileName)
		return res
	#----------------------------------------------------------------------
	def mkdir(self,dirName):
		"""
		mkdir(dirName)
			dirName=unicode

		Creates a sub-directory called dirName .
		Returns true on success; otherwise returns false.
		"""
		res = super(QDir,self).mkdir(dirName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def mkpath(self,dirPath):
		"""
		mkpath(dirPath)
			dirPath=unicode

		Creates the directory path dirPath .
		The function will create all parent directories necessary to create the directory.
		Returns true if successful; otherwise returns false.
		"""
		res = super(QDir,self).mkpath(dirPath)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,dir):
		"""
		__ne__(dir)
			dir=QtCore.QDir

		Returns true if directory dir and this directory have different paths or different sort or filter settings; otherwise returns false.
		Example:
		"""
		res = super(QDir,self).__ne__(dir)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,dir):
		"""
		__eq__(dir)
			dir=QtCore.QDir

		Returns true if directory dir and this directory have the same path and their sort and filter settings are the same; otherwise returns false.
		Example:
		"""
		res = super(QDir,self).__eq__(dir)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def relativeFilePath(self,fileName):
		"""
		relativeFilePath(fileName)
			fileName=unicode

		Returns the path to fileName relative to the directory.
		"""
		res = super(QDir,self).relativeFilePath(fileName)
		return res
	#----------------------------------------------------------------------
	def remove(self,fileName):
		"""
		remove(fileName)
			fileName=unicode

		Removes the file, fileName .
		Returns true if the file is removed successfully; otherwise returns false.
		"""
		res = super(QDir,self).remove(fileName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rename(self,oldName,newName):
		"""
		rename(oldName,newName)
			oldName=unicode
			newName=unicode

		Renames a file or directory from oldName to newName , and returns true if successful; otherwise returns false.
		On most file systems, PySide.QtCore.QDir.rename() fails only if oldName does not exist, if newName and oldName are not on the same partition or if a file with the new name already exists
		However, there are also other reasons why PySide.QtCore.QDir.rename() can fail
		For example, on at least one file system PySide.QtCore.QDir.rename() fails if newName points to an open file.
		"""
		res = super(QDir,self).rename(oldName,newName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rmdir(self,dirName):
		"""
		rmdir(dirName)
			dirName=unicode

		Removes the directory specified by dirName .
		The directory must be empty for PySide.QtCore.QDir.rmdir() to succeed.
		Returns true if successful; otherwise returns false.
		"""
		res = super(QDir,self).rmdir(dirName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rmpath(self,dirPath):
		"""
		rmpath(dirPath)
			dirPath=unicode

		Removes the directory path dirPath .
		The function will remove all parent directories in dirPath , provided that they are empty
		This is the opposite of mkpath(dirPath).
		Returns true if successful; otherwise returns false.
		"""
		res = super(QDir,self).rmpath(dirPath)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setFilter(self,filter):
		"""
		setFilter(filter)
			filter=QtCore.QDir.Filters


		"""
		res = super(QDir,self).setFilter(filter)
		return res
	#----------------------------------------------------------------------
	def setNameFilters(self,nameFilters):
		"""
		setNameFilters(nameFilters)
			nameFilters=list

		Sets the name filters used by PySide.QtCore.QDir.entryList() and PySide.QtCore.QDir.entryInfoList() to the list of filters specified by nameFilters .
		Each name filter is a wildcard (globbing) filter that understands * and ? wildcards
		(See QRegExp wildcard matching .)
		For example, the following code sets three name filters on a PySide.QtCore.QDir to ensure that only files with extensions typically used for C++ source files are listed:
		"""
		res = super(QDir,self).setNameFilters(nameFilters)
		return res
	#----------------------------------------------------------------------
	def setPath(self,path):
		"""
		setPath(path)
			path=unicode

		Sets the path of the directory to path
		The path is cleaned of redundant ., .
		and of multiple separators
		No check is made to see whether a directory with this path actually exists; but you can check for yourself using PySide.QtCore.QDir.exists() .
		The path can be either absolute or relative
		Absolute paths begin with the directory separator / (optionally preceded by a drive specification under Windows)
		Relative file names begin with a directory name or a file name and specify a path relative to the current directory
		An example of an absolute path is the string /tmp/quartz, a relative path might look like src/fatlib.
		"""
		res = super(QDir,self).setPath(path)
		return res
	#----------------------------------------------------------------------
	def setSorting(self,sort):
		"""
		setSorting(sort)
			sort=QtCore.QDir.SortFlags


		"""
		res = super(QDir,self).setSorting(sort)
		return res
