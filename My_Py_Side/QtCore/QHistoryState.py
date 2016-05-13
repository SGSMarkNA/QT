from PySide import QtGui, QtCore

class QHistoryState(QtCore.QHistoryState):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHistoryState,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def defaultState(self):
		"""
		This property holds the default state of this history state.
		"""
		res = super(QHistoryState,self).defaultState()
		isinstance(res,QtCore.QAbstractState)
		return res
	#----------------------------------------------------------------------
	def historyType(self):
		"""
		This property holds the type of history that this history state records.
		The default value of this property is QHistoryState.ShallowHistory .
		"""
		res = super(QHistoryState,self).historyType()
		isinstance(res,QtCore.QHistoryState.HistoryType)
		return res
	#----------------------------------------------------------------------
	def setDefaultState(self,state):
		"""
		setDefaultState(state)
			state=QtCore.QAbstractState

		This property holds the default state of this history state.
		"""
		res = super(QHistoryState,self).setDefaultState(state)
		return res
	#----------------------------------------------------------------------
	def setHistoryType(self,type):
		"""
		setHistoryType(type)
			type=QtCore.QHistoryState.HistoryType

		This property holds the type of history that this history state records.
		The default value of this property is QHistoryState.ShallowHistory .
		"""
		res = super(QHistoryState,self).setHistoryType(type)
		return res
