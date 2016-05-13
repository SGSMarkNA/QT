from PySide import QtGui, QtCore

class QTabWidget(QtGui.QTabWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTabWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all the pages, but does not delete them
		Calling this function is equivalent to calling PySide.QtGui.QTabWidget.removeTab() until the tab widget is empty.
		"""
		res = super(QTabWidget,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of tabs in the tab bar.
		By default, this property contains a value of 0.
		"""
		res = super(QTabWidget,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index position of the current tab page.
		The current index is -1 if there is no current widget.
		By default, this property contains a value of -1 because there are initially no tabs in the widget.
		"""
		res = super(QTabWidget,self).currentIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentWidget(self):
		"""
		Returns a pointer to the page currently being displayed by the tab dialog
		The tab dialog does its best to make sure that this value is never 0 (but if you try hard enough, it can be).
		"""
		res = super(QTabWidget,self).currentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def documentMode(self):
		"""
		This property holds Whether or not the tab widget is rendered in a mode suitable for document pages
		This is the same as document mode on Mac OS X..
		When this property is set the tab widget frame is not rendered
		This mode is useful for showing document-type pages where the page covers most of the tab widget area.
		"""
		res = super(QTabWidget,self).documentMode()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def elideMode(self):
		"""
		This property holds how to elide text in the tab bar.
		This property controls how items are elided when there is not enough space to show them for a given tab bar size.
		By default the value is style dependant.
		"""
		res = super(QTabWidget,self).elideMode()
		isinstance(res,QtCore.Qt.TextElideMode)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds The size for icons in the tab bar.
		The default value is style-dependent
		This is the maximum size that the icons will have
		Icons are not scaled up if they are of smaller size.
		"""
		res = super(QTabWidget,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isMovable(self):
		"""
		This property holds This property holds whether the user can move the tabs within the tabbar area..
		By default, this property is false;
		"""
		res = super(QTabWidget,self).isMovable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def tabBar(self):
		"""
		Returns the current PySide.QtGui.QTabBar .
		"""
		res = super(QTabWidget,self).tabBar()
		isinstance(res,QtGui.QTabBar)
		return res
	#----------------------------------------------------------------------
	def tabPosition(self):
		"""
		This property holds the position of the tabs in this tab widget.
		Possible values for this property are described by the QTabWidget.TabPosition enum.
		By default, this property is set to North .
		"""
		res = super(QTabWidget,self).tabPosition()
		isinstance(res,QtGui.QTabWidget.TabPosition)
		return res
	#----------------------------------------------------------------------
	def tabShape(self):
		"""
		This property holds the shape of the tabs in this tab widget.
		Possible values for this property are QTabWidget.Rounded (default) or QTabWidget.Triangular .
		"""
		res = super(QTabWidget,self).tabShape()
		isinstance(res,QtGui.QTabWidget.TabShape)
		return res
	#----------------------------------------------------------------------
	def tabsClosable(self):
		"""
		This property holds whether close buttons are automatically added to each tab..
		"""
		res = super(QTabWidget,self).tabsClosable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def usesScrollButtons(self):
		"""
		This property holds Whether or not a tab bar should use buttons to scroll tabs when it has many tabs..
		When there are too many tabs in a tab bar for its size, the tab bar can either choose to expand its size or to add buttons that allow you to scroll through the tabs.
		By default the value is style dependant.
		"""
		res = super(QTabWidget,self).usesScrollButtons()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def addTab(self,*args,**kwargs):
		"""
		addTab(widget,arg__2)
			widget=QtGui.QWidget
			arg__2=unicode

		addTab(widget,icon,label)
			widget=QtGui.QWidget
			icon=QtGui.QIcon
			label=unicode

		Adds a tab with the given page and label to the tab widget, and returns the index of the tab in the tab bar.
		If the tabs label contains an ampersand, the letter following the ampersand is used as a shortcut for the tab, e.g
		if the label is Bro&wse then Alt+W becomes a shortcut which will move the focus to this tab.
		"""
		res = super(QTabWidget,self).addTab(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def cornerWidget(self,corner=None):
		"""
		cornerWidget(corner=None)
			corner=QtCore.Qt.Corner


		"""
		res = super(QTabWidget,self).cornerWidget(corner)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,widget):
		"""
		indexOf(widget)
			widget=QtGui.QWidget

		Returns the index position of the page occupied by the widget w , or -1 if the widget cannot be found.
		"""
		res = super(QTabWidget,self).indexOf(widget)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionTabWidgetFrame

		Initialize option with the values from this PySide.QtGui.QTabWidget
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionTabWidgetFrame , but dont want to fill in all the information themselves.
		"""
		res = super(QTabWidget,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def insertTab(self,*args,**kwargs):
		"""
		insertTab(index,widget,arg__3)
			index=QtCore.int
			widget=QtGui.QWidget
			arg__3=unicode

		insertTab(index,widget,icon,label)
			index=QtCore.int
			widget=QtGui.QWidget
			icon=QtGui.QIcon
			label=unicode

		Inserts a tab with the given label and page into the tab widget at the specified index , and returns the index of the inserted tab in the tab bar.
		The label is displayed in the tab and may vary in appearance depending on the configuration of the tab widget.
		If the tabs label contains an ampersand, the letter following the ampersand is used as a shortcut for the tab, e.g
		if the label is Bro&wse then Alt+W becomes a shortcut which will move the focus to this tab.
		If index is out of range, the tab is simply appended
		Otherwise it is inserted at the specified position.
		If the PySide.QtGui.QTabWidget was empty before this function is called, the new page becomes the current page
		Inserting a new tab at an index less than or equal to the current index will increment the current index, but keep the current page.
		"""
		res = super(QTabWidget,self).insertTab(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isTabEnabled(self,index):
		"""
		isTabEnabled(index)
			index=QtCore.int

		Returns true if the page at position index is enabled; otherwise returns false.
		"""
		res = super(QTabWidget,self).isTabEnabled(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def removeTab(self,index):
		"""
		removeTab(index)
			index=QtCore.int

		Removes the tab at position index from this stack of widgets
		The page widget itself is not deleted.
		"""
		res = super(QTabWidget,self).removeTab(index)
		return res
	#----------------------------------------------------------------------
	def setCornerWidget(self,w,corner=None):
		"""
		setCornerWidget(w,corner=None)
			w=QtGui.QWidget
			corner=QtCore.Qt.Corner


		"""
		res = super(QTabWidget,self).setCornerWidget(w,corner)
		return res
	#----------------------------------------------------------------------
	def setDocumentMode(self,set):
		"""
		setDocumentMode(set)
			set=QtCore.bool

		This property holds Whether or not the tab widget is rendered in a mode suitable for document pages
		This is the same as document mode on Mac OS X..
		When this property is set the tab widget frame is not rendered
		This mode is useful for showing document-type pages where the page covers most of the tab widget area.
		"""
		res = super(QTabWidget,self).setDocumentMode(set)
		return res
	#----------------------------------------------------------------------
	def setElideMode(self,arg__1):
		"""
		setElideMode(arg__1)
			arg__1=QtCore.Qt.TextElideMode

		This property holds how to elide text in the tab bar.
		This property controls how items are elided when there is not enough space to show them for a given tab bar size.
		By default the value is style dependant.
		"""
		res = super(QTabWidget,self).setElideMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,size):
		"""
		setIconSize(size)
			size=QtCore.QSize

		This property holds The size for icons in the tab bar.
		The default value is style-dependent
		This is the maximum size that the icons will have
		Icons are not scaled up if they are of smaller size.
		"""
		res = super(QTabWidget,self).setIconSize(size)
		return res
	#----------------------------------------------------------------------
	def setMovable(self,movable):
		"""
		setMovable(movable)
			movable=QtCore.bool

		This property holds This property holds whether the user can move the tabs within the tabbar area..
		By default, this property is false;
		"""
		res = super(QTabWidget,self).setMovable(movable)
		return res
	#----------------------------------------------------------------------
	def setTabBar(self,arg__1):
		"""
		setTabBar(arg__1)
			arg__1=QtGui.QTabBar

		Replaces the dialogs PySide.QtGui.QTabBar heading with the tab bar tb
		Note that this must be called before any tabs have been added, or the behavior is undefined.
		"""
		res = super(QTabWidget,self).setTabBar(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTabEnabled(self,index,arg__2):
		"""
		setTabEnabled(index,arg__2)
			index=QtCore.int
			arg__2=QtCore.bool

		If enable is true, the page at position index is enabled; otherwise the page at position index is disabled
		The pages tab is redrawn appropriately.
		PySide.QtGui.QTabWidget uses QWidget.setEnabled() internally, rather than keeping a separate flag.
		Note that even a disabled tab/page may be visible
		If the page is visible already, PySide.QtGui.QTabWidget will not hide it; if all the pages are disabled, PySide.QtGui.QTabWidget will show one of them.
		"""
		res = super(QTabWidget,self).setTabEnabled(index,arg__2)
		return res
	#----------------------------------------------------------------------
	def setTabIcon(self,index,icon):
		"""
		setTabIcon(index,icon)
			index=QtCore.int
			icon=QtGui.QIcon

		This is an overloaded function.
		Sets the icon for the tab at position index .
		"""
		res = super(QTabWidget,self).setTabIcon(index,icon)
		return res
	#----------------------------------------------------------------------
	def setTabPosition(self,arg__1):
		"""
		setTabPosition(arg__1)
			arg__1=QtGui.QTabWidget.TabPosition

		This property holds the position of the tabs in this tab widget.
		Possible values for this property are described by the QTabWidget.TabPosition enum.
		By default, this property is set to North .
		"""
		res = super(QTabWidget,self).setTabPosition(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTabShape(self,s):
		"""
		setTabShape(s)
			s=QtGui.QTabWidget.TabShape

		This property holds the shape of the tabs in this tab widget.
		Possible values for this property are QTabWidget.Rounded (default) or QTabWidget.Triangular .
		"""
		res = super(QTabWidget,self).setTabShape(s)
		return res
	#----------------------------------------------------------------------
	def setTabText(self,index,arg__2):
		"""
		setTabText(index,arg__2)
			index=QtCore.int
			arg__2=unicode

		Defines a new label for the page at position index s tab.
		If the provided text contains an ampersand character (&), a shortcut is automatically created for it
		The character that follows the & will be used as the shortcut key
		Any previous shortcut will be overwritten, or cleared if no shortcut is defined by the text
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		"""
		res = super(QTabWidget,self).setTabText(index,arg__2)
		return res
	#----------------------------------------------------------------------
	def setTabToolTip(self,index,tip):
		"""
		setTabToolTip(index,tip)
			index=QtCore.int
			tip=unicode

		Sets the tab tool tip for the page at position index to tip .
		"""
		res = super(QTabWidget,self).setTabToolTip(index,tip)
		return res
	#----------------------------------------------------------------------
	def setTabWhatsThis(self,index,text):
		"""
		setTabWhatsThis(index,text)
			index=QtCore.int
			text=unicode

		Sets the Whats This help text for the page at position index to text .
		"""
		res = super(QTabWidget,self).setTabWhatsThis(index,text)
		return res
	#----------------------------------------------------------------------
	def setTabsClosable(self,closeable):
		"""
		setTabsClosable(closeable)
			closeable=QtCore.bool

		This property holds whether close buttons are automatically added to each tab..
		"""
		res = super(QTabWidget,self).setTabsClosable(closeable)
		return res
	#----------------------------------------------------------------------
	def setUpLayout(self,arg__1=None):
		"""
		setUpLayout(arg__1=None)
			arg__1=QtCore.bool


		"""
		res = super(QTabWidget,self).setUpLayout(arg__1)
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
		res = super(QTabWidget,self).setUsesScrollButtons(useButtons)
		return res
	#----------------------------------------------------------------------
	def tabIcon(self,index):
		"""
		tabIcon(index)
			index=QtCore.int

		Returns the icon for the tab on the page at position index .
		"""
		res = super(QTabWidget,self).tabIcon(index)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def tabInserted(self,index):
		"""
		tabInserted(index)
			index=QtCore.int

		This virtual handler is called after a new tab was added or inserted at position index .
		"""
		res = super(QTabWidget,self).tabInserted(index)
		return res
	#----------------------------------------------------------------------
	def tabRemoved(self,index):
		"""
		tabRemoved(index)
			index=QtCore.int

		This virtual handler is called after a tab was removed from position index .
		"""
		res = super(QTabWidget,self).tabRemoved(index)
		return res
	#----------------------------------------------------------------------
	def tabText(self,index):
		"""
		tabText(index)
			index=QtCore.int

		Returns the label text for the tab on the page at position index .
		"""
		res = super(QTabWidget,self).tabText(index)
		return res
	#----------------------------------------------------------------------
	def tabToolTip(self,index):
		"""
		tabToolTip(index)
			index=QtCore.int

		Returns the tab tool tip for the page at position index or an empty string if no tool tip has been set.
		"""
		res = super(QTabWidget,self).tabToolTip(index)
		return res
	#----------------------------------------------------------------------
	def tabWhatsThis(self,index):
		"""
		tabWhatsThis(index)
			index=QtCore.int

		Returns the Whats This help text for the page at position index , or an empty string if no help text has been set.
		"""
		res = super(QTabWidget,self).tabWhatsThis(index)
		return res
	#----------------------------------------------------------------------
	def widget(self,index):
		"""
		widget(index)
			index=QtCore.int

		Returns the tab page at index position index or 0 if the index is out of range.
		"""
		res = super(QTabWidget,self).widget(index)
		isinstance(res,QtGui.QWidget)
		return res
