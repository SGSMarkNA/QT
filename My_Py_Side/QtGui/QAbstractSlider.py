from PySide import QtGui, QtCore

class QAbstractSlider(QtGui.QAbstractSlider):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractSlider,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hasTracking(self):
		"""
		This property holds whether slider tracking is enabled.
		If tracking is enabled (the default), the slider emits the PySide.QtGui.QAbstractSlider.valueChanged() signal while the slider is being dragged
		If tracking is disabled, the slider emits the PySide.QtGui.QAbstractSlider.valueChanged() signal only when the user releases the slider.
		"""
		res = super(QAbstractSlider,self).hasTracking()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def invertedAppearance(self):
		"""
		This property holds whether or not a slider shows its values inverted..
		If this property is false (the default), the minimum and maximum will be shown in its classic position for the inherited widget
		If the value is true, the minimum and maximum appear at their opposite location.
		Note: This property makes most sense for sliders and dials
		For scroll bars, the visual effect of the scroll bar subcontrols depends on whether or not the styles understand inverted appearance; most styles ignore this property for scroll bars.
		"""
		res = super(QAbstractSlider,self).invertedAppearance()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def invertedControls(self):
		"""
		This property holds whether or not the slider inverts its wheel and key events..
		If this property is false, scrolling the mouse wheel up and using keys like page up will increase the sliders value towards its maximum
		Otherwise pressing page up will move value towards the sliders minimum.
		"""
		res = super(QAbstractSlider,self).invertedControls()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSliderDown(self):
		"""
		This property holds whether the slider is pressed down..
		The property is set by subclasses in order to let the abstract slider know whether or not tracking() has any effect.
		Changing the slider down property emits the PySide.QtGui.QAbstractSlider.sliderPressed() and PySide.QtGui.QAbstractSlider.sliderReleased() signals.
		"""
		res = super(QAbstractSlider,self).isSliderDown()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def maximum(self):
		"""
		This property holds the sliders maximum value.
		When setting this property, the PySide.QtGui.QAbstractSlider.minimum() is adjusted if necessary to ensure that the range remains valid
		Also the sliders current value is adjusted to be within the new range.
		"""
		res = super(QAbstractSlider,self).maximum()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minimum(self):
		"""
		This property holds the sliderss minimum value.
		When setting this property, the PySide.QtGui.QAbstractSlider.maximum() is adjusted if necessary to ensure that the range remains valid
		Also the sliders current value is adjusted to be within the new range.
		"""
		res = super(QAbstractSlider,self).minimum()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the slider.
		The orientation must be Qt.Vertical (the default) or Qt.Horizontal .
		"""
		res = super(QAbstractSlider,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def pageStep(self):
		"""
		This property holds the page step..
		The larger of two natural steps that an abstract slider provides and typically corresponds to the user pressing PageUp or PageDown.
		"""
		res = super(QAbstractSlider,self).pageStep()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def repeatAction(self):
		"""
		Returns the current repeat action.
		"""
		res = super(QAbstractSlider,self).repeatAction()
		isinstance(res,QtGui.QAbstractSlider.SliderAction)
		return res
	#----------------------------------------------------------------------
	def singleStep(self):
		"""
		This property holds the single step..
		The smaller of two natural steps that an abstract sliders provides and typically corresponds to the user pressing an arrow key.
		If the property is modified during an auto repeating key event, behavior is undefined.
		"""
		res = super(QAbstractSlider,self).singleStep()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sliderPosition(self):
		"""
		This property holds the current slider position.
		If tracking() is enabled (the default), this is identical to PySide.QtGui.QAbstractSlider.value() .
		"""
		res = super(QAbstractSlider,self).sliderPosition()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sliderPressed(self):
		"""

		"""
		res = super(QAbstractSlider,self).sliderPressed()
		return res
	#----------------------------------------------------------------------
	def sliderReleased(self):
		"""

		"""
		res = super(QAbstractSlider,self).sliderReleased()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the sliders current value.
		The slider forces the value to be within the legal range: PySide.QtGui.QAbstractSlider.minimum() <= value <= PySide.QtGui.QAbstractSlider.maximum() .
		Changing the value also changes the PySide.QtGui.QAbstractSlider.sliderPosition() .
		"""
		res = super(QAbstractSlider,self).value()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setInvertedAppearance(self,arg__1):
		"""
		setInvertedAppearance(arg__1)
			arg__1=QtCore.bool

		This property holds whether or not a slider shows its values inverted..
		If this property is false (the default), the minimum and maximum will be shown in its classic position for the inherited widget
		If the value is true, the minimum and maximum appear at their opposite location.
		Note: This property makes most sense for sliders and dials
		For scroll bars, the visual effect of the scroll bar subcontrols depends on whether or not the styles understand inverted appearance; most styles ignore this property for scroll bars.
		"""
		res = super(QAbstractSlider,self).setInvertedAppearance(arg__1)
		return res
	#----------------------------------------------------------------------
	def setInvertedControls(self,arg__1):
		"""
		setInvertedControls(arg__1)
			arg__1=QtCore.bool

		This property holds whether or not the slider inverts its wheel and key events..
		If this property is false, scrolling the mouse wheel up and using keys like page up will increase the sliders value towards its maximum
		Otherwise pressing page up will move value towards the sliders minimum.
		"""
		res = super(QAbstractSlider,self).setInvertedControls(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMaximum(self,arg__1):
		"""
		setMaximum(arg__1)
			arg__1=QtCore.int

		This property holds the sliders maximum value.
		When setting this property, the PySide.QtGui.QAbstractSlider.minimum() is adjusted if necessary to ensure that the range remains valid
		Also the sliders current value is adjusted to be within the new range.
		"""
		res = super(QAbstractSlider,self).setMaximum(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMinimum(self,arg__1):
		"""
		setMinimum(arg__1)
			arg__1=QtCore.int

		This property holds the sliderss minimum value.
		When setting this property, the PySide.QtGui.QAbstractSlider.maximum() is adjusted if necessary to ensure that the range remains valid
		Also the sliders current value is adjusted to be within the new range.
		"""
		res = super(QAbstractSlider,self).setMinimum(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPageStep(self,arg__1):
		"""
		setPageStep(arg__1)
			arg__1=QtCore.int

		This property holds the page step..
		The larger of two natural steps that an abstract slider provides and typically corresponds to the user pressing PageUp or PageDown.
		"""
		res = super(QAbstractSlider,self).setPageStep(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRange(self,min,max):
		"""
		setRange(min,max)
			min=QtCore.int
			max=QtCore.int

		Sets the sliders minimum to min and its maximum to max .
		If max is smaller than min , min becomes the only legal value.
		"""
		res = super(QAbstractSlider,self).setRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setRepeatAction(self,action,thresholdTime=None,repeatTime=None):
		"""
		setRepeatAction(action,thresholdTime=None,repeatTime=None)
			action=QtGui.QAbstractSlider.SliderAction
			thresholdTime=QtCore.int
			repeatTime=QtCore.int

		Sets action action to be triggered repetitively in intervals of repeatTime , after an initial delay of thresholdTime .
		"""
		res = super(QAbstractSlider,self).setRepeatAction(action,thresholdTime,repeatTime)
		return res
	#----------------------------------------------------------------------
	def setSingleStep(self,arg__1):
		"""
		setSingleStep(arg__1)
			arg__1=QtCore.int

		This property holds the single step..
		The smaller of two natural steps that an abstract sliders provides and typically corresponds to the user pressing an arrow key.
		If the property is modified during an auto repeating key event, behavior is undefined.
		"""
		res = super(QAbstractSlider,self).setSingleStep(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSliderDown(self,arg__1):
		"""
		setSliderDown(arg__1)
			arg__1=QtCore.bool

		This property holds whether the slider is pressed down..
		The property is set by subclasses in order to let the abstract slider know whether or not tracking() has any effect.
		Changing the slider down property emits the PySide.QtGui.QAbstractSlider.sliderPressed() and PySide.QtGui.QAbstractSlider.sliderReleased() signals.
		"""
		res = super(QAbstractSlider,self).setSliderDown(arg__1)
		return res
	#----------------------------------------------------------------------
	def setSliderPosition(self,arg__1):
		"""
		setSliderPosition(arg__1)
			arg__1=QtCore.int

		This property holds the current slider position.
		If tracking() is enabled (the default), this is identical to PySide.QtGui.QAbstractSlider.value() .
		"""
		res = super(QAbstractSlider,self).setSliderPosition(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTracking(self,enable):
		"""
		setTracking(enable)
			enable=QtCore.bool

		This property holds whether slider tracking is enabled.
		If tracking is enabled (the default), the slider emits the PySide.QtGui.QAbstractSlider.valueChanged() signal while the slider is being dragged
		If tracking is disabled, the slider emits the PySide.QtGui.QAbstractSlider.valueChanged() signal only when the user releases the slider.
		"""
		res = super(QAbstractSlider,self).setTracking(enable)
		return res
	#----------------------------------------------------------------------
	def sliderChange(self,change):
		"""
		sliderChange(change)
			change=QtGui.QAbstractSlider.SliderChange

		Reimplement this virtual function to track slider changes such as SliderRangeChange , SliderOrientationChange , SliderStepsChange , or SliderValueChange
		The default implementation only updates the display and ignores the change parameter.
		"""
		res = super(QAbstractSlider,self).sliderChange(change)
		return res
	#----------------------------------------------------------------------
	def triggerAction(self,action):
		"""
		triggerAction(action)
			action=QtGui.QAbstractSlider.SliderAction

		Triggers a slider action
		Possible actions are SliderSingleStepAdd , SliderSingleStepSub , SliderPageStepAdd , SliderPageStepSub , SliderToMinimum , SliderToMaximum , and SliderMove .
		"""
		res = super(QAbstractSlider,self).triggerAction(action)
		return res
