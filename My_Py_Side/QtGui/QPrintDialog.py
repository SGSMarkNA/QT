from PySide import QtGui, QtCore

class QPrintDialog(QtGui.QPrintDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPrintDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def options(self):
		"""
		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QPrintDialog,self).options()
		isinstance(res,QtGui.QAbstractPrintDialog.PrintDialogOptions)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QPrintDialog.accepted() signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QPrintDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QAbstractPrintDialog.PrintDialogOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QPrintDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QAbstractPrintDialog.PrintDialogOptions

		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QPrintDialog,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QAbstractPrintDialog.PrintDialogOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QPrintDialog,self).testOption(option)
		isinstance(res,bool)
		return res
