from PySide import QtGui, QtCore

class QEventLoop(QtCore.QEventLoop):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QEventLoop,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isRunning(self):
		"""
		Returns true if the event loop is running; otherwise returns false
		The event loop is considered running from the time when exec() is called until PySide.QtCore.QEventLoop.exit() is called.
		"""
		res = super(QEventLoop,self).isRunning()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def wakeUp(self):
		"""
		Wakes up the event loop.
		"""
		res = super(QEventLoop,self).wakeUp()
		return res
	#----------------------------------------------------------------------
	def exec_(self,flags=None):
		"""
		exec_(flags=None)
			flags=QtCore.QEventLoop.ProcessEventsFlags


		"""
		res = super(QEventLoop,self).exec_(flags)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def exit(self,returnCode=None):
		"""
		exit(returnCode=None)
			returnCode=QtCore.int

		Tells the event loop to exit with a return code.
		After this function has been called, the event loop returns from the call to exec()
		The exec() function returns returnCode .
		By convention, a returnCode of 0 means success, and any non-zero value indicates an error.
		Note that unlike the C library function of the same name, this function does return to the caller  it is event processing that stops.
		"""
		res = super(QEventLoop,self).exit(returnCode)
		return res
	#----------------------------------------------------------------------
	def processEvents(self,*args,**kwargs):
		"""
		processEvents(flags,maximumTime)
			flags=QtCore.QEventLoop.ProcessEventsFlags
			maximumTime=QtCore.int

		processEvents(flags=None)
			flags=QtCore.QEventLoop.ProcessEventsFlags


		"""
		res = super(QEventLoop,self).processEvents(*args,**kwargs)
		return res
