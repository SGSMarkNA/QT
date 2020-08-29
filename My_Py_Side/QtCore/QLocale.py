from PySide import QtGui, QtCore

class QLocale(QtCore.QLocale):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLocale,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def amText(self):
		"""
		Returns the localized name of the AM suffix for times specified using the conventions of the 12-hour clock.
		"""
		res = super(QLocale,self).amText()
		return res
	#----------------------------------------------------------------------
	def country(self):
		"""
		Returns the country of this locale.
		"""
		res = super(QLocale,self).country()
		isinstance(res,QtCore.QLocale.Country)
		return res
	#----------------------------------------------------------------------
	def decimalPoint(self):
		"""
		Returns the decimal point character of this locale.
		"""
		res = super(QLocale,self).decimalPoint()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def exponential(self):
		"""
		Returns the exponential character of this locale.
		"""
		res = super(QLocale,self).exponential()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def groupSeparator(self):
		"""
		Returns the group separator character of this locale.
		"""
		res = super(QLocale,self).groupSeparator()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def language(self):
		"""
		Returns the language of this locale.
		"""
		res = super(QLocale,self).language()
		isinstance(res,QtCore.QLocale.Language)
		return res
	#----------------------------------------------------------------------
	def measurementSystem(self):
		"""
		Returns the measurement system for the locale.
		"""
		res = super(QLocale,self).measurementSystem()
		isinstance(res,QtCore.QLocale.MeasurementSystem)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the language and country of this locale as a string of the form language_country, where language is a lowercase, two-letter ISO 639 language code, and country is an uppercase, two-letter ISO 3166 country code.
		"""
		res = super(QLocale,self).name()
		return res
	#----------------------------------------------------------------------
	def negativeSign(self):
		"""
		Returns the negative sign character of this locale.
		"""
		res = super(QLocale,self).negativeSign()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def numberOptions(self):
		"""
		Returns the options related to number conversions for this PySide.QtCore.QLocale instance.
		By default, no options are set for the standard locales.
		"""
		res = super(QLocale,self).numberOptions()
		isinstance(res,QtCore.QLocale.NumberOptions)
		return res
	#----------------------------------------------------------------------
	def percent(self):
		"""
		Returns the percent character of this locale.
		"""
		res = super(QLocale,self).percent()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def pmText(self):
		"""
		Returns the localized name of the PM suffix for times specified using the conventions of the 12-hour clock.
		"""
		res = super(QLocale,self).pmText()
		return res
	#----------------------------------------------------------------------
	def positiveSign(self):
		"""
		Returns the positive sign character of this locale.
		"""
		res = super(QLocale,self).positiveSign()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def textDirection(self):
		"""
		Returns the text direction of the language.
		"""
		res = super(QLocale,self).textDirection()
		isinstance(res,QtCore.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def zeroDigit(self):
		"""
		Returns the zero digit character of this locale.
		"""
		res = super(QLocale,self).zeroDigit()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def dateFormat(self,format=None):
		"""
		dateFormat(format=None)
			format=QtCore.QLocale.FormatType

		Returns the date format used for the current locale.
		If format is LongFormat the format will be a long version
		Otherwise it uses a shorter version.
		"""
		res = super(QLocale,self).dateFormat(format)
		return res
	#----------------------------------------------------------------------
	def dateTimeFormat(self,format=None):
		"""
		dateTimeFormat(format=None)
			format=QtCore.QLocale.FormatType

		Returns the date time format used for the current locale.
		If format is ShortFormat the format will be a short version
		Otherwise it uses a longer version.
		"""
		res = super(QLocale,self).dateTimeFormat(format)
		return res
	#----------------------------------------------------------------------
	def dayName(self,arg__1,format=None):
		"""
		dayName(arg__1,format=None)
			arg__1=QtCore.int
			format=QtCore.QLocale.FormatType

		Returns the localized name of the day (where 1 represents Monday, 2 represents Tuesday and so on), in the format specified by type .
		"""
		res = super(QLocale,self).dayName(arg__1,format)
		return res
	#----------------------------------------------------------------------
	def monthName(self,arg__1,format=None):
		"""
		monthName(arg__1,format=None)
			arg__1=QtCore.int
			format=QtCore.QLocale.FormatType

		Returns the localized name of month , in the format specified by type .
		"""
		res = super(QLocale,self).monthName(arg__1,format)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QLocale

		Returns true if the PySide.QtCore.QLocale object is not the same as the other locale specified; otherwise returns false.
		"""
		res = super(QLocale,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QLocale

		Returns true if the PySide.QtCore.QLocale object is the same as the other locale specified; otherwise returns false.
		"""
		res = super(QLocale,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setNumberOptions(self,options):
		"""
		setNumberOptions(options)
			options=QtCore.QLocale.NumberOptions


		"""
		res = super(QLocale,self).setNumberOptions(options)
		return res
	#----------------------------------------------------------------------
	def standaloneDayName(self,arg__1,format=None):
		"""
		standaloneDayName(arg__1,format=None)
			arg__1=QtCore.int
			format=QtCore.QLocale.FormatType

		Returns the localized name of the day (where 1 represents Monday, 2 represents Tuesday and so on) that is used as a standalone text, in the format specified by type .
		If the locale information does not specify the standalone day name then return value is the same as in PySide.QtCore.QLocale.dayName() .
		"""
		res = super(QLocale,self).standaloneDayName(arg__1,format)
		return res
	#----------------------------------------------------------------------
	def standaloneMonthName(self,arg__1,format=None):
		"""
		standaloneMonthName(arg__1,format=None)
			arg__1=QtCore.int
			format=QtCore.QLocale.FormatType

		Returns the localized name of month that is used as a standalone text, in the format specified by type .
		If the locale information doesnt specify the standalone month name then return value is the same as in PySide.QtCore.QLocale.monthName() .
		"""
		res = super(QLocale,self).standaloneMonthName(arg__1,format)
		return res
	#----------------------------------------------------------------------
	def timeFormat(self,format=None):
		"""
		timeFormat(format=None)
			format=QtCore.QLocale.FormatType

		Returns the time format used for the current locale.
		If format is LongFormat the format will be a long version
		Otherwise it uses a shorter version.
		"""
		res = super(QLocale,self).timeFormat(format)
		return res
	#----------------------------------------------------------------------
	def toDate(self,*args,**kwargs):
		"""
		toDate(string,format)
			string=unicode
			format=unicode

		toDate(string,format=None)
			string=unicode
			format=QtCore.QLocale.FormatType

		Parses the date string given in string and returns the date
		See QDate.fromString() for information on the expressions that can be used with this function.
		This function searches month names and the names of the days of the week in the current locale.
		If the date could not be parsed, returns an invalid date.
		"""
		res = super(QLocale,self).toDate(*args,**kwargs)
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def toDateTime(self,*args,**kwargs):
		"""
		toDateTime(string,format)
			string=unicode
			format=unicode

		toDateTime(string,format=None)
			string=unicode
			format=QtCore.QLocale.FormatType

		Parses the date/time string given in string and returns the time
		See QDateTime.fromString() for information on the expressions that can be used with this function.
		If the string could not be parsed, returns an invalid PySide.QtCore.QDateTime .
		"""
		res = super(QLocale,self).toDateTime(*args,**kwargs)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def toDouble(self,s):
		"""
		toDouble(s)
			s=unicode

		Returns the double represented by the localized string s , or 0.0 if the conversion failed.
		If ok is not 0, reports failure by setting *ok to false and success by setting *ok to true.
		Unlike QString.toDouble() , this function does not fall back to the C locale if the string cannot be interpreted in this locale.
		Notice that the last conversion returns 1234.0, because
		is the thousands group separator in the German locale.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toDouble(s)
		return res
	#----------------------------------------------------------------------
	def toFloat(self,s):
		"""
		toFloat(s)
			s=unicode

		Returns the float represented by the localized string s , or 0.0 if the conversion failed.
		If ok is not 0, reports failure by setting *ok to false and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toFloat(s)
		return res
	#----------------------------------------------------------------------
	def toInt(self,s,base=None):
		"""
		toInt(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toInt(s,base)
		return res
	#----------------------------------------------------------------------
	def toLongLong(self,s,base=None):
		"""
		toLongLong(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the long long int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toLongLong(s,base)
		return res
	#----------------------------------------------------------------------
	def toShort(self,s,base=None):
		"""
		toShort(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the short int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toShort(s,base)
		return res
	#----------------------------------------------------------------------
	def toString(self,*args,**kwargs):
		"""
		toString(i,f=None,prec=None)
			i=QtCore.float
			f=QtCore.char
			prec=QtCore.int

		toString(i)
			i=QtCore.qlonglong

		toString(i)
			i=QtCore.int

		toString(i)
			i=QtCore.short

		toString(time,format=None)
			time=QtCore.QTime
			format=QtCore.QLocale.FormatType

		toString(date,format=None)
			date=QtCore.QDate
			format=QtCore.QLocale.FormatType

		toString(date,formatStr)
			date=QtCore.QDate
			formatStr=unicode

		toString(dateTime,format=None)
			dateTime=QtCore.QDateTime
			format=QtCore.QLocale.FormatType

		toString(i,f=None,prec=None)
			i=QtCore.double
			f=QtCore.char
			prec=QtCore.int

		toString(dateTime,format)
			dateTime=QtCore.QDateTime
			format=unicode

		toString(time,formatStr)
			time=QtCore.QTime
			formatStr=unicode

		This is an overloaded function.
		f and prec have the same meaning as in QString::number(double, char, int).
		"""
		res = super(QLocale,self).toString(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def toTime(self,*args,**kwargs):
		"""
		toTime(string,format=None)
			string=unicode
			format=QtCore.QLocale.FormatType

		toTime(string,format)
			string=unicode
			format=unicode

		Parses the time string given in string and returns the time
		The format of the time string is chosen according to the format parameter (see PySide.QtCore.QLocale.timeFormat() ).
		If the time could not be parsed, returns an invalid time.
		"""
		res = super(QLocale,self).toTime(*args,**kwargs)
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def toUInt(self,s,base=None):
		"""
		toUInt(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the unsigned int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toUInt(s,base)
		return res
	#----------------------------------------------------------------------
	def toULongLong(self,s,base=None):
		"""
		toULongLong(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the unsigned long long int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toULongLong(s,base)
		return res
	#----------------------------------------------------------------------
	def toUShort(self,s,base=None):
		"""
		toUShort(s,base=None)
			s=unicode
			base=QtCore.int

		Returns the unsigned short int represented by the localized string s , using base base
		If base is 0 the base is determined automatically using the following rules: If the string begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		If the conversion fails the function returns 0.
		If ok is not 0, failure is reported by setting *ok to false, and success by setting *ok to true.
		This function ignores leading and trailing whitespace.
		"""
		res = super(QLocale,self).toUShort(s,base)
		return res
