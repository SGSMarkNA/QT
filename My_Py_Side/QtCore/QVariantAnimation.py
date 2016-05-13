from PySide import QtGui, QtCore

class QVariantAnimation(QtCore.QVariantAnimation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QVariantAnimation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentValue(self):
		"""
		This property holds the current value of the animation..
		This property describes the current value; an interpolated value between the start value and the end value , using the current time for progress
		The value itself is obtained from PySide.QtCore.QVariantAnimation.interpolated() , which is called repeatedly as the animation is running.
		PySide.QtCore.QVariantAnimation calls the virtual PySide.QtCore.QVariantAnimation.updateCurrentValue() function when the current value changes
		This is particularly useful for subclasses that need to track updates
		For example, PySide.QtCore.QPropertyAnimation uses this function to animate Qt properties .
		"""
		res = super(QVariantAnimation,self).currentValue()
		return res
	#----------------------------------------------------------------------
	def easingCurve(self):
		"""
		This property holds the easing curve of the animation.
		This property defines the easing curve of the animation
		By default, a linear easing curve is used, resulting in linear interpolation
		Other curves are provided, for instance, QEasingCurve.InCirc , which provides a circular entry curve
		Another example is QEasingCurve.InOutElastic , which provides an elastic effect on the values of the interpolated variant.
		PySide.QtCore.QVariantAnimation will use the QEasingCurve.valueForProgress() to transform the normalized progress ( PySide.QtCore.QAbstractAnimation.currentTime() / totalDuration) of the animation into the effective progress actually used by the animation
		It is this effective progress that will be the progress when PySide.QtCore.QVariantAnimation.interpolated() is called
		Also, the steps in the keyValues are referring to this effective progress.
		The easing curve is used with the interpolator, the PySide.QtCore.QVariantAnimation.interpolated() virtual function, the animations duration, and iterationCount, to control how the current value changes as the animation progresses.
		"""
		res = super(QVariantAnimation,self).easingCurve()
		isinstance(res,QtCore.QEasingCurve)
		return res
	#----------------------------------------------------------------------
	def endValue(self):
		"""
		This property holds the end value of the animation.
		This property describes the end value of the animation.
		"""
		res = super(QVariantAnimation,self).endValue()
		return res
	#----------------------------------------------------------------------
	def keyValues(self):
		"""
		Returns the key frames of this animation.
		"""
		res = super(QVariantAnimation,self).keyValues()
		return res
	#----------------------------------------------------------------------
	def startValue(self):
		"""
		This property holds the optional start value of the animation.
		This property describes the optional start value of the animation
		If omitted, or if a null PySide.QtCore.QVariant is assigned as the start value, the animation will use the current position of the end when the animation is started.
		"""
		res = super(QVariantAnimation,self).startValue()
		return res
	#----------------------------------------------------------------------
	def interpolated(self,from,to,progress):
		"""
		interpolated(from,to,progress)
			from=object
			to=object
			progress=QtCore.qreal

		This virtual function returns the linear interpolation between variants from and to , at progress , usually a value between 0 and 1
		You can reimplement this function in a subclass of PySide.QtCore.QVariantAnimation to provide your own interpolation algorithm.
		Note that in order for the interpolation to work with a PySide.QtCore.QEasingCurve that return a value smaller than 0 or larger than 1 (such as QEasingCurve.InBack ) you should make sure that it can extrapolate
		If the semantic of the datatype does not allow extrapolation this function should handle that gracefully.
		You should call the PySide.QtCore.QVariantAnimation implementation of this function if you want your class to handle the types already supported by Qt (see class PySide.QtCore.QVariantAnimation description for a list of supported types).
		"""
		res = super(QVariantAnimation,self).interpolated(from,to,progress)
		return res
	#----------------------------------------------------------------------
	def keyValueAt(self,step):
		"""
		keyValueAt(step)
			step=QtCore.qreal

		Returns the key frame value for the given step
		The given step must be in the range 0 to 1
		If there is no KeyValue for step , it returns an invalid PySide.QtCore.QVariant .
		"""
		res = super(QVariantAnimation,self).keyValueAt(step)
		return res
	#----------------------------------------------------------------------
	def setDuration(self,msecs):
		"""
		setDuration(msecs)
			msecs=QtCore.int

		This property holds the duration of the animation.
		This property describes the duration in milliseconds of the animation
		The default duration is 250 milliseconds.
		"""
		res = super(QVariantAnimation,self).setDuration(msecs)
		return res
	#----------------------------------------------------------------------
	def setEasingCurve(self,easing):
		"""
		setEasingCurve(easing)
			easing=QtCore.QEasingCurve

		This property holds the easing curve of the animation.
		This property defines the easing curve of the animation
		By default, a linear easing curve is used, resulting in linear interpolation
		Other curves are provided, for instance, QEasingCurve.InCirc , which provides a circular entry curve
		Another example is QEasingCurve.InOutElastic , which provides an elastic effect on the values of the interpolated variant.
		PySide.QtCore.QVariantAnimation will use the QEasingCurve.valueForProgress() to transform the normalized progress ( PySide.QtCore.QAbstractAnimation.currentTime() / totalDuration) of the animation into the effective progress actually used by the animation
		It is this effective progress that will be the progress when PySide.QtCore.QVariantAnimation.interpolated() is called
		Also, the steps in the keyValues are referring to this effective progress.
		The easing curve is used with the interpolator, the PySide.QtCore.QVariantAnimation.interpolated() virtual function, the animations duration, and iterationCount, to control how the current value changes as the animation progresses.
		"""
		res = super(QVariantAnimation,self).setEasingCurve(easing)
		return res
	#----------------------------------------------------------------------
	def setEndValue(self,value):
		"""
		setEndValue(value)
			value=object

		This property holds the end value of the animation.
		This property describes the end value of the animation.
		"""
		res = super(QVariantAnimation,self).setEndValue(value)
		return res
	#----------------------------------------------------------------------
	def setKeyValueAt(self,step,value):
		"""
		setKeyValueAt(step,value)
			step=QtCore.qreal
			value=object

		Creates a key frame at the given step with the given value
		The given step must be in the range 0 to 1.
		"""
		res = super(QVariantAnimation,self).setKeyValueAt(step,value)
		return res
	#----------------------------------------------------------------------
	def setKeyValues(self,values):
		"""
		setKeyValues(values)
			values=unKnown


		"""
		res = super(QVariantAnimation,self).setKeyValues(values)
		return res
	#----------------------------------------------------------------------
	def setStartValue(self,value):
		"""
		setStartValue(value)
			value=object

		This property holds the optional start value of the animation.
		This property describes the optional start value of the animation
		If omitted, or if a null PySide.QtCore.QVariant is assigned as the start value, the animation will use the current position of the end when the animation is started.
		"""
		res = super(QVariantAnimation,self).setStartValue(value)
		return res
	#----------------------------------------------------------------------
	def updateCurrentValue(self,value):
		"""
		updateCurrentValue(value)
			value=object

		This pure virtual function is called every time the animations current value changes
		The value argument is the new current value.
		"""
		res = super(QVariantAnimation,self).updateCurrentValue(value)
		return res
