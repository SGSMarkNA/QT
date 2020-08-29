from PySide import QtGui, QtCore

class QDateTimeEdit(QtGui.QDateTimeEdit):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDateTimeEdit,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def calendarPopup(self):
		"""
		This property holds the current calendar pop-up showing mode..
		The calendar pop-up will be shown upon clicking the arrow button
		This property is valid only if there is a valid date display format.
		"""
		res = super(QDateTimeEdit,self).calendarPopup()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def calendarWidget(self):
		"""
		Returns the calendar widget for the editor if PySide.QtGui.QDateTimeEdit.calendarPopup() is set to true and ( sections() & DateSections_Mask ) != 0.
		This function creates and returns a calendar widget if none has been set.
		"""
		res = super(QDateTimeEdit,self).calendarWidget()
		isinstance(res,QtGui.QCalendarWidget)
		return res
	#----------------------------------------------------------------------
	def clearMaximumDate(self):
		"""
		This property holds the maximum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDate() is adjusted if necessary to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to December 31, 7999.
		"""
		res = super(QDateTimeEdit,self).clearMaximumDate()
		return res
	#----------------------------------------------------------------------
	def clearMaximumDateTime(self):
		"""
		This property holds the maximum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.maximumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMaximumDateTime() .
		By default, this property contains a date that refers to 31 December, 7999 and a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).clearMaximumDateTime()
		return res
	#----------------------------------------------------------------------
	def clearMaximumTime(self):
		"""
		This property holds the maximum time of the date time edit.
		When setting this property, the PySide.QtGui.QDateTimeEdit.minimumTime() is adjusted if necessary to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).clearMaximumTime()
		return res
	#----------------------------------------------------------------------
	def clearMinimumDate(self):
		"""
		This property holds the minimum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDate() is adjusted if necessary, to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to September 14, 1752
		The minimum date must be at least the first day in year 100, otherwise PySide.QtGui.QDateTimeEdit.setMinimumDate() has no effect.
		"""
		res = super(QDateTimeEdit,self).clearMinimumDate()
		return res
	#----------------------------------------------------------------------
	def clearMinimumDateTime(self):
		"""
		This property holds the minimum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.minimumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMinimumDateTime()
		By default, this property contains a date that refers to September 14, 1752 and a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).clearMinimumDateTime()
		return res
	#----------------------------------------------------------------------
	def clearMinimumTime(self):
		"""
		This property holds the minimum time of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumTime() is adjusted if necessary, to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).clearMinimumTime()
		return res
	#----------------------------------------------------------------------
	def currentSection(self):
		"""
		This property holds the current section of the spinbox setCurrentSection() .
		"""
		res = super(QDateTimeEdit,self).currentSection()
		isinstance(res,QtGui.QDateTimeEdit.Section)
		return res
	#----------------------------------------------------------------------
	def currentSectionIndex(self):
		"""
		This property holds the current section index of the spinbox.
		If the format is yyyy/MM/dd, the displayText is 2001/05/21 and the cursorPosition is 5 PySide.QtGui.QDateTimeEdit.currentSectionIndex() returns 1
		If the cursorPosition is 3 PySide.QtGui.QDateTimeEdit.currentSectionIndex() is 0 etc.
		setCurrentSection()
		"""
		res = super(QDateTimeEdit,self).currentSectionIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def date(self):
		"""
		This property holds the PySide.QtCore.QDate that is set in the widget.
		By default, this property contains a date that refers to January 1, 2000.
		"""
		res = super(QDateTimeEdit,self).date()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def dateTime(self):
		"""
		This property holds the PySide.QtCore.QDateTime that is set in the PySide.QtGui.QDateTimeEdit .
		When setting this property the timespec of the PySide.QtGui.QDateTimeEdit remains the same and the timespec of the new PySide.QtCore.QDateTime is ignored.
		By default, this property contains a date that refers to January 1, 2000 and a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).dateTime()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def displayFormat(self):
		"""
		This property holds the format used to display the time/date of the date time edit.
		This format is the same as the one used described in QDateTime.toString() and QDateTime.fromString()
		Example format strings (assuming that the date is 2nd of July 1969):
		Note that if you specify a two digit year, it will be interpreted to be in the century in which the date time edit was initialized
		The default century is the 21 (2000-2099).
		If you specify an invalid format the format will not be set.
		"""
		res = super(QDateTimeEdit,self).displayFormat()
		return res
	#----------------------------------------------------------------------
	def displayedSections(self):
		"""
		This property holds the currently displayed fields of the date time edit.
		Returns a bit set of the displayed sections for this format
		setDisplayFormat() , PySide.QtGui.QDateTimeEdit.displayFormat()
		"""
		res = super(QDateTimeEdit,self).displayedSections()
		isinstance(res,QtGui.QDateTimeEdit.Sections)
		return res
	#----------------------------------------------------------------------
	def maximumDate(self):
		"""
		This property holds the maximum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDate() is adjusted if necessary to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to December 31, 7999.
		"""
		res = super(QDateTimeEdit,self).maximumDate()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def maximumDateTime(self):
		"""
		This property holds the maximum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.maximumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMaximumDateTime() .
		By default, this property contains a date that refers to 31 December, 7999 and a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).maximumDateTime()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def maximumTime(self):
		"""
		This property holds the maximum time of the date time edit.
		When setting this property, the PySide.QtGui.QDateTimeEdit.minimumTime() is adjusted if necessary to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).maximumTime()
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def minimumDate(self):
		"""
		This property holds the minimum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDate() is adjusted if necessary, to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to September 14, 1752
		The minimum date must be at least the first day in year 100, otherwise PySide.QtGui.QDateTimeEdit.setMinimumDate() has no effect.
		"""
		res = super(QDateTimeEdit,self).minimumDate()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def minimumDateTime(self):
		"""
		This property holds the minimum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.minimumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMinimumDateTime()
		By default, this property contains a date that refers to September 14, 1752 and a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).minimumDateTime()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def minimumTime(self):
		"""
		This property holds the minimum time of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumTime() is adjusted if necessary, to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).minimumTime()
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def sectionCount(self):
		"""
		This property holds the number of sections displayed
		If the format is yyyy/yy/yyyy, PySide.QtGui.QDateTimeEdit.sectionCount() returns 3.
		"""
		res = super(QDateTimeEdit,self).sectionCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def time(self):
		"""
		This property holds the PySide.QtCore.QTime that is set in the widget.
		By default, this property contains a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).time()
		isinstance(res,QtCore.QTime)
		return res
	#----------------------------------------------------------------------
	def timeSpec(self):
		"""
		This property holds the current timespec used by the date time edit..
		"""
		res = super(QDateTimeEdit,self).timeSpec()
		isinstance(res,QtCore.Qt.TimeSpec)
		return res
	#----------------------------------------------------------------------
	def dateTimeFromText(self,text):
		"""
		dateTimeFromText(text)
			text=unicode

		Returns an appropriate datetime for the given text .
		This virtual function is used by the datetime edit whenever it needs to interpret text entered by the user as a value.
		"""
		res = super(QDateTimeEdit,self).dateTimeFromText(text)
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def sectionAt(self,index):
		"""
		sectionAt(index)
			index=QtCore.int

		Returns the Section at index .
		If the format is yyyy/MM/dd, sectionAt(0) returns YearSection , sectionAt(1) returns MonthSection , and sectionAt(2) returns YearSection ,
		"""
		res = super(QDateTimeEdit,self).sectionAt(index)
		isinstance(res,QtGui.QDateTimeEdit.Section)
		return res
	#----------------------------------------------------------------------
	def sectionText(self,section):
		"""
		sectionText(section)
			section=QtGui.QDateTimeEdit.Section

		Returns the text from the given section .
		"""
		res = super(QDateTimeEdit,self).sectionText(section)
		return res
	#----------------------------------------------------------------------
	def setCalendarPopup(self,enable):
		"""
		setCalendarPopup(enable)
			enable=QtCore.bool

		This property holds the current calendar pop-up showing mode..
		The calendar pop-up will be shown upon clicking the arrow button
		This property is valid only if there is a valid date display format.
		"""
		res = super(QDateTimeEdit,self).setCalendarPopup(enable)
		return res
	#----------------------------------------------------------------------
	def setCalendarWidget(self,calendarWidget):
		"""
		setCalendarWidget(calendarWidget)
			calendarWidget=QtGui.QCalendarWidget

		Sets the given calendarWidget as the widget to be used for the calendar pop-up
		The editor does not automatically take ownership of the calendar widget.
		"""
		res = super(QDateTimeEdit,self).setCalendarWidget(calendarWidget)
		return res
	#----------------------------------------------------------------------
	def setCurrentSection(self,section):
		"""
		setCurrentSection(section)
			section=QtGui.QDateTimeEdit.Section

		This property holds the current section of the spinbox setCurrentSection() .
		"""
		res = super(QDateTimeEdit,self).setCurrentSection(section)
		return res
	#----------------------------------------------------------------------
	def setCurrentSectionIndex(self,index):
		"""
		setCurrentSectionIndex(index)
			index=QtCore.int

		This property holds the current section index of the spinbox.
		If the format is yyyy/MM/dd, the displayText is 2001/05/21 and the cursorPosition is 5 PySide.QtGui.QDateTimeEdit.currentSectionIndex() returns 1
		If the cursorPosition is 3 PySide.QtGui.QDateTimeEdit.currentSectionIndex() is 0 etc.
		setCurrentSection()
		"""
		res = super(QDateTimeEdit,self).setCurrentSectionIndex(index)
		return res
	#----------------------------------------------------------------------
	def setDateRange(self,min,max):
		"""
		setDateRange(min,max)
			min=QtCore.QDate
			max=QtCore.QDate

		Convenience function to set minimum and maximum date with one function call.
		is analogous to:
		If either min or max are not valid, this function does nothing.
		"""
		res = super(QDateTimeEdit,self).setDateRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setDateTimeRange(self,min,max):
		"""
		setDateTimeRange(min,max)
			min=QtCore.QDateTime
			max=QtCore.QDateTime

		Convenience function to set minimum and maximum date time with one function call.
		is analogous to:
		If either min or max are not valid, this function does nothing.
		"""
		res = super(QDateTimeEdit,self).setDateTimeRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setDisplayFormat(self,format):
		"""
		setDisplayFormat(format)
			format=unicode

		This property holds the format used to display the time/date of the date time edit.
		This format is the same as the one used described in QDateTime.toString() and QDateTime.fromString()
		Example format strings (assuming that the date is 2nd of July 1969):
		Note that if you specify a two digit year, it will be interpreted to be in the century in which the date time edit was initialized
		The default century is the 21 (2000-2099).
		If you specify an invalid format the format will not be set.
		"""
		res = super(QDateTimeEdit,self).setDisplayFormat(format)
		return res
	#----------------------------------------------------------------------
	def setMaximumDate(self,max):
		"""
		setMaximumDate(max)
			max=QtCore.QDate

		This property holds the maximum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDate() is adjusted if necessary to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to December 31, 7999.
		"""
		res = super(QDateTimeEdit,self).setMaximumDate(max)
		return res
	#----------------------------------------------------------------------
	def setMaximumDateTime(self,dt):
		"""
		setMaximumDateTime(dt)
			dt=QtCore.QDateTime

		This property holds the maximum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.minimumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.maximumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMaximumDateTime() .
		By default, this property contains a date that refers to 31 December, 7999 and a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).setMaximumDateTime(dt)
		return res
	#----------------------------------------------------------------------
	def setMaximumTime(self,max):
		"""
		setMaximumTime(max)
			max=QtCore.QTime

		This property holds the maximum time of the date time edit.
		When setting this property, the PySide.QtGui.QDateTimeEdit.minimumTime() is adjusted if necessary to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 23:59:59 and 999 milliseconds.
		"""
		res = super(QDateTimeEdit,self).setMaximumTime(max)
		return res
	#----------------------------------------------------------------------
	def setMinimumDate(self,min):
		"""
		setMinimumDate(min)
			min=QtCore.QDate

		This property holds the minimum date of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDate() is adjusted if necessary, to ensure that the range remains valid
		If the date is not a valid PySide.QtCore.QDate object, this function does nothing.
		By default, this property contains a date that refers to September 14, 1752
		The minimum date must be at least the first day in year 100, otherwise PySide.QtGui.QDateTimeEdit.setMinimumDate() has no effect.
		"""
		res = super(QDateTimeEdit,self).setMinimumDate(min)
		return res
	#----------------------------------------------------------------------
	def setMinimumDateTime(self,dt):
		"""
		setMinimumDateTime(dt)
			dt=QtCore.QDateTime

		This property holds the minimum datetime of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumDateTime() is adjusted if necessary to ensure that the range remains valid
		If the datetime is not a valid PySide.QtCore.QDateTime object, this function does nothing.
		The default PySide.QtGui.QDateTimeEdit.minimumDateTime() can be restored with PySide.QtGui.QDateTimeEdit.clearMinimumDateTime()
		By default, this property contains a date that refers to September 14, 1752 and a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).setMinimumDateTime(dt)
		return res
	#----------------------------------------------------------------------
	def setMinimumTime(self,min):
		"""
		setMinimumTime(min)
			min=QtCore.QTime

		This property holds the minimum time of the date time edit.
		When setting this property the PySide.QtGui.QDateTimeEdit.maximumTime() is adjusted if necessary, to ensure that the range remains valid
		If the time is not a valid PySide.QtCore.QTime object, this function does nothing.
		By default, this property contains a time of 00:00:00 and 0 milliseconds.
		"""
		res = super(QDateTimeEdit,self).setMinimumTime(min)
		return res
	#----------------------------------------------------------------------
	def setSelectedSection(self,section):
		"""
		setSelectedSection(section)
			section=QtGui.QDateTimeEdit.Section

		Selects section
		If section doesnt exist in the currently displayed sections this function does nothing
		If section is NoSection this function will unselect all text in the editor
		Otherwise this function will move the cursor and the current section to the selected section.
		"""
		res = super(QDateTimeEdit,self).setSelectedSection(section)
		return res
	#----------------------------------------------------------------------
	def setTimeRange(self,min,max):
		"""
		setTimeRange(min,max)
			min=QtCore.QTime
			max=QtCore.QTime

		Convenience function to set minimum and maximum time with one function call.
		is analogous to:
		If either min or max are not valid, this function does nothing.
		"""
		res = super(QDateTimeEdit,self).setTimeRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setTimeSpec(self,spec):
		"""
		setTimeSpec(spec)
			spec=QtCore.Qt.TimeSpec

		This property holds the current timespec used by the date time edit..
		"""
		res = super(QDateTimeEdit,self).setTimeSpec(spec)
		return res
	#----------------------------------------------------------------------
	def textFromDateTime(self,dt):
		"""
		textFromDateTime(dt)
			dt=QtCore.QDateTime

		This virtual function is used by the date time edit whenever it needs to display dateTime .
		If you reimplement this, you may also need to reimplement PySide.QtGui.QDateTimeEdit.validate() .
		"""
		res = super(QDateTimeEdit,self).textFromDateTime(dt)
		return res
