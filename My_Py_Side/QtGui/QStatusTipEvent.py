from PySide import QtGui, QtCore

class QStatusTipEvent(QtGui.QStatusTipEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStatusTipEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def tip(self):
		"""
		Returns the message to show in the status bar.
		"""
		res = super(QStatusTipEvent,self).tip()
		return res
