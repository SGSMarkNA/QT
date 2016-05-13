from PySide import QtGui, QtCore

class QAbstractFileEngine(QtCore.QAbstractFileEngine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractFileEngine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the current position is at the end of the file; otherwise, returns false.
		This function bases its behavior on calling extension() with AtEndExtension
		If the engine does not support this extension, false is returned.
		"""
		res = super(QAbstractFileEngine,self).atEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def caseSensitive(self):
		"""
		Should return true if the underlying file system is case-sensitive; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).caseSensitive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def close(self):
		"""
		Closes the file, returning true if successful; otherwise returns false.
		The default implementation always returns false.
		"""
		res = super(QAbstractFileEngine,self).close()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the QFile.FileError that resulted from the last failed operation
		If QFile.UnspecifiedError is returned, PySide.QtCore.QFile will use its own idea of the error status.
		"""
		res = super(QAbstractFileEngine,self).error()
		isinstance(res,QtCore.QFile.FileError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns the human-readable message appropriate to the current error reported by PySide.QtCore.QAbstractFileEngine.error()
		If no suitable string is available, an empty string is returned.
		"""
		res = super(QAbstractFileEngine,self).errorString()
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		Flushes the open file, returning true if successful; otherwise returns false.
		The default implementation always returns false.
		"""
		res = super(QAbstractFileEngine,self).flush()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the native file handle for this file engine
		This handle must be used with care; its value and type are platform specific, and using it will most likely lead to non-portable code.
		"""
		res = super(QAbstractFileEngine,self).handle()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isRelativePath(self):
		"""
		Return true if the file referred to by this file engine has a relative path; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).isRelativePath()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSequential(self):
		"""
		Returns true if the file is a sequential access device; returns false if the file is a direct access device.
		Operations involving PySide.QtCore.QAbstractFileEngine.size() and seek(int) are not valid on sequential devices.
		"""
		res = super(QAbstractFileEngine,self).isSequential()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the current file position.
		This is the position of the data read/write head of the file.
		"""
		res = super(QAbstractFileEngine,self).pos()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def remove(self):
		"""
		Requests that the file is deleted from the file system
		If the operation succeeds return true; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).remove()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the file.
		"""
		res = super(QAbstractFileEngine,self).size()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def beginEntryList(self,filters,filterNames):
		"""
		beginEntryList(filters,filterNames)
			filters=QtCore.QDir.Filters
			filterNames=list


		"""
		res = super(QAbstractFileEngine,self).beginEntryList(filters,filterNames)
		isinstance(res,QtCore.QAbstractFileEngineIterator)
		return res
	#----------------------------------------------------------------------
	def copy(self,newName):
		"""
		copy(newName)
			newName=unicode

		Copies the contents of this file to a file with the name newName
		Returns true on success; otherwise, false is returned.
		"""
		res = super(QAbstractFileEngine,self).copy(newName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def entryList(self,filters,filterNames):
		"""
		entryList(filters,filterNames)
			filters=QtCore.QDir.Filters
			filterNames=list


		"""
		res = super(QAbstractFileEngine,self).entryList(filters,filterNames)
		return res
	#----------------------------------------------------------------------
	def fileFlags(self,type=None):
		"""
		fileFlags(type=None)
			type=QtCore.QAbstractFileEngine.FileFlags


		"""
		res = super(QAbstractFileEngine,self).fileFlags(type)
		isinstance(res,QtCore.QAbstractFileEngine.FileFlags)
		return res
	#----------------------------------------------------------------------
	def fileName(self,file=None):
		"""
		fileName(file=None)
			file=QtCore.QAbstractFileEngine.FileName

		Return the file engines current file name in the format specified by file .
		If you dont handle some FileName possibilities, return the file name set in PySide.QtCore.QAbstractFileEngine.setFileName() when an unhandled format is requested.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).fileName(file)
		return res
	#----------------------------------------------------------------------
	def fileTime(self,time):
		"""
		fileTime(time)
			time=QtCore.QAbstractFileEngine.FileTime

		If time is CreationTime , return when the file was created
		If time is ModificationTime , return when the file was most recently modified
		If time is AccessTime , return when the file was most recently accessed (e.g
		read or written)
		If the time cannot be determined return QDateTime() (an invalid date time).
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).fileTime(time)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def link(self,newName):
		"""
		link(newName)
			newName=unicode

		Creates a link from the file currently specified by PySide.QtCore.QAbstractFileEngine.fileName() to newName
		What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix)
		Returns true if successful; otherwise returns false.
		"""
		res = super(QAbstractFileEngine,self).link(newName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def map(self,offset,size,flags):
		"""
		map(offset,size,flags)
			offset=QtCore.qint64
			size=QtCore.qint64
			flags=QtCore.QFile.MemoryMapFlags


		"""
		res = super(QAbstractFileEngine,self).map(offset,size,flags)
		isinstance(res,QtCore.uchar)
		return res
	#----------------------------------------------------------------------
	def mkdir(self,dirName,createParentDirectories):
		"""
		mkdir(dirName,createParentDirectories)
			dirName=unicode
			createParentDirectories=QtCore.bool

		Requests that the directory dirName be created
		If createParentDirectories is true, then any sub-directories in dirName that dont exist must be created
		If createParentDirectories is false then any sub-directories in dirName must already exist for the function to succeed
		If the operation succeeds return true; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).mkdir(dirName,createParentDirectories)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def open(self,openMode):
		"""
		open(openMode)
			openMode=QtCore.QIODevice.OpenMode


		"""
		res = super(QAbstractFileEngine,self).open(openMode)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def owner(self,arg__1):
		"""
		owner(arg__1)
			arg__1=QtCore.QAbstractFileEngine.FileOwner

		If owner is OwnerUser return the name of the user who owns the file
		If owner is OwnerGroup return the name of the group that own the file
		If you cant determine the owner return QString() .
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).owner(arg__1)
		return res
	#----------------------------------------------------------------------
	def ownerId(self,arg__1):
		"""
		ownerId(arg__1)
			arg__1=QtCore.QAbstractFileEngine.FileOwner

		If owner is OwnerUser return the ID of the user who owns the file
		If owner is OwnerGroup return the ID of the group that own the file
		If you cant determine the owner return -2.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).ownerId(arg__1)
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def read(self,maxlen):
		"""
		read(maxlen)
			maxlen=QtCore.qint64

		Reads a number of characters from the file into data
		At most maxlen characters will be read.
		Returns -1 if a fatal error occurs, or 0 if there are no bytes to read.
		"""
		res = super(QAbstractFileEngine,self).read(maxlen)
		return res
	#----------------------------------------------------------------------
	def readLine(self,maxlen):
		"""
		readLine(maxlen)
			maxlen=QtCore.qint64

		This function reads one line, terminated by a n character, from the file info data
		At most maxlen characters will be read
		The end-of-line character is included.
		"""
		res = super(QAbstractFileEngine,self).readLine(maxlen)
		return res
	#----------------------------------------------------------------------
	def rename(self,newName):
		"""
		rename(newName)
			newName=unicode

		Requests that the file be renamed to newName in the file system
		If the operation succeeds return true; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).rename(newName)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rmdir(self,dirName,recurseParentDirectories):
		"""
		rmdir(dirName,recurseParentDirectories)
			dirName=unicode
			recurseParentDirectories=QtCore.bool

		Requests that the directory dirName is deleted from the file system
		When recurseParentDirectories is true, then any empty parent-directories in dirName must also be deleted
		If recurseParentDirectories is false, only the dirName leaf-node should be deleted
		In most file systems a directory cannot be deleted using this function if it is non-empty
		If the operation succeeds return true; otherwise return false.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).rmdir(dirName,recurseParentDirectories)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def seek(self,pos):
		"""
		seek(pos)
			pos=QtCore.qint64

		Sets the file position to the given offset
		Returns true if the position was successfully set; otherwise returns false.
		The offset is from the beginning of the file, unless the file is sequential.
		"""
		res = super(QAbstractFileEngine,self).seek(pos)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setError(self,error,str):
		"""
		setError(error,str)
			error=QtCore.QFile.FileError
			str=unicode


		"""
		res = super(QAbstractFileEngine,self).setError(error,str)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,file):
		"""
		setFileName(file)
			file=unicode

		Sets the file engines file name to file
		This file name is the file that the rest of the virtual functions will operate on.
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).setFileName(file)
		return res
	#----------------------------------------------------------------------
	def setPermissions(self,perms):
		"""
		setPermissions(perms)
			perms=QtCore.uint

		Requests that the files permissions be set to perms
		The argument perms will be set to the OR-ed together combination of QAbstractFileEngine::FileInfo, with only the QAbstractFileEngine.PermsMask being honored
		If the operations succceeds return true; otherwise return false;
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).setPermissions(perms)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setSize(self,size):
		"""
		setSize(size)
			size=QtCore.qint64

		Requests that the file be set to size size
		If size is larger than the current file then it is filled with 0s, if smaller it is simply truncated
		If the operations succceeds return true; otherwise return false;
		This virtual function must be reimplemented by all subclasses.
		"""
		res = super(QAbstractFileEngine,self).setSize(size)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def supportsExtension(self,extension):
		"""
		supportsExtension(extension)
			extension=QtCore.QAbstractFileEngine.Extension

		This virtual function returns true if the file engine supports extension ; otherwise, false is returned
		By default, no extensions are supported.
		"""
		res = super(QAbstractFileEngine,self).supportsExtension(extension)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def unmap(self,ptr):
		"""
		unmap(ptr)
			ptr=QtCore.uchar

		Unmaps the memory address
		Returns true if the unmap succeeds; otherwise returns false.
		This function bases its behavior on calling extension() with UnMapExtensionOption
		If the engine does not support this extension, false is returned.
		"""
		res = super(QAbstractFileEngine,self).unmap(ptr)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def write(self,data,len):
		"""
		write(data,len)
			data=str
			len=QtCore.qint64

		Writes len bytes from data to the file
		Returns the number of characters written on success; otherwise returns -1.
		"""
		res = super(QAbstractFileEngine,self).write(data,len)
		isinstance(res,QtCore.qint64)
		return res
