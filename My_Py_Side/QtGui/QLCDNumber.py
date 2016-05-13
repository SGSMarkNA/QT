from PySide import QtGui, QtCore

class QLCDNumber(QtGui.QLCDNumber):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLCDNumber,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def digitCount(self):
		"""
		This property holds the current number of digits displayed.
		Corresponds to the current number of digits
		If QLCDNumber.smallDecimalPoint is false, the decimal point occupies one digit position.
		By default, this property contains a value of 5.
		"""
		res = super(QLCDNumber,self).digitCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def intValue(self):
		"""
		This property holds the displayed value rounded to the nearest integer.
		This property corresponds to the nearest integer to the current value displayed by the LCDNumber
		This is the value used for hexadecimal, octal and binary modes.
		If the displayed value is not a number, the property has a value of 0.
		By default, this property contains a value of 0.
		"""
		res = super(QLCDNumber,self).intValue()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def mode(self):
		"""
		This property holds the current display mode (number base).
		Corresponds to the current display mode, which is one of Bin , Oct , Dec (the default) and Hex
		Dec mode can display floating point values, the other modes display the integer equivalent.
		"""
		res = super(QLCDNumber,self).mode()
		isinstance(res,QtGui.QLCDNumber.Mode)
		return res
	#----------------------------------------------------------------------
	def numDigits(self):
		"""
		This property holds the current number of digits displayed.
		"""
		res = super(QLCDNumber,self).numDigits()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def overflow(self):
		"""

		"""
		res = super(QLCDNumber,self).overflow()
		return res
	#----------------------------------------------------------------------
	def segmentStyle(self):
		"""
		This property holds the style of the LCDNumber.
		Outline and Filled will additionally use QPalette.light() and QPalette.dark() for shadow effects.
		"""
		res = super(QLCDNumber,self).segmentStyle()
		isinstance(res,QtGui.QLCDNumber.SegmentStyle)
		return res
	#----------------------------------------------------------------------
	def smallDecimalPoint(self):
		"""
		This property holds the style of the decimal point.
		If true the decimal point is drawn between two digit positions
		Otherwise it occupies a digit position of its own, i.e
		is drawn in a digit position
		The default is false.
		The inter-digit space is made slightly wider when the decimal point is drawn between the digits.
		"""
		res = super(QLCDNumber,self).smallDecimalPoint()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the displayed value.
		This property corresponds to the current value displayed by the LCDNumber.
		If the displayed value is not a number, the property has a value of 0.
		By default, this property contains a value of 0.
		"""
		res = super(QLCDNumber,self).value()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def checkOverflow(self,*args,**kwargs):
		"""
		checkOverflow(num)
			num=QtCore.double

		checkOverflow(num)
			num=QtCore.int

		Returns true if num is too big to be displayed in its entirety; otherwise returns false.
		"""
		res = super(QLCDNumber,self).checkOverflow(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setDigitCount(self,nDigits):
		"""
		setDigitCount(nDigits)
			nDigits=QtCore.int

		This property holds the current number of digits displayed.
		Corresponds to the current number of digits
		If QLCDNumber.smallDecimalPoint is false, the decimal point occupies one digit position.
		By default, this property contains a value of 5.
		"""
		res = super(QLCDNumber,self).setDigitCount(nDigits)
		return res
	#----------------------------------------------------------------------
	def setMode(self,arg__1):
		"""
		setMode(arg__1)
			arg__1=QtGui.QLCDNumber.Mode

		This property holds the current display mode (number base).
		Corresponds to the current display mode, which is one of Bin , Oct , Dec (the default) and Hex
		Dec mode can display floating point values, the other modes display the integer equivalent.
		"""
		res = super(QLCDNumber,self).setMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNumDigits(self,nDigits):
		"""
		setNumDigits(nDigits)
			nDigits=QtCore.int

		This property holds the current number of digits displayed.
		"""
		res = super(QLCDNumber,self).setNumDigits(nDigits)
		return res
	#----------------------------------------------------------------------
	def setSegmentStyle(self,arg__1):
		"""
		setSegmentStyle(arg__1)
			arg__1=QtGui.QLCDNumber.SegmentStyle

		This property holds the style of the LCDNumber.
		Outline and Filled will additionally use QPalette.light() and QPalette.dark() for shadow effects.
		"""
		res = super(QLCDNumber,self).setSegmentStyle(arg__1)
		return res
