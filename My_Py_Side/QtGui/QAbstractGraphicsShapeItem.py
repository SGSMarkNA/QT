
from PySide import QtGui, QtCore
from QGraphicsItem import QGraphicsItem
class QAbstractGraphicsShapeItem(QtGui.QAbstractGraphicsShapeItem, QGraphicsItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractGraphicsShapeItem,self).__init__(*args,**kwargs)
		if False:
			isinstance(self,QGraphicsItem)
			isinstance(self.Brush, QtGui.QBrush)
			isinstance(self.Pen, QtGui.QPen)
			#isinstance(self.Bounding_Rect, QtCore.QRectF)
			#isinstance(self.Pos, QtCore.QPointF)
			#isinstance(self.Opaque_Area, QtGui.QPainterPath)
			#isinstance(self.Panel, QtGui.QGraphicsItem)
			#isinstance(self.Parent_Item, QtGui.QGraphicsItem)
			#isinstance(self.Parent_Widget, QtGui.QGraphicsWidget)
			#isinstance(self.Scene, QtGui.QGraphicsScene)
			#isinstance(self.Scene_Bounding_Rect, QtCore.QRectF)
			#isinstance(self.Scene_Pos, QtCore.QPointF)
			#isinstance(self.Scene_Transform, QtGui.QTransform)
			#isinstance(self.Shape, QtGui.QPainterPath)
			#isinstance(self.Top_Level_Item, QtGui.QGraphicsItem)
			#isinstance(self.Top_Level_Widget, QtGui.QGraphicsWidget)
			#isinstance(self.Tranform_Matrix, QtGui.QTransform)
			#isinstance(self.Transform_Origin_Point, QtCore.QPointF)
			#isinstance(self.Transformations, list)

	#----------------------------------------------------------------------
	def brush(self):
		"""
		Returns the items brush, or an empty brush if no brush has been set.
		"""
		res = super(QAbstractGraphicsShapeItem,self).brush()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def pen(self):
		"""
		Returns the items pen
		If no pen has been set, this function returns QPen(), a default black solid line pen with 0 width.
		"""
		res = super(QAbstractGraphicsShapeItem,self).pen()
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def setBrush(self,brush):
		"""
		setBrush(brush)
			brush=QtGui.QBrush

		Sets the items brush to brush .
		The items brush is used to fill the item.
		If you use a brush with a PySide.QtGui.QGradient , the gradient is relative to the items coordinate system.
		"""
		res = super(QAbstractGraphicsShapeItem,self).setBrush(brush)
		return res
	#----------------------------------------------------------------------
	def setPen(self,pen):
		"""
		setPen(pen)
			pen=QtGui.QPen

		Sets the pen for this item to pen .
		The pen is used to draw the items outline.
		"""
		res = super(QAbstractGraphicsShapeItem,self).setPen(pen)
		return res
	Brush                  = property(brush,setBrush)
	Pen                    = property(pen,setPen)

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	item = QAbstractGraphicsShapeItem()

	#Node_Graph_Window.show()
	sys.exit(app.exec_())