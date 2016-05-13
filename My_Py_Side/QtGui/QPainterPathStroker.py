from PySide import QtGui, QtCore

class QPainterPathStroker(QtGui.QPainterPathStroker):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPainterPathStroker,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def capStyle(self):
		"""
		Returns the cap style of the generated outlines.
		"""
		res = super(QPainterPathStroker,self).capStyle()
		isinstance(res,QtCore.Qt.PenCapStyle)
		return res
	#----------------------------------------------------------------------
	def curveThreshold(self):
		"""
		Returns the curve flattening threshold for the generated outlines.
		"""
		res = super(QPainterPathStroker,self).curveThreshold()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dashOffset(self):
		"""
		Returns the dash offset for the generated outlines.
		"""
		res = super(QPainterPathStroker,self).dashOffset()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def dashPattern(self):
		"""
		Returns the dash pattern for the generated outlines.
		"""
		res = super(QPainterPathStroker,self).dashPattern()
		return res
	#----------------------------------------------------------------------
	def joinStyle(self):
		"""
		Returns the join style of the generated outlines.
		"""
		res = super(QPainterPathStroker,self).joinStyle()
		isinstance(res,QtCore.Qt.PenJoinStyle)
		return res
	#----------------------------------------------------------------------
	def miterLimit(self):
		"""
		Returns the miter limit for the generated outlines.
		"""
		res = super(QPainterPathStroker,self).miterLimit()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Returns the width of the generated outlines.
		"""
		res = super(QPainterPathStroker,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def createStroke(self,path):
		"""
		createStroke(path)
			path=QtGui.QPainterPath

		Generates a new path that is a fillable area representing the outline of the given path .
		The various design aspects of the outline are based on the strokers properties: PySide.QtGui.QPainterPathStroker.width() , PySide.QtGui.QPainterPathStroker.capStyle() , PySide.QtGui.QPainterPathStroker.joinStyle() , PySide.QtGui.QPainterPathStroker.dashPattern() , PySide.QtGui.QPainterPathStroker.curveThreshold() and PySide.QtGui.QPainterPathStroker.miterLimit() .
		The generated path should only be used for outlining the given painter path
		Otherwise it may cause unexpected behavior
		Generated outlines also require the Qt.WindingFill rule which is set by default.
		"""
		res = super(QPainterPathStroker,self).createStroke(path)
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def setCapStyle(self,style):
		"""
		setCapStyle(style)
			style=QtCore.Qt.PenCapStyle


		"""
		res = super(QPainterPathStroker,self).setCapStyle(style)
		return res
	#----------------------------------------------------------------------
	def setCurveThreshold(self,threshold):
		"""
		setCurveThreshold(threshold)
			threshold=QtCore.qreal

		Specifies the curve flattening threshold , controlling the granularity with which the generated outlines curve is drawn.
		The default threshold is a well adjusted value (0.25), and normally you should not need to modify it
		However, you can make the curves appearance smoother by decreasing its value.
		"""
		res = super(QPainterPathStroker,self).setCurveThreshold(threshold)
		return res
	#----------------------------------------------------------------------
	def setDashOffset(self,offset):
		"""
		setDashOffset(offset)
			offset=QtCore.qreal

		Sets the dash offset for the generated outlines to offset .
		See the documentation for QPen.setDashOffset() for a description of the dash offset.
		"""
		res = super(QPainterPathStroker,self).setDashOffset(offset)
		return res
	#----------------------------------------------------------------------
	def setDashPattern(self,*args,**kwargs):
		"""
		setDashPattern(dashPattern)
			dashPattern=unKnown

		setDashPattern(arg__1)
			arg__1=QtCore.Qt.PenStyle


		"""
		res = super(QPainterPathStroker,self).setDashPattern(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setJoinStyle(self,style):
		"""
		setJoinStyle(style)
			style=QtCore.Qt.PenJoinStyle


		"""
		res = super(QPainterPathStroker,self).setJoinStyle(style)
		return res
	#----------------------------------------------------------------------
	def setMiterLimit(self,length):
		"""
		setMiterLimit(length)
			length=QtCore.qreal

		Sets the miter limit of the generated outlines to limit .
		The miter limit describes how far from each join the miter join can extend
		The limit is specified in units of the currently set width
		So the pixelwise miter limit will be miterlimit * width .
		This value is only used if the join style is Qt.MiterJoin .
		"""
		res = super(QPainterPathStroker,self).setMiterLimit(length)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,width):
		"""
		setWidth(width)
			width=QtCore.qreal

		Sets the width of the generated outline painter path to width .
		The generated outlines will extend approximately 50% of width to each side of the given input paths original outline.
		"""
		res = super(QPainterPathStroker,self).setWidth(width)
		return res
