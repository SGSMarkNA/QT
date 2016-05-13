from PySide import QtGui, QtCore

class QMessageBox(QtGui.QMessageBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMessageBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns a list of all the buttons that have been added to the message box.
		"""
		res = super(QMessageBox,self).buttons()
		return res
	#----------------------------------------------------------------------
	def clickedButton(self):
		"""
		Returns the button that was clicked by the user, or 0 if the user hit the Esc key and no escape button was set.
		If exec() hasnt been called yet, returns 0.
		Example:
		"""
		res = super(QMessageBox,self).clickedButton()
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def defaultButton(self):
		"""
		Returns the button that should be the message boxs default button
		Returns 0 if no default button was set.
		"""
		res = super(QMessageBox,self).defaultButton()
		isinstance(res,QtGui.QPushButton)
		return res
	#----------------------------------------------------------------------
	def detailedText(self):
		"""
		This property holds the text to be displayed in the details area..
		The text will be interpreted as a plain text.
		By default, this property contains an empty string.
		"""
		res = super(QMessageBox,self).detailedText()
		return res
	#----------------------------------------------------------------------
	def escapeButton(self):
		"""
		Returns the button that is activated when escape is pressed.
		By default, PySide.QtGui.QMessageBox attempts to automatically detect an escape button as follows:
		When an escape button could not be automatically detected, pressing Esc has no effect.
		"""
		res = super(QMessageBox,self).escapeButton()
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the message boxs icon.
		The icon of the message box can be specified with one of the values:
		The default is QMessageBox.NoIcon .
		The pixmap used to display the actual icon depends on the current GUI style
		You can also set a custom pixmap for the icon by setting the icon pixmap property.
		"""
		res = super(QMessageBox,self).icon()
		isinstance(res,QtGui.QMessageBox.Icon)
		return res
	#----------------------------------------------------------------------
	def iconPixmap(self):
		"""
		This property holds the current icon.
		The icon currently used by the message box
		Note that its often hard to draw one pixmap that looks appropriate in all GUI styles; you may want to supply a different pixmap for each platform.
		By default, this property is undefined.
		"""
		res = super(QMessageBox,self).iconPixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def informativeText(self):
		"""
		This property holds the informative text that provides a fuller description for the message.
		Infromative text can be used to expand upon the PySide.QtGui.QMessageBox.text() to give more information to the user
		On the Mac, this text appears in small system font below the PySide.QtGui.QMessageBox.text()
		On other platforms, it is simply appended to the existing text.
		By default, this property contains an empty string.
		"""
		res = super(QMessageBox,self).informativeText()
		return res
	#----------------------------------------------------------------------
	def standardButtons(self):
		"""

		"""
		res = super(QMessageBox,self).standardButtons()
		isinstance(res,QtGui.QMessageBox.StandardButtons)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the message box text to be displayed..
		The text will be interpreted either as a plain text or as rich text, depending on the text format setting ( QMessageBox.textFormat )
		The default setting is Qt.AutoText , i.e., the message box will try to auto-detect the format of the text.
		The default value of this property is an empty string.
		"""
		res = super(QMessageBox,self).text()
		return res
	#----------------------------------------------------------------------
	def textFormat(self):
		"""
		This property holds the format of the text displayed by the message box.
		The current text format used by the message box
		See the Qt.TextFormat enum for an explanation of the possible options.
		The default format is Qt.AutoText .
		"""
		res = super(QMessageBox,self).textFormat()
		isinstance(res,QtCore.Qt.TextFormat)
		return res
	#----------------------------------------------------------------------
	def addButton(self,*args,**kwargs):
		"""
		addButton(text,role)
			text=unicode
			role=QtGui.QMessageBox.ButtonRole

		addButton(button)
			button=QtGui.QMessageBox.StandardButton

		addButton(button,role)
			button=QtGui.QAbstractButton
			role=QtGui.QMessageBox.ButtonRole

		This is an overloaded function.
		Creates a button with the given text , adds it to the message box for the specified role , and returns it.
		"""
		res = super(QMessageBox,self).addButton(*args,**kwargs)
		isinstance(res,QtGui.QPushButton)
		return res
	#----------------------------------------------------------------------
	def button(self,which):
		"""
		button(which)
			which=QtGui.QMessageBox.StandardButton

		Returns a pointer corresponding to the standard button which , or 0 if the standard button doesnt exist in this message box.
		"""
		res = super(QMessageBox,self).button(which)
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def buttonRole(self,button):
		"""
		buttonRole(button)
			button=QtGui.QAbstractButton

		Returns the button role for the specified button
		This function returns InvalidRole if button is 0 or has not been added to the message box.
		"""
		res = super(QMessageBox,self).buttonRole(button)
		isinstance(res,QtGui.QMessageBox.ButtonRole)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QDialog.finished() or PySide.QtGui.QMessageBox.buttonClicked() signal to the slot specified by receiver and member
		If the slot in member has a pointer for its first parameter the connection is to PySide.QtGui.QMessageBox.buttonClicked() , otherwise the connection is to PySide.QtGui.QDialog.finished() .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QMessageBox,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def removeButton(self,button):
		"""
		removeButton(button)
			button=QtGui.QAbstractButton

		Removes button from the button box without deleting it.
		"""
		res = super(QMessageBox,self).removeButton(button)
		return res
	#----------------------------------------------------------------------
	def setDefaultButton(self,*args,**kwargs):
		"""
		setDefaultButton(button)
			button=QtGui.QPushButton

		setDefaultButton(button)
			button=QtGui.QMessageBox.StandardButton

		Sets the message boxs default button to button .
		"""
		res = super(QMessageBox,self).setDefaultButton(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setDetailedText(self,text):
		"""
		setDetailedText(text)
			text=unicode

		This property holds the text to be displayed in the details area..
		The text will be interpreted as a plain text.
		By default, this property contains an empty string.
		"""
		res = super(QMessageBox,self).setDetailedText(text)
		return res
	#----------------------------------------------------------------------
	def setEscapeButton(self,*args,**kwargs):
		"""
		setEscapeButton(button)
			button=QtGui.QMessageBox.StandardButton

		setEscapeButton(button)
			button=QtGui.QAbstractButton

		Sets the buttons that gets activated when the Escape key is pressed to button .
		"""
		res = super(QMessageBox,self).setEscapeButton(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,arg__1):
		"""
		setIcon(arg__1)
			arg__1=QtGui.QMessageBox.Icon

		This property holds the message boxs icon.
		The icon of the message box can be specified with one of the values:
		The default is QMessageBox.NoIcon .
		The pixmap used to display the actual icon depends on the current GUI style
		You can also set a custom pixmap for the icon by setting the icon pixmap property.
		"""
		res = super(QMessageBox,self).setIcon(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIconPixmap(self,pixmap):
		"""
		setIconPixmap(pixmap)
			pixmap=QtGui.QPixmap

		This property holds the current icon.
		The icon currently used by the message box
		Note that its often hard to draw one pixmap that looks appropriate in all GUI styles; you may want to supply a different pixmap for each platform.
		By default, this property is undefined.
		"""
		res = super(QMessageBox,self).setIconPixmap(pixmap)
		return res
	#----------------------------------------------------------------------
	def setInformativeText(self,text):
		"""
		setInformativeText(text)
			text=unicode

		This property holds the informative text that provides a fuller description for the message.
		Infromative text can be used to expand upon the PySide.QtGui.QMessageBox.text() to give more information to the user
		On the Mac, this text appears in small system font below the PySide.QtGui.QMessageBox.text()
		On other platforms, it is simply appended to the existing text.
		By default, this property contains an empty string.
		"""
		res = super(QMessageBox,self).setInformativeText(text)
		return res
	#----------------------------------------------------------------------
	def setStandardButtons(self,buttons):
		"""
		setStandardButtons(buttons)
			buttons=QtGui.QMessageBox.StandardButtons


		"""
		res = super(QMessageBox,self).setStandardButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		This property holds the message box text to be displayed..
		The text will be interpreted either as a plain text or as rich text, depending on the text format setting ( QMessageBox.textFormat )
		The default setting is Qt.AutoText , i.e., the message box will try to auto-detect the format of the text.
		The default value of this property is an empty string.
		"""
		res = super(QMessageBox,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setTextFormat(self,format):
		"""
		setTextFormat(format)
			format=QtCore.Qt.TextFormat

		This property holds the format of the text displayed by the message box.
		The current text format used by the message box
		See the Qt.TextFormat enum for an explanation of the possible options.
		The default format is Qt.AutoText .
		"""
		res = super(QMessageBox,self).setTextFormat(format)
		return res
	#----------------------------------------------------------------------
	def standardButton(self,button):
		"""
		standardButton(button)
			button=QtGui.QAbstractButton

		Returns the standard button enum value corresponding to the given button , or NoButton if the given button isnt a standard button.
		"""
		res = super(QMessageBox,self).standardButton(button)
		isinstance(res,QtGui.QMessageBox.StandardButton)
		return res
