from PySide import QtGui, QtCore

class QFSFileEngine(QtCore.QFSFileEngine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFSFileEngine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def endEntryList(self):
		"""

		"""
		res = super(QFSFileEngine,self).endEntryList()
		isinstance(res,QtCore.QAbstractFileEngineIterator)
		return res
	#----------------------------------------------------------------------
	def open(self,flags,fd):
		"""
		open(flags,fd)
			flags=QtCore.QIODevice.OpenMode
			fd=QtCore.int


		"""
		res = super(QFSFileEngine,self).open(flags,fd)
		isinstance(res,bool)
		return res
