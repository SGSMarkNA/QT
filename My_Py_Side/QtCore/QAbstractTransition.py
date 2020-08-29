from PySide import QtGui, QtCore

class QAbstractTransition(QtCore.QAbstractTransition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractTransition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def animations(self):
		"""
		Returns the list of animations associated with this transition, or an empty list if it has no animations.
		"""
		res = super(QAbstractTransition,self).animations()
		return res
	#----------------------------------------------------------------------
	def machine(self):
		"""
		Returns the state machine that this transition is part of, or 0 if the transition is not part of a state machine.
		"""
		res = super(QAbstractTransition,self).machine()
		isinstance(res,QtCore.QStateMachine)
		return res
	#----------------------------------------------------------------------
	def sourceState(self):
		"""
		This property holds the source state (parent) of this transition.
		"""
		res = super(QAbstractTransition,self).sourceState()
		isinstance(res,QtCore.QState)
		return res
	#----------------------------------------------------------------------
	def targetState(self):
		"""
		This property holds the target state of this transition.
		If a transition has no target state, the transition may still be triggered, but this will not cause the state machines configuration to change (i.e
		the current state will not be exited and re-entered).
		"""
		res = super(QAbstractTransition,self).targetState()
		isinstance(res,QtCore.QAbstractState)
		return res
	#----------------------------------------------------------------------
	def targetStates(self):
		"""
		This property holds the target states of this transition.
		If multiple states are specified, all must be descendants of the same parallel group state.
		"""
		res = super(QAbstractTransition,self).targetStates()
		return res
	#----------------------------------------------------------------------
	def triggered(self):
		"""

		"""
		res = super(QAbstractTransition,self).triggered()
		return res
	#----------------------------------------------------------------------
	def addAnimation(self,animation):
		"""
		addAnimation(animation)
			animation=QtCore.QAbstractAnimation

		Adds the given animation to this transition
		The transition does not take ownership of the animation.
		"""
		res = super(QAbstractTransition,self).addAnimation(animation)
		return res
	#----------------------------------------------------------------------
	def eventTest(self,event):
		"""
		eventTest(event)
			event=QtCore.QEvent

		This function is called to determine whether the given event should cause this transition to trigger
		Reimplement this function and return true if the event should trigger the transition, otherwise return false.
		"""
		res = super(QAbstractTransition,self).eventTest(event)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def onTransition(self,event):
		"""
		onTransition(event)
			event=QtCore.QEvent

		This function is called when the transition is triggered
		The given event is what caused the transition to trigger
		Reimplement this function to perform custom processing when the transition is triggered.
		"""
		res = super(QAbstractTransition,self).onTransition(event)
		return res
	#----------------------------------------------------------------------
	def removeAnimation(self,animation):
		"""
		removeAnimation(animation)
			animation=QtCore.QAbstractAnimation

		Removes the given animation from this transition.
		"""
		res = super(QAbstractTransition,self).removeAnimation(animation)
		return res
	#----------------------------------------------------------------------
	def setTargetState(self,target):
		"""
		setTargetState(target)
			target=QtCore.QAbstractState

		This property holds the target state of this transition.
		If a transition has no target state, the transition may still be triggered, but this will not cause the state machines configuration to change (i.e
		the current state will not be exited and re-entered).
		"""
		res = super(QAbstractTransition,self).setTargetState(target)
		return res
	#----------------------------------------------------------------------
	def setTargetStates(self,targets):
		"""
		setTargetStates(targets)
			targets=unKnown

		This property holds the target states of this transition.
		If multiple states are specified, all must be descendants of the same parallel group state.
		"""
		res = super(QAbstractTransition,self).setTargetStates(targets)
		return res
