from Qt_Tools import QtGui, QtCore
from QAbstractScrollArea import QAbstractScrollArea
class QGraphicsView(QtGui.QGraphicsView, QAbstractScrollArea):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the scene in the view when the whole scene is visible..
		If the whole scene is visible in the view, (i.e., there are no visible scroll bars,) the views alignment will decide where the scene will be rendered in the view
		For example, if the alignment is Qt.AlignCenter , which is default, the scene will be centered in the view, and if the alignment is ( Qt.AlignLeft | Qt.AlignTop ), the scene will be rendered in the top-left corner of the view.
		"""
		res = super(QGraphicsView,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def backgroundBrush(self):
		"""
		This property holds the background brush of the scene..
		This property sets the background brush for the scene in this view
		It is used to override the scenes own background, and defines the behavior of PySide.QtGui.QGraphicsView.drawBackground()
		To provide custom background drawing for this view, you can reimplement PySide.QtGui.QGraphicsView.drawBackground() instead.
		By default, this property contains a brush with the Qt.NoBrush pattern.
		"""
		res = super(QGraphicsView,self).backgroundBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def cacheMode(self):
		"""
		This property holds which parts of the view are cached.
		PySide.QtGui.QGraphicsView can cache pre-rendered content in a PySide.QtGui.QPixmap , which is then drawn onto the viewport
		The purpose of such caching is to speed up the total rendering time for areas that are slow to render
		Texture, gradient and alpha blended backgrounds, for example, can be notibly slow to render; especially with a transformed view
		The CacheBackground flag enables caching of the views background
		For example:
		The cache is invalidated every time the view is transformed
		However, when scrolling, only partial invalidation is required.
		By default, nothing is cached.
		"""
		res = super(QGraphicsView,self).cacheMode()
		isinstance(res,QtGui.QGraphicsView.CacheMode)
		return res
	#----------------------------------------------------------------------
	def dragMode(self):
		"""
		This property holds the behavior for dragging the mouse over the scene while the left mouse button is pressed..
		This property defines what should happen when the user clicks on the scene background and drags the mouse (e.g., scrolling the viewport contents using a pointing hand cursor, or selecting multiple items with a rubber band)
		The default value, NoDrag , does nothing.
		This behavior only affects mouse clicks that are not handled by any item
		You can define a custom behavior by creating a subclass of PySide.QtGui.QGraphicsView and reimplementing PySide.QtGui.QGraphicsView.mouseMoveEvent() .
		"""
		res = super(QGraphicsView,self).dragMode()
		isinstance(res,QtGui.QGraphicsView.DragMode)
		return res
	#----------------------------------------------------------------------
	def foregroundBrush(self):
		"""
		This property holds the foreground brush of the scene..
		This property sets the foreground brush for the scene in this view
		It is used to override the scenes own foreground, and defines the behavior of PySide.QtGui.QGraphicsView.drawForeground()
		To provide custom foreground drawing for this view, you can reimplement PySide.QtGui.QGraphicsView.drawForeground() instead.
		By default, this property contains a brush with the Qt.NoBrush pattern.
		"""
		res = super(QGraphicsView,self).foregroundBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def isInteractive(self):
		"""
		This property holds whether the view allowed scene interaction..
		If enabled, this view is set to allow scene interaction
		Otherwise, this view will not allow interaction, and any mouse or key events are ignored (i.e., it will act as a read-only view).
		By default, this property is true.
		"""
		res = super(QGraphicsView,self).isInteractive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isTransformed(self):
		"""
		Returns true if the view is transformed (i.e., a non-identity transform has been assigned, or the scrollbars are adjusted).
		"""
		res = super(QGraphicsView,self).isTransformed()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def items(self):
		"""
		Returns a list of all the items in the associated scene, in descending stacking order (i.e., the first item in the returned list is the uppermost item).
		"""
		res = super(QGraphicsView,self).items()
		return res
	#----------------------------------------------------------------------
	def matrix(self):
		"""
		Returns the current transformation matrix for the view
		If no current transformation is set, the identity matrix is returned.
		"""
		res = super(QGraphicsView,self).matrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def optimizationFlags(self):
		"""
		This property holds flags that can be used to tune PySide.QtGui.QGraphicsView s performance..
		PySide.QtGui.QGraphicsView uses clipping, extra bounding rect adjustments, and certain other aids to improve rendering quality and performance for the common case graphics scene
		However, depending on the target platform, the scene, and the viewport in use, some of these operations can degrade performance.
		The effect varies from flag to flag; see the OptimizationFlags documentation for details.
		By default, no optimization flags are enabled.
		"""
		res = super(QGraphicsView,self).optimizationFlags()
		isinstance(res,QtGui.QGraphicsView.OptimizationFlags)
		return res
	#----------------------------------------------------------------------
	def renderHints(self):
		"""
		This property holds the default render hints for the view.
		These hints are used to initialize PySide.QtGui.QPainter before each visible item is drawn
		PySide.QtGui.QPainter uses render hints to toggle rendering features such as antialiasing and smooth pixmap transformation.
		QPainter.TextAntialiasing is enabled by default.
		Example:
		"""
		res = super(QGraphicsView,self).renderHints()
		isinstance(res,QtGui.QPainter.RenderHints)
		return res
	#----------------------------------------------------------------------
	def resetCachedContent(self):
		"""
		Resets any cached content
		Calling this function will clear PySide.QtGui.QGraphicsView s cache
		If the current cache mode is CacheNone , this function does nothing.
		This function is called automatically for you when the PySide.QtGui.QGraphicsView.backgroundBrush() or QGraphicsScene.backgroundBrush properties change; you only need to call this function if you have reimplemented QGraphicsScene.drawBackground() or QGraphicsView.drawBackground() to draw a custom background, and need to trigger a full redraw.
		"""
		res = super(QGraphicsView,self).resetCachedContent()
		return res
	#----------------------------------------------------------------------
	def resetMatrix(self):
		"""
		Resets the view transformation matrix to the identity matrix.
		"""
		res = super(QGraphicsView,self).resetMatrix()
		return res
	#----------------------------------------------------------------------
	def resetTransform(self):
		"""
		Resets the view transformation to the identity matrix.
		"""
		res = super(QGraphicsView,self).resetTransform()
		return res
	#----------------------------------------------------------------------
	def resizeAnchor(self):
		"""
		This property holds how the view should position the scene when the view is resized..
		PySide.QtGui.QGraphicsView uses this property to decide how to position the scene in the viewport when the viewport widgets size changes
		The default behavior, NoAnchor , leaves the scenes position unchanged during a resize; the top-left corner of the view will appear to be anchored while resizing.
		Note that the effect of this property is noticeable when only a part of the scene is visible (i.e., when there are scroll bars)
		Otherwise, if the whole scene fits in the view, PySide.QtGui.QGraphicsScene uses the view PySide.QtGui.QGraphicsView.alignment() to position the scene in the view.
		"""
		res = super(QGraphicsView,self).resizeAnchor()
		isinstance(res,QtGui.QGraphicsView.ViewportAnchor)
		return res
	#----------------------------------------------------------------------
	def rubberBandSelectionMode(self):
		"""
		This property holds the behavior for selecting items with a rubber band selection rectangle..
		This property defines how items are selected when using the RubberBandDrag drag mode.
		The default value is Qt.IntersectsItemShape ; all items whose shape intersects with or is contained by the rubber band are selected.
		"""
		res = super(QGraphicsView,self).rubberBandSelectionMode()
		isinstance(res,QtCore.Qt.ItemSelectionMode)
		return res
	#----------------------------------------------------------------------
	def scene(self):
		"""
		Returns a pointer to the scene that is currently visualized in the view
		If no scene is currently visualized, 0 is returned.
		"""
		res = super(QGraphicsView,self).scene()
		isinstance(res,QtGui.QGraphicsScene)
		return res
	#----------------------------------------------------------------------
	def sceneRect(self):
		"""
		This property holds the area of the scene visualized by this view..
		The scene rectangle defines the extent of the scene, and in the views case, this means the area of the scene that you can navigate using the scroll bars.
		If unset, or if a null PySide.QtCore.QRectF is set, this property has the same value as QGraphicsScene.sceneRect , and it changes with QGraphicsScene.sceneRect
		Otherwise, the views scene rect is unaffected by the scene.
		Note that, although the scene supports a virtually unlimited size, the range of the scroll bars will never exceed the range of an integer (INT_MIN, INT_MAX)
		When the scene is larger than the scroll bars values, you can choose to use PySide.QtGui.QGraphicsView.translate() to navigate the scene instead.
		By default, this property contains a rectangle at the origin with zero width and height.
		"""
		res = super(QGraphicsView,self).sceneRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def transform(self):
		"""
		Returns the current transformation matrix for the view
		If no current transformation is set, the identity matrix is returned.
		"""
		res = super(QGraphicsView,self).transform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def transformationAnchor(self):
		"""
		This property holds how the view should position the scene during transformations..
		PySide.QtGui.QGraphicsView uses this property to decide how to position the scene in the viewport when the transformation matrix changes, and the coordinate system of the view is transformed
		The default behavior, AnchorViewCenter , ensures that the scene point at the center of the view remains unchanged during transformations (e.g., when rotating, the scene will appear to rotate around the center of the view).
		Note that the effect of this property is noticeable when only a part of the scene is visible (i.e., when there are scroll bars)
		Otherwise, if the whole scene fits in the view, PySide.QtGui.QGraphicsScene uses the view PySide.QtGui.QGraphicsView.alignment() to position the scene in the view.
		"""
		res = super(QGraphicsView,self).transformationAnchor()
		isinstance(res,QtGui.QGraphicsView.ViewportAnchor)
		return res
	#----------------------------------------------------------------------
	def viewportTransform(self):
		"""
		Returns a matrix that maps viewport coordinates to scene coordinates.
		"""
		res = super(QGraphicsView,self).viewportTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def viewportUpdateMode(self):
		"""
		This property holds how the viewport should update its contents..
		PySide.QtGui.QGraphicsView uses this property to decide how to update areas of the scene that have been reexposed or changed
		Usually you do not need to modify this property, but there are some cases where doing so can improve rendering performance
		See the QGraphicsView.ViewportUpdateMode documentation for specific details.
		The default value is MinimalViewportUpdate , where PySide.QtGui.QGraphicsView will update as small an area of the viewport as possible when the contents change.
		"""
		res = super(QGraphicsView,self).viewportUpdateMode()
		isinstance(res,QtGui.QGraphicsView.ViewportUpdateMode)
		return res
	#----------------------------------------------------------------------
	def centerOn(self,*args,**kwargs):
		"""
		centerOn(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		centerOn(item)
			item=QtGui.QGraphicsItem

		centerOn(pos)
			pos=QtCore.QPointF

		This is an overloaded function.
		This function is provided for convenience
		Its equivalent to calling centerOn( PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsView,self).centerOn(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawBackground(self,painter,rect):
		"""
		drawBackground(painter,rect)
			painter=QtGui.QPainter
			rect=QtCore.QRectF

		Draws the background of the scene using painter , before any items and the foreground are drawn
		Reimplement this function to provide a custom background for this view.
		If all you want is to define a color, texture or gradient for the background, you can call PySide.QtGui.QGraphicsView.setBackgroundBrush() instead.
		All painting is done in scene coordinates
		rect is the exposed rectangle.
		The default implementation fills rect using the views PySide.QtGui.QGraphicsView.backgroundBrush()
		If no such brush is defined (the default), the scenes PySide.QtGui.QGraphicsView.drawBackground() function is called instead.
		"""
		res = super(QGraphicsView,self).drawBackground(painter,rect)
		return res
	#----------------------------------------------------------------------
	def drawForeground(self,painter,rect):
		"""
		drawForeground(painter,rect)
			painter=QtGui.QPainter
			rect=QtCore.QRectF

		Draws the foreground of the scene using painter , after the background and all items are drawn
		Reimplement this function to provide a custom foreground for this view.
		If all you want is to define a color, texture or gradient for the foreground, you can call PySide.QtGui.QGraphicsView.setForegroundBrush() instead.
		All painting is done in scene coordinates
		rect is the exposed rectangle.
		The default implementation fills rect using the views PySide.QtGui.QGraphicsView.foregroundBrush()
		If no such brush is defined (the default), the scenes PySide.QtGui.QGraphicsView.drawForeground() function is called instead.
		"""
		res = super(QGraphicsView,self).drawForeground(painter,rect)
		return res
	#----------------------------------------------------------------------
	def drawItems(self,painter,items,options):
		"""
		drawItems(painter,items,options)
			painter=QtGui.QPainter
			items=QtGui.QGraphicsItem
			options=QtGui.QStyleOptionGraphicsItem


		"""
		res = super(QGraphicsView,self).drawItems(painter,items,options)
		return res
	#----------------------------------------------------------------------
	def ensureVisible(self,*args,**kwargs):
		"""
		ensureVisible(rect,xmargin=None,ymargin=None)
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

		ensureVisible(item,xmargin=None,ymargin=None)
			item=QtGui.QGraphicsItem
			xmargin=QtCore.int
			ymargin=QtCore.int

		Scrolls the contents of the viewport so that the scene rectangle rect is visible, with margins specified in pixels by xmargin and ymargin
		If the specified rect cannot be reached, the contents are scrolled to the nearest valid position
		The default value for both margins is 50 pixels.
		"""
		res = super(QGraphicsView,self).ensureVisible(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def fitInView(self,*args,**kwargs):
		"""
		fitInView(item,aspectRadioMode=None)
			item=QtGui.QGraphicsItem
			aspectRadioMode=QtCore.Qt.AspectRatioMode

		fitInView(rect,aspectRadioMode=None)
			rect=QtCore.QRectF
			aspectRadioMode=QtCore.Qt.AspectRatioMode

		fitInView(x,y,w,h,aspectRadioMode=None)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal
			aspectRadioMode=QtCore.Qt.AspectRatioMode


		"""
		res = super(QGraphicsView,self).fitInView(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,*args,**kwargs):
		"""
		itemAt(x,y)
			x=QtCore.int
			y=QtCore.int

		itemAt(pos)
			pos=QtCore.QPoint

		This is an overloaded function.
		This function is provided for convenience
		Its equivalent to calling itemAt( PySide.QtCore.QPoint (x , y )).
		"""
		res = super(QGraphicsView,self).itemAt(*args,**kwargs)
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def items(self,*args,**kwargs):
		"""
		items(x,y)
			x=QtCore.int
			y=QtCore.int

		items(x,y,w,h,mode=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			mode=QtCore.Qt.ItemSelectionMode

		items(rect,mode=None)
			rect=QtCore.QRect
			mode=QtCore.Qt.ItemSelectionMode

		items(polygon,mode=None)
			polygon=QtGui.QPolygon
			mode=QtCore.Qt.ItemSelectionMode

		items(path,mode=None)
			path=QtGui.QPainterPath
			mode=QtCore.Qt.ItemSelectionMode

		items(pos)
			pos=QtCore.QPoint

		This function is provided for convenience
		Its equivalent to calling items( PySide.QtCore.QPoint (x , y )).
		"""
		res = super(QGraphicsView,self).items(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def mapFromScene(self,*args,**kwargs):
		"""
		mapFromScene(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		mapFromScene(rect)
			rect=QtCore.QRectF

		mapFromScene(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		mapFromScene(path)
			path=QtGui.QPainterPath

		mapFromScene(polygon)
			polygon=QtGui.QPolygonF

		mapFromScene(point)
			point=QtCore.QPointF

		This function is provided for convenience
		Its equivalent to calling mapFromScene( PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsView,self).mapFromScene(*args,**kwargs)
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def mapToScene(self,*args,**kwargs):
		"""
		mapToScene(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		mapToScene(x,y)
			x=QtCore.int
			y=QtCore.int

		mapToScene(rect)
			rect=QtCore.QRect

		mapToScene(polygon)
			polygon=QtGui.QPolygon

		mapToScene(point)
			point=QtCore.QPoint

		mapToScene(path)
			path=QtGui.QPainterPath

		This function is provided for convenience
		Its equivalent to calling mapToScene( PySide.QtCore.QRect (x , y , w , h )).
		"""
		res = super(QGraphicsView,self).mapToScene(*args,**kwargs)
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def render(self,painter,target=None,source=None,aspectRatioMode=None):
		"""
		render(painter,target=None,source=None,aspectRatioMode=None)
			painter=QtGui.QPainter
			target=QtCore.QRectF
			source=QtCore.QRect
			aspectRatioMode=QtCore.Qt.AspectRatioMode


		"""
		res = super(QGraphicsView,self).render(painter,target,source,aspectRatioMode)
		return res
	#----------------------------------------------------------------------
	def rotate(self,angle):
		"""
		rotate(angle)
			angle=QtCore.qreal

		Rotates the current view transformation angle degrees clockwise.
		"""
		res = super(QGraphicsView,self).rotate(angle)
		return res
	#----------------------------------------------------------------------
	def scale(self,sx,sy):
		"""
		scale(sx,sy)
			sx=QtCore.qreal
			sy=QtCore.qreal

		Scales the current view transformation by (sx , sy ).
		"""
		res = super(QGraphicsView,self).scale(sx,sy)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,alignment):
		"""
		setAlignment(alignment)
			alignment=QtCore.Qt.Alignment

		This property holds the alignment of the scene in the view when the whole scene is visible..
		If the whole scene is visible in the view, (i.e., there are no visible scroll bars,) the views alignment will decide where the scene will be rendered in the view
		For example, if the alignment is Qt.AlignCenter , which is default, the scene will be centered in the view, and if the alignment is ( Qt.AlignLeft | Qt.AlignTop ), the scene will be rendered in the top-left corner of the view.
		"""
		res = super(QGraphicsView,self).setAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setBackgroundBrush(self,brush):
		"""
		setBackgroundBrush(brush)
			brush=QtGui.QBrush

		This property holds the background brush of the scene..
		This property sets the background brush for the scene in this view
		It is used to override the scenes own background, and defines the behavior of PySide.QtGui.QGraphicsView.drawBackground()
		To provide custom background drawing for this view, you can reimplement PySide.QtGui.QGraphicsView.drawBackground() instead.
		By default, this property contains a brush with the Qt.NoBrush pattern.
		"""
		res = super(QGraphicsView,self).setBackgroundBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setCacheMode(self,mode):
		"""
		setCacheMode(mode)
			mode=QtGui.QGraphicsView.CacheMode

		This property holds which parts of the view are cached.
		PySide.QtGui.QGraphicsView can cache pre-rendered content in a PySide.QtGui.QPixmap , which is then drawn onto the viewport
		The purpose of such caching is to speed up the total rendering time for areas that are slow to render
		Texture, gradient and alpha blended backgrounds, for example, can be notibly slow to render; especially with a transformed view
		The CacheBackground flag enables caching of the views background
		For example:
		The cache is invalidated every time the view is transformed
		However, when scrolling, only partial invalidation is required.
		By default, nothing is cached.
		"""
		res = super(QGraphicsView,self).setCacheMode(mode)
		return res
	#----------------------------------------------------------------------
	def setDragMode(self,mode):
		"""
		setDragMode(mode)
			mode=QtGui.QGraphicsView.DragMode

		This property holds the behavior for dragging the mouse over the scene while the left mouse button is pressed..
		This property defines what should happen when the user clicks on the scene background and drags the mouse (e.g., scrolling the viewport contents using a pointing hand cursor, or selecting multiple items with a rubber band)
		The default value, NoDrag , does nothing.
		This behavior only affects mouse clicks that are not handled by any item
		You can define a custom behavior by creating a subclass of PySide.QtGui.QGraphicsView and reimplementing PySide.QtGui.QGraphicsView.mouseMoveEvent() .
		"""
		res = super(QGraphicsView,self).setDragMode(mode)
		return res
	#----------------------------------------------------------------------
	def setForegroundBrush(self,brush):
		"""
		setForegroundBrush(brush)
			brush=QtGui.QBrush

		This property holds the foreground brush of the scene..
		This property sets the foreground brush for the scene in this view
		It is used to override the scenes own foreground, and defines the behavior of PySide.QtGui.QGraphicsView.drawForeground()
		To provide custom foreground drawing for this view, you can reimplement PySide.QtGui.QGraphicsView.drawForeground() instead.
		By default, this property contains a brush with the Qt.NoBrush pattern.
		"""
		res = super(QGraphicsView,self).setForegroundBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setInteractive(self,allowed):
		"""
		setInteractive(allowed)
			allowed=QtCore.bool

		This property holds whether the view allowed scene interaction..
		If enabled, this view is set to allow scene interaction
		Otherwise, this view will not allow interaction, and any mouse or key events are ignored (i.e., it will act as a read-only view).
		By default, this property is true.
		"""
		res = super(QGraphicsView,self).setInteractive(allowed)
		return res
	#----------------------------------------------------------------------
	def setMatrix(self,matrix,combine=None):
		"""
		setMatrix(matrix,combine=None)
			matrix=QtGui.QMatrix
			combine=QtCore.bool

		Sets the views current transformation matrix to matrix .
		If combine is true, then matrix is combined with the current matrix; otherwise, matrixreplaces the current matrix
		combine is false by default.
		The transformation matrix tranforms the scene into view coordinates
		Using the default transformation, provided by the identity matrix, one pixel in the view represents one unit in the scene (e.g., a 10x10 rectangular item is drawn using 10x10 pixels in the view)
		If a 2x2 scaling matrix is applied, the scene will be drawn in 1:2 (e.g., a 10x10 rectangular item is then drawn using 20x20 pixels in the view).
		Example:
		To simplify interation with items using a transformed view, PySide.QtGui.QGraphicsView provides mapTo..
		and mapFrom..
		functions that can translate between scene and view coordinates
		For example, you can call PySide.QtGui.QGraphicsView.mapToScene() to map a view coordinate to a floating point scene coordinate, or PySide.QtGui.QGraphicsView.mapFromScene() to map from floating point scene coordinates to view coordinates.
		"""
		res = super(QGraphicsView,self).setMatrix(matrix,combine)
		return res
	#----------------------------------------------------------------------
	def setOptimizationFlag(self,flag,enabled=None):
		"""
		setOptimizationFlag(flag,enabled=None)
			flag=QtGui.QGraphicsView.OptimizationFlag
			enabled=QtCore.bool

		Enables flag if enabled is true; otherwise disables flag .
		"""
		res = super(QGraphicsView,self).setOptimizationFlag(flag,enabled)
		return res
	#----------------------------------------------------------------------
	def setOptimizationFlags(self,flags):
		"""
		setOptimizationFlags(flags)
			flags=QtGui.QGraphicsView.OptimizationFlags

		This property holds flags that can be used to tune PySide.QtGui.QGraphicsView s performance..
		PySide.QtGui.QGraphicsView uses clipping, extra bounding rect adjustments, and certain other aids to improve rendering quality and performance for the common case graphics scene
		However, depending on the target platform, the scene, and the viewport in use, some of these operations can degrade performance.
		The effect varies from flag to flag; see the OptimizationFlags documentation for details.
		By default, no optimization flags are enabled.
		"""
		res = super(QGraphicsView,self).setOptimizationFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setRenderHint(self,hint,enabled=None):
		"""
		setRenderHint(hint,enabled=None)
			hint=QtGui.QPainter.RenderHint
			enabled=QtCore.bool


		"""
		res = super(QGraphicsView,self).setRenderHint(hint,enabled)
		return res
	#----------------------------------------------------------------------
	def setRenderHints(self,hints):
		"""
		setRenderHints(hints)
			hints=QtGui.QPainter.RenderHints

		This property holds the default render hints for the view.
		These hints are used to initialize PySide.QtGui.QPainter before each visible item is drawn
		PySide.QtGui.QPainter uses render hints to toggle rendering features such as antialiasing and smooth pixmap transformation.
		QPainter.TextAntialiasing is enabled by default.
		Example:
		"""
		res = super(QGraphicsView,self).setRenderHints(hints)
		return res
	#----------------------------------------------------------------------
	def setResizeAnchor(self,anchor):
		"""
		setResizeAnchor(anchor)
			anchor=QtGui.QGraphicsView.ViewportAnchor

		This property holds how the view should position the scene when the view is resized..
		PySide.QtGui.QGraphicsView uses this property to decide how to position the scene in the viewport when the viewport widgets size changes
		The default behavior, NoAnchor , leaves the scenes position unchanged during a resize; the top-left corner of the view will appear to be anchored while resizing.
		Note that the effect of this property is noticeable when only a part of the scene is visible (i.e., when there are scroll bars)
		Otherwise, if the whole scene fits in the view, PySide.QtGui.QGraphicsScene uses the view PySide.QtGui.QGraphicsView.alignment() to position the scene in the view.
		"""
		res = super(QGraphicsView,self).setResizeAnchor(anchor)
		return res
	#----------------------------------------------------------------------
	def setRubberBandSelectionMode(self,mode):
		"""
		setRubberBandSelectionMode(mode)
			mode=QtCore.Qt.ItemSelectionMode

		This property holds the behavior for selecting items with a rubber band selection rectangle..
		This property defines how items are selected when using the RubberBandDrag drag mode.
		The default value is Qt.IntersectsItemShape ; all items whose shape intersects with or is contained by the rubber band are selected.
		"""
		res = super(QGraphicsView,self).setRubberBandSelectionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setScene(self,scene):
		"""
		setScene(scene)
			scene=QtGui.QGraphicsScene

		Sets the current scene to scene
		If scene is already being viewed, this function does nothing.
		When a scene is set on a view, the QGraphicsScene.changed() signal is automatically connected to this views PySide.QtGui.QGraphicsView.updateScene() slot, and the views scroll bars are adjusted to fit the size of the scene.
		"""
		res = super(QGraphicsView,self).setScene(scene)
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
		res = super(QGraphicsView,self).setSceneRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setTransform(self,matrix,combine=None):
		"""
		setTransform(matrix,combine=None)
			matrix=QtGui.QTransform
			combine=QtCore.bool

		Sets the views current transformation matrix to matrix .
		If combine is true, then matrix is combined with the current matrix; otherwise, matrixreplaces the current matrix
		combine is false by default.
		The transformation matrix tranforms the scene into view coordinates
		Using the default transformation, provided by the identity matrix, one pixel in the view represents one unit in the scene (e.g., a 10x10 rectangular item is drawn using 10x10 pixels in the view)
		If a 2x2 scaling matrix is applied, the scene will be drawn in 1:2 (e.g., a 10x10 rectangular item is then drawn using 20x20 pixels in the view).
		Example:
		To simplify interation with items using a transformed view, PySide.QtGui.QGraphicsView provides mapTo..
		and mapFrom..
		functions that can translate between scene and view coordinates
		For example, you can call PySide.QtGui.QGraphicsView.mapToScene() to map a view coordiate to a floating point scene coordinate, or PySide.QtGui.QGraphicsView.mapFromScene() to map from floating point scene coordinates to view coordinates.
		"""
		res = super(QGraphicsView,self).setTransform(matrix,combine)
		return res
	#----------------------------------------------------------------------
	def setTransformationAnchor(self,anchor):
		"""
		setTransformationAnchor(anchor)
			anchor=QtGui.QGraphicsView.ViewportAnchor

		This property holds how the view should position the scene during transformations..
		PySide.QtGui.QGraphicsView uses this property to decide how to position the scene in the viewport when the transformation matrix changes, and the coordinate system of the view is transformed
		The default behavior, AnchorViewCenter , ensures that the scene point at the center of the view remains unchanged during transformations (e.g., when rotating, the scene will appear to rotate around the center of the view).
		Note that the effect of this property is noticeable when only a part of the scene is visible (i.e., when there are scroll bars)
		Otherwise, if the whole scene fits in the view, PySide.QtGui.QGraphicsScene uses the view PySide.QtGui.QGraphicsView.alignment() to position the scene in the view.
		"""
		res = super(QGraphicsView,self).setTransformationAnchor(anchor)
		return res
	#----------------------------------------------------------------------
	def setViewportUpdateMode(self,mode):
		"""
		setViewportUpdateMode(mode)
			mode=QtGui.QGraphicsView.ViewportUpdateMode

		This property holds how the viewport should update its contents..
		PySide.QtGui.QGraphicsView uses this property to decide how to update areas of the scene that have been reexposed or changed
		Usually you do not need to modify this property, but there are some cases where doing so can improve rendering performance
		See the QGraphicsView.ViewportUpdateMode documentation for specific details.
		The default value is MinimalViewportUpdate , where PySide.QtGui.QGraphicsView will update as small an area of the viewport as possible when the contents change.
		"""
		res = super(QGraphicsView,self).setViewportUpdateMode(mode)
		return res
	#----------------------------------------------------------------------
	def shear(self,sh,sv):
		"""
		shear(sh,sv)
			sh=QtCore.qreal
			sv=QtCore.qreal

		Shears the current view transformation by (sh , sv ).
		"""
		res = super(QGraphicsView,self).shear(sh,sv)
		return res
	#----------------------------------------------------------------------
	def translate(self,dx,dy):
		"""
		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Translates the current view transformation by (dx , dy ).
		"""
		res = super(QGraphicsView,self).translate(dx,dy)
		return res

	Alignment               = property(alignment)
	BackgroundBrush         = property(backgroundBrush)
	CacheMode               = property(cacheMode)
	DragMode                = property(dragMode)
	ForegroundBrush         = property(foregroundBrush)
	IsInteractive           = property(isInteractive)
	IsTransformed           = property(isTransformed)
	Items                   = property(items)
	Matrix                  = property(matrix)
	OptimizationFlags       = property(optimizationFlags)
	RenderHints             = property(renderHints)
	ResetCachedContent      = property(resetCachedContent)
	ResetMatrix             = property(resetMatrix)
	ResetTransform          = property(resetTransform)
	ResizeAnchor            = property(resizeAnchor)
	RubberBandSelectionMode = property(rubberBandSelectionMode)
	Scene                   = property(scene)
	SceneRect               = property(sceneRect)
	Transform               = property(transform)
	TransformationAnchor    = property(transformationAnchor)
	ViewportTransform       = property(viewportTransform)
	ViewportUpdateMode      = property(viewportUpdateMode)