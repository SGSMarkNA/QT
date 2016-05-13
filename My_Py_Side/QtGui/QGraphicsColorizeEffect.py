from PySide import QtGui, QtCore

class QGraphicsColorizeEffect(QtGui.QGraphicsColorizeEffect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsColorizeEffect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def color(self):
		"""
		This property holds the color of the effect..
		By default, the color is light blue ( PySide.QtGui.QColor (0, 0, 192)).
		"""
		res = super(QGraphicsColorizeEffect,self).color()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def strength(self):
		"""
		This property holds the strength of the effect..
		By default, the strength is 1.0
		A strength 0.0 equals to no effect, while 1.0 means full colorization.
		"""
		res = super(QGraphicsColorizeEffect,self).strength()
		isinstance(res,QtCore.qreal)
		return res
