import Qt_Tools
QtCore = Qt_Tools.QtCore
QtGui  = Qt_Tools.QtGui
Qt     = Qt_Tools.Qt
from QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem
class QGraphicsRectItem(QtGui.QGraphicsRectItem, QAbstractGraphicsShapeItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsRectItem,self).__init__(*args,**kwargs)
		if False:
			isinstance(self.Rect, QtCore.QRectF)
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the items rectangle.
		"""
		res = super(QGraphicsRectItem,self).rect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def setRect(self,*args,**kwargs):
		"""
		setRect(rect)
			rect=QtCore.QRectF

		setRect(x,y,w,h)
			x=QtCore.qreal
			y=QtCore.qreal
			w=QtCore.qreal
			h=QtCore.qreal

		Sets the items rectangle to be the given rectangle .
		"""
		res = super(QGraphicsRectItem,self).setRect(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	Rect = property(rect,setRect)