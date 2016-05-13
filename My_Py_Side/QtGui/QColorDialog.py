from PySide import QtGui, QtCore

class QColorDialog(QtGui.QColorDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QColorDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentColor(self):
		"""
		This property holds the currently selected color in the dialog.
		"""
		res = super(QColorDialog,self).currentColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""
		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QColorDialog,self).options()
		isinstance(res,QtGui.QColorDialog.ColorDialogOptions)
		return res
	#----------------------------------------------------------------------
	def selectedColor(self):
		"""
		Returns the color that the user selected by clicking the OK or equivalent button.
		"""
		res = super(QColorDialog,self).selectedColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QColorDialog.colorSelected() signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QColorDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setCurrentColor(self,color):
		"""
		setCurrentColor(color)
			color=QtGui.QColor


		"""
		res = super(QColorDialog,self).setCurrentColor(color)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QColorDialog.ColorDialogOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QColorDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QColorDialog.ColorDialogOptions

		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QColorDialog,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QColorDialog.ColorDialogOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QColorDialog,self).testOption(option)
		isinstance(res,QtCore.bool)
		return res
