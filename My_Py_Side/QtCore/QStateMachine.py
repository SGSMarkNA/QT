from PySide import QtGui, QtCore

class QStateMachine(QtCore.QStateMachine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStateMachine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def event(self):
		"""
		Returns a clone of the original event.
		"""
		res = super(QStateMachine,self).event()
		isinstance(res,QtCore.QEvent)
		return res
	#----------------------------------------------------------------------
	def object(self):
		"""
		Returns the object that the event is associated with.
		"""
		res = super(QStateMachine,self).object()
		isinstance(res,QtCore.QObject)
		return res
