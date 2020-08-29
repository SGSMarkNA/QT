from PySide import QtGui, QtCore

class QDockWidget(QtGui.QDockWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDockWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def allowedAreas(self):
		"""

		"""
		res = super(QDockWidget,self).allowedAreas()
		isinstance(res,QtCore.Qt.DockWidgetAreas)
		return res
	#----------------------------------------------------------------------
	def features(self):
		"""
		This property holds whether the dock widget is movable, closable, and floatable.
		By default, this property is set to a combination of DockWidgetClosable , DockWidgetMovable and DockWidgetFloatable .
		"""
		res = super(QDockWidget,self).features()
		isinstance(res,QtGui.QDockWidget.DockWidgetFeatures)
		return res
	#----------------------------------------------------------------------
	def isFloating(self):
		"""
		This property holds whether the dock widget is floating.
		A floating dock widget is presented to the user as an independent window on top of its parent PySide.QtGui.QMainWindow , instead of being docked in the PySide.QtGui.QMainWindow .
		By default, this property is true.
		"""
		res = super(QDockWidget,self).isFloating()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def titleBarWidget(self):
		"""
		Returns the custom title bar widget set on the PySide.QtGui.QDockWidget , or 0 if no custom title bar has been set.
		"""
		res = super(QDockWidget,self).titleBarWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def toggleViewAction(self):
		"""
		Returns a checkable action that can be used to show or close this dock widget.
		The actions text is set to the dock widgets window title.
		"""
		res = super(QDockWidget,self).toggleViewAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the widget for the dock widget
		This function returns zero if the widget has not been set.
		"""
		res = super(QDockWidget,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionDockWidget

		Initialize option with the values from this PySide.QtGui.QDockWidget
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionDockWidget , but dont want to fill in all the information themselves.
		"""
		res = super(QDockWidget,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def isAreaAllowed(self,area):
		"""
		isAreaAllowed(area)
			area=QtCore.Qt.DockWidgetArea


		"""
		res = super(QDockWidget,self).isAreaAllowed(area)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAllowedAreas(self,areas):
		"""
		setAllowedAreas(areas)
			areas=QtCore.Qt.DockWidgetAreas


		"""
		res = super(QDockWidget,self).setAllowedAreas(areas)
		return res
	#----------------------------------------------------------------------
	def setFeatures(self,features):
		"""
		setFeatures(features)
			features=QtGui.QDockWidget.DockWidgetFeatures

		This property holds whether the dock widget is movable, closable, and floatable.
		By default, this property is set to a combination of DockWidgetClosable , DockWidgetMovable and DockWidgetFloatable .
		"""
		res = super(QDockWidget,self).setFeatures(features)
		return res
	#----------------------------------------------------------------------
	def setFloating(self,floating):
		"""
		setFloating(floating)
			floating=QtCore.bool

		This property holds whether the dock widget is floating.
		A floating dock widget is presented to the user as an independent window on top of its parent PySide.QtGui.QMainWindow , instead of being docked in the PySide.QtGui.QMainWindow .
		By default, this property is true.
		"""
		res = super(QDockWidget,self).setFloating(floating)
		return res
	#----------------------------------------------------------------------
	def setTitleBarWidget(self,widget):
		"""
		setTitleBarWidget(widget)
			widget=QtGui.QWidget

		Sets an arbitrary widget as the dock widgets title bar
		If widget is 0, any custom title bar widget previously set on the dock widget is removed, but not deleted, and the default title bar will be used instead.
		If a title bar widget is set, PySide.QtGui.QDockWidget will not use native window decorations when it is floated.
		Here are some tips for implementing custom title bars:
		Using qobject_cast() as shown above, the title bar widget has full access to its parent PySide.QtGui.QDockWidget
		Hence it can perform such operations as docking and hiding in response to user actions.
		"""
		res = super(QDockWidget,self).setTitleBarWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Sets the widget for the dock widget to widget .
		If the dock widget is visible when widget is added, you must PySide.QtGui.QWidget.show() it explicitly.
		Note that you must add the layout of the widget before you call this function; if not, the widget will not be visible.
		"""
		res = super(QDockWidget,self).setWidget(widget)
		return res
