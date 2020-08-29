from PySide import QtGui, QtCore

class QTimeLine(QtCore.QTimeLine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTimeLine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentFrame(self):
		"""
		Returns the frame corresponding to the current time.
		"""
		res = super(QTimeLine,self).currentFrame()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentTime(self):
		"""
		This property holds the current time of the time line..
		When PySide.QtCore.QTimeLine is in Running state, this value is updated continuously as a function of the duration and direction of the timeline
		Otherwise, it is value that was current when PySide.QtCore.QTimeLine.stop() was called last, or the value set by PySide.QtCore.QTimeLine.setCurrentTime() .
		By default, this property contains a value of 0.
		"""
		res = super(QTimeLine,self).currentTime()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentValue(self):
		"""
		Returns the value corresponding to the current time.
		"""
		res = super(QTimeLine,self).currentValue()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def curveShape(self):
		"""
		This property holds the shape of the timeline curve..
		The curve shape describes the relation between the time and value for the base implementation of PySide.QtCore.QTimeLine.valueForTime() .
		If you have reimplemented PySide.QtCore.QTimeLine.valueForTime() , this value is ignored.
		By default, this property is set to EaseInOutCurve .
		"""
		res = super(QTimeLine,self).curveShape()
		isinstance(res,QtCore.QTimeLine.CurveShape)
		return res
	#----------------------------------------------------------------------
	def direction(self):
		"""
		This property holds the direction of the timeline when PySide.QtCore.QTimeLine is in Running state..
		This direction indicates whether the time moves from 0 towards the timeline duration, or from the value of the duration and towards 0 after PySide.QtCore.QTimeLine.start() has been called.
		By default, this property is set to Forward .
		"""
		res = super(QTimeLine,self).direction()
		isinstance(res,QtCore.QTimeLine.Direction)
		return res
	#----------------------------------------------------------------------
	def duration(self):
		"""
		This property holds the total duration of the timeline in milliseconds..
		By default, this value is 1000 (i.e., 1 second), but you can change this by either passing a duration to PySide.QtCore.QTimeLine s constructor, or by calling PySide.QtCore.QTimeLine.setDuration()
		The duration must be larger than 0.
		"""
		res = super(QTimeLine,self).duration()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def easingCurve(self):
		"""
		Specifies the easing curve that the timeline will use
		If both easing curve and PySide.QtCore.QTimeLine.curveShape() are set, the last set property will override the previous one
		(If PySide.QtCore.QTimeLine.valueForTime() is reimplemented it will override both)
		"""
		res = super(QTimeLine,self).easingCurve()
		isinstance(res,QtCore.QEasingCurve)
		return res
	#----------------------------------------------------------------------
	def endFrame(self):
		"""
		Returns the end frame, which is the frame corresponding to the end of the timeline (i.e., the frame for which the current value is 1).
		"""
		res = super(QTimeLine,self).endFrame()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QTimeLine,self).finished()
		return res
	#----------------------------------------------------------------------
	def loopCount(self):
		"""
		This property holds the number of times the timeline should loop before its finished..
		A loop count of of 0 means that the timeline will loop forever.
		By default, this property contains a value of 1.
		"""
		res = super(QTimeLine,self).loopCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def startFrame(self):
		"""
		Returns the start frame, which is the frame corresponding to the start of the timeline (i.e., the frame for which the current value is 0).
		"""
		res = super(QTimeLine,self).startFrame()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the state of the timeline.
		"""
		res = super(QTimeLine,self).state()
		isinstance(res,QtCore.QTimeLine.State)
		return res
	#----------------------------------------------------------------------
	def updateInterval(self):
		"""
		This property holds the time in milliseconds between each time PySide.QtCore.QTimeLine updates its current time..
		When updating the current time, PySide.QtCore.QTimeLine will emit PySide.QtCore.QTimeLine.valueChanged() if the current value changed, and PySide.QtCore.QTimeLine.frameChanged() if the frame changed.
		By default, the interval is 40 ms, which corresponds to a rate of 25 updates per second.
		"""
		res = super(QTimeLine,self).updateInterval()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def frameForTime(self,msec):
		"""
		frameForTime(msec)
			msec=QtCore.int

		Returns the frame corresponding to the time msec
		This value is calculated using a linear interpolation of the start and end frame, based on the value returned by PySide.QtCore.QTimeLine.valueForTime() .
		"""
		res = super(QTimeLine,self).frameForTime(msec)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setCurveShape(self,shape):
		"""
		setCurveShape(shape)
			shape=QtCore.QTimeLine.CurveShape

		This property holds the shape of the timeline curve..
		The curve shape describes the relation between the time and value for the base implementation of PySide.QtCore.QTimeLine.valueForTime() .
		If you have reimplemented PySide.QtCore.QTimeLine.valueForTime() , this value is ignored.
		By default, this property is set to EaseInOutCurve .
		"""
		res = super(QTimeLine,self).setCurveShape(shape)
		return res
	#----------------------------------------------------------------------
	def setDirection(self,direction):
		"""
		setDirection(direction)
			direction=QtCore.QTimeLine.Direction

		This property holds the direction of the timeline when PySide.QtCore.QTimeLine is in Running state..
		This direction indicates whether the time moves from 0 towards the timeline duration, or from the value of the duration and towards 0 after PySide.QtCore.QTimeLine.start() has been called.
		By default, this property is set to Forward .
		"""
		res = super(QTimeLine,self).setDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setDuration(self,duration):
		"""
		setDuration(duration)
			duration=QtCore.int

		This property holds the total duration of the timeline in milliseconds..
		By default, this value is 1000 (i.e., 1 second), but you can change this by either passing a duration to PySide.QtCore.QTimeLine s constructor, or by calling PySide.QtCore.QTimeLine.setDuration()
		The duration must be larger than 0.
		"""
		res = super(QTimeLine,self).setDuration(duration)
		return res
	#----------------------------------------------------------------------
	def setEasingCurve(self,curve):
		"""
		setEasingCurve(curve)
			curve=QtCore.QEasingCurve

		Specifies the easing curve that the timeline will use
		If both easing curve and PySide.QtCore.QTimeLine.curveShape() are set, the last set property will override the previous one
		(If PySide.QtCore.QTimeLine.valueForTime() is reimplemented it will override both)
		"""
		res = super(QTimeLine,self).setEasingCurve(curve)
		return res
	#----------------------------------------------------------------------
	def setEndFrame(self,frame):
		"""
		setEndFrame(frame)
			frame=QtCore.int

		Sets the end frame, which is the frame corresponding to the end of the timeline (i.e., the frame for which the current value is 1), to frame .
		"""
		res = super(QTimeLine,self).setEndFrame(frame)
		return res
	#----------------------------------------------------------------------
	def setFrameRange(self,startFrame,endFrame):
		"""
		setFrameRange(startFrame,endFrame)
			startFrame=QtCore.int
			endFrame=QtCore.int

		Sets the timelines frame counter to start at startFrame , and end and endFrame
		For each time value, PySide.QtCore.QTimeLine will find the corresponding frame when you call PySide.QtCore.QTimeLine.currentFrame() or PySide.QtCore.QTimeLine.frameForTime() by interpolating, using the return value of PySide.QtCore.QTimeLine.valueForTime() .
		When in Running state, PySide.QtCore.QTimeLine also emits the PySide.QtCore.QTimeLine.frameChanged() signal when the frame changes.
		"""
		res = super(QTimeLine,self).setFrameRange(startFrame,endFrame)
		return res
	#----------------------------------------------------------------------
	def setLoopCount(self,count):
		"""
		setLoopCount(count)
			count=QtCore.int

		This property holds the number of times the timeline should loop before its finished..
		A loop count of of 0 means that the timeline will loop forever.
		By default, this property contains a value of 1.
		"""
		res = super(QTimeLine,self).setLoopCount(count)
		return res
	#----------------------------------------------------------------------
	def setStartFrame(self,frame):
		"""
		setStartFrame(frame)
			frame=QtCore.int

		Sets the start frame, which is the frame corresponding to the start of the timeline (i.e., the frame for which the current value is 0), to frame .
		"""
		res = super(QTimeLine,self).setStartFrame(frame)
		return res
	#----------------------------------------------------------------------
	def setUpdateInterval(self,interval):
		"""
		setUpdateInterval(interval)
			interval=QtCore.int

		This property holds the time in milliseconds between each time PySide.QtCore.QTimeLine updates its current time..
		When updating the current time, PySide.QtCore.QTimeLine will emit PySide.QtCore.QTimeLine.valueChanged() if the current value changed, and PySide.QtCore.QTimeLine.frameChanged() if the frame changed.
		By default, the interval is 40 ms, which corresponds to a rate of 25 updates per second.
		"""
		res = super(QTimeLine,self).setUpdateInterval(interval)
		return res
	#----------------------------------------------------------------------
	def valueForTime(self,msec):
		"""
		valueForTime(msec)
			msec=QtCore.int

		Returns the timeline value for the time msec
		The returned value, which varies depending on the curve shape, is always between 0 and 1
		If msec is 0, the default implementation always returns 0.
		Reimplement this function to provide a custom curve shape for your timeline.
		"""
		res = super(QTimeLine,self).valueForTime(msec)
		isinstance(res,QtCore.qreal)
		return res
