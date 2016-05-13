from PySide import QtGui, QtCore

class QPixmapCache(QtGui.QPixmapCache):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPixmapCache,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __ne__(self,key):
		"""
		__ne__(key)
			key=QtGui.QPixmapCache::Key


		"""
		res = super(QPixmapCache,self).__ne__(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,key):
		"""
		__eq__(key)
			key=QtGui.QPixmapCache::Key

		Returns true if this key is the same as the given key ; otherwise returns false.
		"""
		res = super(QPixmapCache,self).__eq__(key)
		isinstance(res,QtCore.bool)
		return res
