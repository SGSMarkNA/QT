from PySide import QtGui, QtCore

class QPainter(QtGui.QPainter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPainter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the current background brush.
		"""
		res = super(QPainter,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def backgroundMode(self):
		"""
		Returns the current background mode.
		"""
		res = super(QPainter,self).backgroundMode()
		isinstance(res,QtCore.Qt.BGMode)
		return res
	#----------------------------------------------------------------------
	def beginNativePainting(self):
		"""
		Flushes the painting pipeline and prepares for the user issuing commands directly to the underlying graphics context
		Must be followed by a call to PySide.QtGui.QPainter.endNativePainting() .
		Note that only the states the underlying paint engine changes will be reset to their respective default states
		The states we reset may change from release to release
		The following states are currently reset in the OpenGL 2 engine:
		If, for example, the OpenGL polygon mode is changed by the user inside a beginNativePaint()/ PySide.QtGui.QPainter.endNativePainting() block, it will not be reset to the default state by PySide.QtGui.QPainter.endNativePainting()
		Here is an example that shows intermixing of painter commands and raw OpenGL commands:
		"""
		res = super(QPainter,self).beginNativePainting()
		return res
	#----------------------------------------------------------------------
	def brush(self):
		"""
		Returns the painters current brush.
		"""
		res = super(QPainter,self).brush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def brushOrigin(self):
		"""
		Returns the currently set brush origin.
		"""
		res = super(QPainter,self).brushOrigin()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def clipPath(self):
		"""
		Returns the currently clip as a path
		Note that the clip path is given in logical coordinates.
		"""
		res = super(QPainter,self).clipPath()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def clipRegion(self):
		"""
		Returns the currently set clip region
		Note that the clip region is given in logical coordinates.
		"""
		res = super(QPainter,self).clipRegion()
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def combinedMatrix(self):
		"""
		Returns the transformation matrix combining the current window/viewport and world transformation.
		It is advisable to use PySide.QtGui.QPainter.combinedTransform() instead of this function to preserve the properties of perspective transformations.
		"""
		res = super(QPainter,self).combinedMatrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def combinedTransform(self):
		"""
		Returns the transformation matrix combining the current window/viewport and world transformation.
		"""
		res = super(QPainter,self).combinedTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def compositionMode(self):
		"""
		Returns the current composition mode.
		"""
		res = super(QPainter,self).compositionMode()
		isinstance(res,QtGui.QPainter.CompositionMode)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the paint device on which this painter is currently painting, or 0 if the painter is not active.
		"""
		res = super(QPainter,self).device()
		isinstance(res,QtGui.QPaintDevice)
		return res
	#----------------------------------------------------------------------
	def deviceMatrix(self):
		"""
		Returns the matrix that transforms from logical coordinates to device coordinates of the platform dependent paint device.
		This function is only needed when using platform painting commands on the platform dependent handle ( Qt.HANDLE ), and the platform does not do transformations nativly.
		The QPaintEngine.PaintEngineFeature enum can be queried to determine whether the platform performs the transformations or not.
		"""
		res = super(QPainter,self).deviceMatrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def deviceTransform(self):
		"""
		Returns the matrix that transforms from logical coordinates to device coordinates of the platform dependent paint device.
		This function is only needed when using platform painting commands on the platform dependent handle ( Qt.HANDLE ), and the platform does not do transformations nativly.
		The QPaintEngine.PaintEngineFeature enum can be queried to determine whether the platform performs the transformations or not.
		"""
		res = super(QPainter,self).deviceTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def end(self):
		"""
		Ends painting
		Any resources used while painting are released
		You dont normally need to call this since it is called by the destructor.
		Returns true if the painter is no longer active; otherwise returns false.
		"""
		res = super(QPainter,self).end()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def endNativePainting(self):
		"""
		Restores the painter after manually issuing native painting commands
		Lets the painter restore any native state that it relies on before calling any other painter commands.
		"""
		res = super(QPainter,self).endNativePainting()
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the currently set font used for drawing text.
		"""
		res = super(QPainter,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def fontInfo(self):
		"""
		Returns the font info for the painter if the painter is active
		Otherwise, the return value is undefined.
		"""
		res = super(QPainter,self).fontInfo()
		isinstance(res,QtGui.QFontInfo)
		return res
	#----------------------------------------------------------------------
	def fontMetrics(self):
		"""
		Returns the font metrics for the painter if the painter is active
		Otherwise, the return value is undefined.
		"""
		res = super(QPainter,self).fontMetrics()
		isinstance(res,QtGui.QFontMetrics)
		return res
	#----------------------------------------------------------------------
	def hasClipping(self):
		"""
		Returns true if clipping has been set; otherwise returns false.
		"""
		res = super(QPainter,self).hasClipping()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if PySide.QtGui.QPainter.begin() has been called and PySide.QtGui.QPainter.end() has not yet been called; otherwise returns false.
		"""
		res = super(QPainter,self).isActive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def layoutDirection(self):
		"""
		Returns the layout direction used by the painter when drawing text.
		"""
		res = super(QPainter,self).layoutDirection()
		isinstance(res,QtCore.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def opacity(self):
		"""
		Returns the opacity of the painter
		The default value is 1.
		"""
		res = super(QPainter,self).opacity()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def paintEngine(self):
		"""
		Returns the paint engine that the painter is currently operating on if the painter is active; otherwise 0.
		"""
		res = super(QPainter,self).paintEngine()
		isinstance(res,QtGui.QPaintEngine)
		return res
	#----------------------------------------------------------------------
	def pen(self):
		"""
		Returns the painters current pen.
		"""
		res = super(QPainter,self).pen()
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def renderHints(self):
		"""
		Returns a flag that specifies the rendering hints that are set for this painter.
		"""
		res = super(QPainter,self).renderHints()
		isinstance(res,QtGui.QPainter.RenderHints)
		return res
	#----------------------------------------------------------------------
	def resetMatrix(self):
		"""
		Resets any transformations that were made using PySide.QtGui.QPainter.translate() , PySide.QtGui.QPainter.scale() , PySide.QtGui.QPainter.shear() , PySide.QtGui.QPainter.rotate() , PySide.QtGui.QPainter.setWorldMatrix() , PySide.QtGui.QPainter.setViewport() and PySide.QtGui.QPainter.setWindow() .
		It is advisable to use PySide.QtGui.QPainter.resetTransform() instead of this function to preserve the properties of perspective transformations.
		"""
		res = super(QPainter,self).resetMatrix()
		return res
	#----------------------------------------------------------------------
	def resetTransform(self):
		"""
		Resets any transformations that were made using PySide.QtGui.QPainter.translate() , PySide.QtGui.QPainter.scale() , PySide.QtGui.QPainter.shear() , PySide.QtGui.QPainter.rotate() , PySide.QtGui.QPainter.setWorldTransform() , PySide.QtGui.QPainter.setViewport() and PySide.QtGui.QPainter.setWindow() .
		"""
		res = super(QPainter,self).resetTransform()
		return res
	#----------------------------------------------------------------------
	def restore(self):
		"""
		Restores the current painter state (pops a saved state off the stack).
		"""
		res = super(QPainter,self).restore()
		return res
	#----------------------------------------------------------------------
	def save(self):
		"""
		Saves the current painter state (pushes the state onto a stack)
		A PySide.QtGui.QPainter.save() must be followed by a corresponding PySide.QtGui.QPainter.restore() ; the PySide.QtGui.QPainter.end() function unwinds the stack.
		"""
		res = super(QPainter,self).save()
		return res
	#----------------------------------------------------------------------
	def transform(self):
		"""
		Returns the world transformation matrix.
		"""
		res = super(QPainter,self).transform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def viewTransformEnabled(self):
		"""
		Returns true if view transformation is enabled; otherwise returns false.
		"""
		res = super(QPainter,self).viewTransformEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def viewport(self):
		"""
		Returns the viewport rectangle.
		"""
		res = super(QPainter,self).viewport()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def window(self):
		"""
		Returns the window rectangle.
		"""
		res = super(QPainter,self).window()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def worldMatrix(self):
		"""
		Returns the world transformation matrix.
		It is advisable to use PySide.QtGui.QPainter.worldTransform() because PySide.QtGui.QPainter.worldMatrix() does not preserve the properties of perspective transformations.
		"""
		res = super(QPainter,self).worldMatrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def worldMatrixEnabled(self):
		"""
		Returns true if world transformation is enabled; otherwise returns false.
		"""
		res = super(QPainter,self).worldMatrixEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def worldTransform(self):
		"""
		Returns the world transformation matrix.
		"""
		res = super(QPainter,self).worldTransform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def begin(self,arg__1):
		"""
		begin(arg__1)
			arg__1=QtGui.QPaintDevice

		Begins painting the paint device and returns true if successful; otherwise returns false.
		Notice that all painter settings ( PySide.QtGui.QPainter.setPen() , PySide.QtGui.QPainter.setBrush() etc.) are reset to default values when PySide.QtGui.QPainter.begin() is called.
		The errors that can occur are serious problems, such as these:
		Note that most of the time, you can use one of the constructors instead of PySide.QtGui.QPainter.begin() , and that PySide.QtGui.QPainter.end() is automatically done at destruction.
		"""
		res = super(QPainter,self).begin(arg__1)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def boundingRect(self,*args,**kwargs):
		"""
		boundingRect(x,y,w,h,flags,text)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			flags=QtCore.int
			text=unicode

		boundingRect(rect,flags,text)
			rect=QtCore.QRectF
			flags=QtCore.int
			text=unicode

		boundingRect(rect,flags,text)
			rect=QtCore.QRect
			flags=QtCore.int
			text=unicode

		boundingRect(rect,text,o=None)
			rect=QtCore.QRectF
			text=unicode
			o=QtGui.QTextOption

		This is an overloaded function.
		Returns the bounding rectangle of the given text as it will appear when drawn inside the rectangle beginning at the point (x , y ) with width w and height h .
		"""
		res = super(QPainter,self).boundingRect(*args,**kwargs)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def drawArc(self,*args,**kwargs):
		"""
		drawArc(rect,a,alen)
			rect=QtCore.QRectF
			a=QtCore.int
			alen=QtCore.int

		drawArc(x,y,w,h,a,alen)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			a=QtCore.int
			alen=QtCore.int

		drawArc(arg__1,a,alen)
			arg__1=QtCore.QRect
			a=QtCore.int
			alen=QtCore.int

		Draws the arc defined by the given rectangle , startAngle and spanAngle .
		The startAngle and spanAngle must be specified in 1/16th of a degree, i.e
		a full circle equals 5760 (16 * 360)
		Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction
		Zero degrees is at the 3 oclock position.
		"""
		res = super(QPainter,self).drawArc(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawChord(self,*args,**kwargs):
		"""
		drawChord(rect,a,alen)
			rect=QtCore.QRectF
			a=QtCore.int
			alen=QtCore.int

		drawChord(x,y,w,h,a,alen)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			a=QtCore.int
			alen=QtCore.int

		drawChord(arg__1,a,alen)
			arg__1=QtCore.QRect
			a=QtCore.int
			alen=QtCore.int

		Draws the chord defined by the given rectangle , startAngle and spanAngle
		The chord is filled with the current PySide.QtGui.QPainter.brush() .
		The startAngle and spanAngle must be specified in 1/16th of a degree, i.e
		a full circle equals 5760 (16 * 360)
		Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction
		Zero degrees is at the 3 oclock position.
		"""
		res = super(QPainter,self).drawChord(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawConvexPolygon(self,*args,**kwargs):
		"""
		drawConvexPolygon(polygon)
			polygon=QtGui.QPolygon

		drawConvexPolygon(polygon)
			polygon=QtGui.QPolygonF

		drawConvexPolygon(arg__1)
			arg__1=unKnown

		drawConvexPolygon(arg__1)
			arg__1=unKnown

		This is an overloaded function.
		Draws the convex polygon defined by polygon using the current pen and brush.
		"""
		res = super(QPainter,self).drawConvexPolygon(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawEllipse(self,*args,**kwargs):
		"""
		drawEllipse(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		drawEllipse(r)
			r=QtCore.QRect

		drawEllipse(r)
			r=QtCore.QRectF

		drawEllipse(center,rx,ry)
			center=QtCore.QPointF
			rx=QtCore.qreal
			ry=QtCore.qreal

		drawEllipse(center,rx,ry)
			center=QtCore.QPoint
			rx=QtCore.int
			ry=QtCore.int

		This is an overloaded function.
		Draws the ellipse defined by the rectangle beginning at (x , y ) with the given width and height .
		"""
		res = super(QPainter,self).drawEllipse(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawImage(self,*args,**kwargs):
		"""
		drawImage(r,image)
			r=QtCore.QRectF
			image=QtGui.QImage

		drawImage(targetRect,image,sourceRect,flags=None)
			targetRect=QtCore.QRectF
			image=QtGui.QImage
			sourceRect=QtCore.QRectF
			flags=QtCore.Qt.ImageConversionFlags

		drawImage(x,y,image,sx=None,sy=None,sw=None,sh=None,flags=None)
			x=QtCore.int
			y=QtCore.int
			image=QtGui.QImage
			sx=QtCore.int
			sy=QtCore.int
			sw=QtCore.int
			sh=QtCore.int
			flags=QtCore.Qt.ImageConversionFlags

		drawImage(r,image)
			r=QtCore.QRect
			image=QtGui.QImage

		drawImage(targetRect,image,sourceRect,flags=None)
			targetRect=QtCore.QRect
			image=QtGui.QImage
			sourceRect=QtCore.QRect
			flags=QtCore.Qt.ImageConversionFlags

		drawImage(p,image,sr,flags=None)
			p=QtCore.QPoint
			image=QtGui.QImage
			sr=QtCore.QRect
			flags=QtCore.Qt.ImageConversionFlags

		drawImage(p,image)
			p=QtCore.QPoint
			image=QtGui.QImage

		drawImage(p,image)
			p=QtCore.QPointF
			image=QtGui.QImage

		drawImage(p,image,sr,flags=None)
			p=QtCore.QPointF
			image=QtGui.QImage
			sr=QtCore.QRectF
			flags=QtCore.Qt.ImageConversionFlags

		This is an overloaded function.
		Draws the given image into the given rectangle .
		"""
		res = super(QPainter,self).drawImage(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawLine(self,*args,**kwargs):
		"""
		drawLine(x1,y1,x2,y2)
			x1=QtCore.int
			y1=QtCore.int
			x2=QtCore.int
			y2=QtCore.int

		drawLine(p1,p2)
			p1=QtCore.QPointF
			p2=QtCore.QPointF

		drawLine(p1,p2)
			p1=QtCore.QPoint
			p2=QtCore.QPoint

		drawLine(line)
			line=QtCore.QLineF

		drawLine(line)
			line=QtCore.QLine

		This is an overloaded function.
		Draws a line from (x1 , y1 ) to (x2 , y2 ) and sets the current pen position to (x2 , y2 ).
		"""
		res = super(QPainter,self).drawLine(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawLines(self,*args,**kwargs):
		"""
		drawLines(lines)
			lines=unKnown

		drawLines(pointPairs)
			pointPairs=unKnown

		drawLines(pointPairs)
			pointPairs=unKnown

		drawLines(lines)
			lines=unKnown


		"""
		res = super(QPainter,self).drawLines(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPath(self,path):
		"""
		drawPath(path)
			path=QtGui.QPainterPath

		Draws the given painter path using the current pen for outline and the current brush for filling.
		"""
		res = super(QPainter,self).drawPath(path)
		return res
	#----------------------------------------------------------------------
	def drawPicture(self,*args,**kwargs):
		"""
		drawPicture(x,y,picture)
			x=QtCore.int
			y=QtCore.int
			picture=QtGui.QPicture

		drawPicture(p,picture)
			p=QtCore.QPointF
			picture=QtGui.QPicture

		drawPicture(p,picture)
			p=QtCore.QPoint
			picture=QtGui.QPicture

		This is an overloaded function.
		Draws the given picture at point (x , y ).
		"""
		res = super(QPainter,self).drawPicture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPie(self,*args,**kwargs):
		"""
		drawPie(x,y,w,h,a,alen)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			a=QtCore.int
			alen=QtCore.int

		drawPie(rect,a,alen)
			rect=QtCore.QRectF
			a=QtCore.int
			alen=QtCore.int

		drawPie(arg__1,a,alen)
			arg__1=QtCore.QRect
			a=QtCore.int
			alen=QtCore.int

		This is an overloaded function.
		Draws the pie defined by the rectangle beginning at (x , y ) with the specified width and height , and the given startAngle and spanAngle .
		"""
		res = super(QPainter,self).drawPie(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPixmap(self,*args,**kwargs):
		"""
		drawPixmap(x,y,pm)
			x=QtCore.int
			y=QtCore.int
			pm=QtGui.QPixmap

		drawPixmap(targetRect,pixmap,sourceRect)
			targetRect=QtCore.QRectF
			pixmap=QtGui.QPixmap
			sourceRect=QtCore.QRectF

		drawPixmap(x,y,pm,sx,sy,sw,sh)
			x=QtCore.int
			y=QtCore.int
			pm=QtGui.QPixmap
			sx=QtCore.int
			sy=QtCore.int
			sw=QtCore.int
			sh=QtCore.int

		drawPixmap(x,y,w,h,pm,sx,sy,sw,sh)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			pm=QtGui.QPixmap
			sx=QtCore.int
			sy=QtCore.int
			sw=QtCore.int
			sh=QtCore.int

		drawPixmap(x,y,w,h,pm)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			pm=QtGui.QPixmap

		drawPixmap(r,pm)
			r=QtCore.QRect
			pm=QtGui.QPixmap

		drawPixmap(p,pm)
			p=QtCore.QPoint
			pm=QtGui.QPixmap

		drawPixmap(p,pm)
			p=QtCore.QPointF
			pm=QtGui.QPixmap

		drawPixmap(p,pm,sr)
			p=QtCore.QPoint
			pm=QtGui.QPixmap
			sr=QtCore.QRect

		drawPixmap(p,pm,sr)
			p=QtCore.QPointF
			pm=QtGui.QPixmap
			sr=QtCore.QRectF

		drawPixmap(targetRect,pixmap,sourceRect)
			targetRect=QtCore.QRect
			pixmap=QtGui.QPixmap
			sourceRect=QtCore.QRect

		This is an overloaded function.
		Draws the given pixmap at position (x , y ).
		"""
		res = super(QPainter,self).drawPixmap(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPoint(self,*args,**kwargs):
		"""
		drawPoint(x,y)
			x=QtCore.int
			y=QtCore.int

		drawPoint(p)
			p=QtCore.QPoint

		drawPoint(pt)
			pt=QtCore.QPointF

		This is an overloaded function.
		Draws a single point at position (x , y ).
		"""
		res = super(QPainter,self).drawPoint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPoints(self,*args,**kwargs):
		"""
		drawPoints(points)
			points=QtGui.QPolygon

		drawPoints(points)
			points=QtGui.QPolygonF

		drawPoints(arg__1)
			arg__1=unKnown

		drawPoints(arg__1)
			arg__1=unKnown

		This is an overloaded function.
		Draws the points in the vector points .
		"""
		res = super(QPainter,self).drawPoints(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPolygon(self,*args,**kwargs):
		"""
		drawPolygon(polygon,fillRule=None)
			polygon=QtGui.QPolygonF
			fillRule=QtCore.Qt.FillRule

		drawPolygon(polygon,fillRule=None)
			polygon=QtGui.QPolygon
			fillRule=QtCore.Qt.FillRule

		drawPolygon(arg__1,arg__2)
			arg__1=unKnown
			arg__2=QtCore.Qt.FillRule

		drawPolygon(arg__1,arg__2)
			arg__1=unKnown
			arg__2=QtCore.Qt.FillRule


		"""
		res = super(QPainter,self).drawPolygon(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPolyline(self,*args,**kwargs):
		"""
		drawPolyline(polyline)
			polyline=QtGui.QPolygonF

		drawPolyline(polygon)
			polygon=QtGui.QPolygon

		drawPolyline(arg__1)
			arg__1=unKnown

		drawPolyline(arg__1)
			arg__1=unKnown

		This is an overloaded function.
		Draws the polyline defined by the given points using the current pen.
		"""
		res = super(QPainter,self).drawPolyline(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawRect(self,*args,**kwargs):
		"""
		drawRect(rect)
			rect=QtCore.QRectF

		drawRect(x1,y1,w,h)
			x1=QtCore.int
			y1=QtCore.int
			w=QtCore.int
			h=QtCore.int

		drawRect(rect)
			rect=QtCore.QRect

		Draws the current rectangle with the current pen and brush.
		A filled rectangle has a size of rectangle
		size()
		A stroked rectangle has a size of rectangle
		size() plus the pen width.
		"""
		res = super(QPainter,self).drawRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawRects(self,*args,**kwargs):
		"""
		drawRects(rectangles)
			rectangles=unKnown

		drawRects(rectangles)
			rectangles=unKnown


		"""
		res = super(QPainter,self).drawRects(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawRoundRect(self,*args,**kwargs):
		"""
		drawRoundRect(x,y,w,h,xRound=None,yRound=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			xRound=QtCore.int
			yRound=QtCore.int

		drawRoundRect(r,xround=None,yround=None)
			r=QtCore.QRect
			xround=QtCore.int
			yround=QtCore.int

		drawRoundRect(r,xround=None,yround=None)
			r=QtCore.QRectF
			xround=QtCore.int
			yround=QtCore.int

		This is an overloaded function.
		Draws the rectangle x , y , w , h with rounded corners.
		"""
		res = super(QPainter,self).drawRoundRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawRoundedRect(self,*args,**kwargs):
		"""
		drawRoundedRect(rect,xRadius,yRadius,mode=None)
			rect=QtCore.QRectF
			xRadius=QtCore.qreal
			yRadius=QtCore.qreal
			mode=QtCore.Qt.SizeMode

		drawRoundedRect(x,y,w,h,xRadius,yRadius,mode=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			xRadius=QtCore.qreal
			yRadius=QtCore.qreal
			mode=QtCore.Qt.SizeMode

		drawRoundedRect(rect,xRadius,yRadius,mode=None)
			rect=QtCore.QRect
			xRadius=QtCore.qreal
			yRadius=QtCore.qreal
			mode=QtCore.Qt.SizeMode


		"""
		res = super(QPainter,self).drawRoundedRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawText(self,*args,**kwargs):
		"""
		drawText(r,flags,text)
			r=QtCore.QRectF
			flags=QtCore.int
			text=unicode

		drawText(x,y,s)
			x=QtCore.int
			y=QtCore.int
			s=unicode

		drawText(x,y,w,h,flags,text)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			flags=QtCore.int
			text=unicode

		drawText(r,text,o=None)
			r=QtCore.QRectF
			text=unicode
			o=QtGui.QTextOption

		drawText(p,s)
			p=QtCore.QPoint
			s=unicode

		drawText(p,s)
			p=QtCore.QPointF
			s=unicode

		drawText(r,flags,text)
			r=QtCore.QRect
			flags=QtCore.int
			text=unicode

		This is an overloaded function.
		Draws the given text within the provided rectangle .
		The boundingRect (if not null) is set to the what the bounding rectangle should be in order to enclose the whole text
		The flags argument is a bitwise OR of the following flags:
		By default, PySide.QtGui.QPainter draws text anti-aliased.
		"""
		res = super(QPainter,self).drawText(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawTextItem(self,*args,**kwargs):
		"""
		drawTextItem(x,y,ti)
			x=QtCore.int
			y=QtCore.int
			ti=QtGui.QTextItem

		drawTextItem(p,ti)
			p=QtCore.QPoint
			ti=QtGui.QTextItem

		drawTextItem(p,ti)
			p=QtCore.QPointF
			ti=QtGui.QTextItem

		This is an overloaded function.
		"""
		res = super(QPainter,self).drawTextItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawTiledPixmap(self,*args,**kwargs):
		"""
		drawTiledPixmap(x,y,w,h,arg__5,sx=None,sy=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			arg__5=QtGui.QPixmap
			sx=QtCore.int
			sy=QtCore.int

		drawTiledPixmap(arg__1,arg__2,pos=None)
			arg__1=QtCore.QRect
			arg__2=QtGui.QPixmap
			pos=QtCore.QPoint

		drawTiledPixmap(rect,pm,offset=None)
			rect=QtCore.QRectF
			pm=QtGui.QPixmap
			offset=QtCore.QPointF

		This is an overloaded function.
		Draws a tiled pixmap in the specified rectangle.
		(x , y ) specifies the top-left point in the paint device that is to be drawn onto; with the given width and height
		(sx , sy ) specifies the top-left point in the pixmap that is to be drawn; this defaults to (0, 0).
		"""
		res = super(QPainter,self).drawTiledPixmap(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def eraseRect(self,*args,**kwargs):
		"""
		eraseRect(arg__1)
			arg__1=QtCore.QRectF

		eraseRect(arg__1)
			arg__1=QtCore.QRect

		eraseRect(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		Erases the area inside the given rectangle
		Equivalent to calling
		"""
		res = super(QPainter,self).eraseRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def fillPath(self,path,brush):
		"""
		fillPath(path,brush)
			path=QtGui.QPainterPath
			brush=QtGui.QBrush

		Fills the given path using the given brush
		The outline is not drawn.
		Alternatively, you can specify a PySide.QtGui.QColor instead of a PySide.QtGui.QBrush ; the PySide.QtGui.QBrush constructor (taking a PySide.QtGui.QColor argument) will automatically create a solid pattern brush.
		"""
		res = super(QPainter,self).fillPath(path,brush)
		return res
	#----------------------------------------------------------------------
	def fillRect(self,*args,**kwargs):
		"""
		fillRect(r,c)
			r=QtCore.QRectF
			c=QtCore.Qt.GlobalColor

		fillRect(r,style)
			r=QtCore.QRectF
			style=QtCore.Qt.BrushStyle

		fillRect(x,y,w,h,style)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			style=QtCore.Qt.BrushStyle

		fillRect(x,y,w,h,arg__5)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			arg__5=QtGui.QBrush

		fillRect(x,y,w,h,color)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			color=QtGui.QColor

		fillRect(x,y,w,h,c)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			c=QtCore.Qt.GlobalColor

		fillRect(r,style)
			r=QtCore.QRect
			style=QtCore.Qt.BrushStyle

		fillRect(arg__1,arg__2)
			arg__1=QtCore.QRect
			arg__2=QtGui.QBrush

		fillRect(arg__1,color)
			arg__1=QtCore.QRect
			color=QtGui.QColor

		fillRect(arg__1,color)
			arg__1=QtCore.QRectF
			color=QtGui.QColor

		fillRect(r,c)
			r=QtCore.QRect
			c=QtCore.Qt.GlobalColor

		fillRect(arg__1,arg__2)
			arg__1=QtCore.QRectF
			arg__2=QtGui.QBrush


		"""
		res = super(QPainter,self).fillRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def initFrom(self,widget):
		"""
		initFrom(widget)
			widget=QtGui.QWidget

		Initializes the painters pen, background and font to the same as the given widget
		This function is called automatically when the painter is opened on a PySide.QtGui.QWidget .
		"""
		res = super(QPainter,self).initFrom(widget)
		return res
	#----------------------------------------------------------------------
	def rotate(self,a):
		"""
		rotate(a)
			a=QtCore.qreal

		Rotates the coordinate system the given angle clockwise.
		"""
		res = super(QPainter,self).rotate(a)
		return res
	#----------------------------------------------------------------------
	def scale(self,sx,sy):
		"""
		scale(sx,sy)
			sx=QtCore.qreal
			sy=QtCore.qreal

		Scales the coordinate system by (sx , sy ).
		"""
		res = super(QPainter,self).scale(sx,sy)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,bg):
		"""
		setBackground(bg)
			bg=QtGui.QBrush

		Sets the background brush of the painter to the given brush .
		The background brush is the brush that is filled in when drawing opaque text, stippled lines and bitmaps
		The background brush has no effect in transparent background mode (which is the default).
		"""
		res = super(QPainter,self).setBackground(bg)
		return res
	#----------------------------------------------------------------------
	def setBackgroundMode(self,mode):
		"""
		setBackgroundMode(mode)
			mode=QtCore.Qt.BGMode


		"""
		res = super(QPainter,self).setBackgroundMode(mode)
		return res
	#----------------------------------------------------------------------
	def setBrush(self,*args,**kwargs):
		"""
		setBrush(style)
			style=QtCore.Qt.BrushStyle

		setBrush(brush)
			brush=QtGui.QBrush


		"""
		res = super(QPainter,self).setBrush(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setBrushOrigin(self,*args,**kwargs):
		"""
		setBrushOrigin(arg__1)
			arg__1=QtCore.QPointF

		setBrushOrigin(arg__1)
			arg__1=QtCore.QPoint

		setBrushOrigin(x,y)
			x=QtCore.int
			y=QtCore.int

		Sets the brush origin to position .
		The brush origin specifies the (0, 0) coordinate of the painters brush.
		Note that while the PySide.QtGui.QPainter.brushOrigin() was necessary to adopt the parents background for a widget in Qt 3, this is no longer the case since the Qt 4 painter doesnt paint the background unless you explicitly tell it to do so by setting the widgets PySide.QtGui.QWidget.autoFillBackground() property to true.
		"""
		res = super(QPainter,self).setBrushOrigin(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setClipPath(self,path,op=None):
		"""
		setClipPath(path,op=None)
			path=QtGui.QPainterPath
			op=QtCore.Qt.ClipOperation


		"""
		res = super(QPainter,self).setClipPath(path,op)
		return res
	#----------------------------------------------------------------------
	def setClipRect(self,*args,**kwargs):
		"""
		setClipRect(arg__1,op=None)
			arg__1=QtCore.QRect
			op=QtCore.Qt.ClipOperation

		setClipRect(arg__1,op=None)
			arg__1=QtCore.QRectF
			op=QtCore.Qt.ClipOperation

		setClipRect(x,y,w,h,op=None)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			op=QtCore.Qt.ClipOperation


		"""
		res = super(QPainter,self).setClipRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setClipRegion(self,arg__1,op=None):
		"""
		setClipRegion(arg__1,op=None)
			arg__1=QtGui.QRegion
			op=QtCore.Qt.ClipOperation


		"""
		res = super(QPainter,self).setClipRegion(arg__1,op)
		return res
	#----------------------------------------------------------------------
	def setClipping(self,enable):
		"""
		setClipping(enable)
			enable=QtCore.bool

		Enables clipping if enable is true, or disables clipping if enable is false.
		"""
		res = super(QPainter,self).setClipping(enable)
		return res
	#----------------------------------------------------------------------
	def setCompositionMode(self,mode):
		"""
		setCompositionMode(mode)
			mode=QtGui.QPainter.CompositionMode

		Sets the composition mode to the given mode .
		"""
		res = super(QPainter,self).setCompositionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setFont(self,f):
		"""
		setFont(f)
			f=QtGui.QFont

		Sets the painters font to the given font .
		This font is used by subsequent PySide.QtGui.QPainter.drawText() functions
		The text color is the same as the pen color.
		If you set a font that isnt available, Qt finds a close match
		PySide.QtGui.QPainter.font() will return what you set using PySide.QtGui.QPainter.setFont() and PySide.QtGui.QPainter.fontInfo() returns the font actually being used (which may be the same).
		"""
		res = super(QPainter,self).setFont(f)
		return res
	#----------------------------------------------------------------------
	def setLayoutDirection(self,direction):
		"""
		setLayoutDirection(direction)
			direction=QtCore.Qt.LayoutDirection


		"""
		res = super(QPainter,self).setLayoutDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setOpacity(self,opacity):
		"""
		setOpacity(opacity)
			opacity=QtCore.qreal

		Sets the opacity of the painter to opacity
		The value should be in the range 0.0 to 1.0, where 0.0 is fully transparent and 1.0 is fully opaque.
		Opacity set on the painter will apply to all drawing operations individually.
		"""
		res = super(QPainter,self).setOpacity(opacity)
		return res
	#----------------------------------------------------------------------
	def setPen(self,*args,**kwargs):
		"""
		setPen(color)
			color=QtGui.QColor

		setPen(pen)
			pen=QtGui.QPen

		setPen(style)
			style=QtCore.Qt.PenStyle

		This is an overloaded function.
		Sets the painters pen to have style Qt.SolidLine , width 0 and the specified color .
		"""
		res = super(QPainter,self).setPen(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setRenderHint(self,hint,on=None):
		"""
		setRenderHint(hint,on=None)
			hint=QtGui.QPainter.RenderHint
			on=QtCore.bool

		Sets the given render hint on the painter if on is true; otherwise clears the render hint.
		"""
		res = super(QPainter,self).setRenderHint(hint,on)
		return res
	#----------------------------------------------------------------------
	def setRenderHints(self,hints,on=None):
		"""
		setRenderHints(hints,on=None)
			hints=QtGui.QPainter.RenderHints
			on=QtCore.bool


		"""
		res = super(QPainter,self).setRenderHints(hints,on)
		return res
	#----------------------------------------------------------------------
	def setTransform(self,transform,combine=None):
		"""
		setTransform(transform,combine=None)
			transform=QtGui.QTransform
			combine=QtCore.bool

		Sets the world transformation matrix
		If combine is true, the specified transform is combined with the current matrix; otherwise it replaces the current matrix.
		"""
		res = super(QPainter,self).setTransform(transform,combine)
		return res
	#----------------------------------------------------------------------
	def setViewTransformEnabled(self,enable):
		"""
		setViewTransformEnabled(enable)
			enable=QtCore.bool

		Enables view transformations if enable is true, or disables view transformations if enable is false.
		"""
		res = super(QPainter,self).setViewTransformEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setViewport(self,*args,**kwargs):
		"""
		setViewport(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		setViewport(viewport)
			viewport=QtCore.QRect

		This is an overloaded function.
		Sets the painters viewport rectangle to be the rectangle beginning at (x , y ) with the given width and height .
		"""
		res = super(QPainter,self).setViewport(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setWindow(self,*args,**kwargs):
		"""
		setWindow(window)
			window=QtCore.QRect

		setWindow(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		Sets the painters window to the given rectangle , and enables view transformations.
		The window rectangle is part of the view transformation
		The window specifies the logical coordinate system
		Its sister, the PySide.QtGui.QPainter.viewport() , specifies the device coordinate system.
		The default window rectangle is the same as the devices rectangle.
		"""
		res = super(QPainter,self).setWindow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setWorldMatrix(self,matrix,combine=None):
		"""
		setWorldMatrix(matrix,combine=None)
			matrix=QtGui.QMatrix
			combine=QtCore.bool

		Sets the transformation matrix to matrix and enables transformations.
		If combine is true, then matrix is combined with the current transformation matrix; otherwise matrix replaces the current transformation matrix.
		If matrix is the identity matrix and combine is false, this function calls setWorldMatrixEnabled(false)
		(The identity matrix is the matrix where QMatrix.m11() and QMatrix.m22() are 1.0 and the rest are 0.0.)
		The following functions can transform the coordinate system without using a PySide.QtGui.QMatrix :
		They operate on the painters PySide.QtGui.QPainter.worldMatrix() and are implemented like this:
		Note that when using PySide.QtGui.QPainter.setWorldMatrix() function you should always have combine be true when you are drawing into a PySide.QtGui.QPicture
		Otherwise it may not be possible to replay the picture with additional transformations; using the PySide.QtGui.QPainter.translate() , PySide.QtGui.QPainter.scale() , etc
		convenience functions is safe.
		For more information about the coordinate system, transformations and window-viewport conversion, see Coordinate System .
		"""
		res = super(QPainter,self).setWorldMatrix(matrix,combine)
		return res
	#----------------------------------------------------------------------
	def setWorldMatrixEnabled(self,enabled):
		"""
		setWorldMatrixEnabled(enabled)
			enabled=QtCore.bool

		Enables transformations if enable is true, or disables transformations if enable is false
		The world transformation matrix is not changed.
		"""
		res = super(QPainter,self).setWorldMatrixEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def setWorldTransform(self,matrix,combine=None):
		"""
		setWorldTransform(matrix,combine=None)
			matrix=QtGui.QTransform
			combine=QtCore.bool

		Sets the world transformation matrix
		If combine is true, the specified matrix is combined with the current matrix; otherwise it replaces the current matrix.
		"""
		res = super(QPainter,self).setWorldTransform(matrix,combine)
		return res
	#----------------------------------------------------------------------
	def shear(self,sh,sv):
		"""
		shear(sh,sv)
			sh=QtCore.qreal
			sv=QtCore.qreal

		Shears the coordinate system by (sh , sv ).
		"""
		res = super(QPainter,self).shear(sh,sv)
		return res
	#----------------------------------------------------------------------
	def strokePath(self,path,pen):
		"""
		strokePath(path,pen)
			path=QtGui.QPainterPath
			pen=QtGui.QPen

		Draws the outline (strokes) the path path with the pen specified by pen
		"""
		res = super(QPainter,self).strokePath(path,pen)
		return res
	#----------------------------------------------------------------------
	def testRenderHint(self,hint):
		"""
		testRenderHint(hint)
			hint=QtGui.QPainter.RenderHint

		Returns true if hint is set; otherwise returns false.
		"""
		res = super(QPainter,self).testRenderHint(hint)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(offset)
			offset=QtCore.QPointF

		translate(offset)
			offset=QtCore.QPoint

		translate(dx,dy)
			dx=QtCore.qreal
			dy=QtCore.qreal

		Translates the coordinate system by the given offset ; i.e
		the given offset is added to points.
		"""
		res = super(QPainter,self).translate(*args,**kwargs)
		return res
