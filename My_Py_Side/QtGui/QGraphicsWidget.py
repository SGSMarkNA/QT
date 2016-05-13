from PySide import QtGui, QtCore

class QGraphicsWidget(QtGui.QGraphicsWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def actions(self):
		"""
		Returns the (possibly empty) list of this widgets actions.
		"""
		res = super(QGraphicsWidget,self).actions()
		return res
	#----------------------------------------------------------------------
	def adjustSize(self):
		"""
		Adjusts the size of the widget to its effective preferred size hint.
		This function is called implicitly when the item is shown for the first time.
		"""
		res = super(QGraphicsWidget,self).adjustSize()
		return res
	#----------------------------------------------------------------------
	def autoFillBackground(self):
		"""
		This property holds whether the widget background is filled automatically.
		If enabled, this property will cause Qt to fill the background of the widget before invoking the PySide.QtGui.QGraphicsWidget.paint() method
		The color used is defined by the QPalette.Window color role from the widgets palette .
		In addition, Windows are always filled with QPalette.Window , unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.
		By default, this property is false.
		"""
		res = super(QGraphicsWidget,self).autoFillBackground()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def focusPolicy(self):
		"""
		This property holds the way the widget accepts keyboard focus.
		The focus policy is Qt.TabFocus if the widget accepts keyboard focus by tabbing, Qt.ClickFocus if the widget accepts focus by clicking, Qt.StrongFocus if it accepts both, and Qt.NoFocus (the default) if it does not accept focus at all.
		You must enable keyboard focus for a widget if it processes keyboard events
		This is normally done from the widgets constructor
		For instance, the PySide.QtGui.QLineEdit constructor calls setFocusPolicy( Qt.StrongFocus ).
		If you enable a focus policy (i.e., not Qt.NoFocus ), PySide.QtGui.QGraphicsWidget will automatically enable the ItemIsFocusable flag
		Setting Qt.NoFocus on a widget will clear the ItemIsFocusable flag
		If the widget currently has keyboard focus, the widget will automatically lose focus.
		"""
		res = super(QGraphicsWidget,self).focusPolicy()
		isinstance(res,QtCore.Qt.FocusPolicy)
		return res
	#----------------------------------------------------------------------
	def focusWidget(self):
		"""
		If this widget, a child or descendant of this widget currently has input focus, this function will return a pointer to that widget
		If no descendant widget has input focus, 0 is returned.
		"""
		res = super(QGraphicsWidget,self).focusWidget()
		isinstance(res,QtGui.QGraphicsWidget)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		This property holds the widgets font.
		This property provides the widgets font.
		PySide.QtGui.QFont consists of font properties that have been explicitly defined and properties implicitly inherited from the widgets parent
		Hence, PySide.QtGui.QGraphicsWidget.font() can return a different font compared to the one set with PySide.QtGui.QGraphicsWidget.setFont()
		This scheme allows you to define single entries in a font without affecting the fonts inherited entries.
		When a widgets font changes, it resolves its entries against its parent widget
		If the widget does not have a parent widget, it resolves its entries against the scene
		The widget then sends itself a FontChange event and notifies all its descendants so that they can resolve their fonts as well.
		By default, this property contains the applications default font.
		"""
		res = super(QGraphicsWidget,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def geometryChanged(self):
		"""

		"""
		res = super(QGraphicsWidget,self).geometryChanged()
		return res
	#----------------------------------------------------------------------
	def getWindowFrameMargins(self):
		"""
		Gets the widgets window frame margins
		The margins are stored in left , top , right and bottom as pointers to qreals
		Each argument can be omitted by passing 0.
		"""
		res = super(QGraphicsWidget,self).getWindowFrameMargins()
		return res
	#----------------------------------------------------------------------
	def isActiveWindow(self):
		"""
		Returns true if this widgets window is in the active window, or if the widget does not have a window but is in an active scene (i.e., a scene that currently has focus).
		The active window is the window that either contains a child widget that currently has input focus, or that itself has input focus.
		"""
		res = super(QGraphicsWidget,self).isActiveWindow()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def layout(self):
		"""
		This property holds The layout of the widget.
		Any existing layout manager is deleted before the new layout is assigned
		If layout is 0, the widget is left without a layout
		Existing subwidgets geometries will remain unaffected.
		PySide.QtGui.QGraphicsWidget takes ownership of layout .
		All widgets that are currently managed by layout or all of its sublayouts, are automatically reparented to this item
		The layout is then invalidated, and the child widget geometries are adjusted according to this items PySide.QtGui.QGraphicsLayoutItem.geometry() and contentsMargins()
		Children who are not explicitly managed by layout remain unaffected by the layout after it has been assigned to this widget.
		If no layout is currently managing this widget, PySide.QtGui.QGraphicsWidget.layout() will return 0.
		"""
		res = super(QGraphicsWidget,self).layout()
		isinstance(res,QtGui.QGraphicsLayout)
		return res
	#----------------------------------------------------------------------
	def layoutChanged(self):
		"""

		"""
		res = super(QGraphicsWidget,self).layoutChanged()
		return res
	#----------------------------------------------------------------------
	def layoutDirection(self):
		"""
		This property holds the layout direction for this widget..
		This property modifies this widgets and all of its descendants Qt.WA_RightToLeft attribute
		It also sets this widgets Qt.WA_SetLayoutDirection attribute.
		The widgets layout direction determines the order in which the layout manager horizontally arranges subwidgets of this widget
		The default value depends on the language and locale of the application, and is typically in the same direction as words are read and written
		With Qt.LeftToRight , the layout starts placing subwidgets from the left side of this widget towards the right
		Qt.RightToLeft does the opposite - the layout will place widgets starting from the right edge moving towards the left.
		Subwidgets inherit their layout direction from the parent
		Top-level widget items inherit their layout direction from QGraphicsScene::layoutDirection
		If you change a widgets layout direction by calling PySide.QtGui.QGraphicsWidget.setLayoutDirection() , the widget will send itself a LayoutDirectionChange event, and then propagate the new layout direction to all its descendants.
		"""
		res = super(QGraphicsWidget,self).layoutDirection()
		isinstance(res,QtCore.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def palette(self):
		"""
		This property holds the widgets palette.
		This property provides the widgets palette
		The palette provides colors and brushes for color groups (e.g., QPalette.Button ) and states (e.g., QPalette.Inactive ), loosely defining the general look of the widget and its children.
		PySide.QtGui.QPalette consists of color groups that have been explicitly defined, and groups that are implicitly inherited from the widgets parent
		Because of this, PySide.QtGui.QGraphicsWidget.palette() can return a different palette than what has been set with PySide.QtGui.QGraphicsWidget.setPalette()
		This scheme allows you to define single entries in a palette without affecting the palettes inherited entries.
		When a widgets palette changes, it resolves its entries against its parent widget, or if it doesnt have a parent widget, it resolves against the scene
		It then sends itself a PaletteChange event, and notifies all its descendants so they can resolve their palettes as well.
		By default, this property contains the applications default palette.
		"""
		res = super(QGraphicsWidget,self).palette()
		isinstance(res,QtGui.QPalette)
		return res
	#----------------------------------------------------------------------
	def polishEvent(self):
		"""
		This event is delivered to the item by the scene at some point after it has been constructed, but before it is shown or otherwise accessed through the scene
		You can use this event handler to do last-minute initializations of the widget which require the item to be fully constructed.
		The base implementation does nothing.
		"""
		res = super(QGraphicsWidget,self).polishEvent()
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the items local rect as a PySide.QtCore.QRectF
		This function is equivalent to PySide.QtCore.QRectF ( QPointF() , PySide.QtGui.QGraphicsWidget.size() ).
		"""
		res = super(QGraphicsWidget,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		This property holds the size of the widget.
		Calling PySide.QtGui.QGraphicsWidget.resize() resizes the widget to a size bounded by PySide.QtGui.QGraphicsLayoutItem.minimumSize() and PySide.QtGui.QGraphicsLayoutItem.maximumSize()
		This property only affects the widgets width and height (e.g., its right and bottom edges); the widgets position and top-left corner remains unaffected.
		Resizing a widget triggers the widget to immediately receive a GraphicsSceneResize event with the widgets old and new size
		If the widget has a layout assigned when this event arrives, the layout will be activated and it will automatically update any child widgetss geometry.
		This property does not affect any layout of the parent widget
		If the widget itself is managed by a parent layout; e.g., it has a parent widget with a layout assigned, that layout will not activate.
		By default, this property contains a size with zero width and height.
		"""
		res = super(QGraphicsWidget,self).size()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns a pointer to the widgets style
		If this widget does not have any explicitly assigned style, the scenes style is returned instead
		In turn, if the scene does not have any assigned style, this function returns QApplication.style() .
		"""
		res = super(QGraphicsWidget,self).style()
		isinstance(res,QtGui.QStyle)
		return res
	#----------------------------------------------------------------------
	def unsetLayoutDirection(self):
		"""
		This property holds the layout direction for this widget..
		This property modifies this widgets and all of its descendants Qt.WA_RightToLeft attribute
		It also sets this widgets Qt.WA_SetLayoutDirection attribute.
		The widgets layout direction determines the order in which the layout manager horizontally arranges subwidgets of this widget
		The default value depends on the language and locale of the application, and is typically in the same direction as words are read and written
		With Qt.LeftToRight , the layout starts placing subwidgets from the left side of this widget towards the right
		Qt.RightToLeft does the opposite - the layout will place widgets starting from the right edge moving towards the left.
		Subwidgets inherit their layout direction from the parent
		Top-level widget items inherit their layout direction from QGraphicsScene::layoutDirection
		If you change a widgets layout direction by calling PySide.QtGui.QGraphicsWidget.setLayoutDirection() , the widget will send itself a LayoutDirectionChange event, and then propagate the new layout direction to all its descendants.
		"""
		res = super(QGraphicsWidget,self).unsetLayoutDirection()
		return res
	#----------------------------------------------------------------------
	def unsetWindowFrameMargins(self):
		"""
		Resets the window frame margins to the default value, provided by the style.
		"""
		res = super(QGraphicsWidget,self).unsetWindowFrameMargins()
		return res
	#----------------------------------------------------------------------
	def windowFlags(self):
		"""
		This property holds the widgets window flags.
		Window flags are a combination of a window type (e.g., Qt.Dialog ) and several flags giving hints on the behavior of the window
		The behavior is platform-dependent.
		By default, this property contains no window flags.
		Windows are panels
		If you set the Qt.Window flag, the ItemIsPanel flag will be set automatically
		If you clear the Qt.Window flag, the ItemIsPanel flag is also cleared
		Note that the ItemIsPanel flag can be set independently of Qt.Window .
		"""
		res = super(QGraphicsWidget,self).windowFlags()
		isinstance(res,QtCore.Qt.WindowFlags)
		return res
	#----------------------------------------------------------------------
	def windowFrameGeometry(self):
		"""
		Returns the widgets geometry in parent coordinates including any window frame.
		"""
		res = super(QGraphicsWidget,self).windowFrameGeometry()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def windowFrameRect(self):
		"""
		Returns the widgets local rect including any window frame.
		"""
		res = super(QGraphicsWidget,self).windowFrameRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def windowTitle(self):
		"""
		This property holds This property holds the window title (caption)..
		This property is only used for windows.
		By default, if no title has been set, this property contains an empty string.
		"""
		res = super(QGraphicsWidget,self).windowTitle()
		return res
	#----------------------------------------------------------------------
	def windowType(self):
		"""
		Returns the widgets window type.
		"""
		res = super(QGraphicsWidget,self).windowType()
		isinstance(res,QtCore.Qt.WindowType)
		return res
	#----------------------------------------------------------------------
	def addAction(self,action):
		"""
		addAction(action)
			action=QtGui.QAction

		Appends the action action to this widgets list of actions.
		All QGraphicsWidgets have a list of PySide.QtGui.QAction s, however they can be represented graphically in many different ways
		The default use of the PySide.QtGui.QAction list (as returned by PySide.QtGui.QGraphicsWidget.actions() ) is to create a context PySide.QtGui.QMenu .
		A PySide.QtGui.QGraphicsWidget should only have one of each action and adding an action it already has will not cause the same action to be in the widget twice.
		"""
		res = super(QGraphicsWidget,self).addAction(action)
		return res
	#----------------------------------------------------------------------
	def addActions(self,actions):
		"""
		addActions(actions)
			actions=unKnown


		"""
		res = super(QGraphicsWidget,self).addActions(actions)
		return res
	#----------------------------------------------------------------------
	def changeEvent(self,event):
		"""
		changeEvent(event)
			event=QtCore.QEvent

		This event handler can be reimplemented to handle state changes.
		The state being changed in this event can be retrieved through event .
		Change events include: QEvent.ActivationChange , QEvent.EnabledChange , QEvent.FontChange , QEvent.StyleChange , QEvent.PaletteChange , QEvent.ParentChange , QEvent.LayoutDirectionChange , and QEvent.ContentsRectChange .
		"""
		res = super(QGraphicsWidget,self).changeEvent(event)
		return res
	#----------------------------------------------------------------------
	def closeEvent(self,event):
		"""
		closeEvent(event)
			event=QtGui.QCloseEvent

		This event handler, for event , can be reimplemented in a subclass to receive widget close events
		The default implementation accepts the event.
		"""
		res = super(QGraphicsWidget,self).closeEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusNextPrevChild(self,next):
		"""
		focusNextPrevChild(next)
			next=QtCore.bool

		Finds a new widget to give the keyboard focus to, as appropriate for Tab and Shift+Tab, and returns true if it can find a new widget; returns false otherwise
		If next is true, this function searches forward; if next is false, it searches backward.
		Sometimes, you will want to reimplement this function to provide special focus handling for your widget and its subwidgets
		For example, a web browser might reimplement it to move its current active link forward or backward, and call the base implementation only when it reaches the last or first link on the page.
		Child widgets call PySide.QtGui.QGraphicsWidget.focusNextPrevChild() on their parent widgets, but only the window that contains the child widgets decides where to redirect focus
		By reimplementing this function for an object, you gain control of focus traversal for all child widgets.
		"""
		res = super(QGraphicsWidget,self).focusNextPrevChild(next)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def grabKeyboardEvent(self,event):
		"""
		grabKeyboardEvent(event)
			event=QtCore.QEvent

		This event handler, for event , can be reimplemented in a subclass to receive notifications for Qt::GrabKeyboard events.
		"""
		res = super(QGraphicsWidget,self).grabKeyboardEvent(event)
		return res
	#----------------------------------------------------------------------
	def grabMouseEvent(self,event):
		"""
		grabMouseEvent(event)
			event=QtCore.QEvent

		This event handler, for event , can be reimplemented in a subclass to receive notifications for Qt::GrabMouse events.
		"""
		res = super(QGraphicsWidget,self).grabMouseEvent(event)
		return res
	#----------------------------------------------------------------------
	def grabShortcut(self,sequence,context=None):
		"""
		grabShortcut(sequence,context=None)
			sequence=QtGui.QKeySequence
			context=QtCore.Qt.ShortcutContext


		"""
		res = super(QGraphicsWidget,self).grabShortcut(sequence,context)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def hideEvent(self,event):
		"""
		hideEvent(event)
			event=QtGui.QHideEvent

		This event handler, for Hide events, is delivered after the widget has been hidden, for example, setVisible(false) has been called for the widget or one of its ancestors when the widget was previously shown.
		You can reimplement this event handler to detect when your widget is hidden
		Calling QEvent.accept() or QEvent.ignore() on event has no effect.
		"""
		res = super(QGraphicsWidget,self).hideEvent(event)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOption

		Populates a style option object for this widget based on its current state, and stores the output in option
		The default implementation populates option with the following properties.
		Subclasses of PySide.QtGui.QGraphicsWidget should call the base implementation, and then test the type of option using qstyleoption_cast<>() or test QStyleOption.Type before storing widget-specific options.
		For example:
		"""
		res = super(QGraphicsWidget,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def insertAction(self,before,action):
		"""
		insertAction(before,action)
			before=QtGui.QAction
			action=QtGui.QAction

		Inserts the action action to this widgets list of actions, before the action before
		It appends the action if before is 0 or before is not a valid action for this widget.
		A PySide.QtGui.QGraphicsWidget should only have one of each action.
		"""
		res = super(QGraphicsWidget,self).insertAction(before,action)
		return res
	#----------------------------------------------------------------------
	def insertActions(self,before,actions):
		"""
		insertActions(before,actions)
			before=QtGui.QAction
			actions=unKnown


		"""
		res = super(QGraphicsWidget,self).insertActions(before,actions)
		return res
	#----------------------------------------------------------------------
	def moveEvent(self,event):
		"""
		moveEvent(event)
			event=QtGui.QGraphicsSceneMoveEvent

		This event handler, for GraphicsSceneMove events, is delivered after the widget has moved (e.g., its local position has changed).
		This event is only delivered when the item is moved locally
		Calling PySide.QtGui.QGraphicsItem.setTransform() or moving any of the items ancestors does not affect the items local position.
		You can reimplement this event handler to detect when your widget has moved
		Calling QEvent.accept() or QEvent.ignore() on event has no effect.
		"""
		res = super(QGraphicsWidget,self).moveEvent(event)
		return res
	#----------------------------------------------------------------------
	def paintWindowFrame(self,painter,option,widget=None):
		"""
		paintWindowFrame(painter,option,widget=None)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionGraphicsItem
			widget=QtGui.QWidget

		This virtual function is called by PySide.QtGui.QGraphicsScene to draw the window frame for windows using painter , option , and widget , in local coordinates
		The base implementation uses the current style to render the frame and title bar.
		You can reimplement this function in a subclass of PySide.QtGui.QGraphicsWidget to provide custom rendering of the widgets window frame.
		"""
		res = super(QGraphicsWidget,self).paintWindowFrame(painter,option,widget)
		return res
	#----------------------------------------------------------------------
	def propertyChange(self,propertyName,value):
		"""
		propertyChange(propertyName,value)
			propertyName=unicode
			value=object

		This virtual function is used to notify changes to any property (both dynamic properties, and registered with Q_PROPERTY) in the widget
		Depending on the property itself, the notification can be delivered before or after the value has changed.
		propertyName is the name of the property (e.g., size or font), and value is the (proposed) new value of the property
		The function returns the new value, which may be different from value if the notification supports adjusting the property value
		The base implementation simply returns value for any propertyName .
		PySide.QtGui.QGraphicsWidget delivers notifications for the following properties:
		"""
		res = super(QGraphicsWidget,self).propertyChange(propertyName,value)
		return res
	#----------------------------------------------------------------------
	def releaseShortcut(self,id):
		"""
		releaseShortcut(id)
			id=QtCore.int

		Removes the shortcut with the given id from Qts shortcut system
		The widget will no longer receive QEvent.Shortcut events for the shortcuts key sequence (unless it has other shortcuts with the same key sequence).
		"""
		res = super(QGraphicsWidget,self).releaseShortcut(id)
		return res
	#----------------------------------------------------------------------
	def removeAction(self,action):
		"""
		removeAction(action)
			action=QtGui.QAction

		Removes the action action from this widgets list of actions.
		"""
		res = super(QGraphicsWidget,self).removeAction(action)
		return res
	#----------------------------------------------------------------------
	def resize(self,*args,**kwargs):
		"""
		resize(w,h)
			w=QtCore.qreal
			h=QtCore.qreal

		resize(size)
			size=QtCore.QSizeF

		This convenience function is equivalent to calling resize( PySide.QtCore.QSizeF (w, h)).
		"""
		res = super(QGraphicsWidget,self).resize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def resizeEvent(self,event):
		"""
		resizeEvent(event)
			event=QtGui.QGraphicsSceneResizeEvent

		This event handler, for GraphicsSceneResize events, is delivered after the widget has been resized (i.e., its local size has changed)
		event contains both the old and the new size.
		This event is only delivered when the widget is resized locally; calling PySide.QtGui.QGraphicsItem.setTransform() on the widget or any of its ancestors or view, does not affect the widgets local size.
		You can reimplement this event handler to detect when your widget has been resized
		Calling QEvent.accept() or QEvent.ignore() on event has no effect.
		"""
		res = super(QGraphicsWidget,self).resizeEvent(event)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,attribute,on=None):
		"""
		setAttribute(attribute,on=None)
			attribute=QtCore.Qt.WidgetAttribute
			on=QtCore.bool


		"""
		res = super(QGraphicsWidget,self).setAttribute(attribute,on)
		return res
	#----------------------------------------------------------------------
	def setAutoFillBackground(self,enabled):
		"""
		setAutoFillBackground(enabled)
			enabled=QtCore.bool

		This property holds whether the widget background is filled automatically.
		If enabled, this property will cause Qt to fill the background of the widget before invoking the PySide.QtGui.QGraphicsWidget.paint() method
		The color used is defined by the QPalette.Window color role from the widgets palette .
		In addition, Windows are always filled with QPalette.Window , unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.
		By default, this property is false.
		"""
		res = super(QGraphicsWidget,self).setAutoFillBackground(enabled)
		return res
	#----------------------------------------------------------------------
	def setContentsMargins(self,left,top,right,bottom):
		"""
		setContentsMargins(left,top,right,bottom)
			left=QtCore.qreal
			top=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal

		Sets the widgets contents margins to left , top , right and bottom .
		Contents margins are used by the assigned layout to define the placement of subwidgets and layouts
		Margins are particularly useful for widgets that constrain subwidgets to only a section of its own geometry
		For example, a group box with a layout will place subwidgets inside its frame, but below the title.
		Changing a widgets contents margins will always trigger an PySide.QtGui.QGraphicsItem.update() , and any assigned layout will be activated automatically
		The widget will then receive a ContentsRectChange event.
		"""
		res = super(QGraphicsWidget,self).setContentsMargins(left,top,right,bottom)
		return res
	#----------------------------------------------------------------------
	def setFocusPolicy(self,policy):
		"""
		setFocusPolicy(policy)
			policy=QtCore.Qt.FocusPolicy

		This property holds the way the widget accepts keyboard focus.
		The focus policy is Qt.TabFocus if the widget accepts keyboard focus by tabbing, Qt.ClickFocus if the widget accepts focus by clicking, Qt.StrongFocus if it accepts both, and Qt.NoFocus (the default) if it does not accept focus at all.
		You must enable keyboard focus for a widget if it processes keyboard events
		This is normally done from the widgets constructor
		For instance, the PySide.QtGui.QLineEdit constructor calls setFocusPolicy( Qt.StrongFocus ).
		If you enable a focus policy (i.e., not Qt.NoFocus ), PySide.QtGui.QGraphicsWidget will automatically enable the ItemIsFocusable flag
		Setting Qt.NoFocus on a widget will clear the ItemIsFocusable flag
		If the widget currently has keyboard focus, the widget will automatically lose focus.
		"""
		res = super(QGraphicsWidget,self).setFocusPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		This property holds the widgets font.
		This property provides the widgets font.
		PySide.QtGui.QFont consists of font properties that have been explicitly defined and properties implicitly inherited from the widgets parent
		Hence, PySide.QtGui.QGraphicsWidget.font() can return a different font compared to the one set with PySide.QtGui.QGraphicsWidget.setFont()
		This scheme allows you to define single entries in a font without affecting the fonts inherited entries.
		When a widgets font changes, it resolves its entries against its parent widget
		If the widget does not have a parent widget, it resolves its entries against the scene
		The widget then sends itself a FontChange event and notifies all its descendants so that they can resolve their fonts as well.
		By default, this property contains the applications default font.
		"""
		res = super(QGraphicsWidget,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setGeometry(self,x,y,w,h):
		"""
		setGeometry(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		This convenience function is equivalent to calling setGeometry( PySide.QtCore.QRectF ( x , y , w , h )).
		"""
		res = super(QGraphicsWidget,self).setGeometry(x,y,w,h)
		return res
	#----------------------------------------------------------------------
	def setLayout(self,layout):
		"""
		setLayout(layout)
			layout=QtGui.QGraphicsLayout

		This property holds The layout of the widget.
		Any existing layout manager is deleted before the new layout is assigned
		If layout is 0, the widget is left without a layout
		Existing subwidgets geometries will remain unaffected.
		PySide.QtGui.QGraphicsWidget takes ownership of layout .
		All widgets that are currently managed by layout or all of its sublayouts, are automatically reparented to this item
		The layout is then invalidated, and the child widget geometries are adjusted according to this items PySide.QtGui.QGraphicsLayoutItem.geometry() and contentsMargins()
		Children who are not explicitly managed by layout remain unaffected by the layout after it has been assigned to this widget.
		If no layout is currently managing this widget, PySide.QtGui.QGraphicsWidget.layout() will return 0.
		"""
		res = super(QGraphicsWidget,self).setLayout(layout)
		return res
	#----------------------------------------------------------------------
	def setLayoutDirection(self,direction):
		"""
		setLayoutDirection(direction)
			direction=QtCore.Qt.LayoutDirection

		This property holds the layout direction for this widget..
		This property modifies this widgets and all of its descendants Qt.WA_RightToLeft attribute
		It also sets this widgets Qt.WA_SetLayoutDirection attribute.
		The widgets layout direction determines the order in which the layout manager horizontally arranges subwidgets of this widget
		The default value depends on the language and locale of the application, and is typically in the same direction as words are read and written
		With Qt.LeftToRight , the layout starts placing subwidgets from the left side of this widget towards the right
		Qt.RightToLeft does the opposite - the layout will place widgets starting from the right edge moving towards the left.
		Subwidgets inherit their layout direction from the parent
		Top-level widget items inherit their layout direction from QGraphicsScene::layoutDirection
		If you change a widgets layout direction by calling PySide.QtGui.QGraphicsWidget.setLayoutDirection() , the widget will send itself a LayoutDirectionChange event, and then propagate the new layout direction to all its descendants.
		"""
		res = super(QGraphicsWidget,self).setLayoutDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setPalette(self,palette):
		"""
		setPalette(palette)
			palette=QtGui.QPalette

		This property holds the widgets palette.
		This property provides the widgets palette
		The palette provides colors and brushes for color groups (e.g., QPalette.Button ) and states (e.g., QPalette.Inactive ), loosely defining the general look of the widget and its children.
		PySide.QtGui.QPalette consists of color groups that have been explicitly defined, and groups that are implicitly inherited from the widgets parent
		Because of this, PySide.QtGui.QGraphicsWidget.palette() can return a different palette than what has been set with PySide.QtGui.QGraphicsWidget.setPalette()
		This scheme allows you to define single entries in a palette without affecting the palettes inherited entries.
		When a widgets palette changes, it resolves its entries against its parent widget, or if it doesnt have a parent widget, it resolves against the scene
		It then sends itself a PaletteChange event, and notifies all its descendants so they can resolve their palettes as well.
		By default, this property contains the applications default palette.
		"""
		res = super(QGraphicsWidget,self).setPalette(palette)
		return res
	#----------------------------------------------------------------------
	def setShortcutAutoRepeat(self,id,enabled=None):
		"""
		setShortcutAutoRepeat(id,enabled=None)
			id=QtCore.int
			enabled=QtCore.bool

		If enabled is true, auto repeat of the shortcut with the given id is enabled; otherwise it is disabled.
		"""
		res = super(QGraphicsWidget,self).setShortcutAutoRepeat(id,enabled)
		return res
	#----------------------------------------------------------------------
	def setShortcutEnabled(self,id,enabled=None):
		"""
		setShortcutEnabled(id,enabled=None)
			id=QtCore.int
			enabled=QtCore.bool

		If enabled is true, the shortcut with the given id is enabled; otherwise the shortcut is disabled.
		"""
		res = super(QGraphicsWidget,self).setShortcutEnabled(id,enabled)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,style):
		"""
		setStyle(style)
			style=QtGui.QStyle

		Sets the widgets style to style
		PySide.QtGui.QGraphicsWidget does not take ownership of style .
		If no style is assigned, or style is 0, the widget will use QGraphicsScene.style() (if this has been set)
		Otherwise the widget will use QApplication.style() .
		This function sets the Qt.WA_SetStyle attribute if style is not 0; otherwise it clears the attribute.
		"""
		res = super(QGraphicsWidget,self).setStyle(style)
		return res
	#----------------------------------------------------------------------
	def setWindowFlags(self,wFlags):
		"""
		setWindowFlags(wFlags)
			wFlags=QtCore.Qt.WindowFlags

		This property holds the widgets window flags.
		Window flags are a combination of a window type (e.g., Qt.Dialog ) and several flags giving hints on the behavior of the window
		The behavior is platform-dependent.
		By default, this property contains no window flags.
		Windows are panels
		If you set the Qt.Window flag, the ItemIsPanel flag will be set automatically
		If you clear the Qt.Window flag, the ItemIsPanel flag is also cleared
		Note that the ItemIsPanel flag can be set independently of Qt.Window .
		"""
		res = super(QGraphicsWidget,self).setWindowFlags(wFlags)
		return res
	#----------------------------------------------------------------------
	def setWindowFrameMargins(self,left,top,right,bottom):
		"""
		setWindowFrameMargins(left,top,right,bottom)
			left=QtCore.qreal
			top=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal

		Sets the widgets window frame margins to left , top , right and bottom
		The default frame margins are provided by the style, and they depend on the current window flags.
		If you would like to draw your own window decoration, you can set your own frame margins to override the default margins.
		"""
		res = super(QGraphicsWidget,self).setWindowFrameMargins(left,top,right,bottom)
		return res
	#----------------------------------------------------------------------
	def setWindowTitle(self,title):
		"""
		setWindowTitle(title)
			title=unicode

		This property holds This property holds the window title (caption)..
		This property is only used for windows.
		By default, if no title has been set, this property contains an empty string.
		"""
		res = super(QGraphicsWidget,self).setWindowTitle(title)
		return res
	#----------------------------------------------------------------------
	def showEvent(self,event):
		"""
		showEvent(event)
			event=QtGui.QShowEvent

		This event handler, for Show events, is delivered before the widget has been shown, for example, setVisible(true) has been called for the widget or one of its ancestors when the widget was previously hidden.
		You can reimplement this event handler to detect when your widget is shown
		Calling QEvent.accept() or QEvent.ignore() on event has no effect.
		"""
		res = super(QGraphicsWidget,self).showEvent(event)
		return res
	#----------------------------------------------------------------------
	def testAttribute(self,attribute):
		"""
		testAttribute(attribute)
			attribute=QtCore.Qt.WidgetAttribute


		"""
		res = super(QGraphicsWidget,self).testAttribute(attribute)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def ungrabKeyboardEvent(self,event):
		"""
		ungrabKeyboardEvent(event)
			event=QtCore.QEvent

		This event handler, for event , can be reimplemented in a subclass to receive notifications for Qt::UngrabKeyboard events.
		"""
		res = super(QGraphicsWidget,self).ungrabKeyboardEvent(event)
		return res
	#----------------------------------------------------------------------
	def ungrabMouseEvent(self,event):
		"""
		ungrabMouseEvent(event)
			event=QtCore.QEvent

		This event handler, for event , can be reimplemented in a subclass to receive notifications for Qt::UngrabMouse events.
		"""
		res = super(QGraphicsWidget,self).ungrabMouseEvent(event)
		return res
	#----------------------------------------------------------------------
	def windowFrameEvent(self,e):
		"""
		windowFrameEvent(e)
			e=QtCore.QEvent

		This event handler, for event , receives events for the window frame if this widget is a window
		Its base implementation provides support for default window frame interaction such as moving, resizing, etc.
		You can reimplement this handler in a subclass of PySide.QtGui.QGraphicsWidget to provide your own custom window frame interaction support.
		Returns true if event has been recognized and processed; otherwise, returns false.
		"""
		res = super(QGraphicsWidget,self).windowFrameEvent(e)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def windowFrameSectionAt(self,pos):
		"""
		windowFrameSectionAt(pos)
			pos=QtCore.QPointF

		Returns the window frame section at position pos , or Qt.NoSection if there is no window frame section at this position.
		This function is used in PySide.QtGui.QGraphicsWidget s base implementation for window frame interaction.
		You can reimplement this function if you want to customize how a window can be interactively moved or resized
		For instance, if you only want to allow a window to be resized by the bottom right corner, you can reimplement this function to return Qt.NoSection for all sections except Qt.BottomRightSection .
		"""
		res = super(QGraphicsWidget,self).windowFrameSectionAt(pos)
		isinstance(res,QtCore.Qt.WindowFrameSection)
		return res
