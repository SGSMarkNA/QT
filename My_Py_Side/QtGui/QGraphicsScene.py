from Qt_Tools import QtGui, QtCore
from ..QtCore.QObject import QObject
class QGraphicsScene(QtGui.QGraphicsScene, QObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsScene,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activePanel(self):
		"""
		Returns the current active panel, or 0 if no panel is currently active.
		"""
		res = super(QGraphicsScene,self).activePanel()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def activeWindow(self):
		"""
		Returns the current active window, or 0 if no window is currently active.
		"""
		res = super(QGraphicsScene,self).activeWindow()
		isinstance(res,QtGui.QGraphicsWidget)
		return res
	#----------------------------------------------------------------------
	def backgroundBrush(self):
		"""
		This property holds the background brush of the scene..
		Set this property to changes the scenes background to a different color, gradient or texture
		The default background brush is Qt.NoBrush
		The background is drawn before (behind) the items.
		Example:
		QGraphicsScene.render() calls PySide.QtGui.QGraphicsScene.drawBackground() to draw the scene background
		For more detailed control over how the background is drawn, you can reimplement PySide.QtGui.QGraphicsScene.drawBackground() in a subclass of PySide.QtGui.QGraphicsScene .
		"""
		res = super(QGraphicsScene,self).backgroundBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def bspTreeDepth(self):
		"""
		This property holds the depth of PySide.QtGui.QGraphicsScene s BSP index tree.
		This property has no effect when NoIndex is used.
		This value determines the depth of PySide.QtGui.QGraphicsScene s BSP tree
		The depth directly affects PySide.QtGui.QGraphicsScene s performance and memory usage; the latter growing exponentially with the depth of the tree
		With an optimal tree depth, PySide.QtGui.QGraphicsScene can instantly determine the locality of items, even for scenes with thousands or millions of items
		This also greatly improves rendering performance.
		By default, the value is 0, in which case Qt will guess a reasonable default depth based on the size, location and number of items in the scene
		If these parameters change frequently, however, you may experience slowdowns as PySide.QtGui.QGraphicsScene retunes the depth internally
		You can avoid potential slowdowns by fixating the tree depth through setting this property.
		The depth of the tree and the size of the scene rectangle decide the granularity of the scenes partitioning
		The size of each scene segment is determined by the following algorithm:
		The BSP tree has an optimal size when each segment contains between 0 and 10 items.
		"""
		res = super(QGraphicsScene,self).bspTreeDepth()

		return res
	#----------------------------------------------------------------------
	def clearFocus(self):
		"""
		Clears focus from the scene
		If any item has focus when this function is called, it will lose focus, and regain focus again once the scene regains focus.
		A scene that does not have focus ignores key events.
		"""
		res = super(QGraphicsScene,self).clearFocus()
		return res
	#----------------------------------------------------------------------
	def focusItem(self):
		"""
		When the scene is active, this functions returns the scenes current focus item, or 0 if no item currently has focus
		When the scene is inactive, this functions returns the item that will gain input focus when the scene becomes active.
		The focus item receives keyboard input when the scene receives a key event.
		"""
		res = super(QGraphicsScene,self).focusItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		This property holds the scenes default font.
		This property provides the scenes font
		The scene font defaults to, and resolves all its entries from, QApplication::font.
		If the scenes font changes, either directly through PySide.QtGui.QGraphicsScene.setFont() or indirectly when the application font changes, PySide.QtGui.QGraphicsScene first sends itself a FontChange event, and it then sends FontChange events to all top-level widget items in the scene
		These items respond by resolving their own fonts to the scene, and they then notify their children, who again notify their children, and so on, until all widget items have updated their fonts.
		Changing the scene font, (directly or indirectly through QApplication.setFont() ,) automatically schedules a redraw the entire scene.
		"""
		res = super(QGraphicsScene,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foregroundBrush(self):
		"""
		This property holds the foreground brush of the scene..
		Change this property to set the scenes foreground to a different color, gradient or texture.
		The foreground is drawn after (on top of) the items
		The default foreground brush is Qt.NoBrush ( i.e
		the foreground is not drawn).
		Example:
		QGraphicsScene.render() calls PySide.QtGui.QGraphicsScene.drawForeground() to draw the scene foreground
		For more detailed control over how the foreground is drawn, you can reimplement the PySide.QtGui.QGraphicsScene.drawForeground() function in a PySide.QtGui.QGraphicsScene subclass.
		"""
		res = super(QGraphicsScene,self).foregroundBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def hasFocus(self):
		"""
		Returns true if the scene has focus; otherwise returns false
		If the scene has focus, it will will forward key events from PySide.QtGui.QKeyEvent to any item that has focus.
		"""
		res = super(QGraphicsScene,self).hasFocus()

		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		This convenience function is equivalent to calling sceneRect().height() .
		"""
		res = super(QGraphicsScene,self).height()

		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if the scene is active (e.g., its viewed by at least one PySide.QtGui.QGraphicsView that is active); otherwise returns false.
		"""
		res = super(QGraphicsScene,self).isActive()

		return res
	#----------------------------------------------------------------------
	def isSortCacheEnabled(self):
		"""
		This property holds whether sort caching is enabled.
		Since Qt 4.6, this property has no effect.
		"""
		res = super(QGraphicsScene,self).isSortCacheEnabled()

		return res
	#----------------------------------------------------------------------
	def itemIndexMethod(self):
		"""
		This property holds the item indexing method..
		PySide.QtGui.QGraphicsScene applies an indexing algorithm to the scene, to speed up item discovery functions like PySide.QtGui.QGraphicsScene.items() and PySide.QtGui.QGraphicsScene.itemAt()
		Indexing is most efficient for static scenes (i.e., where items dont move around)
		For dynamic scenes, or scenes with many animated items, the index bookkeeping can outweight the fast lookup speeds.
		For the common case, the default index method BspTreeIndex works fine
		If your scene uses many animations and you are experiencing slowness, you can disable indexing by calling setItemIndexMethod(NoIndex) .
		"""
		res = super(QGraphicsScene,self).itemIndexMethod()
		isinstance(res,QtGui.QGraphicsScene.ItemIndexMethod)
		return res
	#----------------------------------------------------------------------
	def items(self):
		"""
		Returns a list of all items in the scene in descending stacking order.
		"""
		res = super(QGraphicsScene,self).items()
		return res
	#----------------------------------------------------------------------
	def itemsBoundingRect(self):
		"""
		Calculates and returns the bounding rect of all items on the scene
		This function works by iterating over all items, and because if this, it can be slow for large scenes.
		"""
		res = super(QGraphicsScene,self).itemsBoundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def mouseGrabberItem(self):
		"""
		Returns the current mouse grabber item, or 0 if no item is currently grabbing the mouse
		The mouse grabber item is the item that receives all mouse events sent to the scene.
		An item becomes a mouse grabber when it receives and accepts a mouse press event, and it stays the mouse grabber until either of the following events occur:
		If the item loses its mouse grab, the scene will ignore all mouse events until a new item grabs the mouse (i.e., until a new item receives a mouse press event).
		"""
		res = super(QGraphicsScene,self).mouseGrabberItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def palette(self):
		"""
		This property holds the scenes default palette.
		This property provides the scenes palette
		The scene palette defaults to, and resolves all its entries from, QApplication::palette.
		If the scenes palette changes, either directly through PySide.QtGui.QGraphicsScene.setPalette() or indirectly when the application palette changes, PySide.QtGui.QGraphicsScene first sends itself a PaletteChange event, and it then sends PaletteChange events to all top-level widget items in the scene
		These items respond by resolving their own palettes to the scene, and they then notify their children, who again notify their children, and so on, until all widget items have updated their palettes.
		Changing the scene palette, (directly or indirectly through QApplication.setPalette() ,) automatically schedules a redraw the entire scene.
		"""
		res = super(QGraphicsScene,self).palette()
		isinstance(res,QtGui.QPalette)
		return res
	#----------------------------------------------------------------------
	def sceneRect(self):
		"""
		This property holds the scene rectangle; the bounding rectangle of the scene.
		The scene rectangle defines the extent of the scene
		It is primarily used by PySide.QtGui.QGraphicsView to determine the views default scrollable area, and by PySide.QtGui.QGraphicsScene to manage item indexing.
		If unset, or if set to a null PySide.QtCore.QRectF , PySide.QtGui.QGraphicsScene.sceneRect() will return the largest bounding rect of all items on the scene since the scene was created (i.e., a rectangle that grows when items are added to or moved in the scene, but never shrinks).
		"""
		res = super(QGraphicsScene,self).sceneRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def selectedItems(self):
		"""
		Returns a list of all currently selected items
		The items are returned in no particular order.
		"""
		res = super(QGraphicsScene,self).selectedItems()
		return res
	#----------------------------------------------------------------------
	def selectionArea(self):
		"""
		Returns the selection area that was previously set with PySide.QtGui.QGraphicsScene.setSelectionArea() , or an empty PySide.QtGui.QPainterPath if no selection area has been set.
		"""
		res = super(QGraphicsScene,self).selectionArea()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def stickyFocus(self):
		"""
		This property holds whether clicking into the scene background will clear focus.
		In a PySide.QtGui.QGraphicsScene with PySide.QtGui.QGraphicsScene.stickyFocus() set to true, focus will remain unchanged when the user clicks into the scene background or on an item that does not accept focus
		Otherwise, focus will be cleared.
		By default, this property is false.
		Focus changes in response to a mouse press
		You can reimplement PySide.QtGui.QGraphicsScene.mousePressEvent() in a subclass of PySide.QtGui.QGraphicsScene to toggle this property based on where the user has clicked.
		"""
		res = super(QGraphicsScene,self).stickyFocus()

		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the scenes style, or the same as QApplication.style() if the scene has not been explicitly assigned a style.
		"""
		res = super(QGraphicsScene,self).style()
		isinstance(res,QtGui.QStyle)
		return res
	#----------------------------------------------------------------------
	def views(self):
		"""
		Returns a list of all the views that display this scene.
		"""
		res = super(QGraphicsScene,self).views()
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		This convenience function is equivalent to calling PySide.QtGui.QGraphicsScene.sceneRect()
		PySide.QtGui.QGraphicsScene.width() .
		"""
		res = super(QGraphicsScene,self).width()

		return res

	#----------------------------------------------------------------------
	def addEllipse(self,*args,**kwargs):
		"""
		addEllipse(rect,pen=None,brush=None)
			rect=QtCore.QRectF
			pen=QtGui.QPen
			brush=QtGui.QBrush

		addEllipse(x,y,w,h,pen=None,brush=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			pen=QtGui.QPen
			brush=QtGui.QBrush

		Creates and adds an ellipse item to the scene, and returns the item pointer
		The geometry of the ellipse is defined by rect , and its pen and brush are initialized to pen and brush .
		Note that the items geometry is provided in item coordinates, and its position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addEllipse(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsEllipseItem)
		return res
	#----------------------------------------------------------------------
	def addItem(self,item):
		"""
		addItem(item)
			item=QtGui.QGraphicsItem

		Adds or moves the item and all its childen to this scene
		This scene takes ownership of the item .
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		If the item is already in a different scene, it will first be removed from its old scene, and then added to this scene as a top-level.
		PySide.QtGui.QGraphicsScene will send ItemSceneChange notifications to item while it is added to the scene
		If item does not currently belong to a scene, only one notification is sent
		If it does belong to scene already (i.e., it is moved to this scene), PySide.QtGui.QGraphicsScene will send an addition notification as the item is removed from its previous scene.
		If the item is a panel, the scene is active, and there is no active panel in the scene, then the item will be activated.
		"""
		res = super(QGraphicsScene,self).addItem(item)
		return res
	#----------------------------------------------------------------------
	def addLine(self,*args,**kwargs):
		"""
		addLine(x1,y1,x2,y2,pen=None)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal
			pen=QtGui.QPen

		addLine(line,pen=None)
			line=QtCore.QLineF
			pen=QtGui.QPen

		This convenience function is equivalent to calling addLine( PySide.QtCore.QLineF (x1 , y1 , x2 , y2 ), pen ).
		"""
		res = super(QGraphicsScene,self).addLine(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsLineItem)
		return res
	#----------------------------------------------------------------------
	def addPath(self,path,pen=None,brush=None):
		"""
		addPath(path,pen=None,brush=None)
			path=QtGui.QPainterPath
			pen=QtGui.QPen
			brush=QtGui.QBrush

		Creates and adds a path item to the scene, and returns the item pointer
		The geometry of the path is defined by path , and its pen and brush are initialized to pen and brush .
		Note that the items geometry is provided in item coordinates, and its position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addPath(path,pen,brush)
		isinstance(res,QtGui.QGraphicsPathItem)
		return res
	#----------------------------------------------------------------------
	def addPixmap(self,pixmap):
		"""
		addPixmap(pixmap)
			pixmap=QtGui.QPixmap

		Creates and adds a pixmap item to the scene, and returns the item pointer
		The pixmap is defined by pixmap .
		Note that the items geometry is provided in item coordinates, and its position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addPixmap(pixmap)
		isinstance(res,QtGui.QGraphicsPixmapItem)
		return res
	#----------------------------------------------------------------------
	def addPolygon(self,polygon,pen=None,brush=None):
		"""
		addPolygon(polygon,pen=None,brush=None)
			polygon=QtGui.QPolygonF
			pen=QtGui.QPen
			brush=QtGui.QBrush

		Creates and adds a polygon item to the scene, and returns the item pointer
		The polygon is defined by polygon , and its pen and brush are initialized to pen and brush .
		Note that the items geometry is provided in item coordinates, and its position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addPolygon(polygon,pen,brush)
		isinstance(res,QtGui.QGraphicsPolygonItem)
		return res
	#----------------------------------------------------------------------
	def addRect(self,*args,**kwargs):
		"""
		addRect(x,y,w,h,pen=None,brush=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			pen=QtGui.QPen
			brush=QtGui.QBrush

		addRect(rect,pen=None,brush=None)
			rect=QtCore.QRectF
			pen=QtGui.QPen
			brush=QtGui.QBrush

		This convenience function is equivalent to calling addRect( PySide.QtCore.QRectF (x , y , w , h ), pen , brush ).
		"""
		res = super(QGraphicsScene,self).addRect(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsRectItem)
		return res
	#----------------------------------------------------------------------
	def addSimpleText(self,text,font=None):
		"""
		addSimpleText(text,font=None)
			text=unicode
			font=QtGui.QFont

		Creates and adds a PySide.QtGui.QGraphicsSimpleTextItem to the scene, and returns the item pointer
		The text string is initialized to text , and its font is initialized to font .
		The items position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addSimpleText(text,font)
		isinstance(res,QtGui.QGraphicsSimpleTextItem)
		return res
	#----------------------------------------------------------------------
	def addText(self,text,font=None):
		"""
		addText(text,font=None)
			text=unicode
			font=QtGui.QFont

		Creates and adds a text item to the scene, and returns the item pointer
		The text string is initialized to text , and its font is initialized to font .
		The items position is initialized to (0, 0).
		If the item is visible (i.e., QGraphicsItem.isVisible() returns true), PySide.QtGui.QGraphicsScene will emit PySide.QtGui.QGraphicsScene.changed() once control goes back to the event loop.
		"""
		res = super(QGraphicsScene,self).addText(text,font)
		isinstance(res,QtGui.QGraphicsTextItem)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,*args,**kwargs):
		"""
		addWidget(widget,wFlags=None)
			widget=QtGui.QWidget
			wFlags=QtCore.Qt.WindowFlags


		"""
		res = super(QGraphicsScene,self).addWidget(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsProxyWidget)
		return res
	#----------------------------------------------------------------------
	def collidingItems(self,item,mode=None):
		"""
		collidingItems(item,mode=None)
			item=QtGui.QGraphicsItem
			mode=QtCore.Qt.ItemSelectionMode


		"""
		res = super(QGraphicsScene,self).collidingItems(item,mode)
		return res
	#----------------------------------------------------------------------
	def contextMenuEvent(self,event):
		"""
		contextMenuEvent(event)
			event=QtGui.QGraphicsSceneContextMenuEvent

		This event handler, for event contextMenuEvent , can be reimplemented in a subclass to receive context menu events
		The default implementation forwards the event to the topmost item that accepts context menu events at the position of the event
		If no items accept context menu events at this position, the event is ignored.
		"""
		res = super(QGraphicsScene,self).contextMenuEvent(event)
		return res
	#----------------------------------------------------------------------
	def createItemGroup(self,items):
		"""
		createItemGroup(items)
			items=unKnown


		"""
		res = super(QGraphicsScene,self).createItemGroup(items)
		isinstance(res,QtGui.QGraphicsItemGroup)
		return res
	#----------------------------------------------------------------------
	def destroyItemGroup(self,group):
		"""
		destroyItemGroup(group)
			group=QtGui.QGraphicsItemGroup

		Reparents all items in group to group s parent item, then removes group from the scene, and finally deletes it
		The items positions and transformations are mapped from the group to the groups parent.
		"""
		res = super(QGraphicsScene,self).destroyItemGroup(group)
		return res
	#----------------------------------------------------------------------
	def dragEnterEvent(self,event):
		"""
		dragEnterEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented in a subclass to receive drag enter events for the scene.
		The default implementation accepts the event and prepares the scene to accept drag move events.
		"""
		res = super(QGraphicsScene,self).dragEnterEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragLeaveEvent(self,event):
		"""
		dragLeaveEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented in a subclass to receive drag leave events for the scene.
		"""
		res = super(QGraphicsScene,self).dragLeaveEvent(event)
		return res
	#----------------------------------------------------------------------
	def dragMoveEvent(self,event):
		"""
		dragMoveEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented in a subclass to receive drag move events for the scene.
		"""
		res = super(QGraphicsScene,self).dragMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def drawBackground(self,painter,rect):
		"""
		drawBackground(painter,rect)
			painter=QtGui.QPainter
			rect=QtCore.QRectF

		Draws the background of the scene using painter , before any items and the foreground are drawn
		Reimplement this function to provide a custom background for the scene.
		All painting is done in scene coordinates
		The rect parameter is the exposed rectangle.
		If all you want is to define a color, texture, or gradient for the background, you can call PySide.QtGui.QGraphicsScene.setBackgroundBrush() instead.
		"""
		res = super(QGraphicsScene,self).drawBackground(painter,rect)
		return res
	#----------------------------------------------------------------------
	def drawForeground(self,painter,rect):
		"""
		drawForeground(painter,rect)
			painter=QtGui.QPainter
			rect=QtCore.QRectF

		Draws the foreground of the scene using painter , after the background and all items have been drawn
		Reimplement this function to provide a custom foreground for the scene.
		All painting is done in scene coordinates
		The rect parameter is the exposed rectangle.
		If all you want is to define a color, texture or gradient for the foreground, you can call PySide.QtGui.QGraphicsScene.setForegroundBrush() instead.
		"""
		res = super(QGraphicsScene,self).drawForeground(painter,rect)
		return res
	#----------------------------------------------------------------------
	def dropEvent(self,event):
		"""
		dropEvent(event)
			event=QtGui.QGraphicsSceneDragDropEvent

		This event handler, for event event , can be reimplemented in a subclass to receive drop events for the scene.
		"""
		res = super(QGraphicsScene,self).dropEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusInEvent(self,event):
		"""
		focusInEvent(event)
			event=QtGui.QFocusEvent

		This event handler, for event focusEvent , can be reimplemented in a subclass to receive focus in events.
		The default implementation sets focus on the scene, and then on the last focus item.
		"""
		res = super(QGraphicsScene,self).focusInEvent(event)
		return res
	#----------------------------------------------------------------------
	def focusOutEvent(self,event):
		"""
		focusOutEvent(event)
			event=QtGui.QFocusEvent

		This event handler, for event focusEvent , can be reimplemented in a subclass to receive focus out events.
		The default implementation removes focus from any focus item, then removes focus from the scene.
		"""
		res = super(QGraphicsScene,self).focusOutEvent(event)
		return res
	#----------------------------------------------------------------------
	def helpEvent(self,event):
		"""
		helpEvent(event)
			event=QtGui.QGraphicsSceneHelpEvent

		This event handler, for event helpEvent , can be reimplemented in a subclass to receive help events
		The events are of type QEvent.ToolTip , which are created when a tooltip is requested.
		The default implementation shows the tooltip of the topmost item, i.e., the item with the highest z-value, at the mouse cursor position
		If no item has a tooltip set, this function does nothing.
		"""
		res = super(QGraphicsScene,self).helpEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodEvent(self,event):
		"""
		inputMethodEvent(event)
			event=QtGui.QInputMethodEvent

		This event handler, for event event , can be reimplemented in a subclass to receive input method events for the scene.
		The default implementation forwards the event to the PySide.QtGui.QGraphicsScene.focusItem()
		If no item currently has focus or the current focus item does not accept input methods, this function does nothing.
		"""
		res = super(QGraphicsScene,self).inputMethodEvent(event)
		return res
	#----------------------------------------------------------------------
	def inputMethodQuery(self,query):
		"""
		inputMethodQuery(query)
			query=QtCore.Qt.InputMethodQuery


		"""
		res = super(QGraphicsScene,self).inputMethodQuery(query)
		return res
	#----------------------------------------------------------------------
	def invalidate(self,*args,**kwargs):
		"""
		invalidate(rect=None,layers=None)
			rect=QtCore.QRectF
			layers=QtGui.QGraphicsScene.SceneLayers

		invalidate(x,y,w,h,layers=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			layers=QtGui.QGraphicsScene.SceneLayers


		"""
		res = super(QGraphicsScene,self).invalidate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y,deviceTransform)
			x=QtCore.qreal
			y=QtCore.qreal
			deviceTransform=QtGui.QTransform

		itemAt(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		itemAt(pos,deviceTransform)
			pos=QtCore.QPointF
			deviceTransform=QtGui.QTransform

		itemAt(pos)
			pos=QtCore.QPointF

		This is an overloaded function.
		Returns the topmost item at the position specified by (x , y ), or 0 if there are no items at this position.
		deviceTransform is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.
		This convenience function is equivalent to calling itemAt(QPointF(x, y), deviceTransform) .
		"""
		res = super(QGraphicsScene,self).itemAt(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def items(self,*args,**kwargs):
		"""
		items(rect,mode=None)
			rect=QtCore.QRectF
			mode=QtCore.Qt.ItemSelectionMode

		items(rect,mode,order,deviceTransform=None)
			rect=QtCore.QRectF
			mode=QtCore.Qt.ItemSelectionMode
			order=QtCore.Qt.SortOrder
			deviceTransform=QtGui.QTransform

		items(x,y,w,h,mode=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			mode=QtCore.Qt.ItemSelectionMode

		items(x,y,w,h,mode,order,deviceTransform=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			mode=QtCore.Qt.ItemSelectionMode
			order=QtCore.Qt.SortOrder
			deviceTransform=QtGui.QTransform

		items(polygon,mode,order,deviceTransform=None)
			polygon=QtGui.QPolygonF
			mode=QtCore.Qt.ItemSelectionMode
			order=QtCore.Qt.SortOrder
			deviceTransform=QtGui.QTransform

		items(polygon,mode=None)
			polygon=QtGui.QPolygonF
			mode=QtCore.Qt.ItemSelectionMode

		items(order)
			order=QtCore.Qt.SortOrder

		items(path,mode=None)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode

		items(pos,mode,order,deviceTransform=None)
			pos=QtCore.QPointF
			mode=QtCore.Qt.ItemSelectionMode
			order=QtCore.Qt.SortOrder
			deviceTransform=QtGui.QTransform

		items(path,mode,order,deviceTransform=None)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode
			order=QtCore.Qt.SortOrder
			deviceTransform=QtGui.QTransform

		items(pos)
			pos=QtCore.QPointF


		"""
		res = super(QGraphicsScene,self).items(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def keyPressEvent(self,event):
		"""
		keyPressEvent(event)
			event=QtGui.QKeyEvent

		This event handler, for event keyEvent , can be reimplemented in a subclass to receive keypress events
		The default implementation forwards the event to current focus item.
		"""
		res = super(QGraphicsScene,self).keyPressEvent(event)
		return res
	#----------------------------------------------------------------------
	def keyReleaseEvent(self,event):
		"""
		keyReleaseEvent(event)
			event=QtGui.QKeyEvent

		This event handler, for event keyEvent , can be reimplemented in a subclass to receive key release events
		The default implementation forwards the event to current focus item.
		"""
		res = super(QGraphicsScene,self).keyReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseDoubleClickEvent(self,event):
		"""
		mouseDoubleClickEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event mouseEvent , can be reimplemented in a subclass to receive mouse doubleclick events for the scene.
		If someone doubleclicks on the scene, the scene will first receive a mouse press event, followed by a release event (i.e., a click), then a doubleclick event, and finally a release event
		If the doubleclick event is delivered to a different item than the one that received the first press and release, it will be delivered as a press event
		However, tripleclick events are not delivered as doubleclick events in this case.
		The default implementation is similar to PySide.QtGui.QGraphicsScene.mousePressEvent() .
		"""
		res = super(QGraphicsScene,self).mouseDoubleClickEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseMoveEvent(self,event):
		"""
		mouseMoveEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event mouseEvent , can be reimplemented in a subclass to receive mouse move events for the scene.
		The default implementation depends on the mouse grabber state
		If there is a mouse grabber item, the event is sent to the mouse grabber
		If there are any items that accept hover events at the current position, the event is translated into a hover event and accepted; otherwise its ignored.
		"""
		res = super(QGraphicsScene,self).mouseMoveEvent(event)
		return res
	#----------------------------------------------------------------------
	def mousePressEvent(self,event):
		"""
		mousePressEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event mouseEvent , can be reimplemented in a subclass to receive mouse press events for the scene.
		The default implementation depends on the state of the scene
		If there is a mouse grabber item, then the event is sent to the mouse grabber
		Otherwise, it is forwarded to the topmost item that accepts mouse events at the scene position from the event, and that item promptly becomes the mouse grabber item.
		If there is no item at the given position on the scene, the selection area is reset, any focus item loses its input focus, and the event is then ignored.
		"""
		res = super(QGraphicsScene,self).mousePressEvent(event)
		return res
	#----------------------------------------------------------------------
	def mouseReleaseEvent(self,event):
		"""
		mouseReleaseEvent(event)
			event=QtGui.QGraphicsSceneMouseEvent

		This event handler, for event mouseEvent , can be reimplemented in a subclass to receive mouse release events for the scene.
		The default implementation depends on the mouse grabber state
		If there is no mouse grabber, the event is ignored
		Otherwise, if there is a mouse grabber item, the event is sent to the mouse grabber
		If this mouse release represents the last pressed button on the mouse, the mouse grabber item then loses the mouse grab.
		"""
		res = super(QGraphicsScene,self).mouseReleaseEvent(event)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,item):
		"""
		removeItem(item)
			item=QtGui.QGraphicsItem

		Removes the item item and all its children from the scene
		The ownership of item is passed on to the caller (i.e., PySide.QtGui.QGraphicsScene will no longer delete item when destroyed).
		"""
		res = super(QGraphicsScene,self).removeItem(item)
		return res
	#----------------------------------------------------------------------
	def render(self,painter,target=None,source=None,aspectRatioMode=None):
		"""
		render(painter,target=None,source=None,aspectRatioMode=None)
			painter=QtGui.QPainter
			target=QtCore.QRectF
			source=QtCore.QRectF
			aspectRatioMode=QtCore.Qt.AspectRatioMode


		"""
		res = super(QGraphicsScene,self).render(painter,target,source,aspectRatioMode)
		return res
	#----------------------------------------------------------------------
	def sendEvent(self,item,event):
		"""
		sendEvent(item,event)
			item=QtGui.QGraphicsItem
			event=QtCore.QEvent

		Sends event event to item item through possible event filters.
		The event is sent only if the item is enabled.
		Returns false if the event was filtered or if the item is disabled
		Otherwise returns the value that was returned from the event handler.
		"""
		res = super(QGraphicsScene,self).sendEvent(item,event)

		return res
	#----------------------------------------------------------------------
	def setActivePanel(self,item):
		"""
		setActivePanel(item)
			item=QtGui.QGraphicsItem

		Activates item , which must be an item in this scene
		You can also pass 0 for item , in which case PySide.QtGui.QGraphicsScene will deactivate any currently active panel.
		If the scene is currently inactive, item remains inactive until the scene becomes active (or, ir item is 0, no item will be activated).
		"""
		res = super(QGraphicsScene,self).setActivePanel(item)
		return res
	#----------------------------------------------------------------------
	def setActiveWindow(self,widget):
		"""
		setActiveWindow(widget)
			widget=QtGui.QGraphicsWidget

		Activates widget , which must be a widget in this scene
		You can also pass 0 for widget , in which case PySide.QtGui.QGraphicsScene will deactivate any currently active window.
		"""
		res = super(QGraphicsScene,self).setActiveWindow(widget)
		return res
	#----------------------------------------------------------------------
	def setBackgroundBrush(self,brush):
		"""
		setBackgroundBrush(brush)
			brush=QtGui.QBrush

		This property holds the background brush of the scene..
		Set this property to changes the scenes background to a different color, gradient or texture
		The default background brush is Qt.NoBrush
		The background is drawn before (behind) the items.
		Example:
		QGraphicsScene.render() calls PySide.QtGui.QGraphicsScene.drawBackground() to draw the scene background
		For more detailed control over how the background is drawn, you can reimplement PySide.QtGui.QGraphicsScene.drawBackground() in a subclass of PySide.QtGui.QGraphicsScene .
		"""
		res = super(QGraphicsScene,self).setBackgroundBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setBspTreeDepth(self,depth):
		"""
		setBspTreeDepth(depth)
			depth=QtCore.int

		This property holds the depth of PySide.QtGui.QGraphicsScene s BSP index tree.
		This property has no effect when NoIndex is used.
		This value determines the depth of PySide.QtGui.QGraphicsScene s BSP tree
		The depth directly affects PySide.QtGui.QGraphicsScene s performance and memory usage; the latter growing exponentially with the depth of the tree
		With an optimal tree depth, PySide.QtGui.QGraphicsScene can instantly determine the locality of items, even for scenes with thousands or millions of items
		This also greatly improves rendering performance.
		By default, the value is 0, in which case Qt will guess a reasonable default depth based on the size, location and number of items in the scene
		If these parameters change frequently, however, you may experience slowdowns as PySide.QtGui.QGraphicsScene retunes the depth internally
		You can avoid potential slowdowns by fixating the tree depth through setting this property.
		The depth of the tree and the size of the scene rectangle decide the granularity of the scenes partitioning
		The size of each scene segment is determined by the following algorithm:
		The BSP tree has an optimal size when each segment contains between 0 and 10 items.
		"""
		res = super(QGraphicsScene,self).setBspTreeDepth(depth)
		return res
	#----------------------------------------------------------------------
	def setFocus(self,focusReason=None):
		"""
		setFocus(focusReason=None)
			focusReason=QtCore.Qt.FocusReason


		"""
		res = super(QGraphicsScene,self).setFocus(focusReason)
		return res
	#----------------------------------------------------------------------
	def setFocusItem(self,item,focusReason=None):
		"""
		setFocusItem(item,focusReason=None)
			item=QtGui.QGraphicsItem
			focusReason=QtCore.Qt.FocusReason


		"""
		res = super(QGraphicsScene,self).setFocusItem(item,focusReason)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		This property holds the scenes default font.
		This property provides the scenes font
		The scene font defaults to, and resolves all its entries from, QApplication::font.
		If the scenes font changes, either directly through PySide.QtGui.QGraphicsScene.setFont() or indirectly when the application font changes, PySide.QtGui.QGraphicsScene first sends itself a FontChange event, and it then sends FontChange events to all top-level widget items in the scene
		These items respond by resolving their own fonts to the scene, and they then notify their children, who again notify their children, and so on, until all widget items have updated their fonts.
		Changing the scene font, (directly or indirectly through QApplication.setFont() ,) automatically schedules a redraw the entire scene.
		"""
		res = super(QGraphicsScene,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setForegroundBrush(self,brush):
		"""
		setForegroundBrush(brush)
			brush=QtGui.QBrush

		This property holds the foreground brush of the scene..
		Change this property to set the scenes foreground to a different color, gradient or texture.
		The foreground is drawn after (on top of) the items
		The default foreground brush is Qt.NoBrush ( i.e
		the foreground is not drawn).
		Example:
		QGraphicsScene.render() calls PySide.QtGui.QGraphicsScene.drawForeground() to draw the scene foreground
		For more detailed control over how the foreground is drawn, you can reimplement the PySide.QtGui.QGraphicsScene.drawForeground() function in a PySide.QtGui.QGraphicsScene subclass.
		"""
		res = super(QGraphicsScene,self).setForegroundBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setItemIndexMethod(self,method):
		"""
		setItemIndexMethod(method)
			method=QtGui.QGraphicsScene.ItemIndexMethod

		This property holds the item indexing method..
		PySide.QtGui.QGraphicsScene applies an indexing algorithm to the scene, to speed up item discovery functions like PySide.QtGui.QGraphicsScene.items() and PySide.QtGui.QGraphicsScene.itemAt()
		Indexing is most efficient for static scenes (i.e., where items dont move around)
		For dynamic scenes, or scenes with many animated items, the index bookkeeping can outweight the fast lookup speeds.
		For the common case, the default index method BspTreeIndex works fine
		If your scene uses many animations and you are experiencing slowness, you can disable indexing by calling setItemIndexMethod(NoIndex) .
		"""
		res = super(QGraphicsScene,self).setItemIndexMethod(method)
		return res
	#----------------------------------------------------------------------
	def setPalette(self,palette):
		"""
		setPalette(palette)
			palette=QtGui.QPalette

		This property holds the scenes default palette.
		This property provides the scenes palette
		The scene palette defaults to, and resolves all its entries from, QApplication::palette.
		If the scenes palette changes, either directly through PySide.QtGui.QGraphicsScene.setPalette() or indirectly when the application palette changes, PySide.QtGui.QGraphicsScene first sends itself a PaletteChange event, and it then sends PaletteChange events to all top-level widget items in the scene
		These items respond by resolving their own palettes to the scene, and they then notify their children, who again notify their children, and so on, until all widget items have updated their palettes.
		Changing the scene palette, (directly or indirectly through QApplication.setPalette() ,) automatically schedules a redraw the entire scene.
		"""
		res = super(QGraphicsScene,self).setPalette(palette)
		return res
	#----------------------------------------------------------------------
	def setSceneRect(self,*args,**kwargs):
		"""
		setSceneRect(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		setSceneRect(rect)
			rect=QtCore.QRectF


		"""
		res = super(QGraphicsScene,self).setSceneRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSelectionArea(self,*args,**kwargs):
		"""
		setSelectionArea(path,mode,deviceTransform)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode
			deviceTransform=QtGui.QTransform

		setSelectionArea(path,deviceTransform)
			path=QtGui.QPainterPath
			deviceTransform=QtGui.QTransform

		setSelectionArea(path,mode)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode

		setSelectionArea(path)
			path=QtGui.QPainterPath


		"""
		res = super(QGraphicsScene,self).setSelectionArea(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSortCacheEnabled(self,enabled):
		"""
		setSortCacheEnabled(enabled)
			enabled=QtCore.bool

		This property holds whether sort caching is enabled.
		Since Qt 4.6, this property has no effect.
		"""
		res = super(QGraphicsScene,self).setSortCacheEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setStickyFocus(self,enabled):
		"""
		setStickyFocus(enabled)
			enabled=QtCore.bool

		This property holds whether clicking into the scene background will clear focus.
		In a PySide.QtGui.QGraphicsScene with PySide.QtGui.QGraphicsScene.stickyFocus() set to true, focus will remain unchanged when the user clicks into the scene background or on an item that does not accept focus
		Otherwise, focus will be cleared.
		By default, this property is false.
		Focus changes in response to a mouse press
		You can reimplement PySide.QtGui.QGraphicsScene.mousePressEvent() in a subclass of PySide.QtGui.QGraphicsScene to toggle this property based on where the user has clicked.
		"""
		res = super(QGraphicsScene,self).setStickyFocus(enabled)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,style):
		"""
		setStyle(style)
			style=QtGui.QStyle

		Sets or replaces the style of the scene to style , and reparents the style to this scene
		Any previously assigned style is deleted
		The scenes style defaults to QApplication.style() , and serves as the default for all PySide.QtGui.QGraphicsWidget items in the scene.
		Changing the style, either directly by calling this function, or indirectly by calling QApplication.setStyle() , will automatically update the style for all widgets in the scene that do not have a style explicitly assigned to them.
		If style is 0, PySide.QtGui.QGraphicsScene will revert to QApplication.style() .
		"""
		res = super(QGraphicsScene,self).setStyle(style)
		return res
	#----------------------------------------------------------------------
	def wheelEvent(self,event):
		"""
		wheelEvent(event)
			event=QtGui.QGraphicsSceneWheelEvent

		This event handler, for event wheelEvent , can be reimplemented in a subclass to receive mouse wheel events for the scene.
		By default, the event is delivered to the topmost visible item under the cursor
		If ignored, the event propagates to the item beneath, and again until the event is accepted, or it reaches the scene
		If no items accept the event, it is ignored.
		"""
		res = super(QGraphicsScene,self).wheelEvent(event)
		return res

	ActivePanel        = property(activePanel)
	ActiveWindow       = property(activeWindow)
	BackgroundBrush    = property(backgroundBrush)
	BspTreeDepth       = property(bspTreeDepth)
	ClearFocus         = property(clearFocus)
	FocusItem          = property(focusItem)
	Font               = property(font)
	ForegroundBrush    = property(foregroundBrush)
	HasFocus           = property(hasFocus)
	Height             = property(height)
	IsActive           = property(isActive)
	IsSortCacheEnabled = property(isSortCacheEnabled)
	ItemIndexMethod    = property(itemIndexMethod)
	Items              = property(items)
	ItemsBoundingRect  = property(itemsBoundingRect)
	MouseGrabberItem   = property(mouseGrabberItem)
	Palette            = property(palette)
	SceneRect          = property(sceneRect)
	SelectedItems      = property(selectedItems)
	SelectionArea      = property(selectionArea)
	StickyFocus        = property(stickyFocus)
	Style              = property(style)
	Views              = property(views)
	Width              = property(width)