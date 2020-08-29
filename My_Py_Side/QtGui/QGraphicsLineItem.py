from PySide import QtGui, QtCore
from QGraphicsItem import QGraphicsItem
class QGraphicsLineItem(QtGui.QGraphicsLineItem, QGraphicsItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsLineItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def line(self):
		"""
		Returns the items line, or a null line if no line has been set.
		"""
		res = super(QGraphicsLineItem,self).line()
		isinstance(res,QtCore.QLineF)
		return res
	#----------------------------------------------------------------------
	def pen(self):
		"""
		Returns the items pen, or a black solid 0-width pen if no pen has been set.
		"""
		res = super(QGraphicsLineItem,self).pen()
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def setLine(self,*args,**kwargs):
		"""
		setLine(x1,y1,x2,y2)
			x1=QtCore.qreal
			y1=QtCore.qreal
			x2=QtCore.qreal
			y2=QtCore.qreal

		setLine(line)
			line=QtCore.QLineF

		This is an overloaded function.
		Sets the items line to be the line between (x1 , y1 ) and (x2 , y2 ).
		This is the same as calling setLine(QLineF(x1, y1, x2, y2)) .
		"""
		res = super(QGraphicsLineItem,self).setLine(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPen(self,pen):
		"""
		setPen(pen)
			pen=QtGui.QPen

		Sets the items pen to pen
		If no pen is set, the line will be painted using a black solid 0-width pen.
		"""
		res = super(QGraphicsLineItem,self).setPen(pen)
		return res

	Line = property(line, setLine)
	Pen  = property(pen, setPen)