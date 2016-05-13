from PySide import QtGui, QtCore

class QFileSystemWatcher(QtCore.QFileSystemWatcher):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFileSystemWatcher,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def directories(self):
		"""
		Returns a list of paths to directories that are being watched.
		"""
		res = super(QFileSystemWatcher,self).directories()
		return res
	#----------------------------------------------------------------------
	def files(self):
		"""
		Returns a list of paths to files that are being watched.
		"""
		res = super(QFileSystemWatcher,self).files()
		return res
	#----------------------------------------------------------------------
	def addPath(self,file):
		"""
		addPath(file)
			file=unicode

		Adds path to the file system watcher if path exists
		The path is not added if it does not exist, or if it is already being monitored by the file system watcher.
		If path specifies a directory, the PySide.QtCore.QFileSystemWatcher.directoryChanged() signal will be emitted when path is modified or removed from disk; otherwise the PySide.QtCore.QFileSystemWatcher.fileChanged() signal is emitted when path is modified, renamed or removed.
		"""
		res = super(QFileSystemWatcher,self).addPath(file)
		return res
	#----------------------------------------------------------------------
	def addPaths(self,files):
		"""
		addPaths(files)
			files=list

		Adds each path in paths to the file system watcher
		Paths are not added if they not exist, or if they are already being monitored by the file system watcher.
		If a path specifies a directory, the PySide.QtCore.QFileSystemWatcher.directoryChanged() signal will be emitted when the path is modified or removed from disk; otherwise the PySide.QtCore.QFileSystemWatcher.fileChanged() signal is emitted when the path is modified, renamed, or removed.
		"""
		res = super(QFileSystemWatcher,self).addPaths(files)
		return res
	#----------------------------------------------------------------------
	def removePath(self,file):
		"""
		removePath(file)
			file=unicode

		Removes the specified path from the file system watcher.
		"""
		res = super(QFileSystemWatcher,self).removePath(file)
		return res
	#----------------------------------------------------------------------
	def removePaths(self,files):
		"""
		removePaths(files)
			files=list

		Removes the specified paths from the file system watcher.
		"""
		res = super(QFileSystemWatcher,self).removePaths(files)
		return res
