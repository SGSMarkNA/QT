from PySide import QtGui, QtCore

class QSystemSemaphore(QtCore.QSystemSemaphore):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSystemSemaphore,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acquire(self):
		"""
		Acquires one of the resources guarded by this semaphore, if there is one available, and returns true
		If all the resources guarded by this semaphore have already been acquired, the call blocks until one of them is released by another process or thread having a semaphore with the same key.
		If false is returned, a system error has occurred
		Call PySide.QtCore.QSystemSemaphore.error() to get a value of QSystemSemaphore.SystemSemaphoreError that indicates which error occurred.
		"""
		res = super(QSystemSemaphore,self).acquire()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns a value indicating whether an error occurred, and, if so, which error it was.
		"""
		res = super(QSystemSemaphore,self).error()
		isinstance(res,QtCore.QSystemSemaphore.SystemSemaphoreError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a text description of the last error that occurred
		If PySide.QtCore.QSystemSemaphore.error() returns an error value , call this function to get a text string that describes the error.
		"""
		res = super(QSystemSemaphore,self).errorString()
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		Returns the key assigned to this system semaphore
		The key is the name by which the semaphore can be accessed from other processes.
		"""
		res = super(QSystemSemaphore,self).key()
		return res
	#----------------------------------------------------------------------
	def release(self,n=None):
		"""
		release(n=None)
			n=QtCore.int

		Releases n resources guarded by the semaphore
		Returns true unless there is a system error.
		Example: Create a system semaphore having five resources; acquire them all and then release them all.
		This function can also create resources
		For example, immediately following the sequence of statements above, suppose we add the statement:
		Ten new resources are now guarded by the semaphore, in addition to the five that already existed
		You would not normally use this function to create more resources.
		"""
		res = super(QSystemSemaphore,self).release(n)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setKey(self,key,initialValue=None,mode=None):
		"""
		setKey(key,initialValue=None,mode=None)
			key=unicode
			initialValue=QtCore.int
			mode=QtCore.QSystemSemaphore.AccessMode

		This function works the same as the constructor
		It reconstructs this PySide.QtCore.QSystemSemaphore object
		If the new key is different from the old key, calling this function is like calling the destructor of the semaphore with the old key, then calling the constructor to create a new semaphore with the new key
		The initialValue and mode parameters are as defined for the constructor.
		"""
		res = super(QSystemSemaphore,self).setKey(key,initialValue,mode)
		return res
