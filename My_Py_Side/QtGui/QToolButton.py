from PySide import QtGui, QtCore

class QToolButton(QtGui.QToolButton):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QToolButton,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def arrowType(self):
		"""
		This property holds whether the button displays an arrow instead of a normal icon.
		This displays an arrow as the icon for the PySide.QtGui.QToolButton .
		By default, this property is set to Qt.NoArrow .
		"""
		res = super(QToolButton,self).arrowType()
		isinstance(res,QtCore.Qt.ArrowType)
		return res
	#----------------------------------------------------------------------
	def autoRaise(self):
		"""
		This property holds whether auto-raising is enabled or not..
		The default is disabled (i.e
		false).
		This property is currently ignored on Mac OS X when using QMacStyle .
		"""
		res = super(QToolButton,self).autoRaise()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def defaultAction(self):
		"""
		Returns the default action.
		"""
		res = super(QToolButton,self).defaultAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def menu(self):
		"""
		Returns the associated menu, or 0 if no menu has been defined.
		"""
		res = super(QToolButton,self).menu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def popupMode(self):
		"""
		This property describes the way that popup menus are used with tool buttons.
		By default, this property is set to DelayedPopup .
		"""
		res = super(QToolButton,self).popupMode()
		isinstance(res,QtGui.QToolButton.ToolButtonPopupMode)
		return res
	#----------------------------------------------------------------------
	def toolButtonStyle(self):
		"""
		This property holds whether the tool button displays an icon only, text only, or text beside/below the icon..
		The default is Qt.ToolButtonIconOnly .
		To have the style of toolbuttons follow the system settings (as available in GNOME and KDE desktop environments), set this property to Qt.ToolButtonFollowStyle .
		PySide.QtGui.QToolButton automatically connects this slot to the relevant signal in the PySide.QtGui.QMainWindow in which is resides.
		"""
		res = super(QToolButton,self).toolButtonStyle()
		isinstance(res,QtCore.Qt.ToolButtonStyle)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionToolButton

		Initialize option with the values from this PySide.QtGui.QToolButton
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionToolButton , but dont want to fill in all the information themselves.
		"""
		res = super(QToolButton,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setArrowType(self,type):
		"""
		setArrowType(type)
			type=QtCore.Qt.ArrowType

		This property holds whether the button displays an arrow instead of a normal icon.
		This displays an arrow as the icon for the PySide.QtGui.QToolButton .
		By default, this property is set to Qt.NoArrow .
		"""
		res = super(QToolButton,self).setArrowType(type)
		return res
	#----------------------------------------------------------------------
	def setAutoRaise(self,enable):
		"""
		setAutoRaise(enable)
			enable=QtCore.bool

		This property holds whether auto-raising is enabled or not..
		The default is disabled (i.e
		false).
		This property is currently ignored on Mac OS X when using QMacStyle .
		"""
		res = super(QToolButton,self).setAutoRaise(enable)
		return res
	#----------------------------------------------------------------------
	def setMenu(self,menu):
		"""
		setMenu(menu)
			menu=QtGui.QMenu

		Associates the given menu with this tool button.
		The menu will be shown according to the buttons PySide.QtGui.QToolButton.popupMode() .
		Ownership of the menu is not transferred to the tool button.
		"""
		res = super(QToolButton,self).setMenu(menu)
		return res
	#----------------------------------------------------------------------
	def setPopupMode(self,mode):
		"""
		setPopupMode(mode)
			mode=QtGui.QToolButton.ToolButtonPopupMode

		This property describes the way that popup menus are used with tool buttons.
		By default, this property is set to DelayedPopup .
		"""
		res = super(QToolButton,self).setPopupMode(mode)
		return res
