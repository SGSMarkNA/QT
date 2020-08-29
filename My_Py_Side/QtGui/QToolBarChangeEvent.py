from PySide import QtGui, QtCore

class QToolBarChangeEvent(QtGui.QToolBarChangeEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QToolBarChangeEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def toggle(self):
		"""

		"""
		res = super(QToolBarChangeEvent,self).toggle()
		isinstance(res,bool)
		return res
