from PySide import QtGui, QtCore

class QWaitCondition(QtCore.QWaitCondition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWaitCondition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def wakeAll(self):
		"""
		Wakes all threads waiting on the wait condition
		The order in which the threads are woken up depends on the operating systems scheduling policies and cannot be controlled or predicted.
		"""
		res = super(QWaitCondition,self).wakeAll()
		return res
	#----------------------------------------------------------------------
	def wakeOne(self):
		"""
		Wakes one thread waiting on the wait condition
		The thread that is woken up depends on the operating systems scheduling policies, and cannot be controlled or predicted.
		If you want to wake up a specific thread, the solution is typically to use different wait conditions and have different threads wait on different conditions.
		"""
		res = super(QWaitCondition,self).wakeOne()
		return res
	#----------------------------------------------------------------------
	def wait(self,*args,**kwargs):
		"""
		wait(readWriteLock,time=None)
			readWriteLock=QtCore.QReadWriteLock
			time=long

		wait(mutex,time=None)
			mutex=QtCore.QMutex
			time=long

		Releases the locked readWriteLock and waits on the wait condition
		The readWriteLock must be initially locked by the calling thread
		If readWriteLock is not in a locked state, this function returns immediately
		The readWriteLock must not be locked recursively, otherwise this function will not release the lock properly
		The readWriteLock will be unlocked, and the calling thread will block until either of these conditions is met:
		The readWriteLock will be returned to the same locked state
		This function is provided to allow the atomic transition from the locked state to the wait state.
		"""
		res = super(QWaitCondition,self).wait(*args,**kwargs)
		isinstance(res,bool)
		return res
