from PySide import QtGui, QtCore

class QGraphicsBlurEffect(QtGui.QGraphicsBlurEffect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsBlurEffect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def blurHints(self):
		"""
		This property holds the blur hint of the effect..
		Use the PerformanceHint hint to say that you want a faster blur, the QualityHint hint to say that you prefer a higher quality blur, or the AnimationHint when you want to animate the blur radius.
		By default, the blur hint is PerformanceHint .
		"""
		res = super(QGraphicsBlurEffect,self).blurHints()
		isinstance(res,QtGui.QGraphicsBlurEffect.BlurHints)
		return res
	#----------------------------------------------------------------------
	def blurRadius(self):
		"""
		This property holds the blur radius of the effect..
		Using a smaller radius results in a sharper appearance, whereas a bigger radius results in a more blurred appearance.
		By default, the blur radius is 5 pixels.
		The radius is given in device coordinates, meaning it is unaffected by scale.
		"""
		res = super(QGraphicsBlurEffect,self).blurRadius()
		isinstance(res,QtCore.qreal)
		return res
