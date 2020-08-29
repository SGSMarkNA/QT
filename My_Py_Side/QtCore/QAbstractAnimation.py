from PySide import QtGui, QtCore

class QAbstractAnimation(QtCore.QAbstractAnimation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractAnimation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentLoop(self):
		"""
		This property holds the current loop of the animation.
		This property describes the current loop of the animation
		By default, the animations loop count is 1, and so the current loop will always be 0
		If the loop count is 2 and the animation runs past its duration, it will automatically rewind and restart at current time 0, and current loop 1, and so on.
		When the current loop changes, PySide.QtCore.QAbstractAnimation emits the PySide.QtCore.QAbstractAnimation.currentLoopChanged() signal.
		"""
		res = super(QAbstractAnimation,self).currentLoop()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentLoopTime(self):
		"""
		Returns the current time inside the current loop
		It can go from 0 to PySide.QtCore.QAbstractAnimation.duration() .
		"""
		res = super(QAbstractAnimation,self).currentLoopTime()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentTime(self):
		"""
		This property holds the current time and progress of the animation.
		This property describes the animations current time
		You can change the current time by calling setCurrentTime, or you can call PySide.QtCore.QAbstractAnimation.start() and let the animation run, setting the current time automatically as the animation progresses.
		The animations current time starts at 0, and ends at PySide.QtCore.QAbstractAnimation.totalDuration() .
		"""
		res = super(QAbstractAnimation,self).currentTime()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def direction(self):
		"""
		This property holds the direction of the animation when it is in Running state..
		This direction indicates whether the time moves from 0 towards the animation duration, or from the value of the duration and towards 0 after PySide.QtCore.QAbstractAnimation.start() has been called.
		By default, this property is set to Forward .
		"""
		res = super(QAbstractAnimation,self).direction()
		isinstance(res,QtCore.QAbstractAnimation.Direction)
		return res
	#----------------------------------------------------------------------
	def duration(self):
		"""
		This property holds the duration of the animation..
		If the duration is -1, it means that the duration is undefined
		In this case, PySide.QtCore.QAbstractAnimation.loopCount() is ignored.
		"""
		res = super(QAbstractAnimation,self).duration()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QAbstractAnimation,self).finished()
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		If this animation is part of a PySide.QtCore.QAnimationGroup , this function returns a pointer to the group; otherwise, it returns 0.
		"""
		res = super(QAbstractAnimation,self).group()
		isinstance(res,QtCore.QAnimationGroup)
		return res
	#----------------------------------------------------------------------
	def loopCount(self):
		"""
		This property holds the loop count of the animation.
		This property describes the loop count of the animation as an integer
		By default this value is 1, indicating that the animation should run once only, and then stop
		By changing it you can let the animation loop several times
		With a value of 0, the animation will not run at all, and with a value of -1, the animation will loop forever until stopped
		It is not supported to have loop on an animation that has an undefined duration
		It will only run once.
		"""
		res = super(QAbstractAnimation,self).loopCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		This property holds state of the animation..
		This property describes the current state of the animation
		When the animation state changes, PySide.QtCore.QAbstractAnimation emits the PySide.QtCore.QAbstractAnimation.stateChanged() signal.
		"""
		res = super(QAbstractAnimation,self).state()
		isinstance(res,QtCore.QAbstractAnimation.State)
		return res
	#----------------------------------------------------------------------
	def totalDuration(self):
		"""
		Returns the total and effective duration of the animation, including the loop count.
		"""
		res = super(QAbstractAnimation,self).totalDuration()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setDirection(self,direction):
		"""
		setDirection(direction)
			direction=QtCore.QAbstractAnimation.Direction

		This property holds the direction of the animation when it is in Running state..
		This direction indicates whether the time moves from 0 towards the animation duration, or from the value of the duration and towards 0 after PySide.QtCore.QAbstractAnimation.start() has been called.
		By default, this property is set to Forward .
		"""
		res = super(QAbstractAnimation,self).setDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setLoopCount(self,loopCount):
		"""
		setLoopCount(loopCount)
			loopCount=QtCore.int

		This property holds the loop count of the animation.
		This property describes the loop count of the animation as an integer
		By default this value is 1, indicating that the animation should run once only, and then stop
		By changing it you can let the animation loop several times
		With a value of 0, the animation will not run at all, and with a value of -1, the animation will loop forever until stopped
		It is not supported to have loop on an animation that has an undefined duration
		It will only run once.
		"""
		res = super(QAbstractAnimation,self).setLoopCount(loopCount)
		return res
	#----------------------------------------------------------------------
	def updateCurrentTime(self,currentTime):
		"""
		updateCurrentTime(currentTime)
			currentTime=QtCore.int

		This pure virtual function is called every time the animations currentTime changes.
		"""
		res = super(QAbstractAnimation,self).updateCurrentTime(currentTime)
		return res
	#----------------------------------------------------------------------
	def updateDirection(self,direction):
		"""
		updateDirection(direction)
			direction=QtCore.QAbstractAnimation.Direction


		"""
		res = super(QAbstractAnimation,self).updateDirection(direction)
		return res
	#----------------------------------------------------------------------
	def updateState(self,newState,oldState):
		"""
		updateState(newState,oldState)
			newState=QtCore.QAbstractAnimation.State
			oldState=QtCore.QAbstractAnimation.State


		"""
		res = super(QAbstractAnimation,self).updateState(newState,oldState)
		return res
