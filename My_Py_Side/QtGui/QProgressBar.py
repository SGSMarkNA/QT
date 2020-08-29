from PySide import QtGui, QtCore

class QProgressBar(QtGui.QProgressBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QProgressBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the progress bar.
		"""
		res = super(QProgressBar,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		This property holds the string used to generate the current text.
		%p - is replaced by the percentage completed
		%v - is replaced by the current value
		%m - is replaced by the total number of steps.
		The default value is %p%.
		"""
		res = super(QProgressBar,self).format()
		return res
	#----------------------------------------------------------------------
	def invertedAppearance(self):
		"""
		This property holds whether or not a progress bar shows its progress inverted.
		If this property is false, the progress bar grows in the other direction (e.g
		from right to left)
		By default, the progress bar is not inverted.
		"""
		res = super(QProgressBar,self).invertedAppearance()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTextVisible(self):
		"""
		This property holds whether the current completed percentage should be displayed.
		This property may be ignored by the style (e.g., QMacStyle never draws the text).
		"""
		res = super(QProgressBar,self).isTextVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def maximum(self):
		"""
		This property holds the progress bars maximum value.
		When setting this property, the PySide.QtGui.QProgressBar.minimum() is adjusted if necessary to ensure that the range remains valid
		If the current value falls outside the new range, the progress bar is reset with PySide.QtGui.QProgressBar.reset() .
		"""
		res = super(QProgressBar,self).maximum()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minimum(self):
		"""
		This property holds the progress bars minimum value.
		When setting this property, the PySide.QtGui.QProgressBar.maximum() is adjusted if necessary to ensure that the range remains valid
		If the current value falls outside the new range, the progress bar is reset with PySide.QtGui.QProgressBar.reset() .
		"""
		res = super(QProgressBar,self).minimum()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the progress bar.
		The orientation must be Qt.Horizontal (the default) or Qt.Vertical .
		"""
		res = super(QProgressBar,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the descriptive text shown with the progress bar.
		The text returned is the same as the text displayed in the center (or in some styles, to the left) of the progress bar.
		The progress shown in the text may be smaller than the minimum value, indicating that the progress bar is in the reset state before any progress is set.
		In the default implementation, the text either contains a percentage value that indicates the progress so far, or it is blank because the progress bar is in the reset state.
		"""
		res = super(QProgressBar,self).text()
		return res
	#----------------------------------------------------------------------
	def textDirection(self):
		"""
		This property holds the reading direction of the PySide.QtGui.QProgressBar.text() for vertical progress bars.
		This property has no impact on horizontal progress bars
		By default, the reading direction is QProgressBar.TopToBottom .
		"""
		res = super(QProgressBar,self).textDirection()
		isinstance(res,QtGui.QProgressBar.Direction)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the progress bars current value.
		Attempting to change the current value to one outside the minimum-maximum range has no effect on the current value.
		"""
		res = super(QProgressBar,self).value()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionProgressBar

		Initialize option with the values from this PySide.QtGui.QProgressBar
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionProgressBar or PySide.QtGui.QStyleOptionProgressBarV2 , but dont want to fill in all the information themselves
		This function will check the version of the PySide.QtGui.QStyleOptionProgressBar and fill in the additional values for a PySide.QtGui.QStyleOptionProgressBarV2 .
		"""
		res = super(QProgressBar,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,alignment):
		"""
		setAlignment(alignment)
			alignment=QtCore.Qt.Alignment

		This property holds the alignment of the progress bar.
		"""
		res = super(QProgressBar,self).setAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=unicode

		This property holds the string used to generate the current text.
		%p - is replaced by the percentage completed
		%v - is replaced by the current value
		%m - is replaced by the total number of steps.
		The default value is %p%.
		"""
		res = super(QProgressBar,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setInvertedAppearance(self,invert):
		"""
		setInvertedAppearance(invert)
			invert=QtCore.bool

		This property holds whether or not a progress bar shows its progress inverted.
		If this property is false, the progress bar grows in the other direction (e.g
		from right to left)
		By default, the progress bar is not inverted.
		"""
		res = super(QProgressBar,self).setInvertedAppearance(invert)
		return res
	#----------------------------------------------------------------------
	def setTextDirection(self,textDirection):
		"""
		setTextDirection(textDirection)
			textDirection=QtGui.QProgressBar.Direction

		This property holds the reading direction of the PySide.QtGui.QProgressBar.text() for vertical progress bars.
		This property has no impact on horizontal progress bars
		By default, the reading direction is QProgressBar.TopToBottom .
		"""
		res = super(QProgressBar,self).setTextDirection(textDirection)
		return res
	#----------------------------------------------------------------------
	def setTextVisible(self,visible):
		"""
		setTextVisible(visible)
			visible=QtCore.bool

		This property holds whether the current completed percentage should be displayed.
		This property may be ignored by the style (e.g., QMacStyle never draws the text).
		"""
		res = super(QProgressBar,self).setTextVisible(visible)
		return res
