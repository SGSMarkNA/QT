from PySide import QtGui, QtCore

class QGradient(QtGui.QGradient):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGradient,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def coordinateMode(self):
		"""
		Returns the coordinate mode of this gradient
		The default mode is LogicalMode .
		"""
		res = super(QGradient,self).coordinateMode()
		isinstance(res,QtGui.QGradient.CoordinateMode)
		return res
	#----------------------------------------------------------------------
	def interpolationMode(self):
		"""
		Returns the interpolation mode of this gradient
		The default mode is ColorInterpolation .
		"""
		res = super(QGradient,self).interpolationMode()
		isinstance(res,QtGui.QGradient.InterpolationMode)
		return res
	#----------------------------------------------------------------------
	def spread(self):
		"""
		Returns the spread method use by this gradient
		The default is PadSpread .
		"""
		res = super(QGradient,self).spread()
		isinstance(res,QtGui.QGradient.Spread)
		return res
	#----------------------------------------------------------------------
	def stops(self):
		"""
		Returns the stop points for this gradient.
		If no stop points have been specified, a gradient of black at 0 to white at 1 is used.
		"""
		res = super(QGradient,self).stops()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of gradient.
		"""
		res = super(QGradient,self).type()
		isinstance(res,QtGui.QGradient.Type)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QGradient

		Returns true if the gradient is the same as the other gradient specified; otherwise returns false.
		"""
		res = super(QGradient,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,gradient):
		"""
		__eq__(gradient)
			gradient=QtGui.QGradient

		Returns true if the gradient is the same as the other gradient specified; otherwise returns false.
		"""
		res = super(QGradient,self).__eq__(gradient)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setColorAt(self,pos,color):
		"""
		setColorAt(pos,color)
			pos=QtCore.qreal
			color=QtGui.QColor

		Creates a stop point at the given position with the given color
		The given position must be in the range 0 to 1.
		"""
		res = super(QGradient,self).setColorAt(pos,color)
		return res
	#----------------------------------------------------------------------
	def setCoordinateMode(self,mode):
		"""
		setCoordinateMode(mode)
			mode=QtGui.QGradient.CoordinateMode

		Sets the coordinate mode of this gradient to mode
		The default mode is LogicalMode .
		"""
		res = super(QGradient,self).setCoordinateMode(mode)
		return res
	#----------------------------------------------------------------------
	def setInterpolationMode(self,mode):
		"""
		setInterpolationMode(mode)
			mode=QtGui.QGradient.InterpolationMode

		Sets the interpolation mode of this gradient to mode
		The default mode is ColorInterpolation .
		"""
		res = super(QGradient,self).setInterpolationMode(mode)
		return res
	#----------------------------------------------------------------------
	def setSpread(self,spread):
		"""
		setSpread(spread)
			spread=QtGui.QGradient.Spread

		Specifies the spread method that should be used for this gradient.
		Note that this function only has effect for linear and radial gradients.
		"""
		res = super(QGradient,self).setSpread(spread)
		return res
	#----------------------------------------------------------------------
	def setStops(self,stops):
		"""
		setStops(stops)
			stops=unKnown


		"""
		res = super(QGradient,self).setStops(stops)
		return res
