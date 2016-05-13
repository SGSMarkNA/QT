from PySide import QtGui, QtCore

class QSpinBox(QtGui.QSpinBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSpinBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cleanText(self):
		"""
		This property holds the text of the spin box excluding any prefix, suffix, or leading or trailing whitespace..
		"""
		res = super(QSpinBox,self).cleanText()
		return res
	#----------------------------------------------------------------------
	def maximum(self):
		"""
		This property holds the maximum value of the spin box.
		When setting this property the PySide.QtGui.QSpinBox.minimum() is adjusted if necessary, to ensure that the range remains valid.
		The default maximum value is 99.
		"""
		res = super(QSpinBox,self).maximum()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minimum(self):
		"""
		This property holds the minimum value of the spin box.
		When setting this property the PySide.QtGui.QSpinBox.maximum() is adjusted if necessary to ensure that the range remains valid.
		The default minimum value is 0.
		"""
		res = super(QSpinBox,self).minimum()
		isinstance(res,QtCore.int)
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
		The prefix is not displayed when PySide.QtGui.QSpinBox.value() == PySide.QtGui.QSpinBox.minimum() and PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no prefix is set, PySide.QtGui.QSpinBox.prefix() returns an empty string.
		"""
		res = super(QSpinBox,self).prefix()
		return res
	#----------------------------------------------------------------------
	def singleStep(self):
		"""
		This property holds the step value.
		When the user uses the arrows to change the spin boxs value the value will be incremented/decremented by the amount of the PySide.QtGui.QSpinBox.singleStep()
		The default value is 1
		Setting a PySide.QtGui.QSpinBox.singleStep() value of less than 0 does nothing.
		"""
		res = super(QSpinBox,self).singleStep()
		isinstance(res,QtCore.int)
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
		The suffix is not displayed for the PySide.QtGui.QSpinBox.minimum() if PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no suffix is set, PySide.QtGui.QSpinBox.suffix() returns an empty string.
		"""
		res = super(QSpinBox,self).suffix()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the value of the spin box.
		PySide.QtGui.QSpinBox.setValue() will emit PySide.QtGui.QSpinBox.valueChanged() if the new value is different from the old one.
		"""
		res = super(QSpinBox,self).value()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setMaximum(self,max):
		"""
		setMaximum(max)
			max=QtCore.int

		This property holds the maximum value of the spin box.
		When setting this property the PySide.QtGui.QSpinBox.minimum() is adjusted if necessary, to ensure that the range remains valid.
		The default maximum value is 99.
		"""
		res = super(QSpinBox,self).setMaximum(max)
		return res
	#----------------------------------------------------------------------
	def setMinimum(self,min):
		"""
		setMinimum(min)
			min=QtCore.int

		This property holds the minimum value of the spin box.
		When setting this property the PySide.QtGui.QSpinBox.maximum() is adjusted if necessary to ensure that the range remains valid.
		The default minimum value is 0.
		"""
		res = super(QSpinBox,self).setMinimum(min)
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
		The prefix is not displayed when PySide.QtGui.QSpinBox.value() == PySide.QtGui.QSpinBox.minimum() and PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no prefix is set, PySide.QtGui.QSpinBox.prefix() returns an empty string.
		"""
		res = super(QSpinBox,self).setPrefix(prefix)
		return res
	#----------------------------------------------------------------------
	def setRange(self,min,max):
		"""
		setRange(min,max)
			min=QtCore.int
			max=QtCore.int

		Convenience function to set the minimum , and maximum values with a single function call.
		is equivalent to:
		"""
		res = super(QSpinBox,self).setRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setSingleStep(self,val):
		"""
		setSingleStep(val)
			val=QtCore.int

		This property holds the step value.
		When the user uses the arrows to change the spin boxs value the value will be incremented/decremented by the amount of the PySide.QtGui.QSpinBox.singleStep()
		The default value is 1
		Setting a PySide.QtGui.QSpinBox.singleStep() value of less than 0 does nothing.
		"""
		res = super(QSpinBox,self).setSingleStep(val)
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
		The suffix is not displayed for the PySide.QtGui.QSpinBox.minimum() if PySide.QtGui.QAbstractSpinBox.specialValueText() is set.
		If no suffix is set, PySide.QtGui.QSpinBox.suffix() returns an empty string.
		"""
		res = super(QSpinBox,self).setSuffix(suffix)
		return res
	#----------------------------------------------------------------------
	def textFromValue(self,val):
		"""
		textFromValue(val)
			val=QtCore.int

		This virtual function is used by the spin box whenever it needs to display the given value
		The default implementation returns a string containing value printed in the standard way using QWidget.locale()
		toString() , but with the thousand separator removed
		Reimplementations may return anything
		(See the example in the detailed description.)
		Note: PySide.QtGui.QSpinBox does not call this function for PySide.QtGui.QAbstractSpinBox.specialValueText() and that neither PySide.QtGui.QSpinBox.prefix() nor PySide.QtGui.QSpinBox.suffix() should be included in the return value.
		If you reimplement this, you may also need to reimplement PySide.QtGui.QSpinBox.valueFromText() and PySide.QtGui.QSpinBox.validate()
		"""
		res = super(QSpinBox,self).textFromValue(val)
		return res
	#----------------------------------------------------------------------
	def valueFromText(self,text):
		"""
		valueFromText(text)
			text=unicode

		This virtual function is used by the spin box whenever it needs to interpret text entered by the user as a value.
		Subclasses that need to display spin box values in a non-numeric way need to reimplement this function.
		Note: PySide.QtGui.QSpinBox handles PySide.QtGui.QAbstractSpinBox.specialValueText() separately; this function is only concerned with the other values.
		"""
		res = super(QSpinBox,self).valueFromText(text)
		isinstance(res,QtCore.int)
		return res
