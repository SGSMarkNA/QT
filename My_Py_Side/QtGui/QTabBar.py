from PySide import QtGui, QtCore

class QTabBar(QtGui.QTabBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTabBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of tabs in the tab bar.
		"""
		res = super(QTabBar,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index of the tab bars visible tab.
		The current index is -1 if there is no current tab.
		"""
		res = super(QTabBar,self).currentIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def documentMode(self):
		"""
		This property holds Whether or not the tab bar is rendered in a mode suitable for the main window..
		This property is used as a hint for styles to draw the tabs in a different way then they would normally look in a tab widget
		On Mac OS X this will look similar to the tabs in Safari or Leopards Terminal.app.
		"""
		res = super(QTabBar,self).documentMode()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def drawBase(self):
		"""
		This property defines whether or not tab bar should draw its base..
		If true then PySide.QtGui.QTabBar draws a base in relation to the styles overlab
		Otherwise only the tabs are drawn.
		"""
		res = super(QTabBar,self).drawBase()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def elideMode(self):
		"""
		This property holds how to elide text in the tab bar.
		This property controls how items are elided when there is not enough space to show them for a given tab bar size.
		By default the value is style dependent.
		"""
		res = super(QTabBar,self).elideMode()
		isinstance(res,QtCore.Qt.TextElideMode)
		return res
	#----------------------------------------------------------------------
	def expanding(self):
		"""
		This property holds When expanding is true PySide.QtGui.QTabBar will expand the tabs to use the empty space..
		By default the value is true.
		"""
		res = super(QTabBar,self).expanding()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds The size for icons in the tab bar.
		The default value is style-dependent
		iconSize is a maximum size; icons that are smaller are not scaled up.
		"""
		res = super(QTabBar,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isMovable(self):
		"""
		This property holds This property holds whether the user can move the tabs within the tabbar area..
		By default, this property is false;
		"""
		res = super(QTabBar,self).isMovable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def selectionBehaviorOnRemove(self):
		"""
		This property holds What tab should be set as current when removeTab is called if the removed tab is also the current tab..
		By default the value is SelectRightTab .
		"""
		res = super(QTabBar,self).selectionBehaviorOnRemove()
		isinstance(res,QtGui.QTabBar.SelectionBehavior)
		return res
	#----------------------------------------------------------------------
	def shape(self):
		"""
		This property holds the shape of the tabs in the tab bar.
		Possible values for this property are described by the Shape enum.
		"""
		res = super(QTabBar,self).shape()
		isinstance(res,QtGui.QTabBar.Shape)
		return res
	#----------------------------------------------------------------------
	def tabLayoutChange(self):
		"""
		This virtual handler is called whenever the tab layout changes.
		"""
		res = super(QTabBar,self).tabLayoutChange()
		return res
	#----------------------------------------------------------------------
	def tabsClosable(self):
		"""
		This property holds Whether or not a tab bar should place close buttons on each tab.
		When PySide.QtGui.QTabBar.tabsClosable() is set to true a close button will appear on the tab on either the left or right hand side depending upon the style
		When the button is clicked the tab the signal tabCloseRequested will be emitted.
		By default the value is false.
		"""
		res = super(QTabBar,self).tabsClosable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def usesScrollButtons(self):
		"""
		This property holds Whether or not a tab bar should use buttons to scroll tabs when it has many tabs..
		When there are too many tabs in a tab bar for its size, the tab bar can either choose to expand its size or to add buttons that allow you to scroll through the tabs.
		By default the value is style dependant.
		"""
		res = super(QTabBar,self).usesScrollButtons()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def addTab(self,*args,**kwargs):
		"""
		addTab(text)
			text=unicode

		addTab(icon,text)
			icon=QtGui.QIcon
			text=unicode

		Adds a new tab with text text
		Returns the new tabs index.
		"""
		res = super(QTabBar,self).addTab(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option,tabIndex):
		"""
		initStyleOption(option,tabIndex)
			option=QtGui.QStyleOptionTab
			tabIndex=QtCore.int

		Initialize option with the values from the tab at tabIndex
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionTab , PySide.QtGui.QStyleOptionTabV2 , or PySide.QtGui.QStyleOptionTabV3 but dont want to fill in all the information themselves
		This function will check the version of the PySide.QtGui.QStyleOptionTab and fill in the additional values for a PySide.QtGui.QStyleOptionTabV2 and PySide.QtGui.QStyleOptionTabV3 .
		"""
		res = super(QTabBar,self).initStyleOption(option,tabIndex)
		return res
	#----------------------------------------------------------------------
	def insertTab(self,*args,**kwargs):
		"""
		insertTab(index,text)
			index=QtCore.int
			text=unicode

		insertTab(index,icon,text)
			index=QtCore.int
			icon=QtGui.QIcon
			text=unicode

		Inserts a new tab with text text at position index
		If index is out of range, the new tab is appened
		Returns the new tabs index.
		"""
		res = super(QTabBar,self).insertTab(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isTabEnabled(self,index):
		"""
		isTabEnabled(index)
			index=QtCore.int

		Returns true if the tab at position index is enabled; otherwise returns false.
		"""
		res = super(QTabBar,self).isTabEnabled(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def moveTab(self,from,to):
		"""
		moveTab(from,to)
			from=QtCore.int
			to=QtCore.int

		Moves the item at index position from to index position to .
		"""
		res = super(QTabBar,self).moveTab(from,to)
		return res
	#----------------------------------------------------------------------
	def removeTab(self,index):
		"""
		removeTab(index)
			index=QtCore.int

		Removes the tab at position index .
		"""
		res = super(QTabBar,self).removeTab(index)
		return res
	#----------------------------------------------------------------------
	def setDocumentMode(self,set):
		"""
		setDocumentMode(set)
			set=QtCore.bool

		This property holds Whether or not the tab bar is rendered in a mode suitable for the main window..
		This property is used as a hint for styles to draw the tabs in a different way then they would normally look in a tab widget
		On Mac OS X this will look similar to the tabs in Safari or Leopards Terminal.app.
		"""
		res = super(QTabBar,self).setDocumentMode(set)
		return res
	#----------------------------------------------------------------------
	def setDrawBase(self,drawTheBase):
		"""
		setDrawBase(drawTheBase)
			drawTheBase=QtCore.bool

		This property defines whether or not tab bar should draw its base..
		If true then PySide.QtGui.QTabBar draws a base in relation to the styles overlab
		Otherwise only the tabs are drawn.
		"""
		res = super(QTabBar,self).setDrawBase(drawTheBase)
		return res
	#----------------------------------------------------------------------
	def setElideMode(self,arg__1):
		"""
		setElideMode(arg__1)
			arg__1=QtCore.Qt.TextElideMode

		This property holds how to elide text in the tab bar.
		This property controls how items are elided when there is not enough space to show them for a given tab bar size.
		By default the value is style dependent.
		"""
		res = super(QTabBar,self).setElideMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setExpanding(self,enabled):
		"""
		setExpanding(enabled)
			enabled=QtCore.bool

		This property holds When expanding is true PySide.QtGui.QTabBar will expand the tabs to use the empty space..
		By default the value is true.
		"""
		res = super(QTabBar,self).setExpanding(enabled)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QtCore.QSize

		This property holds The size for icons in the tab bar.
		The default value is style-dependent
		iconSize is a maximum size; icons that are smaller are not scaled up.
		"""
		res = super(QTabBar,self).setIconSize(size)
		return res
	#----------------------------------------------------------------------
	def setMovable(self,movable):
		"""
		setMovable(movable)
			movable=QtCore.bool

		This property holds This property holds whether the user can move the tabs within the tabbar area..
		By default, this property is false;
		"""
		res = super(QTabBar,self).setMovable(movable)
		return res
	#----------------------------------------------------------------------
	def setSelectionBehaviorOnRemove(self,behavior):
		"""
		setSelectionBehaviorOnRemove(behavior)
			behavior=QtGui.QTabBar.SelectionBehavior

		This property holds What tab should be set as current when removeTab is called if the removed tab is also the current tab..
		By default the value is SelectRightTab .
		"""
		res = super(QTabBar,self).setSelectionBehaviorOnRemove(behavior)
		return res
	#----------------------------------------------------------------------
	def setShape(self,shape):
		"""
		setShape(shape)
			shape=QtGui.QTabBar.Shape

		This property holds the shape of the tabs in the tab bar.
		Possible values for this property are described by the Shape enum.
		"""
		res = super(QTabBar,self).setShape(shape)
		return res
	#----------------------------------------------------------------------
	def setTabButton(self,index,position,widget):
		"""
		setTabButton(index,position,widget)
			index=QtCore.int
			position=QtGui.QTabBar.ButtonPosition
			widget=QtGui.QWidget

		Sets widget on the tab index
		The widget is placed on the left or right hand side depending upon the position .
		Any previously set widget in position is hidden.
		The tab bar will take ownership of the widget and so all widgets set here will be deleted by the tab bar when it is destroyed unless you separately reparent the widget after setting some other widget (or 0).
		"""
		res = super(QTabBar,self).setTabButton(index,position,widget)
		return res
	#----------------------------------------------------------------------
	def setTabData(self,index,data):
		"""
		setTabData(index,data)
			index=QtCore.int
			data=object

		Sets the data of the tab at position index to data .
		"""
		res = super(QTabBar,self).setTabData(index,data)
		return res
	#----------------------------------------------------------------------
	def setTabEnabled(self,index,arg__2):
		"""
		setTabEnabled(index,arg__2)
			index=QtCore.int
			arg__2=QtCore.bool

		If enabled is true then the tab at position index is enabled; otherwise the item at position index is disabled.
		"""
		res = super(QTabBar,self).setTabEnabled(index,arg__2)
		return res
	#----------------------------------------------------------------------
	def setTabIcon(self,index,icon):
		"""
		setTabIcon(index,icon)
			index=QtCore.int
			icon=QtGui.QIcon

		Sets the icon of the tab at position index to icon .
		"""
		res = super(QTabBar,self).setTabIcon(index,icon)
		return res
	#----------------------------------------------------------------------
	def setTabText(self,index,text):
		"""
		setTabText(index,text)
			index=QtCore.int
			text=unicode

		Sets the text of the tab at position index to text .
		"""
		res = super(QTabBar,self).setTabText(index,text)
		return res
	#----------------------------------------------------------------------
	def setTabTextColor(self,index,color):
		"""
		setTabTextColor(index,color)
			index=QtCore.int
			color=QtGui.QColor

		Sets the color of the text in the tab with the given index to the specified color .
		If an invalid color is specified, the tab will use the PySide.QtGui.QTabBar foreground role instead.
		"""
		res = super(QTabBar,self).setTabTextColor(index,color)
		return res
	#----------------------------------------------------------------------
	def setTabToolTip(self,index,tip):
		"""
		setTabToolTip(index,tip)
			index=QtCore.int
			tip=unicode

		Sets the tool tip of the tab at position index to tip .
		"""
		res = super(QTabBar,self).setTabToolTip(index,tip)
		return res
	#----------------------------------------------------------------------
	def setTabWhatsThis(self,index,text):
		"""
		setTabWhatsThis(index,text)
			index=QtCore.int
			text=unicode

		Sets the Whats This help text of the tab at position index to text .
		"""
		res = super(QTabBar,self).setTabWhatsThis(index,text)
		return res
	#----------------------------------------------------------------------
	def setTabsClosable(self,closable):
		"""
		setTabsClosable(closable)
			closable=QtCore.bool

		This property holds Whether or not a tab bar should place close buttons on each tab.
		When PySide.QtGui.QTabBar.tabsClosable() is set to true a close button will appear on the tab on either the left or right hand side depending upon the style
		When the button is clicked the tab the signal tabCloseRequested will be emitted.
		By default the value is false.
		"""
		res = super(QTabBar,self).setTabsClosable(closable)
		return res
	#----------------------------------------------------------------------
	def setUsesScrollButtons(self,useButtons):
		"""
		setUsesScrollButtons(useButtons)
			useButtons=QtCore.bool

		This property holds Whether or not a tab bar should use buttons to scroll tabs when it has many tabs..
		When there are too many tabs in a tab bar for its size, the tab bar can either choose to expand its size or to add buttons that allow you to scroll through the tabs.
		By default the value is style dependant.
		"""
		res = super(QTabBar,self).setUsesScrollButtons(useButtons)
		return res
	#----------------------------------------------------------------------
	def tabAt(self,pos):
		"""
		tabAt(pos)
			pos=QtCore.QPoint

		Returns the index of the tab that covers position or -1 if no tab covers position ;
		"""
		res = super(QTabBar,self).tabAt(pos)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def tabButton(self,index,position):
		"""
		tabButton(index,position)
			index=QtCore.int
			position=QtGui.QTabBar.ButtonPosition

		Returns the widget set a tab index and position or 0 if one is not set.
		"""
		res = super(QTabBar,self).tabButton(index,position)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def tabData(self,index):
		"""
		tabData(index)
			index=QtCore.int

		Returns the data of the tab at position index , or a null variant if index is out of range.
		"""
		res = super(QTabBar,self).tabData(index)
		return res
	#----------------------------------------------------------------------
	def tabIcon(self,index):
		"""
		tabIcon(index)
			index=QtCore.int

		Returns the icon of the tab at position index , or a null icon if index is out of range.
		"""
		res = super(QTabBar,self).tabIcon(index)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def tabInserted(self,index):
		"""
		tabInserted(index)
			index=QtCore.int

		This virtual handler is called after a new tab was added or inserted at position index .
		"""
		res = super(QTabBar,self).tabInserted(index)
		return res
	#----------------------------------------------------------------------
	def tabRect(self,index):
		"""
		tabRect(index)
			index=QtCore.int

		Returns the visual rectangle of the tab at position index , or a null rectangle if index is out of range.
		"""
		res = super(QTabBar,self).tabRect(index)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def tabRemoved(self,index):
		"""
		tabRemoved(index)
			index=QtCore.int

		This virtual handler is called after a tab was removed from position index .
		"""
		res = super(QTabBar,self).tabRemoved(index)
		return res
	#----------------------------------------------------------------------
	def tabSizeHint(self,index):
		"""
		tabSizeHint(index)
			index=QtCore.int

		Returns the size hint for the tab at position index .
		"""
		res = super(QTabBar,self).tabSizeHint(index)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def tabText(self,index):
		"""
		tabText(index)
			index=QtCore.int

		Returns the text of the tab at position index , or an empty string if index is out of range.
		"""
		res = super(QTabBar,self).tabText(index)
		return res
	#----------------------------------------------------------------------
	def tabTextColor(self,index):
		"""
		tabTextColor(index)
			index=QtCore.int

		Returns the text color of the tab with the given index , or a invalid color if index is out of range.
		"""
		res = super(QTabBar,self).tabTextColor(index)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def tabToolTip(self,index):
		"""
		tabToolTip(index)
			index=QtCore.int

		Returns the tool tip of the tab at position index , or an empty string if index is out of range.
		"""
		res = super(QTabBar,self).tabToolTip(index)
		return res
	#----------------------------------------------------------------------
	def tabWhatsThis(self,index):
		"""
		tabWhatsThis(index)
			index=QtCore.int

		Returns the Whats This help text of the tab at position index , or an empty string if index is out of range.
		"""
		res = super(QTabBar,self).tabWhatsThis(index)
		return res
