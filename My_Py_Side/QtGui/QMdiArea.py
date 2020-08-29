from PySide import QtGui, QtCore

class QMdiArea(QtGui.QMdiArea):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMdiArea,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activationOrder(self):
		"""
		This property holds the ordering criteria for subwindow lists.
		This property specifies the ordering criteria for the list of subwindows returned by PySide.QtGui.QMdiArea.subWindowList()
		By default, it is the window creation order.
		"""
		res = super(QMdiArea,self).activationOrder()
		isinstance(res,QtGui.QMdiArea.WindowOrder)
		return res
	#----------------------------------------------------------------------
	def activeSubWindow(self):
		"""
		Returns a pointer to the current active subwindow
		If no window is currently active, 0 is returned.
		Subwindows are treated as top-level windows with respect to window state, i.e., if a widget outside the MDI area is the active window, no subwindow will be active
		Note that if a widget in the window in which the MDI area lives gains focus, the window will be activated.
		"""
		res = super(QMdiArea,self).activeSubWindow()
		isinstance(res,QtGui.QMdiSubWindow)
		return res
	#----------------------------------------------------------------------
	def background(self):
		"""
		This property holds the background brush for the workspace.
		This property sets the background brush for the workspace area itself
		By default, it is a gray color, but can be any brush (e.g., colors, gradients or pixmaps).
		"""
		res = super(QMdiArea,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def currentSubWindow(self):
		"""
		Returns a pointer to the current subwindow, or 0 if there is no current subwindow.
		This function will return the same as PySide.QtGui.QMdiArea.activeSubWindow() if the PySide.QtGui.QApplication containing PySide.QtGui.QMdiArea is active.
		"""
		res = super(QMdiArea,self).currentSubWindow()
		isinstance(res,QtGui.QMdiSubWindow)
		return res
	#----------------------------------------------------------------------
	def documentMode(self):
		"""
		This property holds whether the tab bar is set to document mode in tabbed view mode..
		Document mode is disabled by default.
		"""
		res = super(QMdiArea,self).documentMode()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def tabPosition(self):
		"""
		This property holds the position of the tabs in tabbed view mode..
		Possible values for this property are described by the QTabWidget.TabPosition enum.
		"""
		res = super(QMdiArea,self).tabPosition()
		isinstance(res,QtGui.QTabWidget.TabPosition)
		return res
	#----------------------------------------------------------------------
	def tabShape(self):
		"""
		This property holds the shape of the tabs in tabbed view mode..
		Possible values for this property are QTabWidget.Rounded (default) or QTabWidget.Triangular .
		"""
		res = super(QMdiArea,self).tabShape()
		isinstance(res,QtGui.QTabWidget.TabShape)
		return res
	#----------------------------------------------------------------------
	def viewMode(self):
		"""
		This property holds the way sub-windows are displayed in the PySide.QtGui.QMdiArea ..
		By default, the SubWindowView is used to display sub-windows.
		"""
		res = super(QMdiArea,self).viewMode()
		isinstance(res,QtGui.QMdiArea.ViewMode)
		return res
	#----------------------------------------------------------------------
	def addSubWindow(self,widget,flags=None):
		"""
		addSubWindow(widget,flags=None)
			widget=QtGui.QWidget
			flags=QtCore.Qt.WindowFlags


		"""
		res = super(QMdiArea,self).addSubWindow(widget,flags)
		isinstance(res,QtGui.QMdiSubWindow)
		return res
	#----------------------------------------------------------------------
	def removeSubWindow(self,widget):
		"""
		removeSubWindow(widget)
			widget=QtGui.QWidget

		Removes widget from the MDI area
		The widget must be either a PySide.QtGui.QMdiSubWindow or a widget that is the internal widget of a subwindow
		Note widget is never actually deleted by PySide.QtGui.QMdiArea
		If a PySide.QtGui.QMdiSubWindow is passed in its parent is set to 0 and it is removed, but if an internal widget is passed in the child widget is set to 0 but the PySide.QtGui.QMdiSubWindow is not removed.
		"""
		res = super(QMdiArea,self).removeSubWindow(widget)
		return res
	#----------------------------------------------------------------------
	def setActivationOrder(self,order):
		"""
		setActivationOrder(order)
			order=QtGui.QMdiArea.WindowOrder

		This property holds the ordering criteria for subwindow lists.
		This property specifies the ordering criteria for the list of subwindows returned by PySide.QtGui.QMdiArea.subWindowList()
		By default, it is the window creation order.
		"""
		res = super(QMdiArea,self).setActivationOrder(order)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,background):
		"""
		setBackground(background)
			background=QtGui.QBrush

		This property holds the background brush for the workspace.
		This property sets the background brush for the workspace area itself
		By default, it is a gray color, but can be any brush (e.g., colors, gradients or pixmaps).
		"""
		res = super(QMdiArea,self).setBackground(background)
		return res
	#----------------------------------------------------------------------
	def setDocumentMode(self,enabled):
		"""
		setDocumentMode(enabled)
			enabled=QtCore.bool

		This property holds whether the tab bar is set to document mode in tabbed view mode..
		Document mode is disabled by default.
		"""
		res = super(QMdiArea,self).setDocumentMode(enabled)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QMdiArea.AreaOption
			on=QtCore.bool

		If on is true, option is enabled on the MDI area; otherwise it is disabled
		See QMdiArea.AreaOption for the effect of each option.
		"""
		res = super(QMdiArea,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setTabPosition(self,position):
		"""
		setTabPosition(position)
			position=QtGui.QTabWidget.TabPosition

		This property holds the position of the tabs in tabbed view mode..
		Possible values for this property are described by the QTabWidget.TabPosition enum.
		"""
		res = super(QMdiArea,self).setTabPosition(position)
		return res
	#----------------------------------------------------------------------
	def setTabShape(self,shape):
		"""
		setTabShape(shape)
			shape=QtGui.QTabWidget.TabShape

		This property holds the shape of the tabs in tabbed view mode..
		Possible values for this property are QTabWidget.Rounded (default) or QTabWidget.Triangular .
		"""
		res = super(QMdiArea,self).setTabShape(shape)
		return res
	#----------------------------------------------------------------------
	def setViewMode(self,mode):
		"""
		setViewMode(mode)
			mode=QtGui.QMdiArea.ViewMode

		This property holds the way sub-windows are displayed in the PySide.QtGui.QMdiArea ..
		By default, the SubWindowView is used to display sub-windows.
		"""
		res = super(QMdiArea,self).setViewMode(mode)
		return res
	#----------------------------------------------------------------------
	def subWindowList(self,order=None):
		"""
		subWindowList(order=None)
			order=QtGui.QMdiArea.WindowOrder

		Returns a list of all subwindows in the MDI area
		If order is CreationOrder (the default), the windows are sorted in the order in which they were inserted into the workspace
		If order is StackingOrder , the windows are listed in their stacking order, with the topmost window as the last item in the list
		If order is ActivationHistoryOrder , the windows are listed according to their recent activation history.
		"""
		res = super(QMdiArea,self).subWindowList(order)
		return res
	#----------------------------------------------------------------------
	def testOption(self,opton):
		"""
		testOption(opton)
			opton=QtGui.QMdiArea.AreaOption

		Returns true if option is enabled; otherwise returns false.
		"""
		res = super(QMdiArea,self).testOption(opton)
		isinstance(res,bool)
		return res
