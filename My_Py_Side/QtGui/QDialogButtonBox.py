from PySide import QtGui, QtCore

class QDialogButtonBox(QtGui.QDialogButtonBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDialogButtonBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def accepted(self):
		"""

		"""
		res = super(QDialogButtonBox,self).accepted()
		return res
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns a list of all the buttons that have been added to the button box.
		"""
		res = super(QDialogButtonBox,self).buttons()
		return res
	#----------------------------------------------------------------------
	def centerButtons(self):
		"""
		This property holds whether the buttons in the button box are centered.
		By default, this property is false
		This behavior is appopriate for most types of dialogs
		A notable exception is message boxes on most platforms (e.g
		Windows), where the button box is centered horizontally.
		"""
		res = super(QDialogButtonBox,self).centerButtons()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the button box, deleting all buttons within it.
		"""
		res = super(QDialogButtonBox,self).clear()
		return res
	#----------------------------------------------------------------------
	def helpRequested(self):
		"""

		"""
		res = super(QDialogButtonBox,self).helpRequested()
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the button box.
		By default, the orientation is horizontal (i.e
		the buttons are laid out side by side)
		The possible orientations are Qt.Horizontal and Qt.Vertical .
		"""
		res = super(QDialogButtonBox,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def rejected(self):
		"""

		"""
		res = super(QDialogButtonBox,self).rejected()
		return res
	#----------------------------------------------------------------------
	def standardButtons(self):
		"""
		This property holds collection of standard buttons in the button box.
		This property controls which standard buttons are used by the button box.
		"""
		res = super(QDialogButtonBox,self).standardButtons()
		isinstance(res,QtGui.QDialogButtonBox.StandardButtons)
		return res
	#----------------------------------------------------------------------
	def addButton(self,*args,**kwargs):
		"""
		addButton(text,role)
			text=unicode
			role=QtGui.QDialogButtonBox.ButtonRole

		addButton(button)
			button=QtGui.QDialogButtonBox.StandardButton

		addButton(button,role)
			button=QtGui.QAbstractButton
			role=QtGui.QDialogButtonBox.ButtonRole

		Creates a push button with the given text , adds it to the button box for the specified role , and returns the corresponding push button
		If role is invalid, no button is created, and zero is returned.
		"""
		res = super(QDialogButtonBox,self).addButton(*args,**kwargs)
		isinstance(res,QtGui.QPushButton)
		return res
	#----------------------------------------------------------------------
	def button(self,which):
		"""
		button(which)
			which=QtGui.QDialogButtonBox.StandardButton

		Returns the PySide.QtGui.QPushButton corresponding to the standard button which , or 0 if the standard button doesnt exist in this button box.
		"""
		res = super(QDialogButtonBox,self).button(which)
		isinstance(res,QtGui.QPushButton)
		return res
	#----------------------------------------------------------------------
	def buttonRole(self,button):
		"""
		buttonRole(button)
			button=QtGui.QAbstractButton

		Returns the button role for the specified button
		This function returns InvalidRole if button is 0 or has not been added to the button box.
		"""
		res = super(QDialogButtonBox,self).buttonRole(button)
		isinstance(res,QtGui.QDialogButtonBox.ButtonRole)
		return res
	#----------------------------------------------------------------------
	def removeButton(self,button):
		"""
		removeButton(button)
			button=QtGui.QAbstractButton

		Removes button from the button box without deleting it and sets its parent to zero.
		"""
		res = super(QDialogButtonBox,self).removeButton(button)
		return res
	#----------------------------------------------------------------------
	def setCenterButtons(self,center):
		"""
		setCenterButtons(center)
			center=QtCore.bool

		This property holds whether the buttons in the button box are centered.
		By default, this property is false
		This behavior is appopriate for most types of dialogs
		A notable exception is message boxes on most platforms (e.g
		Windows), where the button box is centered horizontally.
		"""
		res = super(QDialogButtonBox,self).setCenterButtons(center)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,orientation):
		"""
		setOrientation(orientation)
			orientation=QtCore.Qt.Orientation

		This property holds the orientation of the button box.
		By default, the orientation is horizontal (i.e
		the buttons are laid out side by side)
		The possible orientations are Qt.Horizontal and Qt.Vertical .
		"""
		res = super(QDialogButtonBox,self).setOrientation(orientation)
		return res
	#----------------------------------------------------------------------
	def setStandardButtons(self,buttons):
		"""
		setStandardButtons(buttons)
			buttons=QtGui.QDialogButtonBox.StandardButtons

		This property holds collection of standard buttons in the button box.
		This property controls which standard buttons are used by the button box.
		"""
		res = super(QDialogButtonBox,self).setStandardButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def standardButton(self,button):
		"""
		standardButton(button)
			button=QtGui.QAbstractButton

		Returns the standard button enum value corresponding to the given button , or NoButton if the given button isnt a standard button.
		"""
		res = super(QDialogButtonBox,self).standardButton(button)
		isinstance(res,QtGui.QDialogButtonBox.StandardButton)
		return res
