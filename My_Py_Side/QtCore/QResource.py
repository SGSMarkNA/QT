from PySide import QtGui, QtCore

class QResource(QtCore.QResource):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QResource,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def absoluteFilePath(self):
		"""
		Returns the real path that this PySide.QtCore.QResource represents, if the resource was found via the PySide.QtCore.QResource.searchPaths() it will be indicated in the path.
		"""
		res = super(QResource,self).absoluteFilePath()
		return res
	#----------------------------------------------------------------------
	def children(self):
		"""
		Returns a list of all resources in this directory, if the resource represents a file the list will be empty.
		"""
		res = super(QResource,self).children()
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns a read only buffer object pointing to the segment of data that this resource represents
		If the resource is compressed the data returns is compressed and qUncompress() must be used to access the data
		If the resource is a directory None is returned.
		"""
		res = super(QResource,self).data()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the full path to the file that this PySide.QtCore.QResource represents as it was passed.
		"""
		res = super(QResource,self).fileName()
		return res
	#----------------------------------------------------------------------
	def isCompressed(self):
		"""
		Returns true if the resource represents a file and the data backing it is in a compressed format, false otherwise.
		"""
		res = super(QResource,self).isCompressed()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDir(self):
		"""
		Returns true if the resource represents a directory and thus may have PySide.QtCore.QResource.children() in it, false if it represents a file.
		"""
		res = super(QResource,self).isDir()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFile(self):
		"""
		Returns true if the resource represents a file and thus has data backing it, false if it represents a directory.
		"""
		res = super(QResource,self).isFile()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the resource really exists in the resource hierarchy, false otherwise.
		"""
		res = super(QResource,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def locale(self):
		"""
		Returns the locale used to locate the data for the PySide.QtCore.QResource .
		"""
		res = super(QResource,self).locale()
		isinstance(res,QtCore.QLocale)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the data backing the resource.
		"""
		res = super(QResource,self).size()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,file):
		"""
		setFileName(file)
			file=unicode

		Sets a PySide.QtCore.QResource to point to file
		file can either be absolute, in which case it is opened directly, if relative then the file will be tried to be found in PySide.QtCore.QResource.searchPaths() .
		"""
		res = super(QResource,self).setFileName(file)
		return res
	#----------------------------------------------------------------------
	def setLocale(self,locale):
		"""
		setLocale(locale)
			locale=QtCore.QLocale

		Sets a PySide.QtCore.QResource to only load the localization of resource to for locale
		If a resource for the specific locale is not found then the C locale is used.
		"""
		res = super(QResource,self).setLocale(locale)
		return res
