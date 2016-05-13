from PySide import QtGui, QtCore

class QDoubleSpinBox(QtGui.QDoubleSpinBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDoubleSpinBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cleanText(self):
		"""
		This property holds the text of the spin box excluding any prefix, suffix, or leading or trailing whitespace..
		"""
		res = super(QDoubleSpinBox,self).cleanText()
		return res
	#----------------------------------------------------------------------
	def decimals(self):
		"""
		This property holds the precision of the spin box, in decimals.
		Sets how many decimals the spinbox will use for displaying and interpreting doubles.
		Note: The maximum, minimum and value might change as a result of changing this property.
		"""
		res = super(QDoubleSpinBox,self).decimals()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maximum(self):
		"""
		This property holds the maximum value of the spin box.
		When setting this property the PySide.QtGui.QDoubleSpinBox.minimum() is adjusted if necessary, to ensure that the range remains valid.
		The default maximum value is 99.99.
		Note: The maximum value will be rounded to match the decimals property.
		"""
		res = super(QDoubleSpinBox,self).maximum()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def minimum(self):
		"""
		This property holds the minimum value of the spin box.
		When setting this property the PySide.QtGui.QDoubleSpinBox.maximum() is adjusted if necessary to ensure that the range remains valid.
		The default minimum value is 0.0.
		Note: The minimum value will be rounded to match the decimals property.
		"""
		res = super(QDoubleSpinBox,self).minimum()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def prefix(self):
		"""
		This property holds the spin boxs prefix.
		The prefix is prepended to the start of the displayed value
		Typical use is to display a unit of measurement or a currency symbol
		For example:
		To turn off the prefix display, set this property to an empty string
		The default is no prefix
		The prefix is not displayed when PySide.QtGui.QDoubleSpinBox.value() == PySide.QtGui.QDoubleSpinBox.minimum() and PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no prefix is set, PySide.QtGui.QDoubleSpinBox.prefix() returns an empty string.
		"""
		res = super(QDoubleSpinBox,self).prefix()
		return res
	#----------------------------------------------------------------------
	def singleStep(self):
		"""
		This property holds the step value.
		When the user uses the arrows to change the spin boxs value the value will be incremented/decremented by the amount of the PySide.QtGui.QDoubleSpinBox.singleStep()
		The default value is 1.0
		Setting a PySide.QtGui.QDoubleSpinBox.singleStep() value of less than 0 does nothing.
		"""
		res = super(QDoubleSpinBox,self).singleStep()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def suffix(self):
		"""
		This property holds the suffix of the spin box.
		The suffix is appended to the end of the displayed value
		Typical use is to display a unit of measurement or a currency symbol
		For example:
		To turn off the suffix display, set this property to an empty string
		The default is no suffix
		The suffix is not displayed for the PySide.QtGui.QDoubleSpinBox.minimum() if PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no suffix is set, PySide.QtGui.QDoubleSpinBox.suffix() returns an empty string.
		"""
		res = super(QDoubleSpinBox,self).suffix()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the value of the spin box.
		PySide.QtGui.QDoubleSpinBox.setValue() will emit PySide.QtGui.QDoubleSpinBox.valueChanged() if the new value is different from the old one.
		Note: The value will be rounded so it can be displayed with the current setting of decimals.
		"""
		res = super(QDoubleSpinBox,self).value()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def setDecimals(self,prec):
		"""
		setDecimals(prec)
			prec=QtCore.int

		This property holds the precision of the spin box, in decimals.
		Sets how many decimals the spinbox will use for displaying and interpreting doubles.
		Note: The maximum, minimum and value might change as a result of changing this property.
		"""
		res = super(QDoubleSpinBox,self).setDecimals(prec)
		return res
	#----------------------------------------------------------------------
	def setMaximum(self,max):
		"""
		setMaximum(max)
			max=QtCore.double

		This property holds the maximum value of the spin box.
		When setting this property the PySide.QtGui.QDoubleSpinBox.minimum() is adjusted if necessary, to ensure that the range remains valid.
		The default maximum value is 99.99.
		Note: The maximum value will be rounded to match the decimals property.
		"""
		res = super(QDoubleSpinBox,self).setMaximum(max)
		return res
	#----------------------------------------------------------------------
	def setMinimum(self,min):
		"""
		setMinimum(min)
			min=QtCore.double

		This property holds the minimum value of the spin box.
		When setting this property the PySide.QtGui.QDoubleSpinBox.maximum() is adjusted if necessary to ensure that the range remains valid.
		The default minimum value is 0.0.
		Note: The minimum value will be rounded to match the decimals property.
		"""
		res = super(QDoubleSpinBox,self).setMinimum(min)
		return res
	#----------------------------------------------------------------------
	def setPrefix(self,prefix):
		"""
		setPrefix(prefix)
			prefix=unicode

		This property holds the spin boxs prefix.
		The prefix is prepended to the start of the displayed value
		Typical use is to display a unit of measurement or a currency symbol
		For example:
		To turn off the prefix display, set this property to an empty string
		The default is no prefix
		The prefix is not displayed when PySide.QtGui.QDoubleSpinBox.value() == PySide.QtGui.QDoubleSpinBox.minimum() and PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no prefix is set, PySide.QtGui.QDoubleSpinBox.prefix() returns an empty string.
		"""
		res = super(QDoubleSpinBox,self).setPrefix(prefix)
		return res
	#----------------------------------------------------------------------
	def setRange(self,min,max):
		"""
		setRange(min,max)
			min=QtCore.double
			max=QtCore.double

		Convenience function to set the minimum and maximum values with a single function call.
		Note: The maximum and minimum values will be rounded to match the decimals property.
		is equivalent to:
		"""
		res = super(QDoubleSpinBox,self).setRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setSingleStep(self,val):
		"""
		setSingleStep(val)
			val=QtCore.double

		This property holds the step value.
		When the user uses the arrows to change the spin boxs value the value will be incremented/decremented by the amount of the PySide.QtGui.QDoubleSpinBox.singleStep()
		The default value is 1.0
		Setting a PySide.QtGui.QDoubleSpinBox.singleStep() value of less than 0 does nothing.
		"""
		res = super(QDoubleSpinBox,self).setSingleStep(val)
		return res
	#----------------------------------------------------------------------
	def setSuffix(self,suffix):
		"""
		setSuffix(suffix)
			suffix=unicode

		This property holds the suffix of the spin box.
		The suffix is appended to the end of the displayed value
		Typical use is to display a unit of measurement or a currency symbol
		For example:
		To turn off the suffix display, set this property to an empty string
		The default is no suffix
		The suffix is not displayed for the PySide.QtGui.QDoubleSpinBox.minimum() if PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no suffix is set, PySide.QtGui.QDoubleSpinBox.suffix() returns an empty string.
		"""
		res = super(QDoubleSpinBox,self).setSuffix(suffix)
		return res
	#----------------------------------------------------------------------
	def textFromValue(self,val):
		"""
		textFromValue(val)
			val=QtCore.double

		This virtual function is used by the spin box whenever it needs to display the given value
		The default implementation returns a string containing value printed using QWidget.locale() .toString(value , QLatin1Char (f), PySide.QtGui.QDoubleSpinBox.decimals() ) and will remove the thousand separator
		Reimplementations may return anything.
		Note: PySide.QtGui.QDoubleSpinBox does not call this function for PySide.QtGui.QAbstractSpinBox.specialValueText() and that neither PySide.QtGui.QDoubleSpinBox.prefix() nor PySide.QtGui.QDoubleSpinBox.suffix() should be included in the return value.
		If you reimplement this, you may also need to reimplement PySide.QtGui.QDoubleSpinBox.valueFromText() .
		"""
		res = super(QDoubleSpinBox,self).textFromValue(val)
		return res
	#----------------------------------------------------------------------
	def valueFromText(self,text):
		"""
		valueFromText(text)
			text=unicode

		This virtual function is used by the spin box whenever it needs to interpret text entered by the user as a value.
		Subclasses that need to display spin box values in a non-numeric way need to reimplement this function.
		Note: PySide.QtGui.QDoubleSpinBox handles PySide.QtGui.QAbstractSpinBox.specialValueText() separately; this function is only concerned with the other values.
		"""
		res = super(QDoubleSpinBox,self).valueFromText(text)
		isinstance(res,QtCore.double)
		return res
