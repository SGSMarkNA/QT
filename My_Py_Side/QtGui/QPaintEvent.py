from PySide import QtGui, QtCore

class QPaintEvent(QtGui.QPaintEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPaintEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the rectangle that needs to be updated.
		"""
		res = super(QPaintEvent,self).rect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def region(self):
		"""
		Returns the region that needs to be updated.
		"""
		res = super(QPaintEvent,self).region()
		isinstance(res,QtGui.QRegion)
		return res
