from PySide import QtGui, QtCore

class QShortcut(QtGui.QShortcut):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QShortcut,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activated(self):
		"""

		"""
		res = super(QShortcut,self).activated()
		return res
	#----------------------------------------------------------------------
	def activatedAmbiguously(self):
		"""

		"""
		res = super(QShortcut,self).activatedAmbiguously()
		return res
	#----------------------------------------------------------------------
	def autoRepeat(self):
		"""
		This property holds whether the shortcut can auto repeat.
		If true, the shortcut will auto repeat when the keyboard shortcut combination is held down, provided that keyboard auto repeat is enabled on the system
		The default value is true.
		"""
		res = super(QShortcut,self).autoRepeat()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def context(self):
		"""
		This property holds the context in which the shortcut is valid.
		A shortcuts context decides in which circumstances a shortcut is allowed to be triggered
		The normal context is Qt.WindowShortcut , which allows the shortcut to trigger if the parent (the widget containing the shortcut) is a subwidget of the active top-level window.
		By default, this property is set to Qt.WindowShortcut .
		"""
		res = super(QShortcut,self).context()
		isinstance(res,QtCore.Qt.ShortcutContext)
		return res
	#----------------------------------------------------------------------
	def id(self):
		"""
		Returns the shortcuts ID.
		"""
		res = super(QShortcut,self).id()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		This property holds whether the shortcut is enabled.
		An enabled shortcut emits the PySide.QtGui.QShortcut.activated() or PySide.QtGui.QShortcut.activatedAmbiguously() signal when a PySide.QtGui.QShortcutEvent occurs that matches the shortcuts PySide.QtGui.QShortcut.key() sequence.
		If the application is in WhatsThis mode the shortcut will not emit the signals, but will show the Whats This? text instead.
		By default, this property is true.
		"""
		res = super(QShortcut,self).isEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		This property holds the shortcuts key sequence.
		This is a key sequence with an optional combination of Shift, Ctrl, and Alt
		The key sequence may be supplied in a number of ways:
		By default, this property contains an empty key sequence.
		"""
		res = super(QShortcut,self).key()
		isinstance(res,QtGui.QKeySequence)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		"""
		Returns the shortcuts parent widget.
		"""
		res = super(QShortcut,self).parentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		This property holds the shortcuts Whats This? help text.
		The text will be shown when the application is in Whats This? mode and the user types the shortcut PySide.QtGui.QShortcut.key() sequence.
		To set Whats This? help on a menu item (with or without a shortcut key), set the help on the items action.
		By default, this property contains an empty string.
		"""
		res = super(QShortcut,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def setAutoRepeat(self,on):
		"""
		setAutoRepeat(on)
			on=QtCore.bool

		This property holds whether the shortcut can auto repeat.
		If true, the shortcut will auto repeat when the keyboard shortcut combination is held down, provided that keyboard auto repeat is enabled on the system
		The default value is true.
		"""
		res = super(QShortcut,self).setAutoRepeat(on)
		return res
	#----------------------------------------------------------------------
	def setContext(self,context):
		"""
		setContext(context)
			context=QtCore.Qt.ShortcutContext

		This property holds the context in which the shortcut is valid.
		A shortcuts context decides in which circumstances a shortcut is allowed to be triggered
		The normal context is Qt.WindowShortcut , which allows the shortcut to trigger if the parent (the widget containing the shortcut) is a subwidget of the active top-level window.
		By default, this property is set to Qt.WindowShortcut .
		"""
		res = super(QShortcut,self).setContext(context)
		return res
	#----------------------------------------------------------------------
	def setEnabled(self,enable):
		"""
		setEnabled(enable)
			enable=QtCore.bool

		This property holds whether the shortcut is enabled.
		An enabled shortcut emits the PySide.QtGui.QShortcut.activated() or PySide.QtGui.QShortcut.activatedAmbiguously() signal when a PySide.QtGui.QShortcutEvent occurs that matches the shortcuts PySide.QtGui.QShortcut.key() sequence.
		If the application is in WhatsThis mode the shortcut will not emit the signals, but will show the Whats This? text instead.
		By default, this property is true.
		"""
		res = super(QShortcut,self).setEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setKey(self,key):
		"""
		setKey(key)
			key=QtGui.QKeySequence

		This property holds the shortcuts key sequence.
		This is a key sequence with an optional combination of Shift, Ctrl, and Alt
		The key sequence may be supplied in a number of ways:
		By default, this property contains an empty key sequence.
		"""
		res = super(QShortcut,self).setKey(key)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,text):
		"""
		setWhatsThis(text)
			text=unicode

		This property holds the shortcuts Whats This? help text.
		The text will be shown when the application is in Whats This? mode and the user types the shortcut PySide.QtGui.QShortcut.key() sequence.
		To set Whats This? help on a menu item (with or without a shortcut key), set the help on the items action.
		By default, this property contains an empty string.
		"""
		res = super(QShortcut,self).setWhatsThis(text)
		return res
