from PySide import QtGui, QtCore

class QAction(QtGui.QAction):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAction,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def actionGroup(self):
		"""
		Returns the action group for this action
		If no action group manages this action then 0 will be returned.
		"""
		res = super(QAction,self).actionGroup()
		isinstance(res,QtGui.QActionGroup)
		return res
	#----------------------------------------------------------------------
	def associatedGraphicsWidgets(self):
		"""
		Returns a list of widgets this action has been added to.
		"""
		res = super(QAction,self).associatedGraphicsWidgets()
		return res
	#----------------------------------------------------------------------
	def associatedWidgets(self):
		"""
		Returns a list of widgets this action has been added to.
		"""
		res = super(QAction,self).associatedWidgets()
		return res
	#----------------------------------------------------------------------
	def autoRepeat(self):
		"""
		This property holds whether the action can auto repeat.
		If true, the action will auto repeat when the keyboard shortcut combination is held down, provided that keyboard auto repeat is enabled on the system
		The default value is true.
		"""
		res = super(QAction,self).autoRepeat()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def changed(self):
		"""

		"""
		res = super(QAction,self).changed()
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the user data as set in QAction::setData.
		"""
		res = super(QAction,self).data()
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		This property holds the actions font.
		The font property is used to render the text set on the PySide.QtGui.QAction
		The font will can be considered a hint as it will not be consulted in all cases based upon application and style.
		By default, this property contains the applications default font.
		"""
		res = super(QAction,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def hovered(self):
		"""

		"""
		res = super(QAction,self).hovered()
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the actions icon.
		In toolbars, the icon is used as the tool button icon; in menus, it is displayed to the left of the menu text
		There is no default icon.
		On Symbian the icons which are passed to softkeys, i.e
		to actions with softkey role, need to have pixmap alpha channel correctly set otherwise drawing artifacts will appear when softkey is pressed down.
		If a null icon ( QIcon.isNull() is passed into this function, the icon of the action is cleared.
		"""
		res = super(QAction,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def iconText(self):
		"""
		This property holds the actions descriptive icon text.
		If QToolBar.toolButtonStyle is set to a value that permits text to be displayed, the text defined held in this property appears as a label in the relevant tool button.
		It also serves as the default text in menus and tooltips if the action has not been defined with PySide.QtGui.QAction.setText() or PySide.QtGui.QAction.setToolTip() , and will also be used in toolbar buttons if no icon has been defined using PySide.QtGui.QAction.setIcon() .
		If the icon text is not explicitly set, the actions normal text will be used for the icon text.
		By default, this property contains an empty string.
		"""
		res = super(QAction,self).iconText()
		return res
	#----------------------------------------------------------------------
	def isCheckable(self):
		"""
		This property holds whether the action is a checkable action.
		A checkable action is one which has an on/off state
		For example, in a word processor, a Bold toolbar button may be either on or off
		An action which is not a toggle action is a command action; a command action is simply executed, e.g
		file save
		By default, this property is false.
		In some situations, the state of one toggle action should depend on the state of others
		For example, Left Align, Center and Right Align toggle actions are mutually exclusive
		To achieve exclusive toggling, add the relevant toggle actions to a PySide.QtGui.QActionGroup with the QActionGroup.exclusive property set to true.
		"""
		res = super(QAction,self).isCheckable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isChecked(self):
		"""
		This property holds whether the action is checked..
		Only checkable actions can be checked
		By default, this is false (the action is unchecked).
		"""
		res = super(QAction,self).isChecked()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		This property holds whether the action is enabled.
		Disabled actions cannot be chosen by the user
		They do not disappear from menus or toolbars, but they are displayed in a way which indicates that they are unavailable
		For example, they might be displayed using only shades of gray.
		Whats This? help on disabled actions is still available, provided that the QAction.whatsThis property is set.
		An action will be disabled when all widgets to which it is added (with QWidget.addAction() ) are disabled or not visible
		When an action is disabled, it is not possible to trigger it through its shortcut.
		By default, this property is true (actions are enabled).
		"""
		res = super(QAction,self).isEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isIconVisibleInMenu(self):
		"""
		This property holds Whether or not an action should show an icon in a menu.
		In some applications, it may make sense to have actions with icons in the toolbar, but not in menus
		If true, the icon (if valid) is shown in the menu, when it is false, it is not shown.
		The default is to follow whether the Qt.AA_DontShowIconsInMenus attribute is set for the application
		Explicitly settings this property overrides the presence (or abscence) of the attribute.
		For example:
		"""
		res = super(QAction,self).isIconVisibleInMenu()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSeparator(self):
		"""
		Returns true if this action is a separator action; otherwise it returns false.
		"""
		res = super(QAction,self).isSeparator()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isVisible(self):
		"""
		This property holds whether the action can be seen (e.g
		in menus and toolbars).
		If visible is true the action can be seen (e.g
		in menus and toolbars) and chosen by the user; if visible is false the action cannot be seen or chosen by the user.
		Actions which are not visible are not grayed out; they do not appear at all.
		By default, this property is true (actions are visible).
		"""
		res = super(QAction,self).isVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def menu(self):
		"""
		Returns the menu contained by this action
		Actions that contain menus can be used to create menu items with submenus, or inserted into toolbars to create buttons with popup menus.
		"""
		res = super(QAction,self).menu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def menuRole(self):
		"""
		This property holds the actions menu role.
		This indicates what role the action serves in the application menu on Mac OS X
		By default all action have the TextHeuristicRole , which means that the action is added based on its text (see PySide.QtGui.QMenuBar for more information).
		The menu role can only be changed before the actions are put into the menu bar in Mac OS X (usually just before the first application window is shown).
		"""
		res = super(QAction,self).menuRole()
		isinstance(res,QtGui.QAction.MenuRole)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		"""
		Returns the parent widget.
		"""
		res = super(QAction,self).parentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def priority(self):
		"""
		This property holds the actionss priority in the user interface..
		This property can be set to indicate how the action should be prioritized in the user interface.
		For instance, when toolbars have the Qt.ToolButtonTextBesideIcon mode set, then actions with LowPriority will not show the text labels.
		"""
		res = super(QAction,self).priority()
		isinstance(res,QtGui.QAction.Priority)
		return res
	#----------------------------------------------------------------------
	def shortcut(self):
		"""
		This property holds the actions primary shortcut key.
		Valid keycodes for this property can be found in Qt.Key and Qt.Modifier
		There is no default shortcut key.
		"""
		res = super(QAction,self).shortcut()
		isinstance(res,QtGui.QKeySequence)
		return res
	#----------------------------------------------------------------------
	def shortcutContext(self):
		"""
		This property holds the context for the actions shortcut.
		Valid values for this property can be found in Qt.ShortcutContext
		The default value is Qt.WindowShortcut .
		"""
		res = super(QAction,self).shortcutContext()
		isinstance(res,QtCore.Qt.ShortcutContext)
		return res
	#----------------------------------------------------------------------
	def shortcuts(self):
		"""
		Returns the list of shortcuts, with the primary shortcut as the first element of the list.
		"""
		res = super(QAction,self).shortcuts()
		return res
	#----------------------------------------------------------------------
	def softKeyRole(self):
		"""
		This property holds the actions softkey role.
		This indicates what type of role this action describes in the softkey framework on platforms where such a framework is supported
		Currently this is only supported on the Symbian platform.
		The softkey role can be changed any time.
		"""
		res = super(QAction,self).softKeyRole()
		isinstance(res,QtGui.QAction.SoftKeyRole)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		This property holds the actions status tip.
		The status tip is displayed on all status bars provided by the actions top-level parent widget.
		By default, this property contains an empty string.
		"""
		res = super(QAction,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the actions descriptive text.
		If the action is added to a menu, the menu option will consist of the icon (if there is one), the text, and the shortcut (if there is one)
		If the text is not explicitly set in the constructor, or by using PySide.QtGui.QAction.setText() , the actions description icon text will be used as text
		There is no default text.
		"""
		res = super(QAction,self).text()
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		This property holds the actions tooltip.
		This text is used for the tooltip
		If no tooltip is specified, the actions text is used.
		By default, this property contains the actions text.
		"""
		res = super(QAction,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		This property holds the actions Whats This? help text.
		The Whats This? text is used to provide a brief description of the action
		The text may contain rich text
		There is no default Whats This? text.
		"""
		res = super(QAction,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def activate(self,event):
		"""
		activate(event)
			event=QtGui.QAction.ActionEvent

		Sends the relevant signals for QAction.ActionEvent event .
		Action based widgets use this API to cause the PySide.QtGui.QAction to emit signals as well as emitting their own.
		"""
		res = super(QAction,self).activate(event)
		return res
	#----------------------------------------------------------------------
	def setActionGroup(self,group):
		"""
		setActionGroup(group)
			group=QtGui.QActionGroup

		Sets this action group to group
		The action will be automatically added to the groups list of actions.
		Actions within the group will be mutually exclusive.
		"""
		res = super(QAction,self).setActionGroup(group)
		return res
	#----------------------------------------------------------------------
	def setAutoRepeat(self,arg__1):
		"""
		setAutoRepeat(arg__1)
			arg__1=QtCore.bool

		This property holds whether the action can auto repeat.
		If true, the action will auto repeat when the keyboard shortcut combination is held down, provided that keyboard auto repeat is enabled on the system
		The default value is true.
		"""
		res = super(QAction,self).setAutoRepeat(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCheckable(self,arg__1):
		"""
		setCheckable(arg__1)
			arg__1=QtCore.bool

		This property holds whether the action is a checkable action.
		A checkable action is one which has an on/off state
		For example, in a word processor, a Bold toolbar button may be either on or off
		An action which is not a toggle action is a command action; a command action is simply executed, e.g
		file save
		By default, this property is false.
		In some situations, the state of one toggle action should depend on the state of others
		For example, Left Align, Center and Right Align toggle actions are mutually exclusive
		To achieve exclusive toggling, add the relevant toggle actions to a PySide.QtGui.QActionGroup with the QActionGroup.exclusive property set to true.
		"""
		res = super(QAction,self).setCheckable(arg__1)
		return res
	#----------------------------------------------------------------------
	def setData(self,var):
		"""
		setData(var)
			var=object

		Sets the actions internal data to the given userData .
		"""
		res = super(QAction,self).setData(var)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		This property holds the actions font.
		The font property is used to render the text set on the PySide.QtGui.QAction
		The font will can be considered a hint as it will not be consulted in all cases based upon application and style.
		By default, this property contains the applications default font.
		"""
		res = super(QAction,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		This property holds the actions icon.
		In toolbars, the icon is used as the tool button icon; in menus, it is displayed to the left of the menu text
		There is no default icon.
		On Symbian the icons which are passed to softkeys, i.e
		to actions with softkey role, need to have pixmap alpha channel correctly set otherwise drawing artifacts will appear when softkey is pressed down.
		If a null icon ( QIcon.isNull() is passed into this function, the icon of the action is cleared.
		"""
		res = super(QAction,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setIconText(self,text):
		"""
		setIconText(text)
			text=unicode

		This property holds the actions descriptive icon text.
		If QToolBar.toolButtonStyle is set to a value that permits text to be displayed, the text defined held in this property appears as a label in the relevant tool button.
		It also serves as the default text in menus and tooltips if the action has not been defined with PySide.QtGui.QAction.setText() or PySide.QtGui.QAction.setToolTip() , and will also be used in toolbar buttons if no icon has been defined using PySide.QtGui.QAction.setIcon() .
		If the icon text is not explicitly set, the actions normal text will be used for the icon text.
		By default, this property contains an empty string.
		"""
		res = super(QAction,self).setIconText(text)
		return res
	#----------------------------------------------------------------------
	def setIconVisibleInMenu(self,visible):
		"""
		setIconVisibleInMenu(visible)
			visible=QtCore.bool

		This property holds Whether or not an action should show an icon in a menu.
		In some applications, it may make sense to have actions with icons in the toolbar, but not in menus
		If true, the icon (if valid) is shown in the menu, when it is false, it is not shown.
		The default is to follow whether the Qt.AA_DontShowIconsInMenus attribute is set for the application
		Explicitly settings this property overrides the presence (or abscence) of the attribute.
		For example:
		"""
		res = super(QAction,self).setIconVisibleInMenu(visible)
		return res
	#----------------------------------------------------------------------
	def setMenu(self,menu):
		"""
		setMenu(menu)
			menu=QtGui.QMenu

		Sets the menu contained by this action to the specified menu .
		"""
		res = super(QAction,self).setMenu(menu)
		return res
	#----------------------------------------------------------------------
	def setMenuRole(self,menuRole):
		"""
		setMenuRole(menuRole)
			menuRole=QtGui.QAction.MenuRole

		This property holds the actions menu role.
		This indicates what role the action serves in the application menu on Mac OS X
		By default all action have the TextHeuristicRole , which means that the action is added based on its text (see PySide.QtGui.QMenuBar for more information).
		The menu role can only be changed before the actions are put into the menu bar in Mac OS X (usually just before the first application window is shown).
		"""
		res = super(QAction,self).setMenuRole(menuRole)
		return res
	#----------------------------------------------------------------------
	def setPriority(self,priority):
		"""
		setPriority(priority)
			priority=QtGui.QAction.Priority

		This property holds the actionss priority in the user interface..
		This property can be set to indicate how the action should be prioritized in the user interface.
		For instance, when toolbars have the Qt.ToolButtonTextBesideIcon mode set, then actions with LowPriority will not show the text labels.
		"""
		res = super(QAction,self).setPriority(priority)
		return res
	#----------------------------------------------------------------------
	def setSeparator(self,b):
		"""
		setSeparator(b)
			b=QtCore.bool

		If b is true then this action will be considered a separator.
		How a separator is represented depends on the widget it is inserted into
		Under most circumstances the text, submenu, and icon will be ignored for separator actions.
		"""
		res = super(QAction,self).setSeparator(b)
		return res
	#----------------------------------------------------------------------
	def setShortcut(self,shortcut):
		"""
		setShortcut(shortcut)
			shortcut=QtGui.QKeySequence

		This property holds the actions primary shortcut key.
		Valid keycodes for this property can be found in Qt.Key and Qt.Modifier
		There is no default shortcut key.
		"""
		res = super(QAction,self).setShortcut(shortcut)
		return res
	#----------------------------------------------------------------------
	def setShortcutContext(self,context):
		"""
		setShortcutContext(context)
			context=QtCore.Qt.ShortcutContext

		This property holds the context for the actions shortcut.
		Valid values for this property can be found in Qt.ShortcutContext
		The default value is Qt.WindowShortcut .
		"""
		res = super(QAction,self).setShortcutContext(context)
		return res
	#----------------------------------------------------------------------
	def setShortcuts(self,*args,**kwargs):
		"""
		setShortcuts(arg__1)
			arg__1=QtGui.QKeySequence.StandardKey

		setShortcuts(shortcuts)
			shortcuts=unKnown


		"""
		res = super(QAction,self).setShortcuts(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSoftKeyRole(self,softKeyRole):
		"""
		setSoftKeyRole(softKeyRole)
			softKeyRole=QtGui.QAction.SoftKeyRole

		This property holds the actions softkey role.
		This indicates what type of role this action describes in the softkey framework on platforms where such a framework is supported
		Currently this is only supported on the Symbian platform.
		The softkey role can be changed any time.
		"""
		res = super(QAction,self).setSoftKeyRole(softKeyRole)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,statusTip):
		"""
		setStatusTip(statusTip)
			statusTip=unicode

		This property holds the actions status tip.
		The status tip is displayed on all status bars provided by the actions top-level parent widget.
		By default, this property contains an empty string.
		"""
		res = super(QAction,self).setStatusTip(statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		This property holds the actions descriptive text.
		If the action is added to a menu, the menu option will consist of the icon (if there is one), the text, and the shortcut (if there is one)
		If the text is not explicitly set in the constructor, or by using PySide.QtGui.QAction.setText() , the actions description icon text will be used as text
		There is no default text.
		"""
		res = super(QAction,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,tip):
		"""
		setToolTip(tip)
			tip=unicode

		This property holds the actions tooltip.
		This text is used for the tooltip
		If no tooltip is specified, the actions text is used.
		By default, this property contains the actions text.
		"""
		res = super(QAction,self).setToolTip(tip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,what):
		"""
		setWhatsThis(what)
			what=unicode

		This property holds the actions Whats This? help text.
		The Whats This? text is used to provide a brief description of the action
		The text may contain rich text
		There is no default Whats This? text.
		"""
		res = super(QAction,self).setWhatsThis(what)
		return res
	#----------------------------------------------------------------------
	def showStatusText(self,widget=None):
		"""
		showStatusText(widget=None)
			widget=QtGui.QWidget

		Updates the relevant status bar for the widget specified by sending a PySide.QtGui.QStatusTipEvent to its parent widget
		Returns true if an event was sent; otherwise returns false.
		If a null widget is specified, the event is sent to the actions parent.
		"""
		res = super(QAction,self).showStatusText(widget)
		isinstance(res,QtCore.bool)
		return res
