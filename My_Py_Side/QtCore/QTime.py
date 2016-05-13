from PySide import QtGui, QtCore

class QTime(QtCore.QTime):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTime,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QTime,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QTime,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def ds(self):
		"""

		"""
		res = super(QTime,self).ds()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def elapsed(self):
		"""
		Returns the number of milliseconds that have elapsed since the last time PySide.QtCore.QTime.start() or PySide.QtCore.QTime.restart() was called.
		Note that the counter wraps to zero 24 hours after the last call to PySide.QtCore.QTime.start() or restart.
		Note that the accuracy depends on the accuracy of the underlying operating system; not all systems provide 1-millisecond accuracy.
		"""
		res = super(QTime,self).elapsed()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def hour(self):
		"""
		Returns the hour part (0 to 23) of the time.
		"""
		res = super(QTime,self).hour()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the time is null (i.e., the PySide.QtCore.QTime object was constructed using the default constructor); otherwise returns false
		A null time is also an invalid time.
		"""
		res = super(QTime,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the time is valid; otherwise returns false
		For example, the time 23:30:55.746 is valid, but 24:12:30 is invalid.
		"""
		res = super(QTime,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def minute(self):
		"""
		Returns the minute part (0 to 59) of the time.
		"""
		res = super(QTime,self).minute()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def msec(self):
		"""
		Returns the millisecond part (0 to 999) of the time.
		"""
		res = super(QTime,self).msec()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def restart(self):
		"""
		Sets this time to the current time and returns the number of milliseconds that have elapsed since the last time PySide.QtCore.QTime.start() or PySide.QtCore.QTime.restart() was called.
		This function is guaranteed to be atomic and is thus very handy for repeated measurements
		Call PySide.QtCore.QTime.start() to start the first measurement, and PySide.QtCore.QTime.restart() for each later measurement.
		Note that the counter wraps to zero 24 hours after the last call to PySide.QtCore.QTime.start() or PySide.QtCore.QTime.restart() .
		"""
		res = super(QTime,self).restart()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def second(self):
		"""
		Returns the second part (0 to 59) of the time.
		"""
		res = super(QTime,self).second()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def start(self):
		"""
		Sets this time to the current time
		This is practical for timing:
		"""
		res = super(QTime,self).start()
		return res
	#----------------------------------------------------------------------
	def toPython(self):
		"""

		"""
		res = super(QTime,self).toPython()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def addMSecs(self,ms):
		"""
		addMSecs(ms)
			ms=QtCore.int

		Returns a PySide.QtCore.QTime object containing a time ms milliseconds later than the time of this object (or earlier if ms is negative).
		Note that the time will wrap if it passes midnight
		See PySide.QtCore.QTime.addSecs() for an example.
		"""
		res = super(QTime,self).addMSecs(ms)
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def addSecs(self,secs):
		"""
		addSecs(secs)
			secs=QtCore.int

		Returns a PySide.QtCore.QTime object containing a time s seconds later than the time of this object (or earlier if s is negative).
		Note that the time will wrap if it passes midnight.
		Example:
		"""
		res = super(QTime,self).addSecs(secs)
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def msecsTo(self,arg__1):
		"""
		msecsTo(arg__1)
			arg__1=QtCore.QTime

		Returns the number of milliseconds from this time to t
		If t is earlier than this time, the number of milliseconds returned is negative.
		Because PySide.QtCore.QTime measures time within a day and there are 86400 seconds in a day, the result is always between -86400000 and 86400000 ms.
		"""
		res = super(QTime,self).msecsTo(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QTime

		Returns true if this time is different from t ; otherwise returns false.
		"""
		res = super(QTime,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QTime

		Returns true if this time is earlier than t ; otherwise returns false.
		"""
		res = super(QTime,self).__lt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,other):
		"""
		__le__(other)
			other=QtCore.QTime

		Returns true if this time is earlier than or equal to t ; otherwise returns false.
		"""
		res = super(QTime,self).__le__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QTime

		Returns true if this time is equal to t ; otherwise returns false.
		"""
		res = super(QTime,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,other):
		"""
		__gt__(other)
			other=QtCore.QTime

		Returns true if this time is later than t ; otherwise returns false.
		"""
		res = super(QTime,self).__gt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,other):
		"""
		__ge__(other)
			other=QtCore.QTime

		Returns true if this time is later than or equal to t ; otherwise returns false.
		"""
		res = super(QTime,self).__ge__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def secsTo(self,arg__1):
		"""
		secsTo(arg__1)
			arg__1=QtCore.QTime

		Returns the number of seconds from this time to t
		If t is earlier than this time, the number of seconds returned is negative.
		Because PySide.QtCore.QTime measures time within a day and there are 86400 seconds in a day, the result is always between -86400 and 86400.
		PySide.QtCore.QTime.secsTo() does not take into account any milliseconds.
		"""
		res = super(QTime,self).secsTo(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setHMS(self,h,m,s,ms=None):
		"""
		setHMS(h,m,s,ms=None)
			h=QtCore.int
			m=QtCore.int
			s=QtCore.int
			ms=QtCore.int

		Sets the time to hour h , minute m , seconds s and milliseconds ms .
		h must be in the range 0 to 23, m and s must be in the range 0 to 59, and ms must be in the range 0 to 999
		Returns true if the set time is valid; otherwise returns false.
		"""
		res = super(QTime,self).setHMS(h,m,s,ms)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toString(self,*args,**kwargs):
		"""
		toString(f=None)
			f=QtCore.Qt.DateFormat

		toString(format)
			format=unicode


		"""
		res = super(QTime,self).toString(*args,**kwargs)
		return res
