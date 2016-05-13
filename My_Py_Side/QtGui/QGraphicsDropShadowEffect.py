from PySide import QtGui, QtCore

class QGraphicsDropShadowEffect(QtGui.QGraphicsDropShadowEffect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsDropShadowEffect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def blurRadius(self):
		"""
		This property holds the blur radius in pixels of the drop shadow..
		Using a smaller radius results in a sharper shadow, whereas using a bigger radius results in a more blurred shadow.
		By default, the blur radius is 1 pixel.
		"""
		res = super(QGraphicsDropShadowEffect,self).blurRadius()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def color(self):
		"""
		This property holds the color of the drop shadow..
		By default, the drop color is a semi-transparent dark gray ( PySide.QtGui.QColor (63, 63, 63, 180)).
		"""
		res = super(QGraphicsDropShadowEffect,self).color()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def offset(self):
		"""
		This property holds the shadow offset in pixels..
		By default, the offset is 8 pixels towards the lower right.
		The offset is given in device coordinates, which means it is unaffected by scale.
		"""
		res = super(QGraphicsDropShadowEffect,self).offset()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def xOffset(self):
		"""
		This property holds the horizontal shadow offset in pixels..
		By default, the horizontal shadow offset is 8 pixels.
		"""
		res = super(QGraphicsDropShadowEffect,self).xOffset()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def yOffset(self):
		"""
		This property holds the vertical shadow offset in pixels..
		By default, the vertical shadow offset is 8 pixels.
		"""
		res = super(QGraphicsDropShadowEffect,self).yOffset()
		isinstance(res,QtCore.qreal)
		return res
