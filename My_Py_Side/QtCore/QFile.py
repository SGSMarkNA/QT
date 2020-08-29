from PySide import QtGui, QtCore

class QFile(QtCore.QFile):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFile,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the file error status.
		The I/O device status returns an error code
		For example, if PySide.QtCore.QFile.open() returns false, or a read/write operation returns -1, this function can be called to find out the reason why the operation failed.
		"""
		res = super(QFile,self).error()
		isinstance(res,QtCore.QFile.FileError)
		return res
	#----------------------------------------------------------------------
	def exists(self):
		"""
		This is an overloaded function.
		Returns true if the file specified by PySide.QtCore.QFile.fileName() exists; otherwise returns false.
		"""
		res = super(QFile,self).exists()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fileEngine(self):
		"""
		Returns the QIOEngine for this PySide.QtCore.QFile object.
		"""
		res = super(QFile,self).fileEngine()
		isinstance(res,QtCore.QAbstractFileEngine)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the name set by PySide.QtCore.QFile.setFileName() or to the PySide.QtCore.QFile constructors.
		"""
		res = super(QFile,self).fileName()
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		Flushes any buffered data to the file
		Returns true if successful; otherwise returns false.
		"""
		res = super(QFile,self).flush()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the file handle of the file.
		This is a small positive integer, suitable for use with C library functions such as fdopen() and fcntl()
		On systems that use file descriptors for sockets (i.e
		Unix systems, but not Windows) the handle can be used with PySide.QtCore.QSocketNotifier as well.
		If the file is not open, or there is an error, PySide.QtCore.QFile.handle() returns -1.
		This function is not supported on Windows CE.
		"""
		res = super(QFile,self).handle()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def permissions(self):
		"""
		Returns the complete OR-ed together combination of QFile.Permission for the file.
		"""
		res = super(QFile,self).permissions()
		isinstance(res,QtCore.QFile.Permissions)
		return res
	#----------------------------------------------------------------------
	def readLink(self):
		"""
		Use PySide.QtCore.QFile.symLinkTarget() instead.
		"""
		res = super(QFile,self).readLink()
		return res
	#----------------------------------------------------------------------
	def remove(self):
		"""
		Removes the file specified by PySide.QtCore.QFile.fileName()
		Returns true if successful; otherwise returns false.
		The file is closed before it is removed.
		"""
		res = super(QFile,self).remove()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def symLinkTarget(self):
		"""
		This is an overloaded function.
		Returns the absolute path of the file or directory a symlink (or shortcut on Windows) points to, or a an empty string if the object isnt a symbolic link.
		This name may not represent an existing file; it is only a string
		QFile.exists() returns true if the symlink points to an existing file.
		"""
		res = super(QFile,self).symLinkTarget()
		return res
	#----------------------------------------------------------------------
	def unsetError(self):
		"""
		Sets the files error to QFile.NoError .
		"""
		res = super(QFile,self).unsetError()
		return res
	#----------------------------------------------------------------------
	def copy(self,newName):
		"""
		copy(newName)
			newName=unicode

		Copies the file currently specified by PySide.QtCore.QFile.fileName() to a file called newName
		Returns true if successful; otherwise returns false.
		Note that if a file with the name newName already exists, PySide.QtCore.QFile.copy() returns false (i.e
		PySide.QtCore.QFile will not overwrite it).
		The source file is closed before it is copied.
		"""
		res = super(QFile,self).copy(newName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def link(self,newName):
		"""
		link(newName)
			newName=unicode

		Creates a link named linkName that points to the file currently specified by PySide.QtCore.QFile.fileName()
		What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix)
		Returns true if successful; otherwise returns false.
		This function will not overwrite an already existing entity in the file system; in this case, link() will return false and set PySide.QtCore.QFile.error() to return RenameError .
		"""
		res = super(QFile,self).link(newName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def map(self,offset,size,flags=None):
		"""
		map(offset,size,flags=None)
			offset=QtCore.qint64
			size=QtCore.qint64
			flags=QtCore.QFile.MemoryMapFlags

		Maps size bytes of the file into memory starting at offset
		A file should be open for a map to succeed but the file does not need to stay open after the memory has been mapped
		When the PySide.QtCore.QFile is destroyed or a new file is opened with this object, any maps that have not been unmapped will automatically be unmapped.
		Any mapping options can be passed through flags .
		Returns a pointer to the memory or 0 if there is an error.
		"""
		res = super(QFile,self).map(offset,size,flags)
		isinstance(res,QtCore.uchar)
		return res
	#----------------------------------------------------------------------
	def open(self,fd,flags):
		"""
		open(fd,flags)
			fd=QtCore.int
			flags=QtCore.QIODevice.OpenMode


		"""
		res = super(QFile,self).open(fd,flags)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def rename(self,newName):
		"""
		rename(newName)
			newName=unicode

		Renames the file currently specified by PySide.QtCore.QFile.fileName() to newName
		Returns true if successful; otherwise returns false.
		If a file with the name newName already exists, PySide.QtCore.QFile.rename() returns false (i.e., PySide.QtCore.QFile will not overwrite it).
		The file is closed before it is renamed.
		"""
		res = super(QFile,self).rename(newName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def resize(self,sz):
		"""
		resize(sz)
			sz=QtCore.qint64

		Sets the file size (in bytes) sz
		Returns true if the file if the resize succeeds; false otherwise
		If sz is larger than the file currently is the new bytes will be set to 0, if sz is smaller the file is simply truncated.
		"""
		res = super(QFile,self).resize(sz)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,name):
		"""
		setFileName(name)
			name=unicode

		Sets the name of the file
		The name can have no path, a relative path, or an absolute path.
		Do not call this function if the file has already been opened.
		If the file name has no path or a relative path, the path used will be the applications current directory path at the time of the :meth:`PySide.QtCore.QFile.open` * call.
		Example:
		Note that the directory separator / works for all operating systems supported by Qt.
		"""
		res = super(QFile,self).setFileName(name)
		return res
	#----------------------------------------------------------------------
	def setPermissions(self,permissionSpec):
		"""
		setPermissions(permissionSpec)
			permissionSpec=QtCore.QFile.Permissions


		"""
		res = super(QFile,self).setPermissions(permissionSpec)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def unmap(self,address):
		"""
		unmap(address)
			address=QtCore.uchar

		Unmaps the memory address .
		Returns true if the unmap succeeds; false otherwise.
		"""
		res = super(QFile,self).unmap(address)
		isinstance(res,bool)
		return res
