from PySide import QtGui, QtCore

class QRadialGradient(QtGui.QRadialGradient):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRadialGradient,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def center(self):
		"""
		Returns the center of this radial gradient in logical coordinates.
		"""
		res = super(QRadialGradient,self).center()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def focalPoint(self):
		"""
		Returns the focal point of this radial gradient in logical coordinates.
		"""
		res = super(QRadialGradient,self).focalPoint()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def radius(self):
		"""
		Returns the radius of this radial gradient in logical coordinates.
		"""
		res = super(QRadialGradient,self).radius()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setCenter(self,*args,**kwargs):
		"""
		setCenter(center)
			center=QtCore.QPointF

		setCenter(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		Sets the center of this radial gradient in logical coordinates to center .
		"""
		res = super(QRadialGradient,self).setCenter(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setFocalPoint(self,*args,**kwargs):
		"""
		setFocalPoint(focalPoint)
			focalPoint=QtCore.QPointF

		setFocalPoint(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		Sets the focal point of this radial gradient in logical coordinates to focalPoint .
		"""
		res = super(QRadialGradient,self).setFocalPoint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setRadius(self,radius):
		"""
		setRadius(radius)
			radius=QtCore.qreal

		Sets the radius of this radial gradient in logical coordinates to radius
		"""
		res = super(QRadialGradient,self).setRadius(radius)
		return res
