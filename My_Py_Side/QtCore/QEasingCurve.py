from PySide import QtGui, QtCore

class QEasingCurve(QtCore.QEasingCurve):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QEasingCurve,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def amplitude(self):
		"""
		Returns the amplitude
		This is not applicable for all curve types
		It is only applicable for bounce and elastic curves (curves of PySide.QtCore.QEasingCurve.type() QEasingCurve.InBounce , QEasingCurve.OutBounce , QEasingCurve.InOutBounce , QEasingCurve.OutInBounce , QEasingCurve.InElastic , QEasingCurve.OutElastic , QEasingCurve.InOutElastic or QEasingCurve.OutInElastic ).
		"""
		res = super(QEasingCurve,self).amplitude()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def customType(self):
		"""

		"""
		res = super(QEasingCurve,self).customType()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def overshoot(self):
		"""
		Returns the overshoot
		This is not applicable for all curve types
		It is only applicable if PySide.QtCore.QEasingCurve.type() is QEasingCurve.InBack , QEasingCurve.OutBack , QEasingCurve.InOutBack or QEasingCurve.OutInBack .
		"""
		res = super(QEasingCurve,self).overshoot()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def period(self):
		"""
		Returns the period
		This is not applicable for all curve types
		It is only applicable if PySide.QtCore.QEasingCurve.type() is QEasingCurve.InElastic , QEasingCurve.OutElastic , QEasingCurve.InOutElastic or QEasingCurve.OutInElastic .
		"""
		res = super(QEasingCurve,self).period()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of the easing curve.
		"""
		res = super(QEasingCurve,self).type()
		isinstance(res,QtCore.QEasingCurve.Type)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QEasingCurve

		Compare this easing curve with other and returns true if they are not equal
		It will also compare the properties of a curve.
		"""
		res = super(QEasingCurve,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QEasingCurve

		Compare this easing curve with other and returns true if they are equal
		It will also compare the properties of a curve.
		"""
		res = super(QEasingCurve,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAmplitude(self,amplitude):
		"""
		setAmplitude(amplitude)
			amplitude=QtCore.qreal

		Sets the amplitude to amplitude .
		This will set the amplitude of the bounce or the amplitude of the elastic spring effect
		The higher the number, the higher the amplitude.
		"""
		res = super(QEasingCurve,self).setAmplitude(amplitude)
		return res
	#----------------------------------------------------------------------
	def setCustomType(self,arg__1):
		"""
		setCustomType(arg__1)
			arg__1=Object


		"""
		res = super(QEasingCurve,self).setCustomType(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOvershoot(self,overshoot):
		"""
		setOvershoot(overshoot)
			overshoot=QtCore.qreal

		Sets the overshoot to overshoot .
		0 produces no overshoot, and the default value of 1.70158 produces an overshoot of 10 percent.
		"""
		res = super(QEasingCurve,self).setOvershoot(overshoot)
		return res
	#----------------------------------------------------------------------
	def setPeriod(self,period):
		"""
		setPeriod(period)
			period=QtCore.qreal

		Sets the period to period
		Setting a small period value will give a high frequency of the curve
		A large period will give it a small frequency.
		"""
		res = super(QEasingCurve,self).setPeriod(period)
		return res
	#----------------------------------------------------------------------
	def setType(self,type):
		"""
		setType(type)
			type=QtCore.QEasingCurve.Type

		Sets the type of the easing curve to type .
		"""
		res = super(QEasingCurve,self).setType(type)
		return res
	#----------------------------------------------------------------------
	def valueForProgress(self,progress):
		"""
		valueForProgress(progress)
			progress=QtCore.qreal

		Return the effective progress for the easing curve at progress
		While progress must be between 0 and 1, the returned effective progress can be outside those bounds
		For instance, QEasingCurve.InBack will return negative values in the beginning of the function.
		"""
		res = super(QEasingCurve,self).valueForProgress(progress)
		isinstance(res,QtCore.qreal)
		return res
