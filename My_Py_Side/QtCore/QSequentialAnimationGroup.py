from PySide import QtGui, QtCore

class QSequentialAnimationGroup(QtCore.QSequentialAnimationGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSequentialAnimationGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentAnimation(self):
		"""
		Returns the animation in the current time.
		"""
		res = super(QSequentialAnimationGroup,self).currentAnimation()
		isinstance(res,QtCore.QAbstractAnimation)
		return res
	#----------------------------------------------------------------------
	def addPause(self,msecs):
		"""
		addPause(msecs)
			msecs=QtCore.int

		Adds a pause of msecs to this animation group
		The pause is considered as a special type of animation, thus PySide.QtCore.QAnimationGroup.animationCount() will be increased by one.
		"""
		res = super(QSequentialAnimationGroup,self).addPause(msecs)
		isinstance(res,QtCore.QPauseAnimation)
		return res
	#----------------------------------------------------------------------
	def insertPause(self,index,msecs):
		"""
		insertPause(index,msecs)
			index=QtCore.int
			msecs=QtCore.int

		Inserts a pause of msecs milliseconds at index in this animation group.
		"""
		res = super(QSequentialAnimationGroup,self).insertPause(index,msecs)
		isinstance(res,QtCore.QPauseAnimation)
		return res
