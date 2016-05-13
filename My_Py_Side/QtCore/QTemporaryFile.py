from PySide import QtGui, QtCore

class QTemporaryFile(QtCore.QTemporaryFile):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTemporaryFile,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoRemove(self):
		"""
		Returns true if the PySide.QtCore.QTemporaryFile is in auto remove mode
		Auto-remove mode will automatically delete the filename from disk upon destruction
		This makes it very easy to create your PySide.QtCore.QTemporaryFile object on the stack, fill it with data, read from it, and finally on function return it will automatically clean up after itself.
		Auto-remove is on by default.
		"""
		res = super(QTemporaryFile,self).autoRemove()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fileTemplate(self):
		"""
		Returns the set file template
		The default file template will be called qt_temp and be placed in QDir.tempPath() .
		"""
		res = super(QTemporaryFile,self).fileTemplate()
		return res
	#----------------------------------------------------------------------
	def open(self):
		"""
		A PySide.QtCore.QTemporaryFile will always be opened in QIODevice.ReadWrite mode, this allows easy access to the data in the file
		This function will return true upon success and will set the PySide.QtCore.QTemporaryFile.fileName() to the unique filename used.
		"""
		res = super(QTemporaryFile,self).open()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAutoRemove(self,b):
		"""
		setAutoRemove(b)
			b=QtCore.bool

		Sets the PySide.QtCore.QTemporaryFile into auto-remove mode if b is true.
		Auto-remove is on by default.
		"""
		res = super(QTemporaryFile,self).setAutoRemove(b)
		return res
	#----------------------------------------------------------------------
	def setFileTemplate(self,name):
		"""
		setFileTemplate(name)
			name=unicode

		Sets the static portion of the file name to name
		If the file template ends in XXXXXX that will automatically be replaced with the unique part of the filename, otherwise a filename will be determined automatically based on the static portion specified.
		If name contains a relative file path, the path will be relative to the current working directory
		You can use QDir.tempPath() to construct name if you want use the systems temporary directory.
		"""
		res = super(QTemporaryFile,self).setFileTemplate(name)
		return res
