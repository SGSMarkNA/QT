from PySide import QtGui, QtCore

class QMutex(QtCore.QMutex):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMutex,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def lock(self):
		"""
		Locks the mutex
		If another thread has locked the mutex then this call will block until that thread has unlocked it.
		Calling this function multiple times on the same mutex from the same thread is allowed if this mutex is a recursive mutex
		If this mutex is a non-recursive mutex , this function will dead-lock when the mutex is locked recursively.
		"""
		res = super(QMutex,self).lock()
		return res
	#----------------------------------------------------------------------
	def tryLock(self):
		"""
		Attempts to lock the mutex
		If the lock was obtained, this function returns true
		If another thread has locked the mutex, this function returns false immediately.
		If the lock was obtained, the mutex must be unlocked with PySide.QtCore.QMutex.unlock() before another thread can successfully lock it.
		Calling this function multiple times on the same mutex from the same thread is allowed if this mutex is a recursive mutex
		If this mutex is a non-recursive mutex , this function will always return false when attempting to lock the mutex recursively.
		"""
		res = super(QMutex,self).tryLock()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def unlock(self):
		"""
		Unlocks the mutex
		Attempting to unlock a mutex in a different thread to the one that locked it results in an error
		Unlocking a mutex that is not locked results in undefined behavior.
		"""
		res = super(QMutex,self).unlock()
		return res
	#----------------------------------------------------------------------
	def tryLock(self,timeout):
		"""
		tryLock(timeout)
			timeout=QtCore.int

		This is an overloaded function.
		Attempts to lock the mutex
		This function returns true if the lock was obtained; otherwise it returns false
		If another thread has locked the mutex, this function will wait for at most timeout milliseconds for the mutex to become available.
		Note: Passing a negative number as the timeout is equivalent to calling PySide.QtCore.QMutex.lock() , i.e
		this function will wait forever until mutex can be locked if timeout is negative.
		If the lock was obtained, the mutex must be unlocked with PySide.QtCore.QMutex.unlock() before another thread can successfully lock it.
		Calling this function multiple times on the same mutex from the same thread is allowed if this mutex is a recursive mutex
		If this mutex is a non-recursive mutex , this function will always return false when attempting to lock the mutex recursively.
		"""
		res = super(QMutex,self).tryLock(timeout)
		isinstance(res,QtCore.bool)
		return res
