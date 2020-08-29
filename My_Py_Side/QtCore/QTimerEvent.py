from PySide import QtGui, QtCore

class QTimerEvent(QtCore.QTimerEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTimerEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def timerId(self):
		"""
		Returns the unique timer identifier, which is the same identifier as returned from QObject.startTimer() .
		"""
		res = super(QTimerEvent,self).timerId()
		isinstance(res,int)
		return res
