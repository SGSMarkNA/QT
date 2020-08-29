from PySide import QtGui, QtCore

class QSocketNotifier(QtCore.QSocketNotifier):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSocketNotifier,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		Returns true if the notifier is enabled; otherwise returns false.
		"""
		res = super(QSocketNotifier,self).isEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def socket(self):
		"""
		Returns the socket identifier specified to the constructor.
		"""
		res = super(QSocketNotifier,self).socket()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the socket event type specified to the constructor.
		"""
		res = super(QSocketNotifier,self).type()
		isinstance(res,QtCore.QSocketNotifier.Type)
		return res
