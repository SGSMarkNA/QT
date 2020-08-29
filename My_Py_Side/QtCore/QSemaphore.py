from PySide import QtGui, QtCore

class QSemaphore(QtCore.QSemaphore):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSemaphore,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def available(self):
		"""
		Returns the number of resources currently available to the semaphore
		This number can never be negative.
		"""
		res = super(QSemaphore,self).available()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def acquire(self,n=None):
		"""
		acquire(n=None)
			n=QtCore.int

		Tries to acquire n resources guarded by the semaphore
		If n > PySide.QtCore.QSemaphore.available() , this call will block until enough resources are available.
		"""
		res = super(QSemaphore,self).acquire(n)
		return res
	#----------------------------------------------------------------------
	def release(self,n=None):
		"""
		release(n=None)
			n=QtCore.int

		Releases n resources guarded by the semaphore.
		This function can be used to create resources as well
		For example:
		"""
		res = super(QSemaphore,self).release(n)
		return res
	#----------------------------------------------------------------------
	def tryAcquire(self,*args,**kwargs):
		"""
		tryAcquire(n=None)
			n=QtCore.int

		tryAcquire(n,timeout)
			n=QtCore.int
			timeout=QtCore.int

		Tries to acquire n resources guarded by the semaphore and returns true on success
		If PySide.QtCore.QSemaphore.available() < n , this call immediately returns false without acquiring any resources.
		Example:
		"""
		res = super(QSemaphore,self).tryAcquire(*args,**kwargs)
		isinstance(res,bool)
		return res
