from PySide import QtGui, QtCore

class QMutexLocker(QtCore.QMutexLocker):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMutexLocker,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __enter__(self):
		"""

		"""
		res = super(QMutexLocker,self).__enter__()
		return res
	#----------------------------------------------------------------------
	def mutex(self):
		"""
		Returns a pointer to the mutex that was locked in the constructor.
		"""
		res = super(QMutexLocker,self).mutex()
		isinstance(res,QtCore.QMutex)
		return res
	#----------------------------------------------------------------------
	def relock(self):
		"""
		Relocks an unlocked mutex locker.
		"""
		res = super(QMutexLocker,self).relock()
		return res
	#----------------------------------------------------------------------
	def unlock(self):
		"""
		Unlocks this mutex locker
		You can use relock() to lock it again
		It does not need to be locked when destroyed.
		"""
		res = super(QMutexLocker,self).unlock()
		return res
	#----------------------------------------------------------------------
	def __exit__(self,arg__1,arg__2,arg__3):
		"""
		__exit__(arg__1,arg__2,arg__3)
			arg__1=Object
			arg__2=Object
			arg__3=Object


		"""
		res = super(QMutexLocker,self).__exit__(arg__1,arg__2,arg__3)
		return res
