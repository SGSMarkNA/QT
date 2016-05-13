from PySide import QtGui, QtCore

class QGraphicsScale(QtGui.QGraphicsScale):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsScale,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def origin(self):
		"""
		This property holds the origin of the scale in 3D space..
		All scaling will be done relative to this point (i.e., this point will stay fixed, relative to the parent, when the item is scaled).
		"""
		res = super(QGraphicsScale,self).origin()
		isinstance(res,QtGui.QVector3D)
		return res
	#----------------------------------------------------------------------
	def originChanged(self):
		"""

		"""
		res = super(QGraphicsScale,self).originChanged()
		return res
	#----------------------------------------------------------------------
	def scaleChanged(self):
		"""

		"""
		res = super(QGraphicsScale,self).scaleChanged()
		return res
	#----------------------------------------------------------------------
	def xScale(self):
		"""
		This property holds the horizontal scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be mirrored horizontally around its origin.
		"""
		res = super(QGraphicsScale,self).xScale()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def xScaleChanged(self):
		"""

		"""
		res = super(QGraphicsScale,self).xScaleChanged()
		return res
	#----------------------------------------------------------------------
	def yScale(self):
		"""
		This property holds the vertical scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be flipped vertically around its origin.
		"""
		res = super(QGraphicsScale,self).yScale()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def yScaleChanged(self):
		"""

		"""
		res = super(QGraphicsScale,self).yScaleChanged()
		return res
	#----------------------------------------------------------------------
	def zScale(self):
		"""
		This property holds the depth scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be flipped end for end around its origin.
		"""
		res = super(QGraphicsScale,self).zScale()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def zScaleChanged(self):
		"""

		"""
		res = super(QGraphicsScale,self).zScaleChanged()
		return res
	#----------------------------------------------------------------------
	def setOrigin(self,point):
		"""
		setOrigin(point)
			point=QtGui.QVector3D

		This property holds the origin of the scale in 3D space..
		All scaling will be done relative to this point (i.e., this point will stay fixed, relative to the parent, when the item is scaled).
		"""
		res = super(QGraphicsScale,self).setOrigin(point)
		return res
	#----------------------------------------------------------------------
	def setXScale(self,arg__1):
		"""
		setXScale(arg__1)
			arg__1=QtCore.qreal

		This property holds the horizontal scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be mirrored horizontally around its origin.
		"""
		res = super(QGraphicsScale,self).setXScale(arg__1)
		return res
	#----------------------------------------------------------------------
	def setYScale(self,arg__1):
		"""
		setYScale(arg__1)
			arg__1=QtCore.qreal

		This property holds the vertical scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be flipped vertically around its origin.
		"""
		res = super(QGraphicsScale,self).setYScale(arg__1)
		return res
	#----------------------------------------------------------------------
	def setZScale(self,arg__1):
		"""
		setZScale(arg__1)
			arg__1=QtCore.qreal

		This property holds the depth scale factor..
		The scale factor can be any real number; the default value is 1.0
		If you set the factor to 0.0, the item will be collapsed to a single point
		If you provide a negative value, the item will be flipped end for end around its origin.
		"""
		res = super(QGraphicsScale,self).setZScale(arg__1)
		return res
