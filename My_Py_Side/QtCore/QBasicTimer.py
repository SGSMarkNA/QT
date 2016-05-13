from PySide import QtGui, QtCore

class QBasicTimer(QtCore.QBasicTimer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBasicTimer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if the timer is running and has not been stopped; otherwise returns false.
		"""
		res = super(QBasicTimer,self).isActive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def stop(self):
		"""
		Stops the timer.
		"""
		res = super(QBasicTimer,self).stop()
		return res
	#----------------------------------------------------------------------
	def timerId(self):
		"""
		Returns the timers ID.
		"""
		res = super(QBasicTimer,self).timerId()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def start(self,msec,obj):
		"""
		start(msec,obj)
			msec=QtCore.int
			obj=QtCore.QObject

		Starts (or restarts) the timer with a msec milliseconds timeout.
		The given object will receive timer events.
		"""
		res = super(QBasicTimer,self).start(msec,obj)
		return res
