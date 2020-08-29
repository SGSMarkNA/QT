from PySide import QtGui, QtCore

class QTimer(QtCore.QTimer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTimer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def interval(self):
		"""
		This property holds the timeout interval in milliseconds.
		The default value for this property is 0
		A PySide.QtCore.QTimer with a timeout interval of 0 will time out as soon as all the events in the window systems event queue have been processed.
		Setting the interval of an active timer changes its PySide.QtCore.QTimer.timerId() .
		"""
		res = super(QTimer,self).interval()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		This boolean property is true if the timer is running; otherwise false.
		"""
		res = super(QTimer,self).isActive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSingleShot(self):
		"""
		This property holds whether the timer is a single-shot timer.
		A single-shot timer fires only once, non-single-shot timers fire every PySide.QtCore.QTimer.interval() milliseconds.
		"""
		res = super(QTimer,self).isSingleShot()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def timeout(self):
		"""

		"""
		res = super(QTimer,self).timeout()
		return res
	#----------------------------------------------------------------------
	def timerId(self):
		"""
		Returns the ID of the timer if the timer is running; otherwise returns -1.
		"""
		res = super(QTimer,self).timerId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setInterval(self,msec):
		"""
		setInterval(msec)
			msec=QtCore.int

		This property holds the timeout interval in milliseconds.
		The default value for this property is 0
		A PySide.QtCore.QTimer with a timeout interval of 0 will time out as soon as all the events in the window systems event queue have been processed.
		Setting the interval of an active timer changes its PySide.QtCore.QTimer.timerId() .
		"""
		res = super(QTimer,self).setInterval(msec)
		return res
	#----------------------------------------------------------------------
	def setSingleShot(self,singleShot):
		"""
		setSingleShot(singleShot)
			singleShot=QtCore.bool

		This property holds whether the timer is a single-shot timer.
		A single-shot timer fires only once, non-single-shot timers fire every PySide.QtCore.QTimer.interval() milliseconds.
		"""
		res = super(QTimer,self).setSingleShot(singleShot)
		return res
