from PySide import QtGui, QtCore

class QCalendarWidget(QtGui.QCalendarWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCalendarWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def dateEditAcceptDelay(self):
		"""
		This property holds the time an inactive date edit is shown before its contents are accepted.
		If the calendar widgets date edit is enabled , this property specifies the amount of time (in millseconds) that the date edit remains open after the most recent user input
		Once this time has elapsed, the date specified in the date edit is accepted and the popup is closed.
		By default, the delay is defined to be 1500 milliseconds (1.5 seconds).
		"""
		res = super(QCalendarWidget,self).dateEditAcceptDelay()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def dateTextFormat(self):
		"""
		Returns a QMap from PySide.QtCore.QDate to PySide.QtGui.QTextCharFormat showing all dates that use a special format that alters their rendering.
		"""
		res = super(QCalendarWidget,self).dateTextFormat()
		return res
	#----------------------------------------------------------------------
	def firstDayOfWeek(self):
		"""
		This property holds a value identifying the day displayed in the first column..
		By default, the day displayed in the first column is Sunday
		"""
		res = super(QCalendarWidget,self).firstDayOfWeek()
		isinstance(res,QtCore.Qt.DayOfWeek)
		return res
	#----------------------------------------------------------------------
	def headerTextFormat(self):
		"""
		Returns the text char format for rendering the header.
		"""
		res = super(QCalendarWidget,self).headerTextFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def horizontalHeaderFormat(self):
		"""
		This property holds the format of the horizontal header..
		The default value is QCalendarWidget.ShortDayNames .
		"""
		res = super(QCalendarWidget,self).horizontalHeaderFormat()
		isinstance(res,QtGui.QCalendarWidget.HorizontalHeaderFormat)
		return res
	#----------------------------------------------------------------------
	def isDateEditEnabled(self):
		"""
		This property holds whether the date edit popup is enabled.
		If this property is enabled, pressing a non-modifier key will cause a date edit to popup if the calendar widget has focus, allowing the user to specify a date in the form specified by the current locale.
		By default, this property is enabled.
		The date edit is simpler in appearance than PySide.QtGui.QDateEdit , but allows the user to navigate between fields using the left and right cursor keys, increment and decrement individual fields using the up and down cursor keys, and enter values directly using the number keys.
		"""
		res = super(QCalendarWidget,self).isDateEditEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isGridVisible(self):
		"""
		This property holds whether the table grid is displayed..
		The default value is false.
		"""
		res = super(QCalendarWidget,self).isGridVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNavigationBarVisible(self):
		"""
		This property holds whether the navigation bar is shown or not.
		When this property is true (the default), the next month, previous month, month selection, year selection controls are shown on top.
		When the property is set to false, these controls are hidden.
		"""
		res = super(QCalendarWidget,self).isNavigationBarVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def maximumDate(self):
		"""
		This property holds the maximum date of the currently specified date range..
		The user will not be able to select a date which is after the currently set maximum date.
		By default, the maximum date is the last day the PySide.QtCore.QDate class can handle.
		When setting a maximum date, the PySide.QtGui.QCalendarWidget.minimumDate() and PySide.QtGui.QCalendarWidget.selectedDate() properties are adjusted if the selection range becomes invalid
		If the provided date is not a valid PySide.QtCore.QDate object, the PySide.QtGui.QCalendarWidget.setMaximumDate() function does nothing.
		"""
		res = super(QCalendarWidget,self).maximumDate()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def minimumDate(self):
		"""
		This property holds the minimum date of the currently specified date range..
		The user will not be able to select a date that is before the currently set minimum date.
		By default, the minimum date is the earliest date that the PySide.QtCore.QDate class can handle.
		When setting a minimum date, the PySide.QtGui.QCalendarWidget.maximumDate() and PySide.QtGui.QCalendarWidget.selectedDate() properties are adjusted if the selection range becomes invalid
		If the provided date is not a valid PySide.QtCore.QDate object, the PySide.QtGui.QCalendarWidget.setMinimumDate() function does nothing.
		"""
		res = super(QCalendarWidget,self).minimumDate()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def monthShown(self):
		"""
		Returns the currently displayed month
		Months are numbered from 1 to 12.
		"""
		res = super(QCalendarWidget,self).monthShown()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def selectedDate(self):
		"""
		This property holds the currently selected date..
		The selected date must be within the date range specified by the PySide.QtGui.QCalendarWidget.minimumDate() and PySide.QtGui.QCalendarWidget.maximumDate() properties
		By default, the selected date is the current date.
		"""
		res = super(QCalendarWidget,self).selectedDate()
		isinstance(res,QtCore.QDate)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QCalendarWidget,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def selectionMode(self):
		"""
		This property holds the type of selection the user can make in the calendar.
		When this property is set to SingleSelection , the user can select a date within the minimum and maximum allowed dates, using either the mouse or the keyboard.
		When the property is set to NoSelection , the user will be unable to select dates, but they can still be selected programmatically
		Note that the date that is selected when the property is set to NoSelection will still be the selected date of the calendar.
		The default value is SingleSelection .
		"""
		res = super(QCalendarWidget,self).selectionMode()
		isinstance(res,QtGui.QCalendarWidget.SelectionMode)
		return res
	#----------------------------------------------------------------------
	def updateCells(self):
		"""
		Updates all visible cells unless updates are disabled.
		"""
		res = super(QCalendarWidget,self).updateCells()
		return res
	#----------------------------------------------------------------------
	def verticalHeaderFormat(self):
		"""
		This property holds the format of the vertical header..
		The default value is QCalendarWidget::ISOWeekNumber.
		"""
		res = super(QCalendarWidget,self).verticalHeaderFormat()
		isinstance(res,QtGui.QCalendarWidget.VerticalHeaderFormat)
		return res
	#----------------------------------------------------------------------
	def yearShown(self):
		"""
		Returns the year of the currently displayed month
		Months are numbered from 1 to 12.
		"""
		res = super(QCalendarWidget,self).yearShown()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def dateTextFormat(self,date):
		"""
		dateTextFormat(date)
			date=QtCore.QDate

		Returns a PySide.QtGui.QTextCharFormat for date
		The char format can be be empty if the date is not renderd specially.
		"""
		res = super(QCalendarWidget,self).dateTextFormat(date)
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def paintCell(self,painter,rect,date):
		"""
		paintCell(painter,rect,date)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			date=QtCore.QDate

		Paints the cell specified by the given date , using the given painter and rect .
		"""
		res = super(QCalendarWidget,self).paintCell(painter,rect,date)
		return res
	#----------------------------------------------------------------------
	def setDateEditAcceptDelay(self,delay):
		"""
		setDateEditAcceptDelay(delay)
			delay=QtCore.int

		This property holds the time an inactive date edit is shown before its contents are accepted.
		If the calendar widgets date edit is enabled , this property specifies the amount of time (in millseconds) that the date edit remains open after the most recent user input
		Once this time has elapsed, the date specified in the date edit is accepted and the popup is closed.
		By default, the delay is defined to be 1500 milliseconds (1.5 seconds).
		"""
		res = super(QCalendarWidget,self).setDateEditAcceptDelay(delay)
		return res
	#----------------------------------------------------------------------
	def setDateEditEnabled(self,enable):
		"""
		setDateEditEnabled(enable)
			enable=QtCore.bool

		This property holds whether the date edit popup is enabled.
		If this property is enabled, pressing a non-modifier key will cause a date edit to popup if the calendar widget has focus, allowing the user to specify a date in the form specified by the current locale.
		By default, this property is enabled.
		The date edit is simpler in appearance than PySide.QtGui.QDateEdit , but allows the user to navigate between fields using the left and right cursor keys, increment and decrement individual fields using the up and down cursor keys, and enter values directly using the number keys.
		"""
		res = super(QCalendarWidget,self).setDateEditEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setDateTextFormat(self,date,format):
		"""
		setDateTextFormat(date,format)
			date=QtCore.QDate
			format=QtGui.QTextCharFormat

		Sets the format used to render the given date to that specified by format .
		If date is null, all date formats are cleared.
		"""
		res = super(QCalendarWidget,self).setDateTextFormat(date,format)
		return res
	#----------------------------------------------------------------------
	def setFirstDayOfWeek(self,dayOfWeek):
		"""
		setFirstDayOfWeek(dayOfWeek)
			dayOfWeek=QtCore.Qt.DayOfWeek

		This property holds a value identifying the day displayed in the first column..
		By default, the day displayed in the first column is Sunday
		"""
		res = super(QCalendarWidget,self).setFirstDayOfWeek(dayOfWeek)
		return res
	#----------------------------------------------------------------------
	def setHeaderTextFormat(self,format):
		"""
		setHeaderTextFormat(format)
			format=QtGui.QTextCharFormat

		Sets the text char format for rendering the header to format
		If you also set a weekday text format, this formats foreground and background color will take precedence over the headers format
		The other formatting information will still be decided by the headers format.
		"""
		res = super(QCalendarWidget,self).setHeaderTextFormat(format)
		return res
	#----------------------------------------------------------------------
	def setHorizontalHeaderFormat(self,format):
		"""
		setHorizontalHeaderFormat(format)
			format=QtGui.QCalendarWidget.HorizontalHeaderFormat

		This property holds the format of the horizontal header..
		The default value is QCalendarWidget.ShortDayNames .
		"""
		res = super(QCalendarWidget,self).setHorizontalHeaderFormat(format)
		return res
	#----------------------------------------------------------------------
	def setMaximumDate(self,date):
		"""
		setMaximumDate(date)
			date=QtCore.QDate

		This property holds the maximum date of the currently specified date range..
		The user will not be able to select a date which is after the currently set maximum date.
		By default, the maximum date is the last day the PySide.QtCore.QDate class can handle.
		When setting a maximum date, the PySide.QtGui.QCalendarWidget.minimumDate() and PySide.QtGui.QCalendarWidget.selectedDate() properties are adjusted if the selection range becomes invalid
		If the provided date is not a valid PySide.QtCore.QDate object, the PySide.QtGui.QCalendarWidget.setMaximumDate() function does nothing.
		"""
		res = super(QCalendarWidget,self).setMaximumDate(date)
		return res
	#----------------------------------------------------------------------
	def setMinimumDate(self,date):
		"""
		setMinimumDate(date)
			date=QtCore.QDate

		This property holds the minimum date of the currently specified date range..
		The user will not be able to select a date that is before the currently set minimum date.
		By default, the minimum date is the earliest date that the PySide.QtCore.QDate class can handle.
		When setting a minimum date, the PySide.QtGui.QCalendarWidget.maximumDate() and PySide.QtGui.QCalendarWidget.selectedDate() properties are adjusted if the selection range becomes invalid
		If the provided date is not a valid PySide.QtCore.QDate object, the PySide.QtGui.QCalendarWidget.setMinimumDate() function does nothing.
		"""
		res = super(QCalendarWidget,self).setMinimumDate(date)
		return res
	#----------------------------------------------------------------------
	def setSelectionMode(self,mode):
		"""
		setSelectionMode(mode)
			mode=QtGui.QCalendarWidget.SelectionMode

		This property holds the type of selection the user can make in the calendar.
		When this property is set to SingleSelection , the user can select a date within the minimum and maximum allowed dates, using either the mouse or the keyboard.
		When the property is set to NoSelection , the user will be unable to select dates, but they can still be selected programmatically
		Note that the date that is selected when the property is set to NoSelection will still be the selected date of the calendar.
		The default value is SingleSelection .
		"""
		res = super(QCalendarWidget,self).setSelectionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setVerticalHeaderFormat(self,format):
		"""
		setVerticalHeaderFormat(format)
			format=QtGui.QCalendarWidget.VerticalHeaderFormat

		This property holds the format of the vertical header..
		The default value is QCalendarWidget::ISOWeekNumber.
		"""
		res = super(QCalendarWidget,self).setVerticalHeaderFormat(format)
		return res
	#----------------------------------------------------------------------
	def setWeekdayTextFormat(self,dayOfWeek,format):
		"""
		setWeekdayTextFormat(dayOfWeek,format)
			dayOfWeek=QtCore.Qt.DayOfWeek
			format=QtGui.QTextCharFormat


		"""
		res = super(QCalendarWidget,self).setWeekdayTextFormat(dayOfWeek,format)
		return res
	#----------------------------------------------------------------------
	def updateCell(self,date):
		"""
		updateCell(date)
			date=QtCore.QDate

		Updates the cell specified by the given date unless updates are disabled or the cell is hidden.
		"""
		res = super(QCalendarWidget,self).updateCell(date)
		return res
	#----------------------------------------------------------------------
	def weekdayTextFormat(self,dayOfWeek):
		"""
		weekdayTextFormat(dayOfWeek)
			dayOfWeek=QtCore.Qt.DayOfWeek


		"""
		res = super(QCalendarWidget,self).weekdayTextFormat(dayOfWeek)
		isinstance(res,QtGui.QTextCharFormat)
		return res
