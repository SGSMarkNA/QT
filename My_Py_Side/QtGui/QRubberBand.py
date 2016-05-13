from PySide import QtGui, QtCore

class QRubberBand(QtGui.QRubberBand):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRubberBand,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def shape(self):
		"""
		Returns the shape of this rubber band
		The shape can only be set upon construction.
		"""
		res = super(QRubberBand,self).shape()
		isinstance(res,QtGui.QRubberBand.Shape)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionRubberBand

		Initialize option with the values from this PySide.QtGui.QRubberBand
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionRubberBand , but dont want to fill in all the information themselves.
		"""
		res = super(QRubberBand,self).initStyleOption(option)
		return res
