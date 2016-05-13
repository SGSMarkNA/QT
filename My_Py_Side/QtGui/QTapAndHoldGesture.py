from PySide import QtGui, QtCore

class QTapAndHoldGesture(QtGui.QTapAndHoldGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTapAndHoldGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def position(self):
		"""
		This property holds the position of the tap.
		"""
		res = super(QTapAndHoldGesture,self).position()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,pos):
		"""
		setPosition(pos)
			pos=QtCore.QPointF

		This property holds the position of the tap.
		"""
		res = super(QTapAndHoldGesture,self).setPosition(pos)
		return res
