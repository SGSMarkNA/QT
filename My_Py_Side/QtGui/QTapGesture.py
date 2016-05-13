from PySide import QtGui, QtCore

class QTapGesture(QtGui.QTapGesture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTapGesture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def position(self):
		"""
		This property holds the position of the tap.
		"""
		res = super(QTapGesture,self).position()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,pos):
		"""
		setPosition(pos)
			pos=QtCore.QPointF

		This property holds the position of the tap.
		"""
		res = super(QTapGesture,self).setPosition(pos)
		return res
