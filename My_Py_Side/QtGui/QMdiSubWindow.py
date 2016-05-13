from PySide import QtGui, QtCore

class QMdiSubWindow(QtGui.QMdiSubWindow):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMdiSubWindow,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aboutToActivate(self):
		"""

		"""
		res = super(QMdiSubWindow,self).aboutToActivate()
		return res
	#----------------------------------------------------------------------
	def isShaded(self):
		"""
		Returns true if this window is shaded; otherwise returns false.
		A window is shaded if it is collapsed so that only the title bar is visible.
		"""
		res = super(QMdiSubWindow,self).isShaded()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def keyboardPageStep(self):
		"""
		This property holds sets how far a widget should move or resize when using the keyboard page keys..
		When in keyboard-interactive mode, you can use the arrow and page keys to either move or resize the window
		This property controls the page keys
		The common way to enter keyboard interactive mode is to enter the subwindow menu, and select either resize or move.
		The default keyboard page step value is 20 pixels.
		"""
		res = super(QMdiSubWindow,self).keyboardPageStep()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def keyboardSingleStep(self):
		"""
		This property holds sets how far a widget should move or resize when using the keyboard arrow keys..
		When in keyboard-interactive mode, you can use the arrow and page keys to either move or resize the window
		This property controls the arrow keys
		The common way to enter keyboard interactive mode is to enter the subwindow menu, and select either resize or move.
		The default keyboard single step value is 5 pixels.
		"""
		res = super(QMdiSubWindow,self).keyboardSingleStep()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maximizedButtonsWidget(self):
		"""

		"""
		res = super(QMdiSubWindow,self).maximizedButtonsWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def maximizedSystemMenuIconWidget(self):
		"""

		"""
		res = super(QMdiSubWindow,self).maximizedSystemMenuIconWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def mdiArea(self):
		"""
		Returns the area containing this sub-window, or 0 if there is none.
		"""
		res = super(QMdiSubWindow,self).mdiArea()
		isinstance(res,QtGui.QMdiArea)
		return res
	#----------------------------------------------------------------------
	def systemMenu(self):
		"""
		Returns a pointer to the current system menu, or zero if no system menu is set
		PySide.QtGui.QMdiSubWindow provides a default system menu, but you can also set the menu with PySide.QtGui.QMdiSubWindow.setSystemMenu() .
		"""
		res = super(QMdiSubWindow,self).systemMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the current internal widget.
		"""
		res = super(QMdiSubWindow,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setKeyboardPageStep(self,step):
		"""
		setKeyboardPageStep(step)
			step=QtCore.int

		This property holds sets how far a widget should move or resize when using the keyboard page keys..
		When in keyboard-interactive mode, you can use the arrow and page keys to either move or resize the window
		This property controls the page keys
		The common way to enter keyboard interactive mode is to enter the subwindow menu, and select either resize or move.
		The default keyboard page step value is 20 pixels.
		"""
		res = super(QMdiSubWindow,self).setKeyboardPageStep(step)
		return res
	#----------------------------------------------------------------------
	def setKeyboardSingleStep(self,step):
		"""
		setKeyboardSingleStep(step)
			step=QtCore.int

		This property holds sets how far a widget should move or resize when using the keyboard arrow keys..
		When in keyboard-interactive mode, you can use the arrow and page keys to either move or resize the window
		This property controls the arrow keys
		The common way to enter keyboard interactive mode is to enter the subwindow menu, and select either resize or move.
		The default keyboard single step value is 5 pixels.
		"""
		res = super(QMdiSubWindow,self).setKeyboardSingleStep(step)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QMdiSubWindow.SubWindowOption
			on=QtCore.bool

		If on is true, option is enabled on the subwindow; otherwise it is disabled
		See QMdiSubWindow.SubWindowOption for the effect of each option.
		"""
		res = super(QMdiSubWindow,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setSystemMenu(self,systemMenu):
		"""
		setSystemMenu(systemMenu)
			systemMenu=QtGui.QMenu

		Sets systemMenu as the current system menu for this subwindow.
		By default, each PySide.QtGui.QMdiSubWindow has a standard system menu.
		QActions for the system menu created by PySide.QtGui.QMdiSubWindow will automatically be updated depending on the current window state; e.g., the minimize action will be disabled after the window is minimized.
		QActions added by the user are not updated by PySide.QtGui.QMdiSubWindow .
		PySide.QtGui.QMdiSubWindow takes ownership of systemMenu ; you do not have to delete it
		Any existing menus will be deleted.
		"""
		res = super(QMdiSubWindow,self).setSystemMenu(systemMenu)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Sets widget as the internal widget of this subwindow
		The internal widget is displayed in the center of the subwindow beneath the title bar.
		PySide.QtGui.QMdiSubWindow takes temporary ownership of widget ; you do not have to delete it
		Any existing internal widget will be removed and reparented to the root window.
		"""
		res = super(QMdiSubWindow,self).setWidget(widget)
		return res
	#----------------------------------------------------------------------
	def testOption(self,arg__1):
		"""
		testOption(arg__1)
			arg__1=QtGui.QMdiSubWindow.SubWindowOption

		Returns true if option is enabled; otherwise returns false.
		"""
		res = super(QMdiSubWindow,self).testOption(arg__1)
		isinstance(res,QtCore.bool)
		return res
