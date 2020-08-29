from PySide import QtGui, QtCore

class QPageSetupDialog(QtGui.QPageSetupDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPageSetupDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def enabledOptions(self):
		"""
		Use PySide.QtGui.QPageSetupDialog.options() instead.
		"""
		res = super(QPageSetupDialog,self).enabledOptions()
		isinstance(res,QtGui.QPageSetupDialog.PageSetupDialogOptions)
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""
		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QPageSetupDialog,self).options()
		isinstance(res,QtGui.QPageSetupDialog.PageSetupDialogOptions)
		return res
	#----------------------------------------------------------------------
	def addEnabledOption(self,option):
		"""
		addEnabledOption(option)
			option=QtGui.QPageSetupDialog.PageSetupDialogOption

		Use setOption(option , true) instead.
		"""
		res = super(QPageSetupDialog,self).addEnabledOption(option)
		return res
	#----------------------------------------------------------------------
	def isOptionEnabled(self,option):
		"""
		isOptionEnabled(option)
			option=QtGui.QPageSetupDialog.PageSetupDialogOption

		Use testOption(option ) instead.
		"""
		res = super(QPageSetupDialog,self).isOptionEnabled(option)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QDialog.accepted() signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QPageSetupDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setEnabledOptions(self,options):
		"""
		setEnabledOptions(options)
			options=QtGui.QPageSetupDialog.PageSetupDialogOptions


		"""
		res = super(QPageSetupDialog,self).setEnabledOptions(options)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QPageSetupDialog.PageSetupDialogOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QPageSetupDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QPageSetupDialog.PageSetupDialogOptions

		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QPageSetupDialog,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QPageSetupDialog.PageSetupDialogOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QPageSetupDialog,self).testOption(option)
		isinstance(res,bool)
		return res
