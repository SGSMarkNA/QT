from PySide import QtGui, QtCore

class QCoreApplication(QtCore.QCoreApplication):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCoreApplication,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aboutToQuit(self):
		"""

		"""
		res = super(QCoreApplication,self).aboutToQuit()
		return res
	#----------------------------------------------------------------------
	def init(self):
		"""

		"""
		res = super(QCoreApplication,self).init()
		return res
	#----------------------------------------------------------------------
	def notify(self,arg__1,arg__2):
		"""
		notify(arg__1,arg__2)
			arg__1=QtCore.QObject
			arg__2=QtCore.QEvent

		Sends event to receiver : receiver ->event(event )
		Returns the value that is returned from the receivers event handler
		Note that this function is called for all events sent to any object in any thread.
		For certain types of events (e.g
		mouse and key events), the event will be propagated to the receivers parent and so on up to the top-level object if the receiver is not interested in the event (i.e., it returns false).
		There are five different ways that events can be processed; reimplementing this virtual function is just one of them
		All five approaches are listed below:
		"""
		res = super(QCoreApplication,self).notify(arg__1,arg__2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def notifyInternal(self,receiver,event):
		"""
		notifyInternal(receiver,event)
			receiver=QtCore.QObject
			event=QtCore.QEvent


		"""
		res = super(QCoreApplication,self).notifyInternal(receiver,event)
		isinstance(res,QtCore.bool)
		return res
