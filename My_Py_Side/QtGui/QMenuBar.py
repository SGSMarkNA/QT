from PySide import QtGui, QtCore

class QMenuBar(QtGui.QMenuBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMenuBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeAction(self):
		"""
		Returns the PySide.QtGui.QAction that is currently highlighted
		A null pointer will be returned if no action is currently selected.
		"""
		res = super(QMenuBar,self).activeAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def addSeparator(self):
		"""
		Appends a separator to the menu.
		"""
		res = super(QMenuBar,self).addSeparator()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all the actions from the menu bar.
		"""
		res = super(QMenuBar,self).clear()
		return res
	#----------------------------------------------------------------------
	def isDefaultUp(self):
		"""
		This property holds the popup orientation.
		The default popup orientation
		By default, menus pop down the screen
		By setting the property to true, the menu will pop up
		You might call this for menus that are below the document to which they refer.
		If the menu would not fit on the screen, the other direction is used automatically.
		"""
		res = super(QMenuBar,self).isDefaultUp()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNativeMenuBar(self):
		"""
		This property holds Whether or not a menubar will be used as a native menubar on platforms that support it.
		This property specifies whether or not the menubar should be used as a native menubar on platforms that support it
		The currently supported platforms are Mac OS X and Windows CE
		On these platforms if this property is true, the menubar is used in the native menubar and is not in the window of its parent, if false the menubar remains in the window
		On other platforms the value of this attribute has no effect.
		The default is to follow whether the Qt.AA_DontUseNativeMenuBar attribute is set for the application
		Explicitly settings this property overrides the presence (or abscence) of the attribute.
		"""
		res = super(QMenuBar,self).isNativeMenuBar()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def actionAt(self,arg__1):
		"""
		actionAt(arg__1)
			arg__1=QtCore.QPoint

		Returns the PySide.QtGui.QAction at pt
		Returns 0 if there is no action at pt or if the location has a separator.
		"""
		res = super(QMenuBar,self).actionAt(arg__1)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def actionGeometry(self,arg__1):
		"""
		actionGeometry(arg__1)
			arg__1=QtGui.QAction

		Returns the geometry of action act as a PySide.QtCore.QRect .
		"""
		res = super(QMenuBar,self).actionGeometry(arg__1)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def addAction(self,*args,**kwargs):
		"""
		addAction(text)
			text=unicode

		addAction(text,receiver,member)
			text=unicode
			receiver=QtCore.QObject
			member=str

		addAction(arg__1,arg__2)
			arg__1=unicode
			arg__2=Object

		This is an overloaded function.
		This convenience function creates a new action with text
		The function adds the newly created action to the menus list of actions, and returns it.
		"""
		res = super(QMenuBar,self).addAction(*args,**kwargs)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def addMenu(self,*args,**kwargs):
		"""
		addMenu(icon,title)
			icon=QtGui.QIcon
			title=unicode

		addMenu(menu)
			menu=QtGui.QMenu

		addMenu(title)
			title=unicode

		Appends a new PySide.QtGui.QMenu with icon and title to the menu bar
		The menu bar takes ownership of the menu
		Returns the new menu.
		"""
		res = super(QMenuBar,self).addMenu(*args,**kwargs)
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def cornerWidget(self,corner=None):
		"""
		cornerWidget(corner=None)
			corner=QtCore.Qt.Corner


		"""
		res = super(QMenuBar,self).cornerWidget(corner)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option,action):
		"""
		initStyleOption(option,action)
			option=QtGui.QStyleOptionMenuItem
			action=QtGui.QAction

		Initialize option with the values from the menu bar and information from action
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionMenuItem , but dont want to fill in all the information themselves.
		"""
		res = super(QMenuBar,self).initStyleOption(option,action)
		return res
	#----------------------------------------------------------------------
	def insertMenu(self,before,menu):
		"""
		insertMenu(before,menu)
			before=QtGui.QAction
			menu=QtGui.QMenu

		This convenience function inserts menu before action before and returns the menus menuAction().
		"""
		res = super(QMenuBar,self).insertMenu(before,menu)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def insertSeparator(self,before):
		"""
		insertSeparator(before)
			before=QtGui.QAction

		This convenience function creates a new separator action, i.e
		an action with QAction.isSeparator() returning true
		The function inserts the newly created action into this menu bars list of actions before action before and returns it.
		"""
		res = super(QMenuBar,self).insertSeparator(before)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def setActiveAction(self,action):
		"""
		setActiveAction(action)
			action=QtGui.QAction

		Sets the currently highlighted action to act .
		"""
		res = super(QMenuBar,self).setActiveAction(action)
		return res
	#----------------------------------------------------------------------
	def setCornerWidget(self,w,corner=None):
		"""
		setCornerWidget(w,corner=None)
			w=QtGui.QWidget
			corner=QtCore.Qt.Corner


		"""
		res = super(QMenuBar,self).setCornerWidget(w,corner)
		return res
	#----------------------------------------------------------------------
	def setDefaultUp(self,arg__1):
		"""
		setDefaultUp(arg__1)
			arg__1=QtCore.bool

		This property holds the popup orientation.
		The default popup orientation
		By default, menus pop down the screen
		By setting the property to true, the menu will pop up
		You might call this for menus that are below the document to which they refer.
		If the menu would not fit on the screen, the other direction is used automatically.
		"""
		res = super(QMenuBar,self).setDefaultUp(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNativeMenuBar(self,nativeMenuBar):
		"""
		setNativeMenuBar(nativeMenuBar)
			nativeMenuBar=QtCore.bool

		This property holds Whether or not a menubar will be used as a native menubar on platforms that support it.
		This property specifies whether or not the menubar should be used as a native menubar on platforms that support it
		The currently supported platforms are Mac OS X and Windows CE
		On these platforms if this property is true, the menubar is used in the native menubar and is not in the window of its parent, if false the menubar remains in the window
		On other platforms the value of this attribute has no effect.
		The default is to follow whether the Qt.AA_DontUseNativeMenuBar attribute is set for the application
		Explicitly settings this property overrides the presence (or abscence) of the attribute.
		"""
		res = super(QMenuBar,self).setNativeMenuBar(nativeMenuBar)
		return res
