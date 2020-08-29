from PySide import QtGui, QtCore

class QMenu(QtGui.QMenu):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMenu,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aboutToHide(self):
		"""

		"""
		res = super(QMenu,self).aboutToHide()
		return res
	#----------------------------------------------------------------------
	def aboutToShow(self):
		"""

		"""
		res = super(QMenu,self).aboutToShow()
		return res
	#----------------------------------------------------------------------
	def activeAction(self):
		"""
		Returns the currently highlighted action, or 0 if no action is currently highlighted.
		"""
		res = super(QMenu,self).activeAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def addSeparator(self):
		"""
		This convenience function creates a new separator action, i.e
		an action with QAction.isSeparator() returning true, and adds the new action to this menus list of actions
		It returns the newly created action.
		"""
		res = super(QMenu,self).addSeparator()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all the menus actions
		Actions owned by the menu and not shown in any other widget are deleted.
		"""
		res = super(QMenu,self).clear()
		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		If a menu does not fit on the screen it lays itself out so that it does fit
		It is style dependent what layout means (for example, on Windows it will use multiple columns).
		This functions returns the number of columns necessary.
		"""
		res = super(QMenu,self).columnCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def defaultAction(self):
		"""
		Returns the current default action.
		"""
		res = super(QMenu,self).defaultAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def exec_(self):
		"""
		Executes this menu synchronously.
		This is equivalent to exec(pos()) .
		This returns the triggered PySide.QtGui.QAction in either the popup menu or one of its submenus, or 0 if no item was triggered (normally because the user pressed Esc).
		In most situations youll want to specify the position yourself, for example, the current mouse position:
		or aligned to a widget:
		or in reaction to a PySide.QtGui.QMouseEvent *e:
		"""
		res = super(QMenu,self).exec_()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def hideTearOffMenu(self):
		"""
		This function will forcibly hide the torn off menu making it disappear from the users desktop.
		"""
		res = super(QMenu,self).hideTearOffMenu()
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds The icon of the menu.
		This is equivalent to the QAction.icon property of the PySide.QtGui.QMenu.menuAction() .
		By default, if no icon is explicitly set, this property contains a null icon.
		"""
		res = super(QMenu,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if there are no visible actions inserted into the menu, false otherwise.
		"""
		res = super(QMenu,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTearOffEnabled(self):
		"""
		This property holds whether the menu supports being torn off.
		When true, the menu contains a special tear-off item (often shown as a dashed line at the top of the menu) that creates a copy of the menu when it is triggered.
		This torn-off copy lives in a separate window
		It contains the same menu items as the original menu, with the exception of the tear-off handle.
		By default, this property is false.
		"""
		res = super(QMenu,self).isTearOffEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTearOffMenuVisible(self):
		"""
		When a menu is torn off a second menu is shown to display the menu contents in a new window
		When the menu is in this mode and the menu is visible returns true; otherwise false.
		"""
		res = super(QMenu,self).isTearOffMenuVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def menuAction(self):
		"""
		Returns the action associated with this menu.
		"""
		res = super(QMenu,self).menuAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def separatorsCollapsible(self):
		"""
		This property holds whether consecutive separators should be collapsed.
		This property specifies whether consecutive separators in the menu should be visually collapsed to a single one
		Separators at the beginning or the end of the menu are also hidden.
		By default, this property is true.
		"""
		res = super(QMenu,self).separatorsCollapsible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds The title of the menu.
		This is equivalent to the QAction.text property of the PySide.QtGui.QMenu.menuAction() .
		By default, this property contains an empty string.
		"""
		res = super(QMenu,self).title()
		return res
	#----------------------------------------------------------------------
	def actionAt(self,arg__1):
		"""
		actionAt(arg__1)
			arg__1=QtCore.QPoint

		Returns the item at pt ; returns 0 if there is no item there.
		"""
		res = super(QMenu,self).actionAt(arg__1)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def actionGeometry(self,arg__1):
		"""
		actionGeometry(arg__1)
			arg__1=QtGui.QAction

		Returns the geometry of action act .
		"""
		res = super(QMenu,self).actionGeometry(arg__1)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def addAction(self,*args,**kwargs):
		"""
		addAction(icon,text,receiver,member,shortcut=None)
			icon=QtGui.QIcon
			text=unicode
			receiver=QtCore.QObject
			member=str
			shortcut=QtGui.QKeySequence

		addAction(text)
			text=unicode

		addAction(icon,text)
			icon=QtGui.QIcon
			text=unicode

		addAction(arg__1,arg__2,arg__3=None)
			arg__1=unicode
			arg__2=Object
			arg__3=QtGui.QKeySequence

		addAction(arg__1,arg__2,arg__3,arg__4=None)
			arg__1=QtGui.QIcon
			arg__2=unicode
			arg__3=Object
			arg__4=QtGui.QKeySequence

		addAction(text,receiver,member,shortcut=None)
			text=unicode
			receiver=QtCore.QObject
			member=str
			shortcut=QtGui.QKeySequence

		This is an overloaded function.
		This convenience function creates a new action with an icon and some text and an optional shortcut shortcut
		The actions PySide.QtGui.QAction.triggered() signal is connected to the member slot of the receiver object
		The function adds the newly created action to the menus list of actions, and returns it.
		"""
		res = super(QMenu,self).addAction(*args,**kwargs)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def addMenu(self,*args,**kwargs):
		"""
		addMenu(icon,title)
			icon=QtGui.QIcon
			title=unicode

		addMenu(title)
			title=unicode

		addMenu(menu)
			menu=QtGui.QMenu

		Appends a new PySide.QtGui.QMenu with icon and title to the menu
		The menu takes ownership of the menu
		Returns the new menu.
		"""
		res = super(QMenu,self).addMenu(*args,**kwargs)
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def exec_(self,pos,at=None):
		"""
		exec_(pos,at=None)
			pos=QtCore.QPoint
			at=QtGui.QAction

		This is an overloaded function.
		Executes this menu synchronously.
		Pops up the menu so that the action action will be at the specified global position p
		To translate a widgets local coordinates into global coordinates, use QWidget.mapToGlobal() .
		This returns the triggered PySide.QtGui.QAction in either the popup menu or one of its submenus, or 0 if no item was triggered (normally because the user pressed Esc).
		Note that all signals are emitted as usual
		If you connect a PySide.QtGui.QAction to a slot and call the menus exec() , you get the result both via the signal-slot connection and in the return value of exec() .
		Common usage is to position the menu at the current mouse position:
		or aligned to a widget:
		or in reaction to a PySide.QtGui.QMouseEvent *e:
		When positioning a menu with exec() or PySide.QtGui.QMenu.popup() , bear in mind that you cannot rely on the menus current PySide.QtGui.QWidget.size()
		For performance reasons, the menu adapts its size only when necessary
		So in many cases, the size before and after the show is different
		Instead, use PySide.QtGui.QMenu.sizeHint() which calculates the proper size depending on the menus current contents.
		"""
		res = super(QMenu,self).exec_(pos,at)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option,action):
		"""
		initStyleOption(option,action)
			option=QtGui.QStyleOptionMenuItem
			action=QtGui.QAction

		Initialize option with the values from this menu and information from action
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionMenuItem , but dont want to fill in all the information themselves.
		"""
		res = super(QMenu,self).initStyleOption(option,action)
		return res
	#----------------------------------------------------------------------
	def insertMenu(self,before,menu):
		"""
		insertMenu(before,menu)
			before=QtGui.QAction
			menu=QtGui.QMenu

		This convenience function inserts menu before action before and returns the menus PySide.QtGui.QMenu.menuAction() .
		"""
		res = super(QMenu,self).insertMenu(before,menu)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def insertSeparator(self,before):
		"""
		insertSeparator(before)
			before=QtGui.QAction

		This convenience function creates a new separator action, i.e
		an action with QAction.isSeparator() returning true
		The function inserts the newly created action into this menus list of actions before action before and returns it.
		"""
		res = super(QMenu,self).insertSeparator(before)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def popup(self,pos,at=None):
		"""
		popup(pos,at=None)
			pos=QtCore.QPoint
			at=QtGui.QAction

		Displays the menu so that the action atAction will be at the specified global position p
		To translate a widgets local coordinates into global coordinates, use QWidget.mapToGlobal() .
		When positioning a menu with exec() or PySide.QtGui.QMenu.popup() , bear in mind that you cannot rely on the menus current PySide.QtGui.QWidget.size()
		For performance reasons, the menu adapts its size only when necessary, so in many cases, the size before and after the show is different
		Instead, use PySide.QtGui.QMenu.sizeHint() which calculates the proper size depending on the menus current contents.
		"""
		res = super(QMenu,self).popup(pos,at)
		return res
	#----------------------------------------------------------------------
	def setActiveAction(self,act):
		"""
		setActiveAction(act)
			act=QtGui.QAction

		Sets the currently highlighted action to act .
		"""
		res = super(QMenu,self).setActiveAction(act)
		return res
	#----------------------------------------------------------------------
	def setDefaultAction(self,arg__1):
		"""
		setDefaultAction(arg__1)
			arg__1=QtGui.QAction

		This sets the default action to act
		The default action may have a visual cue, depending on the current PySide.QtGui.QStyle
		A default action usually indicates what will happen by default when a drop occurs.
		"""
		res = super(QMenu,self).setDefaultAction(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		This property holds The icon of the menu.
		This is equivalent to the QAction.icon property of the PySide.QtGui.QMenu.menuAction() .
		By default, if no icon is explicitly set, this property contains a null icon.
		"""
		res = super(QMenu,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setSeparatorsCollapsible(self,collapse):
		"""
		setSeparatorsCollapsible(collapse)
			collapse=QtCore.bool

		This property holds whether consecutive separators should be collapsed.
		This property specifies whether consecutive separators in the menu should be visually collapsed to a single one
		Separators at the beginning or the end of the menu are also hidden.
		By default, this property is true.
		"""
		res = super(QMenu,self).setSeparatorsCollapsible(collapse)
		return res
	#----------------------------------------------------------------------
	def setTearOffEnabled(self,arg__1):
		"""
		setTearOffEnabled(arg__1)
			arg__1=QtCore.bool

		This property holds whether the menu supports being torn off.
		When true, the menu contains a special tear-off item (often shown as a dashed line at the top of the menu) that creates a copy of the menu when it is triggered.
		This torn-off copy lives in a separate window
		It contains the same menu items as the original menu, with the exception of the tear-off handle.
		By default, this property is false.
		"""
		res = super(QMenu,self).setTearOffEnabled(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTitle(self,title):
		"""
		setTitle(title)
			title=unicode

		This property holds The title of the menu.
		This is equivalent to the QAction.text property of the PySide.QtGui.QMenu.menuAction() .
		By default, this property contains an empty string.
		"""
		res = super(QMenu,self).setTitle(title)
		return res
