from PySide import QtGui, QtCore

class QReadLocker(QtCore.QReadLocker):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QReadLocker,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __enter__(self):
		"""

		"""
		res = super(QReadLocker,self).__enter__()
		return res
	#----------------------------------------------------------------------
	def readWriteLock(self):
		"""
		Returns a pointer to the read-write lock that was passed to the constructor.
		"""
		res = super(QReadLocker,self).readWriteLock()
		isinstance(res,QtCore.QReadWriteLock)
		return res
	#----------------------------------------------------------------------
	def relock(self):
		"""
		Relocks an unlocked lock.
		"""
		res = super(QReadLocker,self).relock()
		return res
	#----------------------------------------------------------------------
	def unlock(self):
		"""
		Unlocks the lock associated with this locker.
		"""
		res = super(QReadLocker,self).unlock()
		return res
	#----------------------------------------------------------------------
	def __exit__(self,arg__1,arg__2,arg__3):
		"""
		__exit__(arg__1,arg__2,arg__3)
			arg__1=Object
			arg__2=Object
			arg__3=Object


		"""
		res = super(QReadLocker,self).__exit__(arg__1,arg__2,arg__3)
		return res
