from PySide import QtGui, QtCore

class QMainWindow(QtGui.QMainWindow):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMainWindow,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def centralWidget(self):
		"""
		Returns the central widget for the main window
		This function returns zero if the central widget has not been set.
		"""
		res = super(QMainWindow,self).centralWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def createPopupMenu(self):
		"""
		Returns a popup menu containing checkable entries for the toolbars and dock widgets present in the main window
		If there are no toolbars and dock widgets present, this function returns a null pointer.
		By default, this function is called by the main window when the user activates a context menu, typically by right-clicking on a toolbar or a dock widget.
		If you want to create a custom popup menu, reimplement this function and return a newly-created popup menu
		Ownership of the popup menu is transferred to the caller.
		"""
		res = super(QMainWindow,self).createPopupMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def dockOptions(self):
		"""
		This property holds the docking behavior of PySide.QtGui.QMainWindow .
		The default value is AnimatedDocks | AllowTabbedDocks .
		"""
		res = super(QMainWindow,self).dockOptions()
		isinstance(res,QtGui.QMainWindow.DockOptions)
		return res
	#----------------------------------------------------------------------
	def documentMode(self):
		"""
		This property holds whether the tab bar for tabbed dockwidgets is set to document mode..
		The default is false.
		"""
		res = super(QMainWindow,self).documentMode()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds size of toolbar icons in this mainwindow..
		The default is the default tool bar icon size of the GUI style
		Note that the icons used must be at least of this size as the icons are only scaled down.
		"""
		res = super(QMainWindow,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isAnimated(self):
		"""
		This property holds whether manipulating dock widgets and tool bars is animated.
		When a dock widget or tool bar is dragged over the main window, the main window adjusts its contents to indicate where the dock widget or tool bar will be docked if it is dropped
		Setting this property causes PySide.QtGui.QMainWindow to move its contents in a smooth animation
		Clearing this property causes the contents to snap into their new positions.
		By default, this property is set
		It may be cleared if the main window contains widgets which are slow at resizing or repainting themselves.
		Setting this property is identical to setting the AnimatedDocks option using PySide.QtGui.QMainWindow.setDockOptions() .
		"""
		res = super(QMainWindow,self).isAnimated()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isDockNestingEnabled(self):
		"""
		This property holds whether docks can be nested.
		If this property is false, dock areas can only contain a single row (horizontal or vertical) of dock widgets
		If this property is true, the area occupied by a dock widget can be split in either direction to contain more dock widgets.
		Dock nesting is only necessary in applications that contain a lot of dock widgets
		It gives the user greater freedom in organizing their main window
		However, dock nesting leads to more complex (and less intuitive) behavior when a dock widget is dragged over the main window, since there are more ways in which a dropped dock widget may be placed in the dock area.
		Setting this property is identical to setting the AllowNestedDocks option using PySide.QtGui.QMainWindow.setDockOptions() .
		"""
		res = super(QMainWindow,self).isDockNestingEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def menuBar(self):
		"""
		Returns the menu bar for the main window
		This function creates and returns an empty menu bar if the menu bar does not exist.
		If you want all windows in a Mac application to share one menu bar, dont use this function to create it, because the menu bar created here will have this PySide.QtGui.QMainWindow as its parent
		Instead, you must create a menu bar that does not have a parent, which you can then share among all the Mac windows
		Create a parent-less menu bar this way:
		"""
		res = super(QMainWindow,self).menuBar()
		isinstance(res,QtGui.QMenuBar)
		return res
	#----------------------------------------------------------------------
	def menuWidget(self):
		"""
		Returns the menu bar for the main window
		This function returns null if a menu bar hasnt been constructed yet.
		"""
		res = super(QMainWindow,self).menuWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def statusBar(self):
		"""
		Returns the status bar for the main window
		This function creates and returns an empty status bar if the status bar does not exist.
		"""
		res = super(QMainWindow,self).statusBar()
		isinstance(res,QtGui.QStatusBar)
		return res
	#----------------------------------------------------------------------
	def tabShape(self):
		"""
		This property holds the tab shape used for tabbed dock widgets..
		The default is QTabWidget.Rounded .
		"""
		res = super(QMainWindow,self).tabShape()
		isinstance(res,QtGui.QTabWidget.TabShape)
		return res
	#----------------------------------------------------------------------
	def toolButtonStyle(self):
		"""
		This property holds style of toolbar buttons in this mainwindow..
		The default is Qt.ToolButtonIconOnly .
		"""
		res = super(QMainWindow,self).toolButtonStyle()
		isinstance(res,QtCore.Qt.ToolButtonStyle)
		return res
	#----------------------------------------------------------------------
	def unifiedTitleAndToolBarOnMac(self):
		"""
		This property holds whether the window uses the unified title and toolbar look on Mac OS X.
		This property is false by default and only has any effect on Mac OS X 10.4 or higher.
		If set to true, then the top toolbar area is replaced with a Carbon HIToolbar or a Cocoa NSToolbar (depending on whether Qt was built with Carbon or Cocoa)
		All toolbars in the top toolbar area and any toolbars added afterwards are moved to that
		This means a couple of things.
		Setting this back to false will remove these restrictions.
		The Qt.WA_MacBrushedMetal attribute takes precedence over this property.
		"""
		res = super(QMainWindow,self).unifiedTitleAndToolBarOnMac()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def addDockWidget(self,*args,**kwargs):
		"""
		addDockWidget(area,dockwidget,orientation)
			area=QtCore.Qt.DockWidgetArea
			dockwidget=QtGui.QDockWidget
			orientation=QtCore.Qt.Orientation

		addDockWidget(area,dockwidget)
			area=QtCore.Qt.DockWidgetArea
			dockwidget=QtGui.QDockWidget


		"""
		res = super(QMainWindow,self).addDockWidget(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addToolBar(self,*args,**kwargs):
		"""
		addToolBar(area,toolbar)
			area=QtCore.Qt.ToolBarArea
			toolbar=QtGui.QToolBar

		addToolBar(title)
			title=unicode

		addToolBar(toolbar)
			toolbar=QtGui.QToolBar


		"""
		res = super(QMainWindow,self).addToolBar(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addToolBarBreak(self,area=None):
		"""
		addToolBarBreak(area=None)
			area=QtCore.Qt.ToolBarArea


		"""
		res = super(QMainWindow,self).addToolBarBreak(area)
		return res
	#----------------------------------------------------------------------
	def corner(self,corner):
		"""
		corner(corner)
			corner=QtCore.Qt.Corner


		"""
		res = super(QMainWindow,self).corner(corner)
		isinstance(res,QtCore.Qt.DockWidgetArea)
		return res
	#----------------------------------------------------------------------
	def dockWidgetArea(self,dockwidget):
		"""
		dockWidgetArea(dockwidget)
			dockwidget=QtGui.QDockWidget

		Returns the Qt.DockWidgetArea for dockwidget
		If dockwidget has not been added to the main window, this function returns Qt::NoDockWidgetArea .
		"""
		res = super(QMainWindow,self).dockWidgetArea(dockwidget)
		isinstance(res,QtCore.Qt.DockWidgetArea)
		return res
	#----------------------------------------------------------------------
	def insertToolBar(self,before,toolbar):
		"""
		insertToolBar(before,toolbar)
			before=QtGui.QToolBar
			toolbar=QtGui.QToolBar

		Inserts the toolbar into the area occupied by the before toolbar so that it appears before it
		For example, in normal left-to-right layout operation, this means that toolbar will appear to the left of the toolbar specified by before in a horizontal toolbar area.
		"""
		res = super(QMainWindow,self).insertToolBar(before,toolbar)
		return res
	#----------------------------------------------------------------------
	def insertToolBarBreak(self,before):
		"""
		insertToolBarBreak(before)
			before=QtGui.QToolBar

		Inserts a toolbar break before the toolbar specified by before .
		"""
		res = super(QMainWindow,self).insertToolBarBreak(before)
		return res
	#----------------------------------------------------------------------
	def isSeparator(self,pos):
		"""
		isSeparator(pos)
			pos=QtCore.QPoint


		"""
		res = super(QMainWindow,self).isSeparator(pos)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def removeDockWidget(self,dockwidget):
		"""
		removeDockWidget(dockwidget)
			dockwidget=QtGui.QDockWidget

		Removes the dockwidget from the main window layout and hides it
		Note that the dockwidget is not deleted.
		"""
		res = super(QMainWindow,self).removeDockWidget(dockwidget)
		return res
	#----------------------------------------------------------------------
	def removeToolBar(self,toolbar):
		"""
		removeToolBar(toolbar)
			toolbar=QtGui.QToolBar

		Removes the toolbar from the main window layout and hides it
		Note that the toolbar is not deleted.
		"""
		res = super(QMainWindow,self).removeToolBar(toolbar)
		return res
	#----------------------------------------------------------------------
	def removeToolBarBreak(self,before):
		"""
		removeToolBarBreak(before)
			before=QtGui.QToolBar

		Removes a toolbar break previously inserted before the toolbar specified by before .
		"""
		res = super(QMainWindow,self).removeToolBarBreak(before)
		return res
	#----------------------------------------------------------------------
	def restoreDockWidget(self,dockwidget):
		"""
		restoreDockWidget(dockwidget)
			dockwidget=QtGui.QDockWidget

		Restores the state of dockwidget if it is created after the call to PySide.QtGui.QMainWindow.restoreState()
		Returns true if the state was restored; otherwise returns false.
		"""
		res = super(QMainWindow,self).restoreDockWidget(dockwidget)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def restoreState(self,state,version=None):
		"""
		restoreState(state,version=None)
			state=QtCore.QByteArray
			version=QtCore.int

		Restores the state of this mainwindows toolbars and dockwidgets
		The version number is compared with that stored in state
		If they do not match, the mainwindows state is left unchanged, and this function returns false ; otherwise, the state is restored, and this function returns true .
		To restore geometry saved using PySide.QtCore.QSettings , you can use code like this:
		"""
		res = super(QMainWindow,self).restoreState(state,version)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def saveState(self,version=None):
		"""
		saveState(version=None)
			version=QtCore.int

		Saves the current state of this mainwindows toolbars and dockwidgets
		The version number is stored as part of the data.
		The PySide.QtCore.QObject.objectName() property is used to identify each PySide.QtGui.QToolBar and PySide.QtGui.QDockWidget
		You should make sure that this property is unique for each PySide.QtGui.QToolBar and PySide.QtGui.QDockWidget you add to the PySide.QtGui.QMainWindow
		To restore the saved state, pass the return value and version number to PySide.QtGui.QMainWindow.restoreState() .
		To save the geometry when the window closes, you can implement a close event like this:
		"""
		res = super(QMainWindow,self).saveState(version)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setCentralWidget(self,widget):
		"""
		setCentralWidget(widget)
			widget=QtGui.QWidget

		Sets the given widget to be the main windows central widget.
		Note: PySide.QtGui.QMainWindow takes ownership of the widget pointer and deletes it at the appropriate time.
		"""
		res = super(QMainWindow,self).setCentralWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setCorner(self,corner,area):
		"""
		setCorner(corner,area)
			corner=QtCore.Qt.Corner
			area=QtCore.Qt.DockWidgetArea


		"""
		res = super(QMainWindow,self).setCorner(corner,area)
		return res
	#----------------------------------------------------------------------
	def setDockOptions(self,options):
		"""
		setDockOptions(options)
			options=QtGui.QMainWindow.DockOptions

		This property holds the docking behavior of PySide.QtGui.QMainWindow .
		The default value is AnimatedDocks | AllowTabbedDocks .
		"""
		res = super(QMainWindow,self).setDockOptions(options)
		return res
	#----------------------------------------------------------------------
	def setDocumentMode(self,enabled):
		"""
		setDocumentMode(enabled)
			enabled=QtCore.bool

		This property holds whether the tab bar for tabbed dockwidgets is set to document mode..
		The default is false.
		"""
		res = super(QMainWindow,self).setDocumentMode(enabled)
		return res
	#----------------------------------------------------------------------
	def setIconSize(self,iconSize):
		"""
		setIconSize(iconSize)
			iconSize=QtCore.QSize

		This property holds size of toolbar icons in this mainwindow..
		The default is the default tool bar icon size of the GUI style
		Note that the icons used must be at least of this size as the icons are only scaled down.
		"""
		res = super(QMainWindow,self).setIconSize(iconSize)
		return res
	#----------------------------------------------------------------------
	def setMenuBar(self,menubar):
		"""
		setMenuBar(menubar)
			menubar=QtGui.QMenuBar

		Sets the menu bar for the main window to menuBar .
		Note: PySide.QtGui.QMainWindow takes ownership of the menuBar pointer and deletes it at the appropriate time.
		"""
		res = super(QMainWindow,self).setMenuBar(menubar)
		return res
	#----------------------------------------------------------------------
	def setMenuWidget(self,menubar):
		"""
		setMenuWidget(menubar)
			menubar=QtGui.QWidget

		Sets the menu bar for the main window to menuBar .
		PySide.QtGui.QMainWindow takes ownership of the menuBar pointer and deletes it at the appropriate time.
		"""
		res = super(QMainWindow,self).setMenuWidget(menubar)
		return res
	#----------------------------------------------------------------------
	def setStatusBar(self,statusbar):
		"""
		setStatusBar(statusbar)
			statusbar=QtGui.QStatusBar

		Sets the status bar for the main window to statusbar .
		Setting the status bar to 0 will remove it from the main window
		Note that PySide.QtGui.QMainWindow takes ownership of the statusbar pointer and deletes it at the appropriate time.
		"""
		res = super(QMainWindow,self).setStatusBar(statusbar)
		return res
	#----------------------------------------------------------------------
	def setTabPosition(self,areas,tabPosition):
		"""
		setTabPosition(areas,tabPosition)
			areas=QtCore.Qt.DockWidgetAreas
			tabPosition=QtGui.QTabWidget.TabPosition


		"""
		res = super(QMainWindow,self).setTabPosition(areas,tabPosition)
		return res
	#----------------------------------------------------------------------
	def setTabShape(self,tabShape):
		"""
		setTabShape(tabShape)
			tabShape=QtGui.QTabWidget.TabShape

		This property holds the tab shape used for tabbed dock widgets..
		The default is QTabWidget.Rounded .
		"""
		res = super(QMainWindow,self).setTabShape(tabShape)
		return res
	#----------------------------------------------------------------------
	def setToolButtonStyle(self,toolButtonStyle):
		"""
		setToolButtonStyle(toolButtonStyle)
			toolButtonStyle=QtCore.Qt.ToolButtonStyle

		This property holds style of toolbar buttons in this mainwindow..
		The default is Qt.ToolButtonIconOnly .
		"""
		res = super(QMainWindow,self).setToolButtonStyle(toolButtonStyle)
		return res
	#----------------------------------------------------------------------
	def setUnifiedTitleAndToolBarOnMac(self,set):
		"""
		setUnifiedTitleAndToolBarOnMac(set)
			set=QtCore.bool

		This property holds whether the window uses the unified title and toolbar look on Mac OS X.
		This property is false by default and only has any effect on Mac OS X 10.4 or higher.
		If set to true, then the top toolbar area is replaced with a Carbon HIToolbar or a Cocoa NSToolbar (depending on whether Qt was built with Carbon or Cocoa)
		All toolbars in the top toolbar area and any toolbars added afterwards are moved to that
		This means a couple of things.
		Setting this back to false will remove these restrictions.
		The Qt.WA_MacBrushedMetal attribute takes precedence over this property.
		"""
		res = super(QMainWindow,self).setUnifiedTitleAndToolBarOnMac(set)
		return res
	#----------------------------------------------------------------------
	def splitDockWidget(self,after,dockwidget,orientation):
		"""
		splitDockWidget(after,dockwidget,orientation)
			after=QtGui.QDockWidget
			dockwidget=QtGui.QDockWidget
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QMainWindow,self).splitDockWidget(after,dockwidget,orientation)
		return res
	#----------------------------------------------------------------------
	def tabPosition(self,area):
		"""
		tabPosition(area)
			area=QtCore.Qt.DockWidgetArea


		"""
		res = super(QMainWindow,self).tabPosition(area)
		isinstance(res,QtGui.QTabWidget.TabPosition)
		return res
	#----------------------------------------------------------------------
	def tabifiedDockWidgets(self,dockwidget):
		"""
		tabifiedDockWidgets(dockwidget)
			dockwidget=QtGui.QDockWidget

		Returns the dock widgets that are tabified together with dockwidget .
		"""
		res = super(QMainWindow,self).tabifiedDockWidgets(dockwidget)
		return res
	#----------------------------------------------------------------------
	def tabifyDockWidget(self,first,second):
		"""
		tabifyDockWidget(first,second)
			first=QtGui.QDockWidget
			second=QtGui.QDockWidget

		Moves second dock widget on top of first dock widget, creating a tabbed docked area in the main window.
		"""
		res = super(QMainWindow,self).tabifyDockWidget(first,second)
		return res
	#----------------------------------------------------------------------
	def toolBarArea(self,toolbar):
		"""
		toolBarArea(toolbar)
			toolbar=QtGui.QToolBar

		Returns the Qt.ToolBarArea for toolbar
		If toolbar has not been added to the main window, this function returns Qt::NoToolBarArea .
		"""
		res = super(QMainWindow,self).toolBarArea(toolbar)
		isinstance(res,QtCore.Qt.ToolBarArea)
		return res
	#----------------------------------------------------------------------
	def toolBarBreak(self,toolbar):
		"""
		toolBarBreak(toolbar)
			toolbar=QtGui.QToolBar

		Returns whether there is a toolbar break before the toolbar .
		"""
		res = super(QMainWindow,self).toolBarBreak(toolbar)
		isinstance(res,bool)
		return res
