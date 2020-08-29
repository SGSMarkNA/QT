from PySide import QtGui, QtCore

class QDesktopWidget(QtGui.QDesktopWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDesktopWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isVirtualDesktop(self):
		"""
		This property holds if the system manages the available screens in a virtual desktop..
		For virtual desktops, PySide.QtGui.QDesktopWidget.screen() will always return the same widget
		The size of the virtual desktop is the size of this desktop widget.
		"""
		res = super(QDesktopWidget,self).isVirtualDesktop()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def numScreens(self):
		"""
		Returns the number of available screens.
		This function is deprecated
		Use PySide.QtGui.QDesktopWidget.screenCount() instead.
		"""
		res = super(QDesktopWidget,self).numScreens()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def primaryScreen(self):
		"""
		This property holds the index of the screen that is configured to be the primary screen on the system..
		"""
		res = super(QDesktopWidget,self).primaryScreen()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def screenCount(self):
		"""
		This property holds the number of screens currently available on the system..
		"""
		res = super(QDesktopWidget,self).screenCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def availableGeometry(self,*args,**kwargs):
		"""
		availableGeometry(widget)
			widget=QtGui.QWidget

		availableGeometry(screen=None)
			screen=QtCore.int

		availableGeometry(point)
			point=QtCore.QPoint

		This is an overloaded function.
		Returns the available geometry of the screen which contains widget .
		"""
		res = super(QDesktopWidget,self).availableGeometry(*args,**kwargs)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def screen(self,screen=None):
		"""
		screen(screen=None)
			screen=QtCore.int

		Returns a widget that represents the screen with index screen (a value of -1 means the default screen).
		If the system uses a virtual desktop, the returned widget will have the geometry of the entire virtual desktop; i.e., bounding every screen .
		"""
		res = super(QDesktopWidget,self).screen(screen)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def screenGeometry(self,*args,**kwargs):
		"""
		screenGeometry(screen=None)
			screen=QtCore.int

		screenGeometry(widget)
			widget=QtGui.QWidget

		screenGeometry(point)
			point=QtCore.QPoint

		Returns the geometry of the screen with index screen
		The default screen is used if screen is -1.
		"""
		res = super(QDesktopWidget,self).screenGeometry(*args,**kwargs)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def screenNumber(self,*args,**kwargs):
		"""
		screenNumber(arg__1)
			arg__1=QtCore.QPoint

		screenNumber(widget=None)
			widget=QtGui.QWidget

		This is an overloaded function.
		Returns the index of the screen that contains the point , or the screen which is the shortest distance from the point .
		"""
		res = super(QDesktopWidget,self).screenNumber(*args,**kwargs)
		isinstance(res,int)
		return res
