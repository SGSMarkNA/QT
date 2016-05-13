from PySide import QtGui, QtCore

class QAbstractFileEngineIterator(QtCore.QAbstractFileEngineIterator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractFileEngineIterator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentFileInfo(self):
		"""
		The virtual function returns a PySide.QtCore.QFileInfo for the current directory entry
		This function is provided for convenience
		It can also be slightly faster than creating a PySide.QtCore.QFileInfo object yourself, as the object returned by this function might contain cached information that PySide.QtCore.QFileInfo otherwise would have to access through the file engine.
		"""
		res = super(QAbstractFileEngineIterator,self).currentFileInfo()
		isinstance(res,QtCore.QFileInfo)
		return res
	#----------------------------------------------------------------------
	def currentFileName(self):
		"""
		This pure virtual function returns the name of the current directory entry, excluding the path.
		"""
		res = super(QAbstractFileEngineIterator,self).currentFileName()
		return res
	#----------------------------------------------------------------------
	def currentFilePath(self):
		"""
		Returns the path to the current directory entry
		Its the same as prepending PySide.QtCore.QAbstractFileEngineIterator.path() to the return value of PySide.QtCore.QAbstractFileEngineIterator.currentFileName() .
		"""
		res = super(QAbstractFileEngineIterator,self).currentFilePath()
		return res
	#----------------------------------------------------------------------
	def filters(self):
		"""
		Returns the entry filters for this iterator.
		"""
		res = super(QAbstractFileEngineIterator,self).filters()
		isinstance(res,QtCore.QDir.Filters)
		return res
	#----------------------------------------------------------------------
	def hasNext(self):
		"""
		This pure virtual function returns true if there is at least one more entry in the current directory (i.e., the iterator path is valid and accessible, and the iterator has not reached the end of the entry list).
		"""
		res = super(QAbstractFileEngineIterator,self).hasNext()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def nameFilters(self):
		"""
		Returns the name filters for this iterator.
		"""
		res = super(QAbstractFileEngineIterator,self).nameFilters()
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		This pure virtual function advances the iterator to the next directory entry, and returns the file path to the current entry.
		This function can optionally make use of PySide.QtCore.QAbstractFileEngineIterator.nameFilters() and PySide.QtCore.QAbstractFileEngineIterator.filters() to optimize its performance.
		Reimplement this function in a subclass to advance the iterator.
		"""
		res = super(QAbstractFileEngineIterator,self).next()
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the path for this iterator
		PySide.QtCore.QDirIterator is responsible for assigning this path; it cannot change during the iterators lifetime.
		"""
		res = super(QAbstractFileEngineIterator,self).path()
		return res
	#----------------------------------------------------------------------
	def setPath(self,path):
		"""
		setPath(path)
			path=unicode


		"""
		res = super(QAbstractFileEngineIterator,self).setPath(path)
		return res
