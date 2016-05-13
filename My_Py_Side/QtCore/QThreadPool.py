from PySide import QtGui, QtCore

class QThreadPool(QtCore.QThreadPool):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QThreadPool,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeThreadCount(self):
		"""
		This property represents the number of active threads in the thread pool.
		"""
		res = super(QThreadPool,self).activeThreadCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def expiryTimeout(self):
		"""
		Threads that are unused for expiryTimeout milliseconds are considered to have expired and will exit
		Such threads will be restarted as needed
		The default expiryTimeout is 30000 milliseconds (30 seconds)
		If expiryTimeout is negative, newly created threads will not expire, e.g., they will not exit until the thread pool is destroyed.
		Note that setting expiryTimeout has no effect on already running threads
		Only newly created threads will use the new expiryTimeout
		We recommend setting the expiryTimeout immediately after creating the thread pool, but before calling PySide.QtCore.QThreadPool.start() .
		"""
		res = super(QThreadPool,self).expiryTimeout()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maxThreadCount(self):
		"""
		This property represents the maximum number of threads used by the thread pool.
		The default maxThreadCount is QThread.idealThreadCount() .
		"""
		res = super(QThreadPool,self).maxThreadCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def releaseThread(self):
		"""
		Releases a thread previously reserved by a call to PySide.QtCore.QThreadPool.reserveThread() .
		"""
		res = super(QThreadPool,self).releaseThread()
		return res
	#----------------------------------------------------------------------
	def reserveThread(self):
		"""
		Reserves one thread, disregarding PySide.QtCore.QThreadPool.activeThreadCount() and PySide.QtCore.QThreadPool.maxThreadCount() .
		Once you are done with the thread, call PySide.QtCore.QThreadPool.releaseThread() to allow it to be reused.
		"""
		res = super(QThreadPool,self).reserveThread()
		return res
	#----------------------------------------------------------------------
	def waitForDone(self):
		"""
		Waits for each thread to exit and removes all threads from the thread pool.
		"""
		res = super(QThreadPool,self).waitForDone()
		return res
	#----------------------------------------------------------------------
	def setExpiryTimeout(self,expiryTimeout):
		"""
		setExpiryTimeout(expiryTimeout)
			expiryTimeout=QtCore.int

		Threads that are unused for expiryTimeout milliseconds are considered to have expired and will exit
		Such threads will be restarted as needed
		The default expiryTimeout is 30000 milliseconds (30 seconds)
		If expiryTimeout is negative, newly created threads will not expire, e.g., they will not exit until the thread pool is destroyed.
		Note that setting expiryTimeout has no effect on already running threads
		Only newly created threads will use the new expiryTimeout
		We recommend setting the expiryTimeout immediately after creating the thread pool, but before calling PySide.QtCore.QThreadPool.start() .
		"""
		res = super(QThreadPool,self).setExpiryTimeout(expiryTimeout)
		return res
	#----------------------------------------------------------------------
	def setMaxThreadCount(self,maxThreadCount):
		"""
		setMaxThreadCount(maxThreadCount)
			maxThreadCount=QtCore.int

		This property represents the maximum number of threads used by the thread pool.
		The default maxThreadCount is QThread.idealThreadCount() .
		"""
		res = super(QThreadPool,self).setMaxThreadCount(maxThreadCount)
		return res
	#----------------------------------------------------------------------
	def start(self,runnable,priority=None):
		"""
		start(runnable,priority=None)
			runnable=QtCore.QRunnable
			priority=QtCore.int

		Reserves a thread and uses it to run runnable , unless this thread will make the current thread count exceed PySide.QtCore.QThreadPool.maxThreadCount()
		In that case, runnable is added to a run queue instead
		The priority argument can be used to control the run queues order of execution.
		Note that the thread pool takes ownership of the runnable if runnable->autoDelete() returns true, and the runnable will be deleted automatically by the thread pool after the runnable->run() returns
		If runnable->autoDelete() returns false, ownership of runnable remains with the caller
		Note that changing the auto-deletion on runnable after calling this functions results in undefined behavior.
		"""
		res = super(QThreadPool,self).start(runnable,priority)
		return res
	#----------------------------------------------------------------------
	def tryStart(self,runnable):
		"""
		tryStart(runnable)
			runnable=QtCore.QRunnable

		Attempts to reserve a thread to run runnable .
		If no threads are available at the time of calling, then this function does nothing and returns false
		Otherwise, runnable is run immediately using one available thread and this function returns true.
		Note that the thread pool takes ownership of the runnable if runnable->autoDelete() returns true, and the runnable will be deleted automatically by the thread pool after the runnable->run() returns
		If runnable->autoDelete() returns false, ownership of runnable remains with the caller
		Note that changing the auto-deletion on runnable after calling this function results in undefined behavior.
		"""
		res = super(QThreadPool,self).tryStart(runnable)
		isinstance(res,QtCore.bool)
		return res
