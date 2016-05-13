from PySide import QtGui, QtCore

class QPaintEngineState(QtGui.QPaintEngineState):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPaintEngineState,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def backgroundBrush(self):
		"""
		Returns the background brush in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyBackground flag.
		"""
		res = super(QPaintEngineState,self).backgroundBrush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def backgroundMode(self):
		"""
		Returns the background mode in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyBackgroundMode flag.
		"""
		res = super(QPaintEngineState,self).backgroundMode()
		isinstance(res,QtCore.Qt.BGMode)
		return res
	#----------------------------------------------------------------------
	def brush(self):
		"""
		Returns the brush in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyBrush flag.
		"""
		res = super(QPaintEngineState,self).brush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def brushNeedsResolving(self):
		"""
		Returns whether the coordinate of the fill have been specified as bounded by the current rendering operation and have to be resolved (about the currently rendered primitive).
		"""
		res = super(QPaintEngineState,self).brushNeedsResolving()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def brushOrigin(self):
		"""
		Returns the brush origin in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyBrushOrigin flag.
		"""
		res = super(QPaintEngineState,self).brushOrigin()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def clipOperation(self):
		"""
		Returns the clip operation in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes either the QPaintEngine.DirtyClipPath or the QPaintEngine.DirtyClipRegion flag.
		"""
		res = super(QPaintEngineState,self).clipOperation()
		isinstance(res,QtCore.Qt.ClipOperation)
		return res
	#----------------------------------------------------------------------
	def clipPath(self):
		"""
		Returns the clip path in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyClipPath flag.
		"""
		res = super(QPaintEngineState,self).clipPath()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def clipRegion(self):
		"""
		Returns the clip region in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyClipRegion flag.
		"""
		res = super(QPaintEngineState,self).clipRegion()
		isinstance(res,QtGui.QRegion)
		return res
	#----------------------------------------------------------------------
	def compositionMode(self):
		"""
		Returns the composition mode in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyCompositionMode flag.
		"""
		res = super(QPaintEngineState,self).compositionMode()
		isinstance(res,QtGui.QPainter.CompositionMode)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyFont flag.
		"""
		res = super(QPaintEngineState,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def isClipEnabled(self):
		"""
		Returns whether clipping is enabled or not in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyClipEnabled flag.
		"""
		res = super(QPaintEngineState,self).isClipEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def matrix(self):
		"""
		Returns the matrix in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyTransform flag.
		"""
		res = super(QPaintEngineState,self).matrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def opacity(self):
		"""
		Returns the opacity in the current paint engine state.
		"""
		res = super(QPaintEngineState,self).opacity()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def painter(self):
		"""
		Returns a pointer to the painter currently updating the paint engine.
		"""
		res = super(QPaintEngineState,self).painter()
		isinstance(res,QtGui.QPainter)
		return res
	#----------------------------------------------------------------------
	def pen(self):
		"""
		Returns the pen in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyPen flag.
		"""
		res = super(QPaintEngineState,self).pen()
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def penNeedsResolving(self):
		"""
		Returns whether the coordinate of the stroke have been specified as bounded by the current rendering operation and have to be resolved (about the currently rendered primitive).
		"""
		res = super(QPaintEngineState,self).penNeedsResolving()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def renderHints(self):
		"""
		Returns the render hints in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyHints flag.
		"""
		res = super(QPaintEngineState,self).renderHints()
		isinstance(res,QtGui.QPainter.RenderHints)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns a combination of flags identifying the set of properties that need to be updated when updating the paint engines state (i.e
		during a call to the QPaintEngine.updateState() function).
		"""
		res = super(QPaintEngineState,self).state()
		isinstance(res,QtGui.QPaintEngine.DirtyFlags)
		return res
	#----------------------------------------------------------------------
	def transform(self):
		"""
		Returns the matrix in the current paint engine state.
		This variable should only be used when the PySide.QtGui.QPaintEngineState.state() returns a combination which includes the QPaintEngine.DirtyTransform flag.
		"""
		res = super(QPaintEngineState,self).transform()
		isinstance(res,QtGui.QTransform)
		return res
