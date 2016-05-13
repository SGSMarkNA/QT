from PySide import QtGui, QtCore

class QDateTime(QtCore.QDateTime):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDateTime,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QDateTime,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QDateTime,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def date(self):
		"""
		Returns the date part of the datetime.
		"""
		res = super(QDateTime,self).date()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if both the date and the time are null; otherwise returns false
		A null datetime is invalid.
		"""
		res = super(QDateTime,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if both the date and the time are valid; otherwise returns false.
		"""
		res = super(QDateTime,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def time(self):
		"""
		Returns the time part of the datetime.
		"""
		res = super(QDateTime,self).time()
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def timeSpec(self):
		"""
		Returns the time specification of the datetime.
		"""
		res = super(QDateTime,self).timeSpec()
		isinstance(res,QtCore.Qt.TimeSpec)
		return res
	#----------------------------------------------------------------------
	def toLocalTime(self):
		"""
		Returns a datetime containing the date and time information in this datetime, but specified using the Qt.LocalTime definition.
		"""
		res = super(QDateTime,self).toLocalTime()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def toMSecsSinceEpoch(self):
		"""
		Returns the datetime as the number of milliseconds that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time ( Qt.UTC ).
		On systems that do not support time zones, this function will behave as if local time were Qt.UTC .
		The behavior for this function is undefined if the datetime stored in this object is not valid
		However, for all valid dates, this function returns a unique value.
		"""
		res = super(QDateTime,self).toMSecsSinceEpoch()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def toPython(self):
		"""

		"""
		res = super(QDateTime,self).toPython()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def toTime_t(self):
		"""
		Returns the datetime as the number of seconds that have passed since 1970-01-01T00:00:00, Coordinated Universal Time ( Qt.UTC ).
		On systems that do not support time zones, this function will behave as if local time were Qt.UTC .
		If the date is outside the range 1970-01-01T00:00:00 to 2106-02-07T06:28:14, this function returns -1 cast to an unsigned integer (i.e., 0xFFFFFFFF).
		To get an extended range, use PySide.QtCore.QDateTime.toMSecsSinceEpoch() .
		"""
		res = super(QDateTime,self).toTime_t()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def toUTC(self):
		"""
		Returns a datetime containing the date and time information in this datetime, but specified using the Qt.UTC definition.
		"""
		res = super(QDateTime,self).toUTC()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def utcOffset(self):
		"""
		Returns the UTC offset in seconds
		If the PySide.QtCore.QDateTime.timeSpec() isnt Qt.OffsetFromUTC , 0 is returned
		However, since 0 is a valid UTC offset the return value of this function cannot be used to determine whether a PySide.QtCore.QDateTime.utcOffset() is used or is valid, PySide.QtCore.QDateTime.timeSpec() must be checked.
		Likewise, if this PySide.QtCore.QDateTime.QDateTime() is invalid or if PySide.QtCore.QDateTime.timeSpec() isnt Qt.OffsetFromUTC , 0 is returned.
		The UTC offset only applies if the PySide.QtCore.QDateTime.timeSpec() is Qt.OffsetFromUTC .
		"""
		res = super(QDateTime,self).utcOffset()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def addDays(self,days):
		"""
		addDays(days)
			days=QtCore.int

		Returns a PySide.QtCore.QDateTime object containing a datetime ndays days later than the datetime of this object (or earlier if ndays is negative).
		"""
		res = super(QDateTime,self).addDays(days)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def addMSecs(self,msecs):
		"""
		addMSecs(msecs)
			msecs=QtCore.qint64

		Returns a PySide.QtCore.QDateTime object containing a datetime msecs miliseconds later than the datetime of this object (or earlier if msecs is negative).
		"""
		res = super(QDateTime,self).addMSecs(msecs)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def addMonths(self,months):
		"""
		addMonths(months)
			months=QtCore.int

		Returns a PySide.QtCore.QDateTime object containing a datetime nmonths months later than the datetime of this object (or earlier if nmonths is negative).
		"""
		res = super(QDateTime,self).addMonths(months)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def addSecs(self,secs):
		"""
		addSecs(secs)
			secs=QtCore.int

		Returns a PySide.QtCore.QDateTime object containing a datetime s seconds later than the datetime of this object (or earlier if s is negative).
		"""
		res = super(QDateTime,self).addSecs(secs)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def addYears(self,years):
		"""
		addYears(years)
			years=QtCore.int

		Returns a PySide.QtCore.QDateTime object containing a datetime nyears years later than the datetime of this object (or earlier if nyears is negative).
		"""
		res = super(QDateTime,self).addYears(years)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def daysTo(self,arg__1):
		"""
		daysTo(arg__1)
			arg__1=QtCore.QDateTime

		Returns the number of days from this datetime to the other datetime
		If the other datetime is earlier than this datetime, the value returned is negative.
		"""
		res = super(QDateTime,self).daysTo(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def msecsTo(self,arg__1):
		"""
		msecsTo(arg__1)
			arg__1=QtCore.QDateTime

		Returns the number of milliseconds from this datetime to the other datetime
		If the other datetime is earlier than this datetime, the value returned is negative.
		Before performing the comparison, the two datetimes are converted to Qt.UTC to ensure that the result is correct if one of the two datetimes has daylight saving time (DST) and the other doesnt.
		"""
		res = super(QDateTime,self).msecsTo(arg__1)
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is different from the other datetime; otherwise returns false.
		Two datetimes are different if either the date, the time, or the time zone components are different.
		"""
		res = super(QDateTime,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is earlier than the other datetime; otherwise returns false.
		"""
		res = super(QDateTime,self).__lt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,other):
		"""
		__le__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is earlier than or equal to the other datetime; otherwise returns false.
		"""
		res = super(QDateTime,self).__le__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is equal to the other datetime; otherwise returns false.
		"""
		res = super(QDateTime,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,other):
		"""
		__gt__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is later than the other datetime; otherwise returns false.
		"""
		res = super(QDateTime,self).__gt__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,other):
		"""
		__ge__(other)
			other=QtCore.QDateTime

		Returns true if this datetime is later than or equal to the other datetime; otherwise returns false.
		"""
		res = super(QDateTime,self).__ge__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def secsTo(self,arg__1):
		"""
		secsTo(arg__1)
			arg__1=QtCore.QDateTime

		Returns the number of seconds from this datetime to the other datetime
		If the other datetime is earlier than this datetime, the value returned is negative.
		Before performing the comparison, the two datetimes are converted to Qt.UTC to ensure that the result is correct if one of the two datetimes has daylight saving time (DST) and the other doesnt.
		Example:
		"""
		res = super(QDateTime,self).secsTo(arg__1)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setDate(self,date):
		"""
		setDate(date)
			date=QtCore.QDate

		Sets the date part of this datetime to date
		If no time is set, it is set to midnight.
		"""
		res = super(QDateTime,self).setDate(date)
		return res
	#----------------------------------------------------------------------
	def setMSecsSinceEpoch(self,msecs):
		"""
		setMSecsSinceEpoch(msecs)
			msecs=QtCore.qint64

		Sets the date and time given the number of milliseconds,``msecs`` , that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time ( Qt.UTC )
		On systems that do not support time zones this function will behave as if local time were Qt.UTC .
		Note that there are possible values for msecs that lie outside the valid range of PySide.QtCore.QDateTime , both negative and positive
		The behavior of this function is undefined for those values.
		"""
		res = super(QDateTime,self).setMSecsSinceEpoch(msecs)
		return res
	#----------------------------------------------------------------------
	def setTime(self,time):
		"""
		setTime(time)
			time=QtCore.QTime

		Sets the time part of this datetime to time .
		"""
		res = super(QDateTime,self).setTime(time)
		return res
	#----------------------------------------------------------------------
	def setTimeSpec(self,spec):
		"""
		setTimeSpec(spec)
			spec=QtCore.Qt.TimeSpec


		"""
		res = super(QDateTime,self).setTimeSpec(spec)
		return res
	#----------------------------------------------------------------------
	def setTime_t(self,secsSince1Jan1970UTC):
		"""
		setTime_t(secsSince1Jan1970UTC)
			secsSince1Jan1970UTC=QtCore.uint

		Sets the date and time given the number of seconds that have passed since 1970-01-01T00:00:00, Coordinated Universal Time ( Qt.UTC )
		On systems that do not support time zones this function will behave as if local time were Qt.UTC .
		"""
		res = super(QDateTime,self).setTime_t(secsSince1Jan1970UTC)
		return res
	#----------------------------------------------------------------------
	def setUtcOffset(self,seconds):
		"""
		setUtcOffset(seconds)
			seconds=QtCore.int

		Sets the offset from UTC to seconds , and also sets PySide.QtCore.QDateTime.timeSpec() to Qt.OffsetFromUTC .
		The maximum and minimum offset is 14 positive or negative hours
		If seconds is larger or smaller than that, the result is undefined.
		0 as offset is identical to UTC
		Therefore, if seconds is 0, the PySide.QtCore.QDateTime.timeSpec() will be set to Qt.UTC
		Hence the UTC offset always relates to UTC, and can never relate to local time.
		"""
		res = super(QDateTime,self).setUtcOffset(seconds)
		return res
	#----------------------------------------------------------------------
	def toString(self,*args,**kwargs):
		"""
		toString(format)
			format=unicode

		toString(f=None)
			f=QtCore.Qt.DateFormat

		Returns the datetime as a string
		The format parameter determines the format of the result string.
		These expressions may be used for the date:
		These expressions may be used for the time:
		All other input characters will be ignored
		Any sequence of characters that are enclosed in singlequotes will be treated as text and not be used as an expression
		Two consecutive singlequotes () are replaced by a singlequote in the output.
		Example format strings (assumed that the PySide.QtCore.QDateTime is 21 May 2001 14:13:09):
		If the datetime is invalid, an empty string will be returned.
		"""
		res = super(QDateTime,self).toString(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def toTimeSpec(self,spec):
		"""
		toTimeSpec(spec)
			spec=QtCore.Qt.TimeSpec


		"""
		res = super(QDateTime,self).toTimeSpec(spec)
		isinstance(res,QtCore.QDateTime)
		return res
