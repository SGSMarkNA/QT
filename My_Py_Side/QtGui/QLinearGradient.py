from PySide import QtGui, QtCore

class QLinearGradient(QtGui.QLinearGradient):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLinearGradient,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def finalStop(self):
		"""
		Returns the final stop point of this linear gradient in logical coordinates.
		"""
		res = super(QLinearGradient,self).finalStop()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def start(self):
		"""
		Returns the start point of this linear gradient in logical coordinates.
		"""
		res = super(QLinearGradient,self).start()
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def setFinalStop(self,*args,**kwargs):
		"""
		setFinalStop(stop)
			stop=QtCore.QPointF

		setFinalStop(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		Sets the final stop point of this linear gradient in logical coordinates to stop .
		"""
		res = super(QLinearGradient,self).setFinalStop(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setStart(self,*args,**kwargs):
		"""
		setStart(x,y)
			x=QtCore.qreal
			y=QtCore.qreal

		setStart(start)
			start=QtCore.QPointF

		This is an overloaded function.
		Sets the start point of this linear gradient in logical coordinates to x , y .
		"""
		res = super(QLinearGradient,self).setStart(*args,**kwargs)
		return res
