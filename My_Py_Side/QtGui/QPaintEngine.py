from PySide import QtGui, QtCore

class QPaintEngine(QtGui.QPaintEngine):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPaintEngine,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoDestruct(self):
		"""

		"""
		res = super(QPaintEngine,self).autoDestruct()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def coordinateOffset(self):
		"""
		Returns the offset from the painters origo to the engines origo
		This value is used by PySide.QtGui.QPainter for engines who have internal double buffering.
		This function only makes sense when the engine is active.
		"""
		res = super(QPaintEngine,self).coordinateOffset()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def end(self):
		"""
		Reimplement this function to finish painting on the current paint device
		Return true if painting was finished successfully; otherwise return false.
		"""
		res = super(QPaintEngine,self).end()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if the paint engine is actively drawing; otherwise returns false.
		"""
		res = super(QPaintEngine,self).isActive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isExtended(self):
		"""
		Returns true if the paint engine is a QPaintEngineEx derivative.
		"""
		res = super(QPaintEngine,self).isExtended()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def paintDevice(self):
		"""
		Returns the device that this engine is painting on, if painting is active; otherwise returns 0.
		"""
		res = super(QPaintEngine,self).paintDevice()
		isinstance(res,QtGui.QPaintDevice)
		return res
	#----------------------------------------------------------------------
	def painter(self):
		"""
		Returns the paint engines painter.
		"""
		res = super(QPaintEngine,self).painter()
		isinstance(res,QtGui.QPainter)
		return res
	#----------------------------------------------------------------------
	def syncState(self):
		"""
		Updates all dirty states in this engine
		This function should ONLY be used when drawing with native handles directly and immediate sync from QPainters state to the native state is required.
		"""
		res = super(QPaintEngine,self).syncState()
		return res
	#----------------------------------------------------------------------
	def systemClip(self):
		"""
		Returns the system clip
		The system clip is read only while the painter is active
		An empty region indicates that system clip is not in use.
		"""
		res = super(QPaintEngine,self).systemClip()
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def systemRect(self):
		"""
		Retrieves the rect for drawing within the backing store
		This function should ONLY be used by the backing store.
		"""
		res = super(QPaintEngine,self).systemRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Reimplement this function to return the paint engine QPaintEngine.Type .
		"""
		res = super(QPaintEngine,self).type()
		isinstance(res,QtGui.QPaintEngine.Type)
		return res
	#----------------------------------------------------------------------
	def begin(self,pdev):
		"""
		begin(pdev)
			pdev=QtGui.QPaintDevice

		Reimplement this function to initialise your paint engine when painting is to start on the paint device pdev
		Return true if the initialization was successful; otherwise return false.
		"""
		res = super(QPaintEngine,self).begin(pdev)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def clearDirty(self,df):
		"""
		clearDirty(df)
			df=QtGui.QPaintEngine.DirtyFlags


		"""
		res = super(QPaintEngine,self).clearDirty(df)
		return res
	#----------------------------------------------------------------------
	def drawEllipse(self,*args,**kwargs):
		"""
		drawEllipse(r)
			r=QtCore.QRectF

		drawEllipse(r)
			r=QtCore.QRect

		Reimplement this function to draw the largest ellipse that can be contained within rectangle rect .
		The default implementation calls PySide.QtGui.QPaintEngine.drawPolygon() .
		"""
		res = super(QPaintEngine,self).drawEllipse(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawImage(self,r,pm,sr,flags=None):
		"""
		drawImage(r,pm,sr,flags=None)
			r=QtCore.QRectF
			pm=QtGui.QImage
			sr=QtCore.QRectF
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QPaintEngine,self).drawImage(r,pm,sr,flags)
		return res
	#----------------------------------------------------------------------
	def drawLines(self,*args,**kwargs):
		"""
		drawLines(lines,lineCount)
			lines=QtCore.QLineF
			lineCount=QtCore.int

		drawLines(lines,lineCount)
			lines=QtCore.QLine
			lineCount=QtCore.int

		The default implementation splits the list of lines in lines into lineCount separate calls to PySide.QtGui.QPaintEngine.drawPath() or PySide.QtGui.QPaintEngine.drawPolygon() depending on the feature set of the paint engine.
		"""
		res = super(QPaintEngine,self).drawLines(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPath(self,path):
		"""
		drawPath(path)
			path=QtGui.QPainterPath

		The default implementation ignores the path and does nothing.
		"""
		res = super(QPaintEngine,self).drawPath(path)
		return res
	#----------------------------------------------------------------------
	def drawPixmap(self,r,pm,sr):
		"""
		drawPixmap(r,pm,sr)
			r=QtCore.QRectF
			pm=QtGui.QPixmap
			sr=QtCore.QRectF

		Reimplement this function to draw the part of the pm specified by the sr rectangle in the given r .
		"""
		res = super(QPaintEngine,self).drawPixmap(r,pm,sr)
		return res
	#----------------------------------------------------------------------
	def drawPoints(self,*args,**kwargs):
		"""
		drawPoints(points,pointCount)
			points=QtCore.QPointF
			pointCount=QtCore.int

		drawPoints(points,pointCount)
			points=QtCore.QPoint
			pointCount=QtCore.int

		Draws the first pointCount points in the buffer points
		"""
		res = super(QPaintEngine,self).drawPoints(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawPolygon(self,*args,**kwargs):
		"""
		drawPolygon(points,pointCount,mode)
			points=QtCore.QPointF
			pointCount=QtCore.int
			mode=QtGui.QPaintEngine.PolygonDrawMode

		drawPolygon(points,pointCount,mode)
			points=QtCore.QPoint
			pointCount=QtCore.int
			mode=QtGui.QPaintEngine.PolygonDrawMode

		Reimplement this virtual function to draw the polygon defined by the pointCount first points in points , using mode mode .
		"""
		res = super(QPaintEngine,self).drawPolygon(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawRects(self,*args,**kwargs):
		"""
		drawRects(rects,rectCount)
			rects=QtCore.QRect
			rectCount=QtCore.int

		drawRects(rects,rectCount)
			rects=QtCore.QRectF
			rectCount=QtCore.int

		This is an overloaded function.
		The default implementation converts the first rectCount rectangles in the buffer rects to a PySide.QtCore.QRectF and calls the floating point version of this function.
		"""
		res = super(QPaintEngine,self).drawRects(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def drawTextItem(self,p,textItem):
		"""
		drawTextItem(p,textItem)
			p=QtCore.QPointF
			textItem=QtGui.QTextItem

		This function draws the text item textItem at position p
		The default implementation of this function converts the text to a PySide.QtGui.QPainterPath and paints the resulting path.
		"""
		res = super(QPaintEngine,self).drawTextItem(p,textItem)
		return res
	#----------------------------------------------------------------------
	def drawTiledPixmap(self,r,pixmap,s):
		"""
		drawTiledPixmap(r,pixmap,s)
			r=QtCore.QRectF
			pixmap=QtGui.QPixmap
			s=QtCore.QPointF

		Reimplement this function to draw the pixmap in the given rect , starting at the given p
		The pixmap will be drawn repeatedly until the rect is filled.
		"""
		res = super(QPaintEngine,self).drawTiledPixmap(r,pixmap,s)
		return res
	#----------------------------------------------------------------------
	def hasFeature(self,feature):
		"""
		hasFeature(feature)
			feature=QtGui.QPaintEngine.PaintEngineFeatures


		"""
		res = super(QPaintEngine,self).hasFeature(feature)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setActive(self,newState):
		"""
		setActive(newState)
			newState=QtCore.bool

		Sets the active state of the paint engine to state .
		"""
		res = super(QPaintEngine,self).setActive(newState)
		return res
	#----------------------------------------------------------------------
	def setAutoDestruct(self,autoDestr):
		"""
		setAutoDestruct(autoDestr)
			autoDestr=QtCore.bool


		"""
		res = super(QPaintEngine,self).setAutoDestruct(autoDestr)
		return res
	#----------------------------------------------------------------------
	def setDirty(self,df):
		"""
		setDirty(df)
			df=QtGui.QPaintEngine.DirtyFlags


		"""
		res = super(QPaintEngine,self).setDirty(df)
		return res
	#----------------------------------------------------------------------
	def setSystemClip(self,baseClip):
		"""
		setSystemClip(baseClip)
			baseClip=QtGui.QRegion

		Sets the system clip for this engine
		The system clip defines the basis area that the engine has to draw in
		All clips that are set will be be an intersection with the system clip.
		Reset the systemclip to no clip by setting an empty region.
		"""
		res = super(QPaintEngine,self).setSystemClip(baseClip)
		return res
	#----------------------------------------------------------------------
	def setSystemRect(self,rect):
		"""
		setSystemRect(rect)
			rect=QtCore.QRect

		Sets the target rect for drawing within the backing store
		This function should ONLY be used by the backing store.
		"""
		res = super(QPaintEngine,self).setSystemRect(rect)
		return res
	#----------------------------------------------------------------------
	def testDirty(self,df):
		"""
		testDirty(df)
			df=QtGui.QPaintEngine.DirtyFlags


		"""
		res = super(QPaintEngine,self).testDirty(df)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def updateState(self,state):
		"""
		updateState(state)
			state=QtGui.QPaintEngineState

		Reimplement this function to update the state of a paint engine.
		When implemented, this function is responsible for checking the paint engines current state and update the properties that are changed
		Use the QPaintEngineState.state() function to find out which properties that must be updated, then use the corresponding get function to retrieve the current values for the given properties.
		"""
		res = super(QPaintEngine,self).updateState(state)
		return res
