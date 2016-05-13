from PySide import QtGui, QtCore

class QAbstractPageSetupDialog(QtGui.QAbstractPageSetupDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractPageSetupDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def printer(self):
		"""
		Returns the printer that this page setup dialog is operating on.
		"""
		res = super(QAbstractPageSetupDialog,self).printer()
		isinstance(res,QtGui.QPrinter)
		return res
