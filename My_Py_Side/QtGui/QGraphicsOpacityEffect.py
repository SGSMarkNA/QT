from PySide import QtGui, QtCore

class QGraphicsOpacityEffect(QtGui.QGraphicsOpacityEffect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsOpacityEffect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def opacity(self):
		"""
		This property holds the opacity of the effect..
		The value should be in the range of 0.0 to 1.0, where 0.0 is fully transparent and 1.0 is fully opaque.
		By default, the opacity is 0.7.
		"""
		res = super(QGraphicsOpacityEffect,self).opacity()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def opacityMask(self):
		"""
		This property holds the opacity mask of the effect..
		An opacity mask allows you apply opacity to portions of an element.
		For example:
		There is no opacity mask by default.
		"""
		res = super(QGraphicsOpacityEffect,self).opacityMask()
		isinstance(res,QtGui.QBrush)
		return res
