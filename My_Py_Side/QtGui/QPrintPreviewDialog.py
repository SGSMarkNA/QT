from PySide import QtGui, QtCore

class QPrintPreviewDialog(QtGui.QPrintPreviewDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPrintPreviewDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def printer(self):
		"""
		Returns a pointer to the PySide.QtGui.QPrinter object this dialog is currently operating on.
		"""
		res = super(QPrintPreviewDialog,self).printer()
		isinstance(res,QtGui.QPrinter)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its finished(int) signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QPrintPreviewDialog,self).open(receiver,member)
		return res
