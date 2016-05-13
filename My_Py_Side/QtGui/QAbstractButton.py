from PySide import QtGui, QtCore

class QAbstractButton(QtGui.QAbstractButton):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractButton,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoExclusive(self):
		"""
		This property holds whether auto-exclusivity is enabled.
		If auto-exclusivity is enabled, checkable buttons that belong to the same parent widget behave as if they were part of the same exclusive button group
		In an exclusive button group, only one button can be checked at any time; checking another button automatically unchecks the previously checked one.
		The property has no effect on buttons that belong to a button group.
		PySide.QtGui.QAbstractButton.autoExclusive() is off by default, except for radio buttons.
		"""
		res = super(QAbstractButton,self).autoExclusive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def autoRepeat(self):
		"""
		This property holds whether PySide.QtGui.QAbstractButton.autoRepeat() is enabled.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then the PySide.QtGui.QAbstractButton.pressed() , PySide.QtGui.QAbstractButton.released() , and PySide.QtGui.QAbstractButton.clicked() signals are emitted at regular intervals when the button is down
		PySide.QtGui.QAbstractButton.autoRepeat() is off by default
		The initial delay and the repetition interval are defined in milliseconds by PySide.QtGui.QAbstractButton.autoRepeatDelay() and PySide.QtGui.QAbstractButton.autoRepeatInterval() .
		Note: If a button is pressed down by a shortcut key, then auto-repeat is enabled and timed by the system and not by this class
		The PySide.QtGui.QAbstractButton.pressed() , PySide.QtGui.QAbstractButton.released() , and PySide.QtGui.QAbstractButton.clicked() signals will be emitted like in the normal case.
		"""
		res = super(QAbstractButton,self).autoRepeat()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def autoRepeatDelay(self):
		"""
		This property holds the initial delay of auto-repetition.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then PySide.QtGui.QAbstractButton.autoRepeatDelay() defines the initial delay in milliseconds before auto-repetition kicks in.
		"""
		res = super(QAbstractButton,self).autoRepeatDelay()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def autoRepeatInterval(self):
		"""
		This property holds the interval of auto-repetition.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then PySide.QtGui.QAbstractButton.autoRepeatInterval() defines the length of the auto-repetition interval in millisecons.
		"""
		res = super(QAbstractButton,self).autoRepeatInterval()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def checkStateSet(self):
		"""
		This virtual handler is called when PySide.QtGui.QAbstractButton.setChecked() was called, unless it was called from within PySide.QtGui.QAbstractButton.nextCheckState()
		It allows subclasses to reset their intermediate button states.
		"""
		res = super(QAbstractButton,self).checkStateSet()
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns the group that this button belongs to.
		If the button is not a member of any PySide.QtGui.QButtonGroup , this function returns 0.
		"""
		res = super(QAbstractButton,self).group()
		isinstance(res,QtGui.QButtonGroup)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the icon shown on the button.
		The icons default size is defined by the GUI style, but can be adjusted by setting the PySide.QtGui.QAbstractButton.iconSize() property.
		"""
		res = super(QAbstractButton,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the icon size used for this button..
		The default size is defined by the GUI style
		This is a maximum size for the icons
		Smaller icons will not be scaled up.
		"""
		res = super(QAbstractButton,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isCheckable(self):
		"""
		This property holds whether the button is checkable.
		By default, the button is not checkable.
		"""
		res = super(QAbstractButton,self).isCheckable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isChecked(self):
		"""
		This property holds whether the button is checked.
		Only checkable buttons can be checked
		By default, the button is unchecked.
		"""
		res = super(QAbstractButton,self).isChecked()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isDown(self):
		"""
		This property holds whether the button is pressed down.
		If this property is true, the button is pressed down
		The signals PySide.QtGui.QAbstractButton.pressed() and PySide.QtGui.QAbstractButton.clicked() are not emitted if you set this property to true
		The default is false.
		"""
		res = super(QAbstractButton,self).isDown()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def nextCheckState(self):
		"""
		This virtual handler is called when a button is clicked
		The default implementation calls setChecked(! PySide.QtGui.QAbstractButton.isChecked() ) if the button PySide.QtGui.QAbstractButton.isCheckable()
		It allows subclasses to implement intermediate button states.
		"""
		res = super(QAbstractButton,self).nextCheckState()
		return res
	#----------------------------------------------------------------------
	def pressed(self):
		"""

		"""
		res = super(QAbstractButton,self).pressed()
		return res
	#----------------------------------------------------------------------
	def released(self):
		"""

		"""
		res = super(QAbstractButton,self).released()
		return res
	#----------------------------------------------------------------------
	def shortcut(self):
		"""
		This property holds the mnemonic associated with the button.
		"""
		res = super(QAbstractButton,self).shortcut()
		isinstance(res,QtGui.QKeySequence)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the text shown on the button.
		If the button has no text, the PySide.QtGui.QAbstractButton.text() function will return a an empty string.
		If the text contains an ampersand character (&), a shortcut is automatically created for it
		The character that follows the & will be used as the shortcut key
		Any previous shortcut will be overwritten, or cleared if no shortcut is defined by the text
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		There is no default text.
		"""
		res = super(QAbstractButton,self).text()
		return res
	#----------------------------------------------------------------------
	def hitButton(self,pos):
		"""
		hitButton(pos)
			pos=QtCore.QPoint

		Returns true if pos is inside the clickable button rectangle; otherwise returns false.
		By default, the clickable area is the entire widget
		Subclasses may reimplement this function to provide support for clickable areas of different shapes and sizes.
		"""
		res = super(QAbstractButton,self).hitButton(pos)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAutoExclusive(self,arg__1):
		"""
		setAutoExclusive(arg__1)
			arg__1=QtCore.bool

		This property holds whether auto-exclusivity is enabled.
		If auto-exclusivity is enabled, checkable buttons that belong to the same parent widget behave as if they were part of the same exclusive button group
		In an exclusive button group, only one button can be checked at any time; checking another button automatically unchecks the previously checked one.
		The property has no effect on buttons that belong to a button group.
		PySide.QtGui.QAbstractButton.autoExclusive() is off by default, except for radio buttons.
		"""
		res = super(QAbstractButton,self).setAutoExclusive(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAutoRepeat(self,arg__1):
		"""
		setAutoRepeat(arg__1)
			arg__1=QtCore.bool

		This property holds whether PySide.QtGui.QAbstractButton.autoRepeat() is enabled.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then the PySide.QtGui.QAbstractButton.pressed() , PySide.QtGui.QAbstractButton.released() , and PySide.QtGui.QAbstractButton.clicked() signals are emitted at regular intervals when the button is down
		PySide.QtGui.QAbstractButton.autoRepeat() is off by default
		The initial delay and the repetition interval are defined in milliseconds by PySide.QtGui.QAbstractButton.autoRepeatDelay() and PySide.QtGui.QAbstractButton.autoRepeatInterval() .
		Note: If a button is pressed down by a shortcut key, then auto-repeat is enabled and timed by the system and not by this class
		The PySide.QtGui.QAbstractButton.pressed() , PySide.QtGui.QAbstractButton.released() , and PySide.QtGui.QAbstractButton.clicked() signals will be emitted like in the normal case.
		"""
		res = super(QAbstractButton,self).setAutoRepeat(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAutoRepeatDelay(self,arg__1):
		"""
		setAutoRepeatDelay(arg__1)
			arg__1=QtCore.int

		This property holds the initial delay of auto-repetition.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then PySide.QtGui.QAbstractButton.autoRepeatDelay() defines the initial delay in milliseconds before auto-repetition kicks in.
		"""
		res = super(QAbstractButton,self).setAutoRepeatDelay(arg__1)
		return res
	#----------------------------------------------------------------------
	def setAutoRepeatInterval(self,arg__1):
		"""
		setAutoRepeatInterval(arg__1)
			arg__1=QtCore.int

		This property holds the interval of auto-repetition.
		If PySide.QtGui.QAbstractButton.autoRepeat() is enabled, then PySide.QtGui.QAbstractButton.autoRepeatInterval() defines the length of the auto-repetition interval in millisecons.
		"""
		res = super(QAbstractButton,self).setAutoRepeatInterval(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCheckable(self,arg__1):
		"""
		setCheckable(arg__1)
			arg__1=QtCore.bool

		This property holds whether the button is checkable.
		By default, the button is not checkable.
		"""
		res = super(QAbstractButton,self).setCheckable(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDown(self,arg__1):
		"""
		setDown(arg__1)
			arg__1=QtCore.bool

		This property holds whether the button is pressed down.
		If this property is true, the button is pressed down
		The signals PySide.QtGui.QAbstractButton.pressed() and PySide.QtGui.QAbstractButton.clicked() are not emitted if you set this property to true
		The default is false.
		"""
		res = super(QAbstractButton,self).setDown(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		This property holds the icon shown on the button.
		The icons default size is defined by the GUI style, but can be adjusted by setting the PySide.QtGui.QAbstractButton.iconSize() property.
		"""
		res = super(QAbstractButton,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setShortcut(self,key):
		"""
		setShortcut(key)
			key=QtGui.QKeySequence

		This property holds the mnemonic associated with the button.
		"""
		res = super(QAbstractButton,self).setShortcut(key)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		This property holds the text shown on the button.
		If the button has no text, the PySide.QtGui.QAbstractButton.text() function will return a an empty string.
		If the text contains an ampersand character (&), a shortcut is automatically created for it
		The character that follows the & will be used as the shortcut key
		Any previous shortcut will be overwritten, or cleared if no shortcut is defined by the text
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		There is no default text.
		"""
		res = super(QAbstractButton,self).setText(text)
		return res
