from PySide import QtGui, QtCore

class QToolBar(QtGui.QToolBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QToolBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def addSeparator(self):
		"""
		Adds a separator to the end of the toolbar.
		"""
		res = super(QToolBar,self).addSeparator()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def allowedAreas(self):
		"""

		"""
		res = super(QToolBar,self).allowedAreas()
		isinstance(res,QtCore.Qt.ToolBarAreas)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all actions from the toolbar.
		"""
		res = super(QToolBar,self).clear()
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""

		"""
		res = super(QToolBar,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isFloatable(self):
		"""

		"""
		res = super(QToolBar,self).isFloatable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isFloating(self):
		"""

		"""
		res = super(QToolBar,self).isFloating()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isMovable(self):
		"""
		This property holds whether the user can move the toolbar within the toolbar area, or between toolbar areas.
		By default, this property is true.
		This property only makes sense if the toolbar is in a PySide.QtGui.QMainWindow .
		"""
		res = super(QToolBar,self).isMovable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""

		"""
		res = super(QToolBar,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def toggleViewAction(self):
		"""
		Returns a checkable action that can be used to show or hide this toolbar.
		The actions text is set to the toolbars window title.
		"""
		res = super(QToolBar,self).toggleViewAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def toolButtonStyle(self):
		"""

		"""
		res = super(QToolBar,self).toolButtonStyle()
		isinstance(res,QtCore.Qt.ToolButtonStyle)
		return res
	#----------------------------------------------------------------------
	def actionAt(self,*args,**kwargs):
		"""
		actionAt(p)
			p=QtCore.QPoint

		actionAt(x,y)
			x=QtCore.int
			y=QtCore.int

		Returns the action at point p
		This function returns zero if no action was found.
		"""
		res = super(QToolBar,self).actionAt(*args,**kwargs)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def actionGeometry(self,action):
		"""
		actionGeometry(action)
			action=QtGui.QAction

		Returns the geometry of the toolbar item associated with the given action , or an invalid PySide.QtCore.QRect if no matching item is found.
		"""
		res = super(QToolBar,self).actionGeometry(action)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def addAction(self,*args,**kwargs):
		"""
		addAction(text,receiver)
			text=unicode
			receiver=QtCore.QObject

		addAction(text)
			text=unicode

		addAction(icon,text,receiver)
			icon=QtGui.QIcon
			text=unicode
			receiver=QtCore.QObject

		addAction(icon,text)
			icon=QtGui.QIcon
			text=unicode

		This is an overloaded function.
		Creates a new action with the given text
		This action is added to the end of the toolbar
		The actions PySide.QtGui.QAction.triggered() signal is connected to member in receiver .
		"""
		res = super(QToolBar,self).addAction(*args,**kwargs)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,widget):
		"""
		addWidget(widget)
			widget=QtGui.QWidget

		Adds the given widget to the toolbar as the toolbars last item.
		The toolbar takes ownership of widget .
		If you add a PySide.QtGui.QToolButton with this method, the tools bars Qt.ToolButtonStyle will not be respected.
		"""
		res = super(QToolBar,self).addWidget(widget)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionToolBar


		"""
		res = super(QToolBar,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def insertSeparator(self,before):
		"""
		insertSeparator(before)
			before=QtGui.QAction

		Inserts a separator into the toolbar in front of the toolbar item associated with the before action.
		"""
		res = super(QToolBar,self).insertSeparator(before)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,before,widget):
		"""
		insertWidget(before,widget)
			before=QtGui.QAction
			widget=QtGui.QWidget

		Inserts the given widget in front of the toolbar item associated with the before action.
		Note: You should use QAction.setVisible() to change the visibility of the widget
		Using QWidget.setVisible() , QWidget.show() and QWidget.hide() does not work.
		"""
		res = super(QToolBar,self).insertWidget(before,widget)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def isAreaAllowed(self,area):
		"""
		isAreaAllowed(area)
			area=QtCore.Qt.ToolBarArea


		"""
		res = super(QToolBar,self).isAreaAllowed(area)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAllowedAreas(self,areas):
		"""
		setAllowedAreas(areas)
			areas=QtCore.Qt.ToolBarAreas


		"""
		res = super(QToolBar,self).setAllowedAreas(areas)
		return res
	#----------------------------------------------------------------------
	def setFloatable(self,floatable):
		"""
		setFloatable(floatable)
			floatable=QtCore.bool


		"""
		res = super(QToolBar,self).setFloatable(floatable)
		return res
	#----------------------------------------------------------------------
	def setMovable(self,movable):
		"""
		setMovable(movable)
			movable=QtCore.bool


		"""
		res = super(QToolBar,self).setMovable(movable)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,orientation):
		"""
		setOrientation(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QToolBar,self).setOrientation(orientation)
		return res
	#----------------------------------------------------------------------
	def widgetForAction(self,action):
		"""
		widgetForAction(action)
			action=QtGui.QAction

		Returns the widget associated with the specified action .
		"""
		res = super(QToolBar,self).widgetForAction(action)
		isinstance(res,QtGui.QWidget)
		return res
