from PySide import QtGui, QtCore

class QFontDialog(QtGui.QFontDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentFont(self):
		"""
		This property holds the current font of the dialog..
		"""
		res = super(QFontDialog,self).currentFont()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""
		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QFontDialog,self).options()
		isinstance(res,QtGui.QFontDialog.FontDialogOptions)
		return res
	#----------------------------------------------------------------------
	def selectedFont(self):
		"""
		Returns the font that the user selected by clicking the OK or equivalent button.
		"""
		res = super(QFontDialog,self).selectedFont()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QFontDialog.fontSelected() signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QFontDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setCurrentFont(self,font):
		"""
		setCurrentFont(font)
			font=QtGui.QFont

		This property holds the current font of the dialog..
		"""
		res = super(QFontDialog,self).setCurrentFont(font)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QFontDialog.FontDialogOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QFontDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QFontDialog.FontDialogOptions

		This property holds the various options that affect the look and feel of the dialog.
		By default, all options are disabled.
		Options should be set before showing the dialog
		Setting them while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).
		"""
		res = super(QFontDialog,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QFontDialog.FontDialogOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QFontDialog,self).testOption(option)
		isinstance(res,QtCore.bool)
		return res
