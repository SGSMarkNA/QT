from PySide import QtGui, QtCore

class QThread(QtCore.QThread):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QThread,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def exec_(self):
		"""
		Enters the event loop and waits until PySide.QtCore.QThread.exit() is called, returning the value that was passed to PySide.QtCore.QThread.exit()
		The value returned is 0 if PySide.QtCore.QThread.exit() is called via PySide.QtCore.QThread.quit() .
		It is necessary to call this function to start event handling.
		"""
		res = super(QThread,self).exec_()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QThread,self).finished()
		return res
	#----------------------------------------------------------------------
	def isFinished(self):
		"""
		Returns true if the thread is finished; otherwise returns false.
		"""
		res = super(QThread,self).isFinished()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isRunning(self):
		"""
		Returns true if the thread is running; otherwise returns false.
		"""
		res = super(QThread,self).isRunning()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def priority(self):
		"""
		Returns the priority for a running thread
		If the thread is not running, this function returns InheritPriority .
		"""
		res = super(QThread,self).priority()
		isinstance(res,QtCore.QThread.Priority)
		return res
	#----------------------------------------------------------------------
	def run(self):
		"""
		The starting point for the thread
		After calling PySide.QtCore.QThread.start() , the newly created thread calls this function
		The default implementation simply calls exec() .
		You can reimplemented this function to do other useful work
		Returning from this method will end the execution of the thread.
		"""
		res = super(QThread,self).run()
		return res
	#----------------------------------------------------------------------
	def stackSize(self):
		"""
		Returns the maximum stack size for the thread (if set with PySide.QtCore.QThread.setStackSize() ); otherwise returns zero.
		"""
		res = super(QThread,self).stackSize()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def started(self):
		"""

		"""
		res = super(QThread,self).started()
		return res
	#----------------------------------------------------------------------
	def terminated(self):
		"""

		"""
		res = super(QThread,self).terminated()
		return res
	#----------------------------------------------------------------------
	def exit(self,retcode=None):
		"""
		exit(retcode=None)
			retcode=QtCore.int

		Tells the threads event loop to exit with a return code.
		After calling this function, the thread leaves the event loop and returns from the call to QEventLoop.exec()
		The QEventLoop.exec() function returns returnCode .
		By convention, a returnCode of 0 means success, any non-zero value indicates an error.
		Note that unlike the C library function of the same name, this function does return to the caller  it is event processing that stops.
		This function does nothing if the thread does not have an event loop.
		"""
		res = super(QThread,self).exit(retcode)
		return res
	#----------------------------------------------------------------------
	def setPriority(self,priority):
		"""
		setPriority(priority)
			priority=QtCore.QThread.Priority

		This function sets the priority for a running thread
		If the thread is not running, this function does nothing and returns immediately
		Use PySide.QtCore.QThread.start() to start a thread with a specific priority.
		The priority argument can be any value in the QThread::Priority enum except for InheritPriorty .
		The effect of the priority parameter is dependent on the operating systems scheduling policy
		In particular, the priority will be ignored on systems that do not support thread priorities (such as on Linux, see http://linux.die.net/man/2/sched_setscheduler for more details).
		"""
		res = super(QThread,self).setPriority(priority)
		return res
	#----------------------------------------------------------------------
	def setStackSize(self,stackSize):
		"""
		setStackSize(stackSize)
			stackSize=QtCore.uint

		Sets the maximum stack size for the thread to stackSize
		If stackSize is greater than zero, the maximum stack size is set to stackSize bytes, otherwise the maximum stack size is automatically determined by the operating system.
		"""
		res = super(QThread,self).setStackSize(stackSize)
		return res
	#----------------------------------------------------------------------
	def wait(self,time=None):
		"""
		wait(time=None)
			time=long

		Blocks the thread until either of these conditions is met:
		This provides similar functionality to the POSIX pthread_join() function.
		"""
		res = super(QThread,self).wait(time)
		isinstance(res,bool)
		return res
