from PySide import QtGui, QtCore

class QConicalGradient(QtGui.QConicalGradient):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QConicalGradient,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def angle(self):
		"""
		Returns the start angle of the conical gradient in logical coordinates.
		"""
		res = super(QConicalGradient,self).angle()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def center(self):
		"""
		Returns the center of the conical gradient in logical coordinates.
		"""
		res = super(QConicalGradient,self).center()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setAngle(self,angle):
		"""
		setAngle(angle)
			angle=QtCore.qreal

		Sets angle to be the start angle for this conical gradient in logical coordinates.
		"""
		res = super(QConicalGradient,self).setAngle(angle)
		return res
	#----------------------------------------------------------------------
	def setCenter(self,*args,**kwargs):
		"""
		setCenter(center)
			center=QtCore.QPointF

		setCenter(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		Sets the center of this conical gradient in logical coordinates to center .
		"""
		res = super(QConicalGradient,self).setCenter(*args,**kwargs)
		return res
