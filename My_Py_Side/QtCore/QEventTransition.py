from PySide import QtGui, QtCore

class QEventTransition(QtCore.QEventTransition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QEventTransition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def eventSource(self):
		"""
		This property holds the event source that this event transition is associated with.
		"""
		res = super(QEventTransition,self).eventSource()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def eventType(self):
		"""
		This property holds the type of event that this event transition is associated with.
		"""
		res = super(QEventTransition,self).eventType()
		isinstance(res,QtCore.QEvent.Type)
		return res
	#----------------------------------------------------------------------
	def setEventSource(self,object):
		"""
		setEventSource(object)
			object=QtCore.QObject

		This property holds the event source that this event transition is associated with.
		"""
		res = super(QEventTransition,self).setEventSource(object)
		return res
	#----------------------------------------------------------------------
	def setEventType(self,type):
		"""
		setEventType(type)
			type=QtCore.QEvent.Type

		This property holds the type of event that this event transition is associated with.
		"""
		res = super(QEventTransition,self).setEventType(type)
		return res
