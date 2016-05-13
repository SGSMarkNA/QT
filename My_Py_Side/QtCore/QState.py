from PySide import QtGui, QtCore

class QState(QtCore.QState):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QState,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childMode(self):
		"""
		This property holds the child mode of this state.
		The default value of this property is QState.ExclusiveStates .
		"""
		res = super(QState,self).childMode()
		isinstance(res,QtCore.QState.ChildMode)
		return res
	#----------------------------------------------------------------------
	def errorState(self):
		"""
		This property holds the error state of this state.
		"""
		res = super(QState,self).errorState()
		isinstance(res,QtCore.QAbstractState)
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QState,self).finished()
		return res
	#----------------------------------------------------------------------
	def initialState(self):
		"""
		This property holds the initial state of this state (one of its child states).
		"""
		res = super(QState,self).initialState()
		isinstance(res,QtCore.QAbstractState)
		return res
	#----------------------------------------------------------------------
	def propertiesAssigned(self):
		"""

		"""
		res = super(QState,self).propertiesAssigned()
		return res
	#----------------------------------------------------------------------
	def transitions(self):
		"""
		Returns this states outgoing transitions (i.e
		transitions where this state is the source state ), or an empty list if this state has no outgoing transitions.
		"""
		res = super(QState,self).transitions()
		return res
	#----------------------------------------------------------------------
	def addTransition(self,*args,**kwargs):
		"""
		addTransition(transition)
			transition=QtCore.QAbstractTransition

		addTransition(arg__1,arg__2)
			arg__1=Object
			arg__2=QtCore.QAbstractState

		addTransition(sender,signal,target)
			sender=QtCore.QObject
			signal=str
			target=QtCore.QAbstractState

		addTransition(target)
			target=QtCore.QAbstractState

		Adds the given transition
		The transition has this state as the source
		This state takes ownership of the transition.
		"""
		res = super(QState,self).addTransition(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def assignProperty(self,object,name,value):
		"""
		assignProperty(object,name,value)
			object=QtCore.QObject
			name=str
			value=object

		Instructs this state to set the property with the given name of the given object to the given value when the state is entered.
		"""
		res = super(QState,self).assignProperty(object,name,value)
		return res
	#----------------------------------------------------------------------
	def removeTransition(self,transition):
		"""
		removeTransition(transition)
			transition=QtCore.QAbstractTransition

		Removes the given transition from this state
		The state releases ownership of the transition.
		"""
		res = super(QState,self).removeTransition(transition)
		return res
	#----------------------------------------------------------------------
	def setChildMode(self,mode):
		"""
		setChildMode(mode)
			mode=QtCore.QState.ChildMode

		This property holds the child mode of this state.
		The default value of this property is QState.ExclusiveStates .
		"""
		res = super(QState,self).setChildMode(mode)
		return res
	#----------------------------------------------------------------------
	def setErrorState(self,state):
		"""
		setErrorState(state)
			state=QtCore.QAbstractState

		This property holds the error state of this state.
		"""
		res = super(QState,self).setErrorState(state)
		return res
	#----------------------------------------------------------------------
	def setInitialState(self,state):
		"""
		setInitialState(state)
			state=QtCore.QAbstractState

		This property holds the initial state of this state (one of its child states).
		"""
		res = super(QState,self).setInitialState(state)
		return res
