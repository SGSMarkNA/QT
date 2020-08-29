from PySide import QtGui, QtCore

class QEvent(QtCore.QEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def accept(self):
		"""
		Sets the accept flag of the event object, the equivalent of calling setAccepted(true).
		Setting the accept parameter indicates that the event receiver wants the event
		Unwanted events might be propagated to the parent widget.
		"""
		res = super(QEvent,self).accept()
		return res
	#----------------------------------------------------------------------
	def ignore(self):
		"""
		Clears the accept flag parameter of the event object, the equivalent of calling setAccepted(false).
		Clearing the accept parameter indicates that the event receiver does not want the event
		Unwanted events might be propagated to the parent widget.
		"""
		res = super(QEvent,self).ignore()
		return res
	#----------------------------------------------------------------------
	def isAccepted(self):
		"""

		"""
		res = super(QEvent,self).isAccepted()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def spontaneous(self):
		"""
		Returns true if the event originated outside the application (a system event); otherwise returns false.
		The return value of this function is not defined for paint events.
		"""
		res = super(QEvent,self).spontaneous()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the event type.
		"""
		res = super(QEvent,self).type()
		isinstance(res,QtCore.QEvent.Type)
		return res
	#----------------------------------------------------------------------
	def setAccepted(self,accepted):
		"""
		setAccepted(accepted)
			accepted=QtCore.bool


		"""
		res = super(QEvent,self).setAccepted(accepted)
		return res
