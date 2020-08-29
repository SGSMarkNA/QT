from PySide import QtGui, QtCore

class QUrlInfo(QtNetwork.QUrlInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUrlInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns the group of the URL.
		"""
		res = super(QUrlInfo,self).group()
		return res
	#----------------------------------------------------------------------
	def isDir(self):
		"""
		Returns true if the URL is a directory; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isDir()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isExecutable(self):
		"""
		Returns true if the URL is executable; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isExecutable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFile(self):
		"""
		Returns true if the URL is a file; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isFile()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isReadable(self):
		"""
		Returns true if the URL is readable; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isReadable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSymLink(self):
		"""
		Returns true if the URL is a symbolic link; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isSymLink()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the URL info is valid; otherwise returns false
		Valid means that the PySide.QtNetwork.QUrlInfo contains real information.
		You should always check if the URL info is valid before relying on the values.
		"""
		res = super(QUrlInfo,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if the URL is writable; otherwise returns false.
		"""
		res = super(QUrlInfo,self).isWritable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastModified(self):
		"""
		Returns the last modification date of the URL.
		"""
		res = super(QUrlInfo,self).lastModified()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def lastRead(self):
		"""
		Returns the date when the URL was last read.
		"""
		res = super(QUrlInfo,self).lastRead()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the file name of the URL.
		"""
		res = super(QUrlInfo,self).name()
		return res
	#----------------------------------------------------------------------
	def owner(self):
		"""
		Returns the owner of the URL.
		"""
		res = super(QUrlInfo,self).owner()
		return res
	#----------------------------------------------------------------------
	def permissions(self):
		"""
		Returns the permissions of the URL
		You can use the PermissionSpec flags to test for certain permissions.
		"""
		res = super(QUrlInfo,self).permissions()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the URL.
		"""
		res = super(QUrlInfo,self).size()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,i):
		"""
		__ne__(i)
			i=QtNetwork.QUrlInfo

		Returns true if this PySide.QtNetwork.QUrlInfo is not equal to other ; otherwise returns false.
		"""
		res = super(QUrlInfo,self).__ne__(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,i):
		"""
		__eq__(i)
			i=QtNetwork.QUrlInfo

		Returns true if this PySide.QtNetwork.QUrlInfo is equal to other ; otherwise returns false.
		"""
		res = super(QUrlInfo,self).__eq__(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setDir(self,b):
		"""
		setDir(b)
			b=QtCore.bool

		If b is true then the URL is set to be a directory; if b is false then the URL is set not to be a directory (which normally means it is a file)
		(Note that a URL can refer to both a file and a directory even though most file systems do not support this.)
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setDir(b)
		return res
	#----------------------------------------------------------------------
	def setFile(self,b):
		"""
		setFile(b)
			b=QtCore.bool

		If b is true then the URL is set to be a file; if b is false then the URL is set not to be a file (which normally means it is a directory)
		(Note that a URL can refer to both a file and a directory even though most file systems do not support this.)
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setFile(b)
		return res
	#----------------------------------------------------------------------
	def setGroup(self,s):
		"""
		setGroup(s)
			s=unicode

		Specifies that the owning group of the URL is called s .
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setGroup(s)
		return res
	#----------------------------------------------------------------------
	def setLastModified(self,dt):
		"""
		setLastModified(dt)
			dt=QtCore.QDateTime

		Specifies that the object the URL refers to was last modified at dt .
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setLastModified(dt)
		return res
	#----------------------------------------------------------------------
	def setLastRead(self,dt):
		"""
		setLastRead(dt)
			dt=QtCore.QDateTime

		Specifies that the object the URL refers to was last read at dt .
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setLastRead(dt)
		return res
	#----------------------------------------------------------------------
	def setName(self,name):
		"""
		setName(name)
			name=unicode

		Sets the name of the URL to name
		The name is the full text, for example, http://qt.nokia.com/doc/qurlinfo.html.
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setName(name)
		return res
	#----------------------------------------------------------------------
	def setOwner(self,s):
		"""
		setOwner(s)
			s=unicode

		Specifies that the owner of the URL is called s .
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setOwner(s)
		return res
	#----------------------------------------------------------------------
	def setPermissions(self,p):
		"""
		setPermissions(p)
			p=QtCore.int

		Specifies that the URL has access permissions p .
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setPermissions(p)
		return res
	#----------------------------------------------------------------------
	def setReadable(self,b):
		"""
		setReadable(b)
			b=QtCore.bool

		Specifies that the URL is readable if b is true and not readable if b is false.
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setReadable(b)
		return res
	#----------------------------------------------------------------------
	def setSize(self,size):
		"""
		setSize(size)
			size=QtCore.qint64

		Specifies the size of the URL.
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setSize(size)
		return res
	#----------------------------------------------------------------------
	def setSymLink(self,b):
		"""
		setSymLink(b)
			b=QtCore.bool

		Specifies that the URL refers to a symbolic link if b is true and that it does not if b is false.
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setSymLink(b)
		return res
	#----------------------------------------------------------------------
	def setWritable(self,b):
		"""
		setWritable(b)
			b=QtCore.bool

		Specifies that the URL is writable if b is true and not writable if b is false.
		If you call this function for an invalid URL info, this function turns it into a valid one.
		"""
		res = super(QUrlInfo,self).setWritable(b)
		return res
