from PySide import QtGui, QtCore

class QGraphicsPolygonItem(QtGui.QGraphicsPolygonItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsPolygonItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fillRule(self):
		"""
		Returns the fill rule of the polygon
		The default fill rule is Qt.OddEvenFill .
		"""
		res = super(QGraphicsPolygonItem,self).fillRule()
		isinstance(res,QtCore.Qt.FillRule)
		return res
	#----------------------------------------------------------------------
	def polygon(self):
		"""
		Returns the items polygon, or an empty polygon if no polygon has been set.
		"""
		res = super(QGraphicsPolygonItem,self).polygon()
		isinstance(res,QtGui.QPolygonF)
		return res
	#----------------------------------------------------------------------
	def setFillRule(self,rule):
		"""
		setFillRule(rule)
			rule=QtCore.Qt.FillRule


		"""
		res = super(QGraphicsPolygonItem,self).setFillRule(rule)
		return res
	#----------------------------------------------------------------------
	def setPolygon(self,polygon):
		"""
		setPolygon(polygon)
			polygon=QtGui.QPolygonF

		Sets the items polygon to be the given polygon .
		"""
		res = super(QGraphicsPolygonItem,self).setPolygon(polygon)
		return res
