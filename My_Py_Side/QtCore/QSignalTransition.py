from PySide import QtGui, QtCore

class QSignalTransition(QtCore.QSignalTransition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSignalTransition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def senderObject(self):
		"""
		This property holds the sender object that this signal transition is associated with.
		"""
		res = super(QSignalTransition,self).senderObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def signal(self):
		"""
		This property holds the signal that this signal transition is associated with.
		"""
		res = super(QSignalTransition,self).signal()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setSenderObject(self,sender):
		"""
		setSenderObject(sender)
			sender=QtCore.QObject

		This property holds the sender object that this signal transition is associated with.
		"""
		res = super(QSignalTransition,self).setSenderObject(sender)
		return res
	#----------------------------------------------------------------------
	def setSignal(self,signal):
		"""
		setSignal(signal)
			signal=QtCore.QByteArray

		This property holds the signal that this signal transition is associated with.
		"""
		res = super(QSignalTransition,self).setSignal(signal)
		return res
