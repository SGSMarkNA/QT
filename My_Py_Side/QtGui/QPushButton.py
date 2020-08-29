from PySide import QtGui, QtCore

class QPushButton(QtGui.QPushButton):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPushButton,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoDefault(self):
		"""
		This property holds whether the push button is an auto default button.
		If this property is set to true then the push button is an auto default button.
		In some GUI styles a default button is drawn with an extra frame around it, up to 3 pixels or more
		Qt automatically keeps this space free around auto-default buttons, i.e
		auto-default buttons may have a slightly larger size hint.
		This propertys default is true for buttons that have a PySide.QtGui.QDialog parent; otherwise it defaults to false.
		See the default() property for details of how default() and auto-default interact.
		"""
		res = super(QPushButton,self).autoDefault()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDefault(self):
		"""
		This property holds whether the push button is the default button.
		Default and autodefault buttons decide what happens when the user presses enter in a dialog.
		A button with this property set to true (i.e., the dialogs default button,) will automatically be pressed when the user presses enter, with one exception: if an autoDefault button currently has focus, the PySide.QtGui.QPushButton.autoDefault() button is pressed
		When the dialog has PySide.QtGui.QPushButton.autoDefault() buttons but no default button, pressing enter will press either the PySide.QtGui.QPushButton.autoDefault() button that currently has focus, or if no button has focus, the next PySide.QtGui.QPushButton.autoDefault() button in the focus chain.
		In a dialog, only one push button at a time can be the default button
		This button is then displayed with an additional frame (depending on the GUI style).
		The default button behavior is provided only in dialogs
		Buttons can always be clicked from the keyboard by pressing Spacebar when the button has focus.
		If the default property is set to false on the current default button while the dialog is visible, a new default will automatically be assigned the next time a pushbutton in the dialog receives focus.
		This propertys default is false.
		"""
		res = super(QPushButton,self).isDefault()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFlat(self):
		"""
		This property holds whether the button border is raised.
		This propertys default is false
		If this property is set, most styles will not paint the button background unless the button is being pressed
		PySide.QtGui.QWidget.setAutoFillBackground() can be used to ensure that the background is filled using the QPalette.Button brush.
		"""
		res = super(QPushButton,self).isFlat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def menu(self):
		"""
		Returns the buttons associated popup menu or 0 if no popup menu has been set.
		"""
		res = super(QPushButton,self).menu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionButton

		Initialize option with the values from this PySide.QtGui.QPushButton
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionButton , but dont want to fill in all the information themselves.
		"""
		res = super(QPushButton,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setAutoDefault(self,arg__1):
		"""
		setAutoDefault(arg__1)
			arg__1=QtCore.bool

		This property holds whether the push button is an auto default button.
		If this property is set to true then the push button is an auto default button.
		In some GUI styles a default button is drawn with an extra frame around it, up to 3 pixels or more
		Qt automatically keeps this space free around auto-default buttons, i.e
		auto-default buttons may have a slightly larger size hint.
		This propertys default is true for buttons that have a PySide.QtGui.QDialog parent; otherwise it defaults to false.
		See the default() property for details of how default() and auto-default interact.
		"""
		res = super(QPushButton,self).setAutoDefault(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDefault(self,arg__1):
		"""
		setDefault(arg__1)
			arg__1=QtCore.bool

		This property holds whether the push button is the default button.
		Default and autodefault buttons decide what happens when the user presses enter in a dialog.
		A button with this property set to true (i.e., the dialogs default button,) will automatically be pressed when the user presses enter, with one exception: if an autoDefault button currently has focus, the PySide.QtGui.QPushButton.autoDefault() button is pressed
		When the dialog has PySide.QtGui.QPushButton.autoDefault() buttons but no default button, pressing enter will press either the PySide.QtGui.QPushButton.autoDefault() button that currently has focus, or if no button has focus, the next PySide.QtGui.QPushButton.autoDefault() button in the focus chain.
		In a dialog, only one push button at a time can be the default button
		This button is then displayed with an additional frame (depending on the GUI style).
		The default button behavior is provided only in dialogs
		Buttons can always be clicked from the keyboard by pressing Spacebar when the button has focus.
		If the default property is set to false on the current default button while the dialog is visible, a new default will automatically be assigned the next time a pushbutton in the dialog receives focus.
		This propertys default is false.
		"""
		res = super(QPushButton,self).setDefault(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFlat(self,arg__1):
		"""
		setFlat(arg__1)
			arg__1=QtCore.bool

		This property holds whether the button border is raised.
		This propertys default is false
		If this property is set, most styles will not paint the button background unless the button is being pressed
		PySide.QtGui.QWidget.setAutoFillBackground() can be used to ensure that the background is filled using the QPalette.Button brush.
		"""
		res = super(QPushButton,self).setFlat(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMenu(self,menu):
		"""
		setMenu(menu)
			menu=QtGui.QMenu

		Associates the popup menu menu with this push button
		This turns the button into a menu button, which in some styles will produce a small triangle to the right of the buttons text.
		Ownership of the menu is not transferred to the push button.
		"""
		res = super(QPushButton,self).setMenu(menu)
		return res
