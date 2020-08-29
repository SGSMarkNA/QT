from PySide import QtGui, QtCore

class QAnimationGroup(QtCore.QAnimationGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAnimationGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def animationCount(self):
		"""
		Returns the number of animations managed by this group.
		"""
		res = super(QAnimationGroup,self).animationCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes and deletes all animations in this animation group, and resets the current time to 0.
		"""
		res = super(QAnimationGroup,self).clear()
		return res
	#----------------------------------------------------------------------
	def addAnimation(self,animation):
		"""
		addAnimation(animation)
			animation=QtCore.QAbstractAnimation

		Adds animation to this group
		This will call insertAnimation with index equals to PySide.QtCore.QAnimationGroup.animationCount() .
		"""
		res = super(QAnimationGroup,self).addAnimation(animation)
		return res
	#----------------------------------------------------------------------
	def animationAt(self,index):
		"""
		animationAt(index)
			index=QtCore.int

		Returns a pointer to the animation at index in this group
		This function is useful when you need access to a particular animation
		index is between 0 and PySide.QtCore.QAnimationGroup.animationCount() - 1.
		"""
		res = super(QAnimationGroup,self).animationAt(index)
		isinstance(res,QtCore.QAbstractAnimation)
		return res
	#----------------------------------------------------------------------
	def indexOfAnimation(self,animation):
		"""
		indexOfAnimation(animation)
			animation=QtCore.QAbstractAnimation

		Returns the index of animation
		The returned index can be passed to the other functions that take an index as an argument.
		"""
		res = super(QAnimationGroup,self).indexOfAnimation(animation)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insertAnimation(self,index,animation):
		"""
		insertAnimation(index,animation)
			index=QtCore.int
			animation=QtCore.QAbstractAnimation

		Inserts animation into this animation group at index
		If index is 0 the animation is inserted at the beginning
		If index is PySide.QtCore.QAnimationGroup.animationCount() , the animation is inserted at the end.
		"""
		res = super(QAnimationGroup,self).insertAnimation(index,animation)
		return res
	#----------------------------------------------------------------------
	def removeAnimation(self,animation):
		"""
		removeAnimation(animation)
			animation=QtCore.QAbstractAnimation

		Removes animation from this group
		The ownership of animation is transferred to the caller.
		"""
		res = super(QAnimationGroup,self).removeAnimation(animation)
		return res
	#----------------------------------------------------------------------
	def takeAnimation(self,index):
		"""
		takeAnimation(index)
			index=QtCore.int

		Returns the animation at index and removes it from the animation group.
		"""
		res = super(QAnimationGroup,self).takeAnimation(index)
		isinstance(res,QtCore.QAbstractAnimation)
		return res
