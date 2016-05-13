from PySide import QtGui, QtCore

class QGraphicsPixmapItem(QtGui.QGraphicsPixmapItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsPixmapItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def offset(self):
		"""
		Returns the pixmap items offset , which defines the point of the top-left corner of the pixmap, in local coordinates.
		"""
		res = super(QGraphicsPixmapItem,self).offset()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		Returns the items pixmap, or an invalid PySide.QtGui.QPixmap if no pixmap has been set.
		"""
		res = super(QGraphicsPixmapItem,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def shapeMode(self):
		"""
		Returns the items shape mode
		The shape mode describes how PySide.QtGui.QGraphicsPixmapItem calculates its shape
		The default mode is MaskShape .
		"""
		res = super(QGraphicsPixmapItem,self).shapeMode()
		isinstance(res,QtGui.QGraphicsPixmapItem.ShapeMode)
		return res
	#----------------------------------------------------------------------
	def transformationMode(self):
		"""
		Returns the transformation mode of the pixmap
		The default mode is Qt.FastTransformation , which provides quick transformation with no smoothing.
		"""
		res = super(QGraphicsPixmapItem,self).transformationMode()
		isinstance(res,QtCore.Qt.TransformationMode)
		return res
	#----------------------------------------------------------------------
	def setOffset(self,*args,**kwargs):
		"""
		setOffset(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		setOffset(offset)
			offset=QtCore.QPointF

		This convenience function is equivalent to calling setOffset( PySide.QtCore.QPointF (x , y )).
		"""
		res = super(QGraphicsPixmapItem,self).setOffset(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,pixmap):
		"""
		setPixmap(pixmap)
			pixmap=QtGui.QPixmap

		Sets the items pixmap to pixmap .
		"""
		res = super(QGraphicsPixmapItem,self).setPixmap(pixmap)
		return res
	#----------------------------------------------------------------------
	def setShapeMode(self,mode):
		"""
		setShapeMode(mode)
			mode=QtGui.QGraphicsPixmapItem.ShapeMode

		Sets the items shape mode to mode
		The shape mode describes how PySide.QtGui.QGraphicsPixmapItem calculates its shape
		The default mode is MaskShape .
		"""
		res = super(QGraphicsPixmapItem,self).setShapeMode(mode)
		return res
	#----------------------------------------------------------------------
	def setTransformationMode(self,mode):
		"""
		setTransformationMode(mode)
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QGraphicsPixmapItem,self).setTransformationMode(mode)
		return res
