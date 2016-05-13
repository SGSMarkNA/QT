from PySide import QtGui, QtCore

class QReadWriteLock(QtCore.QReadWriteLock):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QReadWriteLock,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def lockForRead(self):
		"""
		Locks the lock for reading
		This function will block the current thread if any thread (including the current) has locked for writing.
		"""
		res = super(QReadWriteLock,self).lockForRead()
		return res
	#----------------------------------------------------------------------
	def lockForWrite(self):
		"""
		Locks the lock for writing
		This function will block the current thread if another thread has locked for reading or writing.
		"""
		res = super(QReadWriteLock,self).lockForWrite()
		return res
	#----------------------------------------------------------------------
	def tryLockForRead(self):
		"""
		Attempts to lock for reading
		If the lock was obtained, this function returns true, otherwise it returns false instead of waiting for the lock to become available, i.e
		it does not block.
		The lock attempt will fail if another thread has locked for writing.
		If the lock was obtained, the lock must be unlocked with PySide.QtCore.QReadWriteLock.unlock() before another thread can successfully lock it.
		"""
		res = super(QReadWriteLock,self).tryLockForRead()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def tryLockForWrite(self):
		"""
		Attempts to lock for writing
		If the lock was obtained, this function returns true; otherwise, it returns false immediately.
		The lock attempt will fail if another thread has locked for reading or writing.
		If the lock was obtained, the lock must be unlocked with PySide.QtCore.QReadWriteLock.unlock() before another thread can successfully lock it.
		"""
		res = super(QReadWriteLock,self).tryLockForWrite()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def unlock(self):
		"""
		Unlocks the lock.
		Attempting to unlock a lock that is not locked is an error, and will result in program termination.
		"""
		res = super(QReadWriteLock,self).unlock()
		return res
	#----------------------------------------------------------------------
	def tryLockForRead(self,timeout):
		"""
		tryLockForRead(timeout)
			timeout=QtCore.int

		This is an overloaded function.
		Attempts to lock for reading
		This function returns true if the lock was obtained; otherwise it returns false
		If another thread has locked for writing, this function will wait for at most timeout milliseconds for the lock to become available.
		Note: Passing a negative number as the timeout is equivalent to calling PySide.QtCore.QReadWriteLock.lockForRead() , i.e
		this function will wait forever until lock can be locked for reading when timeout is negative.
		If the lock was obtained, the lock must be unlocked with PySide.QtCore.QReadWriteLock.unlock() before another thread can successfully lock it.
		"""
		res = super(QReadWriteLock,self).tryLockForRead(timeout)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def tryLockForWrite(self,timeout):
		"""
		tryLockForWrite(timeout)
			timeout=QtCore.int

		This is an overloaded function.
		Attempts to lock for writing
		This function returns true if the lock was obtained; otherwise it returns false
		If another thread has locked for reading or writing, this function will wait for at most timeout milliseconds for the lock to become available.
		Note: Passing a negative number as the timeout is equivalent to calling PySide.QtCore.QReadWriteLock.lockForWrite() , i.e
		this function will wait forever until lock can be locked for writing when timeout is negative.
		If the lock was obtained, the lock must be unlocked with PySide.QtCore.QReadWriteLock.unlock() before another thread can successfully lock it.
		"""
		res = super(QReadWriteLock,self).tryLockForWrite(timeout)
		isinstance(res,QtCore.bool)
		return res
