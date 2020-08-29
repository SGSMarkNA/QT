from PySide import QtGui, QtCore

class QFileInfo(QtCore.QFileInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFileInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QFileInfo,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def absoluteDir(self):
		"""
		Returns the files absolute path as a PySide.QtCore.QDir object.
		"""
		res = super(QFileInfo,self).absoluteDir()
		isinstance(res,QtCore.QDir)
		return res
	#----------------------------------------------------------------------
	def absoluteFilePath(self):
		"""
		Returns an absolute path including the file name.
		The absolute path name consists of the full path and the file name
		On Unix this will always begin with the root, /, directory
		On Windows this will always begin D:/ where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin //sharename/
		PySide.QtCore.QFileInfo will uppercase drive letters
		Note that PySide.QtCore.QDir does not do this
		The code snippet below shows this.
		This function returns the same as PySide.QtCore.QFileInfo.filePath() , unless PySide.QtCore.QFileInfo.isRelative() is true
		In contrast to PySide.QtCore.QFileInfo.canonicalFilePath() , symbolic links or redundant
		or .
		elements are not necessarily removed.
		If the PySide.QtCore.QFileInfo is empty it returns QDir.currentPath() .
		"""
		res = super(QFileInfo,self).absoluteFilePath()
		return res
	#----------------------------------------------------------------------
	def absolutePath(self):
		"""
		Returns a files path absolute path
		This doesnt include the file name.
		On Unix the absolute path will always begin with the root, /, directory
		On Windows this will always begin D:/ where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin //sharename/.
		In contrast to PySide.QtCore.QFileInfo.canonicalPath() symbolic links or redundant
		or .
		elements are not necessarily removed.
		"""
		res = super(QFileInfo,self).absolutePath()
		return res
	#----------------------------------------------------------------------
	def baseName(self):
		"""
		Returns the base name of the file without the path.
		The base name consists of all characters in the file up to (but not including) the first
		character.
		Example:
		The base name of a file is computed equally on all platforms, independent of file naming conventions (e.g., .bashrc on Unix has an empty base name, and the suffix is bashrc).
		"""
		res = super(QFileInfo,self).baseName()
		return res
	#----------------------------------------------------------------------
	def bundleName(self):
		"""
		Returns the name of the bundle.
		On Mac OS X this returns the proper localized name for a bundle if the path PySide.QtCore.QFileInfo.isBundle()
		On all other platforms an empty PySide.QtCore.QString is returned.
		Example:
		"""
		res = super(QFileInfo,self).bundleName()
		return res
	#----------------------------------------------------------------------
	def caching(self):
		"""
		Returns true if caching is enabled; otherwise returns false.
		"""
		res = super(QFileInfo,self).caching()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canonicalFilePath(self):
		"""
		Returns the canonical path including the file name, i.e
		an absolute path without symbolic links or redundant
		or .
		elements.
		If the file does not exist, PySide.QtCore.QFileInfo.canonicalFilePath() returns an empty string.
		"""
		res = super(QFileInfo,self).canonicalFilePath()
		return res
	#----------------------------------------------------------------------
	def canonicalPath(self):
		"""
		Returns the files path canonical path (excluding the file name), i.e
		an absolute path without symbolic links or redundant
		or .
		elements.
		If the file does not exist, PySide.QtCore.QFileInfo.canonicalPath() returns an empty string.
		"""
		res = super(QFileInfo,self).canonicalPath()
		return res
	#----------------------------------------------------------------------
	def completeBaseName(self):
		"""
		Returns the complete base name of the file without the path.
		The complete base name consists of all characters in the file up to (but not including) the last
		character.
		Example:
		"""
		res = super(QFileInfo,self).completeBaseName()
		return res
	#----------------------------------------------------------------------
	def completeSuffix(self):
		"""
		Returns the complete suffix of the file.
		The complete suffix consists of all characters in the file after (but not including) the first ..
		Example:
		"""
		res = super(QFileInfo,self).completeSuffix()
		return res
	#----------------------------------------------------------------------
	def created(self):
		"""
		Returns the date and time when the file was created.
		On most Unix systems, this function returns the time of the last status change
		A status change occurs when the file is created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).
		If neither creation time nor last status change time are not available, returns the same as PySide.QtCore.QFileInfo.lastModified() .
		"""
		res = super(QFileInfo,self).created()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def dir(self):
		"""
		Returns the path of the objects parent directory as a PySide.QtCore.QDir object.
		For each of the following, PySide.QtCore.QFileInfo.dir() returns a PySide.QtCore.QDir for "~/examples/191697" .
		For each of the following, PySide.QtCore.QFileInfo.dir() returns a PySide.QtCore.QDir for "." .
		"""
		res = super(QFileInfo,self).dir()
		isinstance(res,QtCore.QDir)
		return res
	#----------------------------------------------------------------------
	def exists(self):
		"""
		Returns true if the file exists; otherwise returns false.
		"""
		res = super(QFileInfo,self).exists()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the name of the file, excluding the path.
		Example:
		Note that, if this PySide.QtCore.QFileInfo object is given a path ending in a slash, the name of the file is considered empty.
		"""
		res = super(QFileInfo,self).fileName()
		return res
	#----------------------------------------------------------------------
	def filePath(self):
		"""
		Returns the file name, including the path (which may be absolute or relative).
		"""
		res = super(QFileInfo,self).filePath()
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns the group of the file
		On Windows, on systems where files do not have groups, or if an error occurs, an empty string is returned.
		This function can be time consuming under Unix (in the order of milliseconds).
		"""
		res = super(QFileInfo,self).group()
		return res
	#----------------------------------------------------------------------
	def groupId(self):
		"""
		Returns the id of the group the file belongs to.
		On Windows and on systems where files do not have groups this function always returns (uint) -2.
		"""
		res = super(QFileInfo,self).groupId()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def isAbsolute(self):
		"""
		Returns true if the file path name is absolute, otherwise returns false if the path is relative.
		"""
		res = super(QFileInfo,self).isAbsolute()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isBundle(self):
		"""
		Returns true if this object points to a bundle or to a symbolic link to a bundle on Mac OS X; otherwise returns false.
		"""
		res = super(QFileInfo,self).isBundle()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDir(self):
		"""
		Returns true if this object points to a directory or to a symbolic link to a directory; otherwise returns false.
		"""
		res = super(QFileInfo,self).isDir()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isExecutable(self):
		"""
		Returns true if the file is executable; otherwise returns false.
		"""
		res = super(QFileInfo,self).isExecutable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFile(self):
		"""
		Returns true if this object points to a file or to a symbolic link to a file
		Returns false if the object points to something which isnt a file, such as a directory.
		"""
		res = super(QFileInfo,self).isFile()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if this is a `hidden file; otherwise returns false.
		"""
		res = super(QFileInfo,self).isHidden()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isReadable(self):
		"""
		Returns true if the user can read the file; otherwise returns false.
		"""
		res = super(QFileInfo,self).isReadable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isRelative(self):
		"""
		Returns true if the file path name is relative, otherwise returns false if the path is absolute (e.g
		under Unix a path is absolute if it begins with a /).
		"""
		res = super(QFileInfo,self).isRelative()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isRoot(self):
		"""
		Returns true if the object points to a directory or to a symbolic link to a directory, and that directory is the root directory; otherwise returns false.
		"""
		res = super(QFileInfo,self).isRoot()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSymLink(self):
		"""
		Returns true if this object points to a symbolic link (or to a shortcut on Windows); otherwise returns false.
		On Unix (including Mac OS X), opening a symlink effectively opens the link's target
		On Windows, it opens the .lnk file itself.
		Example:
		"""
		res = super(QFileInfo,self).isSymLink()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if the user can write to the file; otherwise returns false.
		"""
		res = super(QFileInfo,self).isWritable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastModified(self):
		"""
		Returns the date and time when the file was last modified.
		"""
		res = super(QFileInfo,self).lastModified()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def lastRead(self):
		"""
		Returns the date and time when the file was last read (accessed).
		On platforms where this information is not available, returns the same as PySide.QtCore.QFileInfo.lastModified() .
		"""
		res = super(QFileInfo,self).lastRead()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def makeAbsolute(self):
		"""
		Converts the files path to an absolute path if it is not already in that form
		Returns true to indicate that the path was converted; otherwise returns false to indicate that the path was already absolute.
		"""
		res = super(QFileInfo,self).makeAbsolute()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def owner(self):
		"""
		Returns the owner of the file
		On systems where files do not have owners, or if an error occurs, an empty string is returned.
		This function can be time consuming under Unix (in the order of milliseconds).
		"""
		res = super(QFileInfo,self).owner()
		return res
	#----------------------------------------------------------------------
	def ownerId(self):
		"""
		Returns the id of the owner of the file.
		On Windows and on systems where files do not have owners this function returns ((uint) -2).
		"""
		res = super(QFileInfo,self).ownerId()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the files path
		This doesnt include the file name.
		Note that, if this PySide.QtCore.QFileInfo object is given a path ending in a slash, the name of the file is considered empty and this function will return the entire path.
		"""
		res = super(QFileInfo,self).path()
		return res
	#----------------------------------------------------------------------
	def permissions(self):
		"""
		Returns the complete OR-ed together combination of QFile.Permissions for the file.
		"""
		res = super(QFileInfo,self).permissions()
		isinstance(res,QtCore.QFile.Permissions)
		return res
	#----------------------------------------------------------------------
	def readLink(self):
		"""
		Use PySide.QtCore.QFileInfo.symLinkTarget() instead.
		"""
		res = super(QFileInfo,self).readLink()
		return res
	#----------------------------------------------------------------------
	def refresh(self):
		"""
		Refreshes the information about the file, i.e
		reads in information from the file system the next time a cached property is fetched.
		"""
		res = super(QFileInfo,self).refresh()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the file size in bytes
		If the file does not exist or cannot be fetched, 0 is returned.
		"""
		res = super(QFileInfo,self).size()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def suffix(self):
		"""
		Returns the suffix of the file.
		The suffix consists of all characters in the file after (but not including) the last ..
		Example:
		The suffix of a file is computed equally on all platforms, independent of file naming conventions (e.g., .bashrc on Unix has an empty base name, and the suffix is bashrc).
		"""
		res = super(QFileInfo,self).suffix()
		return res
	#----------------------------------------------------------------------
	def symLinkTarget(self):
		"""
		Returns the absolute path to the file or directory a symlink (or shortcut on Windows) points to, or a an empty string if the object isnt a symbolic link.
		This name may not represent an existing file; it is only a string
		QFileInfo.exists() returns true if the symlink points to an existing file.
		"""
		res = super(QFileInfo,self).symLinkTarget()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,fileinfo):
		"""
		__ne__(fileinfo)
			fileinfo=QtCore.QFileInfo

		This is an overloaded function.
		"""
		res = super(QFileInfo,self).__ne__(fileinfo)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,fileinfo):
		"""
		__eq__(fileinfo)
			fileinfo=QtCore.QFileInfo

		This is an overloaded function.
		"""
		res = super(QFileInfo,self).__eq__(fileinfo)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def permission(self,permissions):
		"""
		permission(permissions)
			permissions=QtCore.QFile.Permissions


		"""
		res = super(QFileInfo,self).permission(permissions)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setCaching(self,on):
		"""
		setCaching(on)
			on=QtCore.bool

		If enable is true, enables caching of file information
		If enable is false caching is disabled.
		When caching is enabled, PySide.QtCore.QFileInfo reads the file information from the file system the first time its needed, but generally not later.
		Caching is enabled by default.
		"""
		res = super(QFileInfo,self).setCaching(on)
		return res
	#----------------------------------------------------------------------
	def setFile(self,*args,**kwargs):
		"""
		setFile(dir,file)
			dir=QtCore.QDir
			file=unicode

		setFile(file)
			file=QtCore.QFile

		setFile(file)
			file=unicode

		This is an overloaded function.
		Sets the file that the PySide.QtCore.QFileInfo provides information about to file in directory dir .
		If file includes a relative path, the PySide.QtCore.QFileInfo will also have a relative path.
		"""
		res = super(QFileInfo,self).setFile(*args,**kwargs)
		return res
