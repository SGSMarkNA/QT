from PySide import QtGui, QtCore

class QDirIterator(QtCore.QDirIterator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDirIterator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fileInfo(self):
		"""
		Returns a PySide.QtCore.QFileInfo for the current directory entry.
		"""
		res = super(QDirIterator,self).fileInfo()
		isinstance(res,QtCore.QFileInfo)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the file name for the current directory entry, without the path prepended.
		This function is convenient when iterating a single directory
		When using the QDirIterator.Subdirectories flag, you can use PySide.QtCore.QDirIterator.filePath() to get the full path.
		"""
		res = super(QDirIterator,self).fileName()
		return res
	#----------------------------------------------------------------------
	def filePath(self):
		"""
		Returns the full file path for the current directory entry.
		"""
		res = super(QDirIterator,self).filePath()
		return res
	#----------------------------------------------------------------------
	def hasNext(self):
		"""
		Returns true if there is at least one more entry in the directory; otherwise, false is returned.
		"""
		res = super(QDirIterator,self).hasNext()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		Advances the iterator to the next entry, and returns the file path of this new entry
		If PySide.QtCore.QDirIterator.hasNext() returns false, this function does nothing, and returns a null PySide.QtCore.QString .
		You can call PySide.QtCore.QDirIterator.fileName() or PySide.QtCore.QDirIterator.filePath() to get the current entry file name or path, or PySide.QtCore.QDirIterator.fileInfo() to get a PySide.QtCore.QFileInfo for the current entry.
		"""
		res = super(QDirIterator,self).next()
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the base directory of the iterator.
		"""
		res = super(QDirIterator,self).path()
		return res
