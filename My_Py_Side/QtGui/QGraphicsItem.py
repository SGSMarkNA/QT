from PySide import QtGui, QtCore

class QGraphicsItem(QtGui.QGraphicsItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsItem,self).__init__(*args,**kwargs)
		if False:
			isinstance(self.Bounding_Rect, QtCore.QRectF)
			isinstance(self.Pos, QtCore.QPointF)
			isinstance(self.Opaque_Area, QtGui.QPainterPath)
			isinstance(self.Panel, QtGui.QGraphicsItem)
			isinstance(self.Parent_Item, QtGui.QGraphicsItem)
			isinstance(self.Parent_Widget, QtGui.QGraphicsWidget)
			isinstance(self.Scene, QtGui.QGraphicsScene)
			isinstance(self.Scene_Bounding_Rect, QtCore.QRectF)
			isinstance(self.Scene_Pos, QtCore.QPointF)
			isinstance(self.Scene_Transform, QtGui.QTransform)
			isinstance(self.Shape, QtGui.QPainterPath)
			isinstance(self.Top_Level_Item, QtGui.QGraphicsItem)
			isinstance(self.Top_Level_Widget, QtGui.QGraphicsWidget)
			isinstance(self.Tranform_Matrix, QtGui.QTransform)
			isinstance(self.Transform_Origin_Point, QtCore.QPointF)
			isinstance(self.Transformations, list)
	#----------------------------------------------------------------------
	def acceptDrops(self):
		"""
		Returns true if this item can accept drag and drop events; otherwise, returns false
		By default, items do not accept drag and drop events; items are transparent to drag and drop.
		"""
		res = super(QGraphicsItem,self).acceptDrops()

		return res
	#----------------------------------------------------------------------
	def acceptHoverEvents(self):
		"""
		Returns true if an item accepts hover events ( PySide.QtGui.QGraphicsSceneHoverEvent ); otherwise, returns false
		By default, items do not accept hover events.
		"""
		res = super(QGraphicsItem,self).acceptHoverEvents()

		return res
	#----------------------------------------------------------------------
	def acceptTouchEvents(self):
		"""
		Returns true if an item accepts touch events ; otherwise, returns false
		By default, items do not accept touch events.
		"""
		res = super(QGraphicsItem,self).acceptTouchEvents()

		return res
	#----------------------------------------------------------------------
	def acceptedMouseButtons(self):
		"""
		Returns the mouse buttons that this item accepts mouse events for
		By default, all mouse buttons are accepted.
		If an item accepts a mouse button, it will become the mouse grabber item when a mouse press event is delivered for that mouse button
		However, if the item does not accept the button, PySide.QtGui.QGraphicsScene will forward the mouse events to the first item beneath it that does.
		"""
		res = super(QGraphicsItem,self).acceptedMouseButtons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def acceptsHoverEvents(self):
		"""
		Call PySide.QtGui.QGraphicsItem.acceptHoverEvents() instead.
		"""
		res = super(QGraphicsItem,self).acceptsHoverEvents()

		return res
	#----------------------------------------------------------------------
	def addToIndex(self):
		"""
		Adds this item to the scenes index
		Called in conjunction with PySide.QtGui.QGraphicsItem.removeFromIndex() to ensure the index bookkeeping is correct when the items position, transformation or shape changes.
		"""
		res = super(QGraphicsItem,self).addToIndex()
		return res
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		This pure virtual function defines the outer bounds of the item as a rectangle; all painting must be restricted to inside an items bounding rect
		PySide.QtGui.QGraphicsView uses this to determine whether the item requires redrawing.
		Although the items shape can be arbitrary, the bounding rect is always rectangular, and it is unaffected by the items transformation.
		If you want to change the items bounding rectangle, you must first call PySide.QtGui.QGraphicsItem.prepareGeometryChange()
		This notifies the scene of the imminent change, so that its can update its item geometry index; otherwise, the scene will be unaware of the items new geometry, and the results are undefined (typically, rendering artifacts are left around in the view).
		Reimplement this function to let PySide.QtGui.QGraphicsView determine what parts of the widget, if any, need to be redrawn.
		Note: For shapes that paint an outline / stroke, it is important to include half the pen width in the bounding rect
		It is not necessary to compensate for antialiasing, though.
		Example:
		"""
		res = super(QGraphicsItem,self).boundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def boundingRegionGranularity(self):
		"""
		Returns the items bounding region granularity; a value between and including 0 and 1
		The default value is 0 (i.e., the lowest granularity, where the bounding region corresponds to the items bounding rectangle).
		"""
		res = super(QGraphicsItem,self).boundingRegionGranularity()

		return res
	#----------------------------------------------------------------------
	def cacheMode(self):
		"""
		Returns the cache mode for this item
		The default mode is NoCache (i.e., cache is disabled and all painting is immediate).
		"""
		res = super(QGraphicsItem,self).cacheMode()
		isinstance(res,QtGui.QGraphicsItem.CacheMode)
		return res
	#----------------------------------------------------------------------
	def childItems(self):
		"""
		Returns a list of this items children.
		The items are sorted by stacking order
		This takes into account both the items insertion order and their Z-values.
		"""
		res = super(QGraphicsItem,self).childItems()
		return res
	#----------------------------------------------------------------------
	def childrenBoundingRect(self):
		"""
		Returns the bounding rect of this items descendants (i.e., its children, their children, etc.) in local coordinates
		The rectangle will contain all descendants after they have been mapped to local coordinates
		If the item has no children, this function returns an empty PySide.QtCore.QRectF .
		This does not include this items own bounding rect; it only returns its descendants accumulated bounding rect
		If you need to include this items bounding rect, you can add PySide.QtGui.QGraphicsItem.boundingRect() to PySide.QtGui.QGraphicsItem.childrenBoundingRect() using QRectF::operator|().
		This function is linear in complexity; it determines the size of the returned bounding rect by iterating through all descendants.
		"""
		res = super(QGraphicsItem,self).childrenBoundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def clearFocus(self):
		"""
		Takes keyboard input focus from the item.
		If it has focus, a focus out event is sent to this item to tell it that it is about to lose the focus.
		Only items that set the ItemIsFocusable flag, or widgets that set an appropriate focus policy, can accept keyboard focus.
		"""
		res = super(QGraphicsItem,self).clearFocus()
		return res
	#----------------------------------------------------------------------
	def clipPath(self):
		"""
		Returns this items clip path, or an empty PySide.QtGui.QPainterPath if this item is not clipped
		The clip path constrains the items appearance and interaction (i.e., restricts the area the item can draw, and it also restricts the area that the item receives events).
		You can enable clipping by setting the ItemClipsToShape or ItemClipsChildrenToShape flags
		The items clip path is calculated by intersecting all clipping ancestors shapes
		If the item sets ItemClipsToShape , the final clip is intersected with the items own shape.
		"""
		res = super(QGraphicsItem,self).clipPath()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def cursor(self):
		"""
		Returns the current cursor shape for the item
		The mouse cursor will assume this shape when its over this item
		See the list of predefined cursor objects for a range of useful shapes.
		An editor item might want to use an I-beam cursor:
		If no cursor has been set, the cursor of the item beneath is used.
		"""
		res = super(QGraphicsItem,self).cursor()
		isinstance(res,QtGui.QCursor)
		return res
	#----------------------------------------------------------------------
	def effectiveOpacity(self):
		"""
		Returns this items effective opacity, which is between 0.0 (transparent) and 1.0 (opaque)
		This value is a combination of this items local opacity, and its parent and ancestors opacities
		The effective opacity decides how the item is rendered.
		"""
		res = super(QGraphicsItem,self).effectiveOpacity()

		return res
	#----------------------------------------------------------------------
	def filtersChildEvents(self):
		"""
		Returns true if this item filters child events (i.e., all events intended for any of its children are instead sent to this item); otherwise, false is returned.
		The default value is false; child events are not filtered.
		"""
		res = super(QGraphicsItem,self).filtersChildEvents()

		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns this items flags
		The flags describe what configurable features of the item are enabled and not
		For example, if the flags include ItemIsFocusable , the item can accept input focus.
		By default, no flags are enabled.
		"""
		res = super(QGraphicsItem,self).flags()
		isinstance(res,QtGui.QGraphicsItem.GraphicsItemFlags)
		return res
	#----------------------------------------------------------------------
	def focusItem(self):
		"""
		If this item, a child or descendant of this item currently has input focus, this function will return a pointer to that item
		If no descendant has input focus, 0 is returned.
		"""
		res = super(QGraphicsItem,self).focusItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def focusProxy(self):
		"""
		Returns this items focus proxy, or 0 if this item has no focus proxy.
		"""
		res = super(QGraphicsItem,self).focusProxy()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def focusScopeItem(self):
		"""
		Returns this items focus scope item.
		"""
		res = super(QGraphicsItem,self).focusScopeItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def grabKeyboard(self):
		"""
		Grabs the keyboard input.
		The item will receive all keyboard input to the scene until one of the following events occur:
		When an item gains the keyboard grab, it receives a QEvent.GrabKeyboard event
		When it loses the keyboard grab, it receives a QEvent.UngrabKeyboard event
		These events can be used to detect when your item gains or loses the keyboard grab through other means than gaining input focus.
		It is almost never necessary to explicitly grab the keyboard in Qt, as Qt grabs and releases it sensibly
		In particular, Qt grabs the keyboard when your item gains input focus, and releases it when your item loses input focus, or when the item is hidden.
		Note that only visible items can grab keyboard input
		Calling PySide.QtGui.QGraphicsItem.grabKeyboard() on an invisible item has no effect.
		Keyboard events are not affected.
		"""
		res = super(QGraphicsItem,self).grabKeyboard()
		return res
	#----------------------------------------------------------------------
	def grabMouse(self):
		"""
		Grabs the mouse input.
		This item will receive all mouse events for the scene until any of the following events occurs:
		When an item gains the mouse grab, it receives a QEvent.GrabMouse event
		When it loses the mouse grab, it receives a QEvent.UngrabMouse event
		These events can be used to detect when your item gains or loses the mouse grab through other means than receiving mouse button events.
		It is almost never necessary to explicitly grab the mouse in Qt, as Qt grabs and releases it sensibly
		In particular, Qt grabs the mouse when you press a mouse button, and keeps the mouse grabbed until you release the last mouse button
		Also, Qt.Popup widgets implicitly call PySide.QtGui.QGraphicsItem.grabMouse() when shown, and PySide.QtGui.QGraphicsItem.ungrabMouse() when hidden.
		Note that only visible items can grab mouse input
		Calling PySide.QtGui.QGraphicsItem.grabMouse() on an invisible item has no effect.
		Keyboard events are not affected.
		"""
		res = super(QGraphicsItem,self).grabMouse()
		return res
	#----------------------------------------------------------------------
	def graphicsEffect(self):
		"""
		Returns a pointer to this items effect if it has one; otherwise 0.
		"""
		res = super(QGraphicsItem,self).graphicsEffect()
		isinstance(res,QtGui.QGraphicsEffect)
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns a pointer to this items item group, or 0 if this item is not member of a group.
		"""
		res = super(QGraphicsItem,self).group()
		isinstance(res,QtGui.QGraphicsItemGroup)
		return res
	#----------------------------------------------------------------------
	def handlesChildEvents(self):
		"""
		Returns true if this item handles child events (i.e., all events intended for any of its children are instead sent to this item); otherwise, false is returned.
		This property is useful for item groups; it allows one item to handle events on behalf of its children, as opposed to its children handling their events individually.
		The default is to return false; children handle their own events
		The exception for this is if the item is a PySide.QtGui.QGraphicsItemGroup , then it defaults to return true.
		"""
		res = super(QGraphicsItem,self).handlesChildEvents()

		return res
	#----------------------------------------------------------------------
	def hasCursor(self):
		"""
		Returns true if this item has a cursor set; otherwise, false is returned.
		By default, items dont have any cursor set
		PySide.QtGui.QGraphicsItem.cursor() will return a standard pointing arrow cursor.
		"""
		res = super(QGraphicsItem,self).hasCursor()

		return res
	#----------------------------------------------------------------------
	def hasFocus(self):
		"""
		Returns true if this item is active, and it or its focus proxy has keyboard input focus; otherwise, returns false.
		"""
		res = super(QGraphicsItem,self).hasFocus()

		return res
	#----------------------------------------------------------------------
	def hide(self):
		"""
		Hides the item
		(Items are visible by default.)
		This convenience function is equivalent to calling setVisible(false) .
		"""
		res = super(QGraphicsItem,self).hide()
		return res
	#----------------------------------------------------------------------
	def inputMethodHints(self):
		"""
		Returns the current input method hints of this item.
		Input method hints are only relevant for input items
		The hints are used by the input method to indicate how it should operate
		For example, if the Qt::ImhNumbersOnly flag is set, the input method may change its visual components to reflect that only numbers can be entered.
		The effect may vary between input method implementations.
		"""
		res = super(QGraphicsItem,self).inputMethodHints()
		isinstance(res,QtCore.Qt.InputMethodHints)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if this item is active; otherwise returns false.
		An item can only be active if the scene is active
		An item is active if it is, or is a descendent of, an active panel
		Items in non-active panels are not active.
		Items that are not part of a panel follow scene activation when the scene has no active panel.
		Only active items can gain input focus.
		"""
		res = super(QGraphicsItem,self).isActive()

		return res
	#----------------------------------------------------------------------
	def isBlockedByModalPanel(self):
		"""
		Returns true if this item is blocked by a modal panel, false otherwise
		If blockingPanel is non-zero, blockingPanel will be set to the modal panel that is blocking this item
		If this item is not blocked, blockingPanel will not be set by this function.
		This function always returns false for items not in a scene.
		"""
		res = super(QGraphicsItem,self).isBlockedByModalPanel()
		return res
	#----------------------------------------------------------------------
	def isClipped(self):
		"""
		Returns true if this item is clipped
		An item is clipped if it has either set the ItemClipsToShape flag, or if it or any of its ancestors has set the ItemClipsChildrenToShape flag.
		Clipping affects the items appearance (i.e., painting), as well as mouse and hover event delivery.
		"""
		res = super(QGraphicsItem,self).isClipped()

		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		Returns true if the item is enabled; otherwise, false is returned.
		"""
		res = super(QGraphicsItem,self).isEnabled()

		return res
	#----------------------------------------------------------------------
	def isObscured(self):
		"""
		Returns true if this items bounding rect is completely obscured by the opaque shape of any of colliding items above it (i.e., with a higher Z value than this item).
		Its implementation is based on calling PySide.QtGui.QGraphicsItem.isObscuredBy() , which you can reimplement to provide a custom obscurity algorithm.
		"""
		res = super(QGraphicsItem,self).isObscured()

		return res
	#----------------------------------------------------------------------
	def isPanel(self):
		"""
		Returns true if the item is a panel; otherwise returns false.
		"""
		res = super(QGraphicsItem,self).isPanel()

		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if this item is selected; otherwise, false is returned.
		Items that are in a group inherit the groups selected state.
		Items are not selected by default.
		"""
		res = super(QGraphicsItem,self).isSelected()

		return res
	#----------------------------------------------------------------------
	def isUnderMouse(self):
		"""
		Returns true if this item is currently under the mouse cursor in one of the views; otherwise, false is returned.
		"""
		res = super(QGraphicsItem,self).isUnderMouse()

		return res
	#----------------------------------------------------------------------
	def isVisible(self):
		"""
		Returns true if the item is visible; otherwise, false is returned.
		Note that the items general visibility is unrelated to whether or not it is actually being visualized by a PySide.QtGui.QGraphicsView .
		"""
		res = super(QGraphicsItem,self).isVisible()

		return res
	#----------------------------------------------------------------------
	def isWidget(self):
		"""
		Returns true if this item is a widget (i.e., PySide.QtGui.QGraphicsWidget ); otherwise, returns false.
		"""
		res = super(QGraphicsItem,self).isWidget()

		return res
	#----------------------------------------------------------------------
	def isWindow(self):
		"""
		Returns true if the item is a PySide.QtGui.QGraphicsWidget window, otherwise returns false.
		"""
		res = super(QGraphicsItem,self).isWindow()

		return res
	#----------------------------------------------------------------------
	def opacity(self):
		"""
		Returns this items local opacity, which is between 0.0 (transparent) and 1.0 (opaque)
		This value is combined with parent and ancestor values into the PySide.QtGui.QGraphicsItem.effectiveOpacity()
		The effective opacity decides how the item is rendered.
		The opacity property decides the state of the painter passed to the PySide.QtGui.QGraphicsItem.paint() function
		If the item is cached, i.e., ItemCoordinateCache or DeviceCoordinateCache , the effective property will be applied to the items cache as it is rendered.
		The default opacity is 1.0; fully opaque.
		"""
		res = super(QGraphicsItem,self).opacity()
		return res
	#----------------------------------------------------------------------
	def opaqueArea(self):
		"""
		This virtual function returns a shape representing the area where this item is opaque
		An area is opaque if it is filled using an opaque brush or color (i.e., not transparent).
		This function is used by PySide.QtGui.QGraphicsItem.isObscuredBy() , which is called by underlying items to determine if they are obscured by this item.
		The default implementation returns an empty PySide.QtGui.QPainterPath , indicating that this item is completely transparent and does not obscure any other items.
		"""
		res = super(QGraphicsItem,self).opaqueArea()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def panel(self):
		"""
		Returns the items panel, or 0 if this item does not have a panel
		If the item is a panel, it will return itself
		Otherwise it will return the closest ancestor that is a panel.
		"""
		res = super(QGraphicsItem,self).panel()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def panelModality(self):
		"""
		Returns the modality for this item.
		"""
		res = super(QGraphicsItem,self).panelModality()
		isinstance(res,QtGui.QGraphicsItem.PanelModality)
		return res
	#----------------------------------------------------------------------
	def parentItem(self):
		"""
		Returns a pointer to this items parent item
		If this item does not have a parent, 0 is returned.
		"""
		res = super(QGraphicsItem,self).parentItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def parentObject(self):
		"""
		Returns a pointer to the items parent, cast to a PySide.QtGui.QGraphicsObject
		returns 0 if the parent item is not a PySide.QtGui.QGraphicsObject .
		"""
		res = super(QGraphicsItem,self).parentObject()
		isinstance(res,QtGui.QGraphicsObject)
		return res
	#----------------------------------------------------------------------
	def parentWidget(self):
		"""
		Returns a pointer to the items parent widget
		The items parent widget is the closest parent item that is a widget.
		"""
		res = super(QGraphicsItem,self).parentWidget()
		isinstance(res,QtGui.QGraphicsWidget)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the item in parent coordinates
		If the item has no parent, its position is given in scene coordinates.
		The position of the item describes its origin (local coordinate (0, 0)) in parent coordinates; this function returns the same as mapToParent(0, 0).
		For convenience, you can also call PySide.QtGui.QGraphicsItem.scenePos() to determine the items position in scene coordinates, regardless of its parent.
		"""
		res = super(QGraphicsItem,self).pos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def prepareGeometryChange(self):
		"""
		Prepares the item for a geometry change
		Call this function before changing the bounding rect of an item to keep PySide.QtGui.QGraphicsScene s index up to date.
		PySide.QtGui.QGraphicsItem.prepareGeometryChange() will call PySide.QtGui.QGraphicsItem.update() if this is necessary.
		Example:
		"""
		res = super(QGraphicsItem,self).prepareGeometryChange()
		return res
	#----------------------------------------------------------------------
	def removeFromIndex(self):
		"""
		Removes this item from the scenes index
		Called in conjunction with PySide.QtGui.QGraphicsItem.addToIndex() to ensure the index bookkeeping is correct when the items position, transformation or shape changes.
		"""
		res = super(QGraphicsItem,self).removeFromIndex()
		return res
	#----------------------------------------------------------------------
	def resetTransform(self):
		"""
		Resets this items transformation matrix to the identity matrix or all the transformation properties to their default values
		This is equivalent to calling setTransform(QTransform()) .
		"""
		res = super(QGraphicsItem,self).resetTransform()
		return res
	#----------------------------------------------------------------------
	def rotation(self):
		"""
		Returns the clockwise rotation, in degrees, around the Z axis
		The default value is 0 (i.e., the item is not rotated).
		The rotation is combined with the items PySide.QtGui.QGraphicsItem.scale() , PySide.QtGui.QGraphicsItem.transform() and PySide.QtGui.QGraphicsItem.transformations() to map the items coordinate system to the parent item.
		"""
		res = super(QGraphicsItem,self).rotation()

		return res
	#----------------------------------------------------------------------
	def scale(self):
		"""
		Returns the scale factor of the item
		The default scale factor is 1.0 (i.e., the item is not scaled).
		The scale is combined with the items PySide.QtGui.QGraphicsItem.rotation() , PySide.QtGui.QGraphicsItem.transform() and PySide.QtGui.QGraphicsItem.transformations() to map the items coordinate system to the parent item.
		"""
		res = super(QGraphicsItem,self).scale()

		return res
	#----------------------------------------------------------------------
	def scene(self):
		"""
		Returns the current scene for the item, or 0 if the item is not stored in a scene.
		To add or move an item to a scene, call QGraphicsScene.addItem() .
		"""
		res = super(QGraphicsItem,self).scene()
		isinstance(res,QtGui.QGraphicsScene)
		return res
	#----------------------------------------------------------------------
	def sceneBoundingRect(self):
		"""
		Returns the bounding rect of this item in scene coordinates, by combining PySide.QtGui.QGraphicsItem.sceneTransform() with PySide.QtGui.QGraphicsItem.boundingRect() .
		"""
		res = super(QGraphicsItem,self).sceneBoundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def scenePos(self):
		"""
		Returns the items position in scene coordinates
		This is equivalent to calling mapToScene(0, 0) .
		"""
		res = super(QGraphicsItem,self).scenePos()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def sceneTransform(self):
		"""
		Returns this items scene transformation matrix
		This matrix can be used to map coordinates and geometrical shapes from this items local coordinate system to the scenes coordinate system
		To map coordinates from the scene, you must first invert the returned matrix.
		Example:
		Unlike PySide.QtGui.QGraphicsItem.transform() , which returns only an items local transformation, this function includes the items (and any parents) position, and all the transfomation properties.
		"""
		res = super(QGraphicsItem,self).sceneTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def shape(self):
		"""
		Returns the shape of this item as a PySide.QtGui.QPainterPath in local coordinates
		The shape is used for many things, including collision detection, hit tests, and for the QGraphicsScene.items() functions.
		The default implementation calls PySide.QtGui.QGraphicsItem.boundingRect() to return a simple rectangular shape, but subclasses can reimplement this function to return a more accurate shape for non-rectangular items
		For example, a round item may choose to return an elliptic shape for better collision detection
		For example:
		The outline of a shape can vary depending on the width and style of the pen used when drawing
		If you want to include this outline in the items shape, you can create a shape from the stroke using PySide.QtGui.QPainterPathStroker .
		This function is called by the default implementations of PySide.QtGui.QGraphicsItem.contains() and PySide.QtGui.QGraphicsItem.collidesWithPath() .
		"""
		res = super(QGraphicsItem,self).shape()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def show(self):
		"""
		Shows the item
		(Items are visible by default.)
		This convenience function is equivalent to calling setVisible(true) .
		"""
		res = super(QGraphicsItem,self).show()
		return res
	#----------------------------------------------------------------------
	def toGraphicsObject(self):
		"""
		Return the graphics item cast to a PySide.QtGui.QGraphicsObject , if the class is actually a graphics object, 0 otherwise.
		"""
		res = super(QGraphicsItem,self).toGraphicsObject()
		isinstance(res,QtGui.QGraphicsObject)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the items tool tip, or an empty PySide.QtCore.QString if no tool tip has been set.
		"""
		res = super(QGraphicsItem,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def topLevelItem(self):
		"""
		Returns this items top-level item
		The top-level item is the items topmost ancestor item whose parent is 0
		If an item has no parent, its own pointer is returned (i.e., a top-level item is its own top-level item).
		"""
		res = super(QGraphicsItem,self).topLevelItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def topLevelWidget(self):
		"""
		Returns a pointer to the items top level widget (i.e., the items ancestor whose parent is 0, or whose parent is not a widget), or 0 if this item does not have a top level widget
		If the item is its own top level widget, this function returns a pointer to the item itself.
		"""
		res = super(QGraphicsItem,self).topLevelWidget()
		isinstance(res,QtGui.QGraphicsWidget)
		return res
	#----------------------------------------------------------------------
	def transform(self):
		"""
		Returns this items transformation matrix.
		The transformation matrix is combined with the items PySide.QtGui.QGraphicsItem.rotation() , PySide.QtGui.QGraphicsItem.scale() and PySide.QtGui.QGraphicsItem.transformations() into a combined transformations for the item.
		The default transformation matrix is an identity matrix.
		"""
		res = super(QGraphicsItem,self).transform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def transformOriginPoint(self):
		"""
		Returns the origin point for the transformation in item coordinates.
		The default is PySide.QtCore.QPointF (0,0).
		"""
		res = super(QGraphicsItem,self).transformOriginPoint()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def transformations(self):
		"""
		Returns a list of graphics transforms that currently apply to this item.
		PySide.QtGui.QGraphicsTransform is for applying and controlling a chain of individual transformation operations on an item
		Its particularly useful in animations, where each transform operation needs to be interpolated independently, or differently.
		The transformations are combined with the items PySide.QtGui.QGraphicsItem.rotation() , PySide.QtGui.QGraphicsItem.scale() and PySide.QtGui.QGraphicsItem.transform() to map the items coordinate system to the parent item.
		"""
		res = super(QGraphicsItem,self).transformations()
		isinstance(res, list)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of an item as an int
		All standard graphicsitem classes are associated with a unique value; see QGraphicsItem.Type
		This type information is used by qgraphicsitem_cast() to distinguish between types.
		The default implementation (in PySide.QtGui.QGraphicsItem ) returns UserType .
		To enable use of qgraphicsitem_cast() with a custom item, reimplement this function and declare a Type enum value equal to your custom items type
		Custom items must return a value larger than or equal to UserType (65536).
		For example:
		"""
		res = super(QGraphicsItem,self).type()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def ungrabKeyboard(self):
		"""
		Releases the keyboard grab.
		"""
		res = super(QGraphicsItem,self).ungrabKeyboard()
		return res
	#----------------------------------------------------------------------
	def ungrabMouse(self):
		"""
		Releases the mouse grab.
		"""
		res = super(QGraphicsItem,self).ungrabMouse()
		return res
	#----------------------------------------------------------------------
	def unsetCursor(self):
		"""
		Clears the cursor from this item.
		"""
		res = super(QGraphicsItem,self).unsetCursor()
		return res
	#----------------------------------------------------------------------
	def updateMicroFocus(self):
		"""
		Updates the items micro focus.
		"""
		res = super(QGraphicsItem,self).updateMicroFocus()
		return res
	#----------------------------------------------------------------------
	def window(self):
		"""
		Returns the items window, or 0 if this item does not have a window
		If the item is a window, it will return itself
		Otherwise it will return the closest ancestor that is a window.
		"""
		res = super(QGraphicsItem,self).window()
		isinstance(res,QtGui.QGraphicsWidget)
		return res
	#----------------------------------------------------------------------
	def x(self):
		"""
		This convenience function is equivalent to calling PySide.QtGui.QGraphicsItem.pos()
		PySide.QtGui.QGraphicsItem.x() .
		"""
		res = super(QGraphicsItem,self).x()

		return res
	#----------------------------------------------------------------------
	def y(self):
		"""
		This convenience function is equivalent to calling PySide.QtGui.QGraphicsItem.pos()
		PySide.QtGui.QGraphicsItem.y() .
		"""
		res = super(QGraphicsItem,self).y()

		return res
	#----------------------------------------------------------------------
	def zValue(self):
		"""
		Returns the Z-value of the item
		The Z-value affects the stacking order of sibling (neighboring) items.
		The default Z-value is 0.
		"""
		res = super(QGraphicsItem,self).zValue()

		return res

	#####################
	## VIRTUAL FUNCTIONS
	#####################

	#----------------------------------------------------------------------
	def advance(self,phase):
		"""
		advance(phase)
			phase=QtCore.int

		This virtual function is called twice for all items by the QGraphicsScene.advance() slot
		In the first phase, all items are called with phase == 0, indicating that items on the scene are about to advance, and then all items are called with phase == 1
		Reimplement this function to update your item if you need simple scene-controlled animation.
		The default implementation does nothing.
		For individual item animation, an alternative to this function is to either use PySide.QtGui.QGraphicsItemAnimation , or to multiple-inherit from PySide.QtCore.QObject and PySide.QtGui.QGraphicsItem , and animate your item using QObject.startTimer() and QObject.timerEvent() .
		"""
		res = super(QGraphicsItem,self).advance(phase)
		return res
	#----------------------------------------------------------------------
	def boundingRegion(self,itemToDeviceTransform):
		"""
		boundingRegion(itemToDeviceTransform)
			itemToDeviceTransform=QtGui.QTransform

		Returns the bounding region for this item
		The coordinate space of the returned region depends on itemToDeviceTransform
		If you pass an identity PySide.QtGui.QTransform as a parameter, this function will return a local coordinate region.
		The bounding region describes a coarse outline of the items visual contents
		Although its expensive to calculate, its also more precise than PySide.QtGui.QGraphicsItem.boundingRect() , and it can help to avoid unnecessary repainting when an item is updated
		This is particularly efficient for thin items (e.g., lines or simple polygons)
		You can tune the granularity for the bounding region by calling PySide.QtGui.QGraphicsItem.setBoundingRegionGranularity()
		The default granularity is 0; in which the items bounding region is the same as its bounding rect.
		itemToDeviceTransform is the transformation from item coordinates to device coordinates
		If you want this function to return a PySide.QtGui.QRegion in scene coordinates, you can pass PySide.QtGui.QGraphicsItem.sceneTransform() as an argument.
		"""
		res = super(QGraphicsItem,self).boundingRegion(itemToDeviceTransform)
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def collidesWithItem(self,other,mode=QtCore.Qt.IntersectsItemBoundingRect):
		"""
		collidesWithItem(other,mode=None)
			other=QtGui.QGraphicsItem
			mode=QtCore.Qt.ItemSelectionMode


		"""
		res = super(QGraphicsItem,self).collidesWithItem(other,mode)

		return res
	#----------------------------------------------------------------------
	def collidesWithPath(self,path,mode=QtCore.Qt.IntersectsItemBoundingRect):
		"""
		collidesWithPath(path,mode=None)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode


		"""
		res = super(QGraphicsItem,self).collidesWithPath(path,mode)

		return res
	#----------------------------------------------------------------------
	def collidingItems(self,mode=QtCore.Qt.IntersectsItemBoundingRect):
		"""
		collidingItems(mode=None)
			mode=QtCore.Qt.ItemSelectionMode


		"""
		res = super(QGraphicsItem,self).collidingItems(mode)
		return res
	#----------------------------------------------------------------------
	def commonAncestorItem(self,other):
		"""
		commonAncestorItem(other)
			other=QtGui.QGraphicsItem

		Returns the closest common ancestor item of this item and other , or 0 if either other is 0, or there is no common ancestor.
		"""
		res = super(QGraphicsItem,self).commonAncestorItem(other)
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def contains(self,point):
		"""
		contains(point)
			point=QtCore.QPointF

		Returns true if this item contains point , which is in local coordinates; otherwise, false is returned
		It is most often called from PySide.QtGui.QGraphicsView to determine what item is under the cursor, and for that reason, the implementation of this function should be as light-weight as possible.
		By default, this function calls PySide.QtGui.QGraphicsItem.shape() , but you can reimplement it in a subclass to provide a (perhaps more efficient) implementation.
		"""
		res = super(QGraphicsItem,self).contains(point)

		return res
	#----------------------------------------------------------------------
	def contextMenuEvent(self,event):
		"""
		contextMenuEvent(event)
			event=QtGui.QGraphicsSceneContextMenuEvent

		This event handler can be reimplemented in a subclass to process context menu events
		The event parameter contains details about the event to be handled.
		If you ignore the event, (i.e., by calling QEvent.ignore() ,) event will propagate to any item beneath this item
		If no items accept the event, it will be ignored by the scene, and propagate to the view.
		Its common to open a PySide.QtGui.QMenu in response to receiving a context menu event
		Example:
		The default implementation ignores the event.
		"""
		res = super(QGraphicsItem,self).contextMenuEvent(event)
		return res
	#----------------------------------------------------------------------
	def data(self,key):
		"""
		data(key)
			key=QtCore.int

		Returns this items custom data for the key key as a PySide.QtCore.QVariant .
		Custom item data is useful for storing arbitrary properties in any item
		Example:
		Qt does not use this feature for storing data; it is provided solely for the convenience of the user.
		"""
		res = super(QGraphicsItem,self).data(key)
		return res
	#----------------------------------------------------------------------
	def deviceTransform(self,viewportTransform):
		"""
		deviceTransform(viewportTransform)
			viewportTransform=QtGui.QTransform

		Returns this items device transformation matrix, using viewportTransform to map from scene to device coordinates
		This matrix can be used to map coordinates and geometrical shapes from this items local coordinate system to the viewports (or any devices) coordinate system
		To map coordinates from the viewport, you must first invert the returned matrix.
		Example:
		This function is the same as combining this items scene transform with the views viewport transform, but it also understands the ItemIgnoresTransformations flag
		The device transform can be used to do accurate coordinate mapping (and collision detection) for untransformable items.
		"""
		res = super(QGraphicsItem,self).deviceTransform(viewportTransform)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented to receive drag enter events for this item
		Drag enter events are generated as the cursor enters the items area.
		By accepting the event, (i.e., by calling QEvent.accept() ,) the item will accept drop events, in addition to receiving drag move and drag leave
		Otherwise, the event will be ignored and propagate to the item beneath
		If the event is accepted, the item will receive a drag move event before control goes back to the event loop.
		A common implementation of dragEnterEvent accepts or ignores event depending on the associated mime data in event
		Example:
		Items do not receive drag and drop events by default; to enable this feature, call setAcceptDrops(true) .
		The default implementation does nothing.
		"""
		res = super(QGraphicsItem,self).dragEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented to receive drag leave events for this item
		Drag leave events are generated as the cursor leaves the items area
		Most often you will not need to reimplement this function, but it can be useful for resetting state in your item (e.g., highlighting).
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		Items do not receive drag and drop events by default; to enable this feature, call setAcceptDrops(true) .
		The default implementation does nothing.
		"""
		res = super(QGraphicsItem,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented to receive drag move events for this item
		Drag move events are generated as the cursor moves around inside the items area
		Most often you will not need to reimplement this function; it is used to indicate that only parts of the item can accept drops.
		Calling QEvent.ignore() or QEvent.accept() on event toggles whether or not the item will accept drops at the position from the event
		By default, event is accepted, indicating that the item allows drops at the specified position.
		Items do not receive drag and drop events by default; to enable this feature, call setAcceptDrops(true) .
		The default implementation does nothing.
		"""
		res = super(QGraphicsItem,self).dragMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented to receive drop events for this item
		Items can only receive drop events if the last drag move event was accepted.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		Items do not receive drag and drop events by default; to enable this feature, call setAcceptDrops(true) .
		The default implementation does nothing.
		"""
		res = super(QGraphicsItem,self).dropEvent(event)
		return res
	#----------------------------------------------------------------------
	def ensureVisible(self,*args,**kwargs):
		"""
		ensureVisible(rect=None,xmargin=None,ymargin=None)
			rect=QtCore.QRectF
			xmargin=QtCore.int
			ymargin=QtCore.int

		ensureVisible(x,y,w,h,xmargin=None,ymargin=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			xmargin=QtCore.int
			ymargin=QtCore.int

		If this item is part of a scene that is viewed by a PySide.QtGui.QGraphicsView , this convenience function will attempt to scroll the view to ensure that rect is visible inside the views viewport
		If rect is a null rect (the default), PySide.QtGui.QGraphicsItem will default to the items bounding rect
		xmargin and ymargin are the number of pixels the view should use for margins.
		If the specified rect cannot be reached, the contents are scrolled to the nearest valid position.
		If this item is not viewed by a PySide.QtGui.QGraphicsView , this function does nothing.
		"""
		res = super(QGraphicsItem,self).ensureVisible(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def extension(self,variant):
		"""
		extension(variant)
			variant=object

		Note: This is provided as a hook to avoid future problems related to adding virtual functions.
		"""
		res = super(QGraphicsItem,self).extension(variant)
		return res
	#----------------------------------------------------------------------
	def focusInEvent(self,event):
		"""
		focusInEvent(event)
			event=QtGui.QFocusEvent

		This event handler, for event event , can be reimplemented to receive focus in events for this item
		The default implementation calls PySide.QtGui.QGraphicsItem.ensureVisible() .
		"""
		res = super(QGraphicsItem,self).focusInEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusOutEvent(self,event):
		"""
		focusOutEvent(event)
			event=QtGui.QFocusEvent

		This event handler, for event event , can be reimplemented to receive focus out events for this item
		The default implementation does nothing.
		"""
		res = super(QGraphicsItem,self).focusOutEvent(event)
		return res
	#----------------------------------------------------------------------
	def hoverEnterEvent(self,event):
		"""
		hoverEnterEvent(event)
			event=QtGui.QGraphicsSceneHoverEvent

		This event handler, for event event , can be reimplemented to receive hover enter events for this item
		The default implementation calls PySide.QtGui.QGraphicsItem.update() ; otherwise it does nothing.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		"""
		res = super(QGraphicsItem,self).hoverEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def hoverLeaveEvent(self,event):
		"""
		hoverLeaveEvent(event)
			event=QtGui.QGraphicsSceneHoverEvent

		This event handler, for event event , can be reimplemented to receive hover leave events for this item
		The default implementation calls PySide.QtGui.QGraphicsItem.update() ; otherwise it does nothing.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		"""
		res = super(QGraphicsItem,self).hoverLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def hoverMoveEvent(self,event):
		"""
		hoverMoveEvent(event)
			event=QtGui.QGraphicsSceneHoverEvent

		This event handler, for event event , can be reimplemented to receive hover move events for this item
		The default implementation does nothing.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		"""
		res = super(QGraphicsItem,self).hoverMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodEvent(self,event):
		"""
		inputMethodEvent(event)
			event=QtGui.QInputMethodEvent

		This event handler, for event event , can be reimplemented to receive input method events for this item
		The default implementation ignores the event.
		"""
		res = super(QGraphicsItem,self).inputMethodEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodQuery(self,query):
		"""
		inputMethodQuery(query)
			query=QtCore.Qt.InputMethodQuery


		"""
		res = super(QGraphicsItem,self).inputMethodQuery(query)
		return res
	#----------------------------------------------------------------------
	def installSceneEventFilter(self,filterItem):
		"""
		installSceneEventFilter(filterItem)
			filterItem=QtGui.QGraphicsItem

		Installs an event filter for this item on filterItem , causing all events for this item to first pass through filterItem s PySide.QtGui.QGraphicsItem.sceneEventFilter() function.
		To filter another items events, install this item as an event filter for the other item
		Example:
		An item can only filter events for other items in the same scene
		Also, an item cannot filter its own events; instead, you can reimplement PySide.QtGui.QGraphicsItem.sceneEvent() directly.
		Items must belong to a scene for scene event filters to be installed and used.
		"""
		res = super(QGraphicsItem,self).installSceneEventFilter(filterItem)
		return res
	#----------------------------------------------------------------------
	def isAncestorOf(self,child):
		"""
		isAncestorOf(child)
			child=QtGui.QGraphicsItem

		Returns true if this item is an ancestor of child (i.e., if this item is child s parent, or one of child s parents ancestors).
		"""
		res = super(QGraphicsItem,self).isAncestorOf(child)

		return res
	#----------------------------------------------------------------------
	def isObscured(self,*args,**kwargs):
		"""
		isObscured(rect)
			rect=QtCore.QRectF

		isObscured(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		This is an overloaded function.
		Returns true if rect is completely obscured by the opaque shape of any of colliding items above it (i.e., with a higher Z value than this item).
		Unlike the default PySide.QtGui.QGraphicsItem.isObscured() function, this function does not call PySide.QtGui.QGraphicsItem.isObscuredBy() .
		"""
		res = super(QGraphicsItem,self).isObscured(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def isObscuredBy(self,item):
		"""
		isObscuredBy(item)
			item=QtGui.QGraphicsItem

		Returns true if this items bounding rect is completely obscured by the opaque shape of item .
		The base implementation maps item s PySide.QtGui.QGraphicsItem.opaqueArea() to this items coordinate system, and then checks if this items PySide.QtGui.QGraphicsItem.boundingRect() is fully contained within the mapped shape.
		You can reimplement this function to provide a custom algorithm for determining whether this item is obscured by item .
		"""
		res = super(QGraphicsItem,self).isObscuredBy(item)

		return res
	#----------------------------------------------------------------------
	def isVisibleTo(self,parent):
		"""
		isVisibleTo(parent)
			parent=QtGui.QGraphicsItem

		Returns true if the item is visible to parent ; otherwise, false is returned
		parent can be 0, in which case this function will return whether the item is visible to the scene or not.
		An item may not be visible to its ancestors even if PySide.QtGui.QGraphicsItem.isVisible() is true
		If any ancestor is hidden, the item itself will be implicitly hidden, in which case this function will return false.
		"""
		res = super(QGraphicsItem,self).isVisibleTo(parent)

		return res
	#----------------------------------------------------------------------
	def itemChange(self,change,value):
		"""
		itemChange(change,value)
			change=QtGui.QGraphicsItem.GraphicsItemChange
			value=object

		This virtual function is called by PySide.QtGui.QGraphicsItem to notify custom items that some part of the items state changes
		By reimplementing this function, your can react to a change, and in some cases, (depending on change ,) adjustments can be made.
		change is the parameter of the item that is changing
		value is the new value; the type of the value depends on change .
		Example:
		The default implementation does nothing, and returns value .
		Note: Certain PySide.QtGui.QGraphicsItem functions cannot be called in a reimplementation of this function; see the QGraphicsItem.GraphicsItemChange documentation for details.
		"""
		res = super(QGraphicsItem,self).itemChange(change,value)
		return res
	#----------------------------------------------------------------------
	def itemTransform(self,other,ok=None):
		"""
		itemTransform(other,ok=None)
			other=QtGui.QGraphicsItem
			ok=QtCore.bool

		Returns a PySide.QtGui.QTransform that maps coordinates from this item to other

		If ok is not null, and if there is no such transform,
		the boolean pointed to by ok will be set to false;
		otherwise it will be set to true.

		This transform provides an alternative to the PySide.QtGui.QGraphicsItem.mapToItem()
		or PySide.QtGui.QGraphicsItem.mapFromItem() functions
		by returning the appropriate transform so that you can map shapes and coordinates yourself

		It also helps you write more efficient code when repeatedly mapping between the same two items.
		"""
		res = super(QGraphicsItem,self).itemTransform(other,ok)
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def keyPressEvent(self,event):
		"""
		keyPressEvent(event)
			event=QtGui.QKeyEvent

		This event handler, for event event , can be reimplemented to receive key press events for this item
		The default implementation ignores the event
		If you reimplement this handler, the event will by default be accepted.
		Note that key events are only received for items that set the ItemIsFocusable flag, and that have keyboard input focus.
		"""
		res = super(QGraphicsItem,self).keyPressEvent(event)
		return res
	#----------------------------------------------------------------------
	def keyReleaseEvent(self,event):
		"""
		keyReleaseEvent(event)
			event=QtGui.QKeyEvent

		This event handler, for event event , can be reimplemented to receive key release events for this item
		The default implementation ignores the event
		If you reimplement this handler, the event will by default be accepted.
		Note that key events are only received for items that set the ItemIsFocusable flag, and that have keyboard input focus.
		"""
		res = super(QGraphicsItem,self).keyReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def mapFromItem(self,*args,**kwargs):
		"""
		mapFromItem(item,x,y)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal

		mapFromItem(item,rect)
			item=QtGui.QGraphicsItem
			rect=QtCore.QRectF

		mapFromItem(item,x,y,w,h)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapFromItem(item,path)
			item=QtGui.QGraphicsItem
			path=QtGui.QPainterPath

		mapFromItem(item,polygon)
			item=QtGui.QGraphicsItem
			polygon=QtGui.QPolygonF

		mapFromItem(item,point)
			item=QtGui.QGraphicsItem
			point=QtCore.QPointF

		This is an overloaded function.
		This convenience function is equivalent to calling mapFromItem(item , PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsItem,self).mapFromItem(*args,**kwargs)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def mapFromParent(self,*args,**kwargs):
		"""
		mapFromParent(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapFromParent(rect)
			rect=QtCore.QRectF

		mapFromParent(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		mapFromParent(path)
			path=QtGui.QPainterPath

		mapFromParent(polygon)
			polygon=QtGui.QPolygonF

		mapFromParent(point)
			point=QtCore.QPointF

		This convenience function is equivalent to calling mapFromItem( PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapFromParent(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def mapFromScene(self,*args,**kwargs):
		"""
		mapFromScene(rect)
			rect=QtCore.QRectF

		mapFromScene(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		mapFromScene(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapFromScene(path)
			path=QtGui.QPainterPath

		mapFromScene(point)
			point=QtCore.QPointF

		mapFromScene(polygon)
			polygon=QtGui.QPolygonF

		Maps the rectangle rect , which is in this items scenes coordinate system, to this items coordinate system, and returns the mapped rectangle as a polygon.
		"""
		res = super(QGraphicsItem,self).mapFromScene(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def mapRectFromItem(self,*args,**kwargs):
		"""
		mapRectFromItem(item,x,y,w,h)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapRectFromItem(item,rect)
			item=QtGui.QGraphicsItem
			rect=QtCore.QRectF

		This convenience function is equivalent to calling mapRectFromItem(item, PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapRectFromItem(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapRectFromParent(self,*args,**kwargs):
		"""
		mapRectFromParent(rect)
			rect=QtCore.QRectF

		mapRectFromParent(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		Maps the rectangle rect , which is in this items parents coordinate system, to this items coordinate system, and returns the mapped rectangle as a new rectangle (i.e., the bounding rectangle of the resulting polygon).
		"""
		res = super(QGraphicsItem,self).mapRectFromParent(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapRectFromScene(self,*args,**kwargs):
		"""
		mapRectFromScene(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapRectFromScene(rect)
			rect=QtCore.QRectF

		This convenience function is equivalent to calling mapRectFromScene( PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapRectFromScene(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapRectToItem(self,*args,**kwargs):
		"""
		mapRectToItem(item,x,y,w,h)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapRectToItem(item,rect)
			item=QtGui.QGraphicsItem
			rect=QtCore.QRectF

		This convenience function is equivalent to calling mapRectToItem(item, PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapRectToItem(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapRectToParent(self,*args,**kwargs):
		"""
		mapRectToParent(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapRectToParent(rect)
			rect=QtCore.QRectF

		This convenience function is equivalent to calling mapRectToParent( PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapRectToParent(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapRectToScene(self,*args,**kwargs):
		"""
		mapRectToScene(rect)
			rect=QtCore.QRectF

		mapRectToScene(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		Maps the rectangle rect , which is in this items coordinate system, to the scene coordinate system, and returns the mapped rectangle as a new rectangle (i.e., the bounding rectangle of the resulting polygon).
		"""
		res = super(QGraphicsItem,self).mapRectToScene(*args,**kwargs)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mapToItem(self,*args,**kwargs):
		"""
		mapToItem(item,x,y,w,h)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapToItem(item,rect)
			item=QtGui.QGraphicsItem
			rect=QtCore.QRectF

		mapToItem(item,x,y)
			item=QtGui.QGraphicsItem
			x=QtCore.qreal
			y=QtCore.qreal

		mapToItem(item,path)
			item=QtGui.QGraphicsItem
			path=QtGui.QPainterPath

		mapToItem(item,polygon)
			item=QtGui.QGraphicsItem
			polygon=QtGui.QPolygonF

		mapToItem(item,point)
			item=QtGui.QGraphicsItem
			point=QtCore.QPointF

		This convenience function is equivalent to calling mapToItem(item, PySide.QtCore.QRectF (x , y , w , h )).
		"""
		res = super(QGraphicsItem,self).mapToItem(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def mapToParent(self,*args,**kwargs):
		"""
		mapToParent(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		mapToParent(rect)
			rect=QtCore.QRectF

		mapToParent(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapToParent(path)
			path=QtGui.QPainterPath

		mapToParent(polygon)
			polygon=QtGui.QPolygonF

		mapToParent(point)
			point=QtCore.QPointF

		This is an overloaded function.
		This convenience function is equivalent to calling mapToParent( PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsItem,self).mapToParent(*args,**kwargs)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def mapToScene(self,*args,**kwargs):
		"""
		mapToScene(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		mapToScene(rect)
			rect=QtCore.QRectF

		mapToScene(polygon)
			polygon=QtGui.QPolygonF

		mapToScene(point)
			point=QtCore.QPointF

		mapToScene(path)
			path=QtGui.QPainterPath

		mapToScene(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		This is an overloaded function.
		This convenience function is equivalent to calling mapToScene( PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsItem,self).mapToScene(*args,**kwargs)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event event , can be reimplemented to receive mouse doubleclick events for this item.
		When doubleclicking an item, the item will first receive a mouse press event, followed by a release event (i.e., a click), then a doubleclick event, and finally a release event.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		The default implementation calls PySide.QtGui.QGraphicsItem.mousePressEvent()
		If you want to keep the base implementation when reimplementing this function, call QGraphicsItem.mouseDoubleClickEvent() in your reimplementation.
		Note that an item will not receive double click events if it is neither selectable nor movable (single mouse clicks are ignored in this case, and that stops the generation of double clicks).
		"""
		res = super(QGraphicsItem,self).mouseDoubleClickEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event event , can be reimplemented to receive mouse move events for this item
		If you do receive this event, you can be certain that this item also received a mouse press event, and that this item is the current mouse grabber.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		The default implementation handles basic item interaction, such as selection and moving
		If you want to keep the base implementation when reimplementing this function, call QGraphicsItem.mouseMoveEvent() in your reimplementation.
		Please note that PySide.QtGui.QGraphicsItem.mousePressEvent() decides which graphics item it is that receives mouse events
		See the PySide.QtGui.QGraphicsItem.mousePressEvent() description for details.
		"""
		res = super(QGraphicsItem,self).mouseMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event event , can be reimplemented to receive mouse press events for this item
		Mouse press events are only delivered to items that accept the mouse button that is pressed
		By default, an item accepts all mouse buttons, but you can change this by calling PySide.QtGui.QGraphicsItem.setAcceptedMouseButtons() .
		The mouse press event decides which item should become the mouse grabber (see QGraphicsScene.mouseGrabberItem() )
		If you do not reimplement this function, the press event will propagate to any topmost item beneath this item, and no other mouse events will be delivered to this item.
		If you do reimplement this function, event will by default be accepted (see QEvent.accept() ), and this item is then the mouse grabber
		This allows the item to receive future move, release and doubleclick events
		If you call QEvent.ignore() on event , this item will lose the mouse grab, and event will propagate to any topmost item beneath
		No further mouse events will be delivered to this item unless a new mouse press event is received.
		The default implementation handles basic item interaction, such as selection and moving
		If you want to keep the base implementation when reimplementing this function, call QGraphicsItem.mousePressEvent() in your reimplementation.
		The event is QEvent.ignore() d for items that are neither movable nor selectable .
		"""
		res = super(QGraphicsItem,self).mousePressEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event event , can be reimplemented to receive mouse release events for this item.
		Calling QEvent.ignore() or QEvent.accept() on event has no effect.
		The default implementation handles basic item interaction, such as selection and moving
		If you want to keep the base implementation when reimplementing this function, call QGraphicsItem.mouseReleaseEvent() in your reimplementation.
		Please note that PySide.QtGui.QGraphicsItem.mousePressEvent() decides which graphics item it is that receives mouse events
		See the PySide.QtGui.QGraphicsItem.mousePressEvent() description for details.
		"""
		res = super(QGraphicsItem,self).mouseReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def moveBy(self,dx,dy):
		"""
		moveBy(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Moves the item by dx points horizontally, and dy point vertically
		This function is equivalent to calling setPos( PySide.QtGui.QGraphicsItem.pos() + PySide.QtCore.QPointF (dx , dy )).
		"""
		res = super(QGraphicsItem,self).moveBy(dx,dy)
		return res
	#----------------------------------------------------------------------
	def paint(self,painter,option,widget=None):
		"""
		paint(painter,option,widget=None)
			painter=QtGui.QPainter
			option=QtGui.QStyleOptionGraphicsItem
			widget=QtGui.QWidget

		This function, which is usually called by PySide.QtGui.QGraphicsView , paints the contents of an item in local coordinates.
		Reimplement this function in a PySide.QtGui.QGraphicsItem subclass to provide the items painting implementation, using painter
		The option parameter provides style options for the item, such as its state, exposed area and its level-of-detail hints
		The widget argument is optional
		If provided, it points to the widget that is being painted on; otherwise, it is 0
		For cached painting, widget is always 0.
		The painters pen is 0-width by default, and its pen is initialized to the QPalette.Text brush from the paint devices palette
		The brush is initialized to QPalette.Window .
		Make sure to constrain all painting inside the boundaries of PySide.QtGui.QGraphicsItem.boundingRect() to avoid rendering artifacts (as PySide.QtGui.QGraphicsView does not clip the painter for you)
		In particular, when PySide.QtGui.QPainter renders the outline of a shape using an assigned PySide.QtGui.QPen , half of the outline will be drawn outside, and half inside, the shape youre rendering (e.g., with a pen width of 2 units, you must draw outlines 1 unit inside PySide.QtGui.QGraphicsItem.boundingRect() )
		PySide.QtGui.QGraphicsItem does not support use of cosmetic pens with a non-zero width.
		All painting is done in local coordinates.
		"""
		res = super(QGraphicsItem,self).paint(painter,option,widget)
		return res
	#----------------------------------------------------------------------
	def removeSceneEventFilter(self,filterItem):
		"""
		removeSceneEventFilter(filterItem)
			filterItem=QtGui.QGraphicsItem

		Removes an event filter on this item from filterItem .
		"""
		res = super(QGraphicsItem,self).removeSceneEventFilter(filterItem)
		return res
	#----------------------------------------------------------------------
	def rotate(self,angle):
		"""
		rotate(angle)
			angle=QtCore.qreal

		Use
		instead.
		Rotates the current item transformation angle degrees clockwise around its origin
		To translate around an arbitrary point (x, y), you need to combine translation and rotation with PySide.QtGui.QGraphicsItem.setTransform() .
		Example:
		"""
		res = super(QGraphicsItem,self).rotate(angle)
		return res
	#----------------------------------------------------------------------
	def sceneEvent(self,event):
		"""
		sceneEvent(event)
			event=QtCore.QEvent

		This virtual function receives events to this item
		Reimplement this function to intercept events before they are dispatched to the specialized event handlers PySide.QtGui.QGraphicsItem.contextMenuEvent() , PySide.QtGui.QGraphicsItem.focusInEvent() , PySide.QtGui.QGraphicsItem.focusOutEvent() , PySide.QtGui.QGraphicsItem.hoverEnterEvent() , PySide.QtGui.QGraphicsItem.hoverMoveEvent() , PySide.QtGui.QGraphicsItem.hoverLeaveEvent() , PySide.QtGui.QGraphicsItem.keyPressEvent() , PySide.QtGui.QGraphicsItem.keyReleaseEvent() , PySide.QtGui.QGraphicsItem.mousePressEvent() , PySide.QtGui.QGraphicsItem.mouseReleaseEvent() , PySide.QtGui.QGraphicsItem.mouseMoveEvent() , and PySide.QtGui.QGraphicsItem.mouseDoubleClickEvent() .
		Returns true if the event was recognized and handled; otherwise, (e.g., if the event type was not recognized,) false is returned.
		event is the intercepted event.
		"""
		res = super(QGraphicsItem,self).sceneEvent(event)

		return res
	#----------------------------------------------------------------------
	def sceneEventFilter(self,watched,event):
		"""
		sceneEventFilter(watched,event)
			watched=QtGui.QGraphicsItem
			event=QtCore.QEvent

		Filters events for the item watched
		event is the filtered event.
		Reimplementing this function in a subclass makes it possible for the item to be used as an event filter for other items, intercepting all the events send to those items before they are able to respond.
		Reimplementations must return true to prevent further processing of a given event, ensuring that it will not be delivered to the watched item, or return false to indicate that the event should be propagated further by the event system.
		"""
		res = super(QGraphicsItem,self).sceneEventFilter(watched,event)

		return res
	#----------------------------------------------------------------------
	def scroll(self,dx,dy,rect=None):
		"""
		scroll(dx,dy,rect=None)
			dx=QtCore.qreal
			dy=QtCore.qreal
			rect=QtCore.QRectF

		Scrolls the contents of rect by dx , dy
		If rect is a null rect (the default), the items bounding rect is scrolled.
		Scrolling provides a fast alternative to simply redrawing when the contents of the item (or parts of the item) are shifted vertically or horizontally
		Depending on the current transformation and the capabilities of the paint device (i.e., the viewport), this operation may consist of simply moving pixels from one location to another using memmove()
		In most cases this is faster than rerendering the entire area.
		After scrolling, the item will issue an update for the newly exposed areas
		If scrolling is not supported (e.g., you are rendering to an OpenGL viewport, which does not benefit from scroll optimizations), this function is equivalent to calling update(rect ).
		"""
		res = super(QGraphicsItem,self).scroll(dx,dy,rect)
		return res
	#----------------------------------------------------------------------
	def setAcceptDrops(self,on):
		"""
		setAcceptDrops(on)
			on=QtCore.bool

		If on is true, this item will accept drag and drop events; otherwise, it is transparent for drag and drop events
		By default, items do not accept drag and drop events.
		"""
		res = super(QGraphicsItem,self).setAcceptDrops(on)
		return res
	#----------------------------------------------------------------------
	def setAcceptHoverEvents(self,enabled):
		"""
		setAcceptHoverEvents(enabled)
			enabled=QtCore.bool

		If enabled is true, this item will accept hover events; otherwise, it will ignore them
		By default, items do not accept hover events.
		Hover events are delivered when there is no current mouse grabber item
		They are sent when the mouse cursor enters an item, when it moves around inside the item, and when the cursor leaves an item
		Hover events are commonly used to highlight an item when its entered, and for tracking the mouse cursor as it hovers over the item (equivalent to QWidget.mouseTracking ).
		Parent items receive hover enter events before their children, and leave events after their children
		The parent does not receive a hover leave event if the cursor enters a child, though; the parent stays hovered until the cursor leaves its area, including its childrens areas.
		If a parent item handles child events, it will receive hover move, drag move, and drop events as the cursor passes through its children, but it does not receive hover enter and hover leave, nor drag enter and drag leave events on behalf of its children.
		A PySide.QtGui.QGraphicsWidget with window decorations will accept hover events regardless of the value of PySide.QtGui.QGraphicsItem.acceptHoverEvents() .
		"""
		res = super(QGraphicsItem,self).setAcceptHoverEvents(enabled)
		return res
	#----------------------------------------------------------------------
	def setAcceptTouchEvents(self,enabled):
		"""
		setAcceptTouchEvents(enabled)
			enabled=QtCore.bool

		If enabled is true, this item will accept touch events ; otherwise, it will ignore them
		By default, items do not accept touch events.
		"""
		res = super(QGraphicsItem,self).setAcceptTouchEvents(enabled)
		return res
	#----------------------------------------------------------------------
	def setAcceptedMouseButtons(self,buttons):
		"""
		setAcceptedMouseButtons(buttons)
			buttons=QtCore.Qt.MouseButtons


		"""
		res = super(QGraphicsItem,self).setAcceptedMouseButtons(buttons)
		return res
	#----------------------------------------------------------------------
	def setAcceptsHoverEvents(self,enabled):
		"""
		setAcceptsHoverEvents(enabled)
			enabled=QtCore.bool

		Use setAcceptHoverEvents(enabled ) instead.
		"""
		res = super(QGraphicsItem,self).setAcceptsHoverEvents(enabled)
		return res
	#----------------------------------------------------------------------
	def setActive(self,active):
		"""
		setActive(active)
			active=QtCore.bool

		If active is true, and the scene is active, this items panel will be activated
		Otherwise, the panel is deactivated.
		If the item is not part of an active scene, active will decide what happens to the panel when the scene becomes active or the item is added to the scene
		If true, the items panel will be activated when the item is either added to the scene or the scene is activated
		Otherwise, the item will stay inactive independent of the scenes activated state.
		"""
		res = super(QGraphicsItem,self).setActive(active)
		return res
	#----------------------------------------------------------------------
	def setBoundingRegionGranularity(self,granularity):
		"""
		setBoundingRegionGranularity(granularity)
			granularity=QtCore.qreal

		Sets the bounding region granularity to granularity ; a value between and including 0 and 1
		The default value is 0 (i.e., the lowest granularity, where the bounding region corresponds to the items bounding rectangle).
		The granularity is used by PySide.QtGui.QGraphicsItem.boundingRegion() to calculate how fine the bounding region of the item should be
		The highest achievable granularity is 1, where PySide.QtGui.QGraphicsItem.boundingRegion() will return the finest outline possible for the respective device (e.g., for a PySide.QtGui.QGraphicsView viewport, this gives you a pixel-perfect bounding region)
		The lowest possible granularity is 0
		The value of granularity describes the ratio between device resolution and the resolution of the bounding region (e.g., a value of 0.25 will provide a region where each chunk corresponds to 4x4 device units / pixels).
		"""
		res = super(QGraphicsItem,self).setBoundingRegionGranularity(granularity)
		return res
	#----------------------------------------------------------------------
	def setCacheMode(self,mode,cacheSize=None):
		"""
		setCacheMode(mode,cacheSize=None)
			mode=QtGui.QGraphicsItem.CacheMode
			cacheSize=QtCore.QSize

		Sets the items cache mode to mode .
		The optional logicalCacheSize argument is used only by ItemCoordinateCache mode, and describes the resolution of the cache buffer; if logicalCacheSize is (100, 100), PySide.QtGui.QGraphicsItem will fit the item into 100x100 pixels in graphics memory, regardless of the logical size of the item itself
		By default PySide.QtGui.QGraphicsItem uses the size of PySide.QtGui.QGraphicsItem.boundingRect()
		For all other cache modes than ItemCoordinateCache , logicalCacheSize is ignored.
		Caching can speed up rendering if your item spends a significant time redrawing itself
		In some cases the cache can also slow down rendering, in particular when the item spends less time redrawing than PySide.QtGui.QGraphicsItem spends redrawing from the cache
		When enabled, the items PySide.QtGui.QGraphicsItem.paint() function will be called only once for each call to PySide.QtGui.QGraphicsItem.update() ; for any subsequent repaint requests, the Graphics View framework will redraw from the cache
		This approach works particularly well with PySide.QtOpenGL.QGLWidget , which stores all the cache as OpenGL textures.
		Be aware that PySide.QtGui.QPixmapCache s cache limit may need to be changed to obtain optimal performance.
		You can read more about the different cache modes in the QGraphicsItem.CacheMode documentation.
		"""
		res = super(QGraphicsItem,self).setCacheMode(mode,cacheSize)
		return res
	#----------------------------------------------------------------------
	def setCursor(self,cursor):
		"""
		setCursor(cursor)
			cursor=QtGui.QCursor

		Sets the current cursor shape for the item to cursor
		The mouse cursor will assume this shape when its over this item
		See the list of predefined cursor objects for a range of useful shapes.
		An editor item might want to use an I-beam cursor:
		If no cursor has been set, the cursor of the item beneath is used.
		"""
		res = super(QGraphicsItem,self).setCursor(cursor)
		return res
	#----------------------------------------------------------------------
	def setData(self,key,value):
		"""
		setData(key,value)
			key=QtCore.int
			value=object

		Sets this items custom data for the key key to value .
		Custom item data is useful for storing arbitrary properties for any item
		Qt does not use this feature for storing data; it is provided solely for the convenience of the user.
		"""
		res = super(QGraphicsItem,self).setData(key,value)
		return res
	#----------------------------------------------------------------------
	def setEnabled(self,enabled):
		"""
		setEnabled(enabled)
			enabled=QtCore.bool

		If enabled is true, the item is enabled; otherwise, it is disabled.
		Disabled items are visible, but they do not receive any events, and cannot take focus nor be selected
		Mouse events are discarded; they are not propagated unless the item is also invisible, or if it does not accept mouse events (see PySide.QtGui.QGraphicsItem.acceptedMouseButtons() )
		A disabled item cannot become the mouse grabber, and as a result of this, an item loses the grab if it becomes disabled when grabbing the mouse, just like it loses focus if it had focus when it was disabled.
		Disabled items are traditionally drawn using grayed-out colors (see QPalette.Disabled ).
		If you disable a parent item, all its children will also be disabled
		If you enable a parent item, all children will be enabled, unless they have been explicitly disabled (i.e., if you call setEnabled(false) on a child, it will not be reenabled if its parent is disabled, and then enabled again).
		Items are enabled by default.
		"""
		res = super(QGraphicsItem,self).setEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setFiltersChildEvents(self,enabled):
		"""
		setFiltersChildEvents(enabled)
			enabled=QtCore.bool

		If enabled is true, this item is set to filter all events for all its children (i.e., all events intented for any of its children are instead sent to this item); otherwise, if enabled is false, this item will only handle its own events
		The default value is false.
		"""
		res = super(QGraphicsItem,self).setFiltersChildEvents(enabled)
		return res
	#----------------------------------------------------------------------
	def setFlag(self,flag,enabled=None):
		"""
		setFlag(flag,enabled=None)
			flag=QtGui.QGraphicsItem.GraphicsItemFlag
			enabled=QtCore.bool

		If enabled is true, the item flag flag is enabled; otherwise, it is disabled.
		"""
		res = super(QGraphicsItem,self).setFlag(flag,enabled)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtGui.QGraphicsItem.GraphicsItemFlags


		"""
		res = super(QGraphicsItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFocus(self,focusReason=None):
		"""
		setFocus(focusReason=None)
			focusReason=QtCore.Qt.FocusReason


		"""
		res = super(QGraphicsItem,self).setFocus(focusReason)
		return res
	#----------------------------------------------------------------------
	def setFocusProxy(self,item):
		"""
		setFocusProxy(item)
			item=QtGui.QGraphicsItem

		Sets the items focus proxy to item .
		If an item has a focus proxy, the focus proxy will receive input focus when the item gains input focus
		The item itself will still have focus (i.e., PySide.QtGui.QGraphicsItem.hasFocus() will return true), but only the focus proxy will receive the keyboard input.
		A focus proxy can itself have a focus proxy, and so on
		In such case, keyboard input will be handled by the outermost focus proxy.
		The focus proxy item must belong to the same scene as this item.
		"""
		res = super(QGraphicsItem,self).setFocusProxy(item)
		return res
	#----------------------------------------------------------------------
	def setGraphicsEffect(self,effect):
		"""
		setGraphicsEffect(effect)
			effect=QtGui.QGraphicsEffect

		Sets effect as the items effect
		If there already is an effect installed on this item, PySide.QtGui.QGraphicsItem will delete the existing effect before installing the new effect .
		If effect is the installed on a different item, PySide.QtGui.QGraphicsItem.setGraphicsEffect() will remove the effect from the item and install it on this item.
		PySide.QtGui.QGraphicsItem takes ownership of effect .
		"""
		res = super(QGraphicsItem,self).setGraphicsEffect(effect)
		return res
	#----------------------------------------------------------------------
	def setGroup(self,group):
		"""
		setGroup(group)
			group=QtGui.QGraphicsItemGroup

		Adds this item to the item group group
		If group is 0, this item is removed from any current group and added as a child of the previous groups parent.
		"""
		res = super(QGraphicsItem,self).setGroup(group)
		return res
	#----------------------------------------------------------------------
	def setHandlesChildEvents(self,enabled):
		"""
		setHandlesChildEvents(enabled)
			enabled=QtCore.bool

		If enabled is true, this item is set to handle all events for all its children (i.e., all events intented for any of its children are instead sent to this item); otherwise, if enabled is false, this item will only handle its own events
		The default value is false.
		This property is useful for item groups; it allows one item to handle events on behalf of its children, as opposed to its children handling their events individually.
		If a child item accepts hover events, its parent will receive hover move events as the cursor passes through the child, but it does not receive hover enter and hover leave events on behalf of its child.
		"""
		res = super(QGraphicsItem,self).setHandlesChildEvents(enabled)
		return res
	#----------------------------------------------------------------------
	def setInputMethodHints(self,hints):
		"""
		setInputMethodHints(hints)
			hints=QtCore.Qt.InputMethodHints


		"""
		res = super(QGraphicsItem,self).setInputMethodHints(hints)
		return res
	#----------------------------------------------------------------------
	def setOpacity(self,opacity):
		"""
		setOpacity(opacity)
			opacity=QtCore.qreal

		Sets this items local opacity , between 0.0 (transparent) and 1.0 (opaque)
		The items local opacity is combined with parent and ancestor opacities into the PySide.QtGui.QGraphicsItem.effectiveOpacity() .
		By default, opacity propagates from parent to child, so if a parents opacity is 0.5 and the child is also 0.5, the childs effective opacity will be 0.25.
		The opacity property decides the state of the painter passed to the PySide.QtGui.QGraphicsItem.paint() function
		If the item is cached, i.e., ItemCoordinateCache or DeviceCoordinateCache , the effective property will be applied to the items cache as it is rendered.
		There are two item flags that affect how the items opacity is combined with the parent: ItemIgnoresParentOpacity and ItemDoesntPropagateOpacityToChildren .
		"""
		res = super(QGraphicsItem,self).setOpacity(opacity)
		return res
	#----------------------------------------------------------------------
	def setPanelModality(self,panelModality):
		"""
		setPanelModality(panelModality)
			panelModality=QtGui.QGraphicsItem.PanelModality

		Sets the modality for this item to panelModality .
		Changing the modality of a visible item takes effect immediately.
		"""
		res = super(QGraphicsItem,self).setPanelModality(panelModality)
		return res
	#----------------------------------------------------------------------
	def setParentItem(self,parent):
		"""
		setParentItem(parent)
			parent=QtGui.QGraphicsItem

		Sets this items parent item to newParent
		If this item already has a parent, it is first removed from the previous parent
		If newParent is 0, this item will become a top-level item.
		Note that this implicitly adds this graphics item to the scene of the parent
		You should not add the item to the scene yourself.
		Calling this function on an item that is an ancestor of newParent have undefined behaviour.
		"""
		res = super(QGraphicsItem,self).setParentItem(parent)
		return res
	#----------------------------------------------------------------------
	def setPos(self,*args,**kwargs):
		"""
		setPos(pos)
			pos=QtCore.QPointF

		setPos(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		Sets the position of the item to pos , which is in parent coordinates
		For items with no parent, pos is in scene coordinates.
		The position of the item describes its origin (local coordinate (0, 0)) in parent coordinates.
		"""
		res = super(QGraphicsItem,self).setPos(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setRotation(self,angle):
		"""
		setRotation(angle)
			angle=QtCore.qreal

		Sets the clockwise rotation angle , in degrees, around the Z axis
		The default value is 0 (i.e., the item is not rotated)
		Assigning a negative value will rotate the item counter-clockwise
		Normally the rotation angle is in the range (-360, 360), but its also possible to assign values outside of this range (e.g., a rotation of 370 degrees is the same as a rotation of 10 degrees).
		The item is rotated around its transform origin point, which by default is (0, 0)
		You can select a different transformation origin by calling PySide.QtGui.QGraphicsItem.setTransformOriginPoint() .
		The rotation is combined with the items PySide.QtGui.QGraphicsItem.scale() , PySide.QtGui.QGraphicsItem.transform() and PySide.QtGui.QGraphicsItem.transformations() to map the items coordinate system to the parent item.
		"""
		res = super(QGraphicsItem,self).setRotation(angle)
		return res
	#----------------------------------------------------------------------
	def setScale(self,scale):
		"""
		setScale(scale)
			scale=QtCore.qreal

		Sets the scale factor of the item
		The default scale factor is 1.0 (i.e., the item is not scaled)
		A scale factor of 0.0 will collapse the item to a single point
		If you provide a negative scale factor, the item will be flipped and mirrored (i.e., rotated 180 degrees).
		The item is scaled around its transform origin point, which by default is (0, 0)
		You can select a different transformation origin by calling PySide.QtGui.QGraphicsItem.setTransformOriginPoint() .
		The scale is combined with the items PySide.QtGui.QGraphicsItem.rotation() , PySide.QtGui.QGraphicsItem.transform() and PySide.QtGui.QGraphicsItem.transformations() to map the items coordinate system to the parent item.
		"""
		res = super(QGraphicsItem,self).setScale(scale)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,selected):
		"""
		setSelected(selected)
			selected=QtCore.bool

		If selected is true and this item is selectable, this item is selected; otherwise, it is unselected.
		If the item is in a group, the whole groups selected state is toggled by this function
		If the group is selected, all items in the group are also selected, and if the group is not selected, no item in the group is selected.
		Only visible, enabled, selectable items can be selected
		If selected is true and this item is either invisible or disabled or unselectable, this function does nothing.
		By default, items cannot be selected
		To enable selection, set the ItemIsSelectable flag.
		This function is provided for convenience, allowing individual toggling of the selected state of an item
		However, a more common way of selecting items is to call QGraphicsScene.setSelectionArea() , which will call this function for all visible, enabled, and selectable items within a specified area on the scene.
		"""
		res = super(QGraphicsItem,self).setSelected(selected)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,toolTip):
		"""
		setToolTip(toolTip)
			toolTip=unicode

		Sets the items tool tip to toolTip
		If toolTip is empty, the items tool tip is cleared.
		"""
		res = super(QGraphicsItem,self).setToolTip(toolTip)
		return res
	#----------------------------------------------------------------------
	def setTransform(self,matrix,combine=None):
		"""
		setTransform(matrix,combine=None)
			matrix=QtGui.QTransform
			combine=QtCore.bool

		Sets the items current transformation matrix to matrix .
		If combine is true, then matrix is combined with the current matrix; otherwise, matrixreplaces the current matrix
		combine is false by default.
		To simplify interation with items using a transformed view, PySide.QtGui.QGraphicsItem provides mapTo..
		and mapFrom..
		functions that can translate between items and the scenes coordinates
		For example, you can call PySide.QtGui.QGraphicsItem.mapToScene() to map an item coordiate to a scene coordinate, or PySide.QtGui.QGraphicsItem.mapFromScene() to map from scene coordinates to item coordinates.
		The transformation matrix is combined with the items PySide.QtGui.QGraphicsItem.rotation() , PySide.QtGui.QGraphicsItem.scale() and PySide.QtGui.QGraphicsItem.transformations() into a combined transformation that maps the items coordinate system to its parent.
		"""
		res = super(QGraphicsItem,self).setTransform(matrix,combine)
		return res
	#----------------------------------------------------------------------
	def setTransformOriginPoint(self,*args,**kwargs):
		"""
		setTransformOriginPoint(origin)
			origin=QtCore.QPointF

		setTransformOriginPoint(ax,ay)
			ax=QtCore.qreal
			ay=QtCore.qreal

		Sets the origin point for the transformation in item coordinates.
		"""
		res = super(QGraphicsItem,self).setTransformOriginPoint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setTransformations(self,transformations):
		"""
		setTransformations(transformations)
			transformations=unKnown


		"""
		res = super(QGraphicsItem,self).setTransformations(transformations)
		return res
	#----------------------------------------------------------------------
	def setVisible(self,visible):
		"""
		setVisible(visible)
			visible=QtCore.bool

		If visible is true, the item is made visible
		Otherwise, the item is made invisible
		Invisible items are not painted, nor do they receive any events
		In particular, mouse events pass right through invisible items, and are delivered to any item that may be behind
		Invisible items are also unselectable, they cannot take input focus, and are not detected by PySide.QtGui.QGraphicsScene s item location functions.
		If an item becomes invisible while grabbing the mouse, (i.e., while it is receiving mouse events,) it will automatically lose the mouse grab, and the grab is not regained by making the item visible again; it must receive a new mouse press to regain the mouse grab.
		Similarly, an invisible item cannot have focus, so if the item has focus when it becomes invisible, it will lose focus, and the focus is not regained by simply making the item visible again.
		If you hide a parent item, all its children will also be hidden
		If you show a parent item, all children will be shown, unless they have been explicitly hidden (i.e., if you call setVisible(false) on a child, it will not be reshown even if its parent is hidden, and then shown again).
		Items are visible by default; it is unnecessary to call PySide.QtGui.QGraphicsItem.setVisible() on a new item.
		"""
		res = super(QGraphicsItem,self).setVisible(visible)
		return res
	#----------------------------------------------------------------------
	def setX(self,x):
		"""
		setX(x)
			x=QtCore.qreal

		Sets the x coordinate of the items position
		Equivalent to calling setPos(x, PySide.QtGui.QGraphicsItem.y() ).
		"""
		res = super(QGraphicsItem,self).setX(x)
		return res
	#----------------------------------------------------------------------
	def setY(self,y):
		"""
		setY(y)
			y=QtCore.qreal

		Sets the y coordinate of the items position
		Equivalent to calling setPos( PySide.QtGui.QGraphicsItem.x() , y).
		"""
		res = super(QGraphicsItem,self).setY(y)
		return res
	#----------------------------------------------------------------------
	def setZValue(self,z):
		"""
		setZValue(z)
			z=QtCore.qreal

		Sets the Z-value of the item to z
		The Z value decides the stacking order of sibling (neighboring) items
		A sibling item of high Z value will always be drawn on top of another sibling item with a lower Z value.
		If you restore the Z value, the items insertion order will decide its stacking order.
		The Z-value does not affect the items size in any way.
		The default Z-value is 0.
		"""
		res = super(QGraphicsItem,self).setZValue(z)
		return res
	#----------------------------------------------------------------------
	def shear(self,sh,sv):
		"""
		shear(sh,sv)
			sh=QtCore.qreal
			sv=QtCore.qreal

		Use
		instead.
		Shears the current item transformation by (sh , sv ).
		"""
		res = super(QGraphicsItem,self).shear(sh,sv)
		return res
	#----------------------------------------------------------------------
	def stackBefore(self,sibling):
		"""
		stackBefore(sibling)
			sibling=QtGui.QGraphicsItem

		Stacks this item before sibling , which must be a sibling item (i.e., the two items must share the same parent item, or must both be toplevel items)
		The sibling must have the same Z value as this item, otherwise calling this function will have no effect.
		By default, all sibling items are stacked by insertion order (i.e., the first item you add is drawn before the next item you add)
		If two items Z values are different, then the item with the highest Z value is drawn on top
		When the Z values are the same, the insertion order will decide the stacking order.
		"""
		res = super(QGraphicsItem,self).stackBefore(sibling)
		return res
	#----------------------------------------------------------------------
	def translate(self,dx,dy):
		"""
		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Use PySide.QtGui.QGraphicsItem.setPos() or PySide.QtGui.QGraphicsItem.setTransformOriginPoint() instead
		For identical behavior, use
		Translates the current item transformation by (dx , dy ).
		If all you want is to move an item, you should call PySide.QtGui.QGraphicsItem.moveBy() or PySide.QtGui.QGraphicsItem.setPos() instead; this function changes the items translation, which is conceptually separate from its position.
		"""
		res = super(QGraphicsItem,self).translate(dx,dy)
		return res
	#----------------------------------------------------------------------
	def update(self,*args,**kwargs):
		"""
		update(x,y,width,height)
			x=QtCore.qreal
			y=QtCore.qreal
			width=QtCore.qreal
			height=QtCore.qreal

		update(rect=None)
			rect=QtCore.QRectF

		This is an overloaded function.
		This convenience function is equivalent to calling update( PySide.QtCore.QRectF (x , y , width , height )).
		"""
		res = super(QGraphicsItem,self).update(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def wheelEvent(self,event):
		"""
		wheelEvent(event)
			event=QtGui.QGraphicsSceneWheelEvent

		This event handler, for event event , can be reimplemented to receive wheel events for this item
		If you reimplement this function, event will be accepted by default.
		If you ignore the event, (i.e., by calling QEvent.ignore() ,) it will propagate to any item beneath this item
		If no items accept the event, it will be ignored by the scene, and propagate to the view (e.g., the views vertical scroll bar).
		The default implementation ignores the event.
		"""
		res = super(QGraphicsItem,self).wheelEvent(event)
		return res

	Opacity                = property(opacity,setOpacity)
	Pos                    = property(pos,setPos)
	Rotation               = property(rotation,setRotation)
	Scale                  = property(scale,setScale)
	Tool_Tip               = property(toolTip,setToolTip)
	X                      = property(x,setX)
	Y                      = property(y,setY)
	Z                      = property(zValue,setZValue)
	Data                   = property(data,setData)
	Enabled                = property(isEnabled,setEnabled)
	Is_Obscured            = property(isObscured)
	Is_Panel               = property(isPanel)
	Is_Selected            = property(isSelected)
	Is_UnderMouse          = property(isUnderMouse)
	Is_Visible             = property(isVisible)
	Visablity              = property(isVisible,setVisible)
	Is_Widget              = property(isWidget)
	Is_Window              = property(isWindow)
	Opaque_Area            = property(opaqueArea)
	Panel                  = property(panel)
	Parent_Item            = property(parentItem,setParentItem)
	Parent_Widget          = property(parentWidget)
	Scene                  = property(scene)
	Scene_Bounding_Rect    = property(sceneBoundingRect)
	Scene_Pos              = property(scenePos)
	Scene_Transform        = property(sceneTransform)
	Shape                  = property(shape)
	Top_Level_Item         = property(topLevelItem)
	Top_Level_Widget       = property(topLevelWidget)
	Tranform_Matrix        = property(transform)
	Transform_Origin_Point = property(transformOriginPoint)
	Transformations        = property(transformations)
	Type                   = property(type)
	Accept_Hover_Events    = property(acceptHoverEvents, setAcceptHoverEvents)
	Accepts_Hover_Events   = property(acceptsHoverEvents, setAcceptsHoverEvents)
	Accept_Mouse_Buttons   = property(acceptedMouseButtons, setAcceptedMouseButtons)
	Accept_Drops           = property(acceptDrops, setAcceptDrops)