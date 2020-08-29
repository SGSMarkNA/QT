from PySide import QtGui, QtCore

class QDate(QtCore.QDate):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDate,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QDate,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QDate,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def day(self):
		"""
		Returns the day of the month (1 to 31) of this date.
		"""
		res = super(QDate,self).day()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def dayOfWeek(self):
		"""
		Returns the weekday (1 to 7) for this date.
		"""
		res = super(QDate,self).dayOfWeek()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def dayOfYear(self):
		"""
		Returns the day of the year (1 to 365 or 366 on leap years) for this date.
		"""
		res = super(QDate,self).dayOfYear()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def daysInMonth(self):
		"""
		Returns the number of days in the month (28 to 31) for this date.
		"""
		res = super(QDate,self).daysInMonth()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def daysInYear(self):
		"""
		Returns the number of days in the year (365 or 366) for this date.
		"""
		res = super(QDate,self).daysInYear()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def getDate(self):
		"""
		Extracts the dates year, month, and day, and assigns them to *``year`` , *``month`` , and *``day``
		The pointers may be null.
		"""
		res = super(QDate,self).getDate()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the date is null; otherwise returns false
		A null date is invalid.
		"""
		res = super(QDate,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this date is valid; otherwise returns false.
		"""
		res = super(QDate,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def month(self):
		"""
		Returns the number corresponding to the month of this date, using the following convention:
		"""
		res = super(QDate,self).month()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toJulianDay(self):
		"""
		Converts the date to a Julian day.
		"""
		res = super(QDate,self).toJulianDay()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toPython(self):
		"""

		"""
		res = super(QDate,self).toPython()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def weekNumber(self):
		"""
		Returns the week number (1 to 53), and stores the year in *``yearNumber`` unless yearNumber is null (the default).
		Returns 0 if the date is invalid.
		In accordance with ISO 8601, weeks start on Monday and the first Thursday of a year is always in week 1 of that year
		Most years have 52 weeks, but some have 53.
		*``yearNumber`` is not always the same as PySide.QtCore.QDate.year()
		For example, 1 January 2000 has week number 52 in the year 1999, and 31 December 2002 has week number 1 in the year 2003.
		"""
		res = super(QDate,self).weekNumber()
		return res
	#----------------------------------------------------------------------
	def year(self):
		"""
		Returns the year of this date
		Negative numbers indicate years before 1 A.D
		= 1 C.E., such that year -44 is 44 B.C.
		"""
		res = super(QDate,self).year()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addDays(self,days):
		"""
		addDays(days)
			days=QtCore.int

		Returns a PySide.QtCore.QDate object containing a date ndays later than the date of this object (or earlier if ndays is negative).
		"""
		res = super(QDate,self).addDays(days)
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def addMonths(self,months):
		"""
		addMonths(months)
			months=QtCore.int

		Returns a PySide.QtCore.QDate object containing a date nmonths later than the date of this object (or earlier if nmonths is negative).
		"""
		res = super(QDate,self).addMonths(months)
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def addYears(self,years):
		"""
		addYears(years)
			years=QtCore.int

		Returns a PySide.QtCore.QDate object containing a date nyears later than the date of this object (or earlier if nyears is negative).
		"""
		res = super(QDate,self).addYears(years)
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def daysTo(self,arg__1):
		"""
		daysTo(arg__1)
			arg__1=QtCore.QDate

		Returns the number of days from this date to d (which is negative if d is earlier than this date).
		Example:
		"""
		res = super(QDate,self).daysTo(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QDate

		Returns true if this date is different from d ; otherwise returns false.
		"""
		res = super(QDate,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtCore.QDate

		Returns true if this date is earlier than d ; otherwise returns false.
		"""
		res = super(QDate,self).__lt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,other):
		"""
		__le__(other)
			other=QtCore.QDate

		Returns true if this date is earlier than or equal to d ; otherwise returns false.
		"""
		res = super(QDate,self).__le__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QDate

		Returns true if this date is equal to d ; otherwise returns false.
		"""
		res = super(QDate,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,other):
		"""
		__gt__(other)
			other=QtCore.QDate

		Returns true if this date is later than d ; otherwise returns false.
		"""
		res = super(QDate,self).__gt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,other):
		"""
		__ge__(other)
			other=QtCore.QDate

		Returns true if this date is later than or equal to d ; otherwise returns false.
		"""
		res = super(QDate,self).__ge__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setDate(self,year,month,day):
		"""
		setDate(year,month,day)
			year=QtCore.int
			month=QtCore.int
			day=QtCore.int

		Sets the dates year , month , and day
		Returns true if the date is valid; otherwise returns false.
		If the specified date is invalid, the PySide.QtCore.QDate object is set to be invalid
		Any date before 2 January 4713 B.C
		is considered invalid.
		"""
		res = super(QDate,self).setDate(year,month,day)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setYMD(self,y,m,d):
		"""
		setYMD(y,m,d)
			y=QtCore.int
			m=QtCore.int
			d=QtCore.int

		Sets the dates year y , month m , and day d .
		If y is in the range 0 to 99, it is interpreted as 1900 to 1999.
		Use PySide.QtCore.QDate.setDate() instead.
		"""
		res = super(QDate,self).setYMD(y,m,d)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toString(self,*args,**kwargs):
		"""
		toString(format)
			format=unicode

		toString(f=None)
			f=QtCore.Qt.DateFormat

		Returns the date as a string
		The format parameter determines the format of the result string.
		These expressions may be used:
		All other input characters will be ignored
		Any sequence of characters that are enclosed in singlequotes will be treated as text and not be used as an expression
		Two consecutive singlequotes () are replaced by a singlequote in the output.
		Example format strings (assuming that the PySide.QtCore.QDate is the 20 July 1969):
		If the datetime is invalid, an empty string will be returned.
		"""
		res = super(QDate,self).toString(*args,**kwargs)
		return res
