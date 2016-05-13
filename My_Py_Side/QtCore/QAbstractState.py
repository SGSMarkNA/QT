from PySide import QtGui, QtCore

class QAbstractState(QtCore.QAbstractState):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractState,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def entered(self):
		"""

		"""
		res = super(QAbstractState,self).entered()
		return res
	#----------------------------------------------------------------------
	def exited(self):
		"""

		"""
		res = super(QAbstractState,self).exited()
		return res
	#----------------------------------------------------------------------
	def machine(self):
		"""
		Returns the state machine that this state is part of, or 0 if the state is not part of a state machine.
		"""
		res = super(QAbstractState,self).machine()
		isinstance(res,QtCore.QStateMachine)
		return res
	#----------------------------------------------------------------------
	def parentState(self):
		"""
		Returns this states parent state, or 0 if the state has no parent state.
		"""
		res = super(QAbstractState,self).parentState()
		isinstance(res,QtCore.QState)
		return res
	#----------------------------------------------------------------------
	def onEntry(self,event):
		"""
		onEntry(event)
			event=QtCore.QEvent

		This function is called when the state is entered
		The given event is what caused the state to be entered
		Reimplement this function to perform custom processing when the state is entered.
		"""
		res = super(QAbstractState,self).onEntry(event)
		return res
	#----------------------------------------------------------------------
	def onExit(self,event):
		"""
		onExit(event)
			event=QtCore.QEvent

		This function is called when the state is exited
		The given event is what caused the state to be exited
		Reimplement this function to perform custom processing when the state is exited.
		"""
		res = super(QAbstractState,self).onExit(event)
		return res
