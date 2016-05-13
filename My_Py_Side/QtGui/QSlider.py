from PySide import QtGui, QtCore

class QSlider(QtGui.QSlider):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSlider,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def tickInterval(self):
		"""
		This property holds the interval between tickmarks.
		This is a value interval, not a pixel interval
		If it is 0, the slider will choose between PySide.QtGui.QAbstractSlider.singleStep() and PySide.QtGui.QAbstractSlider.pageStep() .
		The default value is 0.
		"""
		res = super(QSlider,self).tickInterval()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def tickPosition(self):
		"""
		This property holds the tickmark position for this slider.
		The valid values are described by the QSlider.TickPosition enum.
		The default value is QSlider.NoTicks .
		"""
		res = super(QSlider,self).tickPosition()
		isinstance(res,QtGui.QSlider.TickPosition)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionSlider

		Initialize option with the values from this PySide.QtGui.QSlider
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionSlider , but dont want to fill in all the information themselves.
		"""
		res = super(QSlider,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setTickInterval(self,ti):
		"""
		setTickInterval(ti)
			ti=QtCore.int

		This property holds the interval between tickmarks.
		This is a value interval, not a pixel interval
		If it is 0, the slider will choose between PySide.QtGui.QAbstractSlider.singleStep() and PySide.QtGui.QAbstractSlider.pageStep() .
		The default value is 0.
		"""
		res = super(QSlider,self).setTickInterval(ti)
		return res
	#----------------------------------------------------------------------
	def setTickPosition(self,position):
		"""
		setTickPosition(position)
			position=QtGui.QSlider.TickPosition

		This property holds the tickmark position for this slider.
		The valid values are described by the QSlider.TickPosition enum.
		The default value is QSlider.NoTicks .
		"""
		res = super(QSlider,self).setTickPosition(position)
		return res
